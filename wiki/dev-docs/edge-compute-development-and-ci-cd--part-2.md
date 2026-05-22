---
title: Edge Compute Development and CI/CD
summary: An end-to-end guide to building, running locally, configuring, and deploying
  Telnyx Edge Compute functions with the CLI and CI/CD—covering environment variables,
  secrets, routing, versioning, health checks, and known "coming soon" features.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/development
- url: https://developers.telnyx.com/docs/edge-compute/deploy
- url: https://developers.telnyx.com/docs/edge-compute/quickstart/index
- url: https://developers.telnyx.com/docs/edge-compute/configuration/index
- url: https://developers.telnyx.com/docs/edge-compute/configuration/environment-variables
- url: https://developers.telnyx.com/docs/edge-compute/configuration/secrets
- url: https://developers.telnyx.com/docs/edge-compute/configuration/cron-triggers
- url: https://developers.telnyx.com/docs/edge-compute/configuration/routing
- url: https://developers.telnyx.com/docs/edge-compute/configuration/versions
- url: https://developers.telnyx.com/docs/edge-compute/testing/index
updated_at: 2026-05-20T08:17:32Z
---

# Edge Compute Development and CI/CD

*Part 2 of 2 — see also: [Part 1](edge-compute-development-and-ci-cd--part-1.md)*

An end-to-end guide to building, running locally, configuring, and deploying Telnyx Edge Compute functions with the CLI and CI/CD—covering environment variables, secrets, routing, versioning, health checks, and known "coming soon" features.

## Best practices

- Keep parity with production (language/runtime and dependency versions; test with production-like payloads).
- Git ignore local artifacts (.env, caches, build outputs).
- Use health checks and monitoring after deploy.
- Require CI to pass before merges; run tests on all pull requests.
- Choose deployment frequency per environment (dev: per-commit; staging: on merge to staging; prod: on main/tags).

See [Best Practices](best-practices.md).

## Troubleshooting CI/CD

- Invalid API key: ensure TELNYX_API_KEY secret exists, is correctly named, and has Edge Compute permissions.
- Build failures: validate func.toml, verify dependencies and versions match CI runners.
- Deployment timeouts: confirm function size within limits, verify runner network, retry with --verbose; review [Edge Compute limits and quotas](edge-compute-limits-and-quotas.md).

## Related references

- [CLI Reference](cli-reference.md) — full CLI docs
- [Environment Variables](environment-variables.md) — define and use configuration
- [Edge Compute secrets management](edge-compute-secrets-management.md) — secure sensitive data
- [Routes & Domains](routes-domains.md) — URLs and access patterns
- [Edge Compute observability](edge-compute-observability.md) — monitor metrics, errors, latency
- [Runtime](runtime.md) and [Execution Model](execution-model.md) — platform interface and lifecycle
- [Edge Compute architecture](edge-compute-architecture.md) — deeper platform details
- [Edge Compute limits and quotas](edge-compute-limits-and-quotas.md) — sizes and quotas
- External: Documentation index (available pages): https://developers.telnyx.com/llms.txt
