from __future__ import annotations

import re
import subprocess
from typing import TYPE_CHECKING

from oss_maint.cli import main
from oss_maint.sync import prune_repos

if TYPE_CHECKING:
    from pathlib import Path

    import pytest


def test_report(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    for name in ("good", "skipped"):
        checkout = tmp_path / "cache" / "owner" / name
        checkout.mkdir(parents=True)
        (checkout / "pyproject.toml").write_text(
            '[build-system]\nbuild-backend = "hatchling.build"\n', encoding="utf-8"
        )
        git = ["git", "-C", str(checkout), "-c", "user.name=x", "-c", "user.email=x@x"]
        subprocess.run([*git, "init", "-q"], check=True)
        subprocess.run([*git, "commit", "-q", "--allow-empty", "-m", "x"], check=True)
    config = tmp_path / "projects.toml"
    config.write_text(
        '[[groups]]\ntitle = "Main"\nrepos = ["owner/good", "owner/missing"]\n'
        '[[groups]]\ntitle = "Others"\nrepos = ["owner/skipped"]\n'
        '[skip."owner/skipped"]\npackaging = "Not a Python package."\n',
        encoding="utf-8",
    )

    args = ["--config", str(config), "--cache-dir", str(tmp_path / "cache")]
    assert main([*args, "report", "--no-sync", "-d", str(tmp_path)]) == 0

    report = (tmp_path / "REPORT.md").read_text(encoding="utf-8")
    assert (
        "| [`hatchling`](#hatchling) | The build backend is hatchling. | 1/2 passing |"
        in report
    )
    assert "| [owner/good](https://github.com/owner/good) | " in report
    assert report.index("| **Main** |") < report.index("| [owner/good]")
    assert report.index("| **Others** |") < report.index("| [owner/skipped]")
    # Summary cell of the packaging group for the skipped project.
    assert "| [owner/skipped](https://github.com/owner/skipped) | " in report
    assert "[➖](#packaging)" in report
    assert (
        "- ⚠️ [owner/missing](https://github.com/owner/missing): sync failed: not synced yet"
        in report
    )
    assert (
        "- ➖ Not a Python package. [owner/skipped](https://github.com/owner/skipped)"
        in report
    )

    # Failing checks per project, linked from the summary.
    assert re.search(r"\| \[\d+\]\(PROJECTS\.md#ownergood\) \|", report)
    projects = (tmp_path / "PROJECTS.md").read_text(encoding="utf-8")
    good = projects[
        projects.index("### owner/good") : projects.index("### owner/missing")
    ]
    assert "- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): " in good
    assert "hatchling" not in good  # Passes.
    assert "has-sphinx-docs: no" in good
    missing = projects[projects.index("### owner/missing") :]
    assert (
        "- ⚠️ [`hatchling`](REPORT.md#hatchling): sync failed: not synced yet" in missing
    )

    assert main([*args, "run", "--no-sync", "-c", "hatchling", "-p", "good"]) == 0
    out = capsys.readouterr().out
    assert "  ok     owner/good" in out
    assert "1/1 passing" in out


def test_prune(tmp_path: Path) -> None:
    cache = tmp_path / "cache"
    for name, origin in [
        ("owner/kept", "https://github.com/owner/kept.git"),
        ("owner/dropped", "https://github.com/owner/dropped.git"),
        ("other/dropped", "https://github.com/other/dropped.git"),
        ("owner/foreign", "https://example.com/foreign.git"),
    ]:
        checkout = cache / name
        checkout.mkdir(parents=True)
        subprocess.run(["git", "init", "-q", str(checkout)], check=True)
        subprocess.run(
            ["git", "-C", str(checkout), "remote", "add", "origin", origin], check=True
        )
    (cache / "owner" / "not-a-clone").mkdir()

    assert prune_repos(["owner/kept"], cache) == ["other/dropped", "owner/dropped"]
    assert sorted(p.name for p in (cache / "owner").iterdir()) == [
        "foreign",
        "kept",
        "not-a-clone",
    ]
    assert not (cache / "other").exists()
