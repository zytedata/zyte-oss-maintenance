from __future__ import annotations

from datetime import UTC, datetime
from textwrap import dedent
from typing import TYPE_CHECKING

import pytest

from oss_maint import github, pythons
from oss_maint.checks import GROUPS, select_groups
from oss_maint.core import PYPY_CLASSIFIER, Fact, Repo, Result, Status, tally

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

    MakeRepo = Callable[[dict[str, str]], Repo]

CHECKS = {c.id: c for g in GROUPS for c in g.checks}


@pytest.fixture
def make_repo(tmp_path: Path) -> MakeRepo:
    def make_repo(files: dict[str, str]) -> Repo:
        for path, content in files.items():
            (tmp_path / path).parent.mkdir(parents=True, exist_ok=True)
            (tmp_path / path).write_text(dedent(content), encoding="utf-8")
        return Repo("owner/name", tmp_path)

    return make_repo


def run(check_id: str, repo: Repo) -> Result:
    return CHECKS[check_id].run(repo)


def test_every_check_has_a_statement() -> None:
    assert CHECKS
    for check in CHECKS.values():
        assert check.statement.endswith(".")


def test_facts() -> None:
    facts = {f.label: f.run() for g in GROUPS for f in g.facts}
    assert facts == {
        "Latest Python": "3.11",
        "Upcoming Python, with a release candidate": "3.12",
        "Supported Python versions, with EOL dates": "3.10 (2099-10-31), 3.11 (2099-10-31)",
        "Python versions of the latest PyPy release": "3.10, 3.11",
        "End-of-life PyPy Python versions": "3.9",
        "Latest sphinx-scrapy": "0.13.0",
        "Minimum pre-commit hook versions, the newest releases at least 180 days old": (
            "ruff 0.16.0, zizmor 1.1.0"
        ),
    }


def test_fact_error() -> None:
    fact = Fact("Broken", lambda: str(1 / 0))
    assert fact.run() == "error: ZeroDivisionError: division by zero"


def test_select_groups() -> None:
    groups = select_groups(["python-versions", "ruff"])
    assert [g.id for g in groups] == ["python-versions", "linting"]
    assert [c.id for c in groups[0].checks] == [c.id for c in GROUPS[0].checks]
    assert [c.id for c in groups[1].checks] == ["ruff"]
    with pytest.raises(ValueError, match="unknown checks: foo"):
        select_groups(["foo"])


@pytest.mark.parametrize(
    ("requires_python", "status"),
    [
        (">=3.9", Status.FAIL),
        (">=3.9.2", Status.FAIL),
        (">=3.10", Status.PASS),
        ("~=3.10", Status.PASS),
    ],
)
def test_no_eol_python_requires_python(
    make_repo: MakeRepo, requires_python: str, status: Status
) -> None:
    repo = make_repo(
        {"pyproject.toml": f'[project]\nrequires-python = "{requires_python}"\n'}
    )
    assert run("no-eol-python", repo).status is status


def test_no_eol_python_classifiers(make_repo: MakeRepo) -> None:
    repo = make_repo(
        {
            "pyproject.toml": """\
                [project]
                requires-python = ">=3.10"
                classifiers = ["Programming Language :: Python :: 3.9"]
            """
        }
    )
    result = run("no-eol-python", repo)
    assert result.status is Status.FAIL
    assert "classifiers list 3.9" in result.detail


def test_no_eol_python_setup_py(make_repo: MakeRepo) -> None:
    repo = make_repo({"setup.py": "setup(python_requires='>=3.9')\n"})
    assert run("no-eol-python", repo).status is Status.FAIL


def test_latest_python(make_repo: MakeRepo) -> None:
    files = {
        "pyproject.toml": """\
            [project]
            requires-python = ">=3.10"
            classifiers = ["Programming Language :: Python :: 3.11"]
        """,
        ".github/workflows/test.yml": "python-version: ['pypy3.11']\n",
    }
    result = run("latest-python", make_repo(files))
    assert result.status is Status.FAIL
    assert "not found in CI" in result.detail

    files["tox.ini"] = "[tox]\nenvlist = py310,py311\n"
    assert run("latest-python", make_repo(files)).status is Status.PASS


@pytest.mark.parametrize(
    ("workflow", "status"),
    [
        (
            """\
            permissions:
              id-token: write
            jobs:
              publish:
                environment: pypi
                steps:
                - uses: pypa/gh-action-pypi-publish@release/v1
            """,
            Status.PASS,
        ),
        (
            """\
            permissions:
              id-token: write
            jobs:
              publish:
                steps:
                - uses: pypa/gh-action-pypi-publish@release/v1
            """,
            Status.FAIL,
        ),
        (
            """\
            permissions:
              id-token: write
            jobs:
              publish:
                # Job-level permissions replace workflow-level ones.
                permissions:
                  contents: read
                steps:
                - uses: pypa/gh-action-pypi-publish@release/v1
            """,
            Status.FAIL,
        ),
        (
            """\
            jobs:
              publish:
                permissions:
                  id-token: write
                steps:
                - uses: pypa/gh-action-pypi-publish@release/v1
                  with:
                    password: ${{ secrets.PYPI_TOKEN }}
            """,
            Status.FAIL,
        ),
        (
            "jobs:\n  publish:\n    steps:\n    - run: twine upload dist/*\n",
            Status.FAIL,
        ),
    ],
)
def test_trusted_publishing(make_repo: MakeRepo, workflow: str, status: Status) -> None:
    repo = make_repo({".github/workflows/publish.yml": workflow})
    assert run("trusted-publishing", repo).status is status


@pytest.mark.parametrize(
    ("hooks", "status"),
    [
        (["ruff-check", "ruff-format"], Status.PASS),
        (["ruff", "ruff-format"], Status.PASS),
        (["ruff-check", "ruff-format", "black"], Status.FAIL),
        (["ruff-check"], Status.FAIL),
    ],
)
def test_ruff(make_repo: MakeRepo, hooks: list[str], status: Status) -> None:
    config = "repos:\n- repo: x\n  hooks:\n" + "".join(f"  - id: {h}\n" for h in hooks)
    repo = make_repo({".pre-commit-config.yaml": config})
    assert run("ruff", repo).status is status


@pytest.mark.parametrize(
    ("project", "status"),
    [
        ('license = "BSD-3-Clause"', Status.PASS),
        (
            'license = "BSD-3-Clause"\nclassifiers = ["License :: OSI Approved :: BSD License"]',
            Status.FAIL,
        ),
        ('license = {text = "BSD"}', Status.FAIL),
        ('license = "Not SPDX"', Status.FAIL),
    ],
)
def test_pep639_license(make_repo: MakeRepo, project: str, status: Status) -> None:
    repo = make_repo({"pyproject.toml": f"[project]\n{project}\n"})
    assert run("pep639-license", repo).status is status


def test_check_error(make_repo: MakeRepo) -> None:
    repo = make_repo({"pyproject.toml": "not toml ["})
    assert run("hatchling", repo).status is Status.ERROR


@pytest.mark.parametrize("check_id", ["blacken-docs", "sphinx-lint"])
def test_docs_hooks(make_repo: MakeRepo, check_id: str) -> None:
    files = {".pre-commit-config.yaml": "repos: []\n"}
    assert run(check_id, make_repo(files)).status is Status.NA
    files["docs/conf.py"] = ""
    result = run(check_id, make_repo(files))
    assert result.status is Status.FAIL
    assert result.detail == f"missing pre-commit hooks: {check_id}"


def test_ci_versions(make_repo: MakeRepo) -> None:
    repo = make_repo(
        {
            ".github/workflows/test.yml": """\
                jobs:
                  test:
                    strategy:
                      matrix:
                        python-version: ["3.10", "3.12.0-rc.1", "pypy3.9"]
                        # "3.9"
                        include:
                        - python-version: pypy-3.10
                    steps:
                    - uses: actions/setup-python@v6
                      with:
                        python-version: ${{ matrix.python-version }}
                    - run: pip install 'foo>=3.8'
            """,
            "tox.ini": """\
                [tox]
                envlist = py311,pypy3
                # py37
                [testenv:pypy3]
                basepython = pypy3.11
            """,
        }
    )
    assert repo.ci_python_versions == {"3.10", "3.11", "3.12"}
    assert repo.ci_pypy_versions == {"3.9", "3.10", "3.11"}


def test_unreleased_python(
    make_repo: MakeRepo, monkeypatch: pytest.MonkeyPatch
) -> None:
    workflow = "jobs: {test: {steps: [{with: {python-version: '3.12.0-rc.1'}}]}}\n"
    repo = make_repo({".github/workflows/test.yml": workflow})
    assert run("unreleased-python", repo).status is Status.PASS
    monkeypatch.setattr(pythons, "upcoming_python", lambda: "3.13")
    assert run("unreleased-python", repo).status is Status.FAIL
    monkeypatch.setattr(pythons, "upcoming_python", lambda: None)
    assert run("unreleased-python", repo).status is Status.NA


@pytest.mark.parametrize(
    ("files", "supports", "latest", "no_eol"),
    [
        ({}, Status.NO, Status.NA, Status.NA),
        (
            {"tox.ini": "[tox]\nenvlist = pypy3\n"},
            Status.YES,
            Status.FAIL,
            Status.PASS,
        ),
        (
            {
                "pyproject.toml": f'[project]\nclassifiers = ["{PYPY_CLASSIFIER}"]\n',
                ".github/workflows/test.yml": "python-version: [pypy3.9, pypy3.11]\n",
            },
            Status.YES,
            Status.PASS,
            Status.FAIL,
        ),
    ],
)
def test_pypy(
    make_repo: MakeRepo,
    files: dict[str, str],
    supports: Status,
    latest: Status,
    no_eol: Status,
) -> None:
    repo = make_repo(files)
    assert run("supports-pypy", repo).status is supports
    assert run("latest-pypy", repo).status is latest
    assert run("no-eol-pypy", repo).status is no_eol


def test_tally() -> None:
    def results(*statuses: Status) -> list[Result]:
        return [Result(status) for status in statuses]

    statuses = [Status.PASS, Status.FAIL, Status.ERROR, Status.NA, Status.PASS]
    assert tally(CHECKS["ruff"], results(*statuses)) == "2/4 passing"
    statuses = [Status.YES, Status.NO, Status.NA, Status.YES]
    assert tally(CHECKS["supports-pypy"], results(*statuses)) == "2/3 yes"
    values = [
        Result(Status.YES, value="MIT"),
        Result(Status.NO),
        Result(Status.YES, value="BSD-3-Clause"),
        Result(Status.YES, value="MIT"),
    ]
    assert tally(CHECKS["license"], values) == "MIT (2), BSD-3-Clause (1), no (1)"
    values = [Result(Status.YES, value="1.0"), Result(Status.YES, value="2.0")]
    assert tally(CHECKS["latest-release"], [*values, Result(Status.NO)]) == "2/3 yes"


@pytest.mark.parametrize(
    ("on", "status"),
    [
        ("{push: {tags: ['v*']}}", Status.PASS),
        ("{release: {types: [published]}}", Status.FAIL),
        ("[push, release]", Status.FAIL),
        ("push", Status.FAIL),
        ("workflow_dispatch", Status.FAIL),
    ],
)
def test_publish_on_tag(make_repo: MakeRepo, on: str, status: Status) -> None:
    workflow = (
        f"on: {on}\n"
        "jobs: {publish: {steps: [{uses: pypa/gh-action-pypi-publish@release/v1}]}}\n"
    )
    repo = make_repo({".github/workflows/publish.yml": workflow})
    assert run("publish-on-tag", repo).status is status


def test_separate_build_job(make_repo: MakeRepo) -> None:
    workflow = """\
        jobs:
          build:
            steps:
            - run: python -m build
          publish:
            needs: [build]
            steps:
            - uses: actions/download-artifact@v5
            - uses: pypa/gh-action-pypi-publish@release/v1
    """
    repo = make_repo({".github/workflows/publish.yml": workflow})
    assert run("separate-build-job", repo).status is Status.PASS

    workflow = """\
        jobs:
          publish:
            steps:
            - uses: hynek/build-and-inspect-python-package@v2
            - uses: pypa/gh-action-pypi-publish@release/v1
    """
    repo = make_repo({".github/workflows/publish.yml": workflow})
    result = run("separate-build-job", repo)
    assert result.status is Status.FAIL
    assert (
        result.detail
        == ".github/workflows/publish.yml: job 'publish' builds and publishes"
    )


@pytest.mark.parametrize("check_id", ["publish-on-tag", "separate-build-job"])
def test_no_publishing(make_repo: MakeRepo, check_id: str) -> None:
    repo = make_repo({".github/workflows/test.yml": "jobs: {test: {steps: []}}\n"})
    result = run(check_id, repo)
    assert result.status is Status.FAIL
    assert result.detail == "no workflow publishes to PyPI"


@pytest.mark.parametrize(
    ("files", "value"),
    [
        ({"pyproject.toml": '[project]\nlicense = "MIT"\n'}, "MIT"),
        (
            {
                "pyproject.toml": (
                    "[project]\nlicense = {file = 'LICENSE'}\n"
                    'classifiers = ["License :: OSI Approved :: BSD License"]\n'
                )
            },
            "BSD License",
        ),
        ({"setup.py": "setup(license='BSD')\n"}, "BSD"),
        ({}, ""),
    ],
)
def test_license(make_repo: MakeRepo, files: dict[str, str], value: str) -> None:
    result = run("license", make_repo(files))
    assert result.value == value
    assert result.status is (Status.YES if value else Status.NO)


@pytest.mark.parametrize(
    ("files", "status"),
    [
        (
            {"tox.ini": "[testenv:twinecheck]\ncommands =\n    twine check dist/*\n"},
            Status.PASS,
        ),
        (
            {"tox.toml": '[env.twine]\ncommands = [["twine", "check", "dist/*"]]\n'},
            Status.PASS,
        ),
        ({"tox.ini": "# twine check dist/*\n"}, Status.FAIL),
        (
            {
                ".github/workflows/ci.yml": "jobs: {c: {steps: [{run: twine check dist/*}]}}\n"
            },
            Status.FAIL,
        ),
    ],
)
def test_twine_check(
    make_repo: MakeRepo, files: dict[str, str], status: Status
) -> None:
    assert run("twine-check", make_repo(files)).status is status


@pytest.mark.parametrize(
    ("files", "type_checker", "mypy", "pyrefly"),
    [
        ({}, Status.FAIL, Status.NO, Status.NO),
        (
            {"tox.ini": "[testenv:typing]\ncommands = mypy src\n"},
            Status.PASS,
            Status.YES,
            Status.NO,
        ),
        (
            {"tox.toml": '[env.typing]\ncommands = [["pyrefly", "check"]]\n'},
            Status.PASS,
            Status.NO,
            Status.YES,
        ),
        (
            {
                ".pre-commit-config.yaml": (
                    "repos:\n- repo: x\n  hooks:\n  - id: pyrefly-check\n"
                )
            },
            Status.PASS,
            Status.NO,
            Status.YES,
        ),
        (
            {
                "tox.ini": "[testenv:typing]\ncommands = mypy src\n",
                ".github/workflows/ci.yml": (
                    "jobs: {c: {steps: [{run: uvx pyrefly check}]}}\n"
                ),
            },
            Status.PASS,
            Status.YES,
            Status.YES,
        ),
    ],
)
def test_type_checker(
    make_repo: MakeRepo,
    files: dict[str, str],
    type_checker: Status,
    mypy: Status,
    pyrefly: Status,
) -> None:
    repo = make_repo(files)
    assert run("type-checker", repo).status is type_checker
    assert run("mypy", repo).status is mypy
    assert run("pyrefly", repo).status is pyrefly


@pytest.mark.parametrize(
    ("files", "status"),
    [
        ({}, Status.NA),
        ({"tox.toml": '[env.typing]\ncommands = [["pyrefly", "check"]]\n'}, Status.NA),
        ({"tox.ini": "[testenv:typing]\ncommands = mypy src\n"}, Status.FAIL),
        ({"tox.ini": "[testenv:typing]\ncommands = mypy --strict src\n"}, Status.PASS),
        (
            {"tox.toml": '[env.typing]\ncommands = [["mypy", "--strict", "src"]]\n'},
            Status.PASS,
        ),
        (
            {
                "tox.ini": "[testenv:typing]\ncommands = mypy src\n",
                "pyproject.toml": "[tool.mypy]\nstrict = true\n",
            },
            Status.PASS,
        ),
        (
            {
                ".pre-commit-config.yaml": (
                    "repos:\n- repo: x\n  hooks:\n  - id: mypy\n    args: [--strict]\n"
                )
            },
            Status.PASS,
        ),
    ],
)
def test_mypy_strict(
    make_repo: MakeRepo, files: dict[str, str], status: Status
) -> None:
    assert run("mypy-strict", make_repo(files)).status is status


@pytest.mark.parametrize(
    ("files", "status"),
    [
        ({"pyproject.toml": "[tool.coverage.run]\nbranch = true\n"}, Status.PASS),
        ({".coveragerc": "[run]\nbranch = True\n"}, Status.PASS),
        (
            {"tox.ini": "[testenv]\ncommands = pytest --cov=foo --cov-branch\n"},
            Status.PASS,
        ),
        ({".coveragerc": "[run]\nsource = foo\n"}, Status.FAIL),
    ],
)
def test_branch_coverage(
    make_repo: MakeRepo, files: dict[str, str], status: Status
) -> None:
    assert run("branch-coverage", make_repo(files)).status is status


def test_codecov(make_repo: MakeRepo) -> None:
    repo = make_repo({})
    assert run("codecov", repo).status is Status.FAIL
    assert run("codecov-test-results", repo).status is Status.FAIL

    workflow = """\
        jobs:
          test:
            steps:
            - uses: codecov/codecov-action@v5
              with:
                report_type: test_results
    """
    repo = make_repo({".github/workflows/test.yml": workflow})
    assert run("codecov", repo).status is Status.FAIL
    assert run("codecov-test-results", repo).status is Status.PASS

    workflow = workflow.rstrip(" ") + "            - uses: codecov/codecov-action@v5\n"
    repo = make_repo({".github/workflows/test.yml": workflow})
    assert run("codecov", repo).status is Status.PASS


@pytest.mark.parametrize(
    ("owner", "workflow", "result"),
    [
        (
            "owner",
            "jobs:\n  test:\n    steps:\n    - run: pip install codecov\n",
            Result(Status.NA, "Nothing is uploaded to Codecov."),
        ),
        (
            "owner",
            "jobs:\n  test:\n    steps:\n    - uses: codecov/codecov-action@v5\n",
            Result(Status.PASS),
        ),
        (
            "scrapinghub",
            "jobs:\n  test:\n    steps:\n    - uses: codecov/codecov-action@v5\n",
            Result(
                Status.FAIL,
                "expected OIDC, found tokenless in .github/workflows/test.yml",
            ),
        ),
        (
            "owner",
            """\
            jobs:
              test:
                steps:
                - uses: codecov/codecov-action@v5
                  with:
                    token: ${{ secrets.CODECOV_TOKEN }}
                - uses: codecov/codecov-action@v5
                  with:
                    report_type: test_results
            """,
            Result(
                Status.FAIL,
                "expected tokenless, found token in .github/workflows/test.yml",
            ),
        ),
        (
            "owner",
            """\
            env:
              CODECOV_TOKEN: ${{ secrets.CODECOV_TOKEN }}
            jobs:
              test:
                steps:
                - uses: codecov/codecov-action@v5
            """,
            Result(
                Status.FAIL,
                "expected tokenless, found token in .github/workflows/test.yml",
            ),
        ),
        (
            "owner",
            """\
            jobs:
              test:
                steps:
                - run: ./codecov
                  env:
                    CODECOV_TOKEN: ${{ secrets.CODECOV_TOKEN }}
            """,
            Result(
                Status.FAIL,
                "expected tokenless, found token in .github/workflows/test.yml",
            ),
        ),
        (
            "scrapinghub",
            """\
            permissions:
              contents: read
            jobs:
              test:
                permissions:
                  contents: read
                  id-token: write
                steps:
                - uses: codecov/codecov-action@v5
                  with:
                    use_oidc: true
            """,
            Result(Status.PASS),
        ),
        (
            "scrapinghub",
            """\
            permissions:
              id-token: write
            jobs:
              test:
                permissions:
                  contents: read
                steps:
                - uses: codecov/codecov-action@v5
                  with:
                    use_oidc: true
            """,
            Result(
                Status.FAIL,
                "no id-token: write for OIDC in .github/workflows/test.yml",
            ),
        ),
        (
            "owner",
            """\
            permissions:
              id-token: write
            jobs:
              test:
                steps:
                - uses: codecov/codecov-action@v5
                  with:
                    use_oidc: true
            """,
            Result(
                Status.FAIL,
                "expected tokenless, found OIDC in .github/workflows/test.yml",
            ),
        ),
    ],
)
def test_codecov_auth(
    make_repo: MakeRepo, owner: str, workflow: str, result: Result
) -> None:
    repo = make_repo({".github/workflows/test.yml": workflow})
    repo = Repo(f"{owner}/name", repo.path)
    assert run("codecov-auth", repo) == result


CODECOV_WORKFLOW = "jobs:\n  test:\n    steps:\n    - run: codecov\n"


@pytest.mark.parametrize(
    ("files", "result"),
    [
        ({}, Result(Status.NA, "Coverage is not uploaded to Codecov.")),
        (
            {".github/workflows/test.yml": CODECOV_WORKFLOW},
            Result(Status.FAIL, "no Codecov config"),
        ),
        (
            {
                ".github/workflows/test.yml": CODECOV_WORKFLOW,
                ".codecov.yml": (
                    "coverage:\n  status:\n    patch: false\n"
                    "    project:\n      default:\n        target: 100%\n"
                ),
            },
            Result(Status.PASS),
        ),
        (
            {
                ".github/workflows/test.yml": CODECOV_WORKFLOW,
                "codecov.yml": (
                    "coverage:\n  status:\n    project:\n"
                    "      a:\n        target: 100%\n      b:\n        target: 90%\n"
                ),
            },
            Result(
                Status.FAIL,
                "patch status not disabled, project status target not 100% in "
                "codecov.yml",
            ),
        ),
    ],
)
def test_codecov_status(
    make_repo: MakeRepo, files: dict[str, str], result: Result
) -> None:
    assert run("codecov-status", make_repo(files)) == result


@pytest.mark.parametrize(
    ("files", "status"),
    [
        (
            {"pyproject.toml": '[tool.bumpversion]\ncurrent_version = "1.0"\n'},
            Status.PASS,
        ),
        ({".bumpversion.toml": "[tool.bumpversion]\n"}, Status.PASS),
        ({".bumpversion.cfg": "[bumpversion]\n"}, Status.FAIL),
        ({}, Status.FAIL),
    ],
)
def test_bump_my_version(
    make_repo: MakeRepo, files: dict[str, str], status: Status
) -> None:
    assert run("bump-my-version", make_repo(files)).status is status


def test_project_urls(make_repo: MakeRepo) -> None:
    assert run("project-urls", make_repo({})).status is Status.NA
    repo = make_repo({"pyproject.toml": '[project]\nname = "x"\n'})
    assert run("project-urls", repo).status is Status.FAIL
    repo = make_repo({"pyproject.toml": '[project.urls]\nSource = "https://x"\n'})
    assert run("project-urls", repo) == Result(
        Status.FAIL, "missing URLs: issues, changelog"
    )
    repo = make_repo(
        {
            "pyproject.toml": (
                "[project.urls]\n"
                'Homepage = "https://github.com/owner/name/"\n'
                'Tracker = "https://github.com/owner/name/issues"\n'
                '"Release notes" = "https://x/news.html"\n'
            )
        }
    )
    assert run("project-urls", repo).status is Status.PASS
    (repo.path / "docs").mkdir()
    (repo.path / "docs/conf.py").write_text("")
    assert run("project-urls", repo) == Result(
        Status.FAIL, "missing URLs: documentation"
    )


@pytest.mark.parametrize(
    ("setup_cfg", "status"),
    [
        ("", Status.PASS),
        ("[flake8]\nmax-line-length = 88\n", Status.PASS),
        ("[metadata]\nname = x\n", Status.FAIL),
        ("[bdist_wheel]\nuniversal = 1\n", Status.FAIL),
        ("[options.packages.find]\nwhere = src\n", Status.FAIL),
    ],
)
def test_pyproject_metadata(
    make_repo: MakeRepo, setup_cfg: str, status: Status
) -> None:
    files = {"pyproject.toml": '[project]\nname = "x"\n'}
    if setup_cfg:
        files["setup.cfg"] = setup_cfg
    assert run("pyproject-metadata", make_repo(files)).status is status


@pytest.mark.parametrize(
    ("requires_python", "versions", "status", "detail"),
    [
        (">=3.10", ["3.10", "3.11"], Status.PASS, ""),
        (">=3.10", ["3.11"], Status.FAIL, "no classifiers for 3.10"),
        (
            ">=3.11",
            # Unreleased versions are allowed.
            ["3.10", "3.11", "3.12"],
            Status.FAIL,
            "classifiers for 3.10, which requires-python '>=3.11' excludes",
        ),
        (">=3.10", [], Status.FAIL, "no Python version classifiers"),
        (None, ["3.10"], Status.NA, "requires-python is not declared."),
    ],
)
def test_python_classifiers(
    make_repo: MakeRepo,
    requires_python: str | None,
    versions: list[str],
    status: Status,
    detail: str,
) -> None:
    classifiers = [f"Programming Language :: Python :: {v}" for v in versions]
    project = f"[project]\nclassifiers = {classifiers!r}\n"
    if requires_python:
        project += f'requires-python = "{requires_python}"\n'
    result = run("python-classifiers", make_repo({"pyproject.toml": project}))
    assert result == Result(status, detail)


def test_typed_classifier(make_repo: MakeRepo) -> None:
    files = {"pyproject.toml": '[project]\nclassifiers = ["Typing :: Typed"]\n'}
    assert run("typed-classifier", make_repo(files)).status is Status.NA
    files["pkg/py.typed"] = ""
    assert run("typed-classifier", make_repo(files)).status is Status.PASS
    files["pyproject.toml"] = "[project]\nclassifiers = []\n"
    assert run("typed-classifier", make_repo(files)).status is Status.FAIL


@pytest.mark.parametrize(
    ("dependencies", "status"),
    [
        (
            '["lxml>=5", "foo==1.0", "bar~=2.1", "baz>=1; python_version < \'3.12\'"]',
            Status.PASS,
        ),
        ('["lxml>=5", "foo", "bar<3"]', Status.FAIL),
        ("[]", Status.NA),
    ],
)
def test_dependency_lower_bounds(
    make_repo: MakeRepo, dependencies: str, status: Status
) -> None:
    repo = make_repo({"pyproject.toml": f"[project]\ndependencies = {dependencies}\n"})
    result = run("dependency-lower-bounds", repo)
    assert result.status is status
    if status is Status.FAIL:
        assert result.detail == "no lower bound: foo, bar"


@pytest.mark.parametrize(
    ("files", "status"),
    [
        ({"tox.ini": "[tox]\nenvlist = py310,min\n"}, Status.PASS),
        ({"tox.ini": "[testenv:py310-pinned]\n"}, Status.PASS),
        ({"tox.toml": '[env.min-extra]\ncommands = [["pytest"]]\n'}, Status.PASS),
        ({"tox.ini": "[tox]\nminversion = 4\nenvlist = py310\n"}, Status.FAIL),
    ],
)
def test_min_deps_env(
    make_repo: MakeRepo, files: dict[str, str], status: Status
) -> None:
    files["pyproject.toml"] = '[project]\ndependencies = ["lxml>=5"]\n'
    assert run("min-deps-env", make_repo(files)).status is status


def test_min_deps_env_no_dependencies(make_repo: MakeRepo) -> None:
    repo = make_repo({"pyproject.toml": '[project]\nname = "x"\n'})
    assert run("min-deps-env", repo).status is Status.NA


def test_pylint(make_repo: MakeRepo) -> None:
    assert (
        run("pylint", make_repo({"tox.ini": "[tox]\nenvlist = py310\n"})).status
        is Status.NO
    )
    repo = make_repo({"tox.ini": "[testenv:pylint]\ncommands = pylint src\n"})
    assert run("pylint", repo).status is Status.YES


SPHINX_SCRAPY_FILES = {
    "docs/conf.py": 'extensions = ["sphinx_scrapy"]\n',
    "tox.ini": "[tox]\nrequires =\n    sphinx-scrapy[tox]==0.13.0\n",
    ".pre-commit-config.yaml": """\
        repos:
        - repo: https://github.com/scrapy/sphinx-scrapy
          rev: 0.13.0
          hooks:
          - id: sphinx-scrapy
    """,
}


def test_sphinx_scrapy(make_repo: MakeRepo) -> None:
    assert run("sphinx-scrapy", make_repo({})).status is Status.NA
    repo = make_repo({"docs/conf.py": "extensions = []\n"})
    assert run("sphinx-scrapy", repo).status is Status.FAIL
    assert run("sphinx-scrapy-pins", repo).status is Status.NA
    assert run("no-docs-requirements", repo).status is Status.PASS
    repo = make_repo(SPHINX_SCRAPY_FILES)
    for check_id in (
        "no-docs-requirements",
        "sphinx-scrapy",
        "sphinx-scrapy-pins",
        "sphinx-scrapy-latest",
    ):
        assert run(check_id, repo).status is Status.PASS


def test_sphinx_scrapy_pins(make_repo: MakeRepo) -> None:
    repo = make_repo(
        {
            **SPHINX_SCRAPY_FILES,
            "tox.ini": "[tox]\nrequires =\n    sphinx-scrapy[tox]==0.8.4\n",
        }
    )
    result = run("sphinx-scrapy-pins", repo)
    assert result.status is Status.FAIL
    assert result.detail == (
        "different pins: 0.8.4 in tox, 0.13.0 in .pre-commit-config.yaml"
    )
    result = run("sphinx-scrapy-latest", repo)
    assert result.status is Status.FAIL
    assert result.detail == "pinned to 0.8.4, latest is 0.13.0"
    result = run(
        "sphinx-scrapy-pins", make_repo({**SPHINX_SCRAPY_FILES, "tox.ini": ""})
    )
    assert result.detail == "not pinned in tox"


def test_no_docs_requirements(make_repo: MakeRepo) -> None:
    repo = make_repo(
        {
            "docs/conf.py": "",
            "docs/requirements.in": "",
            "docs/requirements.txt": "",
        }
    )
    result = run("no-docs-requirements", repo)
    assert result.status is Status.FAIL
    assert result.detail == "found docs/requirements.in, docs/requirements.txt"


@pytest.mark.parametrize(
    ("files", "status"),
    [
        ({}, Status.NA),
        ({"pyproject.toml": "[tool.ruff.lint]\nextend-select = ['B']\n"}, Status.PASS),
        ({"ruff.toml": "[lint]\nselect = ['ALL']\n"}, Status.PASS),
        (
            {"pyproject.toml": "[tool.ruff.lint]\nselect = ['E4', 'E7', 'E9', 'F']\n"},
            Status.FAIL,
        ),
        (
            {
                ".pre-commit-config.yaml": "repos:\n- repo: x\n  hooks:\n  - id: ruff-check\n"
            },
            Status.FAIL,
        ),
    ],
)
def test_ruff_rules(make_repo: MakeRepo, files: dict[str, str], status: Status) -> None:
    assert run("ruff-rules", make_repo(files)).status is status


@pytest.mark.parametrize(
    ("name", "committed", "status"),
    [
        ("example", datetime(2026, 3, 5, tzinfo=UTC), Status.YES),
        ("example", datetime(2026, 3, 4, tzinfo=UTC), Status.NO),
        ("unpublished", datetime(2026, 3, 5, tzinfo=UTC), Status.NA),
    ],
)
def test_unreleased_changes(
    make_repo: MakeRepo, name: str, committed: datetime, status: Status
) -> None:
    repo = make_repo({"pyproject.toml": f'[project]\nname = "{name}"\n'})
    repo.__dict__["committed"] = committed
    assert run("unreleased-changes", repo).status is status


@pytest.mark.parametrize(
    ("files", "result"),
    [
        ({}, Result(Status.NA, "No .pre-commit-config.yaml.")),
        (
            {
                ".github/workflows/ci.yml": "jobs: {c: {steps: [{uses: pre-commit/action@v3}]}}\n"
            },
            Result(Status.PASS),
        ),
        (
            {
                "tox.ini": "[testenv:lint]\ncommands = pre-commit run --all-files\n",
                ".github/workflows/ci.yml": (
                    "jobs: {c: {strategy: {matrix: {toxenv: [mypy, lint]}}}}\n"
                ),
            },
            Result(Status.PASS),
        ),
        (
            {
                "tox.toml": '[env.pre-commit]\ncommands = [["pre-commit", "run"]]\n',
                ".github/workflows/ci.yml": "jobs: {c: {steps: [{run: tox -e py}]}}\n",
            },
            Result(
                Status.FAIL,
                "tox environments that run pre-commit are not run in CI: pre-commit",
            ),
        ),
        (
            {".github/workflows/ci.yml": "jobs: {c: {steps: [{run: tox -e py}]}}\n"},
            Result(Status.FAIL, "not run in CI workflows or tox"),
        ),
    ],
)
def test_pre_commit_in_ci(
    make_repo: MakeRepo, files: dict[str, str], result: Result
) -> None:
    if files:
        files[".pre-commit-config.yaml"] = "repos: []\n"
    assert run("pre-commit-in-ci", make_repo(files)) == result


def _pre_commit_config(*repos: tuple[str, str]) -> str:
    return "repos:\n" + "".join(
        f"- repo: {url}\n  rev: {rev}\n  hooks: []\n" for url, rev in repos
    )


def test_pre_commit_updates(make_repo: MakeRepo) -> None:
    assert run("pre-commit-updates", make_repo({})).status is Status.NA
    config = _pre_commit_config(
        ("https://github.com/astral-sh/ruff-pre-commit", "v0.15.0"),
        ("https://github.com/zizmorcore/zizmor-pre-commit.git", "v1.1.0"),
        # Not checked.
        ("https://github.com/rhysd/actionlint", "v0.1.0"),
    )
    result = run("pre-commit-updates", make_repo({".pre-commit-config.yaml": config}))
    assert result == Result(
        Status.FAIL, "outdated: ruff v0.15.0 (0.16.0 or later expected)"
    )
    config = _pre_commit_config(
        # Frozen revs are not checked.
        ("https://github.com/astral-sh/ruff-pre-commit", "0123abcd" * 5),
        ("https://github.com/zizmorcore/zizmor-pre-commit", "v1.0.0"),
    )
    result = run("pre-commit-updates", make_repo({".pre-commit-config.yaml": config}))
    assert result == Result(
        Status.FAIL, "outdated: zizmor v1.0.0 (1.1.0 or later expected)"
    )
    config = _pre_commit_config(
        ("https://github.com/astral-sh/ruff-pre-commit", "v0.16.1")
    )
    result = run("pre-commit-updates", make_repo({".pre-commit-config.yaml": config}))
    assert result.status is Status.PASS
    config = _pre_commit_config(("https://github.com/rhysd/actionlint", "v0.1.0"))
    result = run("pre-commit-updates", make_repo({".pre-commit-config.yaml": config}))
    assert result == Result(Status.NA, "No checked hooks.")


def test_dependabot(make_repo: MakeRepo) -> None:
    zizmor = "repos:\n- repo: x\n  hooks:\n  - id: zizmor\n"
    files = {".pre-commit-config.yaml": zizmor}
    assert run("dependabot", make_repo(files)).status is Status.NA
    files[".github/workflows/ci.yml"] = "jobs: {}\n"
    files[".pre-commit-config.yaml"] = "repos: []\n"
    assert run("dependabot", make_repo(files)).status is Status.NA
    files[".pre-commit-config.yaml"] = zizmor
    assert run("dependabot", make_repo(files)) == Result(
        Status.FAIL, "no .github/dependabot.yml"
    )
    files[".github/dependabot.yaml"] = "updates:\n- package-ecosystem: pip\n"
    assert run("dependabot", make_repo(files)) == Result(
        Status.FAIL, "no github-actions updates in .github/dependabot.yaml"
    )
    files[".github/dependabot.yaml"] += "- package-ecosystem: github-actions\n"
    assert run("dependabot", make_repo(files)).status is Status.PASS


@pytest.mark.parametrize(
    ("workflow", "status"),
    [
        ("on: release\n", Status.NA),
        ("on:\n  push:\n    tags: [v*]\n", Status.NA),
        ("on: [push]\n", Status.FAIL),
        ("on:\n  push:\n    branches: [main]\n    tags: [v*]\n", Status.FAIL),
        ("on: pull_request\nconcurrency: ci-${{ github.ref }}\n", Status.FAIL),
        (
            "on: pull_request\nconcurrency: {group: x, cancel-in-progress: true}\n",
            Status.PASS,
        ),
        (
            "on: pull_request\nconcurrency: {group: x, cancel-in-progress: false}\n",
            Status.PASS,
        ),
    ],
)
def test_workflow_concurrency(
    make_repo: MakeRepo, workflow: str, status: Status
) -> None:
    repo = make_repo({".github/workflows/ci.yml": workflow})
    result = run("workflow-concurrency", repo)
    assert result.status is status
    if status is Status.FAIL:
        assert result.detail == "no cancel-in-progress: .github/workflows/ci.yml"


@pytest.mark.parametrize(
    ("files", "detail"),
    [
        ({"pyproject.toml": "[tool.coverage.run]\nbranch = true\n"}, ""),
        (
            {".coveragerc": "", "requirements-dev.txt": ""},
            "legacy files: .coveragerc, requirements-dev.txt",
        ),
        (
            {
                "pyproject.toml": '[build-system]\nbuild-backend = "hatchling.build"\n',
                "MANIFEST.in": "",
            },
            "MANIFEST.in, which hatchling.build ignores",
        ),
        (
            {
                "pyproject.toml": '[build-system]\nbuild-backend = "setuptools.build_meta"\n',
                "MANIFEST.in": "",
            },
            "",
        ),
        (
            {
                "setup.cfg": "[metadata]\nname = x\n[flake8]\n[mypy-foo.*]\n",
                "tox.ini": "[tox]\n[base]\n[testenv:min]\n[pytest]\n",
            },
            (
                "tool sections in setup.cfg: [flake8], [mypy-foo.*]; "
                "tool sections in tox.ini: [pytest]"
            ),
        ),
    ],
)
def test_no_legacy_config(
    make_repo: MakeRepo, files: dict[str, str], detail: str
) -> None:
    result = run("no-legacy-config", make_repo(files))
    assert result == Result(Status.FAIL if detail else Status.PASS, detail)


@pytest.mark.parametrize(
    ("files", "status"),
    [
        (
            {
                "pyproject.toml": (
                    "[tool.pytest.ini_options]\nfilterwarnings = ['error', 'ignore::X']\n"
                )
            },
            Status.PASS,
        ),
        (
            {"pyproject.toml": "[tool.pytest]\nfilterwarnings = ['error']\n"},
            Status.PASS,
        ),
        (
            {"pytest.ini": "[pytest]\nfilterwarnings =\n    error\n    ignore::X\n"},
            Status.PASS,
        ),
        ({"tox.ini": "[testenv]\ncommands = pytest -W error {posargs}\n"}, Status.PASS),
        (
            {
                "pyproject.toml": "[tool.pytest]\nfilterwarnings = ['error::DeprecationWarning']\n"
            },
            Status.FAIL,
        ),
        (
            {"tox.ini": "[testenv]\ncommands = pytest -W error::UserWarning\n"},
            Status.FAIL,
        ),
        ({}, Status.FAIL),
    ],
)
def test_warnings_as_errors(
    make_repo: MakeRepo, files: dict[str, str], status: Status
) -> None:
    assert run("warnings-as-errors", make_repo(files)).status is status


@pytest.mark.parametrize(
    ("files", "value"),
    [
        ({"pyproject.toml": '[project]\nname = "example"\n'}, "1.1 (2026-03-04)"),
        ({"setup.py": "setup(\n    name='example',\n)\n"}, "1.1 (2026-03-04)"),
        ({"pyproject.toml": '[project]\nname = "unpublished"\n'}, ""),
        ({}, ""),
    ],
)
def test_latest_release(make_repo: MakeRepo, files: dict[str, str], value: str) -> None:
    result = run("latest-release", make_repo(files))
    assert result.value == value
    assert result.status is (Status.YES if value else Status.NO)


@pytest.mark.parametrize(
    ("files", "result"),
    [
        ({}, Result(Status.NA, "No .pre-commit-config.yaml.")),
        (
            {"tox.ini": "[testenv:lint]\ncommands = pre-commit run -a\n"},
            Result(Status.PASS),
        ),
        (
            {
                "tox.toml": (
                    '[env.pre-commit]\ncommands = [["pre-commit", "run", '
                    '{ replace = "posargs", default = ["--all-files"] }]]\n'
                )
            },
            Result(Status.PASS),
        ),
        (
            {"tox.ini": "[testenv:lint]\ncommands = pre-commit run {posargs}\n"},
            Result(Status.FAIL, "no tox environment runs pre-commit run --all-files"),
        ),
    ],
)
def test_pre_commit_tox(
    make_repo: MakeRepo, files: dict[str, str], result: Result
) -> None:
    if files:
        files[".pre-commit-config.yaml"] = "repos: []\n"
    assert run("pre-commit-tox", make_repo(files)) == result


def test_pre_commit_in_ci_pre_commit_ci(make_repo: MakeRepo) -> None:
    repo = make_repo(
        {".pre-commit-config.yaml": "ci:\n  autofix_prs: false\nrepos: []\n"}
    )
    assert run("pre-commit-in-ci", repo).status is Status.PASS


def test_pre_commit_hooks(make_repo: MakeRepo) -> None:
    assert run("pre-commit-hooks", make_repo({})).status is Status.NA
    config = _pre_commit_config(("https://github.com/astral-sh/ruff-pre-commit", "v1"))
    assert run("pre-commit-hooks", make_repo({".pre-commit-config.yaml": config})) == (
        Result(
            Status.FAIL,
            "https://github.com/pre-commit/pre-commit-hooks is not used",
        )
    )
    config = _pre_commit_config(
        ("https://github.com/pre-commit/pre-commit-hooks.git", "v6.0.0")
    )
    repo = make_repo({".pre-commit-config.yaml": config})
    assert run("pre-commit-hooks", repo).status is Status.PASS


HATCHLING = '[build-system]\nbuild-backend = "hatchling.build"\n'


@pytest.mark.parametrize(
    ("files", "result"),
    [
        (
            {
                "pyproject.toml": '[build-system]\nbuild-backend = "flit_core.buildapi"\n'
            },
            Result(Status.NA, "The build backend is not hatchling."),
        ),
        (
            {"pyproject.toml": HATCHLING},
            Result(Status.FAIL, "no include in [tool.hatch.build.targets.sdist]"),
        ),
        (
            {
                "pyproject.toml": HATCHLING
                + (
                    "[tool.hatch.build.targets.sdist]\n"
                    "include = ['/pkg', '/tests', 'docs/**', 'tox.ini']\n"
                    "exclude = ['/docs/_build']\n"
                ),
                "tests/test_a.py": "",
                "docs/conf.py": "",
                "tox.ini": "",
            },
            Result(Status.PASS),
        ),
        (
            {
                "pyproject.toml": HATCHLING
                + (
                    "[tool.hatch.build.targets.sdist]\n"
                    "only-include = ['/pkg', '/tests', '/docs']\n"
                    "exclude = ['/docs']\n"
                ),
                "tests/test_a.py": "",
                "docs/conf.py": "",
                "tox.toml": "",
            },
            Result(Status.FAIL, "not included: docs, tox.toml"),
        ),
    ],
)
def test_sdist_contents(
    make_repo: MakeRepo, files: dict[str, str], result: Result
) -> None:
    assert run("sdist-contents", make_repo(files)) == result


@pytest.mark.parametrize(
    ("files", "result"),
    [
        ({}, Result(Status.NA, "No Sphinx docs.")),
        (
            {
                ".readthedocs.yaml": "",
                "README.rst": "See https://name.readthedocs.io/en/latest/.\n",
            },
            Result(Status.PASS),
        ),
        (
            {
                "pyproject.toml": (
                    "[project.urls]\nDocumentation = 'https://docs.example.org/'\n"
                ),
                "README.md": "[Docs](https://docs.example.org/en/latest/)\n",
            },
            Result(Status.FAIL, "no .readthedocs.yml"),
        ),
        (
            {".readthedocs.yml": "", "README.rst": "https://other.readthedocs.io\n"},
            Result(
                Status.FAIL,
                "the README does not link to name.readthedocs.io or "
                "name.readthedocs.org",
            ),
        ),
    ],
)
def test_readthedocs(
    make_repo: MakeRepo, files: dict[str, str], result: Result
) -> None:
    if files:
        files["docs/conf.py"] = ""
    assert run("readthedocs", make_repo(files)) == result


@pytest.mark.parametrize(
    ("files", "result"),
    [
        ({"README.rst": ""}, Result(Status.FAIL, "no docs/conf.py")),
        ({"docs/conf.py": "", "docs/index.rst": ""}, Result(Status.PASS)),
        (
            {"docs/source/conf.py": "", "docs/guide/intro.md": ""},
            Result(Status.FAIL, "no docs/conf.py; Markdown files: docs/guide/intro.md"),
        ),
    ],
)
def test_sphinx_docs(
    make_repo: MakeRepo, files: dict[str, str], result: Result
) -> None:
    assert run("sphinx-docs", make_repo(files)) == result


@pytest.mark.parametrize(
    ("files", "result"),
    [
        ({"README.rst": "", "README.md": ""}, Result(Status.PASS)),
        ({"readme.md": ""}, Result(Status.FAIL, "readme.md instead")),
        ({}, Result(Status.FAIL, "no README")),
    ],
)
def test_readme_rst(make_repo: MakeRepo, files: dict[str, str], result: Result) -> None:
    assert run("readme-rst", make_repo(files)) == result


def test_no_wiki(make_repo: MakeRepo, monkeypatch: pytest.MonkeyPatch) -> None:
    repo = make_repo({})
    assert run("no-wiki", repo).status is Status.PASS
    monkeypatch.setattr(github, "has_wiki", {"owner/name"}.__contains__)
    assert run("no-wiki", repo) == Result(
        Status.FAIL, "https://github.com/owner/name/wiki has pages"
    )


@pytest.mark.parametrize(
    ("files", "status"),
    [
        ({"CHANGES.rst": ""}, Status.PASS),
        ({"Changelog.md": ""}, Status.PASS),
        ({"NEWS": ""}, Status.PASS),
        ({"docs/release-notes.rst": ""}, Status.PASS),
        ({"README.rst": "", "docs/index.rst": ""}, Status.FAIL),
    ],
)
def test_changelog(make_repo: MakeRepo, files: dict[str, str], status: Status) -> None:
    assert run("changelog", make_repo(files)).status is status


@pytest.mark.parametrize(
    ("files", "status"),
    [
        ({}, Status.NA),
        (
            {
                "pyproject.toml": (
                    "[tool.bumpversion]\n[[tool.bumpversion.files]]\n"
                    "filename = 'CHANGES.rst'\nsearch = '\\\\(unreleased\\\\)$'\n"
                    "replace = '({now:%Y-%m-%d})'\n"
                )
            },
            Status.PASS,
        ),
        (
            {
                ".bumpversion.toml": (
                    "[tool.bumpversion]\n[[tool.bumpversion.files]]\n"
                    "filename = 'CHANGES'\nsearch = '^Unreleased.$'\n"
                    "replace = 'Released on {now:%Y-%m-%d}.'\n"
                )
            },
            Status.PASS,
        ),
        (
            {
                "pyproject.toml": (
                    "[tool.bumpversion]\n[[tool.bumpversion.files]]\n"
                    "filename = 'pkg/__init__.py'\n"
                )
            },
            Status.FAIL,
        ),
    ],
)
def test_changelog_date(
    make_repo: MakeRepo, files: dict[str, str], status: Status
) -> None:
    assert run("changelog-date", make_repo(files)).status is status


SCRAPY_PROJECT = "[project]\ndependencies = ['scrapy>=2.13']\n"


@pytest.mark.parametrize(
    ("files", "result"),
    [
        (
            {"pyproject.toml": "[project]\ndependencies = ['scrapy-poet']\n"},
            Result(Status.NA, "Does not depend on Scrapy."),
        ),
        (
            {
                "pyproject.toml": (
                    "[project]\n[project.optional-dependencies]\nx = ['Scrapy']\n"
                ),
                ".github/workflows/ci.yml": (
                    "jobs: {c: {steps: [{run: "
                    "'pip install https://github.com/scrapy/scrapy/archive/master.zip'"
                    "}]}}\n"
                ),
            },
            Result(Status.PASS),
        ),
        (
            {
                "setup.py": "setup(install_requires=['Scrapy>=2.0'])\n",
                "tox.ini": (
                    "[testenv:scrapy-master]\n"
                    "deps = scrapy @ git+https://github.com/scrapy/scrapy@master\n"
                ),
                ".github/workflows/ci.yml": (
                    "jobs: {c: {steps: [{run: tox -e scrapy-master}]}}\n"
                ),
            },
            Result(Status.PASS),
        ),
        (
            {
                "pyproject.toml": SCRAPY_PROJECT,
                "tox.ini": (
                    "[testenv:vcs]\n"
                    "commands_pre = pip install git+https://github.com/scrapy/scrapy\n"
                ),
            },
            Result(
                Status.FAIL,
                "tox environments that install Scrapy master are not run in CI: vcs",
            ),
        ),
        (
            {
                "pyproject.toml": SCRAPY_PROJECT,
                "tox.ini": (
                    "[testenv:old]\n"
                    "deps = scrapy @ git+https://github.com/scrapy/scrapy@2.11\n"
                ),
            },
            Result(
                Status.FAIL, "no CI workflow or tox environment installs Scrapy master"
            ),
        ),
    ],
)
def test_scrapy_master(
    make_repo: MakeRepo, files: dict[str, str], result: Result
) -> None:
    assert run("scrapy-master", make_repo(files)) == result


def test_docs_stable_links(make_repo: MakeRepo) -> None:
    assert run("docs-stable-links", make_repo({})).status is Status.NA
    files = {
        "docs/conf.py": "",
        "README.rst": (
            "https://name.readthedocs.io/\n"
            "https://name.readthedocs.io/en/stable/?badge=stable\n"
            "https://other.readthedocs.io/en/latest/\n"
        ),
        "pyproject.toml": (
            "[project.urls]\nDocs = 'https://docs.example.org/en/stable/'\n"
        ),
    }
    assert run("docs-stable-links", make_repo(files)).status is Status.PASS
    files["README.rst"] += "https://name.readthedocs.io/en/latest/usage.html\n"
    files["pyproject.toml"] += (
        "Changes = 'https://docs.example.org/pt-br/1.0/news.html'\n"
    )
    assert run("docs-stable-links", make_repo(files)) == Result(
        Status.FAIL, "links to latest in README.rst; 1.0 in pyproject.toml"
    )


def test_pr_guard_trusted_users(make_repo: MakeRepo) -> None:
    assert run("pr-guard-trusted-users", make_repo({})).status is Status.NA
    workflow = """\
        jobs:
          guard:
            steps:
            - uses: scrapy/unattended-pr-guard@0123456789abcdef  # 0.2.0
              with:
                {orgs}
                trusted-users: >-
                  {users}
                  carol
        """
    path = ".github/workflows/guard.yml"
    repo = make_repo({path: workflow.format(orgs="", users="Alice, bob,")})
    assert run("pr-guard-trusted-users", repo) == Result(
        Status.FAIL, "public members of trusted orgs: Alice"
    )
    orgs = "trusted-orgs: owner, org"
    repo = make_repo({path: workflow.format(orgs=orgs, users="Alice, bob,")})
    assert run("pr-guard-trusted-users", repo) == Result(
        Status.FAIL, "public members of trusted orgs: Alice, bob"
    )
    repo = make_repo({path: workflow.format(orgs=orgs, users="dave,")})
    assert run("pr-guard-trusted-users", repo).status is Status.PASS
