---
title: Telnyx Edge Compute — Developer Guide
summary: 'A concise, end-to-end guide to Telnyx Edge Compute: architecture, setup,
  configuration, runtime model, bindings, KV storage, best practices, CI/CD, limits,
  and what’s coming next.'
sources:
- url: https://developers.telnyx.com/docs/edge-compute/best-practices
- url: https://developers.telnyx.com/docs/edge-compute/configuration
- url: https://developers.telnyx.com/docs/edge-compute/configuration/cron-triggers
- url: https://developers.telnyx.com/docs/edge-compute/configuration/environment-variables
- url: https://developers.telnyx.com/docs/edge-compute/configuration/routing
- url: https://developers.telnyx.com/docs/edge-compute/configuration/secrets
- url: https://developers.telnyx.com/docs/edge-compute/configuration/versions
- url: https://developers.telnyx.com/docs/edge-compute/demos
- url: https://developers.telnyx.com/docs/edge-compute/demos/build-a-rest-api
- url: https://developers.telnyx.com/docs/edge-compute/demos/image-resizer
- url: https://developers.telnyx.com/docs/edge-compute/demos/sms-webhook-handler
- url: https://developers.telnyx.com/docs/edge-compute/demos/voice-call-router
- url: https://developers.telnyx.com/docs/edge-compute/deploy
- url: https://developers.telnyx.com/docs/edge-compute/development
- url: https://developers.telnyx.com/docs/edge-compute/examples
- url: https://developers.telnyx.com/docs/edge-compute/frameworks
- url: https://developers.telnyx.com/docs/edge-compute/frameworks-support
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/global-api-gateway
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/iot-data-ingestion
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/real-time-media-pipeline
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/telecom-event-processor
- url: https://developers.telnyx.com/docs/edge-compute/kv/api-reference
- url: https://developers.telnyx.com/docs/edge-compute/kv/cli
- url: https://developers.telnyx.com/docs/edge-compute/kv/pricing
- url: https://developers.telnyx.com/docs/edge-compute/kv/quick-start
- url: https://developers.telnyx.com/docs/edge-compute/kv/ttl-and-metadata
- url: https://developers.telnyx.com/docs/edge-compute/kv/use-cases
- url: https://developers.telnyx.com/docs/edge-compute/network
- url: https://developers.telnyx.com/docs/edge-compute/observability
- url: https://developers.telnyx.com/docs/edge-compute/overview
- url: https://developers.telnyx.com/docs/edge-compute/platform-overview
- url: https://developers.telnyx.com/docs/edge-compute/products
- url: https://developers.telnyx.com/docs/edge-compute/quickstart
- url: https://developers.telnyx.com/docs/edge-compute/reference/architecture
- url: https://developers.telnyx.com/docs/edge-compute/reference/cli
- url: https://developers.telnyx.com/docs/edge-compute/reference/limits
- url: https://developers.telnyx.com/docs/edge-compute/runtime
- url: https://developers.telnyx.com/docs/edge-compute/runtime/bindings
- url: https://developers.telnyx.com/docs/edge-compute/runtime/execution-model
- url: https://developers.telnyx.com/docs/edge-compute/sqldb
- url: https://developers.telnyx.com/docs/edge-compute/testing
updated_at: 2026-05-14T09:47:40Z
---

# Telnyx Edge Compute — Developer Guide

*Part 1 of 2 — see also: [Part 2](telnyx-edge-compute-developer-guide--part-2.md)*

A concise, end-to-end guide to Telnyx Edge Compute: architecture, setup, configuration, runtime model, bindings, KV storage, best practices, CI/CD, limits, and what’s coming next.

## What is Telnyx Edge Compute
A serverless platform running your code in real Linux containers across Telnyx’s global edge. You get native runtimes (Python, Go, Node.js, Java/Quarkus), a full POSIX environment, and automatic scaling. See [Edge Compute](edge-compute.md) and [Architecture](architecture.md).

Highlights:
- Global, low-latency PoPs with carrier-grade redundancy
- Native language support and standard libraries (not V8 isolates)
- Auto-scaling with warm containers when traffic is sustained
- Simple usage-based pricing; see [Edge Compute](edge-compute.md) for request/CPU pricing

## Install and deploy a Hello World
1) Install CLI: see [Edge Compute Quick Start](edge-compute-quick-start.md) or [CLI Reference](cli-reference.md)
2) Authenticate: `telnyx-edge auth login` (OAuth) or set an API key
3) Scaffold a function: `telnyx-edge new-func -l=python -n=hello-world`
4) Deploy: `telnyx-edge ship`
5) Test: functions are live at `https://{funcName}-{orgId}.telnyxcompute.com` (dev URLs use `.dev.telnyxcompute.com`)

## Configure your function
Use `func.toml` to define name, timeouts, environment variables, and bindings. See [Configuration](configuration.md).
- Environment variables: declare under `[env_vars]` and access via your language runtime. Use for non-sensitive config. See [Environment Variables](environment-variables.md).
- Secrets: add via CLI (`telnyx-edge secrets add NAME "value"`); injected as env vars at runtime for sensitive data. Rotate regularly. See [Secrets](secrets.md).
- Timeouts: set in `func.toml` (default 30s; max per [Limits](limits.md)). Keep internal timeouts slightly below platform limits.
- Naming: choose descriptive `func_name` (it’s part of the public URL).

## Runtime and execution model
Edge Compute runs functions in lightweight containers. Each container handles one request at a time and stays warm for a period to reduce latency. See [Execution Model](execution-model.md).
- Containers vs isolates: native runtimes, filesystem access, and broader dependency support; cold starts are typically higher than isolates but optimized by keeping code small and initialization lazy.
- Lifecycle: routing → container selection (warm or cold) → execution → response → keep-alive.
- Graceful shutdown: handle termination signals to close connections and flush buffers.

## Bindings (secure Telnyx API access)
Bindings let you call Telnyx APIs without hardcoding keys. See [Bindings](bindings.md).
- Your function receives `TELNYX_BASE_URL` (binding proxy) and `TELNYX_API_KEY` (JWT for the proxy) as env vars.
- Always call `${TELNYX_BASE_URL}/v2/...` with `Authorization: Bearer ${TELNYX_API_KEY}`. Do not call `https://api.telnyx.com` directly with the binding JWT.
- Manage once per org: `telnyx-edge bindings create | validate | update | delete`.
- Cloud Storage caveat: S3-compatible endpoints do not accept the binding JWT. Store a real API key as a secret (e.g., `TELNYX_STORAGE_KEY`) for S3 operations.

## Key-Value (KV) storage
Low-latency key-value storage for sessions, caching, and flags. Start with [KV Quick Start](kv-quick-start.md) and [KV API Reference](kv-api-reference.md).
- Create a namespace: CLI or API. Wait until status is `provision_ok`.
- Bind to your function in `func.toml` (e.g., `[storage.kv.MY_CACHE]`), which injects `KV_MY_CACHE_ID` as an env var.
- Access via REST today; SDKs and KV bindings are coming. Values are base64-encoded; serialize complex data as JSON first.
- TTL and metadata: set `expiration_ttl` (min 60s) or `expiration` (Unix timestamp), and optional JSON `metadata`. See [KV TTL & Metadata](kv-ttl-metadata.md).
- Manage keys/namespaces with `telnyx-edge storage kv ...`. See [KV CLI](kv-cli.md).
- Pricing and free tier: see [KV Pricing](kv-pricing.md).

## Performance best practices
See [Best Practices](best-practices.md) and [Execution Model](execution-model.md).
- Reuse connections: initialize HTTP/DB clients once at module/package level; pool connections.
- Minimize cold starts: lazy-load heavy deps, keep functions small, prefer lightweight frameworks.
- Cache with KV: store expensive computation/API results with appropriate TTLs.
- Keep handlers fast (<100ms p99 when possible); push slow/periodic work to scheduled invocations or background systems.

## Reliability patterns
- Error handling: return structured errors with proper status codes and include a request ID when available.
- Timeouts on outbound calls: set explicit timeouts and abort on slow dependencies to avoid hanging containers.
- Retries with backoff: retry transient 5xx/connection errors; do not retry 4xx client errors.

## Security recommendations
- Validate and sanitize all input; enforce required fields and formats.
- Use HTTPS for all external calls.
- Don’t log secrets or full request bodies that may include PII.
- Store sensitive config in [Secrets](secrets.md); use env vars only for non-sensitive values. Consider regular secret rotation.

## Observability
- Request IDs: generate or forward `X-Request-ID` and echo it in logs and responses.
- Log levels: use debug/info/warn/error consistently and guard verbose logs behind `LOG_LEVEL`.
- Platform observability (logs, metrics, tracing) is coming soon; see [Observability](observability.md).

## Local development and testing
See [Local Development](local-development.md) and [Testing](testing.md).
- Use a `.env` file (gitignored) or shell exports for local env/secrets; in production, use Secrets and Bindings.
- Run and test with your language’s native tools (pytest, go test, JUnit, Jest). Since functions run in real containers, standard testing works well.
- Note differences from prod: no cold starts locally, different network, mocked bindings; check [Limits](limits.md) for production constraints.

## CI/CD and operations
See [CI/CD](ci-cd.md).
- Authenticate CI with a Telnyx API key secret; never commit keys.
- Typical workflow: checkout → install CLI → run tests → `telnyx-edge ship` → health check the live URL.
- Health checks: probe endpoints (e.g., `/health`) and fail the pipeline on non-200.
- Rollbacks: redeploy a previous Git commit (version history/rollback commands are coming soon).
- Environment promotion: target different org keys or flags per branch/tag.

## Routing, domains, and regions
See [Routes & Domains](routes-domains.md).
- Public URLs: `https://{funcName}-{orgId}.telnyxcompute.com` (dev: `...{orgId}.dev.telnyxcompute.com`).
- Custom domains: coming soon.
- Region placement/pinning: coming soon. Today, requests route to the nearest available edge location automatically.

## Versions and deployments
See [Versions & Deployments](versions-deployments.md).
- Current model: each `ship` fully replaces the previous deployment.
- Rollbacks: use Git (revert/checkout) and redeploy until native rollback is available.

## Platform limits (key excerpts)
Full details in [Limits](limits.md). Design within these constraints:
- Execution: 30s default timeout (up to 60s), CPU time up to 60s, request/response bodies up to 10 MB.
- Memory: 256 MB per container (up to 512 MB). Stream large data; avoid unbounded in-memory caches.
- Function size: ~50 MB compressed code+deps. Trim unused deps and split functions if needed.
- Network: up to 100 outbound connections per request; set outbound timeouts.
- Rate: up to 60 deployments/hour; API request rate limits apply. Platform auto-scales concurrency; spiky traffic may see cold starts.
- Storage (preview): KV key up to 512 bytes; value up to 25 MB; strong operational SLAs and quotas apply.
- Error semantics: exceeding limits yields 4xx/5xx (e.g., 504 timeout, 413 payload too large, 429 rate limited). Handle gracefully.
