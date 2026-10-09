"""Shallow clones of project default branches."""

from __future__ import annotations

import contextlib
import os
import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


class SyncError(Exception):
    pass


def _url(name: str) -> str:
    return f"https://github.com/{name}.git"


def _git(*args: str | Path) -> str:
    result = subprocess.run(
        ["git", *map(str, args)],
        capture_output=True,
        text=True,
        env={**os.environ, "GIT_TERMINAL_PROMPT": "0"},
        check=False,
    )
    if result.returncode:
        raise SyncError(result.stderr.strip() or f"git exited with {result.returncode}")
    return result.stdout


def sync_repo(name: str, path: Path) -> None:
    """Clone or update *path* to the latest default branch commit of the
    *name* GitHub repository."""
    if (path / ".git").is_dir():
        _git("-C", path, "fetch", "--quiet", "--depth=1", "origin", "HEAD")
        _git("-C", path, "reset", "--quiet", "--hard", "FETCH_HEAD")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        _git("clone", "--quiet", "--depth=1", _url(name), path)


def sync_repos(names: list[str], cache_dir: Path, jobs: int = 8) -> dict[str, str]:
    """Sync *names* in parallel, and return error messages by repo name."""

    def sync(name: str) -> str | None:
        try:
            sync_repo(name, cache_dir / name)
        except SyncError as e:
            return str(e)
        return None

    with ThreadPoolExecutor(jobs) as executor:
        errors = dict(zip(names, executor.map(sync, names), strict=True))
    return {name: error for name, error in errors.items() if error}


def prune_repos(keep: list[str], cache_dir: Path) -> list[str]:
    """Delete checkouts in *cache_dir* of repos not in *keep*, and return
    their names. Only checkouts cloned by :func:`sync_repo` are deleted."""
    removed = []
    for path in sorted(cache_dir.glob("*/*")):
        name = path.relative_to(cache_dir).as_posix()
        if name in keep or not _is_clone_of(path, name):
            continue
        shutil.rmtree(path)
        removed.append(name)
        with contextlib.suppress(OSError):  # Other repos of the owner remain.
            path.parent.rmdir()
    return removed


def _is_clone_of(path: Path, name: str) -> bool:
    if not (path / ".git").is_dir():
        return False
    try:
        origin = _git("-C", path, "remote", "get-url", "origin").strip()
    except SyncError:
        return False
    return origin == _url(name)
