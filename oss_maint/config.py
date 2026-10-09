"""Loading of projects.toml."""

from __future__ import annotations

import tomllib
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


class ConfigError(Exception):
    pass


@dataclass(frozen=True)
class ProjectGroup:
    title: str
    #: GitHub "owner/name" of each project, in report order.
    repos: list[str]


@dataclass(frozen=True)
class Config:
    groups: list[ProjectGroup]
    #: {repo: {check or group ID: reason}} for checks that do not apply to a
    #: project.
    skip: dict[str, dict[str, str]]

    @property
    def repos(self) -> list[str]:
        """All projects, in report order."""
        return [repo for group in self.groups for repo in group.repos]


def load_config(path: Path, valid_ids: set[str]) -> Config:
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    config = Config(
        groups=[
            ProjectGroup(g["title"], g.get("repos", [])) for g in data.get("groups", [])
        ],
        skip=data.get("skip", {}),
    )
    repos = config.repos
    if duplicates := sorted({r for r in repos if repos.count(r) > 1}):
        raise ConfigError(f"{path}: duplicate repos: {', '.join(duplicates)}")
    for repo, checks in config.skip.items():
        if repo not in repos:
            raise ConfigError(f"{path}: [skip] has unknown repo {repo!r}")
        if unknown := sorted(set(checks) - valid_ids):
            raise ConfigError(
                f"{path}: [skip.{repo!r}] has unknown check or group IDs: {', '.join(unknown)}"
            )
    return config
