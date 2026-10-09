from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from oss_maint.core import Repo, Result, Status, not_applicable
from oss_maint.sync import sync_repos

if TYPE_CHECKING:
    from pathlib import Path

    from oss_maint.core import Group


@dataclass(frozen=True)
class ProjectResults:
    name: str
    #: Checked commit, None if the checkout could not be synced.
    sha: str | None
    #: By check ID.
    results: dict[str, Result]

    @property
    def url(self) -> str:
        return f"https://github.com/{self.name}"


def run_checks(
    repos: list[str],
    groups: list[Group],
    skip: dict[str, dict[str, str]],
    cache_dir: Path,
    *,
    sync: bool,
) -> list[ProjectResults]:
    """Return results for *repos*. *skip* maps repos to {check or group ID:
    reason} for checks that do not apply to them."""
    checks = [(g, c) for g in groups for c in g.checks]
    errors = sync_repos(repos, cache_dir) if sync else {}
    results = []
    for name in repos:
        path = cache_dir / name
        if name not in errors and not (path / ".git").is_dir():
            errors[name] = "not synced yet"
        if name in errors:
            error = Result(Status.ERROR, f"sync failed: {errors[name]}")
            results.append(ProjectResults(name, None, {c.id: error for _, c in checks}))
            continue
        repo = Repo(name, path)
        project_skip = skip.get(name, {})
        project_results = {}
        for group, check in checks:
            reason = project_skip.get(check.id, project_skip.get(group.id))
            project_results[check.id] = (
                not_applicable(reason) if reason else check.run(repo)
            )
        results.append(ProjectResults(name, repo.sha, project_results))
    return results
