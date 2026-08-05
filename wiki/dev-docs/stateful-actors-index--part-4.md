---
title: Stateful Actors - Index
summary: Stateful Actors on Telnyx Edge Compute give each named entity its own durable,
  single-threaded instance with private key/value and SQL storage, alarms, and WebSocket
  support. This page covers when to use them, the storage surfaces, local development,
  the Quick Start, shared actors across functions, and WebSocket patterns.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/guides/storage/key-value/index
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/guides/storage/sql
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/guides/when-to-use
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/local-development
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/quick-start/index
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/shared-actors
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/websockets/index
updated_at: 2026-08-05T13:43:37Z
---

# Stateful Actors - Index

*Part 4 of 7 — see also: [Part 1](stateful-actors-index--part-1.md), [Part 2](stateful-actors-index--part-2.md), [Part 3](stateful-actors-index--part-3.md), [Part 5](stateful-actors-index--part-5.md), [Part 6](stateful-actors-index--part-6.md), [Part 7](stateful-actors-index--part-7.md)*

Stateful Actors on Telnyx Edge Compute give each named entity its own durable, single-threaded instance with private key/value and SQL storage, alarms, and WebSocket support. This page covers when to use them, the storage surfaces, local development, the Quick Start, shared actors across functions, and WebSocket patterns.

## Local Development

A plain Edge Compute function is an ordinary program you run and `curl` directly. A Stateful Actor project is different: the `fetch` handler reaches its actors through an `env.<BINDING>` call, and that binding resolves only against a running actor runtime. There is no in-process emulation to fall back on.

`telnyx-edge dev` supplies the missing runtime. It generates the actor stack your project needs, boots it in Docker, serves your `fetch` handler on a local port, and hot-reloads on save — so `env.<BINDING>` calls hit real actors before you ship.

`telnyx-edge dev` is a development command; it does not deploy anything. When it works locally, ship with `telnyx-edge ship`.

### Prerequisites

- **Docker**, running. The stack is a set of containers booted with `docker compose`.
- **A `telnyx.toml` umbrella project** — the two-export shape: one module that exports an actor class and a `fetch` handler, wired by an `[actors](actors.md)` binding. Run `telnyx-edge dev` from the directory that holds the manifest, or point at it with `-f/--from-dir`. Without a `telnyx.toml`, the command errors:

  ```
  ❌ No project manifest found
  💡 Run 'telnyx-edge dev' from a directory containing a telnyx.toml manifest.
  ```

### The Loop

From an umbrella project directory:

```
telnyx-edge dev
```

This bundles the project, generates the stack under `.telnyx/dev`, and boots it. Your `fetch` handler is served on `http://localhost:8787` (change it with `--port`). Exercise it the same way the Quick Start exercises the deployed URL — but against localhost, and with actors resolving locally:

```
B=http://localhost:8787

curl -sS -X POST $B/accounts/alice/deposit -H 'content-type: application/json' -d '{"amount":100}'
# → {"account":"alice","balance":100}
curl -sS -X POST $B/accounts/alice/debit   -H 'content-type: application/json' -d '{"amount":30}'
# → {"account":"alice","ok":true,"balance":70}
curl -sS $B/accounts/alice/balance
# → {"account":"alice","balance":70}
```

Each `env.ACCOUNT.idFromName(...)` call routes to a real actor instance in the local stack — the same code path that runs deployed. Edit your actor class or `fetch` handler and save; `telnyx-edge dev` watches the source and hot-reloads the affected runtime. Actor state lives in the stack's Postgres store, so it **survives a reload** — `alice` is still `70` after you edit and save.

Press **Ctrl-C** to stop watching. The stack keeps running; the command only detaches the file watcher.

### What the Stack Contains

`telnyx-edge dev` writes the stack under `.telnyx/dev` and runs it with `docker compose`. It is a local stand-in for the deployed platform, containing:

- the **function runtime** — serves your `fetch` handler on the published port;
- the **actor runtime** — hosts your actor instances;
- a **Dapr sidecar** for each runtime, plus **Dapr placement** — the routing layer that sends each actor name to its owner;
- a **Postgres actor state store** — where `ctx.storage` persists, so state survives reloads.

`env.<BINDING>` calls from the function runtime reach the actors in the actor runtime through this layer. This is what a plain `func.toml` function lacks: it has no local binding emulation, so binding-backed code paths only run once deployed.

### Flags

| Flag | Default | Purpose |
| --- | --- | --- |
| `--port int` | `8787` | Host port to publish the function runtime on. |
| `--no-watch` | — | Boot the stack and return, without watching for changes. |
| `--generate-only` | — | Write the stack files under `.telnyx/dev` but do not run `docker compose`. |
| `-f, --from-dir string` | — | Path to the project directory (relative, absolute, or `~/path`). |
| `--function-image string` | `telnyx/function-runtime:dev` | Container image for the function runtime. |
| `--actor-image string` | `telnyx/actor-runtime:dev` | Container image for the actor runtime. |
| `-v, --verbose` | — | Verbose logging. |

Use `--generate-only` to inspect or customize the generated compose stack before booting it, and `--no-watch` when you want the stack up for an out-of-band test run (for example, from a CI script) rather than an interactive edit loop.

### Notes

- **Actor state survives reloads.** Because `ctx.storage` persists to the stack's Postgres store, a hot reload does not reset your instances — balances, counters, and any other state carry across saves. Tear the stack down with `docker compose` (or remove `.telnyx/dev`) when you want a clean slate.
- **Ctrl-C leaves the stack running.** It stops the watcher, not the containers. Stop the stack explicitly with `docker compose` when you're done.
- **A `telnyx.toml` is required.** `telnyx-edge dev` runs umbrella projects. A single-function `func.toml` project has no actors to host.
