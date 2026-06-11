---
title: KV
summary: KV is a globally distributed key-value store designed for low-latency reads
  from Telnyx edge functions. It supports namespace isolation, TTL-based expiration,
  JSON metadata, and eventual consistency with read-after-write guarantees within
  the same region.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/kv
- url: https://developers.telnyx.com/docs/edge-compute/kv/api-reference
- url: https://developers.telnyx.com/docs/edge-compute/kv/cli
- url: https://developers.telnyx.com/docs/edge-compute/kv/pricing
- url: https://developers.telnyx.com/docs/edge-compute/kv/quick-start/index
- url: https://developers.telnyx.com/docs/edge-compute/kv/ttl-and-metadata
- url: https://developers.telnyx.com/docs/edge-compute/kv/use-cases
updated_at: 2026-06-11T10:27:17Z
---

# KV

*Part 2 of 2 — see also: [Part 1](kv--part-1.md)*

KV is a globally distributed key-value store designed for low-latency reads from Telnyx edge functions. It supports namespace isolation, TTL-based expiration, JSON metadata, and eventual consistency with read-after-write guarantees within the same region.

## TTL and Metadata

### Key Expiration (TTL)

KV supports automatic key expiration. Expired keys are automatically deleted and return 404 on read. There are two ways to set expiration:

| Option | Description | Example |
|--------|-------------|----------|
| `expiration_ttl` | Seconds from now until expiration (min: 60) | `3600` = 1 hour |
| `expiration` | Unix timestamp when key expires | `1704067200` |

The minimum TTL is 60 seconds. Keys with a TTL less than 60 seconds will be rejected.

API example with TTL:

```bash
curl -X PUT "https://api.telnyx.com/v2/storage/kvs/{id}/keys/session:abc" \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "value": "c2Vzc2lvbiBkYXRh",
    "expiration_ttl": 3600
  }'
```

CLI example with expiration timestamp:

```bash
telnyx-edge storage kv key put <namespace-id> promo:sale "data" --expiration 1704067200
```

Common TTL use cases:

- **Sessions** — Expire after 24 hours of inactivity
- **Cache** — Expire after 5 minutes to ensure freshness
- **Rate limiting** — Expire counters after the rate limit window
- **Temporary tokens** — Auto-cleanup verification codes

### Metadata

Attach JSON metadata to keys for filtering, tagging, and context. Metadata is returned with the key on read. Metadata must be valid JSON and cannot exceed 1KB when serialized.

API example with metadata:

```bash
curl -X PUT "https://api.telnyx.com/v2/storage/kvs/{id}/keys/user:123" \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "value": "eyJuYW1lIjoiQWxpY2UifQ==",
    "metadata": {
      "type": "user",
      "source": "signup",
      "version": 2
    }
  }'
```

Common metadata use cases:

- **Versioning** — Track schema versions for migrations
- **Tagging** — Categorize keys by type, source, or owner
- **Debugging** — Store creation context (who, when, why)
- **Filtering** — Future: filter list operations by metadata

## Use Cases

### Session Storage

Store user sessions at the edge with automatic expiration (24-hour TTL example):

```javascript
const SESSION_TTL = 86400; // 24 hours

async function handler(request) {
    const sessionId = request.headers.get("X-Session-ID");
    let session = await kvGet(`session:${sessionId}`);
    if (!session) {
        session = JSON.stringify({ created: Date.now(), views: 0 });
    } else {
        const data = JSON.parse(session);
        data.views++;
        session = JSON.stringify(data);
    }
    await kvPutWithTTL(`session:${sessionId}`, session, SESSION_TTL);
    return new Response(session);
}
```

### API Response Caching

Cache expensive API responses with automatic expiration (5-minute TTL example):

```javascript
const CACHE_TTL = 300; // 5 minutes

async function handler(request) {
    const cacheKey = `api:${new URL(request.url).pathname}`;
    const cached = await kvGet(cacheKey);
    if (cached) {
        return new Response(cached, { headers: { "X-Cache": "HIT" } });
    }
    const response = await fetch("https://api.example.com/data");
    const data = await response.text();
    await kvPutWithTTL(cacheKey, data, CACHE_TTL);
    return new Response(data, { headers: { "X-Cache": "MISS" } });
}
```

### Feature Flags

Store and retrieve feature flags:

```javascript
async function handler(request) {
    const newUIEnabled = await kvGet("feature:new-ui");
    if (newUIEnabled === "true") {
        return serveNewUI(request);
    }
    return serveOldUI(request);
}
```

## Best Practices

### Key Naming

Use structured key names with prefixes:

```
user:123              # User data
session:abc           # Session data
cache:api:/users      # Cached API response
flag:new-feature      # Feature flag
```

### Value Serialization

Always serialize complex values as JSON before base64 encoding:

```javascript
// Write
const value = JSON.stringify({ name: "Alice", age: 30 });
await kvPut("user:123", value);

// Read
const user = JSON.parse(await kvGet("user:123"));
```

### Error Handling

Handle missing keys gracefully — `kvGet` returns `null` for keys that don't exist:

```javascript
const value = await kvGet("possibly-missing-key");
if (value === null) {
    return new Response("Not found", { status: 404 });
}
```

## Pricing

| Resource | Free Tier | Paid |
|----------|-----------|------|
| Reads | 10M/month | $0.35/million |
| Writes | 1M/month | $3.50/million |
| Deletes | 1M/month | $3.50/million |
| Lists | 1M/month | $3.50/million |
| Storage | 1 GB/month | $0.35/GB-month |

Egress is free — there are no charges for data transferred out of KV.

## Related Resources

- [Bindings](bindings.md) — Connect to KV and other services from edge functions
- [SQL DB](sql-db.md) — Relational database for complex queries
- [Secrets](secrets.md) — Secure credential storage
