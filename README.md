# zyte-oss-maintenance

Shows which of our open-source Python projects are up to date with maintenance
practices, such as dropping end-of-life Python versions, linting with ruff, or
publishing to PyPI through trusted publishing.

- [`projects.toml`](projects.toml): the projects to check, in groups.
- [`oss_maint/checks/`](oss_maint/checks): the checks, each verifying a
  statement about a project, in groups of related checks (Python versions, packaging,
  linting, …), one module per group.
- [`REPORT.md`](REPORT.md): the latest report by check. It has a project ×
  group summary, then per group the statements, a project × check table, and
  an explanation of every failure.
- [`PROJECTS.md`](PROJECTS.md): the same results by project, listing only
  what fails (and notes worth reading) in each.

## Usage

Requires [uv](https://docs.astral.sh/uv/) and git.

```sh
uv run oss-maint report        # update checkouts, run everything, write the reports
uv run oss-maint checks        # list groups, checks and their statements
uv run oss-maint run -c python -c ruff -p parsel -p w3lib   # print results for a subset
uv run oss-maint sync          # only update checkouts
```

Projects are shallow-cloned from the default branch on GitHub into
`.cache/repos/`. `run` and `report` update the checkouts first unless you pass
`--no-sync`. Syncing also deletes checkouts of projects no longer in
`projects.toml`.

To refresh the reports, run `uv run oss-maint report` and commit `REPORT.md`
and `PROJECTS.md`.

## Adding a project

Add its GitHub `owner/name` to the `repos` of one of the `[[groups]]` in
`projects.toml`; the report shows projects by group. If a check, or a
whole group, does not apply to a project, add an exemption with the reason,
which the report shows as "not applicable":

```toml
[skip."scrapy/sphinx-scrapy"]
py-typed = "Sphinx extension, has no public Python API."
```

## Adding a check

Add a function to the module of the relevant group in `oss_maint/checks/`,
decorated with the group's `check()` and the statement it verifies, which
describes the up-to-date state. The function name is the check ID
(`mypy_strict` → `mypy-strict`):

```python
@group.check("mypy runs in strict mode.")
def mypy_strict(repo: Repo) -> Result:
    mypy = (repo.pyproject or {}).get("tool", {}).get("mypy", {})
    if not mypy.get("strict"):
        return failed("no strict = true in [tool.mypy]")
    return passed()
```

`Repo` gives access to the checkout (`read_text()`, `exists()`, `glob()`) and
parsed metadata (`pyproject`, `project`, `requires_python`, `classifiers`,
`has_sphinx_docs`, `supports_pypy`, `pre_commit_hooks`, `workflows`,
`workflow_steps()`; `workflow_strings` and `tox_strings` with all strings from
workflows and tox config, without comments; and `ci_python_versions` and
`ci_pypy_versions` mentioned there).
Return `failed()` with a short reason, `passed()` (optionally with a note worth
reading), or `not_applicable()` with a reason, e.g. for docs checks on
projects without docs. Exceptions are reported as check errors.

Informational checks, added with `@group.info(...)`, report a fact instead of
passing or failing: the function returns a bool, shown as "yes" or "no", or a
value to show, e.g. the license, or None for "no". They show facts that other
checks depend on, e.g. `has-sphinx-docs` next to the docs linters, or are
useful to see in the report.

To add a group, create a module with `group = Group("id", "Title")` and add
`group` to `GROUPS` in `oss_maint/checks/__init__.py`, which sets the report
order. Group and check IDs must be unique together.

Python and PyPy version data (see `oss_maint/pythons.py`) comes from
[endoflife.date](https://endoflife.date/python) (release and EOL dates),
[python.org](https://www.python.org/api/v2/downloads/release/) (release
candidates) and [PyPy's `versions.json`](https://downloads.python.org/pypy/versions.json)
(the Python versions of each PyPy release).

## Development

```sh
uv run tox                  # tests, pre-commit and pyrefly
uv run tox -e py            # or one of them: py, pre-commit, pyrefly
```
