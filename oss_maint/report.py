"""Markdown report rendering: REPORT.md, by check, and PROJECTS.md, by
project."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

from oss_maint.core import APPLICABLE, Status, tally

if TYPE_CHECKING:
    from collections.abc import Callable
    from datetime import date

    from oss_maint.config import ProjectGroup
    from oss_maint.core import Group
    from oss_maint.runner import ProjectResults

REPORT_FILE = "REPORT.md"
PROJECTS_FILE = "PROJECTS.md"

SYMBOLS = {
    Status.PASS: "✅",
    Status.FAIL: "❌",
    Status.NA: "➖",
    Status.ERROR: "⚠️",
    Status.YES: "yes",
    Status.NO: "no",
}
LEGEND = (
    "✅ passes · ❌ fails · ➖ not applicable · ⚠️ check error · "
    "yes/no or a value: result of an informational check. "
    "Click a symbol for details."
)


def _anchor(heading: str) -> str:
    """Return the anchor GitHub generates for *heading*."""
    return re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")


def _link(project: ProjectResults) -> str:
    return f"[{project.name}]({project.url})"


def _failing(project: ProjectResults) -> int:
    return sum(
        r.status in {Status.FAIL, Status.ERROR} for r in project.results.values()
    )


def _commit_link(project: ProjectResults) -> str:
    if not project.sha:
        return ""
    return f"[`{project.sha[:7]}`]({project.url}/commit/{project.sha})"


def _summary_cell(statuses: list[Status]) -> str:
    """Worst status of a group, and how many applicable checks pass."""
    applicable = [s for s in statuses if s in APPLICABLE]
    if not applicable:
        return SYMBOLS[Status.NA]
    for status in (Status.FAIL, Status.ERROR, Status.PASS):
        if status in applicable:
            return (
                f"{SYMBOLS[status]} {applicable.count(Status.PASS)}/{len(applicable)}"
            )
    raise AssertionError


def _project_rows(
    project_groups: list[ProjectGroup],
    projects: list[ProjectResults],
    columns: int,
    row: Callable[[ProjectResults], str],
) -> list[str]:
    """Return a table row for each project, under a row with the title of its
    group. *columns* is the number of columns after the project one."""
    by_name = {p.name: p for p in projects}
    lines = []
    for project_group in project_groups:
        group_projects = [by_name[r] for r in project_group.repos if r in by_name]
        if group_projects:
            lines.append(f"| **{project_group.title}** |" + " |" * columns)
            lines.extend(row(project) for project in group_projects)
    return lines


def render_report(
    groups: list[Group],
    project_groups: list[ProjectGroup],
    projects: list[ProjectResults],
    today: date,
) -> str:
    lines = [
        "# Maintenance report",
        "",
        (
            f"Generated on {today} with `oss-maint report`. Do not edit by hand. "
            f"See [{PROJECTS_FILE}]({PROJECTS_FILE}) for what fails in each project."
        ),
        "",
        LEGEND,
        *_render_facts(groups),
        "",
        "## Summary",
        "",
        "Checks passing per group.",
        "",
        "| Project | "
        + " | ".join(f"[{g.title}](#{_anchor(g.title)})" for g in groups)
        + " | Failing | Commit |",
        "| --- |" + " :---: |" * len(groups) + " :---: | --- |",
    ]

    def summary_row(project: ProjectResults) -> str:
        cells = [
            f"[{_summary_cell([project.results[c.id].status for c in g.checks])}]"
            f"(#{_anchor(g.title)})"
            for g in groups
        ]
        failing = f"[{_failing(project)}]({PROJECTS_FILE}#{_anchor(project.name)})"
        return (
            f"| {_link(project)} | {' | '.join(cells)} | {failing} "
            f"| {_commit_link(project)} |"
        )

    lines += _project_rows(project_groups, projects, len(groups) + 2, summary_row)

    for group in groups:
        lines += _render_group(group, project_groups, projects)
    return "\n".join(lines) + "\n"


def _render_facts(groups: list[Group]) -> list[str]:
    facts = [fact for group in groups for fact in group.facts]
    if not facts:
        return []
    return [
        "",
        "## Reference data",
        "",
        "Values that checks compare projects against.",
        "",
        *(f"- {fact.label}: {fact.run()}" for fact in facts),
    ]


def _render_group(
    group: Group, project_groups: list[ProjectGroup], projects: list[ProjectResults]
) -> list[str]:
    lines = [
        "",
        f"## {group.title}",
        "",
        "| Check | Statement | Results |",
        "| --- | --- | --- |",
    ]
    for check in group.checks:
        results = [p.results[check.id] for p in projects]
        lines.append(
            f"| [`{check.id}`](#{check.id}) | {check.statement} | {tally(check, results)} |"
        )

    lines += [
        "",
        "| Project | " + " | ".join(f"[{c.id}](#{c.id})" for c in group.checks) + " |",
        "| --- |" + " :---: |" * len(group.checks),
    ]

    def row(project: ProjectResults) -> str:
        cells = []
        for check in group.checks:
            result = project.results[check.id]
            symbol = result.value or SYMBOLS[result.status]
            cells.append(f"[{symbol}](#{check.id})" if result.detail else symbol)
        return f"| {_link(project)} | {' | '.join(cells)} |"

    lines += _project_rows(project_groups, projects, len(group.checks), row)

    for check in group.checks:
        lines += ["", f"### {check.id}", "", check.statement, ""]
        results = [(p, p.results[check.id]) for p in projects]
        noted = False
        for status in (Status.FAIL, Status.ERROR, Status.PASS):
            for project, result in results:
                if result.status is status and result.detail:
                    lines.append(
                        f"- {SYMBOLS[status]} {_link(project)}: {result.detail}"
                    )
                    noted = True
        # Not-applicable results are grouped by reason, which is often shared.
        reasons: dict[str, list[ProjectResults]] = {}
        for project, result in results:
            if result.status is Status.NA:
                reasons.setdefault(result.detail, []).append(project)
        for reason, reason_projects in reasons.items():
            lines.append(
                f"- {SYMBOLS[Status.NA]} {reason or 'Not applicable.'} "
                + ", ".join(_link(p) for p in reason_projects)
            )
            noted = True
        if not noted:
            lines.append("Nothing to report.")
    return lines


def render_projects_report(
    groups: list[Group],
    project_groups: list[ProjectGroup],
    projects: list[ProjectResults],
    today: date,
) -> str:
    """Render a report with what fails in each project."""
    lines = [
        "# Maintenance report by project",
        "",
        (
            f"Generated on {today} with `oss-maint report`. Do not edit by hand. "
            "Lists failing checks and notes for each project; see "
            f"[{REPORT_FILE}]({REPORT_FILE}) for all results."
        ),
    ]
    by_name = {p.name: p for p in projects}
    for project_group in project_groups:
        group_projects = [by_name[r] for r in project_group.repos if r in by_name]
        if not group_projects:
            continue
        lines += ["", f"## {project_group.title}"]
        for project in group_projects:
            lines += _render_project(groups, project)
    return "\n".join(lines) + "\n"


def _render_project(groups: list[Group], project: ProjectResults) -> list[str]:
    checks = [c for g in groups for c in g.checks]
    statuses = [project.results[c.id].status for c in checks]
    applicable = sum(s in APPLICABLE for s in statuses)
    header = [
        f"[Repository]({project.url})",
        *([f"commit {_commit_link(project)}"] if project.sha else []),
        f"{statuses.count(Status.PASS)}/{applicable} checks passing",
    ]
    facts = [
        f"{c.id}: {project.results[c.id].value or SYMBOLS[project.results[c.id].status]}"
        for c in checks
        if c.informational and project.results[c.id].status in {Status.YES, Status.NO}
    ]
    lines = ["", f"### {project.name}", "", " · ".join(header)]
    if facts:
        lines += ["", " · ".join(facts)]
    noted = False
    for group in groups:
        items = []
        for status in (Status.FAIL, Status.ERROR, Status.PASS):
            for check in group.checks:
                result = project.results[check.id]
                if result.status is status and (
                    result.detail or status is not Status.PASS
                ):
                    items.append(
                        f"- {SYMBOLS[status]} [`{check.id}`]({REPORT_FILE}#{check.id}): "
                        f"{result.detail}"
                    )
        if items:
            lines += ["", f"**{group.title}**", "", *items]
            noted = True
    if not noted:
        lines += ["", "All applicable checks pass."]
    return lines
