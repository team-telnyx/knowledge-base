---
title: Telnyx Edge Compute — Developer Guide
summary: A concise, end-to-end guide to building, configuring, deploying, and operating
  serverless functions on Telnyx’s global edge. Covers runtime and execution model,
  configuration (env vars, secrets, bindings), routing, performance and reliability
  patterns, security guidance, KV storage, CI/CD, limits, tutorials, and upcoming
  features.
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
  content_hash: 0edaaa0b78f2afcc1c6cf202c7693658243394d6a191a96a582f9466ca11daa4
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
  content_hash: c5a6cf625195a1f599c110e3fba52f196e91c830ae16b853fbc52d3148ad3177
- url: https://developers.telnyx.com/docs/edge-compute/reference/architecture
  content_hash: b54771dd5fac92eba49cabe366712956b5a829deba47500b91e9d97f58c86d4b
- url: https://developers.telnyx.com/docs/edge-compute/reference/cli
  content_hash: 49aae6d4a62af4c43683e58a13f2ce1d2a6869de3d9f41425418a52b394526cd
- url: https://developers.telnyx.com/docs/edge-compute/reference/limits
  content_hash: 25e024949cb9051b3a8289f1b56910872db0fad2d742aba7317126c21902c513
- url: https://developers.telnyx.com/docs/edge-compute/runtime
  content_hash: 31622c04a8e1fa69b21ad762e43fef34048cddc891adbce8d25d78c9f939c6d8
- url: https://developers.telnyx.com/docs/edge-compute/runtime/bindings
  content_hash: d45211d6d9ea48f8a717d2f8a4b0b7083376b9afb921e4a659ec98ecf7caf8c5
- url: https://developers.telnyx.com/docs/edge-compute/runtime/execution-model
  content_hash: 6e86826e8fbacef6c19a57672d90da01d08644a571e433481527ff992f720b6d
- url: https://developers.telnyx.com/docs/edge-compute/sqldb
  content_hash: 0d230cd6514b60d5fff971d6c9b516c9f5cc70679482b6bd2caa35be9a33b147
- url: https://developers.telnyx.com/docs/edge-compute/testing
  content_hash: 5315563a13131f228a0834769a288c98e7b41a6f7e5f695a5ca45a7633de5564
updated_at: 2026-05-08T13:07:32Z
---

# Telnyx Edge Compute — Developer Guide

*Part 1 of 2 — see also: [Part 2](telnyx-edge-compute-developer-guide--part-2.md)*

A concise, end-to-end guide to building, configuring, deploying, and operating serverless functions on Telnyx’s global edge. Covers runtime and execution model, configuration (env vars, secrets, bindings), routing, performance and reliability patterns, security guidance, KV storage, CI/CD, limits, tutorials, and upcoming features.

## Platform at a glance
- What it is: A serverless platform that runs your code in real Linux containers on Telnyx’s global edge for low-latency APIs, webhooks, and real-time processing.
- Languages: JavaScript/TypeScript (Node), Python, Go, Java (Quarkus).
- Key advantages: Native runtimes (full POSIX), automatic scaling, proximity to users (carrier-grade PoPs), built-in integration with Telnyx Voice, Messaging, AI, and storage.
- Pricing (Edge Compute): Usage-based with free tier; see Overview for current request and CPU-time rates.

## Runtime and execution model
- Containers, not isolates: Your functions run in lightweight Linux containers with native language runtimes and standard libraries (file I/O, networking).
- Request flow: Nearest edge → TLS termination/routing → warm container (or cold start) → your handler → response.
- Concurrency: One request per container at a time; the platform scales horizontally with traffic.
- Cold starts: ~100–500ms typical. Reduce impact by lazy-initializing heavy code, minimizing dependencies, and reusing connections. Containers stay warm under steady load and recycle when idle or upon new deployments.
- Triggers: HTTP requests and Telnyx webhooks today; cron (scheduled) triggers are planned.

## Configuration and routing
- func.toml: Central configuration for a function (name, language, env vars, storage bindings). Deploy with `telnyx-edge ship`.
- Public URLs: `https://{funcName}-{orgId}.telnyxcompute.com` (and `.dev.telnyxcompute.com` for dev). Choose descriptive function names—they appear in URLs.
- Timeouts: Configure in your function config, but plan within platform limits (default 30s, max 60s per request). Keep internal timeouts slightly lower to leave buffer.
- Coming soon: Custom domains, region placement/pinning, version history & CLI rollbacks.

## Environment variables and secrets
- Environment variables
  - Define non-sensitive config in `[env_vars]` of `func.toml` (strings only). Parse types (bool/int) in code and provide defaults.
  - Use UPPER_SNAKE_CASE; validate and document expected values (e.g., LOG_LEVEL, API_BASE_URL, CACHE_TTL).
- Secrets
  - Store sensitive data (API keys, passwords, tokens) via `telnyx-edge secrets add ...`. Injected as environment variables at runtime; encrypted at rest and never echoed.
  - Rotate regularly (update secret → `ship` → verify). Prefer clear names like `STRIPE_API_KEY`, `JWT_SECRET`.
- When to use which
  - Env vars: non-sensitive settings and flags.
  - Secrets: credentials and anything confidential.

## Bindings to Telnyx services
- Purpose: Secure, auto-authenticated access to Telnyx APIs (Voice, Messaging, Numbers, Fax, Verify) and Cloud Storage without hardcoding credentials.
- Setup: `telnyx-edge bindings create` → `validate` → deploy. SDKs pick up `TELNYX_API_KEY` and `TELNYX_BASE_URL` automatically via the binding proxy.
- Storage bindings: Use S3-compatible libraries with the injected credentials for Telnyx Cloud Storage.
- Roadmap: KV and SQL DB bindings coming soon.
- Use bindings for Telnyx services; use Secrets for third-party credentials.

## Local development and testing
- Workflow: `new-func` → code locally (native tools) → test (unit/integration) → `ship`.
- Local env: Use shell exports or a `.env` file (gitignored). For secrets, mock with local env vars; set real values via Secrets in production.
- Testing: Use standard frameworks (pytest, Jest, go test, JUnit). Platform-level testing/staging tooling is planned.
- Manual request testing: Run local server or `telnyx-edge dev` (where available) and hit endpoints with curl/Postman.

## Performance optimization
- Reuse connections: Initialize HTTP/database clients once at module/package level and reuse for every request (connection pooling).
- Minimize cold starts:
  - Lazy-load heavy dependencies and models only when needed.
  - Keep handlers small and focused; reduce dependency bloat.
  - Prefer lightweight frameworks and avoid unnecessary global work.
- Cache expensive work: Use KV to cache API responses or computed data with TTLs; check cache first, then compute/fetch and store.

## Reliability patterns
- Defensive timeouts: Set explicit, conservative timeouts on all outbound calls (e.g., 5–10s) and keep below platform execution limits (~25s internal when platform is 30s).
- Retries with backoff: Retry transient failures (5xx/connection issues) with exponential backoff; never retry on 4xx client errors.
- Graceful error handling: Return informative HTTP statuses and JSON error bodies; include a request ID.
- Health checks: Expose a simple `/health` for CI/CD verification after deploys.

## Security guidance
- Validate input: Enforce required fields, types, and formats; sanitize values (trim, lowercase) before use.
- Always use HTTPS for outbound traffic; never call plaintext HTTP for sensitive data.
- Don’t log secrets or full payloads that could contain PII. Prefer request metadata and request IDs.
- Isolation: Each function runs in its own container with network/filesystem/process isolation. Use storage (KV, Cloud Storage) for persistence—don’t depend on in-memory state across requests or restarts.

## Observability and logging
- Platform features (logs, metrics, traces) are coming. Until then:
  - Generate/propagate a request ID and echo it in responses and downstream calls.
  - Use log levels (debug/info/warn/error) and make verbosity configurable via env vars.
  - Monitor cold-start frequency, latency, error rates via your CI logs and external monitoring.

## Storage: KV quick start
- What it is: Low-latency key-value storage with TTL and optional metadata. Access today via REST API or CLI; SDK and bindings are coming.
- Create a namespace: CLI `telnyx-edge storage kv create --name my-cache` or REST `POST /v2/storage/kvs`. Wait for `provision_ok`.
- Bind to your function: In `func.toml` under `[storage.kv.MY_CACHE]` (injects `KV_MY_CACHE_ID`).
- Read/write:
  - REST: `PUT /v2/storage/kvs/{id}/keys/{key}` with base64-encoded `value`, optional `expiration_ttl` (≥60s) and `metadata` (≤1KB). `GET` to read; returns base64 `value`, optional `metadata`, `expiration`.
  - CLI: `telnyx-edge storage kv key put|get|list|delete`.
- Patterns: Sessions with TTL, API response caching, feature flags. Use structured keys (e.g., `session:{id}`, `cache:api:{path}`) and JSON-serialize complex values.
- Pricing (KV): Free tier for reads/writes/storage; paid per million ops and per-GB-month; egress is free.

## CI/CD automation
- Authentication: Use a Telnyx API key with Edge permissions stored as a secret in your CI platform.
- GitHub Actions (example): checkout → install CLI → run tests → `telnyx-edge ship` → health check. Multi-language examples available.
- Promotions: Use branches/tags to target environments; store environment-specific API keys as CI secrets.
- Rollbacks: Re-deploy a previous commit (Git-based) until native versioned rollbacks land.
- Notifications: Send deployment status to Slack (or your tool of choice).

## Limits and quotas
- Execution (typical defaults): request timeout 30s (max 60s), memory ~256MB (up to 512MB). Request/response body ~10MB. Set internal timeouts with buffer.
- Network: Up to ~100 outbound connections per invocation; set per-request client timeouts; prefer pooled clients.
- Function/package: Compressed code size up to ~50MB; keep dependencies lean. Env vars per function and value sizes have caps—validate early.
- Rate limits: ~60 deployments/hour/org, ~1,000 API req/min; invocations auto-scale (expect some cold starts on sharp spikes).
- Storage (KV): Key ≤512B, value ≤25MB, high read/write throughput targets (see docs) and generous namespace/key counts coming online.
- When you exceed limits: Expect status codes like 504 (timeout), 413 (payload too large), 429 (rate limited). Handle gracefully and retry where appropriate.
