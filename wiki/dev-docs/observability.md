---
title: Observability
summary: 'Edge Compute has no built-in telemetry surface, so observability is assembled
  from three pieces: the CLI''s control-plane views, a function''s own health endpoint,
  and structured events the function emits over HTTPS to a collector you run.'
sources:
- url: https://developers.telnyx.com/docs/edge-compute/observability/index
updated_at: 2026-08-05T13:40:53Z
---

# Observability

Edge Compute has no built-in telemetry surface, so observability is assembled from three pieces: the CLI's control-plane views, a function's own health endpoint, and structured events the function emits over HTTPS to a collector you run.

## Control-plane visibility

The CLI answers "is it deployed, and where does it answer" — not "what is it doing":

| Command | What it tells you |
| --- | --- |
| `telnyx-edge ship` | Build and deploy progress for one revision, ending in the live URL — build and deploy failures surface here |
| `telnyx-edge list` | Every function: id, name, status, creation time, invoke URL |
| `telnyx-edge inspect <function>` | One function's status, invoke URL, timestamps, and actor bindings — accepts a name or an id |
| `telnyx-edge revisions list <function>` | Deploy history, newest first — each successful ship is an immutable revision you can [roll back to](versions.md) |
| `telnyx-edge status` | CLI self-diagnostics: config file, authentication, connectivity to `api.telnyx.com` — it checks your CLI, not your functions |

Add `-v` to any command for verbose client-side logging when a command itself misbehaves. None of this shows requests, errors, or output from the running container.

## Health checks

The scaffolded TypeScript and JavaScript entrypoints answer `/health` before any other routing:

```ts
// index.ts — the scaffold's fast path
if (req.url === '/health' || req.url?.startsWith('/health/')) { res.writeHead(200); res.end(); return; }
```

Keep this route dependency-free — no KV reads, no outbound calls — so an external checker can tell "function down" apart from "dependency down". The Quarkus scaffold serves `/health` through SmallRye Health; in Go and Python, add an equivalent route yourself. HTTP is the only trigger, so probing is external by design: point an uptime monitor — or a scheduled job such as a GitHub Actions cron — at `https://<func-name>-<org>.telnyxcompute.com/health`.

## Emit events to a sink you run

Since nothing shows you a running function's output, the pattern is to send structured events over HTTPS to a collector you control — any log store with an HTTP ingest endpoint works. Store the collector's credential as a [secret](secrets.md), never in code.

Declare the secret in `func.toml` and store its value:

```toml
[secrets](secrets.md)
binding = "LOG_SINK_KEY"   # the handle you pass to env.SECRETS.get()
name    = "LOG_SINK_KEY"   # the secret's name from `secrets add`
```

```
telnyx-edge secrets add LOG_SINK_KEY "<your collector's API key>"
telnyx-edge types   # regenerate telnyx-env.d.ts so the handle type-checks
```

Then instrument the entrypoint. This emits one event per request — off the critical path, with a deadline, and never able to fail the response:

```ts
import * as http from "node:http";
import { randomUUID } from "node:crypto";
import { env } from "@telnyx/edge-runtime";

const SINK_URL = "https://logs.example.com/ingest"; // your collector

function emit(event: Record<string, unknown>): void {
  // Fire-and-forget: telemetry must never delay or fail a response.
  void (async () => {
    const key = await env.SECRETS.get("LOG_SINK_KEY");
    await fetch(SINK_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json", Authorization: `Bearer ${key}` },
      body: JSON.stringify({ ts: new Date().toISOString(), ...event }),
      signal: AbortSignal.timeout(2000), // a slow sink must not pile up sockets
    });
  })().catch(() => {}); // a dead sink must not take the function with it
}

const server = http.createServer((req, res) => {
  if (req.url === "/health" || req.url?.startsWith("/health/")) { res.writeHead(200); res.end(); return; }

  const requestId = (req.headers["x-request-id"] as string) ?? randomUUID();
  const start = Date.now();
  res.setHeader("X-Request-ID", requestId);

  res.on("finish", () => {
    emit({
      level: res.statusCode < 500 ? "info" : "error",
      requestId,
      method: req.method,
      path: req.url,
      status: res.statusCode,
      durationMs: Date.now() - start,
    });
  });

  res.writeHead(200, { "Content-Type": "application/json" });
  res.end(JSON.stringify({ ok: true, requestId }));
});

server.listen(process.env.PORT || 8080);
```

What makes this pattern hold up:

- **Propagate a request id.** Read `X-Request-ID` or generate one, return it in the response, and attach it to every event — a user-reported failure becomes findable in your sink.
- **Log metadata, not payloads.** Method, path, status, duration. Never secret values, and not full request bodies, which may carry PII.
- **Buffering trades loss for volume.** The per-request emit above is the simple, safe default. If volume demands batching, remember events buffered in memory are gone when the container stops — see [Execution Model](execution-model.md) for the container lifecycle.

The `env.SECRETS` binding is TypeScript-only, but secrets are also injected as plain environment variables into every function, so the same pattern works in any runtime: read the key from the environment (`os.Getenv("LOG_SINK_KEY")` in Go, `os.environ` in Python) and POST JSON to your sink.

## Next steps

- [Best Practices](best-practices.md) — error handling and outbound-call deadlines the emitter should respect
- [Limits](limits.md) — the 30 s default / 60 s max request budget your telemetry lives inside
- [Secrets](secrets.md) — both access surfaces for the sink credential
- [CLI Reference](cli-reference--part-1.md) — full flags for `list`, `inspect`, `status`, and `revisions`
