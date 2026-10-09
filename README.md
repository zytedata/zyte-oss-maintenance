# {{REPO_NAME}}

> Created from **zyte-service-template** by the Zyte repo governance portal.

## Governance model

This repository is **governed**. When the portal created it, it set the org
custom property `governed=true` (plus `production`, `contains_code`, and
`lifecycle`). Org-level **rulesets** in your GitHub org then apply automatically,
based on those properties — you don't configure branch protection per repo:

| Ruleset | Applies when | Effect on the default branch |
|---------|--------------|------------------------------|
| `baseline` | `governed=true` | No force-push, no branch deletion |
| `require-pr-production` | `governed=true` AND `production=true` | PRs required, ≥1 approval, stale reviews dismissed |
| `require-secrets-scan` | `governed=true` AND `contains_code=true` | The `secrets / detect-secrets` check must pass |

### Secrets scanning

`.github/workflows/secrets.yml` calls the **central** reusable workflow in
`zytedata/governance`. The required status check is **`secrets / detect-secrets`**.
You cannot weaken this:

- The scan logic lives in the governance repo, not here.
- The check is required by the org ruleset, so a missing/failed check blocks merge.
- New secrets must be explicitly audited into `.secrets.baseline` (and reviewed)
  before a PR can merge.

Run the scan locally before pushing:

```bash
pip install detect-secrets pre-commit
pre-commit install
pre-commit run --all-files
# If you add a legitimate, reviewed value that trips the scanner, audit it:
#   detect-secrets scan > .secrets.baseline   # then review the diff in your PR
```

## License

See [LICENSE](LICENSE) — replace the placeholder with your chosen license.
