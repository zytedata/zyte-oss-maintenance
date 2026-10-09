# Maintenance report

Generated on 2026-10-09 with `oss-maint report`. Do not edit by hand. See [PROJECTS.md](PROJECTS.md) for what fails in each project.

✅ passes · ❌ fails · ➖ not applicable · ⚠️ check error · yes/no or a value: result of an informational check. Click a symbol for details.

## Summary

Checks passing per group.

| Project | [Python versions](#python-versions) | [Packaging](#packaging) | [Dependencies](#dependencies) | [Typing](#typing) | [Tests and coverage](#tests-and-coverage) | [Linting](#linting) | [Releases](#releases) | Failing | Commit |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | --- |
| **Scrapy and its deps** | | | | | | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | [❌ 5/6](#python-versions) | [✅ 5/5](#packaging) | [❌ 1/2](#dependencies) | [❌ 3/4](#typing) | [✅ 3/3](#tests-and-coverage) | [❌ 4/5](#linting) | [✅ 4/4](#releases) | [4](PROJECTS.md#scrapyscrapy) | [`2c9804b`](https://github.com/scrapy/scrapy/commit/2c9804b93a90930403e8278c716e72d97033e4b0) |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | [❌ 3/6](#python-versions) | [✅ 5/5](#packaging) | [➖](#dependencies) | [❌ 3/4](#typing) | [❌ 2/3](#tests-and-coverage) | [✅ 5/5](#linting) | [✅ 4/4](#releases) | [5](PROJECTS.md#scrapycssselect) | [`cf86ab9`](https://github.com/scrapy/cssselect/commit/cf86ab900281f97be409bcb21c6ee25a49a58ed1) |
| [scrapy/formerly](https://github.com/scrapy/formerly) | [❌ 3/6](#python-versions) | [✅ 5/5](#packaging) | [➖](#dependencies) | [❌ 3/4](#typing) | [✅ 3/3](#tests-and-coverage) | [❌ 2/3](#linting) | [✅ 4/4](#releases) | [5](PROJECTS.md#scrapyformerly) | [`1286733`](https://github.com/scrapy/formerly/commit/1286733c171d2138bc6dcb59b49ee4df5228fd40) |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | [❌ 5/6](#python-versions) | [✅ 5/5](#packaging) | [✅ 1/1](#dependencies) | [❌ 2/4](#typing) | [❌ 2/3](#tests-and-coverage) | [✅ 3/3](#linting) | [❌ 3/4](#releases) | [5](PROJECTS.md#scrapyitemadapter) | [`ef0b748`](https://github.com/scrapy/itemadapter/commit/ef0b748c57de506a0524db06537e006a207a40b5) |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | [❌ 3/6](#python-versions) | [✅ 5/5](#packaging) | [✅ 2/2](#dependencies) | [❌ 3/4](#typing) | [❌ 2/3](#tests-and-coverage) | [✅ 5/5](#linting) | [❌ 2/4](#releases) | [7](PROJECTS.md#scrapyitemloaders) | [`f3e6800`](https://github.com/scrapy/itemloaders/commit/f3e680016d0fd49f24a656f440938ec14c0cd9db) |
| [scrapy/parsel](https://github.com/scrapy/parsel) | [❌ 4/6](#python-versions) | [❌ 4/5](#packaging) | [✅ 2/2](#dependencies) | [❌ 3/4](#typing) | [✅ 3/3](#tests-and-coverage) | [✅ 5/5](#linting) | [✅ 4/4](#releases) | [4](PROJECTS.md#scrapyparsel) | [`f88185d`](https://github.com/scrapy/parsel/commit/f88185d022e220e4c1e6107bd0ff2912d190e1dc) |
| [scrapy/protego](https://github.com/scrapy/protego) | [❌ 4/6](#python-versions) | [✅ 5/5](#packaging) | [➖](#dependencies) | [❌ 3/4](#typing) | [✅ 3/3](#tests-and-coverage) | [✅ 3/3](#linting) | [✅ 4/4](#releases) | [3](PROJECTS.md#scrapyprotego) | [`53d6df8`](https://github.com/scrapy/protego/commit/53d6df88ea74a29561d4c415d45ee77ddc86c1af) |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | [❌ 4/6](#python-versions) | [✅ 5/5](#packaging) | [➖](#dependencies) | [❌ 3/4](#typing) | [✅ 3/3](#tests-and-coverage) | [✅ 3/3](#linting) | [✅ 4/4](#releases) | [3](PROJECTS.md#scrapyqueuelib) | [`885ef61`](https://github.com/scrapy/queuelib/commit/885ef61c6ad9b61682329074f539cbb8c262a580) |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | [❌ 5/6](#python-versions) | [✅ 5/5](#packaging) | [➖](#dependencies) | [❌ 3/4](#typing) | [❌ 2/3](#tests-and-coverage) | [✅ 5/5](#linting) | [✅ 4/4](#releases) | [3](PROJECTS.md#scrapyw3lib) | [`ade4b62`](https://github.com/scrapy/w3lib/commit/ade4b62e55da45a8e5ead6ed21dcdedd018b9672) |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | [❌ 2/4](#python-versions) | [❌ 4/5](#packaging) | [❌ 0/2](#dependencies) | [❌ 2/3](#typing) | [❌ 0/3](#tests-and-coverage) | [✅ 3/3](#linting) | [❌ 3/4](#releases) | [10](PROJECTS.md#scrapysphinx-scrapy) | [`52f1427`](https://github.com/scrapy/sphinx-scrapy/commit/52f14275a06d15b7de3b6ecadacbd7ff46ac4764) |
| **scrapy-poet and its deps** | | | | | | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | [❌ 3/4](#python-versions) | [❌ 4/5](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/4](#typing) | [❌ 2/3](#tests-and-coverage) | [❌ 4/5](#linting) | [❌ 3/4](#releases) | [7](PROJECTS.md#scrapinghubscrapy-poet) | [`261e297`](https://github.com/scrapinghub/scrapy-poet/commit/261e297ce06c5b1687c6560c84b4e934d6cdcb74) |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | [❌ 3/4](#python-versions) | [✅ 5/5](#packaging) | [➖](#dependencies) | [❌ 3/4](#typing) | [✅ 3/3](#tests-and-coverage) | [✅ 3/3](#linting) | [✅ 4/4](#releases) | [2](PROJECTS.md#scrapinghubandi) | [`7a07b33`](https://github.com/scrapinghub/andi/commit/7a07b339ca1cc5e3c6495635b02eb01b5c483ebd) |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | [❌ 2/4](#python-versions) | [❌ 4/5](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/4](#typing) | [❌ 1/3](#tests-and-coverage) | [❌ 4/5](#linting) | [❌ 3/4](#releases) | [9](PROJECTS.md#scrapinghubweb-poet) | [`b3cc347`](https://github.com/scrapinghub/web-poet/commit/b3cc347952b9bc6cf534e44543b789d2f5f2fafb) |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | [❌ 2/4](#python-versions) | [✅ 5/5](#packaging) | [✅ 2/2](#dependencies) | [❌ 3/4](#typing) | [✅ 3/3](#tests-and-coverage) | [✅ 5/5](#linting) | [✅ 4/4](#releases) | [3](PROJECTS.md#zytedataurl-matcher) | [`b55ff5c`](https://github.com/zytedata/url-matcher/commit/b55ff5cc14b3346be16edf9e6faa603ebdfbf216) |
| **Zyte API** | | | | | | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | [✅ 4/4](#python-versions) | [✅ 5/5](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/4](#typing) | [❌ 2/3](#tests-and-coverage) | [✅ 5/5](#linting) | [❌ 3/4](#releases) | [4](PROJECTS.md#scrapy-pluginsscrapy-zyte-api) | [`2b15197`](https://github.com/scrapy-plugins/scrapy-zyte-api/commit/2b151972c7fa6412cf552d5c46a59e601d036e59) |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | [✅ 4/4](#python-versions) | [❌ 4/5](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/4](#typing) | [❌ 2/3](#tests-and-coverage) | [❌ 3/5](#linting) | [❌ 3/4](#releases) | [7](PROJECTS.md#zytedatapython-zyte-api) | [`efc4fdc`](https://github.com/zytedata/python-zyte-api/commit/efc4fdc6cebf36de26a946d0e665d539cafbecf9) |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | [❌ 0/4](#python-versions) | [❌ 1/3](#packaging) | [✅ 1/1](#dependencies) | [❌ 1/3](#typing) | [❌ 1/3](#tests-and-coverage) | [❌ 0/5](#linting) | [❌ 3/4](#releases) | [16](PROJECTS.md#scrapy-pluginsscrapy-zyte-smartproxy) | [`debd444`](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy/commit/debd4445343d0c3a1eba9fa0ce269613bb3b9d5c) |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | [❌ 3/4](#python-versions) | [❌ 3/5](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/4](#typing) | [❌ 1/3](#tests-and-coverage) | [❌ 4/5](#linting) | [❌ 2/4](#releases) | [10](PROJECTS.md#zytedatazyte-common-items) | [`1309123`](https://github.com/zytedata/zyte-common-items/commit/13091232ca4eb0b260a45c68f90a0e42d521d811) |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | [❌ 2/4](#python-versions) | [✅ 5/5](#packaging) | [❌ 0/2](#dependencies) | [❌ 3/4](#typing) | [✅ 3/3](#tests-and-coverage) | [✅ 5/5](#linting) | [✅ 4/4](#releases) | [5](PROJECTS.md#zytedatazyte-parsers) | [`4f5d08d`](https://github.com/zytedata/zyte-parsers/commit/4f5d08d1be951fa438f0aedd598d61a61c360ea0) |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | [❌ 2/4](#python-versions) | [✅ 5/5](#packaging) | [✅ 2/2](#dependencies) | [❌ 3/4](#typing) | [✅ 3/3](#tests-and-coverage) | [✅ 3/3](#linting) | [✅ 4/4](#releases) | [3](PROJECTS.md#zytedataclear-html) | [`6b820b1`](https://github.com/zytedata/clear-html/commit/6b820b13221145ceb0814e47e9583e5574d28865) |
| [zytedata/html-text](https://github.com/zytedata/html-text) | [❌ 2/4](#python-versions) | [✅ 5/5](#packaging) | [❌ 0/2](#dependencies) | [❌ 3/4](#typing) | [❌ 2/3](#tests-and-coverage) | [❌ 1/3](#linting) | [❌ 2/4](#releases) | [10](PROJECTS.md#zytedatahtml-text) | [`2dc4e94`](https://github.com/zytedata/html-text/commit/2dc4e94dd92a8b15476a237f0a1693b051f53d6f) |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | [❌ 2/4](#python-versions) | [❌ 4/5](#packaging) | [❌ 1/2](#dependencies) | [❌ 3/4](#typing) | [❌ 2/3](#tests-and-coverage) | [❌ 2/3](#linting) | [❌ 2/4](#releases) | [9](PROJECTS.md#scrapinghubprice-parser) | [`6718bfe`](https://github.com/scrapinghub/price-parser/commit/6718bfe8447f2de17ecc152d3ad2a4c51520c755) |
| **Scrapy Cloud** | | | | | | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | [❌ 1/6](#python-versions) | [❌ 0/3](#packaging) | [❌ 0/1](#dependencies) | [❌ 0/2](#typing) | [❌ 1/3](#tests-and-coverage) | [❌ 0/5](#linting) | [✅ 4/4](#releases) | [18](PROJECTS.md#scrapinghubpython-scrapinghub) | [`d0d7b29`](https://github.com/scrapinghub/python-scrapinghub/commit/d0d7b29153e40bbb0f9c56ab23caab86393f853e) |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | [❌ 2/4](#python-versions) | [❌ 3/5](#packaging) | [❌ 1/2](#dependencies) | [❌ 0/2](#typing) | [❌ 1/3](#tests-and-coverage) | [❌ 0/5](#linting) | [❌ 2/4](#releases) | [16](PROJECTS.md#scrapinghubshub) | [`80a4cad`](https://github.com/scrapinghub/shub/commit/80a4cad661f2a669739c8c3805fd33c67e62674e) |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [❌ 0/4](#python-versions) | [❌ 0/3](#packaging) | [❌ 0/1](#dependencies) | [❌ 0/2](#typing) | [❌ 1/3](#tests-and-coverage) | [❌ 0/3](#linting) | [❌ 2/4](#releases) | [17](PROJECTS.md#scrapinghubscrapinghub-entrypoint-scrapy) | [`6f44137`](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy/commit/6f4413767e33b492eb0e50a0b30e3ae7b5ba7829) |
| **Others** | | | | | | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | [❌ 2/4](#python-versions) | [❌ 4/5](#packaging) | [✅ 2/2](#dependencies) | [❌ 3/4](#typing) | [✅ 3/3](#tests-and-coverage) | [✅ 5/5](#linting) | [✅ 4/4](#releases) | [4](PROJECTS.md#scrapyform2request) | [`a251597`](https://github.com/scrapy/form2request/commit/a251597d9fa44cbd03736ec1da37f85593dfe820) |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | [❌ 2/4](#python-versions) | [✅ 5/5](#packaging) | [✅ 2/2](#dependencies) | [❌ 1/3](#typing) | [❌ 2/3](#tests-and-coverage) | [❌ 4/5](#linting) | [❌ 3/4](#releases) | [7](PROJECTS.md#scrapyscrapy-lint) | [`30a3872`](https://github.com/scrapy/scrapy-lint/commit/30a387279f0be38a48237d31725b1d52a2bcf297) |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | [❌ 3/4](#python-versions) | [✅ 5/5](#packaging) | [✅ 2/2](#dependencies) | [❌ 3/4](#typing) | [✅ 3/3](#tests-and-coverage) | [✅ 3/3](#linting) | [✅ 4/4](#releases) | [2](PROJECTS.md#scrapyscrapy-mcp-official) | [`5530c67`](https://github.com/scrapy/scrapy-mcp-official/commit/5530c671a7078f4f06479422c623d10b846d3db9) |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | [❌ 3/6](#python-versions) | [✅ 5/5](#packaging) | [➖](#dependencies) | [❌ 1/3](#typing) | [❌ 1/3](#tests-and-coverage) | [✅ 3/3](#linting) | [✅ 4/4](#releases) | [7](PROJECTS.md#scrapyxtractmime) | [`9d50fcb`](https://github.com/scrapy/xtractmime/commit/9d50fcb0d7abd7a96f7dee746d9285faba4af6db) |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | [✅ 4/4](#python-versions) | [✅ 5/5](#packaging) | [✅ 2/2](#dependencies) | [❌ 3/4](#typing) | [✅ 3/3](#tests-and-coverage) | [✅ 3/3](#linting) | [✅ 4/4](#releases) | [1](PROJECTS.md#scrapy-pluginsscrapy-download-handlers-incubator) | [`f585f8d`](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator/commit/f585f8da60d14ec804c4b3b7d105c4ce55d5238b) |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | [❌ 2/4](#python-versions) | [❌ 3/5](#packaging) | [✅ 2/2](#dependencies) | [❌ 1/3](#typing) | [❌ 1/3](#tests-and-coverage) | [❌ 0/3](#linting) | [❌ 1/4](#releases) | [14](PROJECTS.md#scrapy-pluginsscrapy-playwright) | [`d99f38d`](https://github.com/scrapy-plugins/scrapy-playwright/commit/d99f38d3483118881add4e2bcbc595d45091f196) |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | [❌ 1/6](#python-versions) | [❌ 3/5](#packaging) | [✅ 2/2](#dependencies) | [❌ 3/4](#typing) | [❌ 2/3](#tests-and-coverage) | [❌ 1/5](#linting) | [❌ 2/4](#releases) | [15](PROJECTS.md#scrapy-pluginsscrapy-spider-metadata) | [`63b3991`](https://github.com/scrapy-plugins/scrapy-spider-metadata/commit/63b3991dc8f181b2ef358e3b09aeda13261dd7c3) |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | [❌ 2/4](#python-versions) | [❌ 3/5](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/3](#typing) | [❌ 1/3](#tests-and-coverage) | [❌ 2/5](#linting) | [❌ 3/4](#releases) | [11](PROJECTS.md#scrapinghubdateparser) | [`fed9cf9`](https://github.com/scrapinghub/dateparser/commit/fed9cf94e9d8a1128b396f01ca66f4a303f03ee4) |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [❌ 0/4](#python-versions) | [❌ 1/3](#packaging) | [❌ 0/1](#dependencies) | [❌ 1/3](#typing) | [❌ 2/3](#tests-and-coverage) | [❌ 0/3](#linting) | [❌ 1/4](#releases) | [16](PROJECTS.md#scrapinghubextruct) | [`dc3bf7d`](https://github.com/scrapinghub/extruct/commit/dc3bf7d2209ecf421222afc90d3d2dd8c6fd23cf) |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | [❌ 0/4](#python-versions) | [✅ 5/5](#packaging) | [✅ 2/2](#dependencies) | [❌ 1/3](#typing) | [❌ 0/3](#tests-and-coverage) | [❌ 3/5](#linting) | [❌ 2/4](#releases) | [13](PROJECTS.md#scrapinghubscrapyrt) | [`6d00a0a`](https://github.com/scrapinghub/scrapyrt/commit/6d00a0ad55c310c268fb13a151a3f3c98f0cabb4) |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | [❌ 2/4](#python-versions) | [❌ 4/5](#packaging) | [✅ 2/2](#dependencies) | [❌ 1/3](#typing) | [❌ 2/3](#tests-and-coverage) | [❌ 4/5](#linting) | [❌ 3/4](#releases) | [8](PROJECTS.md#scrapinghubspidermon) | [`4b9a8ff`](https://github.com/scrapinghub/spidermon/commit/4b9a8ffe16c30a0f61461f1570055c1b8dfded72) |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | [❌ 0/4](#python-versions) | [❌ 3/5](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/4](#typing) | [❌ 2/3](#tests-and-coverage) | [❌ 0/3](#linting) | [❌ 1/4](#releases) | [15](PROJECTS.md#zytedataduplicate-url-discarder) | [`8db08b3`](https://github.com/zytedata/duplicate-url-discarder/commit/8db08b3edf638f34ee6ad7393612f579b5bfb90f) |

## Python versions

| Check | Statement | Results |
| --- | --- | --- |
| [`no-eol-python`](#no-eol-python) | Support for end-of-life Python versions is dropped. | 8/37 passing |
| [`latest-python`](#latest-python) | The latest stable Python version is declared as supported and tested in CI. | 30/37 passing |
| [`unreleased-python`](#unreleased-python) | The upcoming Python version is tested in CI, once it has a release candidate. | 11/37 passing |
| [`python-classifiers`](#python-classifiers) | Python version classifiers match requires-python: there is one for every supported Python version it allows, and none for versions it excludes. | 30/37 passing |
| [`supports-pypy`](#supports-pypy) | The project supports PyPy: it has the PyPy classifier or tests PyPy in CI. | 12/37 yes |
| [`latest-pypy`](#latest-pypy) | The latest PyPy version is declared as supported and tested in CI. | 0/12 passing |
| [`no-eol-pypy`](#no-eol-pypy) | End-of-life PyPy versions are not tested in CI. | 12/12 passing |

| Project | [no-eol-python](#no-eol-python) | [latest-python](#latest-python) | [unreleased-python](#unreleased-python) | [python-classifiers](#python-classifiers) | [supports-pypy](#supports-pypy) | [latest-pypy](#latest-pypy) | [no-eol-pypy](#no-eol-pypy) |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Scrapy and its deps** | | | | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | ✅ | ✅ | ✅ | ✅ | yes | [❌](#latest-pypy) | ✅ |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | [❌](#no-eol-python) | ✅ | [❌](#unreleased-python) | ✅ | yes | [❌](#latest-pypy) | ✅ |
| [scrapy/formerly](https://github.com/scrapy/formerly) | [❌](#no-eol-python) | ✅ | [❌](#unreleased-python) | ✅ | yes | [❌](#latest-pypy) | ✅ |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | ✅ | ✅ | ✅ | ✅ | yes | [❌](#latest-pypy) | ✅ |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | [❌](#no-eol-python) | ✅ | [❌](#unreleased-python) | ✅ | yes | [❌](#latest-pypy) | ✅ |
| [scrapy/parsel](https://github.com/scrapy/parsel) | [❌](#no-eol-python) | ✅ | ✅ | ✅ | yes | [❌](#latest-pypy) | ✅ |
| [scrapy/protego](https://github.com/scrapy/protego) | [❌](#no-eol-python) | ✅ | ✅ | ✅ | yes | [❌](#latest-pypy) | ✅ |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | [❌](#no-eol-python) | ✅ | ✅ | ✅ | yes | [❌](#latest-pypy) | ✅ |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | ✅ | ✅ | ✅ | ✅ | yes | [❌](#latest-pypy) | ✅ |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | [❌](#no-eol-python) | ✅ | [❌](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **scrapy-poet and its deps** | | | | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | ✅ | [❌](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | [❌](#no-eol-python) | ✅ | ✅ | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | [❌](#no-eol-python) | ✅ | [❌](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | [❌](#no-eol-python) | ✅ | [❌](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **Zyte API** | | | | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | ✅ | ✅ | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | ✅ | ✅ | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | [❌](#no-eol-python) | [❌](#latest-python) | [❌](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | ✅ | ✅ | [❌](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | [❌](#no-eol-python) | ✅ | [❌](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | [❌](#no-eol-python) | ✅ | [❌](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/html-text](https://github.com/zytedata/html-text) | [❌](#no-eol-python) | ✅ | [❌](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | [❌](#no-eol-python) | ✅ | [❌](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **Scrapy Cloud** | | | | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | [❌](#no-eol-python) | [❌](#latest-python) | [❌](#unreleased-python) | [❌](#python-classifiers) | yes | [❌](#latest-pypy) | ✅ |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | [❌](#no-eol-python) | ✅ | [❌](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [❌](#no-eol-python) | [❌](#latest-python) | [❌](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **Others** | | | | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | [❌](#no-eol-python) | ✅ | [❌](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | [❌](#no-eol-python) | ✅ | [❌](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | [❌](#no-eol-python) | ✅ | ✅ | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | [❌](#no-eol-python) | ✅ | [❌](#unreleased-python) | ✅ | yes | [❌](#latest-pypy) | ✅ |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | ✅ | ✅ | ✅ | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | [❌](#no-eol-python) | ✅ | [❌](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | [❌](#no-eol-python) | [❌](#latest-python) | [❌](#unreleased-python) | [❌](#python-classifiers) | yes | [❌](#latest-pypy) | ✅ |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | [❌](#no-eol-python) | ✅ | [❌](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [❌](#no-eol-python) | [❌](#latest-python) | [❌](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | [❌](#no-eol-python) | [❌](#latest-python) | [❌](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | [❌](#no-eol-python) | ✅ | [❌](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | [❌](#no-eol-python) | [❌](#latest-python) | [❌](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |

### no-eol-python

Support for end-of-life Python versions is dropped.

- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/formerly](https://github.com/scrapy/formerly): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/parsel](https://github.com/scrapy/parsel): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/protego](https://github.com/scrapy/protego): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/queuelib](https://github.com/scrapy/queuelib): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/andi](https://github.com/scrapinghub/andi): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [zytedata/url-matcher](https://github.com/zytedata/url-matcher): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [zytedata/clear-html](https://github.com/zytedata/clear-html): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): requires-python '>=3.8' allows 3.8 (EOL 2024-10-07), 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.8, 3.9, 3.10
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10

### latest-python

The latest stable Python version is declared as supported and tested in CI.

- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no 'Programming Language :: Python :: 3.14' classifier; 3.14 not found in CI workflows or tox config
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no 'Programming Language :: Python :: 3.14' classifier
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no 'Programming Language :: Python :: 3.14' classifier; 3.14 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): no 'Programming Language :: Python :: 3.14' classifier; 3.14 not found in CI workflows or tox config
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no 'Programming Language :: Python :: 3.14' classifier; 3.14 not found in CI workflows or tox config
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no 'Programming Language :: Python :: 3.14' classifier; 3.14 not found in CI workflows or tox config
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no 'Programming Language :: Python :: 3.14' classifier; 3.14 not found in CI workflows or tox config

### unreleased-python

The upcoming Python version is tested in CI, once it has a release candidate.

- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): 3.15 not found in CI workflows or tox config
- ❌ [scrapy/formerly](https://github.com/scrapy/formerly): 3.15 not found in CI workflows or tox config
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): 3.15 not found in CI workflows or tox config
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): 3.15 not found in CI workflows or tox config
- ❌ [zytedata/url-matcher](https://github.com/zytedata/url-matcher): 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): 3.15 not found in CI workflows or tox config
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): 3.15 not found in CI workflows or tox config
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): 3.15 not found in CI workflows or tox config
- ❌ [zytedata/clear-html](https://github.com/zytedata/clear-html): 3.15 not found in CI workflows or tox config
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): 3.15 not found in CI workflows or tox config
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): 3.15 not found in CI workflows or tox config
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): 3.15 not found in CI workflows or tox config
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): 3.15 not found in CI workflows or tox config
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): 3.15 not found in CI workflows or tox config

### python-classifiers

Python version classifiers match requires-python: there is one for every supported Python version it allows, and none for versions it excludes.

- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no classifiers for 3.14
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no classifiers for 3.14
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no classifiers for 3.14
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): no classifiers for 3.14
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no classifiers for 3.13, 3.14
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no classifiers for 3.14
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no classifiers for 3.14

### supports-pypy

The project supports PyPy: it has the PyPy classifier or tests PyPy in CI.

Nothing to report.

### latest-pypy

The latest PyPy version is declared as supported and tested in CI.

- ❌ [scrapy/scrapy](https://github.com/scrapy/scrapy): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy/formerly](https://github.com/scrapy/formerly): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy/parsel](https://github.com/scrapy/parsel): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy/protego](https://github.com/scrapy/protego): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy/queuelib](https://github.com/scrapy/queuelib): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy/w3lib](https://github.com/scrapy/w3lib): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): PyPy 3.12 not found in CI workflows or tox config
- ➖ Does not support PyPy. [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet), [zytedata/url-matcher](https://github.com/zytedata/url-matcher), [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api), [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items), [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapy/form2request](https://github.com/scrapy/form2request), [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt), [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder)

### no-eol-pypy

End-of-life PyPy versions are not tested in CI.

- ➖ Does not support PyPy. [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet), [zytedata/url-matcher](https://github.com/zytedata/url-matcher), [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api), [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items), [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapy/form2request](https://github.com/scrapy/form2request), [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt), [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder)

## Packaging

| Check | Statement | Results |
| --- | --- | --- |
| [`pyproject-metadata`](#pyproject-metadata) | Package metadata is in the [project] table of pyproject.toml, with no setup.py and no setuptools configuration in setup.cfg. | 32/37 passing |
| [`license`](#license) | The license: the license field of package metadata, or else the license classifiers. | BSD-3-Clause (21), BSD License (8), Apache-2.0 (6), MIT (2) |
| [`pep639-license`](#pep639-license) | The license is declared as an SPDX expression (PEP 639), without license classifiers. | 23/33 passing |
| [`hatchling`](#hatchling) | The build backend is hatchling. | 28/37 passing |
| [`project-urls`](#project-urls) | Project URLs are declared in [project.urls]. | 33/33 passing |
| [`twine-check`](#twine-check) | `twine check` validates the built distributions in tox. | 31/37 passing |

| Project | [pyproject-metadata](#pyproject-metadata) | [license](#license) | [pep639-license](#pep639-license) | [hatchling](#hatchling) | [project-urls](#project-urls) | [twine-check](#twine-check) |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Scrapy and its deps** | | | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| [scrapy/formerly](https://github.com/scrapy/formerly) | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| [scrapy/parsel](https://github.com/scrapy/parsel) | ✅ | BSD-3-Clause | [❌](#pep639-license) | ✅ | ✅ | ✅ |
| [scrapy/protego](https://github.com/scrapy/protego) | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | [❌](#twine-check) |
| **scrapy-poet and its deps** | | | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | BSD-3-Clause | [❌](#pep639-license) | ✅ | ✅ | ✅ |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | ✅ | Apache-2.0 | ✅ | ✅ | ✅ | ✅ |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | ✅ | BSD-3-Clause | [❌](#pep639-license) | ✅ | ✅ | ✅ |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | Apache-2.0 | ✅ | ✅ | ✅ | ✅ |
| **Zyte API** | | | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | BSD License | [❌](#pep639-license) | ✅ | ✅ | ✅ |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | [❌](#pyproject-metadata) | BSD License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#project-urls) | ✅ |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | ✅ | BSD License | [❌](#pep639-license) | [❌](#hatchling) | ✅ | ✅ |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | ✅ | Apache-2.0 | ✅ | ✅ | ✅ | ✅ |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | ✅ | Apache-2.0 | ✅ | ✅ | ✅ | ✅ |
| [zytedata/html-text](https://github.com/zytedata/html-text) | ✅ | MIT | ✅ | ✅ | ✅ | ✅ |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | [❌](#twine-check) |
| **Scrapy Cloud** | | | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | [❌](#pyproject-metadata) | BSD License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#project-urls) | [❌](#twine-check) |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | ✅ | BSD-3-Clause | [❌](#pep639-license) | ✅ | ✅ | [❌](#twine-check) |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [❌](#pyproject-metadata) | BSD License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#project-urls) | [❌](#twine-check) |
| **Others** | | | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | ✅ | Apache-2.0 | [❌](#pep639-license) | ✅ | ✅ | ✅ |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | ✅ | MIT | ✅ | ✅ | ✅ | ✅ |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | ✅ | Apache-2.0 | ✅ | ✅ | ✅ | ✅ |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | ✅ | BSD-3-Clause | ✅ | [❌](#hatchling) | ✅ | [❌](#twine-check) |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | ✅ | BSD License | [❌](#pep639-license) | [❌](#hatchling) | ✅ | ✅ |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | [❌](#pyproject-metadata) | BSD-3-Clause | ✅ | [❌](#hatchling) | ✅ | ✅ |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [❌](#pyproject-metadata) | BSD License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#project-urls) | ✅ |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | ✅ | BSD-3-Clause | [❌](#pep639-license) | ✅ | ✅ | ✅ |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | ✅ | BSD License | [❌](#pep639-license) | [❌](#hatchling) | ✅ | ✅ |

### pyproject-metadata

Package metadata is in the [project] table of pyproject.toml, with no setup.py and no setuptools configuration in setup.cfg.

- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no [project] table in pyproject.toml; setup.py exists
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [metadata], [bdist_wheel]
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [bdist_wheel], [sdist_dsc]
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): setup.py exists
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [wheel]

### license

The license: the license field of package metadata, or else the license classifiers.

Nothing to report.

### pep639-license

The license is declared as an SPDX expression (PEP 639), without license classifiers.

- ❌ [scrapy/parsel](https://github.com/scrapy/parsel): has license classifiers: License :: OSI Approved :: BSD License
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): has license classifiers: License :: OSI Approved :: BSD License
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): has license classifiers: License :: OSI Approved :: BSD License
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): no license field; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): has license classifiers: License :: OSI Approved :: BSD License
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): has license classifiers: License :: OSI Approved :: Apache Software License
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): has license classifiers: License :: OSI Approved :: BSD License
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ➖ No [project] table in pyproject.toml. [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/extruct](https://github.com/scrapinghub/extruct)

### hatchling

The build backend is hatchling.

- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no build-backend in pyproject.toml
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): build backend is setuptools.build_meta
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no build-backend in pyproject.toml
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no build-backend in pyproject.toml
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): build backend is setuptools.build_meta
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): build backend is setuptools.build_meta
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): build backend is setuptools.build_meta
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no build-backend in pyproject.toml
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): build backend is setuptools.build_meta

### project-urls

Project URLs are declared in [project.urls].

- ➖ No [project] table in pyproject.toml. [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/extruct](https://github.com/scrapinghub/extruct)

### twine-check

`twine check` validates the built distributions in tox.

- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no twine check in tox config
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no twine check in tox config
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): twine check runs in a workflow, not in tox
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no twine check in tox config
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no twine check in tox config
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no twine check in tox config

## Dependencies

| Check | Statement | Results |
| --- | --- | --- |
| [`dependency-lower-bounds`](#dependency-lower-bounds) | Every runtime dependency has a lower bound. | 20/25 passing |
| [`min-deps-env`](#min-deps-env) | A tox environment tests the minimum versions of dependencies (its name has min, minimum, lowest or pinned in it). | 23/30 passing |

| Project | [dependency-lower-bounds](#dependency-lower-bounds) | [min-deps-env](#min-deps-env) |
| --- | :---: | :---: |
| **Scrapy and its deps** | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | [❌](#dependency-lower-bounds) | ✅ |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |
| [scrapy/formerly](https://github.com/scrapy/formerly) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | [➖](#dependency-lower-bounds) | ✅ |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | ✅ | ✅ |
| [scrapy/parsel](https://github.com/scrapy/parsel) | ✅ | ✅ |
| [scrapy/protego](https://github.com/scrapy/protego) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | [❌](#dependency-lower-bounds) | [❌](#min-deps-env) |
| **scrapy-poet and its deps** | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | ✅ |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | ✅ | ✅ |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | ✅ |
| **Zyte API** | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | ✅ |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | ✅ |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | [➖](#dependency-lower-bounds) | ✅ |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | ✅ | ✅ |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | [❌](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | ✅ | ✅ |
| [zytedata/html-text](https://github.com/zytedata/html-text) | [❌](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | ✅ | [❌](#min-deps-env) |
| **Scrapy Cloud** | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | [❌](#dependency-lower-bounds) | ✅ |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| **Others** | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | ✅ | ✅ |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | ✅ | ✅ |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | ✅ | ✅ |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | ✅ | ✅ |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | ✅ | ✅ |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | ✅ | ✅ |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | ✅ | ✅ |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | ✅ | ✅ |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | ✅ | ✅ |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | ✅ | ✅ |

### dependency-lower-bounds

Every runtime dependency has a lower bound.

- ❌ [scrapy/scrapy](https://github.com/scrapy/scrapy): no lower bound: packaging, tldextract
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no lower bound: docutils, packaging, sphinx-copybutton, sphinx-design, sphinx-sitemap, sphinxcontrib-youtube, tomli
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): no lower bound: html-text, lxml, parsel, six, w3lib
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): no lower bound: lxml, lxml-html-clean
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no lower bound: click, docker, importlib-metadata, packaging, pip, PyYAML, requests, retrying, setuptools, toml
- ➖ No runtime dependencies. [scrapy/cssselect](https://github.com/scrapy/cssselect), [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/w3lib](https://github.com/scrapy/w3lib), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapy/xtractmime](https://github.com/scrapy/xtractmime)
- ➖ No [project] table in pyproject.toml. [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/extruct](https://github.com/scrapinghub/extruct)

### min-deps-env

A tox environment tests the minimum versions of dependencies (its name has min, minimum, lowest or pinned in it).

- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no tox environment for minimum dependency versions
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): no tox environment for minimum dependency versions
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): no tox environment for minimum dependency versions
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no tox environment for minimum dependency versions
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no tox environment for minimum dependency versions
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no tox environment for minimum dependency versions
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no tox environment for minimum dependency versions
- ➖ No dependencies. [scrapy/cssselect](https://github.com/scrapy/cssselect), [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/w3lib](https://github.com/scrapy/w3lib), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapy/xtractmime](https://github.com/scrapy/xtractmime)

## Typing

| Check | Statement | Results |
| --- | --- | --- |
| [`py-typed`](#py-typed) | The package ships type hints (a py.typed marker). | 25/37 passing |
| [`typed-classifier`](#typed-classifier) | A package with a py.typed marker has the 'Typing :: Typed' classifier. | 0/25 passing |
| [`mypy`](#mypy) | mypy runs in tox, CI workflows or pre-commit. | 34/37 passing |
| [`mypy-strict`](#mypy-strict) | mypy runs in strict mode: strict = true in its config, or --strict. | 20/34 passing |

| Project | [py-typed](#py-typed) | [typed-classifier](#typed-classifier) | [mypy](#mypy) | [mypy-strict](#mypy-strict) |
| --- | :---: | :---: | :---: | :---: |
| **Scrapy and its deps** | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapy/formerly](https://github.com/scrapy/formerly) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | ✅ | [❌](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapy/parsel](https://github.com/scrapy/parsel) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapy/protego](https://github.com/scrapy/protego) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | ✅ |
| **scrapy-poet and its deps** | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | [❌](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | ✅ | [❌](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| **Zyte API** | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | [❌](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | [❌](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | ✅ | [❌](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [zytedata/html-text](https://github.com/zytedata/html-text) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| **Scrapy Cloud** | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| **Others** | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | ✅ |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | ✅ | [❌](#typed-classifier) | ✅ | [❌](#mypy-strict) |

### py-typed

The package ships type hints (a py.typed marker).

- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no py.typed file
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no py.typed file
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no py.typed file
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no py.typed file
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no py.typed file
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): no py.typed file
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no py.typed file
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no py.typed file
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): no py.typed file
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no py.typed file
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no py.typed file
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): no py.typed file

### typed-classifier

A package with a py.typed marker has the 'Typing :: Typed' classifier.

- ❌ [scrapy/scrapy](https://github.com/scrapy/scrapy): no 'Typing :: Typed' classifier
- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): no 'Typing :: Typed' classifier
- ❌ [scrapy/formerly](https://github.com/scrapy/formerly): no 'Typing :: Typed' classifier
- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): no 'Typing :: Typed' classifier
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): no 'Typing :: Typed' classifier
- ❌ [scrapy/parsel](https://github.com/scrapy/parsel): no 'Typing :: Typed' classifier
- ❌ [scrapy/protego](https://github.com/scrapy/protego): no 'Typing :: Typed' classifier
- ❌ [scrapy/queuelib](https://github.com/scrapy/queuelib): no 'Typing :: Typed' classifier
- ❌ [scrapy/w3lib](https://github.com/scrapy/w3lib): no 'Typing :: Typed' classifier
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): no 'Typing :: Typed' classifier
- ❌ [scrapinghub/andi](https://github.com/scrapinghub/andi): no 'Typing :: Typed' classifier
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): no 'Typing :: Typed' classifier
- ❌ [zytedata/url-matcher](https://github.com/zytedata/url-matcher): no 'Typing :: Typed' classifier
- ❌ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): no 'Typing :: Typed' classifier
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): no 'Typing :: Typed' classifier
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): no 'Typing :: Typed' classifier
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): no 'Typing :: Typed' classifier
- ❌ [zytedata/clear-html](https://github.com/zytedata/clear-html): no 'Typing :: Typed' classifier
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): no 'Typing :: Typed' classifier
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no 'Typing :: Typed' classifier
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): no 'Typing :: Typed' classifier
- ❌ [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official): no 'Typing :: Typed' classifier
- ❌ [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator): no 'Typing :: Typed' classifier
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): no 'Typing :: Typed' classifier
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no 'Typing :: Typed' classifier
- ➖ No py.typed file. [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt), [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon)

### mypy

mypy runs in tox, CI workflows or pre-commit.

- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): mypy not found
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): mypy not found
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): mypy not found

### mypy-strict

mypy runs in strict mode: strict = true in its config, or --strict.

- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): no strict = true in mypy config, and no --strict
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): no strict = true in mypy config, and no --strict
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): no strict = true in mypy config, and no --strict
- ❌ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): no strict = true in mypy config, and no --strict
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): no strict = true in mypy config, and no --strict
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no strict = true in mypy config, and no --strict
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): no strict = true in mypy config, and no --strict
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): no strict = true in mypy config, and no --strict
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no strict = true in mypy config, and no --strict
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no strict = true in mypy config, and no --strict
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no strict = true in mypy config, and no --strict
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no strict = true in mypy config, and no --strict
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): no strict = true in mypy config, and no --strict
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no strict = true in mypy config, and no --strict
- ➖ Does not run mypy. [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy)

## Tests and coverage

| Check | Statement | Results |
| --- | --- | --- |
| [`codecov`](#codecov) | Test coverage is uploaded to Codecov in CI workflows. | 35/37 passing |
| [`codecov-test-results`](#codecov-test-results) | Test results are uploaded to Codecov in CI workflows (codecov/codecov-action with report_type: test_results). | 13/37 passing |
| [`branch-coverage`](#branch-coverage) | Branch coverage is enabled. | 25/37 passing |

| Project | [codecov](#codecov) | [codecov-test-results](#codecov-test-results) | [branch-coverage](#branch-coverage) |
| --- | :---: | :---: | :---: |
| **Scrapy and its deps** | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | ✅ | ✅ | ✅ |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | ✅ | [❌](#codecov-test-results) | ✅ |
| [scrapy/formerly](https://github.com/scrapy/formerly) | ✅ | ✅ | ✅ |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | ✅ | [❌](#codecov-test-results) | ✅ |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | ✅ | [❌](#codecov-test-results) | ✅ |
| [scrapy/parsel](https://github.com/scrapy/parsel) | ✅ | ✅ | ✅ |
| [scrapy/protego](https://github.com/scrapy/protego) | ✅ | ✅ | ✅ |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | ✅ | ✅ | ✅ |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | ✅ | [❌](#codecov-test-results) | ✅ |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | [❌](#codecov) | [❌](#codecov-test-results) | [❌](#branch-coverage) |
| **scrapy-poet and its deps** | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | [❌](#codecov-test-results) | ✅ |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | ✅ | ✅ | ✅ |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | ✅ | [❌](#codecov-test-results) | [❌](#branch-coverage) |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | ✅ | ✅ |
| **Zyte API** | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | [❌](#codecov-test-results) | ✅ |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | [❌](#codecov-test-results) | ✅ |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | ✅ | [❌](#codecov-test-results) | [❌](#branch-coverage) |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | ✅ | [❌](#codecov-test-results) | [❌](#branch-coverage) |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | ✅ | ✅ | ✅ |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | ✅ | ✅ | ✅ |
| [zytedata/html-text](https://github.com/zytedata/html-text) | ✅ | [❌](#codecov-test-results) | ✅ |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | ✅ | [❌](#codecov-test-results) | ✅ |
| **Scrapy Cloud** | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | ✅ | [❌](#codecov-test-results) | [❌](#branch-coverage) |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | ✅ | [❌](#codecov-test-results) | [❌](#branch-coverage) |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | ✅ | [❌](#codecov-test-results) | [❌](#branch-coverage) |
| **Others** | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | ✅ | ✅ | ✅ |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | ✅ | ✅ | [❌](#branch-coverage) |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | ✅ | ✅ | ✅ |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | ✅ | [❌](#codecov-test-results) | [❌](#branch-coverage) |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | ✅ | ✅ | ✅ |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | ✅ | [❌](#codecov-test-results) | [❌](#branch-coverage) |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | ✅ | [❌](#codecov-test-results) | ✅ |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | ✅ | [❌](#codecov-test-results) | [❌](#branch-coverage) |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | ✅ | [❌](#codecov-test-results) | ✅ |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | [❌](#codecov) | [❌](#codecov-test-results) | [❌](#branch-coverage) |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | ✅ | [❌](#codecov-test-results) | ✅ |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | ✅ | [❌](#codecov-test-results) | ✅ |

### codecov

Test coverage is uploaded to Codecov in CI workflows.

- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no codecov/codecov-action step for coverage
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no codecov/codecov-action step for coverage

### codecov-test-results

Test results are uploaded to Codecov in CI workflows (codecov/codecov-action with report_type: test_results).

- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy/w3lib](https://github.com/scrapy/w3lib): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): no codecov/codecov-action step with report_type: test_results
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no codecov/codecov-action step with report_type: test_results
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): no codecov/codecov-action step with report_type: test_results
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): no codecov/codecov-action step with report_type: test_results
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no codecov/codecov-action step with report_type: test_results

### branch-coverage

Branch coverage is enabled.

- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no branch = true in coverage config, and no --cov-branch
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no branch = true in coverage config, and no --cov-branch

## Linting

| Check | Statement | Results |
| --- | --- | --- |
| [`ruff`](#ruff) | ruff-check and ruff-format are used, instead of tools that ruff replaces. | 30/37 passing |
| [`pylint`](#pylint) | A tox environment runs pylint. | 10/37 yes |
| [`actionlint`](#actionlint) | GitHub Actions workflows are linted with actionlint. | 20/37 passing |
| [`zizmor`](#zizmor) | GitHub Actions workflows are audited with zizmor. | 23/37 passing |
| [`has-sphinx-docs`](#has-sphinx-docs) | The project has Sphinx docs (docs/conf.py). | 21/37 yes |
| [`blacken-docs`](#blacken-docs) | Code examples in the docs are formatted with blacken-docs. | 16/21 passing |
| [`sphinx-lint`](#sphinx-lint) | The docs are linted with sphinx-lint. | 16/21 passing |

| Project | [ruff](#ruff) | [pylint](#pylint) | [actionlint](#actionlint) | [zizmor](#zizmor) | [has-sphinx-docs](#has-sphinx-docs) | [blacken-docs](#blacken-docs) | [sphinx-lint](#sphinx-lint) |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Scrapy and its deps** | | | | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | ✅ | yes | [❌](#actionlint) | ✅ | yes | ✅ | ✅ |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | ✅ | yes | ✅ | ✅ | yes | ✅ | ✅ |
| [scrapy/formerly](https://github.com/scrapy/formerly) | ✅ | no | [❌](#actionlint) | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | ✅ | yes | ✅ | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | ✅ | yes | ✅ | ✅ | yes | ✅ | ✅ |
| [scrapy/parsel](https://github.com/scrapy/parsel) | ✅ | yes | ✅ | ✅ | yes | ✅ | ✅ |
| [scrapy/protego](https://github.com/scrapy/protego) | ✅ | no | ✅ | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | ✅ | yes | ✅ | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | ✅ | yes | ✅ | ✅ | yes | ✅ | ✅ |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | ✅ | no | ✅ | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| **scrapy-poet and its deps** | | | | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | no | ✅ | [❌](#zizmor) | yes | ✅ | ✅ |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | ✅ | no | ✅ | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | ✅ | no | [❌](#actionlint) | ✅ | yes | ✅ | ✅ |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | no | ✅ | ✅ | yes | ✅ | ✅ |
| **Zyte API** | | | | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | no | ✅ | ✅ | yes | ✅ | ✅ |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | no | [❌](#actionlint) | [❌](#zizmor) | yes | ✅ | ✅ |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | [❌](#ruff) | no | [❌](#actionlint) | [❌](#zizmor) | yes | [❌](#blacken-docs) | [❌](#sphinx-lint) |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | ✅ | no | ✅ | [❌](#zizmor) | yes | ✅ | ✅ |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | ✅ | no | ✅ | ✅ | yes | ✅ | ✅ |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | ✅ | no | ✅ | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [zytedata/html-text](https://github.com/zytedata/html-text) | ✅ | no | [❌](#actionlint) | [❌](#zizmor) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | ✅ | no | [❌](#actionlint) | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| **Scrapy Cloud** | | | | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | [❌](#ruff) | no | [❌](#actionlint) | [❌](#zizmor) | yes | [❌](#blacken-docs) | [❌](#sphinx-lint) |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | [❌](#ruff) | no | [❌](#actionlint) | [❌](#zizmor) | yes | [❌](#blacken-docs) | [❌](#sphinx-lint) |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [❌](#ruff) | no | [❌](#actionlint) | [❌](#zizmor) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| **Others** | | | | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | ✅ | no | ✅ | ✅ | yes | ✅ | ✅ |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | ✅ | yes | [❌](#actionlint) | ✅ | yes | ✅ | ✅ |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | ✅ | no | ✅ | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | ✅ | no | ✅ | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | ✅ | no | ✅ | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | [❌](#ruff) | yes | [❌](#actionlint) | [❌](#zizmor) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | ✅ | no | [❌](#actionlint) | [❌](#zizmor) | yes | [❌](#blacken-docs) | [❌](#sphinx-lint) |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | ✅ | no | [❌](#actionlint) | ✅ | yes | [❌](#blacken-docs) | [❌](#sphinx-lint) |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [❌](#ruff) | no | [❌](#actionlint) | [❌](#zizmor) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | ✅ | yes | [❌](#actionlint) | [❌](#zizmor) | yes | ✅ | ✅ |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | ✅ | no | ✅ | [❌](#zizmor) | yes | ✅ | ✅ |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | [❌](#ruff) | no | [❌](#actionlint) | [❌](#zizmor) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |

### ruff

ruff-check and ruff-format are used, instead of tools that ruff replaces.

- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): missing pre-commit hooks: ruff-check, ruff-format
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): missing pre-commit hooks: ruff-check, ruff-format
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no .pre-commit-config.yaml
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no .pre-commit-config.yaml
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, isort, pyupgrade
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort

### pylint

A tox environment runs pylint.

Nothing to report.

### actionlint

GitHub Actions workflows are linted with actionlint.

- ❌ [scrapy/scrapy](https://github.com/scrapy/scrapy): missing pre-commit hooks: actionlint
- ❌ [scrapy/formerly](https://github.com/scrapy/formerly): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): missing pre-commit hooks: actionlint
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): missing pre-commit hooks: actionlint
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): missing pre-commit hooks: actionlint
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no .pre-commit-config.yaml
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): missing pre-commit hooks: actionlint
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no .pre-commit-config.yaml
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): missing pre-commit hooks: actionlint
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): missing pre-commit hooks: actionlint

### zizmor

GitHub Actions workflows are audited with zizmor.

- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): missing pre-commit hooks: zizmor
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): missing pre-commit hooks: zizmor
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): missing pre-commit hooks: zizmor
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): missing pre-commit hooks: zizmor
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no .pre-commit-config.yaml
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no .pre-commit-config.yaml
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): missing pre-commit hooks: zizmor
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): missing pre-commit hooks: zizmor

### has-sphinx-docs

The project has Sphinx docs (docs/conf.py).

Nothing to report.

### blacken-docs

Code examples in the docs are formatted with blacken-docs.

- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): missing pre-commit hooks: blacken-docs
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): missing pre-commit hooks: blacken-docs
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): missing pre-commit hooks: blacken-docs
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): missing pre-commit hooks: blacken-docs
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): missing pre-commit hooks: blacken-docs
- ➖ No Sphinx docs. [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapinghub/andi](https://github.com/scrapinghub/andi), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder)

### sphinx-lint

The docs are linted with sphinx-lint.

- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): missing pre-commit hooks: sphinx-lint
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): missing pre-commit hooks: sphinx-lint
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): missing pre-commit hooks: sphinx-lint
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): missing pre-commit hooks: sphinx-lint
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): missing pre-commit hooks: sphinx-lint
- ➖ No Sphinx docs. [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapinghub/andi](https://github.com/scrapinghub/andi), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder)

## Releases

| Check | Statement | Results |
| --- | --- | --- |
| [`trusted-publishing`](#trusted-publishing) | Releases are published to PyPI from GitHub Actions through trusted publishing. | 27/37 passing |
| [`publish-on-tag`](#publish-on-tag) | Publishing is triggered by pushing a tag, not by creating a GitHub release. | 34/37 passing |
| [`separate-build-job`](#separate-build-job) | The publish workflow builds distributions in a separate job from the one that publishes them. | 17/37 passing |
| [`bump-my-version`](#bump-my-version) | bump-my-version is configured, in pyproject.toml or .bumpversion.toml. | 35/37 passing |

| Project | [trusted-publishing](#trusted-publishing) | [publish-on-tag](#publish-on-tag) | [separate-build-job](#separate-build-job) | [bump-my-version](#bump-my-version) |
| --- | :---: | :---: | :---: | :---: |
| **Scrapy and its deps** | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | ✅ | ✅ | ✅ | ✅ |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | ✅ | ✅ | ✅ | ✅ |
| [scrapy/formerly](https://github.com/scrapy/formerly) | ✅ | ✅ | ✅ | ✅ |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | ✅ | [❌](#publish-on-tag) | [❌](#separate-build-job) | ✅ |
| [scrapy/parsel](https://github.com/scrapy/parsel) | ✅ | ✅ | ✅ | ✅ |
| [scrapy/protego](https://github.com/scrapy/protego) | ✅ | ✅ | ✅ | ✅ |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | ✅ | ✅ | ✅ | ✅ |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | ✅ | ✅ | ✅ | ✅ |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| **scrapy-poet and its deps** | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | ✅ | ✅ | ✅ | ✅ |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | ✅ | ✅ | ✅ |
| **Zyte API** | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | ✅ | ✅ | ✅ | ✅ |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | ✅ | ✅ | ✅ | ✅ |
| [zytedata/html-text](https://github.com/zytedata/html-text) | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| **Scrapy Cloud** | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | ✅ | ✅ | ✅ | ✅ |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| **Others** | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | ✅ | ✅ | ✅ | ✅ |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | ✅ | ✅ | ✅ | ✅ |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | ✅ | ✅ | ✅ | ✅ |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | ✅ | ✅ | ✅ | ✅ |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | [❌](#trusted-publishing) | [❌](#publish-on-tag) | [❌](#separate-build-job) | ✅ |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | ✅ | [❌](#publish-on-tag) | ✅ | ✅ |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | [❌](#bump-my-version) |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | [❌](#bump-my-version) |

### trusted-publishing

Releases are published to PyPI from GitHub Actions through trusted publishing.

- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): .github/workflows/publish.yml uses an API token
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): .github/workflows/publish.yml publishes with twine upload
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): .github/workflows/publish.yml publishes with twine upload
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): .github/workflows/publish.yml publishes with twine upload
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): .github/workflows/python-publish.yml publishes with twine upload
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): .github/workflows/publish.yml uses an API token
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission

### publish-on-tag

Publishing is triggered by pushing a tag, not by creating a GitHub release.

- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): .github/workflows/publish.yml is triggered by GitHub releases
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): .github/workflows/publish.yml is triggered by GitHub releases
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): .github/workflows/publish.yml is triggered by GitHub releases

### separate-build-job

The publish workflow builds distributions in a separate job from the one that publishes them.

- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): .github/workflows/python-publish.yml: job 'deploy' builds and publishes
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): .github/workflows/publish.yml: job 'deploy' builds and publishes

### bump-my-version

bump-my-version is configured, in pyproject.toml or .bumpversion.toml.

- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): only legacy (bump2version) configuration, in setup.cfg
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): only legacy (bump2version) configuration, in .bumpversion.cfg
