from __future__ import annotations

import re
from datetime import UTC, datetime, timedelta
from typing import Any

from packaging.version import InvalidVersion, Version

from oss_maint import pypi
from oss_maint.core import Group, Repo, Result, failed, not_applicable, passed

group = Group("linting", "Linting")

NO_PRE_COMMIT = "No .pre-commit-config.yaml."

# Hook IDs of tools that ruff replaces.
RUFF_REPLACES = {
    "autoflake",
    "autopep8",
    "black",
    "flake8",
    "isort",
    "pycodestyle",
    "pydocstyle",
    "pyflakes",
    "pyupgrade",
}


def _require_hooks(repo: Repo, *hook_ids: str) -> Result:
    if repo.pre_commit_hook_ids is None:
        return failed("no .pre-commit-config.yaml")
    if missing := [h for h in hook_ids if h not in repo.pre_commit_hook_ids]:
        return failed(f"missing pre-commit hooks: {', '.join(missing)}")
    return passed()


@group.check(
    "ruff-check and ruff-format are used, instead of tools that ruff replaces."
)
def ruff(repo: Repo) -> Result:
    if repo.pre_commit_hook_ids is None:
        return failed("no .pre-commit-config.yaml")
    hook_ids = set(repo.pre_commit_hook_ids)
    if "ruff" in hook_ids:  # Legacy alias.
        hook_ids.add("ruff-check")
    problems = []
    if missing := [h for h in ("ruff-check", "ruff-format") if h not in hook_ids]:
        problems.append(f"missing pre-commit hooks: {', '.join(missing)}")
    if replaced := sorted(hook_ids & RUFF_REPLACES):
        problems.append(f"pre-commit still runs {', '.join(replaced)}")
    return failed("; ".join(problems)) if problems else passed()


# Rules that ruff enables when its configuration does not select any.
DEFAULT_RUFF_RULES = {"E4", "E7", "E9", "F"}


def _ruff_config(repo: Repo) -> dict[str, Any] | None:
    for path in (".ruff.toml", "ruff.toml"):
        if (config := repo.read_toml(path)) is not None:
            return config
    return (repo.pyproject or {}).get("tool", {}).get("ruff")


@group.check("ruff enables rules beyond its defaults, with select or extend-select.")
def ruff_rules(repo: Repo) -> Result:
    config = _ruff_config(repo)
    if config is None and not (repo.pre_commit_hook_ids or set()) & {
        "ruff",
        "ruff-check",
    }:
        return not_applicable("Does not use ruff.")
    rules = set()
    # Top-level select and extend-select are deprecated aliases.
    for table in (config or {}, (config or {}).get("lint", {})):
        rules.update(table.get("select", []), table.get("extend-select", []))
    if not rules - DEFAULT_RUFF_RULES:
        return failed("only the default rules are enabled")
    return passed()


@group.info("A tox environment runs pylint.")
def pylint(repo: Repo) -> bool:
    return any(re.search(r"\bpylint\b", s) for s in repo.tox_strings)


PRE_COMMIT_RUN_RE = re.compile(r"\b(pre-commit|prek) run\b")
PRE_COMMIT_ACTIONS = ("pre-commit/action@", "j178/prek-action@")


@group.check("pre-commit runs in CI workflows, directly or through tox.")
def pre_commit_in_ci(repo: Repo) -> Result:
    if repo.pre_commit_hooks is None:
        return not_applicable(NO_PRE_COMMIT)
    for _, step in repo.workflow_steps():
        if step.get("uses", "").startswith(PRE_COMMIT_ACTIONS) or (
            PRE_COMMIT_RUN_RE.search(step.get("run", ""))
        ):
            return passed()
    envs = [
        name
        for name, strings in repo.tox_envs.items()
        if any(PRE_COMMIT_RUN_RE.search(s) for s in strings)
    ]
    for env in envs:
        env_re = re.compile(rf"(?<![\w-]){re.escape(env)}(?![\w-])")
        if any(env_re.search(s) for s in repo.workflow_strings):
            return passed()
    if envs:
        return failed(
            f"tox environments that run pre-commit are not run in CI: {', '.join(envs)}"
        )
    return failed("not run in CI workflows or tox")


HOOK_UPDATE_DAYS = 180
# Tools of the pre-commit hook repositories that are checked, by repository
# URL. Hook revs match the versions of the tools on PyPI. sphinx-scrapy has its
# own, stricter check.
HOOK_TOOLS = {
    "https://github.com/astral-sh/ruff-pre-commit": "ruff",
    "https://github.com/zizmorcore/zizmor-pre-commit": "zizmor",
}


def min_hook_version(tool: str) -> Version:
    """The newest release of *tool* published at least
    :data:`HOOK_UPDATE_DAYS` days ago."""
    cutoff = datetime.now(tz=UTC) - timedelta(days=HOOK_UPDATE_DAYS)
    releases = pypi.releases(tool) or []
    return max(r.version for r in releases if r.uploaded <= cutoff)


@group.fact(
    f"Minimum pre-commit hook versions, the newest releases at least "
    f"{HOOK_UPDATE_DAYS} days old"
)
def min_hook_versions() -> str:
    return ", ".join(
        f"{tool} {min_hook_version(tool)}" for tool in sorted(HOOK_TOOLS.values())
    )


@group.check(
    f"The {' and '.join(sorted(HOOK_TOOLS.values()))} pre-commit hooks are updated "
    f"within {HOOK_UPDATE_DAYS} days of a new release."
)
def pre_commit_updates(repo: Repo) -> Result:
    config = repo.read_yaml(".pre-commit-config.yaml")
    if config is None:
        return not_applicable(NO_PRE_COMMIT)
    outdated: list[str] = []
    checked = False
    for hook_repo in config.get("repos") or []:
        url = str(hook_repo.get("repo", "")).lower().rstrip("/").removesuffix(".git")
        if (tool := HOOK_TOOLS.get(url)) is None:
            continue
        rev = str(hook_repo.get("rev", ""))
        try:
            version = Version(rev)
        except InvalidVersion:
            continue
        checked = True
        if version < (minimum := min_hook_version(tool)):
            outdated.append(f"{tool} {rev} ({minimum} or later expected)")
    if not checked:
        return not_applicable("No checked hooks.")
    return failed(f"outdated: {', '.join(outdated)}") if outdated else passed()


@group.check("GitHub Actions workflows are linted with actionlint.")
def actionlint(repo: Repo) -> Result:
    if not repo.workflows:
        return not_applicable("No GitHub Actions workflows.")
    return _require_hooks(repo, "actionlint")


@group.check("GitHub Actions workflows are audited with zizmor.")
def zizmor(repo: Repo) -> Result:
    if not repo.workflows:
        return not_applicable("No GitHub Actions workflows.")
    return _require_hooks(repo, "zizmor")


@group.check("Dependabot updates GitHub Actions, which zizmor requires pinning.")
def dependabot(repo: Repo) -> Result:
    if not repo.workflows:
        return not_applicable("No GitHub Actions workflows.")
    if "zizmor" not in (repo.pre_commit_hook_ids or set()):
        return not_applicable("Does not use zizmor.")
    path = next(
        (
            p
            for p in (".github/dependabot.yml", ".github/dependabot.yaml")
            if repo.exists(p)
        ),
        None,
    )
    if path is None:
        return failed("no .github/dependabot.yml")
    updates = (repo.read_yaml(path) or {}).get("updates") or []
    if not any(u.get("package-ecosystem") == "github-actions" for u in updates):
        return failed(f"no github-actions updates in {path}")
    return passed()


@group.info("The project has Sphinx docs (docs/conf.py).")
def has_sphinx_docs(repo: Repo) -> bool:
    return repo.has_sphinx_docs


@group.check("Code examples in the docs are formatted with blacken-docs.")
def blacken_docs(repo: Repo) -> Result:
    if not repo.has_sphinx_docs:
        return not_applicable("No Sphinx docs.")
    return _require_hooks(repo, "blacken-docs")


@group.check("The docs are linted with sphinx-lint.")
def sphinx_lint(repo: Repo) -> Result:
    if not repo.has_sphinx_docs:
        return not_applicable("No Sphinx docs.")
    return _require_hooks(repo, "sphinx-lint")
