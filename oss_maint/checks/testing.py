from __future__ import annotations

import configparser

from oss_maint.core import Group, Repo, Result, failed, passed

group = Group("tests", "Tests and coverage")


def _codecov_report_types(repo: Repo) -> set[str]:
    """``report_type`` values of codecov/codecov-action steps."""
    return {
        (step.get("with") or {}).get("report_type", "coverage")
        for _, step in repo.workflow_steps()
        if step.get("uses", "").startswith("codecov/codecov-action@")
    }


@group.check("Test coverage is uploaded to Codecov in CI workflows.")
def codecov(repo: Repo) -> Result:
    if "coverage" in _codecov_report_types(repo):
        return passed()
    if any("codecov" in step.get("run", "") for _, step in repo.workflow_steps()):
        return passed()
    return failed("no codecov/codecov-action step for coverage")


@group.check(
    "Test results are uploaded to Codecov in CI workflows "
    "(codecov/codecov-action with report_type: test_results)."
)
def codecov_test_results(repo: Repo) -> Result:
    if "test_results" in _codecov_report_types(repo):
        return passed()
    return failed("no codecov/codecov-action step with report_type: test_results")


@group.check("Branch coverage is enabled.")
def branch_coverage(repo: Repo) -> Result:
    coverage = (repo.pyproject or {}).get("tool", {}).get("coverage", {})
    if coverage.get("run", {}).get("branch"):
        return passed()
    for path, section in (
        (".coveragerc", "run"),
        ("setup.cfg", "coverage:run"),
        ("tox.ini", "coverage:run"),
    ):
        config = configparser.ConfigParser(interpolation=None)
        config.read_string(repo.read_text(path) or "")
        if config.getboolean(section, "branch", fallback=False):
            return passed()
    pytest_config = [
        str((repo.pyproject or {}).get("tool", {}).get("pytest", {})),
        repo.read_text("pytest.ini") or "",
        repo.read_text("setup.cfg") or "",
        *repo.ci_strings,
    ]
    if any("--cov-branch" in s for s in pytest_config):
        return passed()
    return failed("no branch = true in coverage config, and no --cov-branch")
