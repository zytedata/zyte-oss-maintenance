from __future__ import annotations

from textwrap import dedent
from typing import TYPE_CHECKING

import pytest

from oss_maint import pythons
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
    }


def test_fact_error() -> None:
    fact = Fact("Broken", lambda: str(1 / 0))
    assert fact.run() == "error: ZeroDivisionError: division by zero"


def test_select_groups() -> None:
    groups = select_groups(["python", "ruff"])
    assert [g.id for g in groups] == ["python", "linting"]
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
    ("files", "mypy", "strict"),
    [
        ({}, Status.FAIL, Status.NA),
        (
            {"tox.ini": "[testenv:typing]\ncommands = mypy src\n"},
            Status.PASS,
            Status.FAIL,
        ),
        (
            {"tox.ini": "[testenv:typing]\ncommands = mypy --strict src\n"},
            Status.PASS,
            Status.PASS,
        ),
        (
            {"tox.toml": '[env.typing]\ncommands = [["mypy", "--strict", "src"]]\n'},
            Status.PASS,
            Status.PASS,
        ),
        (
            {
                "tox.ini": "[testenv:typing]\ncommands = mypy src\n",
                "pyproject.toml": "[tool.mypy]\nstrict = true\n",
            },
            Status.PASS,
            Status.PASS,
        ),
        (
            {
                ".pre-commit-config.yaml": (
                    "repos:\n- repo: x\n  hooks:\n  - id: mypy\n    args: [--strict]\n"
                )
            },
            Status.PASS,
            Status.PASS,
        ),
    ],
)
def test_mypy(
    make_repo: MakeRepo, files: dict[str, str], mypy: Status, strict: Status
) -> None:
    repo = make_repo(files)
    assert run("mypy", repo).status is mypy
    assert run("mypy-strict", repo).status is strict


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
    assert run("project-urls", repo).status is Status.PASS


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
    "docs/requirements.in": (
        "sphinx-scrapy @ git+https://github.com/scrapy/sphinx-scrapy.git@0.13.0\n"
    ),
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
    assert run("docs-requirements-in", repo).status is Status.FAIL
    repo = make_repo(SPHINX_SCRAPY_FILES)
    for check_id in (
        "docs-requirements-in",
        "sphinx-scrapy",
        "sphinx-scrapy-pins",
        "sphinx-scrapy-latest",
    ):
        assert run(check_id, repo).status is Status.PASS


def test_sphinx_scrapy_pins(make_repo: MakeRepo) -> None:
    repo = make_repo(
        {
            **SPHINX_SCRAPY_FILES,
            "tox.ini": "[tox]\n",
            "docs/requirements.in": "sphinx-scrapy==0.8.4\n",
        }
    )
    result = run("sphinx-scrapy-pins", repo)
    assert result.status is Status.FAIL
    assert result.detail == (
        "not pinned in tox; different pins: 0.8.4 in docs/requirements.in, "
        "0.13.0 in .pre-commit-config.yaml"
    )
    result = run("sphinx-scrapy-latest", repo)
    assert result.status is Status.FAIL
    assert result.detail == "pinned to 0.8.4, latest is 0.13.0"
