# The Claw Renovate Showcase

This public repository exists to demo an external agent ("the claw") that uses `github-mcp-server` to inspect, rerun, triage, and merge Renovate dependency PRs.

It is intentionally small and produces three useful scenarios:

- Mass merge: several simple Renovate PRs with green CI.
- Flaky CI: a dedicated `flaky` job fails about 25% of the time and can pass on rerun.
- Breaking change: Renovate opens a separate pydantic v1 to v2 PR that should not be merged automatically.

Point the claw at this repo with:

```bash
github-mcp-server --toolsets=pull_requests,actions,issues,orgs --allowed-pr-authors='renovate[bot]'
```

Renovate is expected to run through the hosted Mend Renovate GitHub App. After the onboarding PR is merged, it should open dependency PRs authored by `renovate[bot]`.
