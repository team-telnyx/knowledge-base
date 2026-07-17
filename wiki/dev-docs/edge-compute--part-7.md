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

*Part 7 of 7 — see also: [Part 1](edge-compute--part-1.md), [Part 2](edge-compute--part-2.md), [Part 3](edge-compute--part-3.md), [Part 4](edge-compute--part-4.md), [Part 5](edge-compute--part-5.md), [Part 6](edge-compute--part-6.md)*

Telnyx Edge Compute is a platform of compute primitives for building and deploying applications to the Telnyx edge. The core primitive is a function: an ordinary HTTP server packaged as a container, deployed to Telnyx's global edge network, and served at its own public URL. The platform adds bindings (pre-authenticated handles to the Telnyx API, secrets, KV, object storage, and Stateful Actors), durable per-entity state via Stateful Actors, globally distributed key-value storage via KV, a mountable POSIX filesystem via CloudFS, and S3-compatible object storage. Functions are real Linux containers running your language's own runtime — Node.js, Go, Python, or Java (Quarkus) — with HTTP as the only trigger. Configuration is declarative through `func.toml` or `telnyx.toml` manifests, deployment is via the `telnyx-edge` CLI, and the platform handles scaling, cold starts, revisions, and rollback automatically.

## Local Development

An Edge Compute function is an ordinary program in a container, not code inside a proprietary runtime. Local development is unremarkable: run the program, `curl localhost:8080`, iterate, then `telnyx-edge ship`.

| Language | Serve locally | Test |
| --- | --- | --- |
| TypeScript | `npm run build && npm start` | `node --test` |
| JavaScript | `node index.js` | `node --test` |
| Python | `uvicorn app:app --port 8080 --interface asgi3 --lifespan off` | `pytest` |
| Go | `go run ./cmd/local` | `go test ./...` |
| Java (Quarkus) | `./mvnw quarkus:dev` | `./mvnw test` |

The `env` binding surface resolves only inside a deployed function. A standalone function has no local binding emulation — to exercise binding-backed code paths, ship to a scratch function and curl its live URL. Plain environment variables are the exception: secrets created with `telnyx-edge secrets add` are injected as environment variables, and declaring a `[telnyx]` binding injects `TELNYX_API_KEY`. Code that reads plain env vars works locally by exporting the same names.

Stateful Actor projects are the exception: `telnyx-edge dev` runs their actor stack locally so `env.<BINDING>` calls resolve. It generates the actor stack your project needs, boots it in Docker, serves your `fetch` handler on a local port, and hot-reloads on save. Actor state lives in the stack's Postgres store, so it survives a reload.

## CLI Reference

| Command | What it does |
| --- | --- |
| `auth` | Log in via OAuth or API key; check or clear credentials |
| `new-func` | Scaffold a project and register the function server-side |
| `ship` | Upload, build, and deploy a function |
| `list` | List your functions with status and invoke URL |
| `inspect` | One function's full details and actor bindings |
| `status` | CLI self-diagnostics: config, auth, connectivity |
| `revisions` | A function's deploy history |
| `rollback` | Retarget traffic to a previous revision |
| `secrets` | Manage organization-scoped secrets |
| `bindings` | Manage the org-level Telnyx API credential |
| `types` | Generate `telnyx-env.d.ts` from the project manifest |
| `storage` | Manage KV namespaces and keys |
| `actors` | Manage account-scoped Stateful Actor types |
| `reset-func` | Return a failed function to the `created` state |
| `delete-func` | Delete a function permanently |

Global flags: `-h`/`--help` for help on any command, `-v`/`--verbose` for verbose logging, `--version` to print the CLI version. Credentials persist in `~/.telnyx-edge/config.toml`.
