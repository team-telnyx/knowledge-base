---
title: Edge Compute Development Guide
summary: A comprehensive guide to building, testing, and deploying serverless functions
  on Telnyx Edge Compute — covering local development workflows, step-by-step tutorials
  for common applications, reusable code snippets across multiple languages, production-grade
  reference architectures, and CI/CD deployment pipelines.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/demos/build-a-rest-api
  content_hash: 4a1165b9c15b973912d03e68c9ad878853f5d1c1484320b5749433de86b7ece2
- url: https://developers.telnyx.com/docs/edge-compute/demos/image-resizer
  content_hash: 17c212723566d69208c1ac7e7a72f39d2f466d2caf3358c12cfda36bdc44c58c
- url: https://developers.telnyx.com/docs/edge-compute/demos/index
  content_hash: e56b0f155ab6790479826995204e40f6a392e7c882bddd0ae9b0b1c7da3e9bc4
- url: https://developers.telnyx.com/docs/edge-compute/demos/sms-webhook-handler
  content_hash: e7d1d54e84876ec01362b96b513e8fafd6280af78da4b555e21fe05ec02d6cab
- url: https://developers.telnyx.com/docs/edge-compute/demos/voice-call-router
  content_hash: 657c1832646180e3a0103aeb096ab1263058d5f4679a1fbd8566f64fd08861c2
- url: https://developers.telnyx.com/docs/edge-compute/deploy
  content_hash: cb8da54f43bf1dff1d8eecbf9ba74ea0f082418b3783a70b04cc49a58c616d05
- url: https://developers.telnyx.com/docs/edge-compute/development
  content_hash: 43d9307d3ce0be3c1656163479d4a3245dc3a332b7369a9b5d092a600a1a73dd
- url: https://developers.telnyx.com/docs/edge-compute/examples/index
  content_hash: c0bea1a073c097b2890f57ffbed24fa6d075d278858d435b783b6b07da58d2d5
- url: https://developers.telnyx.com/docs/edge-compute/frameworks-support
  content_hash: 63295d41eb8c8e328b1b5b9e7c134eb572812291ed38b35f60f3db3b9f765266
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/global-api-gateway
  content_hash: 8d771d0d30f21f84f93d5a886f0006e31bc06369abbcd7e8cafe9e0a59b785ab
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/index
  content_hash: d277e2ae0c7db30f2c4869a5abecc838ac50b904c226ffb9182133200beb3276
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/iot-data-ingestion
  content_hash: 60c36bee09e516502b4cc4e66144e9853c4c6c2bba7d130749b6b3a82dc83596
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/real-time-media-pipeline
  content_hash: 284d7c5b36a8b8665786caa506fc33582e638221746af0745529330423ad7e02
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/telecom-event-processor
  content_hash: 5836ef1c324cc6d59a7e3a203e324549a39fc860065377a28e4e03a90ca2fec8
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
