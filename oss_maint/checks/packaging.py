from __future__ import annotations

import configparser
import re

from packaging.licenses import InvalidLicenseExpression, canonicalize_license_expression

from oss_maint.core import Group, Repo, Result, failed, not_applicable, passed

group = Group("packaging", "Packaging")

NO_PROJECT_TABLE = "No [project] table in pyproject.toml."
# Prefixes of setup.cfg sections with setuptools configuration, as opposed to
# configuration of other tools, e.g. [flake8].
SETUPTOOLS_SECTION_PREFIXES = (
    "aliases",
    "bdist",
    "build",
    "easy_install",
    "egg_info",
    "install",
    "metadata",
    "options",
    "register",
    "sdist",
    "upload",
    "wheel",
)


@group.check(
    "Package metadata is in the [project] table of pyproject.toml, with no "
    "setup.py and no setuptools configuration in setup.cfg."
)
def pyproject_metadata(repo: Repo) -> Result:
    problems = []
    if not repo.project:
        problems.append("no [project] table in pyproject.toml")
    if repo.exists("setup.py"):
        problems.append("setup.py exists")
    setup_cfg = configparser.ConfigParser(interpolation=None)
    setup_cfg.read_string(repo.read_text("setup.cfg") or "")
    if sections := [
        f"[{s}]"
        for s in setup_cfg.sections()
        if s.startswith(SETUPTOOLS_SECTION_PREFIXES)
    ]:
        problems.append(f"setup.cfg has setuptools sections: {', '.join(sections)}")
    return failed("; ".join(problems)) if problems else passed()


@group.info(
    "The license: the license field of package metadata, or else the license "
    "classifiers."
)
def license_(repo: Repo) -> str | None:
    if isinstance(value := repo.project.get("license"), str):
        return value
    if classifiers := [
        c.removeprefix("License :: ").removeprefix("OSI Approved :: ")
        for c in repo.classifiers
        if c.startswith("License ::")
    ]:
        return ", ".join(classifiers)
    if isinstance(value, dict) and "text" in value:
        return value["text"]
    if m := re.search(
        r"license\s*=\s*[\"']([^\"']+)", repo.read_text("setup.py") or ""
    ):
        return m.group(1)
    return None


@group.check(
    "The license is declared as an SPDX expression (PEP 639), without license "
    "classifiers."
)
def pep639_license(repo: Repo) -> Result:
    if not repo.project:
        return not_applicable(NO_PROJECT_TABLE)
    problems = []
    value = repo.project.get("license")
    if value is None:
        if "license" not in repo.project.get("dynamic", []):
            problems.append("no license field")
    elif not isinstance(value, str):
        problems.append("license is a table, not an SPDX expression")
    else:
        try:
            canonicalize_license_expression(value)
        except InvalidLicenseExpression:
            problems.append(f"license {value!r} is not a valid SPDX expression")
    if classifiers := [c for c in repo.classifiers if c.startswith("License ::")]:
        problems.append(f"has license classifiers: {', '.join(classifiers)}")
    return failed("; ".join(problems)) if problems else passed()


@group.check("The build backend is hatchling.")
def hatchling(repo: Repo) -> Result:
    if repo.pyproject is None:
        return failed("no pyproject.toml")
    backend = repo.pyproject.get("build-system", {}).get("build-backend")
    if backend is None:
        return failed("no build-backend in pyproject.toml")
    if backend != "hatchling.build":
        return failed(f"build backend is {backend}")
    return passed()


@group.check("Project URLs are declared in [project.urls].")
def project_urls(repo: Repo) -> Result:
    if not repo.project:
        return not_applicable(NO_PROJECT_TABLE)
    if not repo.project.get("urls") and "urls" not in repo.project.get("dynamic", []):
        return failed("no [project.urls] table")
    return passed()


@group.check("`twine check` validates the built distributions in tox.")
def twine_check(repo: Repo) -> Result:
    if any("twine check" in s for s in repo.tox_strings):
        return passed()
    if any("twine check" in s for s in repo.workflow_strings):
        return failed("twine check runs in a workflow, not in tox")
    return failed("no twine check in tox config")
