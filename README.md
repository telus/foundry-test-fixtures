# Foundry Test Fixtures

Test repo for smoke testing the [Foundry](https://github.com/fuelix/foundry) multi-agent review platform after deploys.

## Test PRs

Open these PRs to validate Foundry behavior:

| Branch | Scenario | Expected Verdict |
|--------|----------|-----------------|
| `test/clean-pr` | Clean code, ticket in title | approve |
| `test/bug-pr` | Deliberate bug (SQL injection) | request_changes |
| `test/no-ticket` | No ticket ref in title or body | request_changes (ComplianceGuard) |

## Usage

```bash
# Open a test PR
gh pr create --base main --head test/clean-pr --title "FOUND-1: Add user greeting" --body ""

# Or trigger via API
curl -X POST https://buildbuddy-....run.app/reviews \
  -H 'Content-Type: application/json' \
  -d '{"repo": "fuelix/foundry-test-fixtures", "pr_number": 1, "dry_run": true}'
```

## Setup

The Foundry GitHub App must be installed on this repo. Add `fuelix/foundry-test-fixtures` to `APPROVE_REPOS` in the Cloud Run Job env vars to enable approve/request_changes verdicts.
