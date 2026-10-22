from __future__ import annotations

import configparser
import re
from typing import Any

from packaging.requirements import Requirement
from packaging.utils import canonicalize_name

from oss_maint.core import Group, Repo, Result, Status, failed, not_applicable, passed

group = Group("tests", "Tests and coverage", frozenset({"python"}))


def _codecov_report_types(repo: Repo) -> set[str]:
    """``report_type`` values of codecov/codecov-action steps."""
    return {
        (step.get("with") or {}).get("report_type", "coverage")
        for _, step in repo.workflow_steps()
        if step.get("uses", "").startswith("codecov/codecov-action@")
    }


@group.check("Test coverage is uploaded to Codecov in CI workflows.")
def codecov(repo: Repo) -> Result:
    if "coverage" in _codecov_report_types(repo):
        return passed()
    if any("codecov" in step.get("run", "") for _, step in repo.workflow_steps()):
        return passed()
    return failed("no codecov/codecov-action step for coverage")


@group.check(
    "Test results are uploaded to Codecov in CI workflows "
    "(codecov/codecov-action with report_type: test_results)."
)
def codecov_test_results(repo: Repo) -> Result:
    if "test_results" in _codecov_report_types(repo):
        return passed()
    return failed("no codecov/codecov-action step with report_type: test_results")


# Organizations where Codecov does not allow tokenless uploads, which use OIDC
# instead of a token secret.
CODECOV_OIDC_ORGS = frozenset({"scrapinghub"})


def _env(data: dict[str, Any]) -> dict[str, Any]:
    """The env of a workflow, job or step, empty if it is an expression."""
    env = data.get("env")
    return env if isinstance(env, dict) else {}


def _codecov_auth(
    workflow: dict[Any, Any], job: dict[str, Any], step: dict[str, Any]
) -> str | None:
    """How *step* authenticates to Codecov: "OIDC", "token" or "tokenless",
    or None if it does not upload to Codecov. Steps that run commands only
    count with a token, as they may only install codecov."""
    token = {**_env(workflow), **_env(job), **_env(step)}.get("CODECOV_TOKEN")
    if step.get("uses", "").startswith("codecov/codecov-action@"):
        with_ = step.get("with") or {}
        if str(with_.get("use_oidc")).lower() == "true":
            return "OIDC"
        return "token" if with_.get("token") or token else "tokenless"
    run = step.get("run", "")
    if "codecov" in run and (token or "CODECOV_TOKEN" in run):
        return "token"
    return None


def _id_token_write(workflow: dict[Any, Any], job: dict[str, Any]) -> bool:
    # Job permissions replace those of the workflow.
    permissions = job.get("permissions", workflow.get("permissions"))
    if permissions == "write-all":
        return True
    return isinstance(permissions, dict) and permissions.get("id-token") == "write"


@group.check(
    "Codecov uploads use OIDC (use_oidc: true, with id-token: write permission) "
    f"in {', '.join(sorted(CODECOV_OIDC_ORGS))}, where tokenless uploads are not "
    "allowed, and are tokenless elsewhere."
)
def codecov_auth(repo: Repo) -> Result:
    expected = "OIDC" if repo.name.split("/")[0] in CODECOV_OIDC_ORGS else "tokenless"
    auths: dict[str, set[str]] = {}
    no_id_token = set()
    for path, workflow in repo.workflows.items():
        for job in (workflow.get("jobs") or {}).values():
            for step in job.get("steps") or []:
                auth = _codecov_auth(workflow, job, step)
                if auth is None:
                    continue
                auths.setdefault(auth, set()).add(path)
                if auth == "OIDC" and not _id_token_write(workflow, job):
                    no_id_token.add(path)
    if not auths:
        return not_applicable("Nothing is uploaded to Codecov.")
    problems = []
    if wrong := [
        f"{auth} in {', '.join(sorted(paths))}"
        for auth, paths in sorted(auths.items())
        if auth != expected
    ]:
        problems.append(f"expected {expected}, found {' and '.join(wrong)}")
    if no_id_token:
        problems.append(
            f"no id-token: write for OIDC in {', '.join(sorted(no_id_token))}"
        )
    if problems:
        return failed("; ".join(problems))
    return passed()


CODECOV_CONFIGS = [
    f"{d}{n}.{e}"
    for d in ("", ".github/")
    for n in ("codecov", ".codecov")
    for e in ("yml", "yaml")
]


@group.check(
    "The Codecov config disables the patch status and sets a 100% target for "
    "the project status."
)
def codecov_status(repo: Repo) -> Result:
    if codecov(repo).status is not Status.PASS:
        return not_applicable("Coverage is not uploaded to Codecov.")
    path = next((p for p in CODECOV_CONFIGS if repo.exists(p)), None)
    if path is None:
        return failed("no Codecov config")
    status = ((repo.read_yaml(path) or {}).get("coverage") or {}).get("status") or {}
    problems = []
    if status.get("patch") is not False:
        problems.append("patch status not disabled")
    project = status.get("project")
    if not (
        isinstance(project, dict)
        and project
        and all(
            str((s or {}).get("target", "")).rstrip("%") == "100"
            for s in project.values()
        )
    ):
        problems.append("project status target not 100%")
    if problems:
        return failed(f"{', '.join(problems)} in {path}")
    return passed()


@group.check("Branch coverage is enabled.")
def branch_coverage(repo: Repo) -> Result:
    coverage = (repo.pyproject or {}).get("tool", {}).get("coverage", {})
    if coverage.get("run", {}).get("branch"):
        return passed()
    for path, section in (
        (".coveragerc", "run"),
        ("setup.cfg", "coverage:run"),
        ("tox.ini", "coverage:run"),
    ):
        config = configparser.ConfigParser(interpolation=None)
        config.read_string(repo.read_text(path) or "")
        if config.getboolean(section, "branch", fallback=False):
            return passed()
    pytest_config = [
        str((repo.pyproject or {}).get("tool", {}).get("pytest", {})),
        repo.read_text("pytest.ini") or "",
        repo.read_text("setup.cfg") or "",
        *repo.ci_strings,
    ]
    if any("--cov-branch" in s for s in pytest_config):
        return passed()
    return failed("no branch = true in coverage config, and no --cov-branch")


def _pytest_option(repo: Repo, name: str) -> list[str]:
    """Values of the *name* pytest option in any pytest configuration, as
    lines or list items."""
    values: list[Any] = []
    pytest = (repo.pyproject or {}).get("tool", {}).get("pytest", {})
    for config in (
        pytest.get("ini_options", pytest),
        (repo.read_toml("pytest.toml") or {}).get("pytest", {}),
        (repo.read_toml(".pytest.toml") or {}).get("pytest", {}),
    ):
        value = config.get(name, [])
        values.extend(value.splitlines() if isinstance(value, str) else value)
    for path, section in (
        ("pytest.ini", "pytest"),
        (".pytest.ini", "pytest"),
        ("tox.ini", "pytest"),
        ("setup.cfg", "tool:pytest"),
    ):
        config = configparser.ConfigParser(interpolation=None, strict=False)
        config.read_string(repo.read_text(path) or "")
        values.extend(config.get(section, name, fallback="").splitlines())
    return [str(v).strip() for v in values]


@group.check(
    'pytest turns warnings into errors: "error" in filterwarnings, or -W error.'
)
def warnings_as_errors(repo: Repo) -> Result:
    if "error" in _pytest_option(repo, "filterwarnings"):
        return passed()
    w_error = re.compile(r"-W\s*error(?![\w:])")
    if any(
        w_error.search(s) for s in [*_pytest_option(repo, "addopts"), *repo.ci_strings]
    ):
        return passed()
    return failed('no "error" in pytest filterwarnings, and no -W error')


# Installs of Scrapy from its master branch: a GitHub URL without a ref or with
# @master, or a master branch archive.
SCRAPY_MASTER_RE = re.compile(
    r"github\.com/scrapy/scrapy(\.git)?"
    r"(@master|/archive/(refs/heads/)?master\.\w+(\.\w+)?)?(?![\w./@-])"
)
# Scrapy in the install_requires of setup.py.
SETUP_PY_SCRAPY_RE = re.compile(r"[\"'][Ss]crapy\s*[\[<>=~!;\"']")


def _depends_on_scrapy(repo: Repo) -> bool:
    if not repo.project:
        return bool(SETUP_PY_SCRAPY_RE.search(repo.read_text("setup.py") or ""))
    requirements = [
        *repo.project.get("dependencies", []),
        *(
            r
            for extra in repo.project.get("optional-dependencies", {}).values()
            for r in extra
        ),
    ]
    return any(canonicalize_name(Requirement(r).name) == "scrapy" for r in requirements)


@group.check("CI tests against Scrapy installed from its master branch.")
def scrapy_master(repo: Repo) -> Result:
    if not _depends_on_scrapy(repo):
        return not_applicable("Does not depend on Scrapy.")
    if any(SCRAPY_MASTER_RE.search(s) for s in repo.workflow_strings):
        return passed()
    envs = [
        name
        for name, strings in repo.tox_envs.items()
        if any(SCRAPY_MASTER_RE.search(s) for s in strings)
    ]
    if any(repo.tox_env_in_ci(env) for env in envs):
        return passed()
    if envs:
        return failed(
            "tox environments that install Scrapy master are not run in CI: "
            + ", ".join(envs)
        )
    return failed("no CI workflow or tox environment installs Scrapy master")
