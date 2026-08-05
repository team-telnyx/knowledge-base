---
title: Edge Compute Best Practices
summary: Operational guidance for building reliable, performant, and secure functions
  on Telnyx Edge Compute, covering configuration, performance, state placement, reliability,
  security, and observability.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/best-practices/index
updated_at: 2026-08-05T13:39:50Z
---

# Edge Compute Best Practices

*Part 1 of 2 — see also: [Part 2](edge-compute-best-practices--part-2.md)*

Operational guidance for building reliable, performant, and secure functions on Telnyx Edge Compute, covering configuration, performance, state placement, reliability, security, and observability.

## Configuration

### Keep Secrets Out of Code

Store credentials as secrets — the CLI takes the key and value as positional arguments:

```
telnyx-edge secrets add API_KEY "sk-..."
```

Every secret is injected into your functions as a plain environment variable, so this works in any language:

```
const apiKey = process.env.API_KEY;
```

TypeScript projects that declare a `[secrets](secrets.md)` binding in `func.toml` can also read it through `env.SECRETS.get("<handle>")`, which `telnyx-edge types` type-checks against the declared handles. Both surfaces are live at the same time — see [Secrets](secrets.md).

### Budget for the Platform Timeout

The request timeout is **30 seconds by default and 60 seconds at most** — there is no `func.toml` field that raises it. A request that exceeds it is terminated with a `504`. Set your own deadlines on outbound calls a few seconds below the platform's so you fail with a useful error instead (see [Time Out and Retry Outbound Calls](#time-out-and-retry-outbound-calls)), and split work that genuinely needs longer. Exact numbers: [Limits](limits.md).

### Name Functions for Their URL

The function name becomes the hostname — `{func-name}-{func-id-prefix}.telnyxcompute.com` — and `new-func` registers the function with the platform at scaffold time, so pick the name up front:

```
# Good — the URL says what it serves
telnyx-edge new-func -l ts -n user-api

# Bad — you'll be curling https://test-yourorg.telnyxcompute.com in production
telnyx-edge new-func -l ts -n test
```

## Performance

### Initialize Once, at Module Scope

A container serves many requests. Module scope runs once per container; the request callback runs per request. Build clients, load config, and compile anything expensive outside the callback:

```
import * as http from "node:http";

// Once per container — reused across requests
const client = new SomeApiClient({ timeout: 5000 });

const server = http.createServer(async (req, res) => {
  // Per request — keep construction out of here
  const data = await client.get("/data");
  res.writeHead(200, { "Content-Type": "application/json" });
  res.end(JSON.stringify(data));
});

server.listen(process.env.PORT || 8080);
```

The same rule holds everywhere: package-level variables in Go, module-level objects in Python.

### Keep Cold Starts Small

A new container starts when traffic scales up or after a deploy, and the first request it serves waits for everything before `server.listen` — imports, client construction, config loads. Keep dependencies minimal, and lazy-load heavy libraries used only on rare paths so the common path doesn't pay for them.

### Cache Expensive Reads in KV

Declare a KV namespace in `func.toml` and it resolves as a binding on `env`:

```
# func.toml
[storage.kv.CACHE]
id = "550e8400-e29b-41d4-a716-446655440000"  # from `telnyx-edge storage kv create`
```

```
import { env } from "@telnyx/edge-runtime";

async function getUser(userId: string) {
  const cached = await env.CACHE.get<User>(`user/${userId}`, { type: "json" });
  if (cached) return cached;

  const user = await fetchUserFromDb(userId);
  await env.CACHE.put(`user/${userId}`, JSON.stringify(user), { expirationTtl: 300 }); // seconds
  return user;
}
```

Two contracts to know:

- `expirationTtl` is server-side expiry in whole seconds (≥ 1) and requires `@telnyx/edge-runtime` **≥ 0.2.2** — earlier versions accept the option and silently ignore it.
- Keys allow `a-z` `A-Z` `0-9` `-` `_` `/` `=` `.` and **forbid colons** — write `user/123`, not `user:123`.

More in [KV Best Practices](kv-best-practices.md).

## Put State Where It Belongs

Containers come and go, and concurrent requests can land on different containers — anything kept in process memory is a cache at best. Pick the store by the shape of the data:

| Data | Use | Why |
| --- | --- | --- |
| Per-entity state, counters, coordination | [Stateful Actors](stateful-actors--part-1.md) | One instance per name, one call at a time — read-modify-write without races |
| Caches, config, feature flags | [KV](kv--part-1.md) | Small values (≤ 1 MiB), fast reads, last-write-wins |
| Files and large blobs | [Storage buckets](storage-buckets.md) | S3-compatible object storage |

Don't build counters, locks, or rate limiters on KV: it has no transactions or compare-and-swap, and concurrent writers to one key are last-write-wins. That job is exactly what [Stateful Actors](stateful-actors--part-1.md) exist for. Full comparison: [Execution Model](execution-model.md).

## Reliability

### Make Handlers Idempotent

Clients retry and webhooks are redelivered, so design handlers where processing the same request twice has the same effect as once. Key side effects on a caller-supplied identifier — a webhook event id, an `Idempotency-Key` header — and skip work already done. If the duplicate check itself must be race-free, do it inside a [Stateful Actor](stateful-actor.md); a check-then-act on KV can race.

### Keep the Health Endpoint Fast

The scaffolds answer `/health` before any other routing:

```
if (req.url === "/health" || req.url?.startsWith("/health/")) {
  res.writeHead(200);
  res.end();
  return;
}
```

Keep that property: return immediately and never call a dependency from it, so a slow upstream can't make your function look down.

### Catch Everything at the Top of the Handler

Your function is one process. An exception that escapes the request callback — including an unhandled promise rejection — crashes it, drops every in-flight request, and makes the next request pay a cold start. Wrap the whole handler body:

```
const server = http.createServer(async (req, res) => {
  try {
    // ... handle the request
  } catch (err) {
    console.error("request failed:", err);
    res.writeHead(500, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ error: "internal error" }));
  }
});
```

### Time Out and Retry Outbound Calls

Don't let a slow upstream ride you into the platform's 30-second `504` — set an explicit deadline on every outbound call:

```
const response = await fetch("https://api.example.com/data", {
  signal: AbortSignal.timeout(5000),
});
```

Retry only network failures and `5xx` responses, with exponential backoff, and keep the total budget under the platform timeout:

```
async function fetchWithRetry(url: string, attempts = 3): Promise<Response> {
  for (let i = 0; ; i++) {
    try {
      const res = await fetch(url, { signal: AbortSignal.timeout(5000) });
      if (res.status < 500) return res; // success or client error — don't retry 4xx
      if (i === attempts - 1) return res;
    } catch (err) {
      if (i === attempts - 1) throw err;
    }
    await new Promise((r) => setTimeout(r, 2 ** i * 100)); // 100 ms, 200 ms, 400 ms
  }
}
```

## Security

- **Validate input before use** — check required fields and types, reject with `400`. Nothing between the internet and your handler does it for you.
- **HTTPS only** for outbound calls.
- **Never log secret values** — and don't log full request bodies, which may carry PII. Log metadata: method, path, status, duration.
- **Authenticate anything that mutates state** — your function URL is public. Require a token or shared secret (stored as a [secret](secret.md), checked in the handler) before acting on a request.

## Observability

There is no logs command and no metrics dashboard today. What you have is the output of `ship`, `status`, and `inspect` — plus whatever your function emits itself. So emit deliberately:

- **Send structured events over HTTP to a sink you control** (a log aggregator, your own collector) if you need request-level visibility. There is no surface that shows you `console.log` output.
- **Propagate a request id** — read `X-Request-ID` or generate one, return it in the response, and attach it to every event you emit, so a user-reported failure is findable in your sink.

Patterns and sink examples: [Observability](observability.md).
