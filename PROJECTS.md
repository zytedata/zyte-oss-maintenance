# Maintenance report by project

Generated on 2026-11-02 with `oss-maint report`. Do not edit by hand. Lists failing checks and notes for each project; see [REPORT.md](REPORT.md) for all results.

## Scrapy and its deps

### scrapy/scrapy

[Repository](https://github.com/scrapy/scrapy) · commit [`943e31d`](https://github.com/scrapy/scrapy/commit/943e31d5d69f2c9802e6673b3478975795670c57) · 42/49 checks passing

supports-pypy: no · license: BSD-3-Clause · mypy: yes · pyrefly: no · pylint: yes · has-sphinx-docs: yes · latest-release: 2.19.0 (2026-09-10) · unreleased-changes: yes

**Dependencies**

- ❌ [`dependency-lower-bounds`](REPORT.md#dependency-lower-bounds): no lower bound: packaging, tldextract

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Linting**

- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`pr-guard-trusted-users`](REPORT.md#pr-guard-trusted-users): public members of trusted orgs: kishan3

**Documentation**

- ❌ [`no-wiki`](REPORT.md#no-wiki): https://github.com/scrapy/scrapy/wiki has pages
- ❌ [`no-docs-requirements`](REPORT.md#no-docs-requirements): found docs/requirements.in, docs/requirements.txt
- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.13.0, latest is 0.15.0

### scrapy/cssselect

[Repository](https://github.com/scrapy/cssselect) · commit [`2834f2c`](https://github.com/scrapy/cssselect/commit/2834f2cd0d1605e44e0aae6945cbed8ab1609f66) · 37/47 checks passing

supports-pypy: yes · license: BSD-3-Clause · mypy: yes · pyrefly: no · pylint: yes · has-sphinx-docs: yes · latest-release: 1.6.0 (2026-10-09) · unreleased-changes: yes

**Python versions**

- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Packaging**

- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, changelog, documentation

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/tests-macos.yml, .github/workflows/tests-ubuntu.yml, .github/workflows/tests-windows.yml

**Documentation**

- ❌ [`no-wiki`](REPORT.md#no-wiki): https://github.com/scrapy/cssselect/wiki has pages
- ❌ [`no-docs-requirements`](REPORT.md#no-docs-requirements): found docs/requirements.txt
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py

### scrapy/formerly

[Repository](https://github.com/scrapy/formerly) · commit [`7d3d184`](https://github.com/scrapy/formerly/commit/7d3d184e2145ed8c67d2144744c3c96350733dc3) · 38/41 checks passing

supports-pypy: yes · license: BSD-3-Clause · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: 0.1.0 (2026-08-05) · unreleased-changes: yes

**Tests and coverage**

- ❌ [`codecov-status`](REPORT.md#codecov-status): patch status not disabled, project status target not 100% in codecov.yml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

### scrapy/itemadapter

[Repository](https://github.com/scrapy/itemadapter) · commit [`9bab3af`](https://github.com/scrapy/itemadapter/commit/9bab3af2034d0e2cf309cce1315f464dab412be6) · 32/43 checks passing

supports-pypy: yes · license: BSD-3-Clause · mypy: yes · pyrefly: no · pylint: yes · has-sphinx-docs: no · latest-release: 0.14.0 (2026-10-29) · unreleased-changes: yes

**Python versions**

- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/tests.yml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ❌ [`readme-rst`](REPORT.md#readme-rst): README.md instead
- ❌ [`no-wiki`](REPORT.md#no-wiki): https://github.com/scrapy/itemadapter/wiki has pages

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapy/itemloaders

[Repository](https://github.com/scrapy/itemloaders) · commit [`2481aee`](https://github.com/scrapy/itemloaders/commit/2481aee65f978357afa8317c6ca84f32e07d2a32) · 40/50 checks passing

supports-pypy: yes · license: BSD-3-Clause · mypy: yes · pyrefly: no · pylint: yes · has-sphinx-docs: yes · latest-release: 1.5.0 (2026-09-29) · unreleased-changes: yes

**Python versions**

- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/tests-macos.yml, .github/workflows/tests-ubuntu.yml, .github/workflows/tests-windows.yml

**Documentation**

- ❌ [`no-wiki`](REPORT.md#no-wiki): https://github.com/scrapy/itemloaders/wiki has pages
- ❌ [`no-docs-requirements`](REPORT.md#no-docs-requirements): found docs/requirements.txt
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py
- ❌ [`docs-stable-links`](REPORT.md#docs-stable-links): links to latest in README.rst; latest in pyproject.toml

**Releases**

- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): .github/workflows/publish.yml is triggered by GitHub releases
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapy/parsel

[Repository](https://github.com/scrapy/parsel) · commit [`8a3f041`](https://github.com/scrapy/parsel/commit/8a3f0412868d65626364db66a84f32fda15776b2) · 45/52 checks passing

supports-pypy: yes · license: BSD-3-Clause · mypy: yes · pyrefly: no · pylint: yes · has-sphinx-docs: yes · latest-release: 1.12.1 (2026-09-28) · unreleased-changes: yes

**Python versions**

- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Tests and coverage**

- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/tests-macos.yml, .github/workflows/tests-ubuntu.yml, .github/workflows/tests-windows.yml

**Documentation**

- ❌ [`no-docs-requirements`](REPORT.md#no-docs-requirements): found docs/requirements.in, docs/requirements.txt
- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.13.0, latest is 0.15.0
- ❌ [`docs-stable-links`](REPORT.md#docs-stable-links): links to latest in pyproject.toml
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

### scrapy/protego

[Repository](https://github.com/scrapy/protego) · commit [`d311dc9`](https://github.com/scrapy/protego/commit/d311dc9154767341aaf7661402cda3ddef9c2225) · 36/41 checks passing

supports-pypy: yes · license: BSD-3-Clause · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: 0.7.0 (2026-09-21) · unreleased-changes: yes

**Python versions**

- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Tests and coverage**

- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/comparison.yml, .github/workflows/tests.yml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ❌ [`no-wiki`](REPORT.md#no-wiki): https://github.com/scrapy/protego/wiki has pages

### scrapy/queuelib

[Repository](https://github.com/scrapy/queuelib) · commit [`d4ed6ab`](https://github.com/scrapy/queuelib/commit/d4ed6abbce003f953cc6a1163d2ea396243417e5) · 32/41 checks passing

supports-pypy: yes · license: BSD-3-Clause · mypy: yes · pyrefly: no · pylint: yes · has-sphinx-docs: no · latest-release: 1.10.0 (2026-08-24) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Packaging**

- ❌ [`sdist-contents`](REPORT.md#sdist-contents): not included: tox.ini

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/tests.yml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

### scrapy/w3lib

[Repository](https://github.com/scrapy/w3lib) · commit [`b9d6f65`](https://github.com/scrapy/w3lib/commit/b9d6f65c83f49358269d089a700c4e24cf578a36) · 38/48 checks passing

supports-pypy: yes · license: BSD-3-Clause · mypy: yes · pyrefly: no · pylint: yes · has-sphinx-docs: yes · latest-release: 2.5.0 (2026-09-30) · unreleased-changes: yes

**Python versions**

- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/test.yml
- ❌ [`pr-guard-trusted-users`](REPORT.md#pr-guard-trusted-users): public members of trusted orgs: kishan3

**Documentation**

- ❌ [`no-docs-requirements`](REPORT.md#no-docs-requirements): found docs/requirements.txt
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py
- ❌ [`docs-stable-links`](REPORT.md#docs-stable-links): links to latest in pyproject.toml
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

### scrapy/xtractmime

[Repository](https://github.com/scrapy/xtractmime) · commit [`9d50fcb`](https://github.com/scrapy/xtractmime/commit/9d50fcb0d7abd7a96f7dee746d9285faba4af6db) · 25/40 checks passing

supports-pypy: yes · license: BSD-3-Clause · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: 0.2.1 (2024-01-16) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15
- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff-rules`](REPORT.md#ruff-rules): only the default rules are enabled
- ❌ [`dependabot`](REPORT.md#dependabot): no .github/dependabot.yml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ❌ [`readme-rst`](REPORT.md#readme-rst): README.md instead
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

## Scrapy plugins

### scrapy-plugins/scrapy-download-handlers-incubator

[Repository](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) · commit [`bfb37fb`](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator/commit/bfb37fb5fdf1c2ffcde595a47f053443c988c15f) · 38/42 checks passing

supports-pypy: no · license: BSD-3-Clause · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: 0.7.0 (2026-10-26) · unreleased-changes: no

**Tests and coverage**

- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

### scrapy-plugins/scrapy-playwright

[Repository](https://github.com/scrapy-plugins/scrapy-playwright) · commit [`2658f86`](https://github.com/scrapy-plugins/scrapy-playwright/commit/2658f86a4771b918dbe1d32c345ca70e34d43648) · 18/47 checks passing

supports-pypy: no · license: BSD-3-Clause · mypy: yes · pyrefly: no · pylint: yes · has-sphinx-docs: yes · latest-release: 0.0.48 (2026-07-10) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: pylintrc; tool sections in setup.cfg: [flake8]
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, changelog, documentation
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-auth`](REPORT.md#codecov-auth): expected tokenless, found token in .github/workflows/tests.yml
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format
- ❌ [`pre-commit-in-ci`](REPORT.md#pre-commit-in-ci): not run in CI workflows or tox
- ❌ [`pre-commit-tox`](REPORT.md#pre-commit-tox): no tox environment runs pre-commit run --all-files
- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/tests.yml
- ❌ [`blacken-docs`](REPORT.md#blacken-docs): missing pre-commit hooks: blacken-docs

**Documentation**

- ❌ [`no-docs-requirements`](REPORT.md#no-docs-requirements): found docs/requirements.in, docs/requirements.txt
- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.9.0, latest is 0.15.0
- ❌ [`docs-stable-links`](REPORT.md#docs-stable-links): links to latest in README.rst
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'publish' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): .github/workflows/publish.yml is triggered by GitHub releases
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapy-plugins/scrapy-spider-metadata

[Repository](https://github.com/scrapy-plugins/scrapy-spider-metadata) · commit [`a8f7a8b`](https://github.com/scrapy-plugins/scrapy-spider-metadata/commit/a8f7a8b52e8b1bd57dfe8f522ac58b98a2c99c76) · 37/51 checks passing

supports-pypy: yes · license: BSD License · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: yes · latest-release: 0.2.0 (2024-09-26) · unreleased-changes: yes

**Python versions**

- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, changelog, documentation

**Tests and coverage**

- ❌ [`codecov-auth`](REPORT.md#codecov-auth): expected tokenless, found token in .github/workflows/test.yml
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Documentation**

- ❌ [`no-docs-requirements`](REPORT.md#no-docs-requirements): found docs/requirements.in, docs/requirements.txt
- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.13.0, latest is 0.15.0
- ❌ [`docs-stable-links`](REPORT.md#docs-stable-links): links to latest in README.rst
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'deploy' has no environment
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes

### zytedata/duplicate-url-discarder

[Repository](https://github.com/zytedata/duplicate-url-discarder) · commit [`8db08b3`](https://github.com/zytedata/duplicate-url-discarder/commit/8db08b3edf638f34ee6ad7393612f579b5bfb90f) · 13/37 checks passing

supports-pypy: no · license: BSD License · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: 0.3.0 (2024-12-30) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.14, 3.15

**Packaging**

- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: .coveragerc, .flake8
- ❌ [`pep639-license`](REPORT.md#pep639-license): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, changelog

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-auth`](REPORT.md#codecov-auth): expected tokenless, found token in .github/workflows/test.yml
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort
- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): only legacy (bump2version) configuration, in .bumpversion.cfg

### zytedata/duplicate-url-discarder-rules

[Repository](https://github.com/zytedata/duplicate-url-discarder-rules) · commit [`7281048`](https://github.com/zytedata/duplicate-url-discarder-rules/commit/7281048b2cfa0538c0b355e8f91185f27367649d) · 11/34 checks passing

supports-pypy: no · license: MIT License · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: 2024.11.5 (2024-11-05) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.14, 3.15

**Packaging**

- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): tool sections in setup.cfg: [flake8]
- ❌ [`pep639-license`](REPORT.md#pep639-license): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: MIT License
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, changelog

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-auth`](REPORT.md#codecov-auth): expected tokenless, found token in .github/workflows/test.yml
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort
- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml

## Scrapy tools

### scrapy/scrapy-lint

[Repository](https://github.com/scrapy/scrapy-lint) · commit [`ca79b29`](https://github.com/scrapy/scrapy-lint/commit/ca79b29dd89f14c33d1df623034449dc2f11f2af) · 33/48 checks passing

supports-pypy: no · license: MIT · mypy: yes · pyrefly: no · pylint: yes · has-sphinx-docs: yes · latest-release: 0.1.1 (2026-01-27) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: documentation

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch

**Linting**

- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/ci.yml

**Documentation**

- ❌ [`no-docs-requirements`](REPORT.md#no-docs-requirements): found docs/requirements.txt
- ❌ [`sphinx-scrapy-pins`](REPORT.md#sphinx-scrapy-pins): not pinned in tox, .pre-commit-config.yaml
- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): not pinned
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapinghub/scrapyrt

[Repository](https://github.com/scrapinghub/scrapyrt) · commit [`066cdaf`](https://github.com/scrapinghub/scrapyrt/commit/066cdafb9dc5e864f3e1dd19cb7fafec7fefb7fe) · 26/46 checks passing

supports-pypy: no · license: BSD-3-Clause · mypy: yes · pyrefly: no · pylint: yes · has-sphinx-docs: yes · latest-release: 0.18.1 (2026-06-29) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.14, 3.15

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`pre-commit-updates`](REPORT.md#pre-commit-updates): outdated: ruff v0.12.5 (0.15.12 or later expected)
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/main.yml

**Documentation**

- ❌ [`no-wiki`](REPORT.md#no-wiki): https://github.com/scrapinghub/scrapyrt/wiki has pages
- ❌ [`no-docs-requirements`](REPORT.md#no-docs-requirements): found docs/requirements.txt
- ❌ [`sphinx-scrapy-pins`](REPORT.md#sphinx-scrapy-pins): not pinned in tox, .pre-commit-config.yaml
- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): not pinned
- ❌ [`docs-stable-links`](REPORT.md#docs-stable-links): links to latest in README.rst; latest in pyproject.toml

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml uses an API token
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

## Feed exporters

### scrapy-plugins/scrapy-feedexport-warc

[Repository](https://github.com/scrapy-plugins/scrapy-feedexport-warc) · commit [`ad7956f`](https://github.com/scrapy-plugins/scrapy-feedexport-warc/commit/ad7956f4825fa2c4671c1849a8ad7a4eb2cc34d1) · 8/35 checks passing

supports-pypy: no · license: Apache Software License · mypy: no · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.13, 3.14, 3.15

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: Apache Software License
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: changelog
- ❌ [`twine-check`](REPORT.md#twine-check): twine check runs in a workflow, not in tox

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`type-checker`](REPORT.md#type-checker): no type checker found

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`pre-commit-tox`](REPORT.md#pre-commit-tox): no tox environment runs pre-commit run --all-files
- ❌ [`pre-commit-updates`](REPORT.md#pre-commit-updates): outdated: ruff v0.8.4 (0.15.12 or later expected)
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/tests.yml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ❌ [`readme-rst`](REPORT.md#readme-rst): README.md instead
- ❌ [`changelog`](REPORT.md#changelog): no changelog file
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): .github/workflows/release.yml is not triggered by tag pushes
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/release.yml: job 'release' builds and publishes
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml

### scrapy-plugins/scrapy-feedexporter-azure-storage

[Repository](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage) · commit [`4f36ff8`](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage/commit/4f36ff805239bace39bacc8c1e02cc8c876013b4) · 2/25 checks passing

supports-pypy: no · license: no · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.8' allows 3.8 (EOL 2024-10-07), 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01)
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no Python version classifiers

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists
- ❌ [`hatchling`](REPORT.md#hatchling): no pyproject.toml
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ❌ [`readme-rst`](REPORT.md#readme-rst): README.md instead
- ❌ [`changelog`](REPORT.md#changelog): no changelog file
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): no workflow publishes to PyPI
- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): no workflow publishes to PyPI
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): no workflow publishes to PyPI
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml

### scrapy-plugins/scrapy-feedexporter-dropbox

[Repository](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox) · commit [`4e4cca6`](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox/commit/4e4cca6f5240d790708219c0344b812eb76a854f) · 1/23 checks passing

supports-pypy: no · license: no · mypy: no · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python is not declared
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists
- ❌ [`hatchling`](REPORT.md#hatchling): no pyproject.toml
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`type-checker`](REPORT.md#type-checker): no type checker found

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ❌ [`readme-rst`](REPORT.md#readme-rst): README.md instead
- ❌ [`changelog`](REPORT.md#changelog): no changelog file
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): no workflow publishes to PyPI
- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): no workflow publishes to PyPI
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): no workflow publishes to PyPI
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml

### scrapy-plugins/scrapy-feedexporter-google-drive

[Repository](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive) · commit [`369598d`](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive/commit/369598d8205938ba851af91fed913335bfd12cd9) · 16/37 checks passing

supports-pypy: no · license: BSD-3-Clause · mypy: no · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: 0.1.0 (2026-10-21) · unreleased-changes: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`dependency-lower-bounds`](REPORT.md#dependency-lower-bounds): no lower bound: google-api-python-client, google-auth, scrapy
- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`type-checker`](REPORT.md#type-checker): no type checker found

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapy-plugins/scrapy-feedexporter-google-sheets

[Repository](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets) · commit [`25f2a8c`](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets/commit/25f2a8c6079e85823c7e640b17eea2ad5ed8f767) · 1/24 checks passing

supports-pypy: no · license: no · mypy: no · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.8' allows 3.8 (EOL 2024-10-07), 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01)
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no Python version classifiers

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists
- ❌ [`hatchling`](REPORT.md#hatchling): no pyproject.toml
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`type-checker`](REPORT.md#type-checker): no type checker found

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ❌ [`readme-rst`](REPORT.md#readme-rst): README.md instead
- ❌ [`changelog`](REPORT.md#changelog): no changelog file
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): no workflow publishes to PyPI
- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): no workflow publishes to PyPI
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): no workflow publishes to PyPI
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml

### scrapy-plugins/scrapy-feedexporter-onedrive

[Repository](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive) · commit [`b97aab3`](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive/commit/b97aab3d3a50e7d7fe829285a7e53fd7f80ea758) · 12/36 checks passing

supports-pypy: no · license: BSD License · mypy: no · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: 0.1.0 (2026-10-21) · unreleased-changes: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.8' allows 3.8 (EOL 2024-10-07), 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.8, 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.14, 3.15

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, changelog
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`dependency-lower-bounds`](REPORT.md#dependency-lower-bounds): no lower bound: requests
- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`type-checker`](REPORT.md#type-checker): no type checker found

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`pre-commit-in-ci`](REPORT.md#pre-commit-in-ci): not run in CI workflows or tox
- ❌ [`pre-commit-tox`](REPORT.md#pre-commit-tox): no tox environment runs pre-commit run --all-files
- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ❌ [`readme-rst`](REPORT.md#readme-rst): README.md instead
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapy-plugins/scrapy-feedexporter-sftp

[Repository](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp) · commit [`38c9e5b`](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp/commit/38c9e5b244bfa363de9ede92f7069ae7bcbce469) · 16/38 checks passing

supports-pypy: no · license: BSD License · mypy: no · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: 1.1.0 (2025-02-12) · unreleased-changes: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.14, 3.15

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, changelog
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`type-checker`](REPORT.md#type-checker): no type checker found

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`pre-commit-updates`](REPORT.md#pre-commit-updates): outdated: ruff v0.9.3 (0.15.12 or later expected)
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

## scrapy-poet and its deps

### scrapinghub/scrapy-poet

[Repository](https://github.com/scrapinghub/scrapy-poet) · commit [`fd70074`](https://github.com/scrapinghub/scrapy-poet/commit/fd700743f97f6a63ed37d3d185abb2477f09d3af) · 35/49 checks passing

supports-pypy: no · license: BSD-3-Clause · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: yes · latest-release: 0.27.2 (2026-04-28) · unreleased-changes: yes

**Python versions**

- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: requirements-dev.txt
- ❌ [`pep639-license`](REPORT.md#pep639-license): has license classifiers: License :: OSI Approved :: BSD License

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-auth`](REPORT.md#codecov-auth): expected OIDC, found token in .github/workflows/scrapy-unreleased.yml, .github/workflows/test.yml
- ❌ [`codecov-status`](REPORT.md#codecov-status): patch status not disabled, project status target not 100% in .codecov.yml
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`pre-commit-updates`](REPORT.md#pre-commit-updates): outdated: ruff v0.15.6 (0.15.12 or later expected)
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/scrapy-unreleased.yml, .github/workflows/test.yml

**Documentation**

- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapinghub/andi

[Repository](https://github.com/scrapinghub/andi) · commit [`5b7f109`](https://github.com/scrapinghub/andi/commit/5b7f1094a5526a016477a3d1c3f7617909f3bbbf) · 31/39 checks passing

supports-pypy: no · license: Apache-2.0 · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: 0.9.0 (2026-09-17) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10

**Packaging**

- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: changelog

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-status`](REPORT.md#codecov-status): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ❌ [`no-wiki`](REPORT.md#no-wiki): https://github.com/scrapinghub/andi/wiki has pages

### scrapinghub/web-poet

[Repository](https://github.com/scrapinghub/web-poet) · commit [`599e041`](https://github.com/scrapinghub/web-poet/commit/599e04110b617531a32884d439a5666126344fdd) · 31/49 checks passing

supports-pypy: no · license: BSD-3-Clause · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: yes · latest-release: 0.24.1 (2026-04-28) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: requirements-dev.txt
- ❌ [`pep639-license`](REPORT.md#pep639-license): has license classifiers: License :: OSI Approved :: BSD License
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, changelog

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-auth`](REPORT.md#codecov-auth): expected OIDC, found token in .github/workflows/tests-ubuntu.yml, .github/workflows/tests-windows.yml
- ❌ [`codecov-status`](REPORT.md#codecov-status): patch status not disabled, project status target not 100% in .codecov.yml
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch

**Linting**

- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/tests-ubuntu.yml, .github/workflows/tests-windows.yml

**Documentation**

- ❌ [`no-docs-requirements`](REPORT.md#no-docs-requirements): found docs/requirements.in, docs/requirements.txt
- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.8.12, latest is 0.15.0
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes

### zytedata/url-matcher

[Repository](https://github.com/zytedata/url-matcher) · commit [`6fe906b`](https://github.com/zytedata/url-matcher/commit/6fe906b4aba1632fa41fc116ed29de84e68bba04) · 41/49 checks passing

supports-pypy: no · license: Apache-2.0 · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: yes · latest-release: 0.6.0 (2025-02-14) · unreleased-changes: yes

**Packaging**

- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: requirements-dev.txt

**Tests and coverage**

- ❌ [`codecov-auth`](REPORT.md#codecov-auth): expected tokenless, found token in .github/workflows/test.yml
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Documentation**

- ❌ [`no-docs-requirements`](REPORT.md#no-docs-requirements): found docs/requirements.in, docs/requirements.txt
- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.13.0, latest is 0.15.0
- ❌ [`changelog-date`](REPORT.md#changelog-date): no file replacement of (unreleased) with {now:%Y-%m-%d}
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

### scrapy/frostwork

[Repository](https://github.com/scrapy/frostwork) · commit [`d1e2d5c`](https://github.com/scrapy/frostwork/commit/d1e2d5c27f4b2664a923e37bc5e0fdf53fd42c02) · 18/34 checks passing

supports-pypy: no · license: Apache-2.0 · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: 0.1.6 (2026-09-23) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier
- ❌ [`type-checker`](REPORT.md#type-checker): no type checker found

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format
- ❌ [`pre-commit-in-ci`](REPORT.md#pre-commit-in-ci): not run in CI workflows or tox
- ❌ [`pre-commit-tox`](REPORT.md#pre-commit-tox): no tox environment runs pre-commit run --all-files
- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/ci.yml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py; Markdown files: docs/BENCHMARKS.md, docs/COMPATIBILITY.md, docs/DESIGN.md, docs/MIGRATION.md, docs/PYTHON.md, docs/RELEASING.md, docs/SUPPORT_SNAPSHOT.md, docs/TESTING.md, docs/WEBPOET_SURFACE.md
- ❌ [`readme-rst`](REPORT.md#readme-rst): README.md instead
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

## Zyte API

### scrapy-plugins/scrapy-zyte-api

[Repository](https://github.com/scrapy-plugins/scrapy-zyte-api) · commit [`9b63ad9`](https://github.com/scrapy-plugins/scrapy-zyte-api/commit/9b63ad94dbc95e276c3e2981dbdd88cf96a4f88d) · 39/50 checks passing

supports-pypy: no · license: BSD-3-Clause · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: yes · latest-release: 0.36.0 (2026-08-20) · unreleased-changes: yes

**Packaging**

- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, changelog

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-auth`](REPORT.md#codecov-auth): expected tokenless, found token in .github/workflows/test.yml

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Documentation**

- ❌ [`no-docs-requirements`](REPORT.md#no-docs-requirements): found docs/requirements.in, docs/requirements.txt
- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.8.12, latest is 0.15.0
- ❌ [`docs-stable-links`](REPORT.md#docs-stable-links): links to latest in README.rst; latest in pyproject.toml
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### zytedata/python-zyte-api

[Repository](https://github.com/zytedata/python-zyte-api) · commit [`5ca09d3`](https://github.com/zytedata/python-zyte-api/commit/5ca09d3691312b0d51fba41e20f92a8426e51f49) · 34/48 checks passing

supports-pypy: no · license: BSD License · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: yes · latest-release: 0.11.0 (2026-07-23) · unreleased-changes: yes

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, changelog

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-auth`](REPORT.md#codecov-auth): expected tokenless, found token in .github/workflows/test.yml
- ❌ [`codecov-status`](REPORT.md#codecov-status): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`pre-commit-in-ci`](REPORT.md#pre-commit-in-ci): tox environments that run pre-commit are not run in CI: pre-commit
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Documentation**

- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapy-plugins/scrapy-zyte-smartproxy

[Repository](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) · commit [`debd444`](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy/commit/debd4445343d0c3a1eba9fa0ce269613bb3b9d5c) · 15/40 checks passing

supports-pypy: no · license: BSD License · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: yes · latest-release: 2.4.1 (2025-03-24) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.14, 3.15

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists
- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: .bandit.yml, .flake8, .isort.cfg; tool sections in setup.cfg: [mypy], [mypy-pytest.*], [mypy-scrapy.*], [mypy-twisted.*], [mypy-w3lib.*]
- ❌ [`hatchling`](REPORT.md#hatchling): no build-backend in pyproject.toml

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-auth`](REPORT.md#codecov-auth): expected tokenless, found token in .github/workflows/main.yml
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort
- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/main.yml
- ❌ [`blacken-docs`](REPORT.md#blacken-docs): missing pre-commit hooks: blacken-docs
- ❌ [`sphinx-lint`](REPORT.md#sphinx-lint): missing pre-commit hooks: sphinx-lint

**Documentation**

- ❌ [`no-docs-requirements`](REPORT.md#no-docs-requirements): found docs/requirements.txt
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### zytedata/zyte-common-items

[Repository](https://github.com/zytedata/zyte-common-items) · commit [`fccd5d4`](https://github.com/zytedata/zyte-common-items/commit/fccd5d44cf037698c3742a4362cf492712878cf1) · 37/49 checks passing

supports-pypy: no · license: BSD-3-Clause · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: yes · latest-release: 0.31.0 (2026-10-16) · unreleased-changes: yes

**Packaging**

- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: requirements-dev.txt

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-auth`](REPORT.md#codecov-auth): expected tokenless, found token in .github/workflows/test.yml
- ❌ [`codecov-status`](REPORT.md#codecov-status): patch status not disabled, project status target not 100% in .codecov.yml
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Documentation**

- ❌ [`no-docs-requirements`](REPORT.md#no-docs-requirements): found docs/requirements.txt
- ❌ [`sphinx-scrapy-pins`](REPORT.md#sphinx-scrapy-pins): not pinned in tox, .pre-commit-config.yaml
- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): not pinned
- ❌ [`docs-stable-links`](REPORT.md#docs-stable-links): links to latest in README.rst
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

## Scrapy Cloud

### scrapinghub/python-scrapinghub

[Repository](https://github.com/scrapinghub/python-scrapinghub) · commit [`c60ab46`](https://github.com/scrapinghub/python-scrapinghub/commit/c60ab4620f67f302a5685e30674fdf41c281af39) · 16/42 checks passing

supports-pypy: yes · license: BSD License · mypy: no · pyrefly: no · pylint: no · has-sphinx-docs: yes · latest-release: 2.9.0 (2026-08-12) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.14, 3.15
- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [metadata], [bdist_wheel]
- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: pytest.ini
- ❌ [`hatchling`](REPORT.md#hatchling): no build-backend in pyproject.toml
- ❌ [`twine-check`](REPORT.md#twine-check): twine check runs in a workflow, not in tox

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`type-checker`](REPORT.md#type-checker): no type checker found

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-auth`](REPORT.md#codecov-auth): expected OIDC, found token in .github/workflows/main.yml
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format
- ❌ [`pre-commit-in-ci`](REPORT.md#pre-commit-in-ci): not run in CI workflows or tox
- ❌ [`pre-commit-tox`](REPORT.md#pre-commit-tox): no tox environment runs pre-commit run --all-files
- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/main.yml
- ❌ [`blacken-docs`](REPORT.md#blacken-docs): missing pre-commit hooks: blacken-docs
- ❌ [`sphinx-lint`](REPORT.md#sphinx-lint): missing pre-commit hooks: sphinx-lint

**Documentation**

- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

### scrapinghub/shub

[Repository](https://github.com/scrapinghub/shub) · commit [`a174e7e`](https://github.com/scrapinghub/shub/commit/a174e7ebc22cded1a1510bfc9cf572c5b79018cf) · 23/46 checks passing

supports-pypy: no · license: BSD-3-Clause · mypy: no · pyrefly: no · pylint: no · has-sphinx-docs: yes · latest-release: 2.18.1 (2026-07-08) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): has license classifiers: License :: OSI Approved :: BSD License
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: changelog
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`dependency-lower-bounds`](REPORT.md#dependency-lower-bounds): no lower bound: docker, importlib-metadata, packaging, PyYAML, requests, retrying, setuptools, toml

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`type-checker`](REPORT.md#type-checker): no type checker found

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-auth`](REPORT.md#codecov-auth): expected OIDC, found token in .github/workflows/tests.yml
- ❌ [`codecov-status`](REPORT.md#codecov-status): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/tests.yml
- ❌ [`blacken-docs`](REPORT.md#blacken-docs): missing pre-commit hooks: blacken-docs
- ❌ [`sphinx-lint`](REPORT.md#sphinx-lint): missing pre-commit hooks: sphinx-lint

**Documentation**

- ❌ [`no-wiki`](REPORT.md#no-wiki): https://github.com/scrapinghub/shub/wiki has pages

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'publish' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapinghub/scrapinghub-entrypoint-scrapy

[Repository](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) · commit [`bf9632c`](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy/commit/bf9632c78355b545126363ce557106c1b9c3bb54) · 6/30 checks passing

supports-pypy: no · license: BSD License · mypy: no · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: 0.18.1 (2026-01-28) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.14, 3.15

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [bdist_wheel], [sdist_dsc]
- ❌ [`hatchling`](REPORT.md#hatchling): no build-backend in pyproject.toml
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`type-checker`](REPORT.md#type-checker): no type checker found

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-auth`](REPORT.md#codecov-auth): expected OIDC, found token in .github/workflows/tests.yml
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml
- ❌ [`actionlint`](REPORT.md#actionlint): no .pre-commit-config.yaml
- ❌ [`zizmor`](REPORT.md#zizmor): no .pre-commit-config.yaml
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/tests.yml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ❌ [`readme-rst`](REPORT.md#readme-rst): README.md instead
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'publish' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapinghub/shub-workflow

[Repository](https://github.com/scrapinghub/shub-workflow) · commit [`5471c35`](https://github.com/scrapinghub/shub-workflow/commit/5471c352f0f4d7ecada0381b69f072a325b87cfa) · 3/27 checks passing

supports-pypy: no · license: Apache Software License · mypy: no · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: 1.14.46 (2026-10-30) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python is not declared
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists
- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): tool sections in setup.cfg: [flake8], [tool:pytest], [coverage:run]
- ❌ [`hatchling`](REPORT.md#hatchling): no build-backend in pyproject.toml
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier
- ❌ [`type-checker`](REPORT.md#type-checker): no type checker found

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml
- ❌ [`actionlint`](REPORT.md#actionlint): no .pre-commit-config.yaml
- ❌ [`zizmor`](REPORT.md#zizmor): no .pre-commit-config.yaml
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/python-app.yml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ❌ [`readme-rst`](REPORT.md#readme-rst): README.md instead
- ❌ [`no-wiki`](REPORT.md#no-wiki): https://github.com/scrapinghub/shub-workflow/wiki has pages

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): no workflow publishes to PyPI
- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): no workflow publishes to PyPI
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): no workflow publishes to PyPI
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml

### scrapinghub/scrapy-frontera

[Repository](https://github.com/scrapinghub/scrapy-frontera) · commit [`56ea2e1`](https://github.com/scrapinghub/scrapy-frontera/commit/56ea2e1ef39a174eac61da2edcdb21d1f1ecf5e5) · 10/35 checks passing

supports-pypy: no · license: BSD License · mypy: no · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: 0.3.0 (2025-06-06) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01)
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no Python version classifiers

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists
- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: .flake8
- ❌ [`hatchling`](REPORT.md#hatchling): no build-backend in pyproject.toml
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`type-checker`](REPORT.md#type-checker): no type checker found

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-auth`](REPORT.md#codecov-auth): expected OIDC, found token in .github/workflows/tests.yml
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`pre-commit-tox`](REPORT.md#pre-commit-tox): no tox environment runs pre-commit run --all-files
- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`pre-commit-updates`](REPORT.md#pre-commit-updates): outdated: ruff v0.9.4 (0.15.12 or later expected)
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/tests.yml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml uses an API token
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapinghub/frontera

[Repository](https://github.com/scrapinghub/frontera) · commit [`c94beae`](https://github.com/scrapinghub/frontera/commit/c94beae2f438492139d24759729d0201779ccf1c) · 3/28 checks passing

supports-pypy: no · license: BSD License · mypy: no · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: 0.8.1 (2019-04-05) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python is not declared
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [metadata]
- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: .coveragerc; tool sections in tox.ini: [flake8], [pytest]
- ❌ [`hatchling`](REPORT.md#hatchling): no pyproject.toml
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`type-checker`](REPORT.md#type-checker): no type checker found

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-auth`](REPORT.md#codecov-auth): expected OIDC, found token in .github/workflows/test.yml
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml
- ❌ [`actionlint`](REPORT.md#actionlint): no .pre-commit-config.yaml
- ❌ [`zizmor`](REPORT.md#zizmor): no .pre-commit-config.yaml
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ❌ [`readme-rst`](REPORT.md#readme-rst): README.md instead
- ❌ [`no-wiki`](REPORT.md#no-wiki): https://github.com/scrapinghub/frontera/wiki has pages
- ❌ [`changelog`](REPORT.md#changelog): no changelog file

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml uses an API token
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml

### scrapinghub/hcf-backend

[Repository](https://github.com/scrapinghub/hcf-backend) · commit [`bbdc50c`](https://github.com/scrapinghub/hcf-backend/commit/bbdc50cd1d250742234aacc2d5da10c4fe4d9508) · 9/33 checks passing

supports-pypy: no · license: BSD License · mypy: no · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: 0.6.1 (2025-10-31) · unreleased-changes: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python is not declared
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists
- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: .flake8
- ❌ [`hatchling`](REPORT.md#hatchling): no build-backend in pyproject.toml
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`type-checker`](REPORT.md#type-checker): no type checker found

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-auth`](REPORT.md#codecov-auth): expected OIDC, found token in .github/workflows/test.yml
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff-rules`](REPORT.md#ruff-rules): only the default rules are enabled
- ❌ [`pre-commit-tox`](REPORT.md#pre-commit-tox): no tox environment runs pre-commit run --all-files
- ❌ [`pre-commit-updates`](REPORT.md#pre-commit-updates): outdated: ruff v0.11.12 (0.15.12 or later expected)
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ❌ [`readme-rst`](REPORT.md#readme-rst): README.md instead
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml uses an API token
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

## Data extraction

### zytedata/zyte-parsers

[Repository](https://github.com/zytedata/zyte-parsers) · commit [`4f5d08d`](https://github.com/zytedata/zyte-parsers/commit/4f5d08d1be951fa438f0aedd598d61a61c360ea0) · 33/47 checks passing

supports-pypy: no · license: Apache-2.0 · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: yes · latest-release: 0.6.0 (2025-10-24) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Dependencies**

- ❌ [`dependency-lower-bounds`](REPORT.md#dependency-lower-bounds): no lower bound: html-text, lxml, parsel, six, w3lib
- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-auth`](REPORT.md#codecov-auth): expected tokenless, found token in .github/workflows/test.yml
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Documentation**

- ❌ [`no-docs-requirements`](REPORT.md#no-docs-requirements): found docs/requirements.txt
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py
- ❌ [`docs-stable-links`](REPORT.md#docs-stable-links): links to latest in README.rst; latest in pyproject.toml
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

### zytedata/clear-html

[Repository](https://github.com/zytedata/clear-html) · commit [`6b820b1`](https://github.com/zytedata/clear-html/commit/6b820b13221145ceb0814e47e9583e5574d28865) · 31/41 checks passing

supports-pypy: no · license: Apache-2.0 · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: 0.5.0 (2025-10-24) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-auth`](REPORT.md#codecov-auth): expected tokenless, found token in .github/workflows/test.yml
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

### zytedata/html-text

[Repository](https://github.com/zytedata/html-text) · commit [`3955be2`](https://github.com/zytedata/html-text/commit/3955be2f85381e7198bdd99f5e9ce903786c7a9e) · 27/40 checks passing

supports-pypy: no · license: MIT · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: 0.7.1 (2025-10-06) · unreleased-changes: yes

**Packaging**

- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, changelog

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-auth`](REPORT.md#codecov-auth): expected tokenless, found token in .github/workflows/test.yml
- ❌ [`codecov-status`](REPORT.md#codecov-status): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes

### scrapinghub/price-parser

[Repository](https://github.com/scrapinghub/price-parser) · commit [`6718bfe`](https://github.com/scrapinghub/price-parser/commit/6718bfe8447f2de17ecc152d3ad2a4c51520c755) · 24/42 checks passing

supports-pypy: no · license: BSD-3-Clause · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: 0.5.1 (2026-03-19) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: changelog
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-auth`](REPORT.md#codecov-auth): expected OIDC, found token in .github/workflows/main.yml
- ❌ [`codecov-status`](REPORT.md#codecov-status): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`pre-commit-updates`](REPORT.md#pre-commit-updates): outdated: ruff v0.13.2 (0.15.12 or later expected)
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/main.yml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ❌ [`no-wiki`](REPORT.md#no-wiki): https://github.com/scrapinghub/price-parser/wiki has pages

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml uses an API token
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapinghub/dateparser

[Repository](https://github.com/scrapinghub/dateparser) · commit [`b1a87f9`](https://github.com/scrapinghub/dateparser/commit/b1a87f9f9c76e612e68a0137521ed3e2e1114702) · 23/46 checks passing

supports-pypy: no · license: BSD-3-Clause · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: yes · latest-release: 1.4.3 (2026-09-03) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): setup.py exists
- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: .coveragerc, pytest.ini
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, documentation

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-auth`](REPORT.md#codecov-auth): expected OIDC, found token in .github/workflows/main.yml
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch

**Linting**

- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/cifuzz.yml, .github/workflows/main.yml
- ❌ [`pr-guard-trusted-users`](REPORT.md#pr-guard-trusted-users): public members of trusted orgs: kishan3
- ❌ [`blacken-docs`](REPORT.md#blacken-docs): missing pre-commit hooks: blacken-docs
- ❌ [`sphinx-lint`](REPORT.md#sphinx-lint): missing pre-commit hooks: sphinx-lint

**Documentation**

- ❌ [`no-docs-requirements`](REPORT.md#no-docs-requirements): found docs/requirements.txt
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py
- ❌ [`docs-stable-links`](REPORT.md#docs-stable-links): links to latest in README.rst; latest in pyproject.toml
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): .github/workflows/publish.yml is triggered by GitHub releases

### scrapinghub/extruct

[Repository](https://github.com/scrapinghub/extruct) · commit [`d24f541`](https://github.com/scrapinghub/extruct/commit/d24f5414fd32c874989492ebd04cb1deb6d7d04e) · 9/32 checks passing

supports-pypy: no · license: BSD License · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: 0.18.0 (2024-11-08) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.8' allows 3.8 (EOL 2024-10-07), 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.8, 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.13, 3.14, 3.15

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [wheel]
- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: .coveragerc, .isort.cfg, pytest.ini, requirements-dev.txt
- ❌ [`hatchling`](REPORT.md#hatchling): no build-backend in pyproject.toml

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-auth`](REPORT.md#codecov-auth): expected OIDC, found token in .github/workflows/python-package.yml
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, isort, pyupgrade
- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/python-package.yml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ❌ [`no-wiki`](REPORT.md#no-wiki): https://github.com/scrapinghub/extruct/wiki has pages

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/python-publish.yml: job 'deploy' has no environment; .github/workflows/python-publish.yml publishes with twine upload
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/python-publish.yml: job 'deploy' builds and publishes
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): only legacy (bump2version) configuration, in setup.cfg

### scrapinghub/number-parser

[Repository](https://github.com/scrapinghub/number-parser) · commit [`a126357`](https://github.com/scrapinghub/number-parser/commit/a1263578628a7743054879095e50532fba1cdb67) · 9/33 checks passing

supports-pypy: no · license: BSD License · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: 0.3.2 (2023-03-28) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python is not declared
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [wheel]
- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: .coveragerc
- ❌ [`hatchling`](REPORT.md#hatchling): no build-backend in pyproject.toml
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-auth`](REPORT.md#codecov-auth): expected OIDC, found tokenless in .github/workflows/main.yml
- ❌ [`codecov-status`](REPORT.md#codecov-status): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`pre-commit-tox`](REPORT.md#pre-commit-tox): no tox environment runs pre-commit run --all-files
- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/main.yml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): .github/workflows/publish.yml is triggered by GitHub releases
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): only legacy (bump2version) configuration, in .bumpversion.cfg

## Forms

### scrapy/form2request

[Repository](https://github.com/scrapy/form2request) · commit [`93af5f1`](https://github.com/scrapy/form2request/commit/93af5f15b9b0c5a0cd0cbddbc404c9ee28006578) · 34/47 checks passing

supports-pypy: no · license: Apache-2.0 · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: yes · latest-release: 0.2.0 (2024-07-15) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): has license classifiers: License :: OSI Approved :: Apache Software License
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, changelog

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Documentation**

- ❌ [`no-docs-requirements`](REPORT.md#no-docs-requirements): found docs/requirements.txt
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py
- ❌ [`docs-stable-links`](REPORT.md#docs-stable-links): links to latest in README.rst; latest in pyproject.toml
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

### scrapinghub/Formasaurus

[Repository](https://github.com/scrapinghub/Formasaurus) · commit [`4bb46a9`](https://github.com/scrapinghub/Formasaurus/commit/4bb46a95c7851622bb63ca7459d4d6d2587297ab) · 12/37 checks passing

supports-pypy: no · license: MIT License · mypy: no · pyrefly: no · pylint: no · has-sphinx-docs: yes · latest-release: 0.10.0 (2024-11-07) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.13, 3.14, 3.15

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [bdist_wheel]
- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: .coveragerc, .flake8; tool sections in setup.cfg: [isort]
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`type-checker`](REPORT.md#type-checker): no type checker found

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort, pyupgrade
- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml
- ❌ [`blacken-docs`](REPORT.md#blacken-docs): missing pre-commit hooks: blacken-docs
- ❌ [`sphinx-lint`](REPORT.md#sphinx-lint): missing pre-commit hooks: sphinx-lint

**Documentation**

- ❌ [`no-docs-requirements`](REPORT.md#no-docs-requirements): found docs/requirements.txt
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py
- ❌ [`readthedocs`](REPORT.md#readthedocs): the README does not link to Formasaurus.readthedocs.io or Formasaurus.readthedocs.org
- ❌ [`changelog-date`](REPORT.md#changelog-date): no file replacement of (unreleased) with {now:%Y-%m-%d}
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes

### scrapinghub/sklearn-crfsuite

[Repository](https://github.com/scrapinghub/sklearn-crfsuite) · commit [`e18a02a`](https://github.com/scrapinghub/sklearn-crfsuite/commit/e18a02ae11b61f703c0ec460c44cfdd90db00591) · 10/35 checks passing

supports-pypy: no · license: MIT License · mypy: no · pyrefly: no · pylint: no · has-sphinx-docs: yes · latest-release: 0.5.0 (2024-06-18) · unreleased-changes: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python is not declared
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [bdist_wheel]
- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: .coveragerc, .flake8
- ❌ [`hatchling`](REPORT.md#hatchling): no pyproject.toml

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`type-checker`](REPORT.md#type-checker): no type checker found

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort, pyupgrade
- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml
- ❌ [`blacken-docs`](REPORT.md#blacken-docs): missing pre-commit hooks: blacken-docs
- ❌ [`sphinx-lint`](REPORT.md#sphinx-lint): missing pre-commit hooks: sphinx-lint

**Documentation**

- ❌ [`no-docs-requirements`](REPORT.md#no-docs-requirements): found docs/requirements.txt
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py
- ❌ [`readthedocs`](REPORT.md#readthedocs): no .readthedocs.yml
- ❌ [`docs-stable-links`](REPORT.md#docs-stable-links): links to latest in README.rst
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): only legacy (bump2version) configuration, in .bumpversion.cfg

### scrapinghub/python-crfsuite

[Repository](https://github.com/scrapinghub/python-crfsuite) · commit [`d3ee2eb`](https://github.com/scrapinghub/python-crfsuite/commit/d3ee2eba443d5d3b313741bed5076b5a36a840d1) · 8/35 checks passing

supports-pypy: no · license: MIT License · mypy: no · pyrefly: no · pylint: no · has-sphinx-docs: yes · latest-release: 0.9.12 (2025-12-23) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): setup.py exists
- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: .flake8
- ❌ [`pep639-license`](REPORT.md#pep639-license): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: MIT License
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, changelog, documentation
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`type-checker`](REPORT.md#type-checker): no type checker found

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml
- ❌ [`actionlint`](REPORT.md#actionlint): no .pre-commit-config.yaml
- ❌ [`zizmor`](REPORT.md#zizmor): no .pre-commit-config.yaml
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/build_and_upload.yml, .github/workflows/tests.yml
- ❌ [`blacken-docs`](REPORT.md#blacken-docs): no .pre-commit-config.yaml
- ❌ [`sphinx-lint`](REPORT.md#sphinx-lint): no .pre-commit-config.yaml

**Documentation**

- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py
- ❌ [`readthedocs`](REPORT.md#readthedocs): no .readthedocs.yml; the README does not link to python-crfsuite.readthedocs.io or python-crfsuite.readthedocs.org
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/build_and_upload.yml: job 'upload_to_pypi' has no environment; .github/workflows/build_and_upload.yml uses an API token; .github/workflows/build_and_upload.yml lacks the id-token: write permission
- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): .github/workflows/build_and_upload.yml is triggered by GitHub releases

## Monitoring

### scrapinghub/spidermon

[Repository](https://github.com/scrapinghub/spidermon) · commit [`5bac6dd`](https://github.com/scrapinghub/spidermon/commit/5bac6dd768463ece308ca67dc9fd18525364c940) · 29/46 checks passing

supports-pypy: no · license: BSD-3-Clause · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: yes · latest-release: 1.27.0 (2026-08-10) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): has license classifiers: License :: OSI Approved :: BSD License

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-auth`](REPORT.md#codecov-auth): expected OIDC, found token in .github/workflows/main.yml
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`pre-commit-tox`](REPORT.md#pre-commit-tox): no tox environment runs pre-commit run --all-files
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor

**Documentation**

- ❌ [`no-docs-requirements`](REPORT.md#no-docs-requirements): found docs/requirements.txt
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py
- ❌ [`docs-stable-links`](REPORT.md#docs-stable-links): links to latest in README.rst; latest in pyproject.toml
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapy-plugins/zyte-spidermon

[Repository](https://github.com/scrapy-plugins/zyte-spidermon) · commit [`8186fbe`](https://github.com/scrapy-plugins/zyte-spidermon/commit/8186fbe6d1c9233dc576ec725d3b2e046de032dd) · 2/26 checks passing

supports-pypy: no · license: no · mypy: no · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python is not declared
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists
- ❌ [`hatchling`](REPORT.md#hatchling): no pyproject.toml
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`type-checker`](REPORT.md#type-checker): no type checker found

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml
- ❌ [`actionlint`](REPORT.md#actionlint): no .pre-commit-config.yaml
- ❌ [`zizmor`](REPORT.md#zizmor): no .pre-commit-config.yaml
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/main.yml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ❌ [`readme-rst`](REPORT.md#readme-rst): README.md instead
- ❌ [`changelog`](REPORT.md#changelog): no changelog file
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): no workflow publishes to PyPI
- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): no workflow publishes to PyPI
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): no workflow publishes to PyPI
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml

## AI agents

### scrapy/scrapy-agent-plugin

[Repository](https://github.com/scrapy/scrapy-agent-plugin) · commit [`d424e42`](https://github.com/scrapy/scrapy-agent-plugin/commit/d424e42a35116c108e986614b75ec7cd9cf9909e) · 4/5 checks passing

has-sphinx-docs: no

**Documentation**

- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

### scrapy/scrapy-mcp-official

[Repository](https://github.com/scrapy/scrapy-mcp-official) · commit [`66aeef9`](https://github.com/scrapy/scrapy-mcp-official/commit/66aeef96b7707072811132e33400b08cb45cff37) · 33/41 checks passing

supports-pypy: no · license: Apache-2.0 · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: 0.1.2 (2026-09-07) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/checks.yml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ❌ [`readme-rst`](REPORT.md#readme-rst): README.md instead
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

### zytedata/agent-exam

[Repository](https://github.com/zytedata/agent-exam) · commit [`e25c638`](https://github.com/zytedata/agent-exam/commit/e25c6380c59e5386caa7085795af12d2dbd2931c) · 30/47 checks passing

supports-pypy: no · license: Apache-2.0 · mypy: no · pyrefly: no · pylint: no · has-sphinx-docs: yes · latest-release: 0.3.0 (2026-10-20) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): has license classifiers: License :: OSI Approved :: Apache Software License
- ❌ [`sdist-contents`](REPORT.md#sdist-contents): no include in [tool.hatch.build.targets.sdist]
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`type-checker`](REPORT.md#type-checker): no type checker found

**Tests and coverage**

- ❌ [`codecov-status`](REPORT.md#codecov-status): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`dependabot`](REPORT.md#dependabot): no .github/dependabot.yml
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/ci.yml

**Documentation**

- ❌ [`readme-rst`](REPORT.md#readme-rst): README.md instead
- ❌ [`no-docs-requirements`](REPORT.md#no-docs-requirements): found docs/requirements.in, docs/requirements.txt
- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.8.10, latest is 0.15.0
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### zytedata/claude-measure-usage

[Repository](https://github.com/zytedata/claude-measure-usage) · commit [`6b4310a`](https://github.com/zytedata/claude-measure-usage/commit/6b4310afeaf2e9c81acd861f8d9bd62006357bf7) · 18/37 checks passing

supports-pypy: no · license: Apache-2.0 · mypy: no · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: 0.1.1 (2026-09-14) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`sdist-contents`](REPORT.md#sdist-contents): not included: docs, tox.ini
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: changelog
- ❌ [`twine-check`](REPORT.md#twine-check): twine check runs in a workflow, not in tox

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`type-checker`](REPORT.md#type-checker): no type checker found

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff-rules`](REPORT.md#ruff-rules): only the default rules are enabled
- ❌ [`pre-commit-tox`](REPORT.md#pre-commit-tox): no tox environment runs pre-commit run --all-files
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/tests.yml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py; Markdown files: docs/tui-ux.md
- ❌ [`readme-rst`](REPORT.md#readme-rst): README.md instead
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

### zytedata/harness-run

[Repository](https://github.com/zytedata/harness-run) · commit [`cc11c24`](https://github.com/zytedata/harness-run/commit/cc11c24d5494bdca045f3cf0f08d5d119918b77e) · 11/31 checks passing

supports-pypy: no · license: Apache-2.0 · mypy: no · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: 0.4.0 (2026-09-23) · unreleased-changes: yes

**Python versions**

- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.14, 3.15

**Packaging**

- ❌ [`sdist-contents`](REPORT.md#sdist-contents): no include in [tool.hatch.build.targets.sdist]
- ❌ [`twine-check`](REPORT.md#twine-check): twine check runs in a workflow, not in tox

**Dependencies**

- ❌ [`dependency-lower-bounds`](REPORT.md#dependency-lower-bounds): no lower bound: google-cloud-storage, google-auth, packaging, pyyaml, jsonschema
- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`type-checker`](REPORT.md#type-checker): no type checker found

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml
- ❌ [`ruff-rules`](REPORT.md#ruff-rules): only the default rules are enabled
- ❌ [`actionlint`](REPORT.md#actionlint): no .pre-commit-config.yaml
- ❌ [`zizmor`](REPORT.md#zizmor): no .pre-commit-config.yaml

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py; Markdown files: docs/configuration.md, docs/gcp-setup.md, docs/getting-started.md, docs/harnesses-and-models.md, docs/local-runtime.md, docs/observability.md, docs/openrouter.md, docs/runs-and-sessions.md, docs/sandbox-runtime.md, docs/secrets-and-security.md, docs/structured-output.md
- ❌ [`readme-rst`](REPORT.md#readme-rst): README.md instead
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`bump-my-version`](REPORT.md#bump-my-version): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml

### scrapy/sphinx-llm-friendly

[Repository](https://github.com/scrapy/sphinx-llm-friendly) · commit [`4672e79`](https://github.com/scrapy/sphinx-llm-friendly/commit/4672e792d58f8c9a6929e7580fe9d6026dc453fa) · 24/38 checks passing

supports-pypy: no · license: MIT · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: 0.7.0 (2026-10-03) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10

**Packaging**

- ❌ [`sdist-contents`](REPORT.md#sdist-contents): not included: tox.ini
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`dependency-lower-bounds`](REPORT.md#dependency-lower-bounds): no lower bound: docutils, tabulate

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`pre-commit-tox`](REPORT.md#pre-commit-tox): no tox environment runs pre-commit run --all-files
- ❌ [`pre-commit-updates`](REPORT.md#pre-commit-updates): outdated: ruff v0.11.13 (0.15.12 or later expected)

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

## Maintenance

### scrapy/sphinx-scrapy

[Repository](https://github.com/scrapy/sphinx-scrapy) · commit [`a740c8e`](https://github.com/scrapy/sphinx-scrapy/commit/a740c8e0f53c96209f65fa5f444eb3a02ca7b94b) · 21/38 checks passing

supports-pypy: no · license: BSD-3-Clause · mypy: yes · pyrefly: no · pylint: no · has-sphinx-docs: no · latest-release: 0.15.0 (2026-10-27) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`sdist-contents`](REPORT.md#sdist-contents): no include in [tool.hatch.build.targets.sdist]
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`dependency-lower-bounds`](REPORT.md#dependency-lower-bounds): no lower bound: docutils, packaging, sphinx-copybutton, sphinx-design, sphinx-sitemap, sphinxcontrib-youtube, tomli
- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`pre-commit-tox`](REPORT.md#pre-commit-tox): no tox environment runs pre-commit run --all-files
- ❌ [`pre-commit-updates`](REPORT.md#pre-commit-updates): outdated: ruff v0.11.13 (0.15.12 or later expected)

**Documentation**

- ❌ [`sphinx-docs`](REPORT.md#sphinx-docs): no docs/conf.py
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapy/unattended-pr-guard

[Repository](https://github.com/scrapy/unattended-pr-guard) · commit [`f15191e`](https://github.com/scrapy/unattended-pr-guard/commit/f15191eebabc3dc4421f8fd205660e9040ef504e) · 9/13 checks passing

has-sphinx-docs: no

**Linting**

- ❌ [`pre-commit-tox`](REPORT.md#pre-commit-tox): no tox environment runs pre-commit run --all-files
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/ci.yml

**Documentation**

- ❌ [`readme-rst`](REPORT.md#readme-rst): README.md instead
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

### zytedata/zyte-oss-maintenance

[Repository](https://github.com/zytedata/zyte-oss-maintenance) · commit [`5383946`](https://github.com/zytedata/zyte-oss-maintenance/commit/5383946efcd3c8a4a51d782739b565f59b6bb786) · 16/23 checks passing

supports-pypy: no · license: Apache-2.0 · mypy: no · pyrefly: yes · pylint: no · has-sphinx-docs: no

**Python versions**

- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Documentation**

- ❌ [`readme-rst`](REPORT.md#readme-rst): README.md instead
- ⚠️ [`no-wiki`](REPORT.md#no-wiki): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
