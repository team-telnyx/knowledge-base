---
title: Runtime APIs
summary: 'Edge Compute functions are real Linux containers running native language
  runtimes (Node.js, Go, Python, Java/Quarkus). The platform adds a small, explicit
  layer on top: an execution environment with cold starts, warm reuse, and a request
  budget; a per-language entrypoint contract for handling HTTP requests; and bindings
  that inject credentials for the Telnyx API, secrets, KV, object storage, SQL databases,
  and stateful actors.'
sources:
- url: https://developers.telnyx.com/docs/edge-compute/runtime/bindings
- url: https://developers.telnyx.com/docs/edge-compute/runtime/execution-model
- url: https://developers.telnyx.com/docs/edge-compute/runtime/http-handler
- url: https://developers.telnyx.com/docs/edge-compute/runtime/index
updated_at: 2026-08-05T13:41:58Z
---

# Runtime APIs

*Part 3 of 3 — see also: [Part 1](runtime-apis--part-1.md), [Part 2](runtime-apis--part-2.md)*

Edge Compute functions are real Linux containers running native language runtimes (Node.js, Go, Python, Java/Quarkus). The platform adds a small, explicit layer on top: an execution environment with cold starts, warm reuse, and a request budget; a per-language entrypoint contract for handling HTTP requests; and bindings that inject credentials for the Telnyx API, secrets, KV, object storage, SQL databases, and stateful actors.

## Bindings

A binding maps a name you declare in `func.toml` to an authenticated resource handle, resolved by the runtime — the credential is injected for you and never appears in your code, bundle, or logs. Each binding resolves on the `env` object (from `@telnyx/edge-runtime`) — `env.MY_TELNYX`, `env.SECRETS`, and so on.

The `env` object and `telnyx-edge types` are **TypeScript-only** today. Other runtimes (`js`, `go`, `python`, `quarkus`) don't get the typed `env` handle, but reach the same resources through the credentials injected into the container — see [Bindings from other languages](#bindings-from-other-languages).

### Every binding works the same way

```toml
# func.toml — 1. declare
[telnyx]
binding = "MY_TELNYX"
```

```bash
# 2. generate types
telnyx-edge types
```

```ts
// 3. use it — typed and authenticated
import { env } from "@telnyx/edge-runtime";
const { data } = await env.MY_TELNYX.availablePhoneNumbers.list({
  filter: { country_code: "US" },
});
```

The binding name (`MY_TELNYX`) is yours to choose; it becomes the property on `env`. `telnyx-edge types` writes `telnyx-env.d.ts` from the manifest — re-run it after every binding change. Typing for `[storage.kv.<name>]` blocks requires CLI **v0.2.3** or later.

The SDK types `.data` as `T | undefined` for list calls. Under `tsc --strict`, indexing into `data` (e.g. `data.length`) fails with `TS18048: 'data' is possibly 'undefined'`. Coalesce before use: `const arr = list.data ?? [];`.

### Catalogue

| Resource | Declaration | On `env` |
| --- | --- | --- |
| [Telnyx API](telnyx-api.md) | `[telnyx]` | `env.<BINDING>` — a pre-authenticated Telnyx SDK client |
| [Secrets](secrets.md) | `[secrets](secrets.md)` | `env.SECRETS.get("<handle>")` → `Promise<string>` |
| [KV](kv--part-1.md) | `[storage.kv.<name>]` | `env.<NAME>` — a `KvNamespace`: `get`, `put`, `delete`, `list` |
| [Cloud Storage](cloud-storage.md) | `[storage.cloudstorage.<name>]` | `env.<NAME>` — a `CloudStorageBucket`: `get`, `put`, `head`, `delete`, `list` |
| [SQL Databases](sql-databases--part-1.md) (Beta) | `[storage.sqldb.<name>]` — `id` must be the database UUID | `env.<NAME>` — a `SqlDatabase`: `prepare`, `batch`, `exec` |
| [Stateful Actors](stateful-actors--part-1.md) (Beta) | `[actors](actors.md)` — umbrella `telnyx.toml` only | `env.<BINDING>` — an actor namespace: one instance per name, addressed via `idFromName` |

### Manifest: `func.toml` or `telnyx.toml`

Bindings are declared in your project manifest. `telnyx-edge types` reads either form and types `env.<binding>` for each declared binding.

- **`func.toml`** (classic) — the standard `[edge_compute]` project file. Can declare `[telnyx]`, `[secrets](secrets.md)`, `[storage.kv.<name>]`, `[storage.cloudstorage.<name>]`, and `[storage.sqldb.<name>]`.
- **`telnyx.toml`** (umbrella) — a manifest with top-level `name` and `main`. Declares the same bindings, plus `[actors](actors.md)` — actor classes are imported from `main`, which is why actors require the umbrella form.

```toml
# telnyx.toml — umbrella manifest
name = "my-app"
main = "src/index.ts"

[telnyx]
binding = "MY_TELNYX"

[secrets](secrets.md)
binding = "GREETING"
name    = "DEMO_GREETING"

[storage.kv.CACHE]
id = "<kv-namespace-uuid>"   # from `telnyx-edge storage kv list`
```

### Bindings from other languages

The `env` SDK surface is TypeScript-only, but the credentials behind it are not:

- **Telnyx API** — declaring `[telnyx]` also injects a `TELNYX_API_KEY` environment variable into the container at runtime. Any language can call the Telnyx REST API with it as a bearer token — see [Using the Telnyx API](using-the-telnyx-api.md).
- **Secrets** — every secret is also injected as a plain environment variable into all your functions (`os.environ["DEMO_GREETING"]`, `os.Getenv("DEMO_GREETING")`, …). `env.SECRETS.get()` and the environment variable are two views of the same value.
- **KV** — any language can use the [KV REST API](https://developers.telnyx.com/docs/edge-compute/kv/quick-start#path-b-the-rest-api) with the injected `TELNYX_API_KEY`.
- **Object storage** — the typed `env` binding is TypeScript only; from any language, reach the same buckets over the [S3-compatible API](https://developers.telnyx.com/docs/cloud-storage/quick-start) with your own access keys.
- **SQL Databases** — the typed `env` binding is TypeScript only; from any language, query the same database over [`POST /v2/storage/sqldbs/{id}/actions/query`](https://developers.telnyx.com/docs/edge-compute/sqldb/quick-start#8-query-it-from-any-language) with a Telnyx API key as a bearer token. `TELNYX_API_KEY` is only in the environment when the function also declares `[telnyx]`, so declare that block as well or supply the key as a [secret](secrets.md). That endpoint takes no bound parameters, so use it for SQL you wrote yourself, never for values that came from a caller.
- **Stateful Actors** — TypeScript only; there is no REST fallback today.

### Bindings vs secrets

- **Binding** — a Telnyx or platform resource, authenticated for you (`env.MY_TELNYX`).
- **Secret** — a value you supply (`env.SECRETS.get("STRIPE_KEY")`).

Use a binding for platform resources; use a [secret](secrets.md) for your own third-party credentials.

## Next steps

- [Telnyx API Quick Start](telnyx-api-quick-start.md) — declare `[telnyx]` and make your first authenticated call
- [KV Quick Start](kv-quick-start.md) — create a namespace, bind it, read and write
- [Cloud Storage Bindings](cloud-storage-bindings--part-1.md) — bind a bucket and read, write, and list objects from `env`
- [SQL Databases Quick Start](sql-databases-quick-start.md) — create a database, bind it, and query it from `env.DB`
- [Secrets](secrets.md) — add, rotate, and access secrets
- [Stateful Actors](stateful-actors--part-1.md) — per-entity state and coordination
- [HTTP Handler](http-handler.md) — the entrypoint contract per language
- [Limits](limits.md) — timeouts, memory, and payload caps
- [Versions](versions.md) — revisions, `ship`, and `rollback`
