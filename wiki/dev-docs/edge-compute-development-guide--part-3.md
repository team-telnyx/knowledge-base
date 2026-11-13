---
title: Edge Compute Development Guide
summary: A comprehensive guide to building, testing, and deploying serverless functions
  on Telnyx Edge Compute — covering local development workflows, step-by-step tutorials
  for common applications, reusable code snippets across multiple languages, production-grade
  reference architectures, and CI/CD deployment pipelines.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/demos/build-a-rest-api
- url: https://developers.telnyx.com/docs/edge-compute/demos/image-resizer
- url: https://developers.telnyx.com/docs/edge-compute/demos/index
- url: https://developers.telnyx.com/docs/edge-compute/demos/sms-webhook-handler
- url: https://developers.telnyx.com/docs/edge-compute/demos/voice-call-router
- url: https://developers.telnyx.com/docs/edge-compute/deploy
- url: https://developers.telnyx.com/docs/edge-compute/development
- url: https://developers.telnyx.com/docs/edge-compute/examples/index
- url: https://developers.telnyx.com/docs/edge-compute/frameworks-support
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/global-api-gateway
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/index
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/iot-data-ingestion
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/real-time-media-pipeline
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/telecom-event-processor
updated_at: 2026-11-13T10:28:47Z
---

# Edge Compute Development Guide

*Part 3 of 3 — see also: [Part 1](edge-compute-development-guide--part-1.md), [Part 2](edge-compute-development-guide--part-2.md)*

A comprehensive guide to building, testing, and deploying serverless functions on Telnyx Edge Compute — covering local development workflows, step-by-step tutorials for common applications, reusable code snippets across multiple languages, production-grade reference architectures, and CI/CD deployment pipelines.

## Deployment

Automate Edge Compute deployments with CI/CD pipelines.

### Authentication

CI/CD pipelines need a Telnyx API key with Edge Compute permissions. Create a deployment key in the [Telnyx Portal](https://portal.telnyx.com) and store it as a secret in your CI/CD platform — never commit API keys to your repository. The CLI does not read `TELNYX_API_KEY` from the environment — each pipeline job must run `telnyx-edge auth api-key set "$TELNYX_API_KEY"` before `telnyx-edge ship`, which persists the key to `~/.telnyx-edge/config.toml` for the rest of the job.

### GitHub Actions

Deploys on every push to `main`; tag pushes also trigger this workflow (that trigger is what fires the production job in the staging and production flow below):

```yaml
# .github/workflows/deploy.yml
name: Deploy Edge Function

on:
  push:
    branches: [main]
    tags: ['v*']

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install Telnyx CLI
        run: |
          wget -qO- https://github.com/team-telnyx/edge-compute/releases/latest/download/telnyx-edge-linux-amd64.tar.gz | tar xz
          sudo mv telnyx-edge /usr/local/bin/
          echo "$HOME/.telnyx/bin" >> $GITHUB_PATH
      - name: Deploy function
        if: github.ref == 'refs/heads/main'
        env:
          TELNYX_API_KEY: ${{ secrets.TELNYX_API_KEY }}
        run: |
          telnyx-edge auth api-key set "$TELNYX_API_KEY"
          telnyx-edge ship
```

This baseline example assumes a single environment. For separate staging and production functions, use the two jobs in the staging and production section below — they replace the Deploy function job, not add to it (otherwise a `main` push would deploy twice, and a tag push would ship the staging config under the production key).

To run tests before deploying, add a separate `test` job that the `deploy` job depends on (`needs: test`). Put a main-branch guard (`if: github.ref == 'refs/heads/main'`) on staging-only jobs; the production job fires on `v*` tags, so it must not be gated on the branch. Keep the shared `test` job itself ungated — if `test` is guarded on the branch, a `v*` tag push skips it, and every job that `needs: test` (including production) is skipped with it.

### GitLab CI

Use a two-stage pipeline (`test`, `deploy`) with the deploy stage restricted to the `main` branch. Download and install the CLI in the deploy script, set `TELNYX_API_KEY` as a CI variable, and run `telnyx-edge auth api-key set "$TELNYX_API_KEY"` before `telnyx-edge ship`.

### CircleCI

Define `test` and `deploy` jobs with a workflow that requires test to pass and filters to the `main` branch. Install the CLI in the deploy job and run `telnyx-edge auth api-key set "$TELNYX_API_KEY"` before `telnyx-edge ship`.

### Staging and production

There is no environment flag and no environment promotion: `telnyx-edge ship` always deploys the function that `func.toml` names. Environments are separate functions — for example `my-api-staging` and `my-api` — each with its own URL, bindings, and revision history. Register each environment's function once with `telnyx-edge new-func -l=ts -n=my-api-staging` (the CLI creates the function and writes its `func_id` into that directory's `func.toml` — a one-time setup step, not a CI step). The committed root `func.toml` is the staging config — one file, one source of truth, doubling as the default for local and manual `telnyx-edge ship` runs — and only the production job overwrites it with `cp deploy/func.production.toml func.toml`, so the staging and production configurations can never drift. The workflow triggers on `main` and `v*` tags (the `on:` block in the GitHub Actions example above); with only `branches: [main]`, the production job's tag condition would never match and only staging would ever deploy. These two steps replace the baseline example's Deploy function job — they are not added alongside it. Each job authenticates by running `telnyx-edge auth api-key set "$TELNYX_API_KEY"` before `telnyx-edge ship` — the CLI does not read `TELNYX_API_KEY` from the environment. Hosted CI runners are ephemeral, so the key's on-disk config lasts only for the job; on self-hosted or persistent runners, provision the key per job from that job's secret and clear it afterwards (`telnyx-edge auth api-key clear`) — the CLI has no stdin or config-file auth option:

```yaml
# .github/workflows/deploy.yml — staging on main, production on v* tags
- name: Ship the staging function
  if: github.ref == 'refs/heads/main'
  env:
    TELNYX_API_KEY: ${{ secrets.TELNYX_API_KEY_STAGING }}
  run: |
    telnyx-edge auth api-key set "$TELNYX_API_KEY"
    telnyx-edge ship

- name: Ship the production function
  if: startsWith(github.ref, 'refs/tags/v')
  env:
    TELNYX_API_KEY: ${{ secrets.TELNYX_API_KEY_PRODUCTION }}
  run: |
    telnyx-edge auth api-key set "$TELNYX_API_KEY"
    cp deploy/func.production.toml func.toml
    telnyx-edge ship
```

Because bindings are declared in `func.toml`, both configs can also point at per-environment resources — for example a separate [KV](kv--part-1.md) namespace id per environment. If staging and production live in different Telnyx accounts, store one API key secret per account and reference the right one in each job, as above. Alternatively, keep one function directory per environment and ship each with `telnyx-edge ship --from-dir=<path>`. Set `timeout-minutes` on each job so a stalled upload fails the job quickly instead of hanging the runner until the default six-hour job timeout.

### Rollbacks

Every `telnyx-edge ship` produces an immutable revision. List a function's deploy history (newest first; the revision currently serving traffic is marked with `*`):

```
telnyx-edge revisions list my-func
```

To roll back — production or staging — retarget traffic to a previous revision (instant; no rebuild, no re-upload):

```
telnyx-edge rollback my-func a1b2c3d
```

Rollback switches traffic across all clusters instantly and leaves your Git working tree untouched; the next `ship` deploys whatever is on disk as a new revision. The target revision must have reached `deploy_ok` — `revisions list` shows each revision's deploy status. To roll forward again, `ship` again or `rollback` to another healthy revision. (`telnyx-edge deployments my-func` lists the same function's deploy events.) See [Versions & Rollback](https://developers.telnyx.com/docs/edge-compute/configuration/versions).

Git-based redeploys also work for code changes — `git revert` plus a push to `main` for staging, or a new `v*` tag for production — but they re-upload and re-validate instead of instantly restoring traffic.

### Health Checks

Add a health check step after deployment to detect issues:

```yaml
- name: Health check
  run: |
    for i in $(seq 1 10); do
      STATUS=$(curl -s --max-time 10 -o /dev/null -w "%{http_code}" https://{func-name}-{func-id-prefix}.telnyxcompute.com/health/readiness)
      if [ "$STATUS" = "200" ]; then
        echo "Health check passed (attempt $i)"
        exit 0
      fi
      sleep 5
    done
    echo "Health check failed after 10 attempts (last status: $STATUS)"
    exit 1
```

### Secrets Management

- **GitHub Actions**: Settings → Secrets and variables → Actions → New repository secret
- **GitLab CI**: Settings → CI/CD → Variables (add as masked variable)
- Give each pipeline job its own API key secret, as in the staging and production jobs above; use separate API keys per account only when staging and production live in different Telnyx accounts

### Deployment Notifications

Integrate Slack notifications using `slackapi/slack-github-action` to report deployment status, commit SHA, and branch name.

### Best Practices

- **Branch protection**: Require CI to pass and PR reviews before merging
- **Deployment frequency**: Dev on feature branches, staging on merge to `main`, production on `v*` version tags
- **Monitoring**: After deployment, monitor invocation metrics, error rates, response latency, and cold start frequency (see [Edge Compute Observability](telnyx-edge-compute--part-3.md))

### Troubleshooting

- **Authentication errors**: Verify the `TELNYX_API_KEY` secret is set correctly and has Edge Compute permissions
- **Build failures**: Check `func.toml` configuration and dependency versions
- **Deployment timeouts**: Verify function size is within platform limits and retry with `--verbose`

## Framework Support

Framework auto-detection and adapters for popular web frameworks are in development. This will enable deploying framework-based applications to Edge Compute with minimal changes.

## Related Resources

- [Edge Compute Quickstart](telnyx-edge-compute--part-1.md) — Deploy your first function
- [Edge Compute CLI Reference](telnyx-edge-compute--part-3.md) — Full command documentation
- [Edge Compute Examples](edge-compute-development-guide--part-2.md) — Code snippets and patterns
- [Edge Compute Observability](telnyx-edge-compute--part-3.md) — Monitor deployments
- [Edge Compute Runtime](telnyx-edge-compute--part-2.md) — Execution environment details
- [Edge Compute Limits](telnyx-edge-compute--part-3.md) — Platform resource limits
