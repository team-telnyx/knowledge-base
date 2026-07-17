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

*Part 2 of 7 — see also: [Part 1](edge-compute--part-1.md), [Part 3](edge-compute--part-3.md), [Part 4](edge-compute--part-4.md), [Part 5](edge-compute--part-5.md), [Part 6](edge-compute--part-6.md), [Part 7](edge-compute--part-7.md)*

Telnyx Edge Compute is a platform of compute primitives for building and deploying applications to the Telnyx edge. The core primitive is a function: an ordinary HTTP server packaged as a container, deployed to Telnyx's global edge network, and served at its own public URL. The platform adds bindings (pre-authenticated handles to the Telnyx API, secrets, KV, object storage, and Stateful Actors), durable per-entity state via Stateful Actors, globally distributed key-value storage via KV, a mountable POSIX filesystem via CloudFS, and S3-compatible object storage. Functions are real Linux containers running your language's own runtime — Node.js, Go, Python, or Java (Quarkus) — with HTTP as the only trigger. Configuration is declarative through `func.toml` or `telnyx.toml` manifests, deployment is via the `telnyx-edge` CLI, and the platform handles scaling, cold starts, revisions, and rollback automatically.

## Configuration

Every Edge Compute project has a TOML manifest at its root. It is the one place a function is configured: it identifies what `telnyx-edge ship` deploys and declares the bindings the runtime resolves onto `env`.

There are two forms:

- **`func.toml`** (classic) — a single function. Written by `telnyx-edge new-func`, which also registers the function server-side, so the UUID `func_id` is already filled in.
- **`telnyx.toml`** (umbrella) — a TypeScript project with a top-level `main` entry, bundled client-side on `ship`. Declares the same binding blocks plus `[actors](actors.md)`, which classic projects cannot.

`telnyx-edge types` reads either form and writes `telnyx-env.d.ts`, typing `env.<binding>` for each declaration. Configuration changes take effect on the next `telnyx-edge ship` — there is no live update.

### Environment Variables

Functions run as real containers, so configuration reaches your code as ordinary process environment variables. There is no separate configuration API to learn.

| Variable | Where it comes from |
| --- | --- |
| `PORT` | Set by the platform. Your HTTP server must listen on it. |
| Every `[env_vars]` key | Declared in `func.toml`; injected verbatim on each deploy. |
| Every secret key | `telnyx-edge secrets add <key> <value>` injects the key into all functions in your organization. |
| `TELNYX_API_KEY` | Injected when the function declares a `[telnyx]` binding. |

Define non-sensitive configuration under `[env_vars]` in `func.toml`. All values are strings — parse numbers and booleans in your code. Changes take effect on the next `telnyx-edge ship`. Names share the `env` namespace with bindings; if an `[env_vars]` entry has the same name as a declared binding, `ship` warns that one shadows the other.

### Secrets

Secrets are key-value pairs for sensitive data — API keys, database passwords, signing keys. They are scoped to your organization, stored server-side, and never displayed by the CLI after you set them.

```
telnyx-edge secrets add STRIPE_API_KEY "sk_live_abc123"
telnyx-edge secrets list      # keys only — values are never shown
telnyx-edge secrets delete OLD_API_KEY
```

Every secret is injected into all functions in your organization as an environment variable named after its key. TypeScript projects can additionally declare a `[secrets](secrets.md)` binding in `func.toml` and read the secret through `env.SECRETS.get("<handle>")`, which `telnyx-edge types` type-checks against the declared handles. Both surfaces read the same store.

Secrets are organization-scoped. There is no per-environment scoping (dev/staging/prod) today — if you need separation, encode it in the key name (`DEV_DATABASE_PASSWORD`, `PROD_DATABASE_PASSWORD`) and pick one in code.

### Routes & Domains

Every function deployed with `telnyx-edge ship` gets a public HTTPS URL:

```
https://{func-name}-{org-nickname}.telnyxcompute.com
```

All HTTP methods and paths under the function's URL are routed to your server — path handling is up to your code. Requests time out after 30 seconds by default (60 seconds maximum). There is no custom domain support today — functions are reachable only at their `telnyxcompute.com` URL. You can't pin a function to a region today; the platform chooses placement.

### Versions & Rollback

Every successful `telnyx-edge ship` produces an immutable revision. `telnyx-edge revisions list` shows a function's deploy history; `telnyx-edge rollback` retargets traffic to a previous revision without rebuilding or re-uploading anything.

```
telnyx-edge revisions list my-func
telnyx-edge rollback my-func a1b2c3d
```

Only revisions that reached `deploy_ok` can be rolled back to. Rollback doesn't touch your source — the next `ship` deploys whatever is on disk as a new revision.

A function stuck in a terminal failure state (`build_failed`, `deploy_failed`, `delete_failed`) can be reset with `telnyx-edge reset-func <name>`, which tears down the function's deployed resources and returns it to the `created` state.

## Bindings

A binding maps a name you declare in `func.toml` to an authenticated resource handle, resolved by the runtime — the credential is injected for you and never appears in your code, bundle, or logs. Each binding resolves on the `env` object (from `@telnyx/edge-runtime`).

The `env` object and `telnyx-edge types` are TypeScript-only today. Other runtimes (`js`, `go`, `python`, `quarkus`) don't get the typed `env` handle, but reach the same resources through the credentials injected into the container.

| Resource | Declaration | On `env` |
| --- | --- | --- |
| Telnyx API | `[telnyx]` | `env.<BINDING>` — a pre-authenticated Telnyx SDK client |
| Secrets | `[secrets](secrets.md)` | `env.SECRETS.get("<handle>")` → `Promise<string>` |
| Key-Value storage | `[storage.kv.<name>]` | `env.<NAME>` — a `KvNamespace`: `get`, `put`, `delete`, `list` |
| Object storage | `[storage.cloudstorage.<name>]` | `env.<NAME>` — a `CloudStorageBucket`: `get`, `put`, `head`, `delete`, `list` |
| Stateful Actors | `[actors](actors.md)` — umbrella `telnyx.toml` only | `env.<BINDING>` — an actor namespace |

The binding name is yours to choose; it becomes the property on `env`. `telnyx-edge types` writes `telnyx-env.d.ts` from the manifest — re-run it after every binding change.

## Execution Model

An Edge Compute function is a Linux container running an HTTP server. The platform starts containers when traffic arrives, reuses them while it continues, and reclaims them — down to zero — when it stops.

### Container Lifecycle

A cold start is the first request's cost of a new container: the image starts, the language runtime boots, your module-level code runs, and then the request is served. Put expensive setup — HTTP clients, connection pools, parsed config — at module scope so it runs once per container instead of once per request.

While traffic continues, requests land on existing containers and skip initialization. Module state persists between requests on the same container — treat it as a cache keyed by container, nothing more. Two requests may or may not share a container, and the platform gives you no way to control which.

Containers are reclaimed without notice: after idling, when a new revision is shipped, or by platform scaling decisions. At zero traffic a function scales to zero containers; the next request pays a cold start.

### Request Timeout

A function must respond within 30 seconds by default, 60 seconds maximum; a request that exceeds the budget is terminated with a 504. There is no `func.toml` field for this. Budget outbound calls below the deadline so you return a real error instead of being cut off:

```
const upstream = await fetch("https://api.example.com/data", {
  signal: AbortSignal.timeout(25_000),
});
```

### Where State Lives

Module state dies with the container, so anything that must survive needs a home:

| Data | Use | Why |
| --- | --- | --- |
| Per-entity state, counters, coordination | [Stateful Actors](stateful-actors.md) | One instance per name, serialized calls, durable writes |
| Cache entries, config, feature flags, sessions | [KV](kv.md) | Globally distributed reads; opaque values up to 1 MiB with optional TTL |
| Files, media, large objects | [Cloud Storage buckets](cloud-storage--part-1.md) | S3-compatible object storage |

Don't build counters or per-entity coordination on KV — concurrent read-modify-write races there, which is exactly the problem Stateful Actors exist to solve.
