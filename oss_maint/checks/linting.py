from __future__ import annotations

import re

from oss_maint.core import Group, Repo, Result, failed, not_applicable, passed

group = Group("linting", "Linting")

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


@group.info("A tox environment runs pylint.")
def pylint(repo: Repo) -> bool:
    return any(re.search(r"\bpylint\b", s) for s in repo.tox_strings)


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
