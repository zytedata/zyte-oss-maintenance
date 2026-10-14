"""Release data from PyPI."""

from __future__ import annotations

import urllib.error
from dataclasses import dataclass
from datetime import datetime
from functools import cache
from http import HTTPStatus
from typing import Any

from packaging.version import InvalidVersion, Version

from oss_maint import pythons

PROJECT_URL = "https://pypi.org/pypi/{}/json"


@dataclass(frozen=True)
class Release:
    version: Version
    #: When its first file was uploaded.
    uploaded: datetime


def _project(name: str) -> dict[str, Any] | None:
    try:
        return pythons._get_json(PROJECT_URL.format(name))
    except urllib.error.HTTPError as e:
        if e.code == HTTPStatus.NOT_FOUND:
            return None
        raise


@cache
def releases(name: str) -> list[Release] | None:
    """Final releases of the *name* project with files that are not yanked,
    oldest first, None if it is not on PyPI."""
    project = _project(name)
    if project is None:
        return None
    result = []
    for version, files in project["releases"].items():
        try:
            parsed = Version(version)
        except InvalidVersion:
            continue
        uploads = [
            datetime.fromisoformat(f["upload_time_iso_8601"])
            for f in files
            if not f.get("yanked")
        ]
        if uploads and not parsed.is_prerelease:
            result.append(Release(parsed, min(uploads)))
    return sorted(result, key=lambda r: r.version)
