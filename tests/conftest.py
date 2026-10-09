from __future__ import annotations

from datetime import date

import pytest

from oss_maint import pythons


@pytest.fixture(autouse=True)
def fake_python_cycles(monkeypatch: pytest.MonkeyPatch) -> None:
    """Replace Python and PyPy version data, which is otherwise fetched over
    the network, with fixed data."""

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
