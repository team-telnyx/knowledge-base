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
updated_at: 2026-11-12T19:19:15Z
---

# Edge Compute Development Guide

*Part 3 of 3 — see also: [Part 1](edge-compute-development-guide--part-1.md), [Part 2](edge-compute-development-guide--part-2.md)*

A comprehensive guide to building, testing, and deploying serverless functions on Telnyx Edge Compute — covering local development workflows, step-by-step tutorials for common applications, reusable code snippets across multiple languages, production-grade reference architectures, and CI/CD deployment pipelines.

## Deployment

Automate Edge Compute deployments with CI/CD pipelines.

### Authentication

CI/CD pipelines need a Telnyx API key with Edge Compute permissions. Create a deployment key in the [Telnyx Portal](https://portal.telnyx.com) and store it as a secret in your CI/CD platform — never commit API keys to your repository. The CLI does not read `TELNYX_API_KEY` from the environment — each pipeline job must run `telnyx-edge auth api-key set "$TELNYX_API_KEY"` before `telnyx-edge ship`.

### GitHub Actions

Deploy on every push to `main`:

```yaml
# .github/workflows/deploy.yml
name: Deploy Edge Function

on:
  push:
    branches: [main]

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
        env:
          TELNYX_API_KEY: ${{ secrets.TELNYX_API_KEY }}
        run: |
          telnyx-edge auth api-key set "$TELNYX_API_KEY"
          telnyx-edge ship
```

To run tests before deploying, add a separate `test` job that the `deploy` job depends on (`needs: test`), with an `if: github.ref == 'refs/heads/main'` guard so deploys only run on the main branch.

### GitLab CI

Use a two-stage pipeline (`test`, `deploy`) with the deploy stage restricted to the `main` branch. Download and install the CLI in the deploy script, set `TELNYX_API_KEY` as a CI variable, and run `telnyx-edge auth api-key set "$TELNYX_API_KEY"` before `telnyx-edge ship`.

### CircleCI

Define `test` and `deploy` jobs with a workflow that requires test to pass and filters to the `main` branch. Install the CLI in the deploy job and run `telnyx-edge auth api-key set "$TELNYX_API_KEY"` before `telnyx-edge ship`.

### Staging and production

There is no environment flag and no environment promotion: `telnyx-edge ship` always deploys the function that `func.toml` names. Environments are separate functions — for example `my-api-staging` and `my-api` — each with its own URL and bindings. Register each environment's function once with `telnyx-edge new-func -l=ts -n=my-api-staging` (the CLI creates the function and writes its `func_id` into that directory's `func.toml` — a one-time setup step, not a CI step), then check in both `deploy/func.staging.toml` and `deploy/func.production.toml` and have each pipeline job copy the matching one over the root `func.toml` before shipping (the checked-in root `func.toml` is the staging config — the default for local and manual `telnyx-edge ship` runs). Also add `tags: ['v*']` to `on.push` alongside `branches: [main]`; with only `branches: [main]`, the production job's tag condition never matches and only staging ever deploys. Each job authenticates by running `telnyx-edge auth api-key set "$TELNYX_API_KEY"` before `telnyx-edge ship` — the CLI does not read `TELNYX_API_KEY` from the environment (CI runners are ephemeral, so the stored key's on-disk config is acceptable):

```yaml
# .github/workflows/deploy.yml — staging on main, production on v* tags
- name: Ship the staging function
  if: github.ref == 'refs/heads/main'
  env:
    TELNYX_API_KEY: ${{ secrets.TELNYX_API_KEY_STAGING }}
  run: |
    telnyx-edge auth api-key set "$TELNYX_API_KEY"
    cp deploy/func.staging.toml func.toml
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

Because bindings are declared in `func.toml`, the two files can also point at per-environment resources — for example a separate [KV](kv--part-1.md) namespace id per environment. If staging and production live in different Telnyx accounts, store one API key secret per account and reference the right one in each job, as above. Alternatively, keep one function directory per environment and ship each with `telnyx-edge ship --from-dir=<path>`. Set `timeout-minutes` on each job so a stalled upload fails the job quickly instead of hanging the runner until the default six-hour job timeout.

### Rollbacks

Redeploy a previous Git commit. To roll back staging, revert and push to `main` — the staging job redeploys on every merge to `main`:

```
git revert HEAD
git push origin main
```

Or check out a specific older commit and redeploy staging from it — the committed root `func.toml` is the staging config, so copy it into place explicitly:

```
git checkout <previous-good-commit-sha>
cp deploy/func.staging.toml func.toml
telnyx-edge ship
git checkout main
```

To roll back production, push a new `v*` tag at the last known-good commit so the production job redeploys it. The production job copies `deploy/func.production.toml` into place itself, and pushing to `main` never touches production:

```
git tag -a v1.2.4 <previous-good-commit-sha>
git push origin v1.2.4
```

(An older checkout that predates the two-config layout has no `deploy/` file to copy, so the `cp` step fails the run instead of silently shipping the wrong environment.) Version history and CLI rollback commands are coming soon.

### Health Checks

Add a health check step after deployment to detect issues:

```yaml
- name: Health check
  run: |
    sleep 10
    STATUS=$(curl -s -o /dev/null -w "%{http_code}" https://my-function-abc123.telnyxcompute.com/health)
    if [ "$STATUS" != "200" ]; then
      echo "Health check failed!"
      exit 1
    fi
```

### Secrets Management

- **GitHub Actions**: Settings → Secrets and variables → Actions → New repository secret
- **GitLab CI**: Settings → CI/CD → Variables (add as masked variable)
- Give each pipeline job its own API key secret, as in the staging and production jobs above; use separate API keys per account only when staging and production live in different Telnyx accounts

### Deployment Notifications

Integrate Slack notifications using `slackapi/slack-github-action` to report deployment status, commit SHA, and branch name.

### Best Practices

- **Branch protection**: Require CI to pass and PR reviews before merging
- **Deployment frequency**: Dev on feature branches, staging on merge to `main`, production on `v*` tags
- **Monitoring**: After deployment, monitor invocation metrics, error rates, response latency, and cold start frequency (see [Edge Compute Observability](edge-compute-observability.md))

### Troubleshooting

- **Authentication errors**: Verify the `TELNYX_API_KEY` secret is set correctly and has Edge Compute permissions
- **Build failures**: Check `func.toml` configuration and dependency versions
- **Deployment timeouts**: Verify function size is within platform limits and retry with `--verbose`

## Framework Support

Framework auto-detection and adapters for popular web frameworks are in development. This will enable deploying framework-based applications to Edge Compute with minimal changes.

## Related Resources

- [Edge Compute Quickstart](edge-compute-quickstart.md) — Deploy your first function
- [Edge Compute CLI Reference](telnyx-edge-compute--part-3.md) — Full command documentation
- [Edge Compute Examples](edge-compute-examples.md) — Code snippets and patterns
- [Edge Compute Observability](edge-compute-observability.md) — Monitor deployments
- [Edge Compute Runtime](edge-compute-runtime.md) — Execution environment details
- [Edge Compute Limits](edge-compute-limits.md) — Platform resource limits
