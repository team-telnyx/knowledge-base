---
title: Telnyx Edge Compute — Developer Guide
summary: 'A concise, end-to-end guide to Telnyx Edge Compute: architecture, setup,
  configuration, runtime model, bindings, KV storage, best practices, CI/CD, limits,
  and what’s coming next.'
sources:
- url: https://developers.telnyx.com/docs/edge-compute/best-practices
  content_hash: 7b3fb7e4f5524b7cba6e9e0530959a8f9873ae82c5f0923b90029f018b887453
- url: https://developers.telnyx.com/docs/edge-compute/configuration
  content_hash: a35cf8fc926cd34c587123eaac411cfc2376d8d35bf79a7182b5ea4bc46b4c7d
- url: https://developers.telnyx.com/docs/edge-compute/configuration/cron-triggers
  content_hash: f526ae7609d9936069ab66a27aaee1e73642156e31daa909b506fe3d87395958
- url: https://developers.telnyx.com/docs/edge-compute/configuration/environment-variables
  content_hash: f4c4fbf7795dd1c9c65271cf25ede227bd1916ef8d1804cd1581003a11c2a69d
- url: https://developers.telnyx.com/docs/edge-compute/configuration/routing
  content_hash: f557e78257201cad46963554f836b7e413aced35a02b8abaf28ca2b9b141ff18
- url: https://developers.telnyx.com/docs/edge-compute/configuration/secrets
  content_hash: fc928e535154be6661b93daee6902d5b5506c57bc9a6f2189ff7a2bbfc74c6ce
- url: https://developers.telnyx.com/docs/edge-compute/configuration/versions
  content_hash: ac0f646bf3a335ac7e1c95a79f29844a83b15e0f2f55e030bcb1f17d8af15ffb
- url: https://developers.telnyx.com/docs/edge-compute/demos
  content_hash: 5ea65ece207f150aff2863d1253518a472c63bd2dc715d4c7b3a7e12794df16a
- url: https://developers.telnyx.com/docs/edge-compute/demos/build-a-rest-api
  content_hash: e765fba7ddff7436cd737dcdd5023e103d29f768abc3dbaf48ddc656651e115a
- url: https://developers.telnyx.com/docs/edge-compute/demos/image-resizer
  content_hash: ec0c36e94f27fff4cef95fbb395e5640b645b7c56ec90a8ee62f8568407a2caa
- url: https://developers.telnyx.com/docs/edge-compute/demos/sms-webhook-handler
  content_hash: 28105ddde5f22d2415da1b661df668558d597ef0f292a1a00529acc2ffd1b7d5
- url: https://developers.telnyx.com/docs/edge-compute/demos/voice-call-router
  content_hash: 753a96661329d8b0d80ded53a20dc50c27c0bda083510a0683a02a3ef759941e
- url: https://developers.telnyx.com/docs/edge-compute/deploy
  content_hash: 7e1e9f5abaa01d2a8c01013e934c94a791d74b86ccbbb98556d3ba89a7a33478
- url: https://developers.telnyx.com/docs/edge-compute/development
  content_hash: de8bd0104bbdd2920ddd2521e75dfbedd39e50cf8e628e0592b646e3a4df5797
- url: https://developers.telnyx.com/docs/edge-compute/examples
  content_hash: 880d35158e87ce0300bbd63103f0009f2c48c3f157c601612ebc9440c8959aea
- url: https://developers.telnyx.com/docs/edge-compute/frameworks
  content_hash: 7d7e65f9f9897d0f761c5dd5478fd6bf8118d3a2a13adfd6785108c43d89a51b
- url: https://developers.telnyx.com/docs/edge-compute/frameworks-support
  content_hash: a589c5f6ddc27e3e08fe75cbd247172dc89ba136ec295da1fea1fcdc8d889839
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/global-api-gateway
  content_hash: feb19f82c850c67839e62558955e8d490b00a9691878b900622e4a3de116ac15
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/iot-data-ingestion
  content_hash: e5a589bf41837d330bcd37a282528d74f0862208f56b05669a4f533667a68c65
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/real-time-media-pipeline
  content_hash: 64d024d16fda5f13581ce2e2d9cd85d7fd69a1e02b775f56b9b99b347466b5f9
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/telecom-event-processor
  content_hash: e2fca500731fca2b0229eed00d88f3455bdb35dbcdb780dcd923bdec983840f4
- url: https://developers.telnyx.com/docs/edge-compute/kv/api-reference
  content_hash: 9e592a2bf61e4d9097ca597d57622db0fcb1d4ca7d81f123f073e614ff3d5faa
- url: https://developers.telnyx.com/docs/edge-compute/kv/cli
  content_hash: cef46af7e62fcf59bff692b0708a78fa50b344b7d9d65142cc094c29760737fa
- url: https://developers.telnyx.com/docs/edge-compute/kv/pricing
  content_hash: aceb7fbcdcd8fc828cb4e8d0fb48e1e8c2b30c7e799c3eb4ddc47ccba2ce4be5
- url: https://developers.telnyx.com/docs/edge-compute/kv/quick-start
  content_hash: 6ac32f6799480ec2a8b2f156f813bd0551b12ec529fbc22c48cdf8bdf4e08204
- url: https://developers.telnyx.com/docs/edge-compute/kv/ttl-and-metadata
  content_hash: 5bcc7143f0bb8c933d6f9ac581c9f46ff0a614b988fc4e90b9bc33183c903762
- url: https://developers.telnyx.com/docs/edge-compute/kv/use-cases
  content_hash: 8ac2275f85cf764b9da32880e0369003695489e081a7b4a30494763c2c8ef79c
- url: https://developers.telnyx.com/docs/edge-compute/network
  content_hash: 6cb6dc9923a84ff85600c722a2659ccf843c4629973c777d97863266be5900aa
- url: https://developers.telnyx.com/docs/edge-compute/observability
  content_hash: 4eaee9817259a0b7da73dbbe24d2f4fceae0b43c9a86c8bcce8aedea7fee73e9
- url: https://developers.telnyx.com/docs/edge-compute/overview
  content_hash: 2b963aed72f0fddd44f3d0f9a698af6838f905f15eb77ab55453e25fc2a477ce
- url: https://developers.telnyx.com/docs/edge-compute/platform-overview
  content_hash: 84a7e22ec65304624462300a6ca97fd543b43e4c9f1a9eb28fddfb953d95dffa
- url: https://developers.telnyx.com/docs/edge-compute/products
  content_hash: cd26142c6ba038b6171f2f4fcb3bbbc7b14e6ec66b0ddc7163dd50c8773b0f06
- url: https://developers.telnyx.com/docs/edge-compute/quickstart
  content_hash: d31989b7a4bcaa90c956bfc3f0b6ac483753983345f53fd5a55a0357d91a9b1c
- url: https://developers.telnyx.com/docs/edge-compute/reference/architecture
  content_hash: b54771dd5fac92eba49cabe366712956b5a829deba47500b91e9d97f58c86d4b
- url: https://developers.telnyx.com/docs/edge-compute/reference/cli
  content_hash: 49aae6d4a62af4c43683e58a13f2ce1d2a6869de3d9f41425418a52b394526cd
- url: https://developers.telnyx.com/docs/edge-compute/reference/limits
  content_hash: 25e024949cb9051b3a8289f1b56910872db0fad2d742aba7317126c21902c513
- url: https://developers.telnyx.com/docs/edge-compute/runtime
  content_hash: 31622c04a8e1fa69b21ad762e43fef34048cddc891adbce8d25d78c9f939c6d8
- url: https://developers.telnyx.com/docs/edge-compute/runtime/bindings
  content_hash: 5d817b89c436ba643e98dce96930874fe373aa3c5b7d7e16905de08655237f80
- url: https://developers.telnyx.com/docs/edge-compute/runtime/execution-model
  content_hash: 6e86826e8fbacef6c19a57672d90da01d08644a571e433481527ff992f720b6d
- url: https://developers.telnyx.com/docs/edge-compute/sqldb
  content_hash: 0d230cd6514b60d5fff971d6c9b516c9f5cc70679482b6bd2caa35be9a33b147
- url: https://developers.telnyx.com/docs/edge-compute/testing
  content_hash: 5315563a13131f228a0834769a288c98e7b41a6f7e5f695a5ca45a7633de5564
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
