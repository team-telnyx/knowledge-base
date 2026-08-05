---
title: CI/CD for Edge Compute
summary: How to deploy Telnyx Edge Compute functions from CI pipelines using the `telnyx-edge`
  CLI, with working examples for GitHub Actions, GitLab CI, and CircleCI, plus patterns
  for staging/production, rollback, smoke testing, and troubleshooting.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/deploy/index
updated_at: 2026-08-05T13:40:22Z
---

# CI/CD for Edge Compute

*Part 2 of 2 — see also: [Part 1](ci-cd-for-edge-compute--part-1.md)*

How to deploy Telnyx Edge Compute functions from CI pipelines using the `telnyx-edge` CLI, with working examples for GitHub Actions, GitLab CI, and CircleCI, plus patterns for staging/production, rollback, smoke testing, and troubleshooting.

## Staging and production

There is no `--env` flag and no environment promotion — `ship` always deploys the function that `func.toml` names. Environments are separate functions, e.g. `my-api-staging` and `my-api`, each with its own URL, secrets bindings, and revision history.

Register both once, locally (`new-func` creates the function server-side and writes its UUID `func_id` into that directory's `func.toml` — this is a one-time setup step, not a CI step):

```bash
telnyx-edge new-func -l=ts -n=my-api-staging
telnyx-edge new-func -l=ts -n=my-api
```

Keep one codebase and both generated `func.toml` files in the repo; each pipeline job copies the matching one into place before shipping:

```
my-api/
├── index.ts
├── package.json
├── func.toml                 # production — func_id of my-api
└── deploy/
    └── func.staging.toml     # staging — func_id of my-api-staging
```

Because bindings are declared in `func.toml`, the two files can also point at per-environment resources — for example a separate [KV](kv--part-1.md) namespace id per environment.

```yaml
# .github/workflows/deploy.yml — staging on main, production on v* tags
name: Deploy

on:
  push:
    branches: [main]
    tags: ['v*']

env:
  TELNYX_EDGE_VERSION: v0.2.3

jobs:
  deploy-staging:
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install telnyx-edge
        run: |
          curl -fsSL "https://github.com/team-telnyx/edge-compute/releases/download/${TELNYX_EDGE_VERSION}/telnyx-edge-${TELNYX_EDGE_VERSION}-linux-amd64.tar.gz" | tar xz
          sudo mv "telnyx-edge-${TELNYX_EDGE_VERSION}-linux-amd64/telnyx-edge" /usr/local/bin/
      - name: Authenticate
        env:
          TELNYX_API_KEY: ${{ secrets.TELNYX_API_KEY }}
        run: telnyx-edge auth api-key set "$TELNYX_API_KEY"
      - name: Ship the staging function
        run: |
          cp deploy/func.staging.toml func.toml
          telnyx-edge ship

  deploy-production:
    if: startsWith(github.ref, 'refs/tags/v')
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install telnyx-edge
        run: |
          curl -fsSL "https://github.com/team-telnyx/edge-compute/releases/download/${TELNYX_EDGE_VERSION}/telnyx-edge-${TELNYX_EDGE_VERSION}-linux-amd64.tar.gz" | tar xz
          sudo mv "telnyx-edge-${TELNYX_EDGE_VERSION}-linux-amd64/telnyx-edge" /usr/local/bin/
      - name: Authenticate
        env:
          TELNYX_API_KEY: ${{ secrets.TELNYX_API_KEY }}
        run: telnyx-edge auth api-key set "$TELNYX_API_KEY"
      - name: Ship the production function
        run: telnyx-edge ship
```

If you prefer fully separate directories over the `func.toml` swap, keep one function directory per environment and ship each with `telnyx-edge ship --from-dir <path>`. If staging and production live in different Telnyx accounts, store one API key secret per account and reference the right one in each job.

## Rollback

Every successful `ship` produces an immutable revision. Rolling back retargets traffic to a previous revision instantly — no rebuild, no re-upload:

```bash
# List recent revisions (newest first) with their ids
telnyx-edge revisions list my-api

# Retarget traffic to a previous revision
telnyx-edge rollback my-api a1b2c3d
```

Only revisions that reached `deploy_ok` can be rolled back to. You can wire these commands into a manually triggered pipeline job (e.g. `workflow_dispatch` on GitHub Actions), but they work just as well from a laptop — rollback does not need your source tree.

A `git revert` + re-ship also works, but it goes through a full build; `rollback` is the fast path.

## Smoke test after deploy

The function URL is stable, and the TypeScript/JavaScript scaffold answers `/health` with 200 — on other runtimes, point the check at a route your function serves. A post-deploy check is one step:

```yaml
- name: Smoke test
  run: curl -fsS --retry 5 --retry-delay 2 --retry-all-errors https://my-api-<func-id-prefix>.telnyxcompute.com/health
```

If it fails, roll back with `telnyx-edge rollback` as above. There is no platform metrics or logs surface to poll — see [Observability](observability.md) for what your function should emit instead.

## CI secrets vs. function secrets

Two different things:

|  | Where it lives | What it's for |
| --- | --- | --- |
| `TELNYX_API_KEY` | Your CI platform's secret store | Lets the pipeline run `auth api-key set` and `ship` |
| Function secrets | The Telnyx platform, via `telnyx-edge secrets add <key> <value>` | Values your function reads at runtime |

Function secrets are not deployed from CI variables — manage them with the CLI (the arguments are positional). Values are injected into function containers at deploy time, so re-ship a function after changing a secret it uses. See [Secrets](secrets.md).

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `ship` fails with an authentication error | The CLI does not pick up `$TELNYX_API_KEY` from the environment. Run `telnyx-edge auth api-key set "$TELNYX_API_KEY"` as a prior step; `telnyx-edge auth status` confirms. |
| Install step 404s | The un-versioned `releases/latest/download/...` URL does not exist. Use the version-stamped asset URL shown above. |
| Function stuck in `build_failed` or `deploy_failed` | `telnyx-edge reset-func <name>` tears down the failed deploy and returns the function to `created` (id, name, and config preserved), then re-ship. |
| `ship` monitoring times out | Default monitoring timeout is 5 minutes. Raise it with `--timeout` (e.g. `telnyx-edge ship --timeout 10m`). |
| Obscure failures | Re-run with `-v` for verbose logging. |

## Next steps

- [CLI reference](cli-reference--part-1.md) — every command and flag.
- [Versions & Rollback](versions-rollback.md) — how revisions and rollback work.
- [Secrets](secrets.md) — runtime secrets for your functions.
- [Observability](observability.md) — what you can (and can't) see after a deploy.
