"""Types and helpers that checks use."""

from __future__ import annotations

import re
import subprocess
import tomllib
from collections import Counter
from dataclasses import dataclass, field
from enum import Enum
from functools import cached_property
from typing import TYPE_CHECKING, Any

import yaml

if TYPE_CHECKING:
    from collections.abc import Callable, Iterator
    from pathlib import Path

    CheckFunc = Callable[["Repo"], "Result"]
    InfoFunc = Callable[["Repo"], bool | str | None]
    FactFunc = Callable[[], str]


class Status(Enum):
    PASS = "pass"  # noqa: S105
    FAIL = "fail"
    NA = "n/a"
    ERROR = "error"
    # Results of informational checks.
    YES = "yes"
    NO = "no"


# Statuses of checks that pass or fail, as opposed to N/A or informational.
APPLICABLE = (Status.PASS, Status.FAIL, Status.ERROR)


def tally(check: Check, results: list[Result]) -> str:
    """Summarize the results of *check* across projects, e.g. "3/5 passing"
    or, for informational checks, "2/5 yes" or "MIT (3), BSD-3-Clause (2)"."""
    statuses = [r.status for r in results]
    if check.informational:
        if values := Counter(r.value for r in results if r.value):
            if no := statuses.count(Status.NO):
                values["no"] = no
            return ", ".join(f"{value} ({n})" for value, n in values.most_common())
        answered = statuses.count(Status.YES) + statuses.count(Status.NO)
        return f"{statuses.count(Status.YES)}/{answered} yes"
    applicable = sum(statuses.count(s) for s in APPLICABLE)
    return f"{statuses.count(Status.PASS)}/{applicable} passing"


@dataclass(frozen=True)
class Result:
    status: Status
    #: Why the check did not pass, or a note worth reading even if it did.
    detail: str = ""
    #: For informational checks that report a value rather than yes or no.
    value: str = ""


def passed(detail: str = "") -> Result:
    return Result(Status.PASS, detail)


def failed(detail: str) -> Result:
    return Result(Status.FAIL, detail)


def not_applicable(detail: str) -> Result:
    return Result(Status.NA, detail)


@dataclass(frozen=True)
class Check:
    #: Function name, without trailing underscores and with underscores
    #: replaced by hyphens.
    id: str
    #: Describes the up-to-date state, true if the check passes. For
    #: informational checks, a fact that is true or not.
    statement: str
    func: CheckFunc
    #: Whether the check reports a fact (yes or no) rather than passing or
    #: failing.
    informational: bool = False

    def run(self, repo: Repo) -> Result:
        try:
            return self.func(repo)
        except Exception as e:
            return Result(Status.ERROR, f"{type(e).__name__}: {e}")


@dataclass(frozen=True)
class Fact:
    """A value that checks compare projects against, e.g. the latest Python
    version, reported once rather than per project."""

    #: What the value is, e.g. "Latest Python".
    label: str
    func: FactFunc

    def run(self) -> str:
        try:
            return self.func()
        except Exception as e:
            return f"error: {type(e).__name__}: {e}"


@dataclass
class Group:
    """Related checks, reported together."""

    id: str
    title: str
    checks: list[Check] = field(default_factory=list)
    facts: list[Fact] = field(default_factory=list)

    def check(self, statement: str) -> Callable[[CheckFunc], CheckFunc]:
        """Decorator that adds a check function to the group."""

        def decorator(func: CheckFunc) -> CheckFunc:
            self.checks.append(Check(_check_id(func), statement, func))
            return func

        return decorator

    def info(self, statement: str) -> Callable[[InfoFunc], InfoFunc]:
        """Decorator that adds an informational check function to the group.
        The function returns whether *statement* is true, or a value that
        *statement* describes, None if there is none."""

        def decorator(func: InfoFunc) -> InfoFunc:
            def run(repo: Repo) -> Result:
                value = func(repo)
                if isinstance(value, str):
                    return Result(Status.YES, value=value)
                return Result(Status.YES if value else Status.NO)

            self.checks.append(
                Check(_check_id(func), statement, run, informational=True)
            )
            return func

        return decorator

    def fact(self, label: str) -> Callable[[FactFunc], FactFunc]:
        """Decorator that adds a fact, a function returning the value that
        *label* describes, to the group."""

        def decorator(func: FactFunc) -> FactFunc:
            self.facts.append(Fact(label, func))
            return func

        return decorator


def _check_id(func: Callable[..., object]) -> str:
    # A trailing underscore avoids shadowing builtins, e.g. license_().
    return func.__name__.rstrip("_").replace("_", "-")


_PYTHON_CLASSIFIER_RE = re.compile(r"^Programming Language :: Python :: (\d+\.\d+)$")
PYPY_CLASSIFIER = "Programming Language :: Python :: Implementation :: PyPy"

# CPython versions in CI configuration: "3.14", "3.15.0-rc.1", "3.14t" (but not
# "pypy3.11" or ">=3.10"), tox's "py314" and "python3.14". The first group is
# the minor version.
_CI_PYTHON_RES = [
    re.compile(r"(?<![\w.<>=~!-])3\.(\d+)(?!\d)"),
    re.compile(r"\bpy3(\d{1,2})\b"),
    re.compile(r"\bpython3\.(\d+)"),
]
# PyPy versions: "pypy3.11", "pypy-3.11", "pypy3.11-v7.3.20", tox's "pypy311".
_CI_PYPY_RES = [
    re.compile(r"\bpypy-?3\.(\d+)"),
    re.compile(r"\bpypy3(\d{2})\b"),
]
# Any PyPy 3, including tox's unversioned "pypy3".
_CI_ANY_PYPY_RE = re.compile(r"\bpypy-?3")


def _strings(data: Any) -> Iterator[str]:
    """Yield all keys and scalar values in parsed YAML or TOML *data*."""
    if isinstance(data, dict):
        for key, value in data.items():
            yield from _strings(key)
            yield from _strings(value)
    elif isinstance(data, list):
        for value in data:
            yield from _strings(value)
        # Commands in TOML are lists of arguments.
        if data and all(isinstance(value, str) for value in data):
            yield " ".join(data)
    elif isinstance(data, str | int | float) and not isinstance(data, bool):
        yield str(data)


class Repo:
    """A read-only checkout of the default branch of a project repository."""

    def __init__(self, name: str, path: Path) -> None:
        #: GitHub "owner/name".
        self.name = name
        self.path = path

    @property
    def url(self) -> str:
        return f"https://github.com/{self.name}"

    @cached_property
    def sha(self) -> str:
        return subprocess.run(
            ["git", "-C", str(self.path), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()

    # Files

    def exists(self, path: str) -> bool:
        return (self.path / path).exists()

    def read_text(self, path: str) -> str | None:
        try:
            return (self.path / path).read_text(encoding="utf-8")
        except FileNotFoundError:
            return None

    def read_toml(self, path: str) -> dict[str, Any] | None:
        text = self.read_text(path)
        return None if text is None else tomllib.loads(text)

    def read_yaml(self, path: str) -> Any:
        text = self.read_text(path)
        return None if text is None else yaml.safe_load(text)

    def glob(self, pattern: str) -> list[str]:
        """Return sorted relative paths matching *pattern*, ignoring .git."""
        return sorted(
            str(p.relative_to(self.path))
            for p in self.path.glob(pattern)
            if ".git" not in p.relative_to(self.path).parts
        )

    # Packaging

    @cached_property
    def pyproject(self) -> dict[str, Any] | None:
        return self.read_toml("pyproject.toml")

    @property
    def project(self) -> dict[str, Any]:
        """The ``[project]`` table of pyproject.toml, empty if missing."""
        return (self.pyproject or {}).get("project", {})

    @cached_property
    def requires_python(self) -> str | None:
        """requires-python from pyproject.toml, or python_requires from
        setup.py or setup.cfg."""
        if "requires-python" in self.project:
            return self.project["requires-python"]
        for path, pattern in (
            ("setup.py", r"python_requires\s*=\s*[\"']([^\"']+)[\"']"),
            ("setup.cfg", r"^python_requires\s*=\s*(.+?)\s*$"),
        ):
            text = self.read_text(path) or ""
            if m := re.search(pattern, text, re.MULTILINE):
                return m.group(1)
        return None

    @cached_property
    def classifiers(self) -> list[str]:
        """Trove classifiers from pyproject.toml, or scraped from setup.py or
        setup.cfg."""
        if "classifiers" in self.project:
            return self.project["classifiers"]
        text = (self.read_text("setup.py") or "") + (self.read_text("setup.cfg") or "")
        return re.findall(
            r"^[\s\"']*(\w[\w ]* :: [^\"'\n]+?)[\"',]*\s*$", text, re.MULTILINE
        )

    @cached_property
    def classifier_python_versions(self) -> set[str]:
        """Python versions, e.g. ``"3.12"``, listed in classifiers."""
        return {
            m.group(1)
            for c in self.classifiers
            if (m := _PYTHON_CLASSIFIER_RE.match(c))
        }

    @property
    def has_sphinx_docs(self) -> bool:
        return self.exists("docs/conf.py")

    @property
    def supports_pypy(self) -> bool:
        """Whether PyPy is declared as supported or tested in CI."""
        return PYPY_CLASSIFIER in self.classifiers or any(
            _CI_ANY_PYPY_RE.search(s) for s in self.ci_strings
        )

    # Tooling

    @cached_property
    def pre_commit_hooks(self) -> list[dict[str, Any]] | None:
        """Hooks in .pre-commit-config.yaml, None if there is no such file."""
        config = self.read_yaml(".pre-commit-config.yaml")
        if config is None:
            return None
        return [
            hook
            for repo in config.get("repos") or []
            for hook in repo.get("hooks") or []
        ]

    @property
    def pre_commit_hook_ids(self) -> set[str] | None:
        """IDs of hooks in .pre-commit-config.yaml, None if there is no such
        file."""
        if self.pre_commit_hooks is None:
            return None
        return {hook["id"] for hook in self.pre_commit_hooks}

    @cached_property
    def workflows(self) -> dict[str, dict[Any, Any]]:
        """Parsed GitHub Actions workflows, by relative path."""
        return {
            path: self.read_yaml(path) or {}
            for path in self.glob(".github/workflows/*.y*ml")
        }

    def workflow_steps(self) -> Iterator[tuple[str, dict[str, Any]]]:
        """``(workflow path, step)`` for every step of every workflow job."""
        for path, workflow in self.workflows.items():
            for job in (workflow.get("jobs") or {}).values():
                for step in job.get("steps") or []:
                    yield path, step

    @cached_property
    def workflow_strings(self) -> list[str]:
        """Keys and values from GitHub Actions workflows."""
        return [s for workflow in self.workflows.values() for s in _strings(workflow)]

    @cached_property
    def tox_strings(self) -> list[str]:
        """Keys and values from tox configuration, or lines of tox.ini, without
        comments. Lists of strings, e.g. TOML commands, are also joined with
        spaces."""
        strings = list(_strings(self.read_toml("tox.toml") or {}))
        strings.extend(_strings((self.pyproject or {}).get("tool", {}).get("tox", {})))
        strings.extend(
            line
            for line in (self.read_text("tox.ini") or "").splitlines()
            if not line.lstrip().startswith(("#", ";"))
        )
        return strings

    @cached_property
    def ci_strings(self) -> list[str]:
        """:attr:`workflow_strings` and :attr:`tox_strings`."""
        return self.workflow_strings + self.tox_strings

    @cached_property
    def ci_python_versions(self) -> set[str]:
        """CPython versions, e.g. ``"3.14"``, mentioned in CI configuration."""
        return {
            f"3.{m.group(1)}"
            for s in self.ci_strings
            for regex in _CI_PYTHON_RES
            for m in regex.finditer(s)
        }

    @cached_property
    def ci_pypy_versions(self) -> set[str]:
        """Python versions of PyPy, e.g. ``"3.11"``, mentioned in CI
        configuration."""
        return {
            f"3.{m.group(1)}"
            for s in self.ci_strings
            for regex in _CI_PYPY_RES
            for m in regex.finditer(s)
        }
