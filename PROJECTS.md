# Maintenance report by project

Generated on 2026-10-09 with `oss-maint report`. Do not edit by hand. Lists failing checks and notes for each project; see [REPORT.md](REPORT.md) for all results.

## Scrapy and its deps

### scrapy/scrapy

[Repository](https://github.com/scrapy/scrapy) · commit [`be7bdc4`](https://github.com/scrapy/scrapy/commit/be7bdc4cd16644018fa56ef3503dce86744fa6d5) · 28/32 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: yes

**Python versions**

- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Dependencies**

- ❌ [`dependency-lower-bounds`](REPORT.md#dependency-lower-bounds): no lower bound: packaging, tldextract

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Linting**

- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint

### scrapy/cssselect

[Repository](https://github.com/scrapy/cssselect) · commit [`d1f8b2a`](https://github.com/scrapy/cssselect/commit/d1f8b2a771a6976efea0038ac3e9b8efb85cfef7) · 20/28 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15
- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in

### scrapy/formerly

[Repository](https://github.com/scrapy/formerly) · commit [`1286733`](https://github.com/scrapy/formerly/commit/1286733c171d2138bc6dcb59b49ee4df5228fd40) · 18/24 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: no · has-sphinx-docs: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15
- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Linting**

- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint

### scrapy/itemadapter

[Repository](https://github.com/scrapy/itemadapter) · commit [`ef0b748`](https://github.com/scrapy/itemadapter/commit/ef0b748c57de506a0524db06537e006a207a40b5) · 20/25 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: no

**Python versions**

- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapy/itemloaders

[Repository](https://github.com/scrapy/itemloaders) · commit [`f3e6800`](https://github.com/scrapy/itemloaders/commit/f3e680016d0fd49f24a656f440938ec14c0cd9db) · 20/30 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15
- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in

**Releases**

- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): .github/workflows/publish.yml is triggered by GitHub releases
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapy/parsel

[Repository](https://github.com/scrapy/parsel) · commit [`8ee96b7`](https://github.com/scrapy/parsel/commit/8ee96b7239775b4dbf214fd17e51d49e95538f16) · 28/32 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): has license classifiers: License :: OSI Approved :: BSD License

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

### scrapy/protego

[Repository](https://github.com/scrapy/protego) · commit [`53d6df8`](https://github.com/scrapy/protego/commit/53d6df88ea74a29561d4c415d45ee77ddc86c1af) · 21/24 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: no · has-sphinx-docs: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

### scrapy/queuelib

[Repository](https://github.com/scrapy/queuelib) · commit [`885ef61`](https://github.com/scrapy/queuelib/commit/885ef61c6ad9b61682329074f539cbb8c262a580) · 21/24 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

### scrapy/w3lib

[Repository](https://github.com/scrapy/w3lib) · commit [`ade4b62`](https://github.com/scrapy/w3lib/commit/ade4b62e55da45a8e5ead6ed21dcdedd018b9672) · 23/28 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: yes

**Python versions**

- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in

### scrapy/sphinx-scrapy

[Repository](https://github.com/scrapy/sphinx-scrapy) · commit [`52f1427`](https://github.com/scrapy/sphinx-scrapy/commit/52f14275a06d15b7de3b6ecadacbd7ff46ac4764) · 12/23 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

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

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapy/sphinx-llm-friendly

[Repository](https://github.com/scrapy/sphinx-llm-friendly) · commit [`2f5b77c`](https://github.com/scrapy/sphinx-llm-friendly/commit/2f5b77c315d5230429761063b475c7c1b015ca79) · 15/23 checks passing

supports-pypy: no · license: MIT · pylint: no · has-sphinx-docs: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10

**Packaging**

- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`dependency-lower-bounds`](REPORT.md#dependency-lower-bounds): no lower bound: docutils, tabulate

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

## scrapy-poet and its deps

### scrapinghub/scrapy-poet

[Repository](https://github.com/scrapinghub/scrapy-poet) · commit [`261e297`](https://github.com/scrapinghub/scrapy-poet/commit/261e297ce06c5b1687c6560c84b4e934d6cdcb74) · 21/30 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: yes

**Python versions**

- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): has license classifiers: License :: OSI Approved :: BSD License

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results

**Linting**

- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.8.4, latest is 0.13.0

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapinghub/andi

[Repository](https://github.com/scrapinghub/andi) · commit [`7a07b33`](https://github.com/scrapinghub/andi/commit/7a07b339ca1cc5e3c6495635b02eb01b5c483ebd) · 20/22 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

### scrapinghub/web-poet

[Repository](https://github.com/scrapinghub/web-poet) · commit [`b3cc347`](https://github.com/scrapinghub/web-poet/commit/b3cc347952b9bc6cf534e44543b789d2f5f2fafb) · 19/30 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): has license classifiers: License :: OSI Approved :: BSD License

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch

**Linting**

- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.8.12, latest is 0.13.0

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes

### zytedata/url-matcher

[Repository](https://github.com/zytedata/url-matcher) · commit [`b55ff5c`](https://github.com/zytedata/url-matcher/commit/b55ff5cc14b3346be16edf9e6faa603ebdfbf216) · 26/30 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

## Zyte API

### scrapy-plugins/scrapy-zyte-api

[Repository](https://github.com/scrapy-plugins/scrapy-zyte-api) · commit [`2b15197`](https://github.com/scrapy-plugins/scrapy-zyte-api/commit/2b151972c7fa6412cf552d5c46a59e601d036e59) · 25/30 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: yes

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.8.12, latest is 0.13.0

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### zytedata/python-zyte-api

[Repository](https://github.com/zytedata/python-zyte-api) · commit [`efc4fdc`](https://github.com/zytedata/python-zyte-api/commit/efc4fdc6cebf36de26a946d0e665d539cafbecf9) · 23/30 checks passing

supports-pypy: no · license: BSD License · pylint: no · has-sphinx-docs: yes

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results

**Linting**

- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapy-plugins/scrapy-zyte-smartproxy

[Repository](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) · commit [`debd444`](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy/commit/debd4445343d0c3a1eba9fa0ce269613bb3b9d5c) · 7/24 checks passing

supports-pypy: no · license: BSD License · pylint: no · has-sphinx-docs: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.14, 3.15

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists
- ❌ [`hatchling`](REPORT.md#hatchling): no build-backend in pyproject.toml

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`blacken-docs`](REPORT.md#blacken-docs): missing pre-commit hooks: blacken-docs
- ❌ [`sphinx-lint`](REPORT.md#sphinx-lint): missing pre-commit hooks: sphinx-lint

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### zytedata/zyte-common-items

[Repository](https://github.com/zytedata/zyte-common-items) · commit [`1309123`](https://github.com/zytedata/zyte-common-items/commit/13091232ca4eb0b260a45c68f90a0e42d521d811) · 16/30 checks passing

supports-pypy: no · license: BSD License · pylint: no · has-sphinx-docs: yes

**Python versions**

- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): no license field; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch

**Linting**

- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy-pins`](REPORT.md#sphinx-scrapy-pins): not pinned in tox, docs/requirements.in, .pre-commit-config.yaml
- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): not pinned

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes

### zytedata/zyte-parsers

[Repository](https://github.com/zytedata/zyte-parsers) · commit [`4f5d08d`](https://github.com/zytedata/zyte-parsers/commit/4f5d08d1be951fa438f0aedd598d61a61c360ea0) · 20/28 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Dependencies**

- ❌ [`dependency-lower-bounds`](REPORT.md#dependency-lower-bounds): no lower bound: html-text, lxml, parsel, six, w3lib
- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in

### zytedata/clear-html

[Repository](https://github.com/zytedata/clear-html) · commit [`6b820b1`](https://github.com/zytedata/clear-html/commit/6b820b13221145ceb0814e47e9583e5574d28865) · 20/24 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

### zytedata/html-text

[Repository](https://github.com/zytedata/html-text) · commit [`2dc4e94`](https://github.com/zytedata/html-text/commit/2dc4e94dd92a8b15476a237f0a1693b051f53d6f) · 13/24 checks passing

supports-pypy: no · license: MIT · pylint: no · has-sphinx-docs: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Dependencies**

- ❌ [`dependency-lower-bounds`](REPORT.md#dependency-lower-bounds): no lower bound: lxml, lxml-html-clean
- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results

**Linting**

- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes

### scrapinghub/price-parser

[Repository](https://github.com/scrapinghub/price-parser) · commit [`6718bfe`](https://github.com/scrapinghub/price-parser/commit/6718bfe8447f2de17ecc152d3ad2a4c51520c755) · 14/24 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results

**Linting**

- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml uses an API token
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

## Scrapy Cloud

### scrapinghub/python-scrapinghub

[Repository](https://github.com/scrapinghub/python-scrapinghub) · commit [`d0d7b29`](https://github.com/scrapinghub/python-scrapinghub/commit/d0d7b29153e40bbb0f9c56ab23caab86393f853e) · 9/27 checks passing

supports-pypy: yes · license: BSD License · pylint: no · has-sphinx-docs: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.14, 3.15
- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [metadata], [bdist_wheel]
- ❌ [`hatchling`](REPORT.md#hatchling): no build-backend in pyproject.toml
- ❌ [`twine-check`](REPORT.md#twine-check): twine check runs in a workflow, not in tox

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`blacken-docs`](REPORT.md#blacken-docs): missing pre-commit hooks: blacken-docs
- ❌ [`sphinx-lint`](REPORT.md#sphinx-lint): missing pre-commit hooks: sphinx-lint

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.7.1, latest is 0.13.0

### scrapinghub/shub

[Repository](https://github.com/scrapinghub/shub) · commit [`80a4cad`](https://github.com/scrapinghub/shub/commit/80a4cad661f2a669739c8c3805fd33c67e62674e) · 10/28 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): has license classifiers: License :: OSI Approved :: BSD License
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`dependency-lower-bounds`](REPORT.md#dependency-lower-bounds): no lower bound: click, docker, importlib-metadata, packaging, pip, PyYAML, requests, retrying, setuptools, toml

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`blacken-docs`](REPORT.md#blacken-docs): missing pre-commit hooks: blacken-docs
- ❌ [`sphinx-lint`](REPORT.md#sphinx-lint): missing pre-commit hooks: sphinx-lint

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.8.4, latest is 0.13.0

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml publishes with twine upload
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapinghub/scrapinghub-entrypoint-scrapy

[Repository](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) · commit [`bf9632c`](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy/commit/bf9632c78355b545126363ce557106c1b9c3bb54) · 3/19 checks passing

supports-pypy: no · license: BSD License · pylint: no · has-sphinx-docs: no

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
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml
- ❌ [`actionlint`](REPORT.md#actionlint): no .pre-commit-config.yaml
- ❌ [`zizmor`](REPORT.md#zizmor): no .pre-commit-config.yaml

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml publishes with twine upload
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

## Others

### scrapy/form2request

[Repository](https://github.com/scrapy/form2request) · commit [`a251597`](https://github.com/scrapy/form2request/commit/a251597d9fa44cbd03736ec1da37f85593dfe820) · 21/28 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): has license classifiers: License :: OSI Approved :: Apache Software License

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in

### scrapy/frostwork

[Repository](https://github.com/scrapy/frostwork) · commit [`d8ef1a1`](https://github.com/scrapy/frostwork/commit/d8ef1a1b7bcb76a60821bf13fe7d19e224bc01a9) · 13/20 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format

### scrapy/scrapy-agent-plugin

[Repository](https://github.com/scrapy/scrapy-agent-plugin) · commit [`d424e42`](https://github.com/scrapy/scrapy-agent-plugin/commit/d424e42a35116c108e986614b75ec7cd9cf9909e) · 1/1 checks passing

has-sphinx-docs: no

All applicable checks pass.

### scrapy/scrapy-lint

[Repository](https://github.com/scrapy/scrapy-lint) · commit [`30a3872`](https://github.com/scrapy/scrapy-lint/commit/30a387279f0be38a48237d31725b1d52a2bcf297) · 18/29 checks passing

supports-pypy: no · license: MIT · pylint: yes · has-sphinx-docs: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch

**Linting**

- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy-pins`](REPORT.md#sphinx-scrapy-pins): not pinned in tox, docs/requirements.in, .pre-commit-config.yaml
- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): not pinned

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapy/scrapy-mcp-official

[Repository](https://github.com/scrapy/scrapy-mcp-official) · commit [`5530c67`](https://github.com/scrapy/scrapy-mcp-official/commit/5530c671a7078f4f06479422c623d10b846d3db9) · 22/24 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

### scrapy/unattended-pr-guard

[Repository](https://github.com/scrapy/unattended-pr-guard) · commit [`1e3c311`](https://github.com/scrapy/unattended-pr-guard/commit/1e3c31134253813934af43f3505d4492eee26c2a) · 3/3 checks passing

has-sphinx-docs: no

All applicable checks pass.

### scrapy/xtractmime

[Repository](https://github.com/scrapy/xtractmime) · commit [`9d50fcb`](https://github.com/scrapy/xtractmime/commit/9d50fcb0d7abd7a96f7dee746d9285faba4af6db) · 15/23 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: no · has-sphinx-docs: no

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
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch

### scrapy-plugins/scrapy-download-handlers-incubator

[Repository](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) · commit [`f585f8d`](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator/commit/f585f8da60d14ec804c4b3b7d105c4ce55d5238b) · 23/24 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: no

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

### scrapy-plugins/scrapy-playwright

[Repository](https://github.com/scrapy-plugins/scrapy-playwright) · commit [`d99f38d`](https://github.com/scrapy-plugins/scrapy-playwright/commit/d99f38d3483118881add4e2bcbc595d45091f196) · 8/23 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml
- ❌ [`actionlint`](REPORT.md#actionlint): no .pre-commit-config.yaml
- ❌ [`zizmor`](REPORT.md#zizmor): no .pre-commit-config.yaml

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml publishes with twine upload
- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): .github/workflows/publish.yml is triggered by GitHub releases
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapy-plugins/scrapy-spider-metadata

[Repository](https://github.com/scrapy-plugins/scrapy-spider-metadata) · commit [`63b3991`](https://github.com/scrapy-plugins/scrapy-spider-metadata/commit/63b3991dc8f181b2ef358e3b09aeda13261dd7c3) · 14/30 checks passing

supports-pypy: yes · license: BSD License · pylint: no · has-sphinx-docs: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.14, 3.15
- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results

**Linting**

- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`blacken-docs`](REPORT.md#blacken-docs): missing pre-commit hooks: blacken-docs
- ❌ [`sphinx-lint`](REPORT.md#sphinx-lint): missing pre-commit hooks: sphinx-lint

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes

### scrapy-plugins/zyte-spidermon

[Repository](https://github.com/scrapy-plugins/zyte-spidermon) · commit [`8186fbe`](https://github.com/scrapy-plugins/zyte-spidermon/commit/8186fbe6d1c9233dc576ec725d3b2e046de032dd) · 1/18 checks passing

supports-pypy: no · license: no · pylint: no · has-sphinx-docs: no

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
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml
- ❌ [`actionlint`](REPORT.md#actionlint): no .pre-commit-config.yaml
- ❌ [`zizmor`](REPORT.md#zizmor): no .pre-commit-config.yaml

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): no workflow publishes to PyPI
- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): no workflow publishes to PyPI
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): no workflow publishes to PyPI
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml

### scrapinghub/dateparser

[Repository](https://github.com/scrapinghub/dateparser) · commit [`fed9cf9`](https://github.com/scrapinghub/dateparser/commit/fed9cf94e9d8a1128b396f01ca66f4a303f03ee4) · 13/27 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): setup.py exists
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch

**Linting**

- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`blacken-docs`](REPORT.md#blacken-docs): missing pre-commit hooks: blacken-docs
- ❌ [`sphinx-lint`](REPORT.md#sphinx-lint): missing pre-commit hooks: sphinx-lint

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in

**Releases**

- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): .github/workflows/publish.yml is triggered by GitHub releases

### scrapinghub/extruct

[Repository](https://github.com/scrapinghub/extruct) · commit [`dc3bf7d`](https://github.com/scrapinghub/extruct/commit/dc3bf7d2209ecf421222afc90d3d2dd8c6fd23cf) · 5/20 checks passing

supports-pypy: no · license: BSD License · pylint: no · has-sphinx-docs: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.8' allows 3.8 (EOL 2024-10-07), 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.8, 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.13, 3.14, 3.15

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [wheel]
- ❌ [`hatchling`](REPORT.md#hatchling): no build-backend in pyproject.toml

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, isort, pyupgrade
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/python-publish.yml publishes with twine upload
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/python-publish.yml: job 'deploy' builds and publishes
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): only legacy (bump2version) configuration, in setup.cfg

### scrapinghub/number-parser

[Repository](https://github.com/scrapinghub/number-parser) · commit [`a126357`](https://github.com/scrapinghub/number-parser/commit/a1263578628a7743054879095e50532fba1cdb67) · 4/19 checks passing

supports-pypy: no · license: BSD License · pylint: no · has-sphinx-docs: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python is not declared
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [wheel]
- ❌ [`hatchling`](REPORT.md#hatchling): no build-backend in pyproject.toml
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results

**Linting**

- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml publishes with twine upload
- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): .github/workflows/publish.yml is triggered by GitHub releases
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): only legacy (bump2version) configuration, in .bumpversion.cfg

### scrapinghub/scrapyrt

[Repository](https://github.com/scrapinghub/scrapyrt) · commit [`6d00a0a`](https://github.com/scrapinghub/scrapyrt/commit/6d00a0ad55c310c268fb13a151a3f3c98f0cabb4) · 14/29 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: yes

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

**Linting**

- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy-pins`](REPORT.md#sphinx-scrapy-pins): not pinned in tox, docs/requirements.in, .pre-commit-config.yaml
- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): not pinned

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml uses an API token
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapinghub/spidermon

[Repository](https://github.com/scrapinghub/spidermon) · commit [`4b9a8ff`](https://github.com/scrapinghub/spidermon/commit/4b9a8ffe16c30a0f61461f1570055c1b8dfded72) · 16/27 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: yes

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

**Linting**

- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### zytedata/agent-exam

[Repository](https://github.com/zytedata/agent-exam) · commit [`c88fec1`](https://github.com/zytedata/agent-exam/commit/c88fec170ff9683dad9d769601206088fdbaeb7d) · 17/28 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): has license classifiers: License :: OSI Approved :: Apache Software License

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.8.10, latest is 0.13.0

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### zytedata/claude-measure-usage

[Repository](https://github.com/zytedata/claude-measure-usage) · commit [`6b4310a`](https://github.com/zytedata/claude-measure-usage/commit/6b4310afeaf2e9c81acd861f8d9bd62006357bf7) · 12/22 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`twine-check`](REPORT.md#twine-check): twine check runs in a workflow, not in tox

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch

### zytedata/duplicate-url-discarder

[Repository](https://github.com/zytedata/duplicate-url-discarder) · commit [`8db08b3`](https://github.com/zytedata/duplicate-url-discarder/commit/8db08b3edf638f34ee6ad7393612f579b5bfb90f) · 10/24 checks passing

supports-pypy: no · license: BSD License · pylint: no · has-sphinx-docs: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.14, 3.15

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): only legacy (bump2version) configuration, in .bumpversion.cfg

### zytedata/harness-run

[Repository](https://github.com/zytedata/harness-run) · commit [`4028849`](https://github.com/zytedata/harness-run/commit/4028849faf48ac448b1634140cfe3a9cac8f2749) · 8/22 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: no

**Python versions**

- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.14, 3.15

**Packaging**

- ❌ [`twine-check`](REPORT.md#twine-check): twine check runs in a workflow, not in tox

**Dependencies**

- ❌ [`dependency-lower-bounds`](REPORT.md#dependency-lower-bounds): no lower bound: google-cloud-storage, google-auth, packaging, pyyaml, jsonschema
- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml
- ❌ [`actionlint`](REPORT.md#actionlint): no .pre-commit-config.yaml
- ❌ [`zizmor`](REPORT.md#zizmor): no .pre-commit-config.yaml

**Releases**

- ❌ [`bump-my-version`](REPORT.md#bump-my-version): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml
