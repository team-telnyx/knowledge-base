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

*Part 1 of 3 — see also: [Part 2](runtime-apis--part-2.md), [Part 3](runtime-apis--part-3.md)*

Edge Compute functions are real Linux containers running native language runtimes (Node.js, Go, Python, Java/Quarkus). The platform adds a small, explicit layer on top: an execution environment with cold starts, warm reuse, and a request budget; a per-language entrypoint contract for handling HTTP requests; and bindings that inject credentials for the Telnyx API, secrets, KV, object storage, SQL databases, and stateful actors.

## Overview

Edge Compute functions are real Linux containers running your language's own runtime — Node.js, Go, Python, or Java (Quarkus). The bulk of the "runtime API" is just the standard library and any dependency you install, exactly as it behaves on any Linux box. The platform adds a small, explicit layer on top:

- **An execution environment** — how containers start, stay warm, scale, and get a request budget.
- **An entrypoint contract** — which file the platform runs and how a request reaches your code, per language.
- **Bindings** — declared connections to platform resources (the Telnyx API, secrets, KV, object storage, SQL databases, and stateful actors) with credentials injected for you.

Everything else — HTTP parsing, crypto, file I/O, database drivers — comes from your language, not from the platform.

## Real containers

Because a function is a real container:

- **Native runtimes** — Node.js, Go, Python, and Java (Quarkus) run as themselves. No fetch-only sandbox, no restricted language subset.
- **Any dependency that installs** — npm packages, Go modules, PyPI packages, Maven artifacts.
- **POSIX environment** — environment variables, plus file I/O in the working directory and `/tmp`. The root filesystem is read-only and writes are ephemeral — they don't survive the container being recycled, so persist real data in [KV](kv--part-1.md) or a [Cloud Storage](cloud-storage.md) bucket.
- **Outbound network** — HTTP clients, TCP sockets, DNS resolution.

The trade-off is container lifecycle: instances cold-start, stay warm between requests, and are recycled. See [Execution Model](execution-model.md) for what that means for initialization and in-memory state.

## Execution model

An Edge Compute function is a Linux container running an HTTP server — one you run yourself in TypeScript and JavaScript, one run for you in Go, Python, and Java. The platform starts containers when traffic arrives, reuses them while it continues, and reclaims them — down to zero — when it stops.

### Request path

1. **Route** — a request to `https://<func-name>-<func-id-prefix>.telnyxcompute.com` reaches the platform (see [Routing](routing.md)).
2. **Place** — a warm container takes it, or a new one starts (a cold start).
3. **Execute** — the server process handles the request and writes the response.
4. **Keep warm** — the container stays up for subsequent requests until it is recycled.

### Cold start

A cold start is the first request's cost of a new container: the image starts, the language runtime boots, your module-level code runs, and then the request is served. Put expensive setup — HTTP clients, connection pools, parsed config — at module scope so it runs once per container instead of once per request:

```ts
import * as http from "node:http";

// Module scope — runs once per container, at cold start
const startedAt = Date.now();
const cache = new Map<string, string>(); // per-container cache — not durable

const server = http.createServer((req, res) => {
  // Handler scope — runs per request
  res.writeHead(200, { "Content-Type": "application/json" });
  res.end(JSON.stringify({ containerAgeMs: Date.now() - startedAt }));
});

server.listen(process.env.PORT || 8080);
```

Curl that function twice: a near-zero `containerAgeMs` means the request paid a cold start; a growing one means the container was reused. The same split exists in every runtime — package-level `var`s and `init()` in Go, module scope or the optional `start(cfg)` hook in Python, application-scoped state in Quarkus. The per-language entrypoint contracts are in [HTTP Handler](http-handler.md).

### Warm reuse

While traffic continues, requests land on existing containers and skip initialization. Module state persists between requests **on the same container** — treat it as a cache keyed by container, nothing more. Two requests may or may not share a container, and the platform gives you no way to control which.

### Recycling and scale to zero

Containers are reclaimed without notice: after idling, when a new revision is shipped (`telnyx-edge ship` — see [Versions](versions.md)), or by platform scaling decisions. At zero traffic a function scales to zero containers; the next request pays a cold start. Treat container memory like a process that can be killed at any instant: only what you wrote to durable storage is real. In Python, your function class may define an optional `stop()` hook, called on scale-down or update — use it for best-effort cleanup, never for durability.

### Scaling

The platform scales the container count with concurrent load. There is no concurrency knob to configure — scaling is automatic.

| Traffic pattern | Platform response |
| --- | --- |
| Spike | New containers start — expect cold starts |
| Sustained | Containers stay warm |
| Falling | Containers are gradually reclaimed |
| Zero | Scale to zero after an idle period |

### Request timeout

A function must respond within **30 seconds** by default, **60 seconds** maximum; a request that exceeds the budget is terminated with a `504`. There is no `func.toml` field for this — see [Limits](limits.md) for the full table. Budget outbound calls below the deadline so you return a real error instead of being cut off:

```ts
const upstream = await fetch("https://api.example.com/data", {
  signal: AbortSignal.timeout(25_000), // fail at 25 s, inside the 30 s budget
});
```

### Triggers

**HTTP is the only trigger** — there are no cron, queue, or event triggers. A Telnyx webhook (a messaging profile or Call Control application pointed at your function URL) is just an HTTP request, so your function handles it like any other — see [Receiving Messages](receiving-messages.md) and [Handling Calls](handling-calls.md). For periodic work, call the URL from an external scheduler (a GitHub Actions cron job is enough), or use a [Stateful Actors](stateful-actors--part-1.md) alarm to fire a callback on the platform itself.

### Where state lives

Module state dies with the container, so anything that must survive needs a home:

| Data | Use | Why |
| --- | --- | --- |
| Per-entity state, counters, coordination | [Stateful Actors](stateful-actors--part-1.md) (Beta) | One instance per name, serialized calls, durable writes — correct under concurrency |
| Cache entries, config, feature flags, sessions | [KV](kv--part-1.md) | Globally distributed reads; opaque values up to 1 MiB with optional TTL |
| Files, media, large objects | [Cloud Storage](cloud-storage.md) buckets | S3-compatible object storage |

Don't build counters or per-entity coordination on KV — concurrent read-modify-write races there, which is exactly the problem Stateful Actors exist to solve.
