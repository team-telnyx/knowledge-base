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

*Part 1 of 2 — see also: [Part 2](kv--part-2.md)*

KV is a globally distributed key-value store designed for low-latency reads from Telnyx edge functions. It supports namespace isolation, TTL-based expiration, JSON metadata, and eventual consistency with read-after-write guarantees within the same region.

## Overview

KV provides the following capabilities:

- **Low-latency reads** — Data accessible from edge locations worldwide
- **Simple API** — `get`, `put`, `delete`, `list` operations
- **Namespace isolation** — Separate key spaces per application
- **Binary-safe storage** — Store any data type (values are base64-encoded)
- **Global distribution** — No region selection; KV is globally replicated
- **TTL support** — Auto-expire keys after a specified duration (minimum 60 seconds)
- **Metadata** — Attach JSON metadata to keys for filtering and context (max 1KB)

### Consistency Model

KV uses **eventual consistency**:

- Writes are immediately visible in the region where they occur
- Changes propagate globally within seconds
- Read-after-write consistency is guaranteed within the same region

For use cases requiring strong consistency, consider using [SQL DB](sql-db.md) instead.

## Quick Start

### 1. Create a Namespace

CLI:

```bash
telnyx-edge storage kv create --name my-cache
```

API:

```bash
curl -X POST https://api.telnyx.com/v2/storage/kvs \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name": "my-cache"}'
```

Namespace creation is asynchronous. Poll the namespace endpoint until `status` changes from `pending` to `provision_ok`.

### 2. Add to Your Function

Configure the binding in `func.toml`:

```toml
[edge_compute]
func_name = "my-function"

[storage.kv.MY_CACHE]
id = "550e8400-e29b-41d4-a716-446655440000"
```

The binding name is injected as environment variables. For a binding named `MY_CACHE`, the variable `KV_MY_CACHE_ID` contains the namespace ID.

### 3. Access KV in Your Code

KV can be accessed via HTTP endpoints. Values must be base64-encoded. Examples in JavaScript:

```javascript
const KV_NAMESPACE_ID = process.env.KV_MY_CACHE_ID;
const API_KEY = process.env.TELNYX_API_KEY;

function toBase64(str) {
    const bytes = new TextEncoder().encode(str);
    let binary = '';
    for (let i = 0; i < bytes.length; i++) {
        binary += String.fromCharCode(bytes[i]);
    }
    return btoa(binary);
}
function fromBase64(b64) {
    const binary = atob(b64);
    const bytes = new Uint8Array(binary.length);
    for (let i = 0; i < binary.length; i++) {
        bytes[i] = binary.charCodeAt(i);
    }
    return new TextDecoder().decode(bytes);
}

async function kvGet(key) {
    const response = await fetch(
        `https://api.telnyx.com/v2/storage/kvs/${KV_NAMESPACE_ID}/keys/${encodeURIComponent(key)}`,
        { headers: { "Authorization": `Bearer ${API_KEY}` } }
    );
    if (response.status === 404) return null;
    if (!response.ok) throw new Error(`KV error: ${response.status}`);
    const data = await response.json();
    return fromBase64(data.data.value);
}

async function kvPut(key, value) {
    const response = await fetch(
        `https://api.telnyx.com/v2/storage/kvs/${KV_NAMESPACE_ID}/keys/${encodeURIComponent(key)}`,
        {
            method: "PUT",
            headers: {
                "Authorization": `Bearer ${API_KEY}`,
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ value: toBase64(value) })
        }
    );
    if (!response.ok) throw new Error(`KV write error: ${response.status}`);
}
```

A native SDK is planned. The intended pattern:

```javascript
import Telnyx from 'telnyx';
const client = new Telnyx({ apiKey: process.env.TELNYX_API_KEY });

const value = await client.storage.kvs.keys.get("kv-abc123", "user:123");
await client.storage.kvs.keys.put("kv-abc123", "user:123", {
  value: "data",
  expirationTtl: 3600,
  metadata: { type: "session" }
});
```

## API Reference

Base URL: `https://api.telnyx.com/v2/storage/kvs`

### Namespace Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/v2/storage/kvs` | Create a new namespace |
| GET | `/v2/storage/kvs` | List all namespaces |
| GET | `/v2/storage/kvs/{id}` | Get namespace details |
| DELETE | `/v2/storage/kvs/{id}` | Delete a namespace |

### Key-Value Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| PUT | `/v2/storage/kvs/{id}/keys/{key}` | Write a value |
| GET | `/v2/storage/kvs/{id}/keys/{key}` | Read a value |
| DELETE | `/v2/storage/kvs/{id}/keys/{key}` | Delete a key |
| GET | `/v2/storage/kvs/{id}/keys` | List keys |

### Namespace Status

| Status | Description |
|--------|-------------|
| `pending` | Provisioning in progress |
| `provision_ok` | Ready to use |
| `provision_failed` | Provisioning failed |
| `deleting` | Deletion in progress |
| `delete_failed` | Deletion failed |
| `deleted` | Fully removed (returns 404) |

### Write Options

| Field | Type | Description |
|-------|------|-------------|
| `value` | string | Base64-encoded value (required) |
| `expiration_ttl` | integer | Seconds until key expires (minimum: 60) |
| `expiration` | integer | Unix timestamp when key expires |
| `metadata` | object | JSON metadata to attach to key (max 1KB) |

### Read Response

The read response returns a JSON object. The `value` field is base64-encoded. The `expiration` and `metadata` fields are only present if they were set on the key:

```json
{
  "data": {
    "key": "my-key",
    "value": "SGVsbG8gV29ybGQ=",
    "metadata": { "type": "user", "created_by": "signup-flow" },
    "expiration": 1704067200
  }
}
```

### List Keys Query Parameters

- `prefix` — Filter keys by prefix
- `page[number]` — Page number (default: 1)
- `page[size]` — Results per page (default: 20, max: 250)

When using curl, pass the `-g` flag to disable glob parsing so square brackets in `page[size]` work correctly.

## CLI Reference

Manage KV namespaces and keys using the `telnyx-edge` CLI.

### Namespace Management

```bash
# List all namespaces
telnyx-edge storage kv list

# Create a namespace
telnyx-edge storage kv create --name my-cache

# Delete a namespace
telnyx-edge storage kv delete <namespace-id>
```

### Key Operations

```bash
# List keys in a namespace
telnyx-edge storage kv key list <namespace-id>

# Get a value
telnyx-edge storage kv key get <namespace-id> <key>

# Put a value
telnyx-edge storage kv key put <namespace-id> <key> "value"

# Put a value with TTL (expires in 3600 seconds)
telnyx-edge storage kv key put <namespace-id> <key> "value" --ttl 3600

# Put a value with metadata
telnyx-edge storage kv key put <namespace-id> <key> "value" --metadata '{"type":"session"}'

# Delete a key
telnyx-edge storage kv key delete <namespace-id> <key>
```
