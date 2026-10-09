from __future__ import annotations

import re

from oss_maint.core import Group, Repo, Result, failed, not_applicable, passed

group = Group("typing", "Typing")

MYPY_RE = re.compile(r"\bmypy\b")
MYPY_STRICT_RE = re.compile(r"\bmypy\b.*\s--strict(?![\w-])")


TYPED_CLASSIFIER = "Typing :: Typed"


def _ships_py_typed(repo: Repo) -> bool:
    return any(
        not path.startswith(("tests/", "docs/")) for path in repo.glob("**/py.typed")
    )


@group.check("The package ships type hints (a py.typed marker).")
def py_typed(repo: Repo) -> Result:
    return passed() if _ships_py_typed(repo) else failed("no py.typed file")


@group.check(
    f"A package with a py.typed marker has the '{TYPED_CLASSIFIER}' classifier."
)
def typed_classifier(repo: Repo) -> Result:
    if not _ships_py_typed(repo):
        return not_applicable("No py.typed file.")
    if TYPED_CLASSIFIER not in repo.classifiers:
        return failed(f"no '{TYPED_CLASSIFIER}' classifier")
    return passed()


def _runs_mypy(repo: Repo) -> bool:
    return "mypy" in (repo.pre_commit_hook_ids or set()) or any(
        MYPY_RE.search(s) for s in repo.ci_strings
    )


@group.check("mypy runs in tox, CI workflows or pre-commit.")
def mypy(repo: Repo) -> Result:
    return passed() if _runs_mypy(repo) else failed("mypy not found")


@group.check("mypy runs in strict mode: strict = true in its config, or --strict.")
def mypy_strict(repo: Repo) -> Result:
    if not _runs_mypy(repo):
        return not_applicable("Does not run mypy.")
    mypy_config = (repo.pyproject or {}).get("tool", {}).get("mypy", {})
    if mypy_config.get("strict"):
        return passed()
    for path in ("mypy.ini", ".mypy.ini", "setup.cfg"):
        text = repo.read_text(path) or ""
        if re.search(r"^strict\s*=\s*true\b", text, re.MULTILINE | re.IGNORECASE):
            return passed()
    if any(MYPY_STRICT_RE.search(s) for s in repo.ci_strings):
        return passed()
    for hook in repo.pre_commit_hooks or []:
        if hook["id"] == "mypy" and "--strict" in (hook.get("args") or []):
            return passed()
    return failed("no strict = true in mypy config, and no --strict")
