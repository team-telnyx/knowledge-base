---
title: Configuration
summary: Every Telnyx Edge Compute project is configured by a single TOML manifest
  at its root — `func.toml` for classic single-function projects or `telnyx.toml`
  for umbrella TypeScript projects. The manifest declares the function's identity,
  environment variables, secret bindings, storage bindings, and (for umbrella projects)
  actors; configuration changes take effect on the next `telnyx-edge ship`.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/configuration/environment-variables
- url: https://developers.telnyx.com/docs/edge-compute/configuration/index
- url: https://developers.telnyx.com/docs/edge-compute/configuration/routing
- url: https://developers.telnyx.com/docs/edge-compute/configuration/secrets
- url: https://developers.telnyx.com/docs/edge-compute/configuration/versions
updated_at: 2026-08-05T13:40:37Z
---

# Configuration

*Part 1 of 4 — see also: [Part 2](configuration--part-2.md), [Part 3](configuration--part-3.md), [Part 4](configuration--part-4.md)*

Every Telnyx Edge Compute project is configured by a single TOML manifest at its root — `func.toml` for classic single-function projects or `telnyx.toml` for umbrella TypeScript projects. The manifest declares the function's identity, environment variables, secret bindings, storage bindings, and (for umbrella projects) actors; configuration changes take effect on the next `telnyx-edge ship`.

## Overview

Every Edge Compute project has a TOML manifest at its root. It is the one place a function is configured: it identifies what `telnyx-edge ship` deploys and declares the bindings the runtime resolves onto `env`. There are two forms:

- **`func.toml`** (classic) — a single function. Written by `telnyx-edge new-func`, which also registers the function server-side, so the UUID `func_id` is already filled in. Declares `[env_vars]`, `[telnyx]`, `[secrets](secrets.md)`, `[storage.kv.<NAME>]`, `[storage.cloudstorage.<NAME>]`, and `[storage.sqldb.<NAME>]`.
- **`telnyx.toml`** (umbrella) — a TypeScript project with a top-level `main` entry, bundled client-side on `ship`. Declares the same binding blocks plus `[actors](actors.md)`, which classic projects cannot.

`telnyx-edge types` reads either form and writes `telnyx-env.d.ts`, typing `env.<binding>` for each declaration. Configuration changes take effect on the next `telnyx-edge ship` — there is no live update; re-run `telnyx-edge types` after changing a binding declaration so `telnyx-env.d.ts` matches the manifest.

The binding blocks — `[telnyx]`, `[secrets](secrets.md)`, `[storage.kv.<NAME>]`, `[storage.cloudstorage.<NAME>]`, `[storage.sqldb.<NAME>]`, and `[actors](actors.md)` (umbrella only) — each resolve to a typed handle on `env`. See [Bindings](bindings.md) for the full catalogue.

## func.toml

`new-func` writes the minimal manifest — and because it registers the function server-side at scaffold time, the UUID `func_id` is already in it:

```toml
[edge_compute]
func_id = "7819cf01-39a8-400e-9bce-3d792ffa4017"
func_name = "demo-ts"

# For environment variables and secrets:
# Use telnyx-edge secrets add <name> <value>
# Secrets are injected as environment variables into all your functions
```

A manifest using every available block:

```toml
[edge_compute]
func_id   = "7819cf01-39a8-400e-9bce-3d792ffa4017"  # written by new-func — the function ship deploys
func_name = "demo-ts"                                # → https://demo-ts-7819cf01-3.telnyxcompute.com (name + func_id prefix)

[env_vars]                     # plain string env vars, injected on each deploy
LOG_LEVEL   = "info"
MAX_RETRIES = "3"

[telnyx]                       # pre-authenticated Telnyx API client
binding = "MY_TELNYX"          # → env.MY_TELNYX (TS); also injects TELNYX_API_KEY

[secrets](secrets.md)                    # typed handle onto a stored secret
binding = "STRIPE_KEY"         # → env.SECRETS.get("STRIPE_KEY")
name    = "STRIPE_API_KEY"     # the key stored with `secrets add`

[storage.kv.MY_KV]             # KV namespace binding — block key is the handle
id = "550e8400-e29b-41d4-a716-446655440000"   # → env.MY_KV

[storage.cloudstorage.ASSETS]  # Cloud Storage bucket binding — block key is the handle
bucket_name = "my-assets"      # → env.ASSETS; an existing bucket
region      = "us-east-1"      # us-central-1 | us-east-1 | us-west-1 | eu-central-1 | ap-southeast-1

[storage.sqldb.DB]             # SQL database binding — block key is the handle
id = "550e8400-e29b-41d4-a716-446655440000"   # → env.DB; the database UUID
```

There is no `language` key (the runtime comes from the project files the scaffold creates), no build block, and no timeout key — the request timeout is a platform property (default 30 s, maximum 60 s; see [Limits](limits.md)).

### [edge_compute] — identity

| Key | Value |
| --- | --- |
| `func_id` | The function's UUID, written by `new-func` when it registers the function server-side. This — not the directory — is what `ship` deploys, so swapping `func.toml` files switches deploy targets (the [CI/CD](ci-cd.md) staging pattern relies on this). |
| `func_name` | The function name, and the first part of the invoke URL: `https://{func_name}-{func_id-prefix}.telnyxcompute.com` (the suffix is derived from `func_id`; `telnyx-edge ship` and `list` print the exact host). See [Routes & Domains](routes-domains.md). |

### [env_vars] — environment variables

Free-form key-value pairs injected as process environment variables on each deploy. All values are strings; changes take effect on the next `ship`; values are plaintext in git — put credentials in [Secrets](secrets.md) instead. See [Environment Variables](environment-variables.md) for the full picture.

### [secrets](secrets.md) — secret bindings

| Key | Value |
| --- | --- |
| `binding` | The handle your code passes to `env.SECRETS.get()`. |
| `name` | The stored secret key, from `telnyx-edge secrets add <key> <value>`. |

The binding is the typed TypeScript surface; independently of it, every secret is injected as an environment variable into all functions in your organization. See [Secrets](secrets.md).

### [telnyx] — Telnyx API binding

| Key | Value |
| --- | --- |
| `binding` | The property on `env` — `env.<binding>` is a pre-authenticated Telnyx SDK client in TypeScript functions. |

Declaring the block also injects a `TELNYX_API_KEY` environment variable into the container — this is how non-TypeScript runtimes call the Telnyx API over plain REST. See [Telnyx API binding](telnyx-api-binding--part-1.md).

### [storage.kv.<NAME>] — KV namespace binding

| Key | Value |
| --- | --- |
| block key `<NAME>` | The handle — a name you choose. `env.<NAME>` is a `KvNamespace` (get/put/delete/list). |
| `id` | The KV namespace UUID, from `telnyx-edge storage kv create`. |

Multiple blocks are allowed — each becomes its own `env` property. `telnyx-edge types` generates `KvNamespace` types for these blocks since CLI v0.2.4. See the [KV quick start](kv-quick-start.md).

### [storage.cloudstorage.<NAME>] — Cloud Storage bucket binding

| Key | Value |
| --- | --- |
| block key `<NAME>` | The handle — a name you choose. `env.<NAME>` is a `CloudStorageBucket` (get/put/head/delete/list). TypeScript-only, via `@telnyx/edge-runtime` ≥ 0.3.0. |
| `bucket_name` | The name of an existing Cloud Storage bucket — the binding points at a bucket, it doesn't create one. |
| `region` | The bucket's region: `us-central-1`, `us-east-1`, `us-west-1`, `eu-central-1`, or `ap-southeast-1`. |

Multiple blocks are allowed — each becomes its own `env` property. The runtime injects the credential, so no access key or secret key appears in your code. See [Cloud Storage binding](cloud-storage-binding.md).

### [storage.sqldb.<NAME>] — SQL database binding

| Key | Value |
| --- | --- |
| block key `<NAME>` | The handle — a name you choose. `env.<NAME>` is a `SqlDatabase` (prepare/batch/exec). TypeScript-only, via `@telnyx/edge-runtime` ≥ 0.9.0. |
| `id` | The database UUID, from `telnyx-edge storage sqldb create`. Binding by name, or creating a database from the manifest, is rejected before deploy. |

Multiple blocks are allowed — each becomes its own `env` property, and two blocks carrying different ids are two separate databases. The id is checked when the function ships: an id that does not exist, belongs to another organization, or has not finished provisioning fails the deploy (currently as a generic `HTTP 500` that does not name the binding). See [SQL Databases](sql-databases--part-1.md).
