---
title: KV (Edge Key-Value Store)
summary: Telnyx KV is a globally distributed, binary-safe key-value store built for
  low-latency access from edge functions. It offers simple get/put/delete/list APIs,
  namespace isolation, TTL-based expiration, and JSON metadata—accessible via REST
  or the telnyx-edge CLI, with eventual consistency and free egress.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/kv
  content_hash: 5a1cd7eddf969208a313913c8a3a1a8b9b115510bdc90009498e2bd182c91f3a
- url: https://developers.telnyx.com/docs/edge-compute/kv/api-reference
  content_hash: 9e592a2bf61e4d9097ca597d57622db0fcb1d4ca7d81f123f073e614ff3d5faa
- url: https://developers.telnyx.com/docs/edge-compute/kv/cli
  content_hash: cef46af7e62fcf59bff692b0708a78fa50b344b7d9d65142cc094c29760737fa
- url: https://developers.telnyx.com/docs/edge-compute/kv/pricing
  content_hash: aceb7fbcdcd8fc828cb4e8d0fb48e1e8c2b30c7e799c3eb4ddc47ccba2ce4be5
- url: https://developers.telnyx.com/docs/edge-compute/kv/quick-start/index
  content_hash: 6ac32f6799480ec2a8b2f156f813bd0551b12ec529fbc22c48cdf8bdf4e08204
- url: https://developers.telnyx.com/docs/edge-compute/kv/ttl-and-metadata
  content_hash: 5bcc7143f0bb8c933d6f9ac581c9f46ff0a614b988fc4e90b9bc33183c903762
- url: https://developers.telnyx.com/docs/edge-compute/kv/use-cases
  content_hash: 8ac2275f85cf764b9da32880e0369003695489e081a7b4a30494763c2c8ef79c
- url: https://developers.telnyx.com/docs/edge-compute/sqldb/index
  content_hash: 9248ecb5ea8d3e826d968414e82980e35d8712c0c6092d9c01845df1b0918c2a
updated_at: 2026-05-20T08:26:04Z
---

# KV (Edge Key-Value Store)

Telnyx KV is a globally distributed, binary-safe key-value store built for low-latency access from edge functions. It offers simple get/put/delete/list APIs, namespace isolation, TTL-based expiration, and JSON metadata—accessible via REST or the telnyx-edge CLI, with eventual consistency and free egress.

## Overview
- Low-latency reads from edge locations worldwide
- Simple operations: get, put, delete, list
- Namespace isolation for per-app separation
- Binary-safe values (must be base64-encoded)
- Global distribution (no region selection)
- TTL-based automatic key expiration
- Optional JSON metadata on keys (for context and future filtering)

## Consistency model
- Eventual consistency across the globe
- Writes are immediately visible in the region where they occur
- Read-after-write consistency within the same region
- For strong consistency or relational queries, consider [SQL DB](sql-db.md)

## Namespaces and provisioning
- Create/list/get/delete namespaces via the Storage API
- Namespace creation is asynchronous; poll until status is provision_ok
- Possible statuses: pending, provision_ok, provision_failed, deleting, delete_failed, deleted (404 once removed)

## Connecting from edge functions
- Bind a KV namespace in func.toml and use the injected env var in your code
- Example func.toml:
  - [edge_compute] func_name = "my-function"
  - [storage.kv.MY_CACHE] id = "<namespace-id>"
- Environment variables per binding:
  - KV_MY_CACHE_ID — the namespace ID
- See [Bindings](bindings.md) for how bindings map into your runtime

## REST API endpoints
- Base URL: https://api.telnyx.com/v2/storage/kvs
- Namespaces
  - POST /v2/storage/kvs — create namespace
  - GET /v2/storage/kvs — list namespaces
  - GET /v2/storage/kvs/{id} — get namespace details
  - DELETE /v2/storage/kvs/{id} — delete namespace
- Keys
  - PUT /v2/storage/kvs/{id}/keys/{key} — write a value
  - GET /v2/storage/kvs/{id}/keys/{key} — read a value
  - DELETE /v2/storage/kvs/{id}/keys/{key} — delete a key
  - GET /v2/storage/kvs/{id}/keys — list keys
- Authenticate with Authorization: Bearer <TELNYX_API_KEY>

## Key operations and options
- Writes require a JSON body with base64-encoded value
  - value (string, required) — base64-encoded data
  - expiration_ttl (integer, seconds) — min 60
  - expiration (integer, Unix timestamp)
  - metadata (object, JSON up to 1KB)
- Reads return base64-encoded value; expiration and metadata are included only if set
- Deletes remove the key; expired keys behave as 404 on read

## Listing keys and pagination
- GET /v2/storage/kvs/{id}/keys supports:
  - prefix — filter keys by prefix
  - page[number] — default 1
  - page[size] — default 20, max 250
- curl tip: use -g to disable globbing when passing page[size]

## CLI commands
- Namespaces
  - telnyx-edge storage kv list
  - telnyx-edge storage kv create --name <name>
  - telnyx-edge storage kv delete <namespace-id>
- Keys
  - telnyx-edge storage kv key list <namespace-id>
  - telnyx-edge storage kv key get <namespace-id> <key>
  - telnyx-edge storage kv key put <namespace-id> <key> "value"
  - With TTL: ... key put <namespace-id> <key> "value" --ttl 3600
  - With metadata: ... key put <namespace-id> <key> "value" --metadata '{"type":"session"}'
  - Delete: ... key delete <namespace-id> <key>

## Quick start workflow
1) Create a namespace (CLI or API) and wait for provision_ok
- telnyx-edge storage kv create --name my-cache
2) Bind it to your function (func.toml) and read KV_MY_CACHE_ID at runtime
3) Access KV via HTTP from your function
- PUT: base64-encode your value in the request body
- GET: decode base64 from the response
- Handle 404 for missing or expired keys
- Note: Native SDK support is coming soon; use HTTP endpoints for now

## TTL and metadata
- TTL options (min 60 seconds):
  - expiration_ttl — seconds from now
  - expiration — Unix timestamp
- Expired keys are auto-deleted and read as 404
- Metadata: attach a JSON object (≤1KB) stored with the key and returned on read
- Future capability: filtering list results by metadata

## Best practices
- Key naming with prefixes for organization:
  - user:123, session:abc, cache:api:/users, flag:new-feature
- Value serialization: JSON-serialize complex values before base64-encoding
- Error handling: treat 404 as “missing key” (including expired keys)
- URL safety: encode key as a path segment when calling the API

## Common use cases
- Session storage with TTL (e.g., 24h) to keep user state at the edge
- API response caching with short TTLs (e.g., 5 minutes) for freshness
- Feature flags (e.g., feature:new-ui) read on each request for instant rollout

## Pricing
- Free tier per month:
  - Reads: 10M
  - Writes: 1M
  - Deletes: 1M
  - Lists: 1M
  - Storage: 1 GB
- Paid rates:
  - Reads: $0.35 / million
  - Writes: $3.50 / million
  - Deletes: $3.50 / million
  - Lists: $3.50 / million
  - Storage: $0.35 / GB-month
- Egress is free (no charges for data transferred out of KV)

## Notes and limitations
- Eventual consistency across regions; read-after-write only guaranteed in the same region
- Minimum TTL 60 seconds; lower values are rejected
- Metadata must be valid JSON and ≤1KB
- Values are always base64-encoded in the API
- SDK support is planned; use REST for now

## Related resources
- [Bindings](bindings.md) — connect your function to KV and other services
- [SQL DB](sql-db.md) — serverless SQL (coming soon) for strongly consistent and relational workloads
