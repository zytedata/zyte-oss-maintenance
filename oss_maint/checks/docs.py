from __future__ import annotations

import re
from functools import cache

from oss_maint import pythons
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
    return "sphinx_scrapy" in (
        repo.read_text("docs/conf.py") or ""
    ) or "sphinx-scrapy" in (repo.read_text("docs/requirements.in") or "")


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
        "docs/requirements.in": _pin([repo.read_text("docs/requirements.in") or ""]),
        ".pre-commit-config.yaml": rev,
    }


@group.check("Sphinx docs requirements are defined in docs/requirements.in.")
def docs_requirements_in(repo: Repo) -> Result:
    if not repo.has_sphinx_docs:
        return not_applicable("No Sphinx docs.")
    if not repo.exists("docs/requirements.in"):
        return failed("no docs/requirements.in")
    return passed()


@group.check("Sphinx docs use sphinx-scrapy.")
def sphinx_scrapy(repo: Repo) -> Result:
    if not repo.has_sphinx_docs:
        return not_applicable("No Sphinx docs.")
    if not _uses_sphinx_scrapy(repo):
        return failed("sphinx_scrapy not in docs/conf.py or docs/requirements.in")
    return passed()


@group.check(
    "sphinx-scrapy is pinned to the same version in the tox requires, the docs "
    "requirements and the pre-commit hook rev."
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
