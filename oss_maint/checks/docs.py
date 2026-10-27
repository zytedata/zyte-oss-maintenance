from __future__ import annotations

import re
from functools import cache
from pathlib import PurePath
from urllib.parse import urlsplit

from oss_maint import github, pythons
from oss_maint.core import Group, Repo, Result, failed, not_applicable, passed

group = Group("docs", "Documentation")

SPHINX_SCRAPY_PYPI_URL = "https://pypi.org/pypi/sphinx-scrapy/json"
SPHINX_SCRAPY_REPO_RE = re.compile(r"github\.com/scrapy/sphinx-scrapy(?:\.git)?/?$")
# "sphinx-scrapy[tox]==0.13.0" or
# "sphinx-scrapy @ git+https://github.com/scrapy/sphinx-scrapy.git@0.8.4".
# The version is in the first or second group.
SPHINX_SCRAPY_PIN_RE = re.compile(
    r"\bsphinx-scrapy(?:\[[^\]]*\])?\s*"
    r"(?:==\s*([\w.]+)|@\s*git\+https://github\.com/scrapy/sphinx-scrapy(?:\.git)?@([\w.]+))"
)


@cache
def latest_sphinx_scrapy() -> str:
    return pythons._get_json(SPHINX_SCRAPY_PYPI_URL)["info"]["version"]


@group.fact("Latest sphinx-scrapy")
def latest_sphinx_scrapy_version() -> str:
    return latest_sphinx_scrapy()


def _uses_sphinx_scrapy(repo: Repo) -> bool:
    return "sphinx_scrapy" in (repo.read_text("docs/conf.py") or "")


def _pin(texts: list[str]) -> str | None:
    for text in texts:
        if m := SPHINX_SCRAPY_PIN_RE.search(text):
            return m.group(1) or m.group(2)
    return None


def _sphinx_scrapy_pins(repo: Repo) -> dict[str, str | None]:
    """sphinx-scrapy versions by where they are pinned, None if not pinned
    there."""
    rev = None
    config = repo.read_yaml(".pre-commit-config.yaml") or {}
    for pre_commit_repo in config.get("repos") or []:
        if SPHINX_SCRAPY_REPO_RE.search(pre_commit_repo.get("repo", "")):
            rev = str(pre_commit_repo.get("rev"))
    return {
        "tox": _pin(repo.tox_strings),
        ".pre-commit-config.yaml": rev,
    }


@group.check(
    "The documentation is a Sphinx project in docs/, written in reStructuredText.",
    tags={"python", "released"},
)
def sphinx_docs(repo: Repo) -> Result:
    problems = []
    if not repo.has_sphinx_docs:
        problems.append("no docs/conf.py")
    if markdown := repo.glob("docs/**/*.md"):
        problems.append(f"Markdown files: {', '.join(markdown)}")
    return failed("; ".join(problems)) if problems else passed()


def _readmes(repo: Repo) -> list[str]:
    return [path for path in repo.glob("*") if path.lower().startswith("readme")]


@group.check("The README is in reStructuredText, as README.rst.")
def readme_rst(repo: Repo) -> Result:
    readmes = _readmes(repo)
    if "README.rst" in readmes:
        return passed()
    return failed(f"{', '.join(readmes)} instead" if readmes else "no README")


@group.check("The GitHub wiki has no pages.")
def no_wiki(repo: Repo) -> Result:
    if github.has_wiki(repo.name):
        return failed(f"{repo.url}/wiki has pages")
    return passed()


@group.check(
    "Sphinx docs requirements other than sphinx-scrapy are in a docs dependency "
    "group, not in docs/requirements.in or docs/requirements.txt."
)
def no_docs_requirements(repo: Repo) -> Result:
    if not repo.has_sphinx_docs:
        return not_applicable("No Sphinx docs.")
    if files := [
        path
        for path in ("docs/requirements.in", "docs/requirements.txt")
        if repo.exists(path)
    ]:
        return failed(f"found {', '.join(files)}")
    return passed()


@group.check("Sphinx docs use sphinx-scrapy.")
def sphinx_scrapy(repo: Repo) -> Result:
    if not repo.has_sphinx_docs:
        return not_applicable("No Sphinx docs.")
    if not _uses_sphinx_scrapy(repo):
        return failed("sphinx_scrapy not in docs/conf.py")
    return passed()


@group.check(
    "sphinx-scrapy is pinned to the same version in the tox requires and the "
    "pre-commit hook rev."
)
def sphinx_scrapy_pins(repo: Repo) -> Result:
    if not repo.has_sphinx_docs or not _uses_sphinx_scrapy(repo):
        return not_applicable("Does not use sphinx-scrapy.")
    pins = _sphinx_scrapy_pins(repo)
    problems = []
    if missing := [where for where, version in pins.items() if version is None]:
        problems.append(f"not pinned in {', '.join(missing)}")
    if len({v for v in pins.values() if v is not None}) > 1:
        problems.append(
            "different pins: "
            + ", ".join(f"{v} in {where}" for where, v in pins.items() if v)
        )
    return failed("; ".join(problems)) if problems else passed()


@group.check("sphinx-scrapy is pinned to its latest release.")
def sphinx_scrapy_latest(repo: Repo) -> Result:
    if not repo.has_sphinx_docs or not _uses_sphinx_scrapy(repo):
        return not_applicable("Does not use sphinx-scrapy.")
    pins = {v for v in _sphinx_scrapy_pins(repo).values() if v}
    if not pins:
        return failed("not pinned")
    latest = latest_sphinx_scrapy()
    if outdated := sorted(pins - {latest}):
        return failed(f"pinned to {', '.join(outdated)}, latest is {latest}")
    return passed()


@group.check(
    "Sphinx docs are built on Read the Docs (.readthedocs.yml), and the README "
    "links to them."
)
def readthedocs(repo: Repo) -> Result:
    if not repo.has_sphinx_docs:
        return not_applicable("No Sphinx docs.")
    problems = []
    if not repo.exists(".readthedocs.yml") and not repo.exists(".readthedocs.yaml"):
        problems.append("no .readthedocs.yml")
    hosts = _docs_hosts(repo)
    readme = "".join(repo.read_text(path) or "" for path in _readmes(repo))
    if not any(f"//{host}" in readme for host in hosts):
        problems.append(f"the README does not link to {' or '.join(sorted(hosts))}")
    return failed("; ".join(problems)) if problems else passed()


def _docs_hosts(repo: Repo) -> set[str]:
    """Hosts of the published docs: on Read the Docs under the repository
    name, or of a documentation URL in [project.urls]."""
    name = repo.name.split("/")[1]
    hosts = {f"{name}.readthedocs.io", f"{name}.readthedocs.org"}
    hosts.update(
        urlsplit(url).netloc
        for key, url in (repo.project.get("urls") or {}).items()
        if key.lower().startswith("doc")
    )
    return hosts


@group.check(
    "Links to the docs in the README and in [project.urls] that name a version "
    "use stable, which is built from the latest release.",
    tags={"released"},
)
def docs_stable_links(repo: Repo) -> Result:
    if not repo.has_sphinx_docs:
        return not_applicable("No Sphinx docs.")
    # Read the Docs URLs have the language and the version first, e.g. /en/latest/.
    version_re = re.compile(
        rf"//(?:{'|'.join(map(re.escape, _docs_hosts(repo)))})"
        r"/[a-z]{2}(?:-[a-z]+)?/([\w.-]+)"
    )
    texts = {path: repo.read_text(path) or "" for path in _readmes(repo)}
    texts["pyproject.toml"] = " ".join(
        map(str, (repo.project.get("urls") or {}).values())
    )
    if problems := [
        f"{', '.join(versions)} in {path}"
        for path, text in texts.items()
        if (versions := sorted(set(version_re.findall(text)) - {"stable"}))
    ]:
        return failed(f"links to {'; '.join(problems)}")
    return passed()


CHANGELOG_RE = re.compile(
    r"(changes|changelog|news|history|release-notes)(\.\w+)?", re.IGNORECASE
)


@group.check(
    "There is a changelog, e.g. CHANGES.rst, CHANGELOG.md, NEWS or docs/news.rst.",
    tags={"released"},
)
def changelog(repo: Repo) -> Result:
    if any(
        CHANGELOG_RE.fullmatch(PurePath(path).name)
        for path in [*repo.glob("*"), *repo.glob("docs/*")]
    ):
        return passed()
    return failed("no changelog file")


@group.check(
    "bump-my-version replaces (unreleased) in the changelog with the release date.",
    tags={"released"},
)
def changelog_date(repo: Repo) -> Result:
    config = (repo.pyproject or {}).get("tool", {}).get("bumpversion") or (
        repo.read_toml(".bumpversion.toml") or {}
    ).get("tool", {}).get("bumpversion")
    if config is None:
        return not_applicable("Does not use bump-my-version.")
    if any(
        "unreleased" in str(file.get("search", "")).lower()
        and "{now:" in str(file.get("replace", ""))
        for file in config.get("files") or []
    ):
        return passed()
    return failed("no file replacement of (unreleased) with {now:%Y-%m-%d}")
