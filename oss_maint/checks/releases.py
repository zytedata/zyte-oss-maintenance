from __future__ import annotations

import re
from typing import Any

from oss_maint.core import Group, Repo, Result, failed, passed

group = Group("releases", "Releases")

NO_PUBLISHING = "no workflow publishes to PyPI"
PYPI_PUBLISH_ACTION = "pypa/gh-action-pypi-publish@"
# Commands and actions that build distributions.
BUILD_COMMAND_RE = re.compile(
    r"python3? -m build|pyproject-build|\b(uv|hatch|poetry|flit) build"
    r"|setup\.py (sdist|bdist)|pip wheel"
)
BUILD_ACTION_RE = re.compile(r"build")


def _publish_jobs(repo: Repo) -> list[tuple[str, dict[Any, Any], str, dict[str, Any]]]:
    """``(workflow path, workflow, job ID, job)`` of jobs that publish to
    PyPI."""
    return [
        (path, workflow, job_id, job)
        for path, workflow in repo.workflows.items()
        for job_id, job in (workflow.get("jobs") or {}).items()
        if any(_publishes(step) for step in job.get("steps") or [])
    ]


def _publishes(step: dict[str, Any]) -> bool:
    return step.get("uses", "").startswith(PYPI_PUBLISH_ACTION) or (
        "twine upload" in step.get("run", "")
    )


def _builds(step: dict[str, Any]) -> bool:
    if BUILD_COMMAND_RE.search(step.get("run", "")):
        return True
    uses = step.get("uses", "")
    return bool(BUILD_ACTION_RE.search(uses)) and not uses.startswith("actions/")


def _triggers(workflow: dict[Any, Any]) -> dict[str, Any]:
    # YAML 1.1 parses the "on" key as True.
    triggers = workflow.get("on", workflow.get(True)) or {}
    if isinstance(triggers, str):
        return {triggers: None}
    if isinstance(triggers, list):
        return dict.fromkeys(triggers)
    return triggers


@group.check(
    "Releases are published to PyPI from GitHub Actions through trusted publishing."
)
def trusted_publishing(repo: Repo) -> Result:
    jobs = _publish_jobs(repo)
    if not jobs:
        return failed(NO_PUBLISHING)
    problems = []
    for path, workflow, _, job in jobs:
        for step in job.get("steps") or []:
            if "twine upload" in step.get("run", ""):
                problems.append(f"{path} publishes with twine upload")
            elif step.get("uses", "").startswith(PYPI_PUBLISH_ACTION):
                if "password" in (step.get("with") or {}):
                    problems.append(f"{path} uses an API token")
                # Job-level permissions replace workflow-level ones.
                permissions = job.get("permissions", workflow.get("permissions"))
                if not _has_id_token(permissions):
                    problems.append(f"{path} lacks the id-token: write permission")
    return failed("; ".join(problems)) if problems else passed()


def _has_id_token(permissions: object) -> bool:
    if permissions == "write-all":
        return True
    return isinstance(permissions, dict) and permissions.get("id-token") == "write"


@group.check(
    "Publishing is triggered by pushing a tag, not by creating a GitHub release."
)
def publish_on_tag(repo: Repo) -> Result:
    jobs = _publish_jobs(repo)
    if not jobs:
        return failed(NO_PUBLISHING)
    problems = []
    for path in sorted({path for path, _, _, _ in jobs}):
        triggers = _triggers(repo.workflows[path])
        if "release" in triggers:
            problems.append(f"{path} is triggered by GitHub releases")
        elif "tags" not in (triggers.get("push") or {}):
            problems.append(f"{path} is not triggered by tag pushes")
    return failed("; ".join(problems)) if problems else passed()


@group.check(
    "The publish workflow builds distributions in a separate job from the one "
    "that publishes them."
)
def separate_build_job(repo: Repo) -> Result:
    jobs = _publish_jobs(repo)
    if not jobs:
        return failed(NO_PUBLISHING)
    problems = [
        f"{path}: job {job_id!r} builds and publishes"
        for path, _, job_id, job in jobs
        if any(_builds(step) for step in job.get("steps") or [])
    ]
    return failed("; ".join(problems)) if problems else passed()


@group.check("bump-my-version is configured, in pyproject.toml or .bumpversion.toml.")
def bump_my_version(repo: Repo) -> Result:
    if "bumpversion" in (repo.pyproject or {}).get("tool", {}):
        return passed()
    if repo.exists(".bumpversion.toml"):
        return passed()
    if repo.exists(".bumpversion.cfg"):
        return failed("only legacy (bump2version) configuration, in .bumpversion.cfg")
    if "[bumpversion]" in (repo.read_text("setup.cfg") or ""):
        return failed("only legacy (bump2version) configuration, in setup.cfg")
    return failed("no [tool.bumpversion] in pyproject.toml or .bumpversion.toml")
