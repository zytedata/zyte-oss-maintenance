from __future__ import annotations

import re

from oss_maint.core import Group, Repo, Result, failed, not_applicable, passed

group = Group("typing", "Typing", frozenset({"python"}))

# Type checkers: the regular expression that finds them in tox or CI
# workflows, and their pre-commit hook ID.
TYPE_CHECKERS = {
    "mypy": (re.compile(r"\bmypy\b"), "mypy"),
    "pyrefly": (re.compile(r"\bpyrefly\b"), "pyrefly-check"),
}
MYPY_STRICT_RE = re.compile(r"\bmypy\b.*\s--strict(?![\w-])")


TYPED_CLASSIFIER = "Typing :: Typed"


def _ships_py_typed(repo: Repo) -> bool:
    return any(
        not path.startswith(("tests/", "docs/")) for path in repo.glob("**/py.typed")
    )


@group.check("The package ships type hints (a py.typed marker).", tags={"released"})
def py_typed(repo: Repo) -> Result:
    return passed() if _ships_py_typed(repo) else failed("no py.typed file")


@group.check(
    f"A package with a py.typed marker has the '{TYPED_CLASSIFIER}' classifier.",
    tags={"released"},
)
def typed_classifier(repo: Repo) -> Result:
    if not _ships_py_typed(repo):
        return not_applicable("No py.typed file.")
    if TYPED_CLASSIFIER not in repo.classifiers:
        return failed(f"no '{TYPED_CLASSIFIER}' classifier")
    return passed()


def _runs(repo: Repo, checker: str) -> bool:
    regex, hook_id = TYPE_CHECKERS[checker]
    return hook_id in (repo.pre_commit_hook_ids or set()) or any(
        regex.search(s) for s in repo.ci_strings
    )


@group.check(
    f"A type checker ({' or '.join(TYPE_CHECKERS)}) runs in tox, CI workflows or "
    "pre-commit."
)
def type_checker(repo: Repo) -> Result:
    if any(_runs(repo, checker) for checker in TYPE_CHECKERS):
        return passed()
    return failed("no type checker found")


@group.info("mypy runs in tox, CI workflows or pre-commit.")
def mypy(repo: Repo) -> bool:
    return _runs(repo, "mypy")


@group.info("pyrefly runs in tox, CI workflows or pre-commit.")
def pyrefly(repo: Repo) -> bool:
    return _runs(repo, "pyrefly")


@group.check("mypy runs in strict mode: strict = true in its config, or --strict.")
def mypy_strict(repo: Repo) -> Result:
    if not _runs(repo, "mypy"):
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
