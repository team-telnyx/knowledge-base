---
title: Edge Compute observability
summary: Observability for Telnyx Edge Compute (logs, metrics, tracing) is in development.
  This page outlines what’s coming and how to monitor, debug, and operate your functions
  today using proven patterns, platform limits, and the telnyx-edge CLI.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/observability/index
- url: https://developers.telnyx.com/docs/edge-compute/reference/cli
- url: https://developers.telnyx.com/docs/edge-compute/reference/limits
- url: https://developers.telnyx.com/docs/edge-compute/best-practices
- url: https://developers.telnyx.com/docs/edge-compute/network/index
updated_at: 2026-05-20T08:18:09Z
---

# Edge Compute observability

Observability for Telnyx Edge Compute (logs, metrics, tracing) is in development. This page outlines what’s coming and how to monitor, debug, and operate your functions today using proven patterns, platform limits, and the telnyx-edge CLI.

## Status and scope
Observability features—centralized logs, performance metrics, and request tracing—are coming soon. Until then, you can instrument your functions to capture key signals (latency, error rates, timeouts, memory pressure) and use the CLI for deployment/runtime checks. See [Edge Compute limits and quotas](edge-compute-limits-and-quotas.md) and [Best Practices](best-practices.md) for platform constraints and optimization guidance.

## What to monitor now
Focus on a few high-signal indicators:
- Request volume and latency (p50/p95/p99)
- Error rate by type (4xx vs 5xx; platform vs application)
- Timeouts (your internal timeouts vs platform limits)
- Memory usage symptoms (process restarts, large payload handling)
- Outbound call behavior (failures/timeouts; connection pooling efficacy)
- Deployment events (version, timestamp) to correlate with regressions

## Implement structured logging
Emit concise, structured logs that are easy to grep and correlate.

Example (JavaScript):
```
function log(level, msg, fields = {}) {
  const entry = { ts: new Date().toISOString(), level, msg, ...fields };
  console.log(JSON.stringify(entry));
}

export async function handler(request) {
  const start = Date.now();
  try {
    // ... your code ...
    const ms = Date.now() - start;
    log('info', 'request_ok', { path: new URL(request.url).pathname, ms });
    return new Response('OK');
  } catch (err) {
    const ms = Date.now() - start;
    log('error', 'request_failed', { err: String(err), ms });
    return new Response('Internal error', { status: 500 });
  }
}
```

Use log levels consistently. See logging guidance in [Best Practices](best-practices.md).

## Correlate requests with IDs
Attach a request ID to every log and response header so you can follow a request end-to-end.
```
export async function handler(request) {
  const requestId = request.headers.get('X-Request-ID') || crypto.randomUUID();
  console.log(JSON.stringify({ level: 'info', msg: 'start', requestId }));
  // ...
  return new Response(JSON.stringify({ ok: true }), {
    headers: { 'Content-Type': 'application/json', 'X-Request-ID': requestId }
  });
}
```

## Guard external calls with timeouts and retries
Set your own timeouts shorter than platform limits and implement backoff for transient failures.

JavaScript (fetch with AbortController):
```
const controller = new AbortController();
const t = setTimeout(() => controller.abort(), 25000); // 25s
try {
  const res = await fetch('https://api.example.com/data', { signal: controller.signal });
  clearTimeout(t);
  if (!res.ok && res.status >= 500) {
    // optional: retry with backoff
  }
  return res;
} catch (e) {
  if (e.name === 'AbortError') return new Response('Upstream timeout', { status: 504 });
  throw e;
}
```

Python (httpx):
```
import httpx

client = httpx.Client(timeout=25.0)

def handler(request):
  try:
    r = client.get('https://api.example.com/data')
    r.raise_for_status()
    return { 'body': r.text }
  except httpx.TimeoutException:
    return { 'error': 'Upstream API timed out', 'status': 504 }
```

## Stay within critical limits
A few limits that commonly affect observability and reliability (see full list in [Edge Compute limits and quotas](edge-compute-limits-and-quotas.md)):
- Request timeout: default 30s (up to 60s). Set your internal timeouts a bit lower (e.g., 25s) and log timeout events.
- Memory per container: 256 MB (up to 512 MB). Stream large payloads; log payload sizes and branch to streaming paths.
- Request/response body size: 10 MB. Log content length and return 413 early if too large.
- Outbound connections per request: 100. Use connection pooling and reuse clients across invocations.

Memory-friendly pattern:
```
# Avoid loading entire files into memory; stream instead
for chunk in stream_file():
  yield process_chunk(chunk)
```

## Deployment and runtime checks with CLI
Use the telnyx-edge CLI to validate auth, list functions, and ship updates you’ve instrumented.
```
# Check authentication and connectivity
telnyx-edge auth status
telnyx-edge status

# List functions with status/URLs
telnyx-edge list

# Deploy current directory
telnyx-edge ship

# Roll out from a specific path
telnyx-edge ship --from-dir=./my-function
```
Manage secrets for log levels or endpoints:
```
telnyx-edge secrets add LOG_LEVEL "info"
```
See [CLI Reference](cli-reference.md) for full command coverage.

## Error codes and troubleshooting quick reference
When limits are exceeded, the platform returns specific errors (see details in [Edge Compute limits and quotas](edge-compute-limits-and-quotas.md)):
- 504 Request Timeout — function didn’t respond in time
- 500 Memory Exceeded — container terminated due to memory
- 413 Payload Too Large — request/response body exceeded limit
- 429 Rate Limited — too many requests or deployments

Example error payload:
```
{
  "error": {
    "code": "timeout_exceeded",
    "message": "Function execution exceeded 30 second timeout",
    "request_id": "req_abc123"
  }
}
```
Log the code, message, and request_id; echo request_id back to clients for support.

## Preparing for first‑party observability
To be ready for built-in logs/metrics/tracing as they roll out:
- Standardize log fields (ts, level, request_id, path, status, ms)
- Keep logs lean; avoid sensitive data and full request bodies
- Tag logs with deploy version/commit to correlate changes
- Capture p50/p95/p99 latency in your own counters for continuity

## Related resources
- [Best Practices](best-practices.md)
- [Edge Compute limits and quotas](edge-compute-limits-and-quotas.md)
- [CLI Reference](cli-reference.md)
- [Edge Network](edge-network.md)
