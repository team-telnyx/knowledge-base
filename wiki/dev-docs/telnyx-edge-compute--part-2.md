---
title: Telnyx Edge Compute
summary: Telnyx Edge Compute is a serverless platform for deploying code across Telnyx's
  carrier-grade infrastructure, offering low latency, global distribution, and no
  infrastructure to manage. Functions run in real Linux containers with native language
  runtimes (Python, Go, Node.js, Java/Quarkus, TypeScript) and integrate directly
  with Telnyx Voice, Messaging, AI, and Storage services.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/network/index
- url: https://developers.telnyx.com/docs/edge-compute/observability/index
- url: https://developers.telnyx.com/docs/edge-compute/overview/index
- url: https://developers.telnyx.com/docs/edge-compute/platform-overview/index
- url: https://developers.telnyx.com/docs/edge-compute/products
- url: https://developers.telnyx.com/docs/edge-compute/quickstart/index
- url: https://developers.telnyx.com/docs/edge-compute/reference/architecture
- url: https://developers.telnyx.com/docs/edge-compute/reference/cli
- url: https://developers.telnyx.com/docs/edge-compute/reference/limits
- url: https://developers.telnyx.com/docs/edge-compute/runtime/bindings
- url: https://developers.telnyx.com/docs/edge-compute/runtime/execution-model
- url: https://developers.telnyx.com/docs/edge-compute/runtime/index
- url: https://developers.telnyx.com/docs/edge-compute/sqldb/index
- url: https://developers.telnyx.com/docs/edge-compute/testing/index
updated_at: 2026-06-11T10:27:59Z
---

# Telnyx Edge Compute

*Part 2 of 3 — see also: [Part 1](telnyx-edge-compute--part-1.md), [Part 3](telnyx-edge-compute--part-3.md)*

Telnyx Edge Compute is a serverless platform for deploying code across Telnyx's carrier-grade infrastructure, offering low latency, global distribution, and no infrastructure to manage. Functions run in real Linux containers with native language runtimes (Python, Go, Node.js, Java/Quarkus, TypeScript) and integrate directly with Telnyx Voice, Messaging, AI, and Storage services.

## Execution Model

### Function Lifecycle

**Cold start phase** — When a function receives its first request or scales up, a new container initializes:

1. Container image pulled (cached at edge) — ~0 ms when cached
2. Runtime initializes (Python/Go/Node/Quarkus) — ~50–200 ms
3. Global code executes (imports, connections) — ~50–300 ms
4. First request handled

**Warm execution** — Subsequent requests reuse the same container instance. Global variables and initialized resources (database connections, HTTP clients) persist between requests.

**Container recycling** — Containers are recycled when idle for extended periods, when memory limits are approached, after a new deployment, or due to platform scaling decisions. Do not rely on container persistence for critical state; use KV or external storage instead.

### Cold Start Optimization

1. **Lazy initialization** — Defer expensive operations until needed. Use `sync.Once` in Go, lazy globals in Python, `Suppliers.memoize` in Java.
2. **Minimize dependencies** — Import only what you need. Smaller images start faster.
3. **Connection pooling** — Initialize database and HTTP connection pools globally (once per container), reuse across requests.

### Concurrency and Scaling

Each container handles **one request at a time**. The platform scales horizontally by adding containers as needed. There is no hard limit on concurrent invocations — the platform auto-scales to handle traffic.

| Traffic Pattern | Platform Response |
|---|---|
| Low traffic | Fewer containers (may scale to zero) |
| Traffic spike | New containers start (cold starts) |
| Sustained load | Containers stay warm |
| Traffic drops | Containers gradually recycle |

### Request Timeouts

| Tier | Timeout |
|---|---|
| Default | 30 seconds |
| Extended | 60 seconds (configurable) |

Set internal timeouts shorter than the platform limit (e.g., 25 seconds) to leave a buffer.

### Triggers

Functions are invoked via **HTTP requests** (accessible at `https://{funcName}-{orgId}.telnyxcompute.com`) and **webhooks** (configure Telnyx services to call your function). Cron triggers are coming soon.

### Graceful Shutdown

When containers recycle, your function receives a `SIGTERM` signal. Handle it to clean up resources (close database connections, flush caches). Use `signal.signal(signal.SIGTERM, ...)` in Python, `signal.Notify(stop, syscall.SIGTERM)` in Go, or `@Observes ShutdownEvent` in Quarkus.

## Runtime Environment

Your functions run in lightweight containers with:

- **Full language runtimes** — Python 3.11+, Node.js 18+, Go 1.25+, Java 17+ (Quarkus)
- **Standard libraries** — Use native packages and dependencies
- **POSIX APIs** — File I/O, environment variables, process control
- **Network access** — HTTP clients, TCP sockets, DNS resolution

### Accessing Environment Configuration

Configuration is injected via environment variables. Variables defined in `[env_vars]` in `func.toml` and binding credentials (`TELNYX_API_KEY`, `TELNYX_BASE_URL`) are available at runtime through the standard environment API for each language (`process.env` in JS/TS, `os.Getenv` in Go, `os.environ` in Python, `System.getenv` in Java).

### HTTP Handling

Functions receive HTTP requests and return responses. You can use raw HTTP servers, Express (Node.js), Flask (Python), or the standard library HTTP handler (Go), all listening on port 8080.

### Outbound Networking

Functions can make outbound HTTP requests, open TCP sockets, and perform DNS resolution. Connection pooling is recommended for outbound HTTP and database connections.

## Bindings

Bindings provide secure, auto-authenticated access to Telnyx platform services without managing API keys in your code.

### Available Bindings

| Binding | Description | Status |
|---|---|---|
| Voice | Make and receive calls | ✅ Available |
| Messaging | Send SMS/MMS | ✅ Available |
| Phone Numbers | Manage numbers | ✅ Available |
| Fax | Send faxes | ✅ Available |
| Verify | 2FA/verification | ✅ Available |
| Cloud Storage | S3-compatible storage | ✅ Available |
| KV | Key-value store | 🔜 Coming soon |
| SQL DB | Serverless database | 🔜 Coming soon |

### How Bindings Work

When you deploy a function with an active binding:

1. Your function receives a JWT credential as the `TELNYX_API_KEY` environment variable.
2. Your function receives the binding proxy URL as `TELNYX_BASE_URL`.
3. API calls made to `${TELNYX_BASE_URL}/<api-path>` are routed through the binding proxy, which authenticates with your real API key.
4. The API call proceeds with proper authentication.

**Important:** You must construct API URLs using `TELNYX_BASE_URL` — do **not** call `https://api.telnyx.com` directly. Direct calls will return 401 because the binding-injected JWT is not a standard Telnyx API key.

### Managing Bindings

```bash
# Create a binding (one-time per organization)
telnyx-edge bindings create

# Validate the binding
telnyx-edge bindings validate

# View current binding
telnyx-edge bindings get

# Rotate credentials (recommended monthly)
telnyx-edge bindings update

# Remove the binding
telnyx-edge bindings delete
```

### Using Bindings with Telnyx SDKs

The Telnyx SDKs for Python, Go, and Java automatically use `TELNYX_API_KEY` and `TELNYX_BASE_URL` environment variables. No manual configuration is needed when a binding is active. For JavaScript, use `fetch()` with the `TELNYX_BASE_URL` and `TELNYX_API_KEY` from `process.env`.

### Cloud Storage Exception

The binding-injected JWT does **not** work for S3-compatible Cloud Storage operations. The Cloud Storage endpoint requires AWS SigV4 authentication. For Cloud Storage operations, store a regular Telnyx API key as a secret and use it as the S3 access key:

```bash
telnyx-edge secrets add TELNYX_STORAGE_KEY YOUR_API_KEY
```

The binding proxy handles `api.telnyx.com` routes only; S3-compatible calls go directly to the storage endpoint.

### Bindings vs Secrets

| Feature | Bindings | Secrets |
|---|---|---|
| Purpose | Telnyx service access | General sensitive data |
| Scope | One per organization | Unlimited per organization |
| Credentials | Auto-managed (JWT via proxy) | User-provided |
| Injection | `TELNYX_API_KEY` (JWT), `TELNYX_BASE_URL` (proxy URL) | Custom environment variables |
| Rotation | `bindings update` | Manual re-add |
| Use case | Telnyx SDK/API integration | Database passwords, external API keys |

Use bindings for Telnyx service access; use [secrets](telnyx-edge-compute-secrets-and-configuration.md) for third-party services or when you need multiple different credentials.
