"""Python and PyPy version data."""

from __future__ import annotations

import json
import re
import urllib.request
from dataclasses import dataclass
from datetime import UTC, date, datetime
from functools import cache
from typing import Any

from packaging.specifiers import SpecifierSet
from packaging.version import Version

# Release cycles, with release and EOL dates. It can lag behind python.org for
# new releases.
CYCLES_URL = "https://endoflife.date/api/v1/products/python"
# All releases, including pre-releases.
RELEASES_URL = "https://www.python.org/api/v2/downloads/release/?is_published=true"
# All PyPy releases, used by actions/setup-python.
PYPY_URL = "https://downloads.python.org/pypy/versions.json"


def _get_json(url: str) -> Any:
    with urllib.request.urlopen(url, timeout=30) as response:  # noqa: S310
        return json.load(response)


def _minor(version: str) -> str:
    """Return e.g. "3.12" for "3.12.4"."""
    return ".".join(version.split(".")[:2])


@dataclass(frozen=True)
class PythonCycle:
    #: e.g. "3.12"
    version: str
    release_date: date
    #: None if not known yet.
    eol_date: date | None

    @property
    def released(self) -> bool:
        return self.release_date <= datetime.now(tz=UTC).date()

    @property
    def eol(self) -> bool:
        return (
            self.eol_date is not None and self.eol_date <= datetime.now(tz=UTC).date()
        )

    @property
    def sort_key(self) -> tuple[int, ...]:
        return tuple(int(part) for part in self.version.split("."))


@cache
def _python_releases() -> list[dict[str, Any]]:
    return _get_json(RELEASES_URL)


def _final_release_dates() -> dict[str, date]:
    """Dates of the first final releases of Python 3 versions, e.g. of 3.12.0
    for "3.12", from python.org."""
    return {
        m.group(1): datetime.fromisoformat(release["release_date"]).date()
        for release in _python_releases()
        if (m := re.fullmatch(r"Python (3\.\d+)\.0", release["name"]))
    }


@cache
def python_cycles() -> list[PythonCycle]:
    """Python 3 release cycles, oldest first. Versions released on python.org
    but missing from endoflife.date, which can lag behind, have no EOL date."""
    released = _final_release_dates()
    cycles = {}
    for release in _get_json(CYCLES_URL)["result"]["releases"]:
        if not release["name"].startswith("3."):
            continue
        release_date = date.fromisoformat(release["releaseDate"])
        if release["name"] in released:
            release_date = min(release_date, released[release["name"]])
        cycles[release["name"]] = PythonCycle(
            version=release["name"],
            release_date=release_date,
            eol_date=date.fromisoformat(release["eolFrom"]),
        )
    for version, release_date in released.items():
        cycles.setdefault(version, PythonCycle(version, release_date, None))
    return sorted(cycles.values(), key=lambda c: c.sort_key)


def latest_python() -> PythonCycle:
    return [c for c in python_cycles() if c.released][-1]


def allows(requires_python: str, version: str) -> bool:
    """Return whether *requires_python* allows any release of the *version*
    (e.g. "3.12") cycle."""
    spec = SpecifierSet(requires_python)
    return any(spec.contains(f"{version}.{patch}") for patch in range(100))


@cache
def upcoming_python() -> str | None:
    """Return the Python version, e.g. "3.15", that has a release candidate
    but no final release yet, if any."""
    candidates, finals = set(), set()
    for release in _python_releases():
        if m := re.fullmatch(r"Python (\d+\.\d+)\.\d+(rc\d+)?", release["name"]):
            (candidates if m.group(2) else finals).add(m.group(1))
    if upcoming := candidates - finals:
        return min(upcoming, key=Version)
    return None


@dataclass(frozen=True)
class PyPyVersions:
    #: Python versions, e.g. "3.11", provided by the latest PyPy release,
    #: oldest first.
    supported: list[str]
    #: Python 3 versions provided only by older PyPy releases, oldest first.
    eol: list[str]


@cache
def pypy_versions() -> PyPyVersions:
    releases = [
        r
        for r in _get_json(PYPY_URL)
        if r["stable"] and r["python_version"].startswith("3.")
    ]
    latest = max((r["pypy_version"] for r in releases), key=Version)
    supported = {
        _minor(r["python_version"]) for r in releases if r["pypy_version"] == latest
    }
    eol = {_minor(r["python_version"]) for r in releases} - supported
    return PyPyVersions(sorted(supported, key=Version), sorted(eol, key=Version))
