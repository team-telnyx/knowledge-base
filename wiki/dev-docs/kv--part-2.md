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

*Part 2 of 4 — see also: [Part 1](kv--part-1.md), [Part 3](kv--part-3.md), [Part 4](kv--part-4.md)*

KV is a globally distributed key-value store built for read-heavy edge workloads such as session data, cached responses, and feature flags. It stores opaque bytes under string keys and is reachable from TypeScript edge functions via an `env` binding or from any language via the REST API.

## Runtime API

The types in this reference are exported from `@telnyx/edge-runtime` (TypeScript) and describe version **≥ 0.2.2** — the first release where `expirationTtl` is applied and `list()` entries carry `sizeBytes`/`updatedAt`. They describe the `env` binding — the in-function surface. To read or write KV from another language or outside a function, use the REST API.

A namespace declared as `[storage.kv.<NAME>]` in `func.toml` resolves on `env.<NAME>` as a `KvNamespace`.

| Surface | Where it lives | What it's for |
| --- | --- | --- |
| `KvNamespace` | `env.<BINDING>` | The binding handle — `get`, `put`, `delete`, `list`. |
| `KvGetTextOptions` / `KvGetJsonOptions` | `get()` options | Select the raw-text read or a `JSON.parse`d read. |
| `KvPutOptions` | `put()` options | `expirationTtl` — server-side TTL in seconds (`metadata` is deprecated and ignored). |
| `KvListOptions` / `KvListResult` / `KvKeyInfo` | `list()` options + result | Prefix, pagination cursor, and the returned key entries. |

### KvNamespace

`env.<BINDING>` (a `KvNamespace`) is the in-function handle to a KV namespace. It's a thin, pre-authenticated wrapper over the KV REST API — the runtime injects the credential, so your code holds no API key.

```
interface KvNamespace {
  get(key: string, options?: KvGetTextOptions): Promise<string | null>;
  get<T>(key: string, options: KvGetJsonOptions): Promise<T | null>;
  put(key: string, value: string, options?: KvPutOptions): Promise<void>;
  delete(key: string): Promise<void>;
  list(options?: KvListOptions): Promise<KvListResult>;
}
```

Key behaviors:

- **Values are opaque bytes** — `put` stores the string you pass verbatim (no base64, no envelope); `get` returns it byte-for-byte.
- **Missing keys read as `null`** — `get` resolves to `null` for a key that doesn't exist, not an error.
- **`delete` is idempotent** — deleting a missing key succeeds.
- **Read-your-writes** — a read after a successful `put` from the same location reflects it.
- **Errors throw** — a non-2xx from the store (other than the `404`→`null` on `get`) rejects the promise with an `Error` describing the operation and status.

### `get(key, options?)`

Read a value. Two overloads, selected by `options.type`:

```
interface KvGetTextOptions { type?: "text" }   // default
interface KvGetJsonOptions { type: "json" }    // JSON.parse the stored value
```

```
// Text (default) -> string | null
const raw = await env.MY_KV.get("user/123");

// JSON -> T | null (JSON.parse applied; an empty stored value yields null)
const user = await env.MY_KV.get<{ name: string }>("user/123", { type: "json" });
```

Returns `null` if the key does not exist. With `{ type: "json" }`, a malformed stored value throws from `JSON.parse`.

### `put(key, value, options?)`

Write a value. `value` is a string, stored verbatim. Resolves once the write is acknowledged.

```
interface KvPutOptions {
  expirationTtl?: number;   // seconds until the key expires server-side
  /** @deprecated Not supported by the API. Accepted but ignored. */
  metadata?: unknown;
}
```

```
await env.MY_KV.put("user/123", JSON.stringify({ name: "Alice" }));

// Expire automatically after one hour
await env.MY_KV.put("session/abc", token, { expirationTtl: 3600 });
```

`expirationTtl` maps to the REST API's `?ttl_secs=` parameter: the key is deleted server-side roughly that many seconds after the write. The value is floored to a whole number of seconds; anything below `1` is not sent — the write succeeds without a TTL.

`expirationTtl` requires `@telnyx/edge-runtime` **≥ 0.2.2** — earlier versions accept it but silently ignore it. `metadata` is ignored on every version (KV has no per-key metadata); it remains on the type, deprecated, so code that sets it keeps compiling.

### `delete(key)`

Remove a key. Idempotent — deleting a missing key resolves normally.

```
await env.MY_KV.delete("user/123");
```

### `list(options?)`

Enumerate keys (names only — `list` does not return values).

```
interface KvListOptions {
  prefix?: string;
  limit?: number;
  cursor?: string;   // from a previous result's `cursor`
}

interface KvListResult {
  keys: KvKeyInfo[];
  list_complete: boolean;
  cursor?: string;   // present when list_complete is false
}

interface KvKeyInfo {
  name: string;
  sizeBytes?: number;   // stored value size, from the API's size_bytes
  updatedAt?: Date;     // last write time, from the API's updated_at
  /** @deprecated Not populated by the API. Always undefined. */
  metadata?: unknown;
}
```

```
const { keys } = await env.MY_KV.list({ prefix: "user/" });
// [{ name: "user/123", sizeBytes: 21, updatedAt: 2026-06-18T14:48:17.475Z }, …]
```

`list()` requires `@telnyx/edge-runtime` ≥ 0.2.1 — on 0.2.0 it throws `Unexpected KV list response shape`. `sizeBytes` and `updatedAt` are populated from **0.2.2**; on 0.2.1 entries carry only `name`.

`KvKeyInfo.metadata` is never populated — KV has no per-key metadata. It remains on the type, deprecated, so code that reads it keeps compiling.

## How KV Works

KV is a single global key-value store optimized for low-latency reads from edge functions. A value is opaque bytes — you choose the serialization (text, JSON, binary), and KV stores exactly what you send and returns it byte-for-byte, with no envelope, base64 encoding, or server-side interpretation.

### Keys

A key is a path-like string. Allowed characters are `a-z`, `A-Z`, `0-9`, and `-` `_` `/` `=` `.`. Use `/` to group related keys (for example `user/123`, `session/abc`). Colons (`:`) are **not** allowed.

### Expiration (TTL)

By default a value lives until you delete it. You can also set a **server-side TTL** so a key expires automatically: pass `expirationTtl` on a binding `put`, `ttl_secs` on a REST write, or `--ttl` on the CLI. The TTL is a whole number of seconds; once it elapses the key is gone and reads return `null`/`404`.

An invalid `ttl_secs` (non-integer, `0`, or negative) is rejected with `422` and the key is not written. The binding never produces that `422`: it floors `expirationTtl` to a whole number of seconds and, if the result is less than `1`, sends no TTL at all — the write succeeds and the key does not expire. There is no way to read the remaining TTL back — a `get`/`list` on a live key does not report its expiry.

### No Per-Key Metadata

KV has **no per-key metadata**. The binding's `put` accepts a `metadata` option so older code keeps compiling, but it is ignored (deprecated as of 0.2.2), and `list` never returns metadata.

### Consistency and Regionality

KV is a **single global store**. There is no region to choose at creation time and no per-region copies to reconcile — every namespace is one logical dataset reachable from every edge location. Writes are replicated for durability and committed by quorum before they're acknowledged.

- **Read-your-writes** from a given location is reliable: once a write returns, a subsequent read sees it.
- **Across locations**, a read issued immediately after a write elsewhere may briefly observe the previous value; treat cross-location visibility as near-real-time rather than instantaneous.
- **Distance costs latency, not staleness** — a location far from where the data is coordinated pays network round-trip on the request, but reads the same authoritative data as everywhere else.
- **No transactions or compare-and-swap.** Don't use KV for atomic read-modify-write, counters, or coordination — concurrent writers to one key are last-write-wins.
