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

*Part 1 of 7 — see also: [Part 2](edge-compute--part-2.md), [Part 3](edge-compute--part-3.md), [Part 4](edge-compute--part-4.md), [Part 5](edge-compute--part-5.md), [Part 6](edge-compute--part-6.md), [Part 7](edge-compute--part-7.md)*

Telnyx Edge Compute is a platform of compute primitives for building and deploying applications to the Telnyx edge. The core primitive is a function: an ordinary HTTP server packaged as a container, deployed to Telnyx's global edge network, and served at its own public URL. The platform adds bindings (pre-authenticated handles to the Telnyx API, secrets, KV, object storage, and Stateful Actors), durable per-entity state via Stateful Actors, globally distributed key-value storage via KV, a mountable POSIX filesystem via CloudFS, and S3-compatible object storage. Functions are real Linux containers running your language's own runtime — Node.js, Go, Python, or Java (Quarkus) — with HTTP as the only trigger. Configuration is declarative through `func.toml` or `telnyx.toml` manifests, deployment is via the `telnyx-edge` CLI, and the platform handles scaling, cold starts, revisions, and rollback automatically.

## Overview

Telnyx Edge Compute is a platform of compute primitives for building and deploying applications to the Telnyx edge. The core primitive is a **function**: an ordinary HTTP server packaged as a container, deployed to Telnyx's global edge network, and served at its own public URL. Functions are real Linux containers running your language's own runtime — Node.js, Go, Python, or Java (Quarkus) — so the bulk of your "runtime API" is just the standard library and any dependency you install.

The platform adds a small, explicit set of capabilities on top:

- **Bindings** — declared connections to platform resources (the Telnyx API, secrets, KV, object storage, and Stateful Actors) with credentials injected for you.
- **Stateful Actors** — durable per-entity state and coordination: one instance per name, one call at a time.
- **KV** — globally distributed key-value storage with server-side TTL.
- **CloudFS** — a POSIX filesystem you mount on any host or container, backed by Telnyx Cloud Storage.
- **Object storage** — S3-compatible buckets for files and media.
- **Edge Network** — private WireGuard-based mesh networking.

HTTP is the only trigger today — there are no cron, queue, or event triggers. For scheduled work, call the function's URL from an external scheduler (a GitHub Actions cron job is enough), or use a [Stateful Actor](stateful-actors.md) alarm.

## Quickstart

Install the CLI, authenticate, scaffold, ship, and curl a live URL. The CLI ships as GitHub release binaries only — it is not on npm and there is no Homebrew formula. Assets are version-stamped; there is no un-versioned "latest" asset.

```
VERSION=v0.2.5
curl -fsSL "https://github.com/team-telnyx/edge-compute/releases/download/${VERSION}/telnyx-edge-${VERSION}-linux-amd64.tar.gz" | tar xz
sudo mv "telnyx-edge-${VERSION}-linux-amd64/telnyx-edge" /usr/local/bin/
telnyx-edge --version
```

Authenticate before creating a function — `new-func` registers the function with the platform, which requires credentials:

```
telnyx-edge auth login                       # OAuth 2.0 in the browser
telnyx-edge auth api-key set "KEY..."        # persist a Telnyx API key instead
telnyx-edge auth status                      # who am I, and does the token work
```

The CLI does not read a `TELNYX_API_KEY` environment variable. In CI, run `telnyx-edge auth api-key set "$TELNYX_API_KEY"` as a pipeline step. Credentials persist to `~/.telnyx-edge/config.toml`.

Scaffold a function. `new-func` creates the function server-side, writes the assigned UUID into `func.toml`, and scaffolds a working project:

```
telnyx-edge new-func -l ts -n hello
cd hello
npm install
```

Ship it:

```
telnyx-edge ship
# 📡 Your function is live at:
#    https://hello-<org>.telnyxcompute.com
```

Every function gets a URL of the form `{func-name}-{org-nickname}.telnyxcompute.com`. Each successful ship creates an immutable revision you can roll back to.

## The Entrypoint Contract

What "handling a request" means differs by language:

| Language | `new-func -l` | Entrypoint | Server owned by |
| --- | --- | --- | --- |
| TypeScript | `ts` | `index.ts` — your own `node:http` server on `process.env.PORT \|\| 8080` | You |
| JavaScript | `js` | `index.js` — same contract as TypeScript | You |
| Go | `go` | `handler.go` — exported `Handle(w, r)` in `package function` | Platform |
| Python | `python` | `function/func.py` — ASGI `new()` factory | Platform |
| Java | `quarkus` | Quarkus Funqy `@Funq` method | Quarkus |

In TypeScript and JavaScript you own and run the HTTP server. Two things are contractual: listen on `process.env.PORT` (falling back to 8080), and answer `/health` (and paths under it) with a 200. The platform's liveness and readiness probes hit it — a function that doesn't answer isn't routed traffic and can be restarted. Keep the probe path fast: respond before any other work.

In Go, Python, and Java the server is run for you and your code is called per request. Go exports `Handle(w, r)` in `package function` with no `main()`. Python exposes a module-level `new()` factory returning an object with `async def handle(self, scope, receive, send)`. Java uses Quarkus Funqy with a method annotated `@Funq`.

Bodies pass through raw, both directions — there is no base64 envelope and no JSON wrapping between the caller and your code. Headers are yours. Bodies are size-capped at 10 MB request and 10 MB response.
