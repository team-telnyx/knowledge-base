---
title: Limits
summary: Resource limits and quotas for Edge Compute functions.
sources:
  - url: https://developers.telnyx.com/docs/edge-compute/reference/limits
    content_hash: 23fd63f4570db0e06f36b15450073a7f1a349c75525ee7aa91c2d7daa14ce63a
updated_at: 2026-04-10T00:00:00Z
---

# Limits

Resource limits and quotas for Edge Compute functions.

Edge Compute enforces resource limits to ensure fair usage and platform stability.

## Execution Limits

| Limit                | Default    | Maximum    |
| -------------------- | ---------- | ---------- |
| Request timeout      | 30 seconds | 60 seconds |
| CPU time per request | 30 seconds | 60 seconds |
| Memory per container | 256 MB     | 512 MB     |
| Request body size    | 10 MB      | 10 MB      |
| Response body size   | 10 MB      | 10 MB      |

### Request Timeout

Functions must return a response within the timeout period. If exceeded, the request is terminated and returns a 504 Gateway Timeout.

```python theme={null}


## Related Pages

- [Limits](../runbooks/limits.md)
- [Limits](../runbooks/limits-3.md)
