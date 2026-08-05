---
title: KV
summary: KV is a globally distributed key-value store built for read-heavy edge workloads
  such as session data, cached responses, and feature flags. It stores opaque bytes
  under string keys and is reachable from TypeScript edge functions via an `env` binding
  or from any language via the REST API.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/kv
- url: https://developers.telnyx.com/docs/edge-compute/kv/best-practices
- url: https://developers.telnyx.com/docs/edge-compute/kv/cli
- url: https://developers.telnyx.com/docs/edge-compute/kv/concepts/how-kv-works/index
- url: https://developers.telnyx.com/docs/edge-compute/kv/examples/api-response-caching
- url: https://developers.telnyx.com/docs/edge-compute/kv/examples/feature-flags
- url: https://developers.telnyx.com/docs/edge-compute/kv/examples/session-storage/index
- url: https://developers.telnyx.com/docs/edge-compute/kv/pricing/index
- url: https://developers.telnyx.com/docs/edge-compute/kv/quick-start
- url: https://developers.telnyx.com/docs/edge-compute/kv/reference/index
- url: https://developers.telnyx.com/docs/edge-compute/kv/reference/kv-namespace
- url: https://developers.telnyx.com/docs/edge-compute/kv/ttl-and-metadata
updated_at: 2026-08-05T13:41:30Z
---

# KV

*Part 4 of 4 — see also: [Part 1](kv--part-1.md), [Part 2](kv--part-2.md), [Part 3](kv--part-3.md)*

KV is a globally distributed key-value store built for read-heavy edge workloads such as session data, cached responses, and feature flags. It stores opaque bytes under string keys and is reachable from TypeScript edge functions via an `env` binding or from any language via the REST API.

## Examples

### Session Storage

Store user sessions at the edge and expire them after a day. This uses the KV binding (bound as `MY_KV`) with a **server-side TTL**: pass `expirationTtl` on the write and KV deletes the session automatically once it elapses. Each write renews the TTL, so an active session slides forward and an abandoned one expires. Requires `@telnyx/edge-runtime` ≥ 0.2.2.

```
import { env } from "@telnyx/edge-runtime";

const SESSION_TTL = 86_400; // 24 hours

interface Session {
    created: number;
    views: number;
}

export async function handler(request: Request): Promise<Response> {
    const sessionId = request.headers.get("X-Session-ID");
    if (!sessionId) {
        return new Response("Missing X-Session-ID", { status: 400 });
    }
    const key = `session/${sessionId}`;

    // Read session (null if missing or expired)
    const existing = await env.MY_KV.get<Session>(key, { type: "json" });
    const data = existing
        ? { ...existing, views: existing.views + 1 }
        : { created: Date.now(), views: 0 };

    // Store with a 24h server-side TTL — renewed on every write
    await env.MY_KV.put(key, JSON.stringify(data), { expirationTtl: SESSION_TTL });

    return new Response(JSON.stringify(data), {
        headers: { "Content-Type": "application/json" },
    });
}
```

Non-TypeScript functions get the same behavior with the `ttl_secs` parameter on a REST API write. If you need to inspect *when* a session expires, use the application-level envelope instead.

### API Response Caching

Cache expensive upstream responses for a few minutes. This uses the KV binding (bound as `MY_KV`) with a **server-side TTL**: pass `expirationTtl` on the write and KV deletes the key automatically once it elapses — no cleanup code. Requires `@telnyx/edge-runtime` ≥ 0.2.2.

```
import { env } from "@telnyx/edge-runtime";

const CACHE_TTL = 300; // 5 minutes

export async function handler(request: Request): Promise<Response> {
    const cacheKey = `cache/api${new URL(request.url).pathname}`;

    // null once the TTL has elapsed (or if never cached)
    const cached = await env.MY_KV.get(cacheKey);
    if (cached !== null) {
        return new Response(cached, { headers: { "X-Cache": "HIT" } });
    }

    const upstream = await fetch("https://api.example.com/data");
    const data = await upstream.text();

    await env.MY_KV.put(cacheKey, data, { expirationTtl: CACHE_TTL });

    return new Response(data, { headers: { "X-Cache": "MISS" } });
}
```

Non-TypeScript functions get the same behavior with the `ttl_secs` parameter on a REST API write.

### Feature Flags

Read flags on the request path — no expiry needed, so use the KV binding (`env.MY_KV`) directly.

```
import { env } from "@telnyx/edge-runtime";

export async function handler(request: Request): Promise<Response> {
    const newUiEnabled = await env.MY_KV.get("flag/new-ui");

    // Swap in whatever each branch should serve.
    return newUiEnabled === "true"
        ? new Response("new UI")
        : new Response("old UI");
}
```

Flip a flag without redeploying — from the CLI:

```
telnyx-edge storage kv key put <namespace-id> flag/new-ui true
```

## Pricing

KV pricing is based on operations and storage. Egress is free.

| Resource | Free Tier | Paid |
| --- | --- | --- |
| Reads | 10M/month | $0.35/million |
| Writes | 1M/month | $3.50/million |
| Deletes | 1M/month | $3.50/million |
| Lists | 1M/month | $3.50/million |
| Storage | 1 GB/month | $0.35/GB-month |

Egress is free. No charges for data transferred out of KV.

## Related Resources

- [Bindings](bindings.md) — How the `env` binding surface works
- [Secrets](secrets.md) — Secure credential storage
