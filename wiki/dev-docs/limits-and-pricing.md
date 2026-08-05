---
title: Limits and Pricing
summary: Telnyx Edge Compute enforces behavioral contracts across execution, function
  packaging, networking, rate, account, and KV storage dimensions, and bills function
  usage on two meters — requests and CPU time — with a monthly free tier on each.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/platform/limits
- url: https://developers.telnyx.com/docs/edge-compute/platform/pricing
updated_at: 2026-08-05T13:41:09Z
---

# Limits and Pricing

Telnyx Edge Compute enforces behavioral contracts across execution, function packaging, networking, rate, account, and KV storage dimensions, and bills function usage on two meters — requests and CPU time — with a monthly free tier on each.

## Execution Limits

| Limit | Default | Maximum |
| --- | --- | --- |
| Request timeout | 30 seconds | 60 seconds |
| Memory per container | 256 MB | 512 MB |
| Request body size | 10 MB | 10 MB |
| Response body size | 10 MB | 10 MB |

**Request timeout.** A function must respond within the timeout or the request is terminated with a `504 Gateway Timeout`. The timeout is not set in `func.toml` — there is no `timeout_seconds` field. Budget your own upstream calls below the platform limit (for example, a 25-second timeout on outbound requests) so you can return a real error instead of a `504`.

**Memory.** Each container has a fixed allocation. Exceed it and the container is terminated; the next request starts a fresh one (a cold start). Stream large payloads instead of buffering them, and don't let in-memory caches grow unbounded — memory is per-container and disappears on restart anyway. For durable state, see [Execution Model](execution-model.md).

## Function Limits

| Limit | Value |
| --- | --- |
| Function code size | 50 MB (compressed) |
| Environment variables per function | 64 |
| Environment variable name size | 256 bytes |
| Environment variable value size | 5 KB |
| Secrets per organization | 100 |
| Secret value size | 10 KB |

The code size limit includes dependencies after compression. If you hit it: remove unused dependencies, exclude development dependencies from the shipped directory, or split into multiple functions.

## Network Limits

| Limit | Value |
| --- | --- |
| Outbound connections per request | 100 |
| Outbound request timeout | Set by your code, bounded by the request timeout |
| DNS resolution timeout | 5 seconds |

The outbound connection count covers HTTP/HTTPS requests, database connections, and TCP sockets. Since a container serves many requests over its lifetime, open clients and connection pools once at module scope and reuse them across requests rather than reconnecting per invocation.

## Rate Limits

| Limit | Value |
| --- | --- |
| Deployments per hour | 60 |
| API requests per minute | 1,000 |
| Concurrent function invocations | No hard limit (auto-scales) |

Function creation is also rate limited: `telnyx-edge new-func` registers the function server-side at scaffold time, and rapid successive calls return `429`. Wait and retry.

There is no hard cap on concurrent invocations — the platform scales containers with traffic. Each new container pays a cold start, so sharply spiky traffic sees higher tail latency.

## Account Limits

| Limit | Value |
| --- | --- |
| Functions per organization | 100 |

Total requests and CPU time are usage-billed with a monthly free tier — see the pricing section below.

Need higher limits? Contact [support@telnyx.com](mailto:support@telnyx.com).

## KV Storage Limits

| Limit | Value |
| --- | --- |
| Key length | 256 characters — over returns `400` |
| Key characters | `a-z` `A-Z` `0-9` `-` `_` `/` `=` `.` (no colons) |
| Value size | 1 MiB (1,048,576 bytes) — over returns `413` |
| TTL | Whole seconds, minimum 1 |

[KV Best Practices](kv-best-practices.md) is the authoritative KV limits page. For values over 1 MiB, store the object in [Cloud Storage](https://developers.telnyx.com/docs/cloud-storage/quick-start) and keep a reference in KV.

## When a Limit Is Exceeded

| Error | Code | Meaning |
| --- | --- |
| Request Timeout | 504 | Function didn't respond in time |
| Memory Exceeded | 500 | Container terminated due to memory |
| Payload Too Large | 413 | Request/response body exceeded limit |
| Rate Limited | 429 | Too many requests or deployments |

## Pricing

Functions bill on two meters: **requests** (each HTTP request your function handles) and **CPU time** (metered in milliseconds). These are the only two meters — there is no charge for deploying, for the number of functions you keep, or for idle functions.

| Resource | Free tier | Paid |
| --- | --- | --- |
| Requests | 3.6M/month | $0.21/million |
| CPU time | 36M ms/month | $0.014/million ms |

Storage is billed separately from function execution:

- **KV** bills per operation and per GB-month stored — see [KV Pricing](kv-pricing.md).

## Related

- [Limits](limits.md) — execution, size, and rate limits (this page)
- [Execution Model](execution-model.md) — container lifecycle and cold starts
- [KV Best Practices](kv-best-practices.md) — full KV limits and guidance
- [KV Pricing](kv-pricing.md) — operation and storage rates for KV
