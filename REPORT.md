# Maintenance report

Generated on 2026-11-02 with `oss-maint report`. Do not edit by hand. See [PROJECTS.md](PROJECTS.md) for what fails in each project.

✅ passes · ❌ fails · ➖ not applicable · ⚠️ check error · yes/no or a value: result of an informational check. Click a symbol for details.

## Reference data

Values that checks compare projects against.

- Latest Python: 3.15
- Upcoming Python, with a release candidate: none
- Supported Python versions, with EOL dates: 3.11 (2027-10-31), 3.12 (2028-10-31), 3.13 (2029-10-31), 3.14 (2030-10-31), 3.15 (2031-10-31)
- Python versions of the latest PyPy release: 3.11, 3.12
- End-of-life PyPy Python versions: 3.6, 3.7, 3.8, 3.9, 3.10
- Minimum pre-commit hook versions, the newest releases at least 180 days old: ruff 0.15.12, zizmor 1.24.1
- Latest sphinx-scrapy: 0.15.0

## Summary

Checks passing per group.

| Project | [Python versions](#python-versions) | [Packaging](#packaging) | [Dependencies](#dependencies) | [Typing](#typing) | [Tests and coverage](#tests-and-coverage) | [Linting](#linting) | [Documentation](#documentation) | [Releases](#releases) | Failing | Commit |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | --- |
| **Scrapy and its deps** | | | | | | | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | [✅ 3/3](#python-versions) | [✅ 7/7](#packaging) | [❌ 1/2](#dependencies) | [❌ 3/4](#typing) | [✅ 6/6](#tests-and-coverage) | [❌ 11/13](#linting) | [❌ 7/10](#documentation) | [✅ 4/4](#releases) | [7](PROJECTS.md#scrapyscrapy) | [`943e31d`](https://github.com/scrapy/scrapy/commit/943e31d5d69f2c9802e6673b3478975795670c57) |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | [❌ 4/5](#python-versions) | [❌ 6/7](#packaging) | [➖](#dependencies) | [❌ 3/4](#typing) | [❌ 3/6](#tests-and-coverage) | [❌ 11/12](#linting) | [❌ 6/9](#documentation) | [✅ 4/4](#releases) | [10](PROJECTS.md#scrapycssselect) | [`2834f2c`](https://github.com/scrapy/cssselect/commit/2834f2cd0d1605e44e0aae6945cbed8ab1609f66) |
| [scrapy/formerly](https://github.com/scrapy/formerly) | [✅ 5/5](#python-versions) | [✅ 7/7](#packaging) | [➖](#dependencies) | [✅ 4/4](#typing) | [❌ 5/6](#tests-and-coverage) | [✅ 10/10](#linting) | [❌ 3/5](#documentation) | [✅ 4/4](#releases) | [3](PROJECTS.md#scrapyformerly) | [`7d3d184`](https://github.com/scrapy/formerly/commit/7d3d184e2145ed8c67d2144744c3c96350733dc3) |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | [❌ 4/5](#python-versions) | [✅ 7/7](#packaging) | [✅ 1/1](#dependencies) | [❌ 3/4](#typing) | [❌ 3/7](#tests-and-coverage) | [❌ 9/10](#linting) | [❌ 2/5](#documentation) | [❌ 3/4](#releases) | [11](PROJECTS.md#scrapyitemadapter) | [`9bab3af`](https://github.com/scrapy/itemadapter/commit/9bab3af2034d0e2cf309cce1315f464dab412be6) |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | [❌ 4/5](#python-versions) | [✅ 7/7](#packaging) | [✅ 2/2](#dependencies) | [✅ 4/4](#typing) | [❌ 4/6](#tests-and-coverage) | [❌ 12/13](#linting) | [❌ 5/9](#documentation) | [❌ 2/4](#releases) | [10](PROJECTS.md#scrapyitemloaders) | [`2481aee`](https://github.com/scrapy/itemloaders/commit/2481aee65f978357afa8317c6ca84f32e07d2a32) |
| [scrapy/parsel](https://github.com/scrapy/parsel) | [❌ 4/5](#python-versions) | [✅ 7/7](#packaging) | [✅ 2/2](#dependencies) | [✅ 4/4](#typing) | [❌ 5/6](#tests-and-coverage) | [❌ 12/13](#linting) | [❌ 7/11](#documentation) | [✅ 4/4](#releases) | [7](PROJECTS.md#scrapyparsel) | [`8a3f041`](https://github.com/scrapy/parsel/commit/8a3f0412868d65626364db66a84f32fda15776b2) |
| [scrapy/protego](https://github.com/scrapy/protego) | [❌ 4/5](#python-versions) | [✅ 7/7](#packaging) | [➖](#dependencies) | [✅ 4/4](#typing) | [❌ 5/6](#tests-and-coverage) | [❌ 9/10](#linting) | [❌ 3/5](#documentation) | [✅ 4/4](#releases) | [5](PROJECTS.md#scrapyprotego) | [`d311dc9`](https://github.com/scrapy/protego/commit/d311dc9154767341aaf7661402cda3ddef9c2225) |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | [❌ 3/5](#python-versions) | [❌ 6/7](#packaging) | [➖](#dependencies) | [❌ 3/4](#typing) | [❌ 4/6](#tests-and-coverage) | [❌ 9/10](#linting) | [❌ 3/5](#documentation) | [✅ 4/4](#releases) | [9](PROJECTS.md#scrapyqueuelib) | [`d4ed6ab`](https://github.com/scrapy/queuelib/commit/d4ed6abbce003f953cc6a1163d2ea396243417e5) |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | [❌ 4/5](#python-versions) | [✅ 7/7](#packaging) | [➖](#dependencies) | [❌ 3/4](#typing) | [❌ 4/6](#tests-and-coverage) | [❌ 11/13](#linting) | [❌ 5/9](#documentation) | [✅ 4/4](#releases) | [10](PROJECTS.md#scrapyw3lib) | [`b9d6f65`](https://github.com/scrapy/w3lib/commit/b9d6f65c83f49358269d089a700c4e24cf578a36) |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | [❌ 1/5](#python-versions) | [✅ 7/7](#packaging) | [➖](#dependencies) | [❌ 1/3](#typing) | [❌ 2/6](#tests-and-coverage) | [❌ 8/10](#linting) | [❌ 2/5](#documentation) | [✅ 4/4](#releases) | [15](PROJECTS.md#scrapyxtractmime) | [`9d50fcb`](https://github.com/scrapy/xtractmime/commit/9d50fcb0d7abd7a96f7dee746d9285faba4af6db) |
| **Scrapy plugins** | | | | | | | | | | |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | [✅ 3/3](#python-versions) | [✅ 7/7](#packaging) | [✅ 2/2](#dependencies) | [✅ 4/4](#typing) | [❌ 5/7](#tests-and-coverage) | [✅ 10/10](#linting) | [❌ 3/5](#documentation) | [✅ 4/4](#releases) | [4](PROJECTS.md#scrapy-pluginsscrapy-download-handlers-incubator) | [`bfb37fb`](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator/commit/bfb37fb5fdf1c2ffcde595a47f053443c988c15f) |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | [❌ 0/3](#python-versions) | [❌ 2/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 1/3](#typing) | [❌ 1/7](#tests-and-coverage) | [❌ 4/11](#linting) | [❌ 7/11](#documentation) | [❌ 1/4](#releases) | [29](PROJECTS.md#scrapy-pluginsscrapy-playwright) | [`2658f86`](https://github.com/scrapy-plugins/scrapy-playwright/commit/2658f86a4771b918dbe1d32c345ca70e34d43648) |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | [❌ 4/5](#python-versions) | [❌ 3/6](#packaging) | [✅ 2/2](#dependencies) | [✅ 4/4](#typing) | [❌ 4/7](#tests-and-coverage) | [❌ 11/12](#linting) | [❌ 7/11](#documentation) | [❌ 2/4](#releases) | [14](PROJECTS.md#scrapy-pluginsscrapy-spider-metadata) | [`a8f7a8b`](https://github.com/scrapy-plugins/scrapy-spider-metadata/commit/a8f7a8b52e8b1bd57dfe8f522ac58b98a2c99c76) |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | [❌ 0/3](#python-versions) | [❌ 2/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/4](#typing) | [❌ 2/7](#tests-and-coverage) | [❌ 2/7](#linting) | [❌ 2/4](#documentation) | [❌ 1/4](#releases) | [24](PROJECTS.md#zytedataduplicate-url-discarder) | [`8db08b3`](https://github.com/zytedata/duplicate-url-discarder/commit/8db08b3edf638f34ee6ad7393612f579b5bfb90f) |
| [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules) | [❌ 0/3](#python-versions) | [❌ 2/6](#packaging) | [➖](#dependencies) | [❌ 3/4](#typing) | [❌ 1/6](#tests-and-coverage) | [❌ 2/7](#linting) | [❌ 2/4](#documentation) | [❌ 1/4](#releases) | [23](PROJECTS.md#zytedataduplicate-url-discarder-rules) | [`7281048`](https://github.com/zytedata/duplicate-url-discarder-rules/commit/7281048b2cfa0538c0b355e8f91185f27367649d) |
| **Scrapy tools** | | | | | | | | | | |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | [❌ 0/3](#python-versions) | [❌ 6/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 1/3](#typing) | [❌ 4/6](#tests-and-coverage) | [❌ 10/12](#linting) | [❌ 7/11](#documentation) | [❌ 3/4](#releases) | [15](PROJECTS.md#scrapyscrapy-lint) | [`ca79b29`](https://github.com/scrapy/scrapy-lint/commit/ca79b29dd89f14c33d1df623034449dc2f11f2af) |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | [❌ 0/3](#python-versions) | [✅ 7/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 1/3](#typing) | [❌ 1/5](#tests-and-coverage) | [❌ 7/11](#linting) | [❌ 6/11](#documentation) | [❌ 2/4](#releases) | [20](PROJECTS.md#scrapinghubscrapyrt) | [`066cdaf`](https://github.com/scrapinghub/scrapyrt/commit/066cdafb9dc5e864f3e1dd19cb7fafec7fefb7fe) |
| **Feed exporters** | | | | | | | | | | |
| [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc) | [❌ 0/3](#python-versions) | [❌ 2/6](#packaging) | [❌ 1/2](#dependencies) | [❌ 0/2](#typing) | [❌ 0/5](#tests-and-coverage) | [❌ 4/9](#linting) | [❌ 0/4](#documentation) | [❌ 1/4](#releases) | [27](PROJECTS.md#scrapy-pluginsscrapy-feedexport-warc) | [`ad7956f`](https://github.com/scrapy-plugins/scrapy-feedexport-warc/commit/ad7956f4825fa2c4671c1849a8ad7a4eb2cc34d1) |
| [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage) | [❌ 0/3](#python-versions) | [❌ 1/4](#packaging) | [❌ 0/1](#dependencies) | [❌ 1/3](#typing) | [❌ 0/5](#tests-and-coverage) | [❌ 0/1](#linting) | [❌ 0/4](#documentation) | [❌ 0/4](#releases) | [23](PROJECTS.md#scrapy-pluginsscrapy-feedexporter-azure-storage) | [`4f36ff8`](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage/commit/4f36ff805239bace39bacc8c1e02cc8c876013b4) |
| [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox) | [❌ 0/2](#python-versions) | [❌ 1/4](#packaging) | [❌ 0/1](#dependencies) | [❌ 0/2](#typing) | [❌ 0/5](#tests-and-coverage) | [❌ 0/1](#linting) | [❌ 0/4](#documentation) | [❌ 0/4](#releases) | [22](PROJECTS.md#scrapy-pluginsscrapy-feedexporter-dropbox) | [`4e4cca6`](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox/commit/4e4cca6f5240d790708219c0344b812eb76a854f) |
| [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive) | [❌ 0/3](#python-versions) | [❌ 3/6](#packaging) | [❌ 0/2](#dependencies) | [❌ 0/2](#typing) | [❌ 0/5](#tests-and-coverage) | [❌ 7/10](#linting) | [❌ 3/5](#documentation) | [❌ 3/4](#releases) | [21](PROJECTS.md#scrapy-pluginsscrapy-feedexporter-google-drive) | [`369598d`](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive/commit/369598d8205938ba851af91fed913335bfd12cd9) |
| [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets) | [❌ 0/3](#python-versions) | [❌ 1/4](#packaging) | [❌ 0/1](#dependencies) | [❌ 0/2](#typing) | [❌ 0/5](#tests-and-coverage) | [❌ 0/1](#linting) | [❌ 0/4](#documentation) | [❌ 0/4](#releases) | [23](PROJECTS.md#scrapy-pluginsscrapy-feedexporter-google-sheets) | [`25f2a8c`](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets/commit/25f2a8c6079e85823c7e640b17eea2ad5ed8f767) |
| [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive) | [❌ 0/3](#python-versions) | [❌ 2/6](#packaging) | [❌ 0/2](#dependencies) | [❌ 0/2](#typing) | [❌ 0/5](#tests-and-coverage) | [❌ 5/9](#linting) | [❌ 2/5](#documentation) | [❌ 3/4](#releases) | [24](PROJECTS.md#scrapy-pluginsscrapy-feedexporter-onedrive) | [`b97aab3`](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive/commit/b97aab3d3a50e7d7fe829285a7e53fd7f80ea758) |
| [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp) | [❌ 0/3](#python-versions) | [❌ 2/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 0/2](#typing) | [❌ 2/7](#tests-and-coverage) | [❌ 4/9](#linting) | [❌ 3/5](#documentation) | [❌ 3/4](#releases) | [22](PROJECTS.md#scrapy-pluginsscrapy-feedexporter-sftp) | [`38c9e5b`](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp/commit/38c9e5b244bfa363de9ede92f7069ae7bcbce469) |
| **scrapy-poet and its deps** | | | | | | | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | [❌ 1/3](#python-versions) | [❌ 5/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 3/4](#typing) | [❌ 3/7](#tests-and-coverage) | [❌ 8/11](#linting) | [⚠️ 10/11](#documentation) | [❌ 3/4](#releases) | [14](PROJECTS.md#scrapinghubscrapy-poet) | [`fd70074`](https://github.com/scrapinghub/scrapy-poet/commit/fd700743f97f6a63ed37d3d185abb2477f09d3af) |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | [❌ 2/3](#python-versions) | [❌ 6/7](#packaging) | [➖](#dependencies) | [❌ 3/4](#typing) | [❌ 4/6](#tests-and-coverage) | [❌ 9/10](#linting) | [❌ 3/5](#documentation) | [✅ 4/4](#releases) | [8](PROJECTS.md#scrapinghubandi) | [`5b7f109`](https://github.com/scrapinghub/andi/commit/5b7f1094a5526a016477a3d1c3f7617909f3bbbf) |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | [❌ 0/3](#python-versions) | [❌ 4/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/4](#typing) | [❌ 2/6](#tests-and-coverage) | [❌ 10/12](#linting) | [❌ 8/11](#documentation) | [❌ 3/4](#releases) | [18](PROJECTS.md#scrapinghubweb-poet) | [`599e041`](https://github.com/scrapinghub/web-poet/commit/599e04110b617531a32884d439a5666126344fdd) |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | [✅ 3/3](#python-versions) | [❌ 6/7](#packaging) | [✅ 2/2](#dependencies) | [✅ 4/4](#typing) | [❌ 4/6](#tests-and-coverage) | [❌ 11/12](#linting) | [❌ 7/11](#documentation) | [✅ 4/4](#releases) | [8](PROJECTS.md#zytedataurl-matcher) | [`6fe906b`](https://github.com/zytedata/url-matcher/commit/6fe906b4aba1632fa41fc116ed29de84e68bba04) |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | [❌ 2/3](#python-versions) | [✅ 4/4](#packaging) | [❌ 1/2](#dependencies) | [❌ 1/3](#typing) | [❌ 0/4](#tests-and-coverage) | [❌ 4/9](#linting) | [❌ 2/5](#documentation) | [✅ 4/4](#releases) | [16](PROJECTS.md#scrapyfrostwork) | [`d1e2d5c`](https://github.com/scrapy/frostwork/commit/d1e2d5c27f4b2664a923e37bc5e0fdf53fd42c02) |
| **Zyte API** | | | | | | | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | [✅ 3/3](#python-versions) | [❌ 6/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/4](#typing) | [❌ 5/7](#tests-and-coverage) | [❌ 11/12](#linting) | [❌ 7/11](#documentation) | [❌ 3/4](#releases) | [11](PROJECTS.md#scrapy-pluginsscrapy-zyte-api) | [`9b63ad9`](https://github.com/scrapy-plugins/scrapy-zyte-api/commit/9b63ad94dbc95e276c3e2981dbdd88cf96a4f88d) |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | [✅ 3/3](#python-versions) | [❌ 5/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/4](#typing) | [❌ 2/6](#tests-and-coverage) | [❌ 7/11](#linting) | [⚠️ 10/11](#documentation) | [❌ 3/4](#releases) | [14](PROJECTS.md#zytedatapython-zyte-api) | [`5ca09d3`](https://github.com/zytedata/python-zyte-api/commit/5ca09d3691312b0d51fba41e20f92a8426e51f49) |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | [❌ 0/3](#python-versions) | [❌ 1/4](#packaging) | [✅ 1/1](#dependencies) | [❌ 1/3](#typing) | [❌ 1/7](#tests-and-coverage) | [❌ 2/9](#linting) | [❌ 6/9](#documentation) | [❌ 3/4](#releases) | [25](PROJECTS.md#scrapy-pluginsscrapy-zyte-smartproxy) | [`debd444`](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy/commit/debd4445343d0c3a1eba9fa0ce269613bb3b9d5c) |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | [✅ 3/3](#python-versions) | [❌ 6/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/4](#typing) | [❌ 3/6](#tests-and-coverage) | [❌ 11/12](#linting) | [❌ 6/11](#documentation) | [✅ 4/4](#releases) | [12](PROJECTS.md#zytedatazyte-common-items) | [`fccd5d4`](https://github.com/zytedata/zyte-common-items/commit/fccd5d44cf037698c3742a4362cf492712878cf1) |
| **Scrapy Cloud** | | | | | | | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | [❌ 1/5](#python-versions) | [❌ 0/4](#packaging) | [❌ 0/1](#dependencies) | [❌ 0/2](#typing) | [❌ 1/6](#tests-and-coverage) | [❌ 0/9](#linting) | [⚠️ 10/11](#documentation) | [✅ 4/4](#releases) | [26](PROJECTS.md#scrapinghubpython-scrapinghub) | [`c60ab46`](https://github.com/scrapinghub/python-scrapinghub/commit/c60ab4620f67f302a5685e30674fdf41c281af39) |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | [❌ 0/3](#python-versions) | [❌ 4/7](#packaging) | [❌ 1/2](#dependencies) | [❌ 0/2](#typing) | [❌ 1/6](#tests-and-coverage) | [❌ 5/11](#linting) | [❌ 10/11](#documentation) | [❌ 2/4](#releases) | [23](PROJECTS.md#scrapinghubshub) | [`a174e7e`](https://github.com/scrapinghub/shub/commit/a174e7ebc22cded1a1510bfc9cf572c5b79018cf) |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [❌ 0/3](#python-versions) | [❌ 1/4](#packaging) | [❌ 0/1](#dependencies) | [❌ 0/2](#typing) | [❌ 1/7](#tests-and-coverage) | [❌ 0/4](#linting) | [❌ 2/5](#documentation) | [❌ 2/4](#releases) | [24](PROJECTS.md#scrapinghubscrapinghub-entrypoint-scrapy) | [`bf9632c`](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy/commit/bf9632c78355b545126363ce557106c1b9c3bb54) |
| [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow) | [❌ 0/2](#python-versions) | [❌ 0/4](#packaging) | [❌ 0/1](#dependencies) | [❌ 1/3](#typing) | [❌ 1/5](#tests-and-coverage) | [❌ 0/4](#linting) | [❌ 1/4](#documentation) | [❌ 0/4](#releases) | [24](PROJECTS.md#scrapinghubshub-workflow) | [`5471c35`](https://github.com/scrapinghub/shub-workflow/commit/5471c352f0f4d7ecada0381b69f072a325b87cfa) |
| [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera) | [❌ 0/3](#python-versions) | [❌ 0/4](#packaging) | [✅ 1/1](#dependencies) | [❌ 0/2](#typing) | [❌ 1/7](#tests-and-coverage) | [❌ 3/9](#linting) | [❌ 3/5](#documentation) | [❌ 2/4](#releases) | [25](PROJECTS.md#scrapinghubscrapy-frontera) | [`56ea2e1`](https://github.com/scrapinghub/scrapy-frontera/commit/56ea2e1ef39a174eac61da2edcdb21d1f1ecf5e5) |
| [scrapinghub/frontera](https://github.com/scrapinghub/frontera) | [❌ 0/2](#python-versions) | [❌ 0/4](#packaging) | [❌ 0/1](#dependencies) | [❌ 0/2](#typing) | [❌ 2/7](#tests-and-coverage) | [❌ 0/4](#linting) | [❌ 0/4](#documentation) | [❌ 1/4](#releases) | [25](PROJECTS.md#scrapinghubfrontera) | [`c94beae`](https://github.com/scrapinghub/frontera/commit/c94beae2f438492139d24759729d0201779ccf1c) |
| [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend) | [❌ 0/2](#python-versions) | [❌ 0/4](#packaging) | [✅ 1/1](#dependencies) | [❌ 0/2](#typing) | [❌ 1/6](#tests-and-coverage) | [❌ 3/9](#linting) | [❌ 2/5](#documentation) | [❌ 2/4](#releases) | [24](PROJECTS.md#scrapinghubhcf-backend) | [`bbdc50c`](https://github.com/scrapinghub/hcf-backend/commit/bbdc50cd1d250742234aacc2d5da10c4fe4d9508) |
| **Data extraction** | | | | | | | | | | |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | [❌ 0/3](#python-versions) | [✅ 7/7](#packaging) | [❌ 0/2](#dependencies) | [❌ 3/4](#typing) | [❌ 3/6](#tests-and-coverage) | [❌ 11/12](#linting) | [❌ 5/9](#documentation) | [✅ 4/4](#releases) | [14](PROJECTS.md#zytedatazyte-parsers) | [`4f5d08d`](https://github.com/zytedata/zyte-parsers/commit/4f5d08d1be951fa438f0aedd598d61a61c360ea0) |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | [❌ 0/3](#python-versions) | [✅ 7/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 3/4](#typing) | [❌ 3/6](#tests-and-coverage) | [❌ 9/10](#linting) | [❌ 3/5](#documentation) | [✅ 4/4](#releases) | [10](PROJECTS.md#zytedataclear-html) | [`6b820b1`](https://github.com/zytedata/clear-html/commit/6b820b13221145ceb0814e47e9583e5574d28865) |
| [zytedata/html-text](https://github.com/zytedata/html-text) | [✅ 3/3](#python-versions) | [❌ 6/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 3/4](#typing) | [❌ 2/6](#tests-and-coverage) | [❌ 6/9](#linting) | [❌ 3/5](#documentation) | [❌ 2/4](#releases) | [13](PROJECTS.md#zytedatahtml-text) | [`3955be2`](https://github.com/zytedata/html-text/commit/3955be2f85381e7198bdd99f5e9ce903786c7a9e) |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | [❌ 0/3](#python-versions) | [❌ 5/7](#packaging) | [❌ 1/2](#dependencies) | [❌ 3/4](#typing) | [❌ 2/6](#tests-and-coverage) | [❌ 8/11](#linting) | [❌ 3/5](#documentation) | [❌ 2/4](#releases) | [18](PROJECTS.md#scrapinghubprice-parser) | [`6718bfe`](https://github.com/scrapinghub/price-parser/commit/6718bfe8447f2de17ecc152d3ad2a4c51520c755) |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | [❌ 0/3](#python-versions) | [❌ 2/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/3](#typing) | [❌ 2/6](#tests-and-coverage) | [❌ 7/13](#linting) | [❌ 5/9](#documentation) | [❌ 3/4](#releases) | [23](PROJECTS.md#scrapinghubdateparser) | [`b1a87f9`](https://github.com/scrapinghub/dateparser/commit/b1a87f9f9c76e612e68a0137521ed3e2e1114702) |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [❌ 0/3](#python-versions) | [❌ 1/4](#packaging) | [❌ 0/1](#dependencies) | [❌ 1/3](#typing) | [❌ 2/6](#tests-and-coverage) | [❌ 2/7](#linting) | [❌ 2/4](#documentation) | [❌ 1/4](#releases) | [23](PROJECTS.md#scrapinghubextruct) | [`d24f541`](https://github.com/scrapinghub/extruct/commit/d24f5414fd32c874989492ebd04cb1deb6d7d04e) |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | [❌ 0/2](#python-versions) | [❌ 0/4](#packaging) | [❌ 0/1](#dependencies) | [❌ 1/3](#typing) | [❌ 2/6](#tests-and-coverage) | [❌ 4/9](#linting) | [❌ 2/4](#documentation) | [❌ 0/4](#releases) | [24](PROJECTS.md#scrapinghubnumber-parser) | [`a126357`](https://github.com/scrapinghub/number-parser/commit/a1263578628a7743054879095e50532fba1cdb67) |
| **Forms** | | | | | | | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | [❌ 0/3](#python-versions) | [❌ 5/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 3/4](#typing) | [❌ 4/6](#tests-and-coverage) | [❌ 11/12](#linting) | [❌ 5/9](#documentation) | [✅ 4/4](#releases) | [13](PROJECTS.md#scrapyform2request) | [`93af5f1`](https://github.com/scrapy/form2request/commit/93af5f15b9b0c5a0cd0cbddbc404c9ee28006578) |
| [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus) | [❌ 0/3](#python-versions) | [❌ 1/4](#packaging) | [✅ 1/1](#dependencies) | [❌ 0/2](#typing) | [❌ 2/5](#tests-and-coverage) | [❌ 2/9](#linting) | [❌ 4/9](#documentation) | [❌ 2/4](#releases) | [25](PROJECTS.md#scrapinghubformasaurus) | [`4bb46a9`](https://github.com/scrapinghub/Formasaurus/commit/4bb46a95c7851622bb63ca7459d4d6d2587297ab) |
| [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite) | [❌ 0/2](#python-versions) | [❌ 1/4](#packaging) | [✅ 1/1](#dependencies) | [❌ 0/2](#typing) | [❌ 2/5](#tests-and-coverage) | [❌ 2/9](#linting) | [❌ 3/8](#documentation) | [❌ 1/4](#releases) | [25](PROJECTS.md#scrapinghubsklearn-crfsuite) | [`e18a02a`](https://github.com/scrapinghub/sklearn-crfsuite/commit/e18a02ae11b61f703c0ec460c44cfdd90db00591) |
| [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite) | [❌ 0/3](#python-versions) | [❌ 0/6](#packaging) | [❌ 0/1](#dependencies) | [❌ 0/2](#typing) | [❌ 0/4](#tests-and-coverage) | [❌ 0/6](#linting) | [❌ 6/9](#documentation) | [❌ 2/4](#releases) | [27](PROJECTS.md#scrapinghubpython-crfsuite) | [`d3ee2eb`](https://github.com/scrapinghub/python-crfsuite/commit/d3ee2eba443d5d3b313741bed5076b5a36a840d1) |
| **Monitoring** | | | | | | | | | | |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | [❌ 0/3](#python-versions) | [❌ 6/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 1/3](#typing) | [❌ 3/7](#tests-and-coverage) | [❌ 9/11](#linting) | [❌ 5/9](#documentation) | [❌ 3/4](#releases) | [17](PROJECTS.md#scrapinghubspidermon) | [`5bac6dd`](https://github.com/scrapinghub/spidermon/commit/5bac6dd768463ece308ca67dc9fd18525364c940) |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | [❌ 0/2](#python-versions) | [❌ 1/4](#packaging) | [❌ 0/1](#dependencies) | [❌ 0/2](#typing) | [❌ 1/5](#tests-and-coverage) | [❌ 0/4](#linting) | [❌ 0/4](#documentation) | [❌ 0/4](#releases) | [24](PROJECTS.md#scrapy-pluginszyte-spidermon) | [`8186fbe`](https://github.com/scrapy-plugins/zyte-spidermon/commit/8186fbe6d1c9233dc576ec725d3b2e046de032dd) |
| **AI agents** | | | | | | | | | | |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | [➖](#python-versions) | [➖](#packaging) | [➖](#dependencies) | [➖](#typing) | [➖](#tests-and-coverage) | [➖](#linting) | [⚠️ 3/4](#documentation) | [✅ 1/1](#releases) | [1](PROJECTS.md#scrapyscrapy-agent-plugin) | [`d424e42`](https://github.com/scrapy/scrapy-agent-plugin/commit/d424e42a35116c108e986614b75ec7cd9cf9909e) |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | [❌ 2/3](#python-versions) | [✅ 7/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 3/4](#typing) | [❌ 4/6](#tests-and-coverage) | [❌ 9/10](#linting) | [❌ 2/5](#documentation) | [✅ 4/4](#releases) | [8](PROJECTS.md#scrapyscrapy-mcp-official) | [`66aeef9`](https://github.com/scrapy/scrapy-mcp-official/commit/66aeef96b7707072811132e33400b08cb45cff37) |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | [❌ 0/3](#python-versions) | [❌ 4/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 0/2](#typing) | [❌ 4/6](#tests-and-coverage) | [❌ 10/12](#linting) | [❌ 7/11](#documentation) | [❌ 3/4](#releases) | [17](PROJECTS.md#zytedataagent-exam) | [`e25c638`](https://github.com/zytedata/agent-exam/commit/e25c6380c59e5386caa7085795af12d2dbd2931c) |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | [❌ 0/3](#python-versions) | [❌ 4/7](#packaging) | [❌ 1/2](#dependencies) | [❌ 0/2](#typing) | [❌ 0/4](#tests-and-coverage) | [❌ 7/10](#linting) | [❌ 2/5](#documentation) | [✅ 4/4](#releases) | [19](PROJECTS.md#zytedataclaude-measure-usage) | [`6b4310a`](https://github.com/zytedata/claude-measure-usage/commit/6b4310afeaf2e9c81acd861f8d9bd62006357bf7) |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | [❌ 1/3](#python-versions) | [❌ 5/7](#packaging) | [❌ 0/2](#dependencies) | [❌ 0/2](#typing) | [❌ 0/4](#tests-and-coverage) | [❌ 1/5](#linting) | [❌ 1/4](#documentation) | [❌ 3/4](#releases) | [20](PROJECTS.md#zytedataharness-run) | [`cc11c24`](https://github.com/zytedata/harness-run/commit/cc11c24d5494bdca045f3cf0f08d5d119918b77e) |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | [❌ 2/3](#python-versions) | [❌ 5/7](#packaging) | [❌ 1/2](#dependencies) | [❌ 2/3](#typing) | [❌ 0/4](#tests-and-coverage) | [❌ 8/10](#linting) | [❌ 3/5](#documentation) | [❌ 3/4](#releases) | [14](PROJECTS.md#scrapysphinx-llm-friendly) | [`4672e79`](https://github.com/scrapy/sphinx-llm-friendly/commit/4672e792d58f8c9a6929e7580fe9d6026dc453fa) |
| **Maintenance** | | | | | | | | | | |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | [❌ 0/3](#python-versions) | [❌ 5/7](#packaging) | [❌ 0/2](#dependencies) | [❌ 2/3](#typing) | [❌ 0/4](#tests-and-coverage) | [❌ 8/10](#linting) | [❌ 3/5](#documentation) | [❌ 3/4](#releases) | [17](PROJECTS.md#scrapysphinx-scrapy) | [`a740c8e`](https://github.com/scrapy/sphinx-scrapy/commit/a740c8e0f53c96209f65fa5f444eb3a02ca7b94b) |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | [➖](#python-versions) | [➖](#packaging) | [➖](#dependencies) | [➖](#typing) | [➖](#tests-and-coverage) | [❌ 6/8](#linting) | [❌ 2/4](#documentation) | [✅ 1/1](#releases) | [4](PROJECTS.md#scrapyunattended-pr-guard) | [`f15191e`](https://github.com/scrapy/unattended-pr-guard/commit/f15191eebabc3dc4421f8fd205660e9040ef504e) |
| [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance) | [❌ 1/2](#python-versions) | [✅ 4/4](#packaging) | [➖](#dependencies) | [✅ 1/1](#typing) | [❌ 0/4](#tests-and-coverage) | [✅ 10/10](#linting) | [❌ 0/2](#documentation) | [➖](#releases) | [7](PROJECTS.md#zytedatazyte-oss-maintenance) | [`5383946`](https://github.com/zytedata/zyte-oss-maintenance/commit/5383946efcd3c8a4a51d782739b565f59b6bb786) |

## Release candidates

Projects with commits since their latest release, oldest release first.

- [scrapinghub/frontera](https://github.com/scrapinghub/frontera): 0.8.1 (2019-04-05)
- [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): 0.3.2 (2023-03-28)
- [scrapy/xtractmime](https://github.com/scrapy/xtractmime): 0.2.1 (2024-01-16)
- [scrapy/form2request](https://github.com/scrapy/form2request): 0.2.0 (2024-07-15)
- [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): 0.2.0 (2024-09-26)
- [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): 2024.11.5 (2024-11-05)
- [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): 0.10.0 (2024-11-07)
- [scrapinghub/extruct](https://github.com/scrapinghub/extruct): 0.18.0 (2024-11-08)
- [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): 0.3.0 (2024-12-30)
- [zytedata/url-matcher](https://github.com/zytedata/url-matcher): 0.6.0 (2025-02-14)
- [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): 2.4.1 (2025-03-24)
- [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): 0.3.0 (2025-06-06)
- [zytedata/html-text](https://github.com/zytedata/html-text): 0.7.1 (2025-10-06)
- [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): 0.6.0 (2025-10-24)
- [zytedata/clear-html](https://github.com/zytedata/clear-html): 0.5.0 (2025-10-24)
- [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): 0.9.12 (2025-12-23)
- [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): 0.1.1 (2026-01-27)
- [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): 0.18.1 (2026-01-28)
- [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): 0.5.1 (2026-03-19)
- [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): 0.27.2 (2026-04-28)
- [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): 0.24.1 (2026-04-28)
- [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): 0.18.1 (2026-06-29)
- [scrapinghub/shub](https://github.com/scrapinghub/shub): 2.18.1 (2026-07-08)
- [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): 0.0.48 (2026-07-10)
- [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): 0.11.0 (2026-07-23)
- [scrapy/formerly](https://github.com/scrapy/formerly): 0.1.0 (2026-08-05)
- [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): 1.27.0 (2026-08-10)
- [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): 2.9.0 (2026-08-12)
- [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): 0.36.0 (2026-08-20)
- [scrapy/queuelib](https://github.com/scrapy/queuelib): 1.10.0 (2026-08-24)
- [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): 1.4.3 (2026-09-03)
- [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official): 0.1.2 (2026-09-07)
- [scrapy/scrapy](https://github.com/scrapy/scrapy): 2.19.0 (2026-09-10)
- [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): 0.1.1 (2026-09-14)
- [scrapinghub/andi](https://github.com/scrapinghub/andi): 0.9.0 (2026-09-17)
- [scrapy/protego](https://github.com/scrapy/protego): 0.7.0 (2026-09-21)
- [scrapy/frostwork](https://github.com/scrapy/frostwork): 0.1.6 (2026-09-23)
- [zytedata/harness-run](https://github.com/zytedata/harness-run): 0.4.0 (2026-09-23)
- [scrapy/parsel](https://github.com/scrapy/parsel): 1.12.1 (2026-09-28)
- [scrapy/itemloaders](https://github.com/scrapy/itemloaders): 1.5.0 (2026-09-29)
- [scrapy/w3lib](https://github.com/scrapy/w3lib): 2.5.0 (2026-09-30)
- [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): 0.7.0 (2026-10-03)
- [scrapy/cssselect](https://github.com/scrapy/cssselect): 1.6.0 (2026-10-09)
- [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): 0.31.0 (2026-10-16)
- [zytedata/agent-exam](https://github.com/zytedata/agent-exam): 0.3.0 (2026-10-20)
- [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): 0.15.0 (2026-10-27)
- [scrapy/itemadapter](https://github.com/scrapy/itemadapter): 0.14.0 (2026-10-29)
- [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): 1.14.46 (2026-10-30)

## Python versions

| Check | Statement | Results |
| --- | --- | --- |
| [`no-eol-python`](#no-eol-python) | Support for end-of-life Python versions is dropped. | 18/60 passing |
| [`latest-python`](#latest-python) | The latest stable Python version is declared as supported and tested in CI. | 20/60 passing |
| [`unreleased-python`](#unreleased-python) | The upcoming Python version is tested in CI, once it has a release candidate. | 0/0 passing |
| [`python-classifiers`](#python-classifiers) | Python version classifiers match requires-python: there is one for every supported Python version it allows, and none for versions it excludes. | 20/52 passing |
| [`supports-pypy`](#supports-pypy) | The project supports PyPy: it has the PyPy classifier or tests PyPy in CI. | 11/60 yes |
| [`latest-pypy`](#latest-pypy) | The latest PyPy version is declared as supported and tested in CI. | 1/11 passing |
| [`no-eol-pypy`](#no-eol-pypy) | End-of-life PyPy versions are not tested in CI. | 11/11 passing |

| Project | [no-eol-python](#no-eol-python) | [latest-python](#latest-python) | [unreleased-python](#unreleased-python) | [python-classifiers](#python-classifiers) | [supports-pypy](#supports-pypy) | [latest-pypy](#latest-pypy) | [no-eol-pypy](#no-eol-pypy) |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Scrapy and its deps** | | | | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | yes | [❌](#latest-pypy) | ✅ |
| [scrapy/formerly](https://github.com/scrapy/formerly) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | yes | ✅ | ✅ |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | yes | [❌](#latest-pypy) | ✅ |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | yes | [❌](#latest-pypy) | ✅ |
| [scrapy/parsel](https://github.com/scrapy/parsel) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | yes | [❌](#latest-pypy) | ✅ |
| [scrapy/protego](https://github.com/scrapy/protego) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | yes | [❌](#latest-pypy) | ✅ |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | [❌](#no-eol-python) | ✅ | [➖](#unreleased-python) | ✅ | yes | [❌](#latest-pypy) | ✅ |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | yes | [❌](#latest-pypy) | ✅ |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | yes | [❌](#latest-pypy) | ✅ |
| **Scrapy plugins** | | | | | | | |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | yes | [❌](#latest-pypy) | ✅ |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **Scrapy tools** | | | | | | | |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **Feed exporters** | | | | | | | |
| [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [➖](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **scrapy-poet and its deps** | | | | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | [❌](#no-eol-python) | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | [❌](#no-eol-python) | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **Zyte API** | | | | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **Scrapy Cloud** | | | | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | yes | [❌](#latest-pypy) | ✅ |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [➖](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/frontera](https://github.com/scrapinghub/frontera) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [➖](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [➖](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **Data extraction** | | | | | | | |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/html-text](https://github.com/zytedata/html-text) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [➖](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **Forms** | | | | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [➖](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **Monitoring** | | | | | | | |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [➖](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **AI agents** | | | | | | | |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | [➖](#no-eol-python) | [➖](#latest-python) | [➖](#unreleased-python) | [➖](#python-classifiers) | [➖](#supports-pypy) | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | [❌](#no-eol-python) | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | ✅ | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | [❌](#no-eol-python) | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **Maintenance** | | | | | | | |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | [➖](#no-eol-python) | [➖](#latest-python) | [➖](#unreleased-python) | [➖](#python-classifiers) | [➖](#supports-pypy) | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance) | ✅ | [❌](#latest-python) | [➖](#unreleased-python) | [➖](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |

### no-eol-python

Support for end-of-life Python versions is dropped.

- ❌ [scrapy/queuelib](https://github.com/scrapy/queuelib): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): requires-python '>=3.8' allows 3.8 (EOL 2024-10-07), 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01)
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): requires-python is not declared
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): requires-python '>=3.8' allows 3.8 (EOL 2024-10-07), 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01)
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): requires-python '>=3.8' allows 3.8 (EOL 2024-10-07), 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.8, 3.9, 3.10
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [scrapinghub/andi](https://github.com/scrapinghub/andi): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): requires-python is not declared
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01)
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): requires-python is not declared
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): requires-python is not declared
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [zytedata/clear-html](https://github.com/zytedata/clear-html): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): requires-python '>=3.8' allows 3.8 (EOL 2024-10-07), 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.8, 3.9, 3.10
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): requires-python is not declared
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): requires-python is not declared
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): requires-python is not declared
- ❌ [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### latest-python

The latest stable Python version is declared as supported and tested in CI.

- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no 'Programming Language :: Python :: 3.15' classifier
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [zytedata/clear-html](https://github.com/zytedata/clear-html): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance): no 'Programming Language :: Python :: 3.15' classifier
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### unreleased-python

The upcoming Python version is tested in CI, once it has a release candidate.

- ➖ No upcoming Python version has a release candidate. [scrapy/scrapy](https://github.com/scrapy/scrapy), [scrapy/cssselect](https://github.com/scrapy/cssselect), [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/itemloaders](https://github.com/scrapy/itemloaders), [scrapy/parsel](https://github.com/scrapy/parsel), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/w3lib](https://github.com/scrapy/w3lib), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint), [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet), [zytedata/url-matcher](https://github.com/zytedata/url-matcher), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api), [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapy/form2request](https://github.com/scrapy/form2request), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [zytedata/agent-exam](https://github.com/zytedata/agent-exam), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### python-classifiers

Python version classifiers match requires-python: there is one for every supported Python version it allows, and none for versions it excludes.

- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no classifiers for 3.15
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no classifiers for 3.15
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no classifiers for 3.14, 3.15
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): no classifiers for 3.14, 3.15
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): no classifiers for 3.15
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no classifiers for 3.14, 3.15
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no classifiers for 3.13, 3.14, 3.15
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no Python version classifiers
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no classifiers for 3.15
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no Python version classifiers
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no classifiers for 3.14, 3.15
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): no classifiers for 3.14, 3.15
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): no classifiers for 3.15
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): no classifiers for 3.15
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no classifiers for 3.14, 3.15
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no classifiers for 3.14, 3.15
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no classifiers for 3.15
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no classifiers for 3.14, 3.15
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no Python version classifiers
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): no classifiers for 3.15
- ❌ [zytedata/clear-html](https://github.com/zytedata/clear-html): no classifiers for 3.15
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no classifiers for 3.15
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): no classifiers for 3.15
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no classifiers for 3.13, 3.14, 3.15
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): no classifiers for 3.15
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): no classifiers for 3.13, 3.14, 3.15
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no classifiers for 3.15
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): no classifiers for 3.15
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): no classifiers for 3.15
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no classifiers for 3.15
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no classifiers for 3.14, 3.15
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no classifiers for 3.15
- ➖ requires-python is not declared. [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### supports-pypy

The project supports PyPy: it has the PyPy classifier or tests PyPy in CI.

- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### latest-pypy

The latest PyPy version is declared as supported and tested in CI.

- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy/parsel](https://github.com/scrapy/parsel): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy/protego](https://github.com/scrapy/protego): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy/queuelib](https://github.com/scrapy/queuelib): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy/w3lib](https://github.com/scrapy/w3lib): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): PyPy 3.12 not found in CI workflows or tox config
- ➖ Does not support PyPy. [scrapy/scrapy](https://github.com/scrapy/scrapy), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint), [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet), [zytedata/url-matcher](https://github.com/zytedata/url-matcher), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api), [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapy/form2request](https://github.com/scrapy/form2request), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [zytedata/agent-exam](https://github.com/zytedata/agent-exam), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### no-eol-pypy

End-of-life PyPy versions are not tested in CI.

- ➖ Does not support PyPy. [scrapy/scrapy](https://github.com/scrapy/scrapy), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint), [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet), [zytedata/url-matcher](https://github.com/zytedata/url-matcher), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api), [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapy/form2request](https://github.com/scrapy/form2request), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [zytedata/agent-exam](https://github.com/zytedata/agent-exam), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

## Packaging

| Check | Statement | Results |
| --- | --- | --- |
| [`pyproject-metadata`](#pyproject-metadata) | Package metadata is in the [project] table of pyproject.toml, with no setup.py and no setuptools configuration in setup.cfg. | 43/60 passing |
| [`no-legacy-config`](#no-legacy-config) | There are no legacy configuration files, e.g. .coveragerc, pytest.ini, .flake8 or requirements-dev.txt, and no tool configuration in setup.cfg or tox.ini. | 41/60 passing |
| [`license`](#license) | The license: the license field of package metadata, or else the license classifiers. | BSD-3-Clause (23), BSD License (13), Apache-2.0 (11), MIT License (4), no (4), MIT (3), Apache Software License (2) |
| [`pep639-license`](#pep639-license) | The license is declared as an SPDX expression (PEP 639), without license classifiers. | 31/45 passing |
| [`hatchling`](#hatchling) | The build backend is hatchling. | 34/59 passing |
| [`sdist-contents`](#sdist-contents) | The sdist includes only listed files, which include the tests, the docs and the tox configuration. | 27/33 passing |
| [`project-urls`](#project-urls) | [project.urls] links to the source, the issue tracker, the changelog and, if there are Sphinx docs, the documentation, with labels that PyPI recognizes. | 22/44 passing |
| [`twine-check`](#twine-check) | `twine check` validates the built distributions in tox. | 35/58 passing |

| Project | [pyproject-metadata](#pyproject-metadata) | [no-legacy-config](#no-legacy-config) | [license](#license) | [pep639-license](#pep639-license) | [hatchling](#hatchling) | [sdist-contents](#sdist-contents) | [project-urls](#project-urls) | [twine-check](#twine-check) |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Scrapy and its deps** | | | | | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ | ✅ |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | [❌](#project-urls) | ✅ |
| [scrapy/formerly](https://github.com/scrapy/formerly) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ | ✅ |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ | ✅ |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ | ✅ |
| [scrapy/parsel](https://github.com/scrapy/parsel) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ | ✅ |
| [scrapy/protego](https://github.com/scrapy/protego) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ | ✅ |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | [❌](#sdist-contents) | ✅ | ✅ |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ | ✅ |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Scrapy plugins** | | | | | | | | |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ | ✅ |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | ✅ | [❌](#no-legacy-config) | BSD-3-Clause | ✅ | [❌](#hatchling) | [➖](#sdist-contents) | [❌](#project-urls) | [❌](#twine-check) |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | ✅ | ✅ | BSD License | [❌](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [❌](#project-urls) | ✅ |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | ✅ | [❌](#no-legacy-config) | BSD License | [❌](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [❌](#project-urls) | ✅ |
| [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules) | ✅ | [❌](#no-legacy-config) | MIT License | [❌](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [❌](#project-urls) | ✅ |
| **Scrapy tools** | | | | | | | | |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | ✅ | ✅ | MIT | ✅ | ✅ | ✅ | [❌](#project-urls) | ✅ |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Feed exporters** | | | | | | | | |
| [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc) | ✅ | ✅ | Apache Software License | [❌](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [❌](#project-urls) | [❌](#twine-check) |
| [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage) | [❌](#pyproject-metadata) | ✅ | no | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [❌](#twine-check) |
| [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox) | [❌](#pyproject-metadata) | ✅ | no | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [❌](#twine-check) |
| [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive) | ✅ | ✅ | BSD-3-Clause | ✅ | [❌](#hatchling) | [➖](#sdist-contents) | [❌](#project-urls) | [❌](#twine-check) |
| [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets) | [❌](#pyproject-metadata) | ✅ | no | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [❌](#twine-check) |
| [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive) | ✅ | ✅ | BSD License | [❌](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [❌](#project-urls) | [❌](#twine-check) |
| [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp) | ✅ | ✅ | BSD License | [❌](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [❌](#project-urls) | [❌](#twine-check) |
| **scrapy-poet and its deps** | | | | | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | [❌](#no-legacy-config) | BSD-3-Clause | [❌](#pep639-license) | ✅ | ✅ | ✅ | ✅ |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | ✅ | ✅ | Apache-2.0 | ✅ | ✅ | ✅ | [❌](#project-urls) | ✅ |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | ✅ | [❌](#no-legacy-config) | BSD-3-Clause | [❌](#pep639-license) | ✅ | ✅ | [❌](#project-urls) | ✅ |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | [❌](#no-legacy-config) | Apache-2.0 | ✅ | ✅ | ✅ | ✅ | ✅ |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | ✅ | ✅ | Apache-2.0 | ✅ | [➖](#hatchling) | [➖](#sdist-contents) | ✅ | [➖](#twine-check) |
| **Zyte API** | | | | | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | [❌](#project-urls) | ✅ |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | ✅ | BSD License | [❌](#pep639-license) | ✅ | ✅ | [❌](#project-urls) | ✅ |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | BSD License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | ✅ |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | ✅ | [❌](#no-legacy-config) | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Scrapy Cloud** | | | | | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | BSD License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [❌](#twine-check) |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | ✅ | ✅ | BSD-3-Clause | [❌](#pep639-license) | ✅ | ✅ | [❌](#project-urls) | [❌](#twine-check) |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [❌](#pyproject-metadata) | ✅ | BSD License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [❌](#twine-check) |
| [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | Apache Software License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [❌](#twine-check) |
| [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | BSD License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [❌](#twine-check) |
| [scrapinghub/frontera](https://github.com/scrapinghub/frontera) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | BSD License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [❌](#twine-check) |
| [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | BSD License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [❌](#twine-check) |
| **Data extraction** | | | | | | | | |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | ✅ | ✅ | Apache-2.0 | ✅ | ✅ | ✅ | ✅ | ✅ |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | ✅ | ✅ | Apache-2.0 | ✅ | ✅ | ✅ | ✅ | ✅ |
| [zytedata/html-text](https://github.com/zytedata/html-text) | ✅ | ✅ | MIT | ✅ | ✅ | ✅ | [❌](#project-urls) | ✅ |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | [❌](#project-urls) | [❌](#twine-check) |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | BSD-3-Clause | ✅ | [❌](#hatchling) | [➖](#sdist-contents) | [❌](#project-urls) | ✅ |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | BSD License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | ✅ |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | BSD License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [❌](#twine-check) |
| **Forms** | | | | | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | ✅ | ✅ | Apache-2.0 | [❌](#pep639-license) | ✅ | ✅ | [❌](#project-urls) | ✅ |
| [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | MIT License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | ✅ |
| [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | MIT License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | ✅ |
| [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | MIT License | [❌](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [❌](#project-urls) | [❌](#twine-check) |
| **Monitoring** | | | | | | | | |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | ✅ | ✅ | BSD-3-Clause | [❌](#pep639-license) | ✅ | ✅ | ✅ | ✅ |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | [❌](#pyproject-metadata) | ✅ | no | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [❌](#twine-check) |
| **AI agents** | | | | | | | | |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | [➖](#pyproject-metadata) | [➖](#no-legacy-config) | [➖](#license) | [➖](#pep639-license) | [➖](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [➖](#twine-check) |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | ✅ | ✅ | Apache-2.0 | ✅ | ✅ | ✅ | ✅ | ✅ |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | ✅ | ✅ | Apache-2.0 | [❌](#pep639-license) | ✅ | [❌](#sdist-contents) | [❌](#project-urls) | ✅ |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | ✅ | ✅ | Apache-2.0 | ✅ | ✅ | [❌](#sdist-contents) | [❌](#project-urls) | [❌](#twine-check) |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | ✅ | ✅ | Apache-2.0 | ✅ | ✅ | [❌](#sdist-contents) | ✅ | [❌](#twine-check) |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | ✅ | ✅ | MIT | ✅ | ✅ | [❌](#sdist-contents) | ✅ | [❌](#twine-check) |
| **Maintenance** | | | | | | | | |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | [❌](#sdist-contents) | ✅ | [❌](#twine-check) |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | [➖](#pyproject-metadata) | [➖](#no-legacy-config) | [➖](#license) | [➖](#pep639-license) | [➖](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [➖](#twine-check) |
| [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance) | ✅ | ✅ | Apache-2.0 | ✅ | ✅ | [➖](#sdist-contents) | [➖](#project-urls) | [➖](#twine-check) |

### pyproject-metadata

Package metadata is in the [project] table of pyproject.toml, with no setup.py and no setuptools configuration in setup.cfg.

- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no [project] table in pyproject.toml; setup.py exists
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no [project] table in pyproject.toml; setup.py exists
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no [project] table in pyproject.toml; setup.py exists
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no [project] table in pyproject.toml; setup.py exists
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [metadata], [bdist_wheel]
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [bdist_wheel], [sdist_dsc]
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no [project] table in pyproject.toml; setup.py exists
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no [project] table in pyproject.toml; setup.py exists
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [metadata]
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): no [project] table in pyproject.toml; setup.py exists
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): setup.py exists
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [wheel]
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [wheel]
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [bdist_wheel]
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [bdist_wheel]
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): setup.py exists
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no [project] table in pyproject.toml; setup.py exists
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### no-legacy-config

There are no legacy configuration files, e.g. .coveragerc, pytest.ini, .flake8 or requirements-dev.txt, and no tool configuration in setup.cfg or tox.ini.

- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): legacy files: pylintrc; tool sections in setup.cfg: [flake8]
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): legacy files: .coveragerc, .flake8
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): tool sections in setup.cfg: [flake8]
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): legacy files: requirements-dev.txt
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): legacy files: requirements-dev.txt
- ❌ [zytedata/url-matcher](https://github.com/zytedata/url-matcher): legacy files: requirements-dev.txt
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): legacy files: .bandit.yml, .flake8, .isort.cfg; tool sections in setup.cfg: [mypy], [mypy-pytest.*], [mypy-scrapy.*], [mypy-twisted.*], [mypy-w3lib.*]
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): legacy files: requirements-dev.txt
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): legacy files: pytest.ini
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): tool sections in setup.cfg: [flake8], [tool:pytest], [coverage:run]
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): legacy files: .flake8
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): legacy files: .coveragerc; tool sections in tox.ini: [flake8], [pytest]
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): legacy files: .flake8
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): legacy files: .coveragerc, pytest.ini
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): legacy files: .coveragerc, .isort.cfg, pytest.ini, requirements-dev.txt
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): legacy files: .coveragerc
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): legacy files: .coveragerc, .flake8; tool sections in setup.cfg: [isort]
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): legacy files: .coveragerc, .flake8
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): legacy files: .flake8
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### license

The license: the license field of package metadata, or else the license classifiers.

- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### pep639-license

The license is declared as an SPDX expression (PEP 639), without license classifiers.

- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: MIT License
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: Apache Software License
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): has license classifiers: License :: OSI Approved :: BSD License
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): has license classifiers: License :: OSI Approved :: BSD License
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): has license classifiers: License :: OSI Approved :: BSD License
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): has license classifiers: License :: OSI Approved :: Apache Software License
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: MIT License
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): has license classifiers: License :: OSI Approved :: BSD License
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): has license classifiers: License :: OSI Approved :: Apache Software License
- ➖ No [project] table in pyproject.toml. [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### hatchling

The build backend is hatchling.

- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): build backend is setuptools.build_meta
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): build backend is setuptools.build_meta
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): build backend is setuptools.build_meta
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): build backend is setuptools.build_meta
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): build backend is setuptools.build_meta
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no pyproject.toml
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no pyproject.toml
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): build backend is setuptools.build_meta
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no pyproject.toml
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): build backend is setuptools.build_meta
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): build backend is setuptools.build_meta
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no build-backend in pyproject.toml
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no build-backend in pyproject.toml
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no build-backend in pyproject.toml
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no build-backend in pyproject.toml
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no build-backend in pyproject.toml
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no pyproject.toml
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): no build-backend in pyproject.toml
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): build backend is setuptools.build_meta
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no build-backend in pyproject.toml
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no build-backend in pyproject.toml
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): build backend is setuptools.build_meta
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): no pyproject.toml
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): build backend is setuptools.build_meta
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no pyproject.toml
- ➖ Rust extension, built with maturin. [scrapy/frostwork](https://github.com/scrapy/frostwork)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### sdist-contents

The sdist includes only listed files, which include the tests, the docs and the tox configuration.

- ❌ [scrapy/queuelib](https://github.com/scrapy/queuelib): not included: tox.ini
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): no include in [tool.hatch.build.targets.sdist]
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): not included: docs, tox.ini
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no include in [tool.hatch.build.targets.sdist]
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): not included: tox.ini
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no include in [tool.hatch.build.targets.sdist]
- ➖ The build backend is not hatchling. [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### project-urls

[project.urls] links to the source, the issue tracker, the changelog and, if there are Sphinx docs, the documentation, with labels that PyPI recognizes.

- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): missing URLs: issues, changelog, documentation
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): missing URLs: issues, changelog, documentation
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): missing URLs: issues, changelog, documentation
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): missing URLs: issues, changelog
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): missing URLs: issues, changelog
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): missing URLs: documentation
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): missing URLs: changelog
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): missing URLs: issues
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): missing URLs: issues, changelog
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): missing URLs: issues, changelog
- ❌ [scrapinghub/andi](https://github.com/scrapinghub/andi): missing URLs: changelog
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): missing URLs: issues, changelog
- ❌ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): missing URLs: issues, changelog
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): missing URLs: issues, changelog
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): missing URLs: changelog
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): missing URLs: issues, changelog
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): missing URLs: changelog
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): missing URLs: issues, documentation
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): missing URLs: issues, changelog
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): missing URLs: issues, changelog, documentation
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): missing URLs: issues
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): missing URLs: changelog
- ➖ No [project] table in pyproject.toml. [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### twine-check

`twine check` validates the built distributions in tox.

- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no twine check in tox config
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): twine check runs in a workflow, not in tox
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no twine check in tox config
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no twine check in tox config
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no twine check in tox config
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no twine check in tox config
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no twine check in tox config
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): no twine check in tox config
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): twine check runs in a workflow, not in tox
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no twine check in tox config
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no twine check in tox config
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no twine check in tox config
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no twine check in tox config
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no twine check in tox config
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): no twine check in tox config
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no twine check in tox config
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no twine check in tox config
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no twine check in tox config
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no twine check in tox config
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): twine check runs in a workflow, not in tox
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): twine check runs in a workflow, not in tox
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): no twine check in tox config
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no twine check in tox config
- ➖ Wheels are built per platform by maturin in CI, where twine check runs on them. [scrapy/frostwork](https://github.com/scrapy/frostwork)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

## Dependencies

| Check | Statement | Results |
| --- | --- | --- |
| [`dependency-lower-bounds`](#dependency-lower-bounds) | Every runtime dependency has a lower bound. | 26/34 passing |
| [`min-deps-env`](#min-deps-env) | A tox environment tests the minimum versions of dependencies (its name has min, minimum, lowest or pinned in it). | 31/51 passing |

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
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |
| **Scrapy plugins** | | |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | ✅ | ✅ |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | ✅ | ✅ |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | ✅ | ✅ |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | ✅ | ✅ |
| [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |
| **Scrapy tools** | | |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | ✅ | ✅ |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | ✅ | ✅ |
| **Feed exporters** | | |
| [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc) | ✅ | [❌](#min-deps-env) |
| [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive) | [❌](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive) | [❌](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp) | ✅ | ✅ |
| **scrapy-poet and its deps** | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | ✅ |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | ✅ | ✅ |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | ✅ |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | ✅ | [❌](#min-deps-env) |
| **Zyte API** | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | ✅ |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | ✅ |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | [➖](#dependency-lower-bounds) | ✅ |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | ✅ | ✅ |
| **Scrapy Cloud** | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | [❌](#dependency-lower-bounds) | ✅ |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera) | [➖](#dependency-lower-bounds) | ✅ |
| [scrapinghub/frontera](https://github.com/scrapinghub/frontera) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend) | [➖](#dependency-lower-bounds) | ✅ |
| **Data extraction** | | |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | [❌](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | ✅ | ✅ |
| [zytedata/html-text](https://github.com/zytedata/html-text) | ✅ | ✅ |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | ✅ | [❌](#min-deps-env) |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | ✅ | ✅ |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| **Forms** | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | ✅ | ✅ |
| [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus) | [➖](#dependency-lower-bounds) | ✅ |
| [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite) | [➖](#dependency-lower-bounds) | ✅ |
| [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| **Monitoring** | | |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | ✅ | ✅ |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| **AI agents** | | |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | ✅ | ✅ |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | ✅ | ✅ |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | ✅ | [❌](#min-deps-env) |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | [❌](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | [❌](#dependency-lower-bounds) | ✅ |
| **Maintenance** | | |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | [❌](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |
| [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |

### dependency-lower-bounds

Every runtime dependency has a lower bound.

- ❌ [scrapy/scrapy](https://github.com/scrapy/scrapy): no lower bound: packaging, tldextract
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no lower bound: google-api-python-client, google-auth, scrapy
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no lower bound: requests
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no lower bound: docker, importlib-metadata, packaging, PyYAML, requests, retrying, setuptools, toml
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): no lower bound: html-text, lxml, parsel, six, w3lib
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no lower bound: google-cloud-storage, google-auth, packaging, pyyaml, jsonschema
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): no lower bound: docutils, tabulate
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no lower bound: docutils, packaging, sphinx-copybutton, sphinx-design, sphinx-sitemap, sphinxcontrib-youtube, tomli
- ➖ No runtime dependencies. [scrapy/cssselect](https://github.com/scrapy/cssselect), [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/w3lib](https://github.com/scrapy/w3lib), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite)
- ➖ No [project] table in pyproject.toml. [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### min-deps-env

A tox environment tests the minimum versions of dependencies (its name has min, minimum, lowest or pinned in it).

- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no tox environment for minimum dependency versions
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no tox environment for minimum dependency versions
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no tox environment for minimum dependency versions
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no tox environment for minimum dependency versions
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no tox environment for minimum dependency versions
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no tox environment for minimum dependency versions
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): no tox environment for minimum dependency versions
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no tox environment for minimum dependency versions
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no tox environment for minimum dependency versions
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no tox environment for minimum dependency versions
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no tox environment for minimum dependency versions
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): no tox environment for minimum dependency versions
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no tox environment for minimum dependency versions
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no tox environment for minimum dependency versions
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no tox environment for minimum dependency versions
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no tox environment for minimum dependency versions
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no tox environment for minimum dependency versions
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no tox environment for minimum dependency versions
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no tox environment for minimum dependency versions
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no tox environment for minimum dependency versions
- ➖ No dependencies. [scrapy/cssselect](https://github.com/scrapy/cssselect), [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/w3lib](https://github.com/scrapy/w3lib), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapinghub/andi](https://github.com/scrapinghub/andi)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

## Typing

| Check | Statement | Results |
| --- | --- | --- |
| [`py-typed`](#py-typed) | The package ships type hints (a py.typed marker). | 28/59 passing |
| [`typed-classifier`](#typed-classifier) | A package with a py.typed marker has the 'Typing :: Typed' classifier. | 7/28 passing |
| [`type-checker`](#type-checker) | A type checker (mypy or pyrefly) runs in tox, CI workflows or pre-commit. | 39/60 passing |
| [`mypy`](#mypy) | mypy runs in tox, CI workflows or pre-commit. | 38/59 yes |
| [`pyrefly`](#pyrefly) | pyrefly runs in tox, CI workflows or pre-commit. | 1/60 yes |
| [`mypy-strict`](#mypy-strict) | mypy runs in strict mode: strict = true in its config, or --strict. | 24/38 passing |

| Project | [py-typed](#py-typed) | [typed-classifier](#typed-classifier) | [type-checker](#type-checker) | [mypy](#mypy) | [pyrefly](#pyrefly) | [mypy-strict](#mypy-strict) |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Scrapy and its deps** | | | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | ✅ | [❌](#typed-classifier) | ✅ | yes | no | ✅ |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | ✅ | [❌](#typed-classifier) | ✅ | yes | no | ✅ |
| [scrapy/formerly](https://github.com/scrapy/formerly) | ✅ | ✅ | ✅ | yes | no | ✅ |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | ✅ | [❌](#typed-classifier) | ✅ | yes | no | ✅ |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | ✅ | ✅ | ✅ | yes | no | ✅ |
| [scrapy/parsel](https://github.com/scrapy/parsel) | ✅ | ✅ | ✅ | yes | no | ✅ |
| [scrapy/protego](https://github.com/scrapy/protego) | ✅ | ✅ | ✅ | yes | no | ✅ |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | ✅ | [❌](#typed-classifier) | ✅ | yes | no | ✅ |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | ✅ | [❌](#typed-classifier) | ✅ | yes | no | ✅ |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | yes | no | [❌](#mypy-strict) |
| **Scrapy plugins** | | | | | | |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | ✅ | ✅ | ✅ | yes | no | ✅ |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | yes | no | [❌](#mypy-strict) |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | ✅ | ✅ | ✅ | yes | no | ✅ |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | ✅ | [❌](#typed-classifier) | ✅ | yes | no | [❌](#mypy-strict) |
| [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules) | ✅ | [❌](#typed-classifier) | ✅ | yes | no | ✅ |
| **Scrapy tools** | | | | | | |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | yes | no | [❌](#mypy-strict) |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | yes | no | [❌](#mypy-strict) |
| **Feed exporters** | | | | | | |
| [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#type-checker) | no | no | [➖](#mypy-strict) |
| [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | yes | no | [❌](#mypy-strict) |
| [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#type-checker) | no | no | [➖](#mypy-strict) |
| [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#type-checker) | no | no | [➖](#mypy-strict) |
| [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#type-checker) | no | no | [➖](#mypy-strict) |
| [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#type-checker) | no | no | [➖](#mypy-strict) |
| [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#type-checker) | no | no | [➖](#mypy-strict) |
| **scrapy-poet and its deps** | | | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | [❌](#typed-classifier) | ✅ | yes | no | ✅ |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | ✅ | [❌](#typed-classifier) | ✅ | yes | no | ✅ |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | ✅ | [❌](#typed-classifier) | ✅ | yes | no | [❌](#mypy-strict) |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | ✅ | ✅ | yes | no | ✅ |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | ✅ | [❌](#typed-classifier) | [❌](#type-checker) | [➖](#mypy) | no | [➖](#mypy-strict) |
| **Zyte API** | | | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | [❌](#typed-classifier) | ✅ | yes | no | [❌](#mypy-strict) |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | [❌](#typed-classifier) | ✅ | yes | no | [❌](#mypy-strict) |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | yes | no | [❌](#mypy-strict) |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | ✅ | [❌](#typed-classifier) | ✅ | yes | no | [❌](#mypy-strict) |
| **Scrapy Cloud** | | | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#type-checker) | no | no | [➖](#mypy-strict) |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#type-checker) | no | no | [➖](#mypy-strict) |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#type-checker) | no | no | [➖](#mypy-strict) |
| [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow) | ✅ | [❌](#typed-classifier) | [❌](#type-checker) | no | no | [➖](#mypy-strict) |
| [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#type-checker) | no | no | [➖](#mypy-strict) |
| [scrapinghub/frontera](https://github.com/scrapinghub/frontera) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#type-checker) | no | no | [➖](#mypy-strict) |
| [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#type-checker) | no | no | [➖](#mypy-strict) |
| **Data extraction** | | | | | | |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | ✅ | [❌](#typed-classifier) | ✅ | yes | no | ✅ |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | ✅ | [❌](#typed-classifier) | ✅ | yes | no | ✅ |
| [zytedata/html-text](https://github.com/zytedata/html-text) | ✅ | [❌](#typed-classifier) | ✅ | yes | no | ✅ |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | ✅ | [❌](#typed-classifier) | ✅ | yes | no | ✅ |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | yes | no | ✅ |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | yes | no | [❌](#mypy-strict) |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | yes | no | [❌](#mypy-strict) |
| **Forms** | | | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | ✅ | [❌](#typed-classifier) | ✅ | yes | no | ✅ |
| [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#type-checker) | no | no | [➖](#mypy-strict) |
| [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#type-checker) | no | no | [➖](#mypy-strict) |
| [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#type-checker) | no | no | [➖](#mypy-strict) |
| **Monitoring** | | | | | | |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | yes | no | [❌](#mypy-strict) |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#type-checker) | no | no | [➖](#mypy-strict) |
| **AI agents** | | | | | | |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | [➖](#py-typed) | [➖](#typed-classifier) | [➖](#type-checker) | [➖](#mypy) | [➖](#pyrefly) | [➖](#mypy-strict) |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | ✅ | [❌](#typed-classifier) | ✅ | yes | no | ✅ |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#type-checker) | no | no | [➖](#mypy-strict) |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#type-checker) | no | no | [➖](#mypy-strict) |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#type-checker) | no | no | [➖](#mypy-strict) |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | yes | no | ✅ |
| **Maintenance** | | | | | | |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | yes | no | ✅ |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | [➖](#py-typed) | [➖](#typed-classifier) | [➖](#type-checker) | [➖](#mypy) | [➖](#pyrefly) | [➖](#mypy-strict) |
| [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance) | [➖](#py-typed) | [➖](#typed-classifier) | ✅ | no | yes | [➖](#mypy-strict) |

### py-typed

The package ships type hints (a py.typed marker).

- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no py.typed file
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no py.typed file
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): no py.typed file
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no py.typed file
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no py.typed file
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no py.typed file
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no py.typed file
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no py.typed file
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no py.typed file
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no py.typed file
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): no py.typed file
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no py.typed file
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no py.typed file
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no py.typed file
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no py.typed file
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no py.typed file
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no py.typed file
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): no py.typed file
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): no py.typed file
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no py.typed file
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no py.typed file
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): no py.typed file
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): no py.typed file
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no py.typed file
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): no py.typed file
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no py.typed file
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): no py.typed file
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no py.typed file
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no py.typed file
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): no py.typed file
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no py.typed file
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### typed-classifier

A package with a py.typed marker has the 'Typing :: Typed' classifier.

- ❌ [scrapy/scrapy](https://github.com/scrapy/scrapy): no 'Typing :: Typed' classifier
- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): no 'Typing :: Typed' classifier
- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): no 'Typing :: Typed' classifier
- ❌ [scrapy/queuelib](https://github.com/scrapy/queuelib): no 'Typing :: Typed' classifier
- ❌ [scrapy/w3lib](https://github.com/scrapy/w3lib): no 'Typing :: Typed' classifier
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no 'Typing :: Typed' classifier
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): no 'Typing :: Typed' classifier
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): no 'Typing :: Typed' classifier
- ❌ [scrapinghub/andi](https://github.com/scrapinghub/andi): no 'Typing :: Typed' classifier
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): no 'Typing :: Typed' classifier
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): no 'Typing :: Typed' classifier
- ❌ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): no 'Typing :: Typed' classifier
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): no 'Typing :: Typed' classifier
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): no 'Typing :: Typed' classifier
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no 'Typing :: Typed' classifier
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): no 'Typing :: Typed' classifier
- ❌ [zytedata/clear-html](https://github.com/zytedata/clear-html): no 'Typing :: Typed' classifier
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): no 'Typing :: Typed' classifier
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no 'Typing :: Typed' classifier
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): no 'Typing :: Typed' classifier
- ❌ [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official): no 'Typing :: Typed' classifier
- ➖ No py.typed file. [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint), [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [zytedata/agent-exam](https://github.com/zytedata/agent-exam), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### type-checker

A type checker (mypy or pyrefly) runs in tox, CI workflows or pre-commit.

- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no type checker found
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no type checker found
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no type checker found
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no type checker found
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no type checker found
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): no type checker found
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): no type checker found
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no type checker found
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no type checker found
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no type checker found
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no type checker found
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no type checker found
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no type checker found
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): no type checker found
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): no type checker found
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): no type checker found
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no type checker found
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no type checker found
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): no type checker found
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no type checker found
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no type checker found
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### mypy

mypy runs in tox, CI workflows or pre-commit.

- ➖ Runs mypy through make py, in CI. [scrapy/frostwork](https://github.com/scrapy/frostwork)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### pyrefly

pyrefly runs in tox, CI workflows or pre-commit.

- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### mypy-strict

mypy runs in strict mode: strict = true in its config, or --strict.

- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no strict = true in mypy config, and no --strict
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no strict = true in mypy config, and no --strict
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no strict = true in mypy config, and no --strict
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): no strict = true in mypy config, and no --strict
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no strict = true in mypy config, and no --strict
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no strict = true in mypy config, and no --strict
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): no strict = true in mypy config, and no --strict
- ❌ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): no strict = true in mypy config, and no --strict
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): no strict = true in mypy config, and no --strict
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no strict = true in mypy config, and no --strict
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): no strict = true in mypy config, and no --strict
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no strict = true in mypy config, and no --strict
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no strict = true in mypy config, and no --strict
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): no strict = true in mypy config, and no --strict
- ➖ Does not run mypy. [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [zytedata/agent-exam](https://github.com/zytedata/agent-exam), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

## Tests and coverage

| Check | Statement | Results |
| --- | --- | --- |
| [`codecov`](#codecov) | Test coverage is uploaded to Codecov in CI workflows. | 45/60 passing |
| [`codecov-test-results`](#codecov-test-results) | Test results are uploaded to Codecov in CI workflows (codecov/codecov-action with report_type: test_results). | 16/60 passing |
| [`codecov-auth`](#codecov-auth) | Codecov uploads use OIDC (use_oidc: true, with id-token: write permission) in scrapinghub, where tokenless uploads are not allowed, and are tokenless elsewhere. | 17/42 passing |
| [`codecov-status`](#codecov-status) | The Codecov config disables the patch status and sets a 100% target for the project status. | 8/45 passing |
| [`branch-coverage`](#branch-coverage) | Branch coverage is enabled. | 32/60 passing |
| [`warnings-as-errors`](#warnings-as-errors) | pytest turns warnings into errors: "error" in filterwarnings, or -W error. | 9/60 passing |
| [`scrapy-master`](#scrapy-master) | CI tests against Scrapy installed from its master branch. | 2/21 passing |

| Project | [codecov](#codecov) | [codecov-test-results](#codecov-test-results) | [codecov-auth](#codecov-auth) | [codecov-status](#codecov-status) | [branch-coverage](#branch-coverage) | [warnings-as-errors](#warnings-as-errors) | [scrapy-master](#scrapy-master) |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Scrapy and its deps** | | | | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [➖](#scrapy-master) |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | ✅ | [❌](#codecov-test-results) | ✅ | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapy/formerly](https://github.com/scrapy/formerly) | ✅ | ✅ | ✅ | [❌](#codecov-status) | ✅ | ✅ | [➖](#scrapy-master) |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | ✅ | [❌](#codecov-test-results) | ✅ | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | ✅ | [❌](#codecov-test-results) | ✅ | ✅ | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapy/parsel](https://github.com/scrapy/parsel) | ✅ | ✅ | ✅ | ✅ | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapy/protego](https://github.com/scrapy/protego) | ✅ | ✅ | ✅ | ✅ | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | ✅ | ✅ | ✅ | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | ✅ | [❌](#codecov-test-results) | ✅ | ✅ | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | ✅ | [❌](#codecov-test-results) | ✅ | [❌](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| **Scrapy plugins** | | | | | | | |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | ✅ | ✅ | ✅ | [❌](#codecov-status) | ✅ | ✅ | [❌](#scrapy-master) |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-auth) | [❌](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | ✅ | ✅ | [❌](#codecov-auth) | ✅ | ✅ | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-auth) | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-auth) | [❌](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| **Scrapy tools** | | | | | | | |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | ✅ | ✅ | ✅ | [❌](#codecov-status) | [❌](#branch-coverage) | ✅ | [➖](#scrapy-master) |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-auth) | [➖](#codecov-status) | [❌](#branch-coverage) | ✅ | [❌](#scrapy-master) |
| **Feed exporters** | | | | | | | |
| [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-auth) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-auth) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-auth) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-auth) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-auth) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-auth) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp) | ✅ | [❌](#codecov-test-results) | ✅ | [❌](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| **scrapy-poet and its deps** | | | | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-auth) | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | ✅ |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | ✅ | ✅ | ✅ | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-auth) | [❌](#codecov-status) | [❌](#branch-coverage) | ✅ | [➖](#scrapy-master) |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | ✅ | [❌](#codecov-auth) | ✅ | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-auth) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| **Zyte API** | | | | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-auth) | ✅ | ✅ | ✅ | ✅ |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-auth) | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-auth) | [❌](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | ✅ | ✅ | [❌](#codecov-auth) | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| **Scrapy Cloud** | | | | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-auth) | [❌](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-auth) | [❌](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-auth) | [❌](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-auth) | [➖](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-auth) | [❌](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [scrapinghub/frontera](https://github.com/scrapinghub/frontera) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-auth) | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-auth) | [❌](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| **Data extraction** | | | | | | | |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | ✅ | ✅ | [❌](#codecov-auth) | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | ✅ | ✅ | [❌](#codecov-auth) | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [zytedata/html-text](https://github.com/zytedata/html-text) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-auth) | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-auth) | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-auth) | [❌](#codecov-status) | [❌](#branch-coverage) | ✅ | [➖](#scrapy-master) |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-auth) | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-auth) | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| **Forms** | | | | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | ✅ | ✅ | ✅ | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus) | ✅ | [❌](#codecov-test-results) | [➖](#codecov-auth) | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite) | ✅ | [❌](#codecov-test-results) | [➖](#codecov-auth) | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-auth) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| **Monitoring** | | | | | | | |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-auth) | [❌](#codecov-status) | ✅ | ✅ | [❌](#scrapy-master) |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | ✅ | [❌](#codecov-test-results) | [➖](#codecov-auth) | [❌](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| **AI agents** | | | | | | | |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | [➖](#codecov) | [➖](#codecov-test-results) | [➖](#codecov-auth) | [➖](#codecov-status) | [➖](#branch-coverage) | [➖](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | ✅ | ✅ | ✅ | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | ✅ | ✅ | ✅ | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-auth) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-auth) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-auth) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| **Maintenance** | | | | | | | |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-auth) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | [➖](#codecov) | [➖](#codecov-test-results) | [➖](#codecov-auth) | [➖](#codecov-status) | [➖](#branch-coverage) | [➖](#warnings-as-errors) | [➖](#scrapy-master) |
| [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-auth) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |

### codecov

Test coverage is uploaded to Codecov in CI workflows.

- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no codecov/codecov-action step for coverage
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no codecov/codecov-action step for coverage
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no codecov/codecov-action step for coverage
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no codecov/codecov-action step for coverage
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no codecov/codecov-action step for coverage
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no codecov/codecov-action step for coverage
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no codecov/codecov-action step for coverage
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): no codecov/codecov-action step for coverage
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no codecov/codecov-action step for coverage
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no codecov/codecov-action step for coverage
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no codecov/codecov-action step for coverage
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no codecov/codecov-action step for coverage
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): no codecov/codecov-action step for coverage
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no codecov/codecov-action step for coverage
- ❌ [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance): no codecov/codecov-action step for coverage
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### codecov-test-results

Test results are uploaded to Codecov in CI workflows (codecov/codecov-action with report_type: test_results).

- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy/w3lib](https://github.com/scrapy/w3lib): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no codecov/codecov-action step with report_type: test_results
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no codecov/codecov-action step with report_type: test_results
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): no codecov/codecov-action step with report_type: test_results
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): no codecov/codecov-action step with report_type: test_results
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no codecov/codecov-action step with report_type: test_results
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no codecov/codecov-action step with report_type: test_results
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no codecov/codecov-action step with report_type: test_results
- ❌ [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance): no codecov/codecov-action step with report_type: test_results
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### codecov-auth

Codecov uploads use OIDC (use_oidc: true, with id-token: write permission) in scrapinghub, where tokenless uploads are not allowed, and are tokenless elsewhere.

- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): expected tokenless, found token in .github/workflows/tests.yml
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): expected tokenless, found token in .github/workflows/test.yml
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): expected tokenless, found token in .github/workflows/test.yml
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): expected tokenless, found token in .github/workflows/test.yml
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): expected OIDC, found token in .github/workflows/scrapy-unreleased.yml, .github/workflows/test.yml
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): expected OIDC, found token in .github/workflows/tests-ubuntu.yml, .github/workflows/tests-windows.yml
- ❌ [zytedata/url-matcher](https://github.com/zytedata/url-matcher): expected tokenless, found token in .github/workflows/test.yml
- ❌ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): expected tokenless, found token in .github/workflows/test.yml
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): expected tokenless, found token in .github/workflows/test.yml
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): expected tokenless, found token in .github/workflows/main.yml
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): expected tokenless, found token in .github/workflows/test.yml
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): expected OIDC, found token in .github/workflows/main.yml
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): expected OIDC, found token in .github/workflows/tests.yml
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): expected OIDC, found token in .github/workflows/tests.yml
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): expected OIDC, found token in .github/workflows/tests.yml
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): expected OIDC, found token in .github/workflows/test.yml
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): expected OIDC, found token in .github/workflows/test.yml
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): expected tokenless, found token in .github/workflows/test.yml
- ❌ [zytedata/clear-html](https://github.com/zytedata/clear-html): expected tokenless, found token in .github/workflows/test.yml
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): expected tokenless, found token in .github/workflows/test.yml
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): expected OIDC, found token in .github/workflows/main.yml
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): expected OIDC, found token in .github/workflows/main.yml
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): expected OIDC, found token in .github/workflows/python-package.yml
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): expected OIDC, found tokenless in .github/workflows/main.yml
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): expected OIDC, found token in .github/workflows/main.yml
- ➖ Nothing is uploaded to Codecov. [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### codecov-status

The Codecov config disables the patch status and sets a 100% target for the project status.

- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): no Codecov config
- ❌ [scrapy/formerly](https://github.com/scrapy/formerly): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): no Codecov config
- ❌ [scrapy/queuelib](https://github.com/scrapy/queuelib): no Codecov config
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no Codecov config
- ❌ [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator): no Codecov config
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no Codecov config
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no Codecov config
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): no Codecov config
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): no Codecov config
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): no Codecov config
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): patch status not disabled, project status target not 100% in .codecov.yml
- ❌ [scrapinghub/andi](https://github.com/scrapinghub/andi): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): patch status not disabled, project status target not 100% in .codecov.yml
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no Codecov config
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): patch status not disabled, project status target not 100% in .codecov.yml
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no Codecov config
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no Codecov config
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no Codecov config
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no Codecov config
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): no Codecov config
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): no Codecov config
- ❌ [zytedata/clear-html](https://github.com/zytedata/clear-html): no Codecov config
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): no Codecov config
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no Codecov config
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): no Codecov config
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): no Codecov config
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): no Codecov config
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): no Codecov config
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no Codecov config
- ❌ [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official): no Codecov config
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): patch status not disabled, project status target not 100% in codecov.yml
- ➖ Coverage is not uploaded to Codecov. [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### branch-coverage

Branch coverage is enabled.

- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no branch = true in coverage config, and no --cov-branch
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no branch = true in coverage config, and no --cov-branch
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no branch = true in coverage config, and no --cov-branch
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no branch = true in coverage config, and no --cov-branch
- ❌ [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance): no branch = true in coverage config, and no --cov-branch
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### warnings-as-errors

pytest turns warnings into errors: "error" in filterwarnings, or -W error.

- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/parsel](https://github.com/scrapy/parsel): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/protego](https://github.com/scrapy/protego): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/queuelib](https://github.com/scrapy/queuelib): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/w3lib](https://github.com/scrapy/w3lib): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/andi](https://github.com/scrapinghub/andi): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/url-matcher](https://github.com/zytedata/url-matcher): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/clear-html](https://github.com/zytedata/clear-html): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance): no "error" in pytest filterwarnings, and no -W error
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### scrapy-master

CI tests against Scrapy installed from its master branch.

- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): no CI workflow or tox environment installs Scrapy master
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): no CI workflow or tox environment installs Scrapy master
- ➖ Does not depend on Scrapy. [scrapy/scrapy](https://github.com/scrapy/scrapy), [scrapy/cssselect](https://github.com/scrapy/cssselect), [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemloaders](https://github.com/scrapy/itemloaders), [scrapy/parsel](https://github.com/scrapy/parsel), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/w3lib](https://github.com/scrapy/w3lib), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet), [zytedata/url-matcher](https://github.com/zytedata/url-matcher), [scrapy/frostwork](https://github.com/scrapy/frostwork), [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api), [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapy/form2request](https://github.com/scrapy/form2request), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [zytedata/agent-exam](https://github.com/zytedata/agent-exam), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

## Linting

| Check | Statement | Results |
| --- | --- | --- |
| [`ruff`](#ruff) | ruff-check and ruff-format are used, instead of tools that ruff replaces. | 42/60 passing |
| [`ruff-rules`](#ruff-rules) | ruff enables rules beyond its defaults, with select or extend-select. | 39/43 passing |
| [`pylint`](#pylint) | A tox environment runs pylint. | 10/60 yes |
| [`pre-commit-in-ci`](#pre-commit-in-ci) | pre-commit runs in CI workflows, directly or through tox, or in pre-commit.ci. | 47/52 passing |
| [`pre-commit-tox`](#pre-commit-tox) | A tox environment runs pre-commit on all files. | 39/52 passing |
| [`pre-commit-hooks`](#pre-commit-hooks) | The hooks of https://github.com/pre-commit/pre-commit-hooks are used. | 36/52 passing |
| [`pre-commit-updates`](#pre-commit-updates) | The ruff and zizmor pre-commit hooks are updated within 180 days of a new release. | 36/45 passing |
| [`actionlint`](#actionlint) | GitHub Actions workflows are linted with actionlint. | 28/58 passing |
| [`zizmor`](#zizmor) | GitHub Actions workflows are audited with zizmor. | 34/58 passing |
| [`dependabot`](#dependabot) | Dependabot updates GitHub Actions, which zizmor requires pinning. | 32/34 passing |
| [`workflow-concurrency`](#workflow-concurrency) | Workflows triggered by pull requests or branch pushes cancel superseded runs (a top-level concurrency with cancel-in-progress), unless they set cancel-in-progress: false. | 9/57 passing |
| [`pr-guard-trusted-users`](#pr-guard-trusted-users) | The trusted-users of scrapy/unattended-pr-guard include no public members of its trusted-orgs, which it trusts already. | 3/6 passing |
| [`has-sphinx-docs`](#has-sphinx-docs) | The project has Sphinx docs (docs/conf.py). | 26/62 yes |
| [`blacken-docs`](#blacken-docs) | Code examples in the docs are formatted with blacken-docs. | 18/26 passing |
| [`sphinx-lint`](#sphinx-lint) | The docs are linted with sphinx-lint. | 19/26 passing |

| Project | [ruff](#ruff) | [ruff-rules](#ruff-rules) | [pylint](#pylint) | [pre-commit-in-ci](#pre-commit-in-ci) | [pre-commit-tox](#pre-commit-tox) | [pre-commit-hooks](#pre-commit-hooks) | [pre-commit-updates](#pre-commit-updates) | [actionlint](#actionlint) | [zizmor](#zizmor) | [dependabot](#dependabot) | [workflow-concurrency](#workflow-concurrency) | [pr-guard-trusted-users](#pr-guard-trusted-users) | [has-sphinx-docs](#has-sphinx-docs) | [blacken-docs](#blacken-docs) | [sphinx-lint](#sphinx-lint) |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Scrapy and its deps** | | | | | | | | | | | | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | ✅ | ✅ | yes | ✅ | ✅ | ✅ | ✅ | [❌](#actionlint) | ✅ | ✅ | ✅ | [❌](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | ✅ | ✅ | yes | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [scrapy/formerly](https://github.com/scrapy/formerly) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | ✅ | ✅ | yes | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | ✅ | ✅ | yes | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [❌](#workflow-concurrency) | ✅ | yes | ✅ | ✅ |
| [scrapy/parsel](https://github.com/scrapy/parsel) | ✅ | ✅ | yes | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [❌](#workflow-concurrency) | ✅ | yes | ✅ | ✅ |
| [scrapy/protego](https://github.com/scrapy/protego) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | ✅ | ✅ | yes | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | ✅ | ✅ | yes | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [❌](#workflow-concurrency) | [❌](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | ✅ | [❌](#ruff-rules) | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [❌](#dependabot) | ✅ | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| **Scrapy plugins** | | | | | | | | | | | | | | | |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | [❌](#ruff) | [➖](#ruff-rules) | yes | [❌](#pre-commit-in-ci) | [❌](#pre-commit-tox) | [❌](#pre-commit-hooks) | ✅ | [❌](#actionlint) | ✅ | ✅ | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | yes | [❌](#blacken-docs) | ✅ |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | [❌](#ruff) | [➖](#ruff-rules) | no | ✅ | ✅ | [❌](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules) | [❌](#ruff) | [➖](#ruff-rules) | no | ✅ | ✅ | [❌](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| **Scrapy tools** | | | | | | | | | | | | | | | |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | ✅ | ✅ | yes | ✅ | ✅ | ✅ | ✅ | [❌](#actionlint) | ✅ | ✅ | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | ✅ | ✅ | yes | ✅ | ✅ | ✅ | [❌](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| **Feed exporters** | | | | | | | | | | | | | | | |
| [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc) | ✅ | ✅ | no | ✅ | [❌](#pre-commit-tox) | ✅ | [❌](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage) | [❌](#ruff) | [➖](#ruff-rules) | no | [➖](#pre-commit-in-ci) | [➖](#pre-commit-tox) | [➖](#pre-commit-hooks) | [➖](#pre-commit-updates) | [➖](#actionlint) | [➖](#zizmor) | [➖](#dependabot) | [➖](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox) | [❌](#ruff) | [➖](#ruff-rules) | no | [➖](#pre-commit-in-ci) | [➖](#pre-commit-tox) | [➖](#pre-commit-hooks) | [➖](#pre-commit-updates) | [➖](#actionlint) | [➖](#zizmor) | [➖](#dependabot) | [➖](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive) | ✅ | ✅ | no | ✅ | ✅ | [❌](#pre-commit-hooks) | ✅ | [❌](#actionlint) | ✅ | ✅ | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets) | [❌](#ruff) | [➖](#ruff-rules) | no | [➖](#pre-commit-in-ci) | [➖](#pre-commit-tox) | [➖](#pre-commit-hooks) | [➖](#pre-commit-updates) | [➖](#actionlint) | [➖](#zizmor) | [➖](#dependabot) | [➖](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive) | ✅ | ✅ | no | [❌](#pre-commit-in-ci) | [❌](#pre-commit-tox) | [❌](#pre-commit-hooks) | ✅ | [❌](#actionlint) | ✅ | ✅ | [➖](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp) | ✅ | ✅ | no | ✅ | ✅ | [❌](#pre-commit-hooks) | [❌](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| **scrapy-poet and its deps** | | | | | | | | | | | | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | ✅ | no | ✅ | ✅ | ✅ | [❌](#pre-commit-updates) | ✅ | [❌](#zizmor) | [➖](#dependabot) | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | [❌](#actionlint) | ✅ | ✅ | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | [❌](#ruff) | [➖](#ruff-rules) | no | [❌](#pre-commit-in-ci) | [❌](#pre-commit-tox) | [❌](#pre-commit-hooks) | ✅ | ✅ | ✅ | ✅ | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| **Zyte API** | | | | | | | | | | | | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | ✅ | no | [❌](#pre-commit-in-ci) | ✅ | ✅ | ✅ | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | [❌](#ruff) | [➖](#ruff-rules) | no | ✅ | ✅ | [❌](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | yes | [❌](#blacken-docs) | [❌](#sphinx-lint) |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| **Scrapy Cloud** | | | | | | | | | | | | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | [❌](#ruff) | [➖](#ruff-rules) | no | [❌](#pre-commit-in-ci) | [❌](#pre-commit-tox) | [❌](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | yes | [❌](#blacken-docs) | [❌](#sphinx-lint) |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | ✅ | ✅ | no | ✅ | ✅ | [❌](#pre-commit-hooks) | ✅ | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | yes | [❌](#blacken-docs) | [❌](#sphinx-lint) |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [❌](#ruff) | [➖](#ruff-rules) | no | [➖](#pre-commit-in-ci) | [➖](#pre-commit-tox) | [➖](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow) | [❌](#ruff) | [➖](#ruff-rules) | no | [➖](#pre-commit-in-ci) | [➖](#pre-commit-tox) | [➖](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera) | ✅ | ✅ | no | ✅ | [❌](#pre-commit-tox) | [❌](#pre-commit-hooks) | [❌](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapinghub/frontera](https://github.com/scrapinghub/frontera) | [❌](#ruff) | [➖](#ruff-rules) | no | [➖](#pre-commit-in-ci) | [➖](#pre-commit-tox) | [➖](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend) | ✅ | [❌](#ruff-rules) | no | ✅ | [❌](#pre-commit-tox) | ✅ | [❌](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| **Data extraction** | | | | | | | | | | | | | | | |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [zytedata/html-text](https://github.com/zytedata/html-text) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | ✅ | ✅ | no | ✅ | ✅ | ✅ | [❌](#pre-commit-updates) | [❌](#actionlint) | ✅ | ✅ | [❌](#workflow-concurrency) | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | ✅ | ✅ | no | ✅ | ✅ | [❌](#pre-commit-hooks) | ✅ | [❌](#actionlint) | ✅ | ✅ | [❌](#workflow-concurrency) | [❌](#pr-guard-trusted-users) | yes | [❌](#blacken-docs) | [❌](#sphinx-lint) |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [❌](#ruff) | [➖](#ruff-rules) | no | ✅ | ✅ | [❌](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | ✅ | ✅ | no | ✅ | [❌](#pre-commit-tox) | [❌](#pre-commit-hooks) | ✅ | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| **Forms** | | | | | | | | | | | | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus) | [❌](#ruff) | [➖](#ruff-rules) | no | ✅ | ✅ | [❌](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | yes | [❌](#blacken-docs) | [❌](#sphinx-lint) |
| [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite) | [❌](#ruff) | [➖](#ruff-rules) | no | ✅ | ✅ | [❌](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | yes | [❌](#blacken-docs) | [❌](#sphinx-lint) |
| [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite) | [❌](#ruff) | [➖](#ruff-rules) | no | [➖](#pre-commit-in-ci) | [➖](#pre-commit-tox) | [➖](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | yes | [❌](#blacken-docs) | [❌](#sphinx-lint) |
| **Monitoring** | | | | | | | | | | | | | | | |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | ✅ | ✅ | no | ✅ | [❌](#pre-commit-tox) | ✅ | ✅ | ✅ | [❌](#zizmor) | [➖](#dependabot) | ✅ | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | [❌](#ruff) | [➖](#ruff-rules) | no | [➖](#pre-commit-in-ci) | [➖](#pre-commit-tox) | [➖](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| **AI agents** | | | | | | | | | | | | | | | |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | [➖](#ruff) | [➖](#ruff-rules) | [➖](#pylint) | [➖](#pre-commit-in-ci) | [➖](#pre-commit-tox) | [➖](#pre-commit-hooks) | [➖](#pre-commit-updates) | [➖](#actionlint) | [➖](#zizmor) | [➖](#dependabot) | [➖](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [❌](#dependabot) | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | ✅ | [❌](#ruff-rules) | no | ✅ | [❌](#pre-commit-tox) | ✅ | ✅ | ✅ | ✅ | ✅ | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | [❌](#ruff) | [❌](#ruff-rules) | no | [➖](#pre-commit-in-ci) | [➖](#pre-commit-tox) | [➖](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | ✅ | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | ✅ | ✅ | no | ✅ | [❌](#pre-commit-tox) | ✅ | [❌](#pre-commit-updates) | ✅ | ✅ | ✅ | ✅ | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| **Maintenance** | | | | | | | | | | | | | | | |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | ✅ | ✅ | no | ✅ | [❌](#pre-commit-tox) | ✅ | [❌](#pre-commit-updates) | ✅ | ✅ | ✅ | ✅ | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | [➖](#ruff) | [➖](#ruff-rules) | [➖](#pylint) | ✅ | [❌](#pre-commit-tox) | ✅ | ✅ | ✅ | ✅ | ✅ | [❌](#workflow-concurrency) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |

### ruff

ruff-check and ruff-format are used, instead of tools that ruff replaces.

- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): missing pre-commit hooks: ruff-check, ruff-format
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no .pre-commit-config.yaml
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no .pre-commit-config.yaml
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no .pre-commit-config.yaml
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): missing pre-commit hooks: ruff-check, ruff-format
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): missing pre-commit hooks: ruff-check, ruff-format
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no .pre-commit-config.yaml
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no .pre-commit-config.yaml
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no .pre-commit-config.yaml
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, isort, pyupgrade
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort, pyupgrade
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort, pyupgrade
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no .pre-commit-config.yaml
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no .pre-commit-config.yaml
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no .pre-commit-config.yaml
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### ruff-rules

ruff enables rules beyond its defaults, with select or extend-select.

- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): only the default rules are enabled
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): only the default rules are enabled
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): only the default rules are enabled
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): only the default rules are enabled
- ➖ Does not use ruff. [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### pylint

A tox environment runs pylint.

- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### pre-commit-in-ci

pre-commit runs in CI workflows, directly or through tox, or in pre-commit.ci.

- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): not run in CI workflows or tox
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): not run in CI workflows or tox
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): not run in CI workflows or tox
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): tox environments that run pre-commit are not run in CI: pre-commit
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): not run in CI workflows or tox
- ➖ No .pre-commit-config.yaml. [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [zytedata/harness-run](https://github.com/zytedata/harness-run)

### pre-commit-tox

A tox environment runs pre-commit on all files.

- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no tox environment runs pre-commit run --all-files
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no tox environment runs pre-commit run --all-files
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no tox environment runs pre-commit run --all-files
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): no tox environment runs pre-commit run --all-files
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no tox environment runs pre-commit run --all-files
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no tox environment runs pre-commit run --all-files
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): no tox environment runs pre-commit run --all-files
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no tox environment runs pre-commit run --all-files
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): no tox environment runs pre-commit run --all-files
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no tox environment runs pre-commit run --all-files
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): no tox environment runs pre-commit run --all-files
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no tox environment runs pre-commit run --all-files
- ❌ [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard): no tox environment runs pre-commit run --all-files
- ➖ No .pre-commit-config.yaml. [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [zytedata/harness-run](https://github.com/zytedata/harness-run)

### pre-commit-hooks

The hooks of https://github.com/pre-commit/pre-commit-hooks are used.

- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): https://github.com/pre-commit/pre-commit-hooks is not used
- ➖ No .pre-commit-config.yaml. [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [zytedata/harness-run](https://github.com/zytedata/harness-run)

### pre-commit-updates

The ruff and zizmor pre-commit hooks are updated within 180 days of a new release.

- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): outdated: ruff v0.12.5 (0.15.12 or later expected)
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): outdated: ruff v0.8.4 (0.15.12 or later expected)
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): outdated: ruff v0.9.3 (0.15.12 or later expected)
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): outdated: ruff v0.15.6 (0.15.12 or later expected)
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): outdated: ruff v0.9.4 (0.15.12 or later expected)
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): outdated: ruff v0.11.12 (0.15.12 or later expected)
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): outdated: ruff v0.13.2 (0.15.12 or later expected)
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): outdated: ruff v0.11.13 (0.15.12 or later expected)
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): outdated: ruff v0.11.13 (0.15.12 or later expected)
- ➖ No checked hooks. [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite)
- ➖ No .pre-commit-config.yaml. [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [zytedata/harness-run](https://github.com/zytedata/harness-run)

### actionlint

GitHub Actions workflows are linted with actionlint.

- ❌ [scrapy/scrapy](https://github.com/scrapy/scrapy): missing pre-commit hooks: actionlint
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): missing pre-commit hooks: actionlint
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): missing pre-commit hooks: actionlint
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): missing pre-commit hooks: actionlint
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): missing pre-commit hooks: actionlint
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): missing pre-commit hooks: actionlint
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): missing pre-commit hooks: actionlint
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): missing pre-commit hooks: actionlint
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): missing pre-commit hooks: actionlint
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): missing pre-commit hooks: actionlint
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no .pre-commit-config.yaml
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no .pre-commit-config.yaml
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no .pre-commit-config.yaml
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): missing pre-commit hooks: actionlint
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no .pre-commit-config.yaml
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no .pre-commit-config.yaml
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no .pre-commit-config.yaml
- ➖ No GitHub Actions workflows. [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)

### zizmor

GitHub Actions workflows are audited with zizmor.

- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): missing pre-commit hooks: zizmor
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): missing pre-commit hooks: zizmor
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): missing pre-commit hooks: zizmor
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): missing pre-commit hooks: zizmor
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): missing pre-commit hooks: zizmor
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no .pre-commit-config.yaml
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no .pre-commit-config.yaml
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no .pre-commit-config.yaml
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): missing pre-commit hooks: zizmor
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no .pre-commit-config.yaml
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): missing pre-commit hooks: zizmor
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no .pre-commit-config.yaml
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no .pre-commit-config.yaml
- ➖ No GitHub Actions workflows. [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)

### dependabot

Dependabot updates GitHub Actions, which zizmor requires pinning.

- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no .github/dependabot.yml
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): no .github/dependabot.yml
- ➖ Does not use zizmor. [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet), [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [zytedata/harness-run](https://github.com/zytedata/harness-run)
- ➖ No GitHub Actions workflows. [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)

### workflow-concurrency

Workflows triggered by pull requests or branch pushes cancel superseded runs (a top-level concurrency with cancel-in-progress), unless they set cancel-in-progress: false.

- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/tests-macos.yml, .github/workflows/tests-ubuntu.yml, .github/workflows/tests-windows.yml
- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/tests.yml
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): no cancel-in-progress: .github/workflows/tests-macos.yml, .github/workflows/tests-ubuntu.yml, .github/workflows/tests-windows.yml
- ❌ [scrapy/parsel](https://github.com/scrapy/parsel): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/tests-macos.yml, .github/workflows/tests-ubuntu.yml, .github/workflows/tests-windows.yml
- ❌ [scrapy/protego](https://github.com/scrapy/protego): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/comparison.yml, .github/workflows/tests.yml
- ❌ [scrapy/queuelib](https://github.com/scrapy/queuelib): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/tests.yml
- ❌ [scrapy/w3lib](https://github.com/scrapy/w3lib): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/test.yml
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/tests.yml
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): no cancel-in-progress: .github/workflows/test.yml
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no cancel-in-progress: .github/workflows/test.yml
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): no cancel-in-progress: .github/workflows/test.yml
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): no cancel-in-progress: .github/workflows/ci.yml
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no cancel-in-progress: .github/workflows/main.yml
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no cancel-in-progress: .github/workflows/tests.yml
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no cancel-in-progress: .github/workflows/test.yml
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): no cancel-in-progress: .github/workflows/test.yml
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): no cancel-in-progress: .github/workflows/scrapy-unreleased.yml, .github/workflows/test.yml
- ❌ [scrapinghub/andi](https://github.com/scrapinghub/andi): no cancel-in-progress: .github/workflows/test.yml
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): no cancel-in-progress: .github/workflows/tests-ubuntu.yml, .github/workflows/tests-windows.yml
- ❌ [zytedata/url-matcher](https://github.com/zytedata/url-matcher): no cancel-in-progress: .github/workflows/test.yml
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): no cancel-in-progress: .github/workflows/ci.yml
- ❌ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): no cancel-in-progress: .github/workflows/test.yml
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): no cancel-in-progress: .github/workflows/test.yml
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no cancel-in-progress: .github/workflows/main.yml
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): no cancel-in-progress: .github/workflows/test.yml
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no cancel-in-progress: .github/workflows/main.yml
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/tests.yml
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no cancel-in-progress: .github/workflows/tests.yml
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no cancel-in-progress: .github/workflows/python-app.yml
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no cancel-in-progress: .github/workflows/tests.yml
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no cancel-in-progress: .github/workflows/test.yml
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): no cancel-in-progress: .github/workflows/test.yml
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): no cancel-in-progress: .github/workflows/test.yml
- ❌ [zytedata/clear-html](https://github.com/zytedata/clear-html): no cancel-in-progress: .github/workflows/test.yml
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): no cancel-in-progress: .github/workflows/test.yml
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no cancel-in-progress: .github/workflows/main.yml
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): no cancel-in-progress: .github/workflows/cifuzz.yml, .github/workflows/main.yml
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no cancel-in-progress: .github/workflows/python-package.yml
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no cancel-in-progress: .github/workflows/main.yml
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): no cancel-in-progress: .github/workflows/test.yml
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): no cancel-in-progress: .github/workflows/test.yml
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): no cancel-in-progress: .github/workflows/test.yml
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no cancel-in-progress: .github/workflows/build_and_upload.yml, .github/workflows/tests.yml
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no cancel-in-progress: .github/workflows/main.yml
- ❌ [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official): no cancel-in-progress: .github/workflows/checks.yml
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): no cancel-in-progress: .github/workflows/ci.yml
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/tests.yml
- ❌ [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard): no cancel-in-progress: .github/workflows/ci.yml
- ➖ No workflows triggered by pull requests or pushes. [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)

### pr-guard-trusted-users

The trusted-users of scrapy/unattended-pr-guard include no public members of its trusted-orgs, which it trusts already.

- ❌ [scrapy/scrapy](https://github.com/scrapy/scrapy): public members of trusted orgs: kishan3
- ❌ [scrapy/w3lib](https://github.com/scrapy/w3lib): public members of trusted orgs: kishan3
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): public members of trusted orgs: kishan3
- ➖ Does not use scrapy/unattended-pr-guard. [scrapy/cssselect](https://github.com/scrapy/cssselect), [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint), [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet), [zytedata/url-matcher](https://github.com/zytedata/url-matcher), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api), [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapy/form2request](https://github.com/scrapy/form2request), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [zytedata/agent-exam](https://github.com/zytedata/agent-exam), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### has-sphinx-docs

The project has Sphinx docs (docs/conf.py).

Nothing to report.

### blacken-docs

Code examples in the docs are formatted with blacken-docs.

- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): missing pre-commit hooks: blacken-docs
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): missing pre-commit hooks: blacken-docs
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): missing pre-commit hooks: blacken-docs
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): missing pre-commit hooks: blacken-docs
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): missing pre-commit hooks: blacken-docs
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): missing pre-commit hooks: blacken-docs
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): missing pre-commit hooks: blacken-docs
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no .pre-commit-config.yaml
- ➖ No Sphinx docs. [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### sphinx-lint

The docs are linted with sphinx-lint.

- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): missing pre-commit hooks: sphinx-lint
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): missing pre-commit hooks: sphinx-lint
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): missing pre-commit hooks: sphinx-lint
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): missing pre-commit hooks: sphinx-lint
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): missing pre-commit hooks: sphinx-lint
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): missing pre-commit hooks: sphinx-lint
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no .pre-commit-config.yaml
- ➖ No Sphinx docs. [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

## Documentation

| Check | Statement | Results |
| --- | --- | --- |
| [`sphinx-docs`](#sphinx-docs) | The documentation is a Sphinx project in docs/, written in reStructuredText. | 26/59 passing |
| [`readme-rst`](#readme-rst) | The README is in reStructuredText, as README.rst. | 43/62 passing |
| [`no-wiki`](#no-wiki) | The GitHub wiki has no pages. | 0/62 passing |
| [`no-docs-requirements`](#no-docs-requirements) | Sphinx docs requirements other than sphinx-scrapy are in a docs dependency group, not in docs/requirements.in or docs/requirements.txt. | 5/26 passing |
| [`sphinx-scrapy`](#sphinx-scrapy) | Sphinx docs use sphinx-scrapy. | 15/26 passing |
| [`sphinx-scrapy-pins`](#sphinx-scrapy-pins) | sphinx-scrapy is pinned to the same version in the tox requires and the pre-commit hook rev. | 12/15 passing |
| [`sphinx-scrapy-latest`](#sphinx-scrapy-latest) | sphinx-scrapy is pinned to its latest release. | 4/15 passing |
| [`readthedocs`](#readthedocs) | Sphinx docs are built on Read the Docs (.readthedocs.yml), and the README links to them. | 23/26 passing |
| [`docs-stable-links`](#docs-stable-links) | Links to the docs in the README and in [project.urls] that name a version use stable, which is built from the latest release. | 12/25 passing |
| [`changelog`](#changelog) | There is a changelog, e.g. CHANGES.rst, CHANGELOG.md, NEWS or docs/news.rst. | 55/61 passing |
| [`changelog-date`](#changelog-date) | bump-my-version replaces (unreleased) in the changelog with the release date. | 46/48 passing |

| Project | [sphinx-docs](#sphinx-docs) | [readme-rst](#readme-rst) | [no-wiki](#no-wiki) | [no-docs-requirements](#no-docs-requirements) | [sphinx-scrapy](#sphinx-scrapy) | [sphinx-scrapy-pins](#sphinx-scrapy-pins) | [sphinx-scrapy-latest](#sphinx-scrapy-latest) | [readthedocs](#readthedocs) | [docs-stable-links](#docs-stable-links) | [changelog](#changelog) | [changelog-date](#changelog-date) |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Scrapy and its deps** | | | | | | | | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | ✅ | ✅ | [❌](#no-wiki) | [❌](#no-docs-requirements) | ✅ | ✅ | [❌](#sphinx-scrapy-latest) | ✅ | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | ✅ | ✅ | [❌](#no-wiki) | [❌](#no-docs-requirements) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | ✅ | ✅ | ✅ | ✅ |
| [scrapy/formerly](https://github.com/scrapy/formerly) | [❌](#sphinx-docs) | ✅ | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | [❌](#sphinx-docs) | [❌](#readme-rst) | [❌](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | ✅ | ✅ | [❌](#no-wiki) | [❌](#no-docs-requirements) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | ✅ | [❌](#docs-stable-links) | ✅ | ✅ |
| [scrapy/parsel](https://github.com/scrapy/parsel) | ✅ | ✅ | [⚠️](#no-wiki) | [❌](#no-docs-requirements) | ✅ | ✅ | [❌](#sphinx-scrapy-latest) | ✅ | [❌](#docs-stable-links) | ✅ | ✅ |
| [scrapy/protego](https://github.com/scrapy/protego) | [❌](#sphinx-docs) | ✅ | [❌](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | [❌](#sphinx-docs) | ✅ | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | ✅ | ✅ | [⚠️](#no-wiki) | [❌](#no-docs-requirements) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | ✅ | [❌](#docs-stable-links) | ✅ | ✅ |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | [❌](#sphinx-docs) | [❌](#readme-rst) | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| **Scrapy plugins** | | | | | | | | | | | |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | [❌](#sphinx-docs) | ✅ | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | ✅ | ✅ | [⚠️](#no-wiki) | [❌](#no-docs-requirements) | ✅ | ✅ | [❌](#sphinx-scrapy-latest) | ✅ | [❌](#docs-stable-links) | ✅ | ✅ |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | ✅ | ✅ | [⚠️](#no-wiki) | [❌](#no-docs-requirements) | ✅ | ✅ | [❌](#sphinx-scrapy-latest) | ✅ | [❌](#docs-stable-links) | ✅ | ✅ |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | [❌](#sphinx-docs) | ✅ | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | [➖](#changelog-date) |
| [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules) | [❌](#sphinx-docs) | ✅ | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | [➖](#changelog-date) |
| **Scrapy tools** | | | | | | | | | | | |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | ✅ | ✅ | [⚠️](#no-wiki) | [❌](#no-docs-requirements) | ✅ | [❌](#sphinx-scrapy-pins) | [❌](#sphinx-scrapy-latest) | ✅ | ✅ | ✅ | ✅ |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | ✅ | ✅ | [❌](#no-wiki) | [❌](#no-docs-requirements) | ✅ | [❌](#sphinx-scrapy-pins) | [❌](#sphinx-scrapy-latest) | ✅ | [❌](#docs-stable-links) | ✅ | ✅ |
| **Feed exporters** | | | | | | | | | | | |
| [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc) | [❌](#sphinx-docs) | [❌](#readme-rst) | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | [❌](#changelog) | [➖](#changelog-date) |
| [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage) | [❌](#sphinx-docs) | [❌](#readme-rst) | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | [❌](#changelog) | [➖](#changelog-date) |
| [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox) | [❌](#sphinx-docs) | [❌](#readme-rst) | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | [❌](#changelog) | [➖](#changelog-date) |
| [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive) | [❌](#sphinx-docs) | ✅ | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets) | [❌](#sphinx-docs) | [❌](#readme-rst) | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | [❌](#changelog) | [➖](#changelog-date) |
| [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive) | [❌](#sphinx-docs) | [❌](#readme-rst) | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp) | [❌](#sphinx-docs) | ✅ | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| **scrapy-poet and its deps** | | | | | | | | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | ✅ | [⚠️](#no-wiki) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | [❌](#sphinx-docs) | ✅ | [❌](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | ✅ | ✅ | [⚠️](#no-wiki) | [❌](#no-docs-requirements) | ✅ | ✅ | [❌](#sphinx-scrapy-latest) | ✅ | ✅ | ✅ | ✅ |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | ✅ | [⚠️](#no-wiki) | [❌](#no-docs-requirements) | ✅ | ✅ | [❌](#sphinx-scrapy-latest) | ✅ | ✅ | ✅ | [❌](#changelog-date) |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | [❌](#sphinx-docs) | [❌](#readme-rst) | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| **Zyte API** | | | | | | | | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | ✅ | [⚠️](#no-wiki) | [❌](#no-docs-requirements) | ✅ | ✅ | [❌](#sphinx-scrapy-latest) | ✅ | [❌](#docs-stable-links) | ✅ | ✅ |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | ✅ | [⚠️](#no-wiki) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | ✅ | ✅ | [⚠️](#no-wiki) | [❌](#no-docs-requirements) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | ✅ | ✅ | ✅ | ✅ |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | ✅ | ✅ | [⚠️](#no-wiki) | [❌](#no-docs-requirements) | ✅ | [❌](#sphinx-scrapy-pins) | [❌](#sphinx-scrapy-latest) | ✅ | [❌](#docs-stable-links) | ✅ | ✅ |
| **Scrapy Cloud** | | | | | | | | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | ✅ | ✅ | [⚠️](#no-wiki) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | ✅ | ✅ | [❌](#no-wiki) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [❌](#sphinx-docs) | [❌](#readme-rst) | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow) | [❌](#sphinx-docs) | [❌](#readme-rst) | [❌](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | [➖](#changelog-date) |
| [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera) | [❌](#sphinx-docs) | ✅ | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapinghub/frontera](https://github.com/scrapinghub/frontera) | [❌](#sphinx-docs) | [❌](#readme-rst) | [❌](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | [❌](#changelog) | [➖](#changelog-date) |
| [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend) | [❌](#sphinx-docs) | [❌](#readme-rst) | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| **Data extraction** | | | | | | | | | | | |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | ✅ | ✅ | [⚠️](#no-wiki) | [❌](#no-docs-requirements) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | ✅ | [❌](#docs-stable-links) | ✅ | ✅ |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | [❌](#sphinx-docs) | ✅ | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [zytedata/html-text](https://github.com/zytedata/html-text) | [❌](#sphinx-docs) | ✅ | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | [❌](#sphinx-docs) | ✅ | [❌](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | ✅ | ✅ | [⚠️](#no-wiki) | [❌](#no-docs-requirements) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | ✅ | [❌](#docs-stable-links) | ✅ | ✅ |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [❌](#sphinx-docs) | ✅ | [❌](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | [➖](#changelog-date) |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | [❌](#sphinx-docs) | ✅ | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | [➖](#changelog-date) |
| **Forms** | | | | | | | | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | ✅ | ✅ | [⚠️](#no-wiki) | [❌](#no-docs-requirements) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | ✅ | [❌](#docs-stable-links) | ✅ | ✅ |
| [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus) | ✅ | ✅ | [⚠️](#no-wiki) | [❌](#no-docs-requirements) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [❌](#readthedocs) | ✅ | ✅ | [❌](#changelog-date) |
| [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite) | ✅ | ✅ | [⚠️](#no-wiki) | [❌](#no-docs-requirements) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [❌](#readthedocs) | [❌](#docs-stable-links) | ✅ | [➖](#changelog-date) |
| [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite) | ✅ | ✅ | [⚠️](#no-wiki) | ✅ | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [❌](#readthedocs) | ✅ | ✅ | ✅ |
| **Monitoring** | | | | | | | | | | | |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | ✅ | ✅ | [⚠️](#no-wiki) | [❌](#no-docs-requirements) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | ✅ | [❌](#docs-stable-links) | ✅ | ✅ |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | [❌](#sphinx-docs) | [❌](#readme-rst) | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | [❌](#changelog) | [➖](#changelog-date) |
| **AI agents** | | | | | | | | | | | |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | [➖](#sphinx-docs) | ✅ | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | [❌](#sphinx-docs) | [❌](#readme-rst) | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | ✅ | [❌](#readme-rst) | [⚠️](#no-wiki) | [❌](#no-docs-requirements) | ✅ | ✅ | [❌](#sphinx-scrapy-latest) | ✅ | ✅ | ✅ | ✅ |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | [❌](#sphinx-docs) | [❌](#readme-rst) | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | [❌](#sphinx-docs) | [❌](#readme-rst) | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | [➖](#changelog-date) |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | [❌](#sphinx-docs) | ✅ | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| **Maintenance** | | | | | | | | | | | |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | [❌](#sphinx-docs) | ✅ | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | [➖](#sphinx-docs) | [❌](#readme-rst) | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance) | [➖](#sphinx-docs) | [❌](#readme-rst) | [⚠️](#no-wiki) | [➖](#no-docs-requirements) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | [➖](#changelog) | [➖](#changelog-date) |

### sphinx-docs

The documentation is a Sphinx project in docs/, written in reStructuredText.

- ❌ [scrapy/formerly](https://github.com/scrapy/formerly): no docs/conf.py
- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): no docs/conf.py
- ❌ [scrapy/protego](https://github.com/scrapy/protego): no docs/conf.py
- ❌ [scrapy/queuelib](https://github.com/scrapy/queuelib): no docs/conf.py
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no docs/conf.py
- ❌ [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator): no docs/conf.py
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no docs/conf.py
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): no docs/conf.py
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no docs/conf.py
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no docs/conf.py
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no docs/conf.py
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no docs/conf.py
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no docs/conf.py
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no docs/conf.py
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): no docs/conf.py
- ❌ [scrapinghub/andi](https://github.com/scrapinghub/andi): no docs/conf.py
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): no docs/conf.py; Markdown files: docs/BENCHMARKS.md, docs/COMPATIBILITY.md, docs/DESIGN.md, docs/MIGRATION.md, docs/PYTHON.md, docs/RELEASING.md, docs/SUPPORT_SNAPSHOT.md, docs/TESTING.md, docs/WEBPOET_SURFACE.md
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no docs/conf.py
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no docs/conf.py
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no docs/conf.py
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no docs/conf.py
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): no docs/conf.py
- ❌ [zytedata/clear-html](https://github.com/zytedata/clear-html): no docs/conf.py
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): no docs/conf.py
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no docs/conf.py
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no docs/conf.py
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no docs/conf.py
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no docs/conf.py
- ❌ [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official): no docs/conf.py
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no docs/conf.py; Markdown files: docs/tui-ux.md
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no docs/conf.py; Markdown files: docs/configuration.md, docs/gcp-setup.md, docs/getting-started.md, docs/harnesses-and-models.md, docs/local-runtime.md, docs/observability.md, docs/openrouter.md, docs/runs-and-sessions.md, docs/sandbox-runtime.md, docs/secrets-and-security.md, docs/structured-output.md
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): no docs/conf.py
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no docs/conf.py
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### readme-rst

The README is in reStructuredText, as README.rst.

- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): README.md instead
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): README.md instead
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): README.md instead
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): README.md instead
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): README.md instead
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): README.md instead
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): README.md instead
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): README.md instead
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): README.md instead
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): README.md instead
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): README.md instead
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): README.md instead
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): README.md instead
- ❌ [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official): README.md instead
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): README.md instead
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): README.md instead
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): README.md instead
- ❌ [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard): README.md instead
- ❌ [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance): README.md instead

### no-wiki

The GitHub wiki has no pages.

- ❌ [scrapy/scrapy](https://github.com/scrapy/scrapy): https://github.com/scrapy/scrapy/wiki has pages
- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): https://github.com/scrapy/cssselect/wiki has pages
- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): https://github.com/scrapy/itemadapter/wiki has pages
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): https://github.com/scrapy/itemloaders/wiki has pages
- ❌ [scrapy/protego](https://github.com/scrapy/protego): https://github.com/scrapy/protego/wiki has pages
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): https://github.com/scrapinghub/scrapyrt/wiki has pages
- ❌ [scrapinghub/andi](https://github.com/scrapinghub/andi): https://github.com/scrapinghub/andi/wiki has pages
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): https://github.com/scrapinghub/shub/wiki has pages
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): https://github.com/scrapinghub/shub-workflow/wiki has pages
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): https://github.com/scrapinghub/frontera/wiki has pages
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): https://github.com/scrapinghub/price-parser/wiki has pages
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): https://github.com/scrapinghub/extruct/wiki has pages
- ⚠️ [scrapy/formerly](https://github.com/scrapy/formerly): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapy/parsel](https://github.com/scrapy/parsel): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapy/queuelib](https://github.com/scrapy/queuelib): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapy/w3lib](https://github.com/scrapy/w3lib): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [zytedata/url-matcher](https://github.com/zytedata/url-matcher): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapy/frostwork](https://github.com/scrapy/frostwork): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [zytedata/clear-html](https://github.com/zytedata/clear-html): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [zytedata/html-text](https://github.com/zytedata/html-text): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapy/form2request](https://github.com/scrapy/form2request): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [zytedata/harness-run](https://github.com/zytedata/harness-run): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled
- ⚠️ [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance): SyncError: fatal: could not read Username for 'https://github.com': terminal prompts disabled

### no-docs-requirements

Sphinx docs requirements other than sphinx-scrapy are in a docs dependency group, not in docs/requirements.in or docs/requirements.txt.

- ❌ [scrapy/scrapy](https://github.com/scrapy/scrapy): found docs/requirements.in, docs/requirements.txt
- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): found docs/requirements.txt
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): found docs/requirements.txt
- ❌ [scrapy/parsel](https://github.com/scrapy/parsel): found docs/requirements.in, docs/requirements.txt
- ❌ [scrapy/w3lib](https://github.com/scrapy/w3lib): found docs/requirements.txt
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): found docs/requirements.in, docs/requirements.txt
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): found docs/requirements.in, docs/requirements.txt
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): found docs/requirements.txt
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): found docs/requirements.txt
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): found docs/requirements.in, docs/requirements.txt
- ❌ [zytedata/url-matcher](https://github.com/zytedata/url-matcher): found docs/requirements.in, docs/requirements.txt
- ❌ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): found docs/requirements.in, docs/requirements.txt
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): found docs/requirements.txt
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): found docs/requirements.txt
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): found docs/requirements.txt
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): found docs/requirements.txt
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): found docs/requirements.txt
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): found docs/requirements.txt
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): found docs/requirements.txt
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): found docs/requirements.txt
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): found docs/requirements.in, docs/requirements.txt
- ➖ No Sphinx docs. [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### sphinx-scrapy

Sphinx docs use sphinx-scrapy.

- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): sphinx_scrapy not in docs/conf.py
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): sphinx_scrapy not in docs/conf.py
- ❌ [scrapy/w3lib](https://github.com/scrapy/w3lib): sphinx_scrapy not in docs/conf.py
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): sphinx_scrapy not in docs/conf.py
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): sphinx_scrapy not in docs/conf.py
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): sphinx_scrapy not in docs/conf.py
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): sphinx_scrapy not in docs/conf.py
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): sphinx_scrapy not in docs/conf.py
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): sphinx_scrapy not in docs/conf.py
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): sphinx_scrapy not in docs/conf.py
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): sphinx_scrapy not in docs/conf.py
- ➖ No Sphinx docs. [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### sphinx-scrapy-pins

sphinx-scrapy is pinned to the same version in the tox requires and the pre-commit hook rev.

- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): not pinned in tox, .pre-commit-config.yaml
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): not pinned in tox, .pre-commit-config.yaml
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): not pinned in tox, .pre-commit-config.yaml
- ➖ Does not use sphinx-scrapy. [scrapy/cssselect](https://github.com/scrapy/cssselect), [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/itemloaders](https://github.com/scrapy/itemloaders), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/w3lib](https://github.com/scrapy/w3lib), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapy/form2request](https://github.com/scrapy/form2request), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### sphinx-scrapy-latest

sphinx-scrapy is pinned to its latest release.

- ❌ [scrapy/scrapy](https://github.com/scrapy/scrapy): pinned to 0.13.0, latest is 0.15.0
- ❌ [scrapy/parsel](https://github.com/scrapy/parsel): pinned to 0.13.0, latest is 0.15.0
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): pinned to 0.9.0, latest is 0.15.0
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): pinned to 0.13.0, latest is 0.15.0
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): not pinned
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): not pinned
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): pinned to 0.8.12, latest is 0.15.0
- ❌ [zytedata/url-matcher](https://github.com/zytedata/url-matcher): pinned to 0.13.0, latest is 0.15.0
- ❌ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): pinned to 0.8.12, latest is 0.15.0
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): not pinned
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): pinned to 0.8.10, latest is 0.15.0
- ➖ Does not use sphinx-scrapy. [scrapy/cssselect](https://github.com/scrapy/cssselect), [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/itemloaders](https://github.com/scrapy/itemloaders), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/w3lib](https://github.com/scrapy/w3lib), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapy/form2request](https://github.com/scrapy/form2request), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### readthedocs

Sphinx docs are built on Read the Docs (.readthedocs.yml), and the README links to them.

- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): the README does not link to Formasaurus.readthedocs.io or Formasaurus.readthedocs.org
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): no .readthedocs.yml
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no .readthedocs.yml; the README does not link to python-crfsuite.readthedocs.io or python-crfsuite.readthedocs.org
- ➖ No Sphinx docs. [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### docs-stable-links

Links to the docs in the README and in [project.urls] that name a version use stable, which is built from the latest release.

- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): links to latest in README.rst; latest in pyproject.toml
- ❌ [scrapy/parsel](https://github.com/scrapy/parsel): links to latest in pyproject.toml
- ❌ [scrapy/w3lib](https://github.com/scrapy/w3lib): links to latest in pyproject.toml
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): links to latest in README.rst
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): links to latest in README.rst
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): links to latest in README.rst; latest in pyproject.toml
- ❌ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): links to latest in README.rst; latest in pyproject.toml
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): links to latest in README.rst
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): links to latest in README.rst; latest in pyproject.toml
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): links to latest in README.rst; latest in pyproject.toml
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): links to latest in README.rst; latest in pyproject.toml
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): links to latest in README.rst
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): links to latest in README.rst; latest in pyproject.toml
- ➖ On docs.scrapy.org, latest is the latest release and master the default branch. [scrapy/scrapy](https://github.com/scrapy/scrapy)
- ➖ No Sphinx docs. [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### changelog

There is a changelog, e.g. CHANGES.rst, CHANGELOG.md, NEWS or docs/news.rst.

- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no changelog file
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no changelog file
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no changelog file
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no changelog file
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no changelog file
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no changelog file
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### changelog-date

bump-my-version replaces (unreleased) in the changelog with the release date.

- ❌ [zytedata/url-matcher](https://github.com/zytedata/url-matcher): no file replacement of (unreleased) with {now:%Y-%m-%d}
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): no file replacement of (unreleased) with {now:%Y-%m-%d}
- ➖ Does not use bump-my-version. [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [zytedata/harness-run](https://github.com/zytedata/harness-run)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

## Releases

| Check | Statement | Results |
| --- | --- | --- |
| [`latest-release`](#latest-release) | The latest release on PyPI, with its date. | no (5), 0.1.0 (2026-10-21) (2), 2.19.0 (2026-09-10) (1), 1.6.0 (2026-10-09) (1), 0.1.0 (2026-08-05) (1), 0.14.0 (2026-10-29) (1), 1.5.0 (2026-09-29) (1), 1.12.1 (2026-09-28) (1), 0.7.0 (2026-09-21) (1), 1.10.0 (2026-08-24) (1), 2.5.0 (2026-09-30) (1), 0.2.1 (2024-01-16) (1), 0.7.0 (2026-10-26) (1), 0.0.48 (2026-07-10) (1), 0.2.0 (2024-09-26) (1), 0.3.0 (2024-12-30) (1), 2024.11.5 (2024-11-05) (1), 0.1.1 (2026-01-27) (1), 0.18.1 (2026-06-29) (1), 1.1.0 (2025-02-12) (1), 0.27.2 (2026-04-28) (1), 0.9.0 (2026-09-17) (1), 0.24.1 (2026-04-28) (1), 0.6.0 (2025-02-14) (1), 0.1.6 (2026-09-23) (1), 0.36.0 (2026-08-20) (1), 0.11.0 (2026-07-23) (1), 2.4.1 (2025-03-24) (1), 0.31.0 (2026-10-16) (1), 2.9.0 (2026-08-12) (1), 2.18.1 (2026-07-08) (1), 0.18.1 (2026-01-28) (1), 1.14.46 (2026-10-30) (1), 0.3.0 (2025-06-06) (1), 0.8.1 (2019-04-05) (1), 0.6.1 (2025-10-31) (1), 0.6.0 (2025-10-24) (1), 0.5.0 (2025-10-24) (1), 0.7.1 (2025-10-06) (1), 0.5.1 (2026-03-19) (1), 1.4.3 (2026-09-03) (1), 0.18.0 (2024-11-08) (1), 0.3.2 (2023-03-28) (1), 0.2.0 (2024-07-15) (1), 0.10.0 (2024-11-07) (1), 0.5.0 (2024-06-18) (1), 0.9.12 (2025-12-23) (1), 1.27.0 (2026-08-10) (1), 0.1.2 (2026-09-07) (1), 0.3.0 (2026-10-20) (1), 0.1.1 (2026-09-14) (1), 0.4.0 (2026-09-23) (1), 0.7.0 (2026-10-03) (1), 0.15.0 (2026-10-27) (1) |
| [`unreleased-changes`](#unreleased-changes) | The default branch has commits since the latest release on PyPI. | 48/54 yes |
| [`trusted-publishing`](#trusted-publishing) | Releases are published to PyPI from GitHub Actions through trusted publishing, in a job with a GitHub environment. | 37/59 passing |
| [`publish-on-tag`](#publish-on-tag) | Publishing is triggered by pushing a tag, not by creating a GitHub release. | 48/59 passing |
| [`separate-build-job`](#separate-build-job) | The publish workflow builds distributions in a separate job from the one that publishes them. | 22/59 passing |
| [`bump-my-version`](#bump-my-version) | bump-my-version is configured, in pyproject.toml or .bumpversion.toml. | 48/61 passing |

| Project | [latest-release](#latest-release) | [unreleased-changes](#unreleased-changes) | [trusted-publishing](#trusted-publishing) | [publish-on-tag](#publish-on-tag) | [separate-build-job](#separate-build-job) | [bump-my-version](#bump-my-version) |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Scrapy and its deps** | | | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | 2.19.0 (2026-09-10) | yes | ✅ | ✅ | ✅ | ✅ |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | 1.6.0 (2026-10-09) | yes | ✅ | ✅ | ✅ | ✅ |
| [scrapy/formerly](https://github.com/scrapy/formerly) | 0.1.0 (2026-08-05) | yes | ✅ | ✅ | ✅ | ✅ |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | 0.14.0 (2026-10-29) | yes | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | 1.5.0 (2026-09-29) | yes | ✅ | [❌](#publish-on-tag) | [❌](#separate-build-job) | ✅ |
| [scrapy/parsel](https://github.com/scrapy/parsel) | 1.12.1 (2026-09-28) | yes | ✅ | ✅ | ✅ | ✅ |
| [scrapy/protego](https://github.com/scrapy/protego) | 0.7.0 (2026-09-21) | yes | ✅ | ✅ | ✅ | ✅ |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | 1.10.0 (2026-08-24) | yes | ✅ | ✅ | ✅ | ✅ |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | 2.5.0 (2026-09-30) | yes | ✅ | ✅ | ✅ | ✅ |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | 0.2.1 (2024-01-16) | yes | ✅ | ✅ | ✅ | ✅ |
| **Scrapy plugins** | | | | | | |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | 0.7.0 (2026-10-26) | no | ✅ | ✅ | ✅ | ✅ |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | 0.0.48 (2026-07-10) | yes | [❌](#trusted-publishing) | [❌](#publish-on-tag) | [❌](#separate-build-job) | ✅ |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | 0.2.0 (2024-09-26) | yes | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | 0.3.0 (2024-12-30) | yes | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | [❌](#bump-my-version) |
| [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules) | 2024.11.5 (2024-11-05) | yes | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | [❌](#bump-my-version) |
| **Scrapy tools** | | | | | | |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | 0.1.1 (2026-01-27) | yes | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | 0.18.1 (2026-06-29) | yes | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| **Feed exporters** | | | | | | |
| [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc) | no | [➖](#unreleased-changes) | ✅ | [❌](#publish-on-tag) | [❌](#separate-build-job) | [❌](#bump-my-version) |
| [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage) | no | [➖](#unreleased-changes) | [❌](#trusted-publishing) | [❌](#publish-on-tag) | [❌](#separate-build-job) | [❌](#bump-my-version) |
| [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox) | no | [➖](#unreleased-changes) | [❌](#trusted-publishing) | [❌](#publish-on-tag) | [❌](#separate-build-job) | [❌](#bump-my-version) |
| [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive) | 0.1.0 (2026-10-21) | no | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets) | no | [➖](#unreleased-changes) | [❌](#trusted-publishing) | [❌](#publish-on-tag) | [❌](#separate-build-job) | [❌](#bump-my-version) |
| [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive) | 0.1.0 (2026-10-21) | no | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp) | 1.1.0 (2025-02-12) | no | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| **scrapy-poet and its deps** | | | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | 0.27.2 (2026-04-28) | yes | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | 0.9.0 (2026-09-17) | yes | ✅ | ✅ | ✅ | ✅ |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | 0.24.1 (2026-04-28) | yes | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | 0.6.0 (2025-02-14) | yes | ✅ | ✅ | ✅ | ✅ |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | 0.1.6 (2026-09-23) | yes | ✅ | ✅ | ✅ | ✅ |
| **Zyte API** | | | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | 0.36.0 (2026-08-20) | yes | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | 0.11.0 (2026-07-23) | yes | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | 2.4.1 (2025-03-24) | yes | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | 0.31.0 (2026-10-16) | yes | ✅ | ✅ | ✅ | ✅ |
| **Scrapy Cloud** | | | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | 2.9.0 (2026-08-12) | yes | ✅ | ✅ | ✅ | ✅ |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | 2.18.1 (2026-07-08) | yes | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | 0.18.1 (2026-01-28) | yes | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow) | 1.14.46 (2026-10-30) | yes | [❌](#trusted-publishing) | [❌](#publish-on-tag) | [❌](#separate-build-job) | [❌](#bump-my-version) |
| [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera) | 0.3.0 (2025-06-06) | yes | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapinghub/frontera](https://github.com/scrapinghub/frontera) | 0.8.1 (2019-04-05) | yes | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | [❌](#bump-my-version) |
| [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend) | 0.6.1 (2025-10-31) | no | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| **Data extraction** | | | | | | |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | 0.6.0 (2025-10-24) | yes | ✅ | ✅ | ✅ | ✅ |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | 0.5.0 (2025-10-24) | yes | ✅ | ✅ | ✅ | ✅ |
| [zytedata/html-text](https://github.com/zytedata/html-text) | 0.7.1 (2025-10-06) | yes | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | 0.5.1 (2026-03-19) | yes | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | 1.4.3 (2026-09-03) | yes | ✅ | [❌](#publish-on-tag) | ✅ | ✅ |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | 0.18.0 (2024-11-08) | yes | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | [❌](#bump-my-version) |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | 0.3.2 (2023-03-28) | yes | [❌](#trusted-publishing) | [❌](#publish-on-tag) | [❌](#separate-build-job) | [❌](#bump-my-version) |
| **Forms** | | | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | 0.2.0 (2024-07-15) | yes | ✅ | ✅ | ✅ | ✅ |
| [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus) | 0.10.0 (2024-11-07) | yes | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite) | 0.5.0 (2024-06-18) | no | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | [❌](#bump-my-version) |
| [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite) | 0.9.12 (2025-12-23) | yes | [❌](#trusted-publishing) | [❌](#publish-on-tag) | ✅ | ✅ |
| **Monitoring** | | | | | | |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | 1.27.0 (2026-08-10) | yes | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | no | [➖](#unreleased-changes) | [❌](#trusted-publishing) | [❌](#publish-on-tag) | [❌](#separate-build-job) | [❌](#bump-my-version) |
| **AI agents** | | | | | | |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | [➖](#latest-release) | [➖](#unreleased-changes) | [➖](#trusted-publishing) | [➖](#publish-on-tag) | [➖](#separate-build-job) | ✅ |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | 0.1.2 (2026-09-07) | yes | ✅ | ✅ | ✅ | ✅ |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | 0.3.0 (2026-10-20) | yes | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | 0.1.1 (2026-09-14) | yes | ✅ | ✅ | ✅ | ✅ |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | 0.4.0 (2026-09-23) | yes | ✅ | ✅ | ✅ | [❌](#bump-my-version) |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | 0.7.0 (2026-10-03) | yes | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| **Maintenance** | | | | | | |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | 0.15.0 (2026-10-27) | yes | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | [➖](#latest-release) | [➖](#unreleased-changes) | [➖](#trusted-publishing) | [➖](#publish-on-tag) | [➖](#separate-build-job) | ✅ |
| [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance) | [➖](#latest-release) | [➖](#unreleased-changes) | [➖](#trusted-publishing) | [➖](#publish-on-tag) | [➖](#separate-build-job) | [➖](#bump-my-version) |

### latest-release

The latest release on PyPI, with its date.

- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### unreleased-changes

The default branch has commits since the latest release on PyPI.

- ➖ Not on PyPI. [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### trusted-publishing

Releases are published to PyPI from GitHub Actions through trusted publishing, in a job with a GitHub environment.

- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): .github/workflows/publish.yml: job 'publish' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): .github/workflows/publish.yml: job 'deploy' has no environment
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): .github/workflows/publish.yml uses an API token
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no workflow publishes to PyPI
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no workflow publishes to PyPI
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no workflow publishes to PyPI
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): .github/workflows/publish.yml: job 'publish' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): .github/workflows/publish.yml: job 'publish' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no workflow publishes to PyPI
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): .github/workflows/publish.yml uses an API token
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): .github/workflows/publish.yml uses an API token
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): .github/workflows/publish.yml uses an API token
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): .github/workflows/publish.yml uses an API token
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): .github/workflows/python-publish.yml: job 'deploy' has no environment; .github/workflows/python-publish.yml publishes with twine upload
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): .github/workflows/build_and_upload.yml: job 'upload_to_pypi' has no environment; .github/workflows/build_and_upload.yml uses an API token; .github/workflows/build_and_upload.yml lacks the id-token: write permission
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no workflow publishes to PyPI
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### publish-on-tag

Publishing is triggered by pushing a tag, not by creating a GitHub release.

- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): .github/workflows/publish.yml is triggered by GitHub releases
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): .github/workflows/publish.yml is triggered by GitHub releases
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): .github/workflows/release.yml is not triggered by tag pushes
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no workflow publishes to PyPI
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no workflow publishes to PyPI
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no workflow publishes to PyPI
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no workflow publishes to PyPI
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): .github/workflows/publish.yml is triggered by GitHub releases
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): .github/workflows/publish.yml is triggered by GitHub releases
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): .github/workflows/build_and_upload.yml is triggered by GitHub releases
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no workflow publishes to PyPI
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### separate-build-job

The publish workflow builds distributions in a separate job from the one that publishes them.

- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): .github/workflows/release.yml: job 'release' builds and publishes
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no workflow publishes to PyPI
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no workflow publishes to PyPI
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no workflow publishes to PyPI
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no workflow publishes to PyPI
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): .github/workflows/python-publish.yml: job 'deploy' builds and publishes
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no workflow publishes to PyPI
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): .github/workflows/publish.yml: job 'publish' builds and publishes
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### bump-my-version

bump-my-version is configured, in pyproject.toml or .bumpversion.toml.

- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): only legacy (bump2version) configuration, in .bumpversion.cfg
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): only legacy (bump2version) configuration, in setup.cfg
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): only legacy (bump2version) configuration, in .bumpversion.cfg
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): only legacy (bump2version) configuration, in .bumpversion.cfg
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)
