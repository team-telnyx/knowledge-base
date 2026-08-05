---
title: KV
summary: KV is a globally distributed key-value store built for read-heavy edge workloads
  such as session data, cached responses, and feature flags. It stores opaque bytes
  under string keys and is reachable from TypeScript edge functions via an `env` binding
  or from any language via the REST API.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/kv
- url: https://developers.telnyx.com/docs/edge-compute/kv/best-practices
- url: https://developers.telnyx.com/docs/edge-compute/kv/cli
- url: https://developers.telnyx.com/docs/edge-compute/kv/concepts/how-kv-works/index
- url: https://developers.telnyx.com/docs/edge-compute/kv/examples/api-response-caching
- url: https://developers.telnyx.com/docs/edge-compute/kv/examples/feature-flags
- url: https://developers.telnyx.com/docs/edge-compute/kv/examples/session-storage/index
- url: https://developers.telnyx.com/docs/edge-compute/kv/pricing/index
- url: https://developers.telnyx.com/docs/edge-compute/kv/quick-start
- url: https://developers.telnyx.com/docs/edge-compute/kv/reference/index
- url: https://developers.telnyx.com/docs/edge-compute/kv/reference/kv-namespace
- url: https://developers.telnyx.com/docs/edge-compute/kv/ttl-and-metadata
updated_at: 2026-08-05T13:41:30Z
---

# KV

*Part 1 of 4 — see also: [Part 2](kv--part-2.md), [Part 3](kv--part-3.md), [Part 4](kv--part-4.md)*

KV is a globally distributed key-value store built for read-heavy edge workloads such as session data, cached responses, and feature flags. It stores opaque bytes under string keys and is reachable from TypeScript edge functions via an `env` binding or from any language via the REST API.

## Overview

KV is a globally distributed key-value store: you write bytes under a string key and read them back, fast, from anywhere. It is built for read-heavy edge workloads — session data, cached responses, feature flags, and other small values a function needs on every request.

A value is **opaque bytes**. You choose the serialization (text, JSON, binary); KV stores exactly what you send and returns it byte-for-byte. There is no envelope, no base64 encoding, and no server-side interpretation of the value.

## Two Ways to Use KV

The same namespaces and keys are reachable two ways. Pick based on where your code runs.

| | `env` binding | REST API |
| --- | --- | --- |
| **Where** | Inside a TypeScript edge function | Anywhere — any language, any host |
| **Auth** | Injected by the runtime; no API key in your code | Your `TELNYX_API_KEY` as a bearer token |
| **Shape** | `env.<name>.get(...)`, `.put(...)`, `.delete(...)` | `GET`/`PUT`/`DELETE https://api.telnyx.com/v2/storage/kvs/{id}/keys/{key}` |
| **Use it for** | Reads and writes on the request path from your function | Provisioning namespaces, non-TS runtimes, tooling, back-office scripts |

Both hit the same store, so a value written through the binding is immediately readable over REST and vice versa. The binding is a thin, pre-authenticated wrapper over the same REST endpoints — it just means your function never handles an API key.

The `env` KV binding is **TypeScript-only** and requires `@telnyx/edge-runtime` ≥ 0.2.2. Go, JS, Python, and Quarkus functions use the REST API directly.

## Quick Start

### Create a Namespace

A namespace is an isolated key space. Create one with the CLI or the API:

```
telnyx-edge storage kv create --name my-cache
```

```
curl -X POST https://api.telnyx.com/v2/storage/kvs \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name": "my-cache"}'
```

The response includes the namespace `id` (a UUID). A new namespace starts in `status: "pending"` and isn't writable yet: writes return `409` (`"Namespace is not ready (status: pending)"`) until provisioning finishes, which typically takes a few seconds and can stretch to ~20. If you're scripting, poll `GET https://api.telnyx.com/v2/storage/kvs/{id}` until `"status": "provision_ok"` before your first write.

### Path A: The Function Binding

Declare the namespace in `func.toml`. The block key is a name you choose — it becomes the property on `env`. This example uses `MY_KV`, so the binding is reached as `env.MY_KV`:

```
[edge_compute]
func_name = "my-function"

[storage.kv.MY_KV]
id = "550e8400-e29b-41d4-a716-446655440000"  # Namespace ID from step 1
```

Add `@telnyx/edge-runtime` (≥ 0.2.2) to your `package.json` dependencies, then regenerate the environment types:

```
telnyx-edge types   # writes telnyx-env.d.ts — env.MY_KV is now a typed KvNamespace
```

Each `[storage.kv.<NAME>]` block becomes `env.<NAME>: KvNamespace` in the generated `telnyx-env.d.ts` — declare as many namespaces as you need. KV type generation requires CLI **≥ v0.2.3**. The binding itself resolves at runtime from `func.toml` — types are for the compiler, and a stale `telnyx-env.d.ts` doesn't affect the deployed function.

Use the binding in your code:

```
import { env } from "@telnyx/edge-runtime";

// Write — value is stored verbatim (UTF-8 preserved)
await env.MY_KV.put("user/123", JSON.stringify({ name: "Alice 👋" }));

// Read as text -> '{"name":"Alice 👋"}'  (null if the key is missing)
const raw = await env.MY_KV.get("user/123");

// Read and JSON.parse in one step -> { name: "Alice 👋" }  (null if missing)
const user = await env.MY_KV.get<{ name: string }>("user/123", { type: "json" });

// Write with a server-side TTL — the key deletes itself after ~60 seconds
await env.MY_KV.put("otp/123", "482913", { expirationTtl: 60 });

// Delete (idempotent — deleting a missing key is not an error)
await env.MY_KV.delete("user/123");
```

### Path B: The REST API

Use this anywhere outside a TypeScript edge function — a non-TypeScript function (Go, JS, Python, Quarkus), your own backend, or tooling. Authenticate with your `TELNYX_API_KEY`. The value is the raw request/response body — no base64, no envelope.

KV support landed in the official server SDKs in **telnyx-node ≥ 7.5.0**, **telnyx-python ≥ 4.166.0**, **telnyx-php ≥ 7.88.0**, **telnyx-ruby ≥ 5.152.0**, and **telnyx-go ≥ v4.85.0** — on earlier versions the `storage` resource is object storage (buckets) only. The Java SDK doesn't cover KV yet; call the endpoints over plain HTTP.

```
# Write — the request body is stored verbatim (no base64, no envelope)
curl -X PUT "https://api.telnyx.com/v2/storage/kvs/$KV_NAMESPACE_ID/keys/user/123" \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  --data-binary '{"name":"Alice 👋"}'

# Read — the response body is the raw stored value (404 if the key doesn't exist)
curl "https://api.telnyx.com/v2/storage/kvs/$KV_NAMESPACE_ID/keys/user/123" \
  -H "Authorization: Bearer $TELNYX_API_KEY"

# Write with a server-side TTL — the key deletes itself after ~60 seconds
curl -X PUT "https://api.telnyx.com/v2/storage/kvs/$KV_NAMESPACE_ID/keys/otp/123?ttl_secs=60" \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  --data-binary '482913'

# Delete (idempotent — deleting a missing key is not an error)
curl -X DELETE "https://api.telnyx.com/v2/storage/kvs/$KV_NAMESPACE_ID/keys/user/123" \
  -H "Authorization: Bearer $TELNYX_API_KEY"

# List keys by prefix — returns key names and metadata, never values
curl "https://api.telnyx.com/v2/storage/kvs/$KV_NAMESPACE_ID/keys?prefix=user/&limit=100" \
  -H "Authorization: Bearer $TELNYX_API_KEY"
```

`list` returns key names and per-key metadata, never values:

```
{
  "record_type": "storage_kv_key",
  "data": [{ "key": "user/123", "size_bytes": 21, "updated_at": "2026-06-18T14:48:17.475129983Z" }],
  "meta": { "has_more": false }
}
```

When `meta.has_more` is `true`, pass the returned `meta.cursor` back as `?cursor=` (in the SDKs, the `cursor` parameter) to fetch the next page — key listing does not auto-paginate in any SDK.

Inside an edge function, the org binding injects `TELNYX_API_KEY` (and a base-URL proxy) at runtime, so REST calls from a function authenticate without you shipping a key.
