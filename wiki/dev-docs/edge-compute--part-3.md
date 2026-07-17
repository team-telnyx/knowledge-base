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

*Part 3 of 7 — see also: [Part 1](edge-compute--part-1.md), [Part 2](edge-compute--part-2.md), [Part 4](edge-compute--part-4.md), [Part 5](edge-compute--part-5.md), [Part 6](edge-compute--part-6.md), [Part 7](edge-compute--part-7.md)*

Telnyx Edge Compute is a platform of compute primitives for building and deploying applications to the Telnyx edge. The core primitive is a function: an ordinary HTTP server packaged as a container, deployed to Telnyx's global edge network, and served at its own public URL. The platform adds bindings (pre-authenticated handles to the Telnyx API, secrets, KV, object storage, and Stateful Actors), durable per-entity state via Stateful Actors, globally distributed key-value storage via KV, a mountable POSIX filesystem via CloudFS, and S3-compatible object storage. Functions are real Linux containers running your language's own runtime — Node.js, Go, Python, or Java (Quarkus) — with HTTP as the only trigger. Configuration is declarative through `func.toml` or `telnyx.toml` manifests, deployment is via the `telnyx-edge` CLI, and the platform handles scaling, cold starts, revisions, and rollback automatically.

## KV

KV is a globally distributed key-value store optimized for low-latency reads from edge functions. A value is opaque bytes — you choose the serialization (text, JSON, binary), and KV stores exactly what you send and returns it byte-for-byte, with no envelope, base64 encoding, or server-side interpretation.

### Keys

A key is a path-like string. Allowed characters are `a-z`, `A-Z`, `0-9`, and `-` `_` `/` `=`. Use `/` to group related keys (for example `user/123`, `session/abc`). Colons (`:`) are not allowed.

### Expiration (TTL)

By default a value lives until you delete it. You can also set a server-side TTL so a key expires automatically: pass `expirationTtl` on a binding `put`, `ttl_secs` on a REST write, or `--ttl` on the CLI. The TTL is a whole number of seconds; once it elapses the key is gone and reads return `null`/`404`.

`expirationTtl` requires `@telnyx/edge-runtime` ≥ 0.2.2 — earlier versions accept the option but silently ignore it. KV has no per-key metadata.

### Consistency

KV is a single global store. There is no region to choose at creation time and no per-region copies to reconcile — every namespace is one logical dataset reachable from every edge location. Writes are replicated for durability and committed by quorum before they're acknowledged.

- **Read-your-writes** from a given location is reliable: once a write returns, a subsequent read sees it.
- **Across locations**, a read issued immediately after a write elsewhere may briefly observe the previous value.
- **No transactions or compare-and-swap.** Don't use KV for atomic read-modify-write, counters, or coordination — concurrent writers to one key are last-write-wins.

### Using KV

The same namespaces and keys are reachable two ways. The `env` binding is a thin, pre-authenticated wrapper over the REST API — it just means your function never handles an API key. The `env` KV binding is TypeScript-only and requires `@telnyx/edge-runtime` ≥ 0.2.2. Go, JS, Python, and Quarkus functions use the REST API directly.

```
import { env } from "@telnyx/edge-runtime";

await env.MY_KV.put("user/123", JSON.stringify({ name: "Alice" }));
const user = await env.MY_KV.get<{ name: string }>("user/123", { type: "json" });
await env.MY_KV.put("otp/123", "482913", { expirationTtl: 60 });
await env.MY_KV.delete("user/123");
```

### Limits

| Limit | Value |
| --- | --- |
| Max value size | 1 MiB (1,048,576 bytes) — over → 413 |
| Max key length | 256 characters — over → 400 |
| Key characters | `a-z` `A-Z` `0-9` `-` `_` `/` `=` `.` (no colons) |
| `list` page size | `limit` 1–1000 (default 1000) |

### Pricing

| Resource | Free Tier | Paid |
| --- | --- | --- |
| Reads | 10M/month | $0.35/million |
| Writes | 1M/month | $3.50/million |
| Deletes | 1M/month | $3.50/million |
| Lists | 1M/month | $3.50/million |
| Storage | 1 GB/month | $0.35/GB-month |

Egress is free.
