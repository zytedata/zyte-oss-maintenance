from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

import pytest

from oss_maint import pythons

if TYPE_CHECKING:
    from collections.abc import Iterator

# The real functions, which conftest.py replaces with fixed data.
python_cycles = pythons.python_cycles
upcoming_python = pythons.upcoming_python

CYCLES = {
    "result": {
        "releases": [
            {"name": "3.14", "releaseDate": "2099-10-07", "eolFrom": "2030-10-31"},
            {"name": "3.13", "releaseDate": "2024-10-07", "eolFrom": "2029-10-31"},
            {"name": "2.7", "releaseDate": "2010-07-03", "eolFrom": "2020-01-01"},
        ]
    }
}
RELEASES = [
    {"name": f"Python {version}", "release_date": f"{day}T12:00:00Z"}
    for version, day in [
        ("3.13.0", "2024-10-07"),
        ("3.13.1", "2024-12-03"),
        ("3.14.0", "2025-10-07"),
        ("3.15.0rc1", "2026-08-01"),
        ("3.15.0", "2026-10-01"),
        ("3.16.0rc1", "2027-08-01"),
    ]
]


@pytest.fixture(autouse=True)
def fake_sources(monkeypatch: pytest.MonkeyPatch) -> Iterator[None]:
    def get_json(url: str) -> Any:
        return {pythons.CYCLES_URL: CYCLES, pythons.RELEASES_URL: RELEASES}[url]

    monkeypatch.setattr(pythons, "_get_json", get_json)
    monkeypatch.setattr(pythons, "python_cycles", python_cycles)
    monkeypatch.setattr(pythons, "upcoming_python", upcoming_python)
    yield
    for func in (python_cycles, upcoming_python, pythons._python_releases):
        func.cache_clear()


def test_python_cycles() -> None:
    assert pythons.python_cycles() == [
        pythons.PythonCycle("3.13", date(2024, 10, 7), date(2029, 10, 31)),
        # python.org has a final release that endoflife.date does not list yet.
        pythons.PythonCycle("3.14", date(2025, 10, 7), date(2030, 10, 31)),
        pythons.PythonCycle("3.15", date(2026, 10, 1), None),
    ]
    assert pythons.latest_python().version == "3.15"
    assert pythons.upcoming_python() == "3.16"
