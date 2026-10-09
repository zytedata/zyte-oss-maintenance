from __future__ import annotations

from packaging.version import Version

from oss_maint import pythons
from oss_maint.core import (
    PYPY_CLASSIFIER,
    Group,
    Repo,
    Result,
    failed,
    not_applicable,
    passed,
)

group = Group("python", "Python versions")


@group.fact("Latest Python")
def latest_python_version() -> str:
    return pythons.latest_python().version


@group.fact("Upcoming Python, with a release candidate")
def upcoming_python_version() -> str:
    return pythons.upcoming_python() or "none"


@group.fact("Supported Python versions, with EOL dates")
def supported_python_versions() -> str:
    return ", ".join(
        f"{c.version} ({c.eol_date or 'unknown'})"
        for c in pythons.python_cycles()
        if c.released and not c.eol
    )


@group.fact("Python versions of the latest PyPy release")
def pypy_python_versions() -> str:
    return ", ".join(pythons.pypy_versions().supported)


@group.fact("End-of-life PyPy Python versions")
def eol_pypy_python_versions() -> str:
    return ", ".join(pythons.pypy_versions().eol) or "none"


@group.check("Support for end-of-life Python versions is dropped.")
def no_eol_python(repo: Repo) -> Result:
    requires_python = repo.requires_python
    if requires_python is None:
        return failed("requires-python is not declared")
    supported = [
        c for c in pythons.python_cycles() if pythons.allows(requires_python, c.version)
    ]
    if not supported:
        return failed(f"requires-python {requires_python!r} allows no Python 3 version")
    problems = []
    if eol := [c for c in supported if c.eol]:
        problems.append(
            f"requires-python {requires_python!r} allows "
            + ", ".join(f"{c.version} (EOL {c.eol_date})" for c in eol)
        )
    if eol := [
        c
        for c in pythons.python_cycles()
        if c.eol and c.version in repo.classifier_python_versions
    ]:
        problems.append(f"classifiers list {', '.join(c.version for c in eol)}")
    if problems:
        return failed("; ".join(problems))
    return passed()


@group.check(
    "The latest stable Python version is declared as supported and tested in CI."
)
def latest_python(repo: Repo) -> Result:
    version = pythons.latest_python().version
    problems = []
    if repo.requires_python and not pythons.allows(repo.requires_python, version):
        problems.append(f"requires-python {repo.requires_python!r} excludes {version}")
    if version not in repo.classifier_python_versions:
        problems.append(f"no 'Programming Language :: Python :: {version}' classifier")
    if version not in repo.ci_python_versions:
        problems.append(f"{version} not found in CI workflows or tox config")
    return failed("; ".join(problems)) if problems else passed()


@group.check(
    "The upcoming Python version is tested in CI, once it has a release candidate."
)
def unreleased_python(repo: Repo) -> Result:
    version = pythons.upcoming_python()
    if version is None:
        return not_applicable("No upcoming Python version has a release candidate.")
    if version not in repo.ci_python_versions:
        return failed(f"{version} not found in CI workflows or tox config")
    return passed()


@group.check(
    "Python version classifiers match requires-python: there is one for every "
    "supported Python version it allows, and none for versions it excludes."
)
def python_classifiers(repo: Repo) -> Result:
    requires_python = repo.requires_python
    if requires_python is None:
        return not_applicable("requires-python is not declared.")
    classified = repo.classifier_python_versions
    if not classified:
        return failed("no Python version classifiers")
    problems = []
    if missing := [
        c.version
        for c in pythons.python_cycles()
        if c.released
        and not c.eol
        and pythons.allows(requires_python, c.version)
        and c.version not in classified
    ]:
        problems.append(f"no classifiers for {', '.join(missing)}")
    if excluded := sorted(
        (v for v in classified if not pythons.allows(requires_python, v)), key=Version
    ):
        problems.append(
            f"classifiers for {', '.join(excluded)}, which requires-python "
            f"{requires_python!r} excludes"
        )
    return failed("; ".join(problems)) if problems else passed()


PYPY_NOT_SUPPORTED = "Does not support PyPy."


@group.info(
    "The project supports PyPy: it has the PyPy classifier or tests PyPy in CI."
)
def supports_pypy(repo: Repo) -> bool:
    return repo.supports_pypy


@group.check("The latest PyPy version is declared as supported and tested in CI.")
def latest_pypy(repo: Repo) -> Result:
    if not repo.supports_pypy:
        return not_applicable(PYPY_NOT_SUPPORTED)
    version = pythons.pypy_versions().supported[-1]
    problems = []
    if PYPY_CLASSIFIER not in repo.classifiers:
        problems.append(f"no '{PYPY_CLASSIFIER}' classifier")
    if version not in repo.ci_pypy_versions:
        problems.append(f"PyPy {version} not found in CI workflows or tox config")
    return failed("; ".join(problems)) if problems else passed()


@group.check("End-of-life PyPy versions are not tested in CI.")
def no_eol_pypy(repo: Repo) -> Result:
    if not repo.supports_pypy:
        return not_applicable(PYPY_NOT_SUPPORTED)
    if eol := [v for v in pythons.pypy_versions().eol if v in repo.ci_pypy_versions]:
        return failed(f"CI tests PyPy {', '.join(eol)}")
    return passed()
