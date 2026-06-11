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
updated_at: 2026-06-11T10:26:49Z
---

# Edge Compute Development Guide

*Part 3 of 3 — see also: [Part 1](edge-compute-development-guide--part-1.md), [Part 2](edge-compute-development-guide--part-2.md)*

A comprehensive guide to building, testing, and deploying serverless functions on Telnyx Edge Compute — covering local development workflows, step-by-step tutorials for common applications, reusable code snippets across multiple languages, production-grade reference architectures, and CI/CD deployment pipelines.

## Deployment

Automate Edge Compute deployments with CI/CD pipelines.

### Authentication

CI/CD pipelines need a Telnyx API key with Edge Compute permissions. Create a deployment key in the [Telnyx Portal](https://portal.telnyx.com) and store it as a secret in your CI/CD platform — never commit API keys to your repository.

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
        run: telnyx-edge ship
```

To run tests before deploying, add a separate `test` job that the `deploy` job depends on (`needs: test`), with an `if: github.ref == 'refs/heads/main'` guard so deploys only run on the main branch.

### GitLab CI

Use a two-stage pipeline (`test`, `deploy`) with the deploy stage restricted to the `main` branch. Download and install the CLI in the deploy script, and set `TELNYX_API_KEY` as a CI variable.

### CircleCI

Define `test` and `deploy` jobs with a workflow that requires test to pass and filters to the `main` branch. Install the CLI in the deploy job and run `telnyx-edge ship`.

### Environment Promotion

Deploy to different environments using branches or tags. Map the `staging` branch to dev and the `main` branch or `v*` tags to production using separate API key secrets:

```yaml
- name: Deploy to dev
  if: github.ref == 'refs/heads/staging'
  env:
    TELNYX_API_KEY: ${{ secrets.TELNYX_API_KEY_DEV }}
  run: telnyx-edge ship --env dev

- name: Deploy to production
  if: github.ref == 'refs/heads/main' || startsWith(github.ref, 'refs/tags/v')
  env:
    TELNYX_API_KEY: ${{ secrets.TELNYX_API_KEY_PRODUCTION }}
  run: telnyx-edge ship --env prod
```

### Rollbacks

Redeploy a previous Git commit:

```
git revert HEAD
git push origin main
```

Or checkout a specific commit and deploy:

```
git checkout <previous-commit-sha>
telnyx-edge ship
git checkout main
```

Version history and CLI rollback commands are coming soon.

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
- Use different API keys per environment with conditional expressions

### Deployment Notifications

Integrate Slack notifications using `slackapi/slack-github-action` to report deployment status, commit SHA, and branch name.

### Best Practices

- **Branch protection**: Require CI to pass and PR reviews before merging
- **Deployment frequency**: Dev on feature branches, staging on merge to `staging`, production on merge to `main` or version tags
- **Monitoring**: After deployment, monitor invocation metrics, error rates, response latency, and cold start frequency (see [Edge Compute Observability](edge-compute-observability.md))

### Troubleshooting

- **Authentication errors**: Verify the `TELNYX_API_KEY` secret is set correctly and has Edge Compute permissions
- **Build failures**: Check `func.toml` configuration and dependency versions
- **Deployment timeouts**: Verify function size is within platform limits and retry with `--verbose`

## Framework Support

Framework auto-detection and adapters for popular web frameworks are in development. This will enable deploying framework-based applications to Edge Compute with minimal changes.

## Related Resources

- [Edge Compute Quickstart](edge-compute-quickstart.md) — Deploy your first function
- [Edge Compute CLI Reference](edge-compute-cli-reference.md) — Full command documentation
- [Edge Compute Examples](edge-compute-examples.md) — Code snippets and patterns
- [Edge Compute Observability](edge-compute-observability.md) — Monitor deployments
- [Edge Compute Runtime](edge-compute-runtime.md) — Execution environment details
- [Edge Compute Limits](edge-compute-limits.md) — Platform resource limits
