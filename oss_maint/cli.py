from __future__ import annotations

import argparse
import sys
from datetime import UTC, datetime
from pathlib import Path

from oss_maint.checks import ALL_IDS, GROUPS, select_groups
from oss_maint.config import ConfigError, load_config
from oss_maint.core import Status, tally
from oss_maint.report import (
    PROJECTS_FILE,
    REPORT_FILE,
    render_projects_report,
    render_report,
)
from oss_maint.runner import run_checks
from oss_maint.sync import prune_repos, sync_repos

ROOT = Path(__file__).resolve().parent.parent

LABELS = {
    Status.PASS: "ok",
    Status.FAIL: "FAIL",
    Status.NA: "n/a",
    Status.ERROR: "ERROR",
    Status.YES: "yes",
    Status.NO: "no",
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="oss-maint",
        description="Check which projects are up to date with maintenance practices.",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=ROOT / "projects.toml",
        help="default: %(default)s",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=ROOT / ".cache" / "repos",
        help="where project checkouts live; default: %(default)s",
    )
    commands = parser.add_subparsers(dest="command", required=True)

    commands.add_parser("checks", help="list checks and their statements")

    sync_parser = commands.add_parser("sync", help="clone or update project checkouts")
    _add_project_arg(sync_parser)

    run_parser = commands.add_parser("run", help="run checks and print the results")
    run_parser.add_argument(
        "-c",
        "--check",
        action="append",
        dest="checks",
        metavar="CHECK",
        help="check or group ID; repeatable; default: all",
    )
    _add_project_arg(run_parser)
    _add_no_sync_arg(run_parser)

    report_parser = commands.add_parser(
        "report",
        help=f"run all checks on all projects and write {REPORT_FILE} and {PROJECTS_FILE}",
    )
    report_parser.add_argument(
        "-d",
        "--output-dir",
        type=Path,
        default=ROOT,
        help=f"where to write {REPORT_FILE} and {PROJECTS_FILE}; default: %(default)s",
    )
    _add_no_sync_arg(report_parser)

    args = parser.parse_args(argv)
    groups = GROUPS
    try:
        config = load_config(args.config, ALL_IDS)
        repos = _select_repos(config.repos, getattr(args, "projects", None))
        if getattr(args, "checks", None):
            groups = select_groups(args.checks)
    except (ConfigError, ValueError) as e:
        parser.error(str(e))

    if args.command in {"sync", "run", "report"} and not getattr(
        args, "no_sync", False
    ):
        for name in prune_repos(config.repos, args.cache_dir):
            print(f"Deleted checkout of {name}, not in {args.config}", file=sys.stderr)

    if args.command == "checks":
        for group in groups:
            print(f"{group.id}: {group.title}")
            for check in group.checks:
                print(f"  {check.id}: {check.statement}")
    elif args.command == "sync":
        errors = sync_repos(repos, args.cache_dir)
        for name, error in errors.items():
            print(f"{name}: {error}", file=sys.stderr)
        return 1 if errors else 0
    elif args.command == "run":
        projects = run_checks(
            repos, groups, config.skip, args.cache_dir, sync=not args.no_sync
        )
        width = max(len(p.name) for p in projects)
        for group in groups:
            print(f"\n# {group.title}")
            for check in group.checks:
                print(f"\n{check.id}: {check.statement}")
                for project in projects:
                    result = project.results[check.id]
                    label = result.value or LABELS[result.status]
                    line = f"  {label:<5}  {project.name:<{width}}  {result.detail}"
                    print(line.rstrip())
                print(f"  {tally(check, [p.results[check.id] for p in projects])}")
    elif args.command == "report":
        projects = run_checks(
            repos, groups, config.skip, args.cache_dir, sync=not args.no_sync
        )
        today = datetime.now(tz=UTC).date()
        for filename, render in (
            (REPORT_FILE, render_report),
            (PROJECTS_FILE, render_projects_report),
        ):
            path = args.output_dir / filename
            path.write_text(
                render(groups, config.groups, projects, today), encoding="utf-8"
            )
            print(f"Wrote {path}")
    return 0


def _add_project_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-p",
        "--project",
        action="append",
        dest="projects",
        metavar="PROJECT",
        help="owner/name or name of a project; repeatable; default: all",
    )


def _add_no_sync_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--no-sync",
        action="store_true",
        help="use existing checkouts instead of fetching the latest commits",
    )


def _select_repos(repos: list[str], selectors: list[str] | None) -> list[str]:
    if not selectors:
        return repos
    selected = []
    for selector in selectors:
        matches = [r for r in repos if selector in (r, r.split("/")[1])]
        if not matches:
            raise ConfigError(f"unknown project: {selector}")
        selected.extend(m for m in matches if m not in selected)
    return selected


if __name__ == "__main__":
    sys.exit(main())
