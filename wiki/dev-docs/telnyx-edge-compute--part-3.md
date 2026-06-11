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

*Part 3 of 3 — see also: [Part 1](telnyx-edge-compute--part-1.md), [Part 2](telnyx-edge-compute--part-2.md)*

Telnyx Edge Compute is a serverless platform for deploying code across Telnyx's carrier-grade infrastructure, offering low latency, global distribution, and no infrastructure to manage. Functions run in real Linux containers with native language runtimes (Python, Go, Node.js, Java/Quarkus, TypeScript) and integrate directly with Telnyx Voice, Messaging, AI, and Storage services.

## CLI Reference

The `telnyx-edge` CLI is the primary tool for deploying and managing Edge Compute functions.

### Authentication Commands

| Command | Description |
|---|---|
| `telnyx-edge auth login` | OAuth browser login |
| `telnyx-edge auth api-key set KEY` | Set API key directly |
| `telnyx-edge auth api-key clear` | Clear stored API key |
| `telnyx-edge auth status` | Check authentication status |
| `telnyx-edge auth logout` | Clear stored credentials |

### Function Management

| Command | Description |
|---|---|
| `telnyx-edge new-func -l=LANG -n=NAME` | Create a new function |
| `telnyx-edge ship` | Deploy from current directory |
| `telnyx-edge ship --from-dir=DIR` | Deploy from a specific directory |
| `telnyx-edge delete-func NAME` | Permanently delete a function |
| `telnyx-edge list` | List all functions in your organization |

The `new-func` command supports languages: `python`, `go`, `quarkus`, `js`, `ts`.

### Secrets Management

| Command | Description |
|---|---|
| `telnyx-edge secrets add NAME "VALUE"` | Add an encrypted secret |
| `telnyx-edge secrets list` | List secret names (values hidden) |
| `telnyx-edge secrets delete NAME` | Delete a secret |

Secrets are available as environment variables in your function at runtime.

### System Commands

| Command | Description |
|---|---|
| `telnyx-edge status` | Show CLI version, auth status, connectivity |
| `telnyx-edge --help` | General help |
| `telnyx-edge COMMAND --help` | Command-specific help |

### Configuration File

Each function has a `func.toml`:

```toml
[edge_compute]
func_name = "my-webhook"
language = "python"

[env_vars]
LOG_LEVEL = "info"
API_ENDPOINT = "https://api.example.com"

[build]
entry_point = "main.py"
```

| Field | Description | Required |
|---|---|---|
| `func_name` | Function name (used in URL) | Yes |
| `language` | Runtime language | Yes |
| `[env_vars]` | Environment variables | No |
| `[build]` | Build configuration | No |

## Limits and Quotas

### Execution Limits

| Limit | Default | Maximum |
|---|---|---|
| Request timeout | 30 seconds | 60 seconds |
| CPU time per request | 30 seconds | 60 seconds |
| Memory per container | 256 MB | 512 MB |
| Request body size | 10 MB | 10 MB |
| Response body size | 10 MB | 10 MB |

If a function exceeds the request timeout, the platform returns a 504 Gateway Timeout. If memory limits are exceeded, the container is terminated and a new one starts.

### Function Limits

| Limit | Value |
|---|---|
| Function code size | 50 MB (compressed) |
| Environment variables per function | 64 |
| Environment variable name size | 256 bytes |
| Environment variable value size | 5 KB |
| Secrets per organization | 100 |
| Secret value size | 10 KB |

### Network Limits

| Limit | Value |
|---|---|
| Outbound connections per request | 100 |
| Outbound request timeout | 30 seconds (configurable) |
| DNS resolution timeout | 5 seconds |

### Rate Limits

| Limit | Value |
|---|---|
| Deployments per hour | 60 |
| API requests per minute | 1,000 |
| Concurrent function invocations | No hard limit (auto-scales) |

### Account Limits

| Limit | Value |
|---|---|
| Functions per organization | 100 |
| Total function invocations | Based on plan |
| Total CPU time | Based on plan |

Contact [support@telnyx.com](mailto:support@telnyx.com) for higher enterprise limits.

### Error Codes

| Error | Code | Meaning |
|---|---|---|
| Request Timeout | 504 | Function didn't respond in time |
| Memory Exceeded | 500 | Container terminated due to memory |
| Payload Too Large | 413 | Request/response body exceeded limit |
| Rate Limited | 429 | Too many requests or deployments |

### Storage Limits (Coming Soon)

**KV Storage:**

| Limit | Value |
|---|---|
| Key size | 512 bytes |
| Value size | 25 MB |
| Keys per namespace | 1 billion |
| Namespaces per organization | 100 |
| Read ops/sec | 10,000 |
| Write ops/sec | 1,000 |

**SQL Database:**

| Limit | Value |
|---|---|
| Database size | 10 GB |
| Databases per organization | 10 |
| Rows per table | No hard limit |
| Query timeout | 30 seconds |

## Security

Each function runs in its own isolated container with network isolation (functions cannot communicate with each other directly), filesystem isolation (no shared filesystem between functions), and process isolation (separate process namespace).

API credentials are never exposed in code: bindings inject credentials securely, secrets are encrypted at rest, and credentials don't appear in logs.

## Integrations and Storage

Edge Compute integrates with Telnyx services through bindings:

- **Voice API** — Handle calls, transcribe audio, build IVRs
- **Messaging API** — Send and receive SMS/MMS with custom logic
- **AI APIs** — Transcription, inference, and embeddings at the edge
- **Cloud Storage** — S3-compatible storage for files and media (see Cloud Storage exception above)
- **KV** — Low-latency key-value storage for caching and session data (coming soon)
- **SQL DB** — Serverless SQL database with SQLite compatibility (coming soon)

## Observability

Observability features (logs, metrics, tracing) are in development. They will let you monitor your Edge Compute functions with real-time logs, performance metrics, and request tracing.

## Testing

Testing tooling and staging environments are in development. Since Edge Compute runs real containers, standard testing tools (pytest, Jest, go test, JUnit) work out of the box for local testing.

## Network

Private WireGuard-based mesh networking connecting your edge compute workloads, on-premise infrastructure, and cloud resources is planned for a future release.

## Common Workflows

### First Deployment

```bash
telnyx-edge auth login
telnyx-edge new-func -l=python -n=my-first-function
cd my-first-function
# ... edit your code ...
telnyx-edge ship
```

### Adding Secrets

```bash
telnyx-edge secrets add DATABASE_URL "postgres://..."
telnyx-edge secrets add API_KEY "secret-key"
telnyx-edge ship
```

### Setting Up Bindings

```bash
telnyx-edge bindings create    # one-time setup
telnyx-edge bindings validate   # verify it works
telnyx-edge ship               # deploy function that uses Telnyx SDK
```

### Troubleshooting

- **"Not authenticated" error:** Run `telnyx-edge auth logout` then `telnyx-edge auth login`.
- **Deployment fails:** Check `func.toml`, verify you're in the right directory, and run `telnyx-edge status`.
- **Function not responding:** Run `telnyx-edge list` to check the function exists, then `telnyx-edge ship` to redeploy.
- **Binding not found:** Run `telnyx-edge bindings create` to create one.
- **Validation failed:** Run `telnyx-edge bindings update`, check your Telnyx account status, and verify with `telnyx-edge auth status`.
- **Function can't access Telnyx API:** Check the binding exists with `telnyx-edge bindings get`, validate it with `telnyx-edge bindings validate`, and redeploy with `telnyx-edge ship`.
