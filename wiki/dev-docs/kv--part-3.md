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

*Part 3 of 4 — see also: [Part 1](kv--part-1.md), [Part 2](kv--part-2.md), [Part 4](kv--part-4.md)*

KV is a globally distributed key-value store built for read-heavy edge workloads such as session data, cached responses, and feature flags. It stores opaque bytes under string keys and is reachable from TypeScript edge functions via an `env` binding or from any language via the REST API.

## Key Expiration

KV supports **server-side expiration (TTL)**: set a TTL on a write and the key is deleted automatically once it elapses. Without a TTL, a value lives until you delete it. KV has **no per-key metadata**.

### Server-Side TTL

Pass `expirationTtl` on a binding `put`, a `ttl_secs` query parameter on a REST write, or `--ttl` on the CLI. The value is a whole number of seconds (`1`–`9223372036`); the key expires roughly that many seconds after the write, after which reads return `null`/`404`.

```
import { env } from "@telnyx/edge-runtime";

// Expire this key ~30 seconds after writing
await env.MY_KV.put("session/abc", JSON.stringify({ userId: 42 }), { expirationTtl: 30 });
```

```
# Expire this key ~30 seconds after writing
curl -X PUT "https://api.telnyx.com/v2/storage/kvs/$KV_NAMESPACE_ID/keys/session%2Fabc?ttl_secs=30" \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  --data-binary '{"userId": 42}'
```

```
telnyx-edge storage kv key put <namespace-id> session/abc '{"userId": 42}' --ttl 30s
```

`expirationTtl` requires `@telnyx/edge-runtime` **≥ 0.2.2**. Earlier versions accept the option but silently ignore it — the key is written without a TTL.

### Application-Level Expiry

Server-side TTL deletes the key and tells you nothing else — there is no way to read a key's remaining lifetime. Use this pattern instead when you want an absolute `expires_at` timestamp you can inspect on read (or when you're pinned to `@telnyx/edge-runtime` < 0.2.2, where `expirationTtl` is ignored). Wrap your value with the timestamp and check it when you read; if it's in the past, treat the key as missing (and optionally delete it).

```
import { env } from "@telnyx/edge-runtime";

async function putWithExpiry(key: string, value: string, ttlSeconds: number) {
    await env.MY_KV.put(key, JSON.stringify({
        value,
        expires_at: Date.now() + ttlSeconds * 1000,
    }));
}

async function getWithExpiry(key: string): Promise<string | null> {
    const wrapped = await env.MY_KV.get<{ value: string; expires_at: number }>(key, { type: "json" });
    if (wrapped === null) return null;              // key not found

    if (Date.now() > wrapped.expires_at) {
        await env.MY_KV.delete(key);                    // lazily clean up
        return null;                                 // expired
    }
    return wrapped.value;
}
```

```
// Usage: a session that "expires" after one hour
await putWithExpiry("session/abc", JSON.stringify({ userId: 42 }), 3600);

const session = await getWithExpiry("session/abc"); // null once an hour has passed
```

Notes on this pattern:

- **Reads do the enforcing.** An expired key still occupies storage until it's read (and lazily deleted) or you delete it explicitly. Prefer native TTL (`expirationTtl`/`ttl_secs`) for eager server-side cleanup; if you do need a sweep, drive it from an external scheduler hitting your function over HTTP — HTTP is the only function trigger today.
- **Use a consistent clock.** `Date.now()` on the edge node is fine for coarse expiry; don't rely on it for sub-second precision.
- **Keep the envelope small.** You pay for stored bytes, so the wrapper adds a little overhead per key.

## Best Practices

### Key Naming

Keys may contain `a-z`, `A-Z`, `0-9`, and `-` `_` `/` `=` `.` (no colons). Use `/` to group related keys:

```
user/123              # User data
session/abc           # Session data
cache/api/users       # Cached API response
flag/new-feature      # Feature flag
```

Grouping by prefix also lets you enumerate a subset later — `list({ prefix: "user/" })` (or `?prefix=user/` over REST).

### Value Serialization

KV stores values verbatim, so serialize complex values yourself (no base64 needed):

```
// Write
await env.MY_KV.put("user/123", JSON.stringify({ name: "Alice", age: 30 }));

// Read + parse
const user = await env.MY_KV.get<{ name: string; age: number }>("user/123", { type: "json" });
```

### Missing Keys

`get` returns `null` for a key that doesn't exist — handle it explicitly:

```
const value = await env.MY_KV.get("possibly-missing-key");
if (value === null) {
    return new Response("Not found", { status: 404 });
}
```

### Keep Values Small

KV is built for many small values read on the request path, not for large blobs. A value is capped at **1 MiB** (1,048,576 bytes) — a larger write is rejected with `413`. Store big or binary objects in [Cloud Storage](cloud-storage.md) and keep only the key or a small reference in KV.

### Limits

| Limit | Value |
| --- | --- |
| Max value size | 1 MiB (1,048,576 bytes) — over → `413` |
| Max key length | 256 characters — over → `400` |
| Key characters | `a-z` `A-Z` `0-9` `-` `_` `/` `=` `.` (no colons) |
| `list` page size | `limit` 1–1000 (default 1000) |

### Don't Rely on Atomicity

KV has no transactions or compare-and-swap, and concurrent writers to one key are last-write-wins. Don't use it for counters, locks, or coordination.

## CLI

Manage KV namespaces and keys using the `telnyx-edge` CLI.

### Namespace Management

```
# List all namespaces
telnyx-edge storage kv list

# Create a namespace (name: lowercase letters, numbers, hyphens)
telnyx-edge storage kv create --name my-cache

# Get a namespace
telnyx-edge storage kv get <namespace-id>

# Delete a namespace
telnyx-edge storage kv delete <namespace-id>
```

### Key Operations

The value is stored verbatim — pass it as a positional argument, or use `--path` to store the contents of a file.

```
# List keys in a namespace
telnyx-edge storage kv key list <namespace-id>

# List keys filtered by prefix
telnyx-edge storage kv key list <namespace-id> --prefix user/

# Get a value (prints the raw stored bytes)
telnyx-edge storage kv key get <namespace-id> user/123

# Put a value
telnyx-edge storage kv key put <namespace-id> user/123 "hello"

# Put a value from a file
telnyx-edge storage kv key put <namespace-id> user/123 --path ./value.json

# Put a value with a server-side TTL (key expires after the duration)
telnyx-edge storage kv key put <namespace-id> session/abc "hello" --ttl 30s

# Delete a key
telnyx-edge storage kv key delete <namespace-id> user/123
```

#### Key Put Flags

| Flag | Description |
| --- | --- |
| `--path` | Store the contents of a file as the value, instead of a positional argument |
| `--ttl` | Server-side expiry as a duration (`30s`, `5m`, `1h`); the key is deleted after it elapses |

#### Key List Flags

| Flag | Description |
| --- | --- |
| `--prefix` | Filter keys by prefix |
| `--cursor` | Pagination cursor from a previous response |
| `--limit` | Maximum number of keys to return, `1`–`1000` (default `1000`) |

Keys may contain `a-z`, `A-Z`, `0-9`, and `-` `_` `/` `=` `.` (no colons). Use `--ttl` for server-side expiry. KV has no per-key metadata, so there is no `--metadata` flag.
