from __future__ import annotations

import re

from packaging.requirements import Requirement

from oss_maint.core import Group, Repo, Result, failed, not_applicable, passed

group = Group("dependencies", "Dependencies")

LOWER_BOUND_OPERATORS = {">=", ">", "==", "~=", "==="}
# Names of tox environments that test minimum dependency versions, e.g. "min",
# "min-extra", "py310-pinned".
MIN_ENV_RE = re.compile(r"\b(min|minimum|lowest|pinned)\b")


@group.check("Every runtime dependency has a lower bound.")
def dependency_lower_bounds(repo: Repo) -> Result:
    if not repo.project:
        return not_applicable("No [project] table in pyproject.toml.")
    dependencies = [Requirement(d) for d in repo.project.get("dependencies", [])]
    if not dependencies:
        return not_applicable("No runtime dependencies.")
    if unbounded := list(
        dict.fromkeys(
            d.name
            for d in dependencies
            if not any(s.operator in LOWER_BOUND_OPERATORS for s in d.specifier)
        )
    ):
        return failed(f"no lower bound: {', '.join(unbounded)}")
    return passed()


@group.check(
    "A tox environment tests the minimum versions of dependencies (its name has "
    "min, minimum, lowest or pinned in it)."
)
def min_deps_env(repo: Repo) -> Result:
    if repo.project and not (
        repo.project.get("dependencies") or repo.project.get("optional-dependencies")
    ):
        return not_applicable("No dependencies.")
    if any(MIN_ENV_RE.search(s) for s in repo.tox_strings):
        return passed()
    return failed("no tox environment for minimum dependency versions")
