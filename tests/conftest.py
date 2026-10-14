from __future__ import annotations

from datetime import UTC, date, datetime, timedelta

import pytest
from packaging.version import Version

from oss_maint import pypi, pythons
from oss_maint.checks import docs


def _release(version: str, uploaded: datetime | int) -> pypi.Release:
    """A release uploaded on *uploaded*, or that many days ago."""
    if isinstance(uploaded, int):
        uploaded = datetime.now(tz=UTC) - timedelta(days=uploaded)
    return pypi.Release(Version(version), uploaded)


#: Releases of PyPI projects, oldest first.
RELEASES = {
    "ruff": [_release("0.15.0", 300), _release("0.16.0", 200), _release("0.17.0", 10)],
    "zizmor": [_release("1.0.0", 300), _release("1.1.0", 200)],
    "example": [
        _release("1.0", datetime(2025, 1, 2, tzinfo=UTC)),
        _release("1.1", datetime(2026, 3, 4, tzinfo=UTC)),
    ],
}


@pytest.fixture(autouse=True)
def fake_python_cycles(monkeypatch: pytest.MonkeyPatch) -> None:
    """Replace Python, PyPy and PyPI release data, which is otherwise fetched
    over the network, with fixed data."""

    def no_network(url: str) -> None:
        raise AssertionError(f"tests must not fetch {url}")

    monkeypatch.setattr(pythons, "_get_json", no_network)
    cycles = [
        pythons.PythonCycle("3.9", date(2020, 10, 5), date(2025, 10, 31)),
        pythons.PythonCycle("3.10", date(2021, 10, 4), date(2099, 10, 31)),
        pythons.PythonCycle("3.11", date(2022, 10, 24), date(2099, 10, 31)),
        pythons.PythonCycle("3.12", date(2099, 10, 2), date(2099, 10, 31)),
    ]
    monkeypatch.setattr(pythons, "python_cycles", lambda: cycles)
    monkeypatch.setattr(pythons, "upcoming_python", lambda: "3.12")
    monkeypatch.setattr(
        pythons,
        "pypy_versions",
        lambda: pythons.PyPyVersions(supported=["3.10", "3.11"], eol=["3.9"]),
    )
    monkeypatch.setattr(docs, "latest_sphinx_scrapy", lambda: "0.13.0")
    monkeypatch.setattr(pypi, "releases", RELEASES.get)
