---
title: Edge Compute Development and CI/CD
summary: An end-to-end guide to building, running locally, configuring, and deploying
  Telnyx Edge Compute functions with the CLI and CI/CD—covering environment variables,
  secrets, routing, versioning, health checks, and known "coming soon" features.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/development
  content_hash: 64ec83b81b366ca746d8b12342702bad3df6b4656a73ab74ed35d65b65b6afed
- url: https://developers.telnyx.com/docs/edge-compute/deploy
  content_hash: 640fccf85eddb2a3173f8de57fcba41dda9ee390b5ff2a5f77fdc0c7987411cc
- url: https://developers.telnyx.com/docs/edge-compute/quickstart/index
  content_hash: 5b0ca73a289f247dcc4975ce432443b9a915ab51d474934775ad023902e1cc30
- url: https://developers.telnyx.com/docs/edge-compute/configuration/index
  content_hash: a76cae2bdd7825206bfae765d9f8f86774c471716ba3dc8f08f4af0f967b4123
- url: https://developers.telnyx.com/docs/edge-compute/configuration/environment-variables
  content_hash: 04144a7958a3b1dd19229714f69847fbd5e9743ddb0b89c68a5952a72c133d46
- url: https://developers.telnyx.com/docs/edge-compute/configuration/secrets
  content_hash: b59a20493aba4087bde0865e54b4084e4e69f1f52044c17847bd88fd25ec27c0
- url: https://developers.telnyx.com/docs/edge-compute/configuration/cron-triggers
  content_hash: 3d449ed8fdd8c7020d14c829c9c5b5a06683c86d6c28013c442cc2ed3b3cffd1
- url: https://developers.telnyx.com/docs/edge-compute/configuration/routing
  content_hash: 93fed130fbaf18e475091b93b5b01fabb9ed596fbba09a7ee014a8078e8fefbe
- url: https://developers.telnyx.com/docs/edge-compute/configuration/versions
  content_hash: e14d9a7d869b8a12b1267f887637eb63440d1f404b65381c984bc0c97df9fc43
- url: https://developers.telnyx.com/docs/edge-compute/testing/index
  content_hash: b08788ca96f7c435997f177a2bebdc682bce580145f9bbc619d1c49f4b8ca8a2
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
