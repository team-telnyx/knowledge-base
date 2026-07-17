---
title: Edge Compute
summary: 'Telnyx Edge Compute is a platform of compute primitives for building and
  deploying applications to the Telnyx edge. The core primitive is a function: an
  ordinary HTTP server packaged as a container, deployed to Telnyx''s global edge
  network, and served at its own public URL. The platform adds bindings (pre-authenticated
  handles to the Telnyx API, secrets, KV, object storage, and Stateful Actors), durable
  per-entity state via Stateful Actors, globally distributed key-value storage via
  KV, a mountable POSIX filesystem via CloudFS, and S3-compatible object storage.
  Functions are real Linux containers running your language''s own runtime — Node.js,
  Go, Python, or Java (Quarkus) — with HTTP as the only trigger. Configuration is
  declarative through `func.toml` or `telnyx.toml` manifests, deployment is via the
  `telnyx-edge` CLI, and the platform handles scaling, cold starts, revisions, and
  rollback automatically.'
sources:
- url: https://developers.telnyx.com/docs/edge-compute/best-practices/index
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/concepts/filesystems-from-first-principles/index
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/concepts/how-cloudfs-works
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/concepts/network-filesystems
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/concurrent-access
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/index
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/mount/index
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/quickstart
- url: https://developers.telnyx.com/docs/edge-compute/configuration/environment-variables
- url: https://developers.telnyx.com/docs/edge-compute/configuration/index
- url: https://developers.telnyx.com/docs/edge-compute/configuration/routing
- url: https://developers.telnyx.com/docs/edge-compute/configuration/secrets
- url: https://developers.telnyx.com/docs/edge-compute/configuration/versions
- url: https://developers.telnyx.com/docs/edge-compute/deploy/index
- url: https://developers.telnyx.com/docs/edge-compute/development/index
- url: https://developers.telnyx.com/docs/edge-compute/guides/ai-assistant-backend
- url: https://developers.telnyx.com/docs/edge-compute/kv/best-practices
- url: https://developers.telnyx.com/docs/edge-compute/kv/cli
- url: https://developers.telnyx.com/docs/edge-compute/kv/concepts/how-kv-works/index
- url: https://developers.telnyx.com/docs/edge-compute/kv/examples/api-response-caching
- url: https://developers.telnyx.com/docs/edge-compute/kv/examples/feature-flags
- url: https://developers.telnyx.com/docs/edge-compute/kv/examples/session-storage/index
- url: https://developers.telnyx.com/docs/edge-compute/kv/index
- url: https://developers.telnyx.com/docs/edge-compute/kv/pricing/index
- url: https://developers.telnyx.com/docs/edge-compute/kv/quick-start
- url: https://developers.telnyx.com/docs/edge-compute/kv/reference/index
- url: https://developers.telnyx.com/docs/edge-compute/kv/reference/kv-namespace
- url: https://developers.telnyx.com/docs/edge-compute/kv/ttl-and-metadata
- url: https://developers.telnyx.com/docs/edge-compute/network/index
- url: https://developers.telnyx.com/docs/edge-compute/observability/index
- url: https://developers.telnyx.com/docs/edge-compute/overview/index
- url: https://developers.telnyx.com/docs/edge-compute/platform-overview/index
- url: https://developers.telnyx.com/docs/edge-compute/platform/limits
- url: https://developers.telnyx.com/docs/edge-compute/platform/pricing
- url: https://developers.telnyx.com/docs/edge-compute/quickstart/index
- url: https://developers.telnyx.com/docs/edge-compute/reference/cli
- url: https://developers.telnyx.com/docs/edge-compute/runtime/bindings
- url: https://developers.telnyx.com/docs/edge-compute/runtime/execution-model
- url: https://developers.telnyx.com/docs/edge-compute/runtime/http-handler
- url: https://developers.telnyx.com/docs/edge-compute/runtime/index
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/alarms
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/api-reference/base
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/api-reference/configuration
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/api-reference/context
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/api-reference/errors
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/api-reference/index
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/api-reference/namespace
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/api-reference/storage
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/api-reference/stub
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/concepts/addressing
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/concepts/execution-model
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/concepts/how-it-works/index
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/concepts/lifecycle
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/guides/project-structure/index
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/guides/when-to-use
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/index
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/local-development
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/quick-start/index
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/shared-actors
- url: https://developers.telnyx.com/docs/edge-compute/telnyx-api/api-reference
- url: https://developers.telnyx.com/docs/edge-compute/telnyx-api/handling-calls
- url: https://developers.telnyx.com/docs/edge-compute/telnyx-api/index
- url: https://developers.telnyx.com/docs/edge-compute/telnyx-api/quick-start
- url: https://developers.telnyx.com/docs/edge-compute/telnyx-api/receiving-messages
updated_at: 2026-07-17T09:13:17Z
---

# Edge Compute

*Part 6 of 7 — see also: [Part 1](edge-compute--part-1.md), [Part 2](edge-compute--part-2.md), [Part 3](edge-compute--part-3.md), [Part 4](edge-compute--part-4.md), [Part 5](edge-compute--part-5.md), [Part 7](edge-compute--part-7.md)*

Telnyx Edge Compute is a platform of compute primitives for building and deploying applications to the Telnyx edge. The core primitive is a function: an ordinary HTTP server packaged as a container, deployed to Telnyx's global edge network, and served at its own public URL. The platform adds bindings (pre-authenticated handles to the Telnyx API, secrets, KV, object storage, and Stateful Actors), durable per-entity state via Stateful Actors, globally distributed key-value storage via KV, a mountable POSIX filesystem via CloudFS, and S3-compatible object storage. Functions are real Linux containers running your language's own runtime — Node.js, Go, Python, or Java (Quarkus) — with HTTP as the only trigger. Configuration is declarative through `func.toml` or `telnyx.toml` manifests, deployment is via the `telnyx-edge` CLI, and the platform handles scaling, cold starts, revisions, and rollback automatically.

## Best Practices

### Configuration

- **Keep secrets out of code.** Store credentials as secrets — the CLI takes the key and value as positional arguments. Every secret is injected into your functions as a plain environment variable.
- **Budget for the platform timeout.** The request timeout is 30 seconds by default and 60 seconds at most — there is no `func.toml` field that raises it. Set your own deadlines on outbound calls a few seconds below the platform's so you fail with a useful error instead.
- **Name functions for their URL.** The function name becomes the hostname — `{func-name}-{org-nickname}.telnyxcompute.com` — so pick the name up front.

### Performance

- **Initialize once, at module scope.** A container serves many requests. Module scope runs once per container; the request callback runs per request. Build clients, load config, and compile anything expensive outside the callback.
- **Keep cold starts small.** A new container starts when traffic scales up or after a deploy, and the first request it serves waits for everything before `server.listen`. Keep dependencies minimal, and lazy-load heavy libraries used only on rare paths.
- **Cache expensive reads in KV.** Declare a KV namespace in `func.toml` and it resolves as a binding on `env`. Use `expirationTtl` for server-side expiry.

### Reliability

- **Make handlers idempotent.** Clients retry and webhooks are redelivered, so design handlers where processing the same request twice has the same effect as once. Key side effects on a caller-supplied identifier.
- **Keep the health endpoint fast.** Return immediately and never call a dependency from it, so a slow upstream can't make your function look down.
- **Catch everything at the top of the handler.** An exception that escapes the request callback crashes the process, drops every in-flight request, and makes the next request pay a cold start.
- **Time out and retry outbound calls.** Set an explicit deadline on every outbound call. Retry only network failures and 5xx responses, with exponential backoff, and keep the total budget under the platform timeout.

### Security

- **Validate input before use** — check required fields and types, reject with 400.
- **HTTPS only** for outbound calls.
- **Never log secret values** — and don't log full request bodies, which may carry PII. Log metadata: method, path, status, duration.
- **Authenticate anything that mutates state** — your function URL is public. Require a token or shared secret before acting on a request.

## Observability

Edge Compute has no customer-facing telemetry surface today: there is no `telnyx-edge logs` command, no log dashboard, and no metrics or traces. `console.log` output from a running function is not readable anywhere.

The CLI answers "is it deployed, and where does it answer" — not "what is it doing":

| Command | What it tells you |
| --- | --- |
| `telnyx-edge ship` | Build and deploy progress for one revision |
| `telnyx-edge list` | Every function: id, name, status, creation time, invoke URL |
| `telnyx-edge inspect <function>` | One function's status, invoke URL, timestamps, and actor bindings |
| `telnyx-edge revisions list <function>` | Deploy history, newest first |
| `telnyx-edge status` | CLI self-diagnostics |

The scaffolded TypeScript and JavaScript entrypoints answer `/health` before any other routing. Keep this route dependency-free — no KV reads, no outbound calls — so an external checker can tell "function down" apart from "dependency down". Point an uptime monitor at `https://<func-name>-<org>.telnyxcompute.com/health`.

Since nothing shows you a running function's output, the pattern is to send structured events over HTTPS to a collector you control. Store the collector's credential as a secret, never in code. Propagate a request id — read `X-Request-ID` or generate one, return it in the response, and attach it to every event you emit.

## Limits

### Execution Limits

| Limit | Default | Maximum |
| --- | --- | --- |
| Request timeout | 30 seconds | 60 seconds |
| Memory per container | 256 MB | 512 MB |
| Request body size | 10 MB | 10 MB |
| Response body size | 10 MB | 10 MB |

### Function Limits

| Limit | Value |
| --- | --- |
| Function code size | 50 MB (compressed) |
| Environment variables per function | 64 |
| Environment variable name size | 256 bytes |
| Environment variable value size | 5 KB |
| Secrets per organization | 100 |
| Secret value size | 10 KB |

### Network Limits

| Limit | Value |
| --- | --- |
| Outbound connections per request | 100 |
| DNS resolution timeout | 5 seconds |

### Rate Limits

| Limit | Value |
| --- | --- |
| Deployments per hour | 60 |
| API requests per minute | 1,000 |
| Concurrent function invocations | No hard limit (auto-scales) |

### Account Limits

| Limit | Value |
| --- | --- |
| Functions per organization | 100 |

## Pricing

Functions bill on two meters: requests (each HTTP request your function handles) and CPU time (metered in milliseconds). These are the only two meters — there is no charge for deploying, for the number of functions you keep, or for idle functions.

| Resource | Free tier | Paid |
| --- | --- | --- |
| Requests | 3.6M/month | $0.21/million |
| CPU time | 36M ms/month | $0.014/million ms |

Storage is billed separately — see [KV Pricing](kv.md).

## CI/CD

Every Edge Compute deployment from CI is the same three steps: install a pinned `telnyx-edge` binary, authenticate with `auth api-key set`, and run `ship`.

```
TELNYX_EDGE_VERSION=v0.2.3

curl -fsSL "https://github.com/team-telnyx/edge-compute/releases/download/${TELNYX_EDGE_VERSION}/telnyx-edge-${TELNYX_EDGE_VERSION}-linux-amd64.tar.gz" | tar xz
sudo mv "telnyx-edge-${TELNYX_EDGE_VERSION}-linux-amd64/telnyx-edge" /usr/local/bin/

telnyx-edge auth api-key set "$TELNYX_API_KEY"
telnyx-edge ship
```

The CLI ships as GitHub release binaries only — it is not on npm and there is no package manager formula. There is also no un-versioned "latest" asset: `releases/latest/download/...` URLs return 404. Pin a version in a `TELNYX_EDGE_VERSION` variable so bumping is a one-line change.

`telnyx-edge` does not read a `TELNYX_API_KEY` environment variable on its own. Store your API key as a CI secret and run `telnyx-edge auth api-key set "$TELNYX_API_KEY"` as a pipeline step.

`ship` has no environment flag. It deploys the function identified by `func.toml` in the shipped directory. Staging and production are separate functions — register both once locally with `new-func`, keep one codebase and both generated `func.toml` files in the repo, and have each pipeline job copy the matching one into place before shipping.
