---
title: Functions Overview
summary: 'A function is the compute primitive of Telnyx Edge Compute: an ordinary
  HTTP server packaged as a container, deployed to Telnyx''s global edge network,
  and served at its own public URL. The platform around it provides key-value storage,
  durable per-entity state, object storage, the Telnyx API, and private networking
  through declarative bindings.'
sources:
- url: https://developers.telnyx.com/docs/edge-compute/overview
updated_at: 2026-08-05T13:41:00Z
---

# Functions Overview

A function is the compute primitive of Telnyx Edge Compute: an ordinary HTTP server packaged as a container, deployed to Telnyx's global edge network, and served at its own public URL. The platform around it provides key-value storage, durable per-entity state, object storage, the Telnyx API, and private networking through declarative bindings.

A function is the compute primitive of Telnyx Edge Compute: an ordinary HTTP server, packaged as a container, deployed to Telnyx's global edge network, and served at its own public URL. You write a server that listens on `PORT`; one command builds and ships it.

```ts
import * as http from "node:http";

const server = http.createServer((req, res) => {
  if (req.url === "/health") { res.writeHead(200); res.end(); return; }
  res.writeHead(200, { "Content-Type": "application/json" });
  res.end(JSON.stringify({ message: "Hello from Telnyx Edge Compute!" }));
});

server.listen(process.env.PORT || 8080);
```

```
telnyx-edge ship
# 📡 Your function is live at:
#    https://demo-0198c2c5-8.telnyxcompute.com
```

On its own, a function just echoes HTTP. What makes it useful is the platform it plugs into — key-value storage, durable per-entity state, object storage, the Telnyx API, and private networking — each declared as a binding and reachable from your handler. The rest of these docs go deep on each piece.

## Quickstart

Install the CLI, scaffold a function, ship it, and curl the live URL — about five minutes.

HTTP is the only trigger today — there are no cron triggers. For scheduled work, call the function's URL from an external scheduler, such as a GitHub Actions cron job.

## The platform around your functions

Declare a binding in `func.toml` and it surfaces on `env` at runtime in TypeScript, or as REST and injected environment variables in every other language. See [Bindings](bindings.md) for the mechanics — these are the products worth reaching for.

### State and storage

- **KV** — Globally distributed key-value storage with server-side TTL — an `env` binding in TypeScript, REST everywhere else. For caches, sessions, and feature flags.
- **Stateful Actors** — Beta — durable per-entity state and coordination: one instance per name, one call at a time. For counters, per-user state, and anything that needs a serialized owner.
- **Object storage** — S3-compatible buckets for files and media — a separate product, reached over its S3 API from any language.

### Connect to Telnyx

- **Telnyx API** — A pre-authenticated client for Voice, Messaging, and AI — or plain REST with the injected key. Answer calls, send messages, and run inference without managing credentials.

## Languages

`telnyx-edge new-func -l <language>` scaffolds a project in TypeScript (`ts`), JavaScript (`js`), Go (`go`), Python (`python`), or Java (`quarkus`). Each language uses its own standard server contract — `node:http`, Go's `http.Handler`, ASGI, Quarkus Funqy — documented in [HTTP handler](http-handler.md).

The binding SDK (`@telnyx/edge-runtime`) — a typed `env` exposing a pre-authenticated Telnyx client, secrets, and KV namespaces — is TypeScript-only today. The other runtimes use the same features over REST and injected environment variables.

## Where your code runs

Functions run on the infrastructure that carries Telnyx voice and messaging traffic: edge sites inside carrier facilities, close to end users rather than in generic cloud availability zones. Each region is backed by multiple independent sites across different providers, with automatic failover if a site goes down.

## Resources

- [HTTP handler](http-handler.md) — The entrypoint contract for each language.
- [Configuration](configuration--part-1.md) — Environment variables, secrets, routing, and versions.
- [CLI reference](cli-reference--part-1.md) — Every `telnyx-edge` command and flag.
- [Limits](limits.md) — Request timeouts, payload sizes, and quotas.
- [Pricing](pricing.md) — Free tier plus usage-based rates for requests and CPU time.
- [Community](community.md) — Ask questions and share what you build.
