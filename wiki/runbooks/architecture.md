---
title: Architecture
summary: How Edge Compute works under the hood.
sources:
  - url: https://developers.telnyx.com/docs/edge-compute/reference/architecture
    content_hash: 71fd8ccc945051646a3b14c00cf76028a38c4fb5dd85f89c730d5509a290ded0
updated_at: 2026-04-10T00:00:00Z
---

# Architecture

How Edge Compute works under the hood.

Edge Compute runs your code in real Linux containers on Telnyx's global edge network. Unlike V8 isolate-based platforms, you get a full POSIX environment with native language runtimes.

## Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     Your Request                            │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Edge Location                            │
│              (nearest to your users)                        │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Ingress (TLS termination, routing)                  │  │
│  └──────────────────────────────────────────────────────┘  │
│                              │                              │
│                              ▼                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  KNative Serving                                      │  │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐      │  │
│  │  │ Container  │  │ Container  │  │ Container  │      │  │
│  │  │ (your fn)  │  │ (your fn)  │  │ (your fn)  │      │  │
│  │  └────────────┘  └────────────┘  └────────────┘      │  │
│  │        ▲               ▲               ▲              │  │
│  │        └───────────────┴───────────────┘              │  │
│  │               Auto-scaled based on load               │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## Containers vs Isolates

Edge Compute uses **real containers**, not V8 isolates. This gives you:

| Feature       | V8 Isolates (Cloudflare) | Containers (Telnyx)          |
| ------------- | ------------------------ | ---------------------------- |
| Languages     | JavaScript/WASM only     | Python, Go, Node.js, Java    |
| Runtime       | Reimplemented web APIs   | Native runtimes, full stdlib |
| File system   | None                     | Full POSIX filesystem        |
| Cold start    | \~5ms                    | \~100-500ms                  |
| Dependencies  | Limited, bundled         | Any native packages          |
| Process model | Single-threaded          | Multi-process capable        |

**When to choose containers:**

* Need native packages (ML libraries, image processing, etc.)
* Porting existing server code
* Require language-specific features not available in V8
* Need filesystem access

## Request Lifecycle

When a request arrives at your function:

### 1. Routing

The request hits the nearest edge location. TLS is terminated, and the request is routed to your function based on the URL:

```
https://my-function-abc123.telnyxcompute.com/api/data
        └──────────┬──────────┘
            Routes to your function
```

### 2. Container Selection

The platform selects a container to handle the request:

* **Warm container available** → Request handled immediately (\~1-5ms routing overhead)
* **No warm container** → Cold start: new container initialized (\~100-500ms)

### 3. Execution

Your function code runs with:

* Full network access (outbound HTTP, TCP, UDP)
* Environment variables and secrets injected
* [Bindings](bindings.md) for Telnyx services

### 4. Response

The response is returned to the caller. The container stays warm for subsequent requests.

## Cold Starts

A cold start occurs when a new container must be initialized:

```
Cold Start Timeline
├── Container image pull (cached at edge)      ~0ms (cached)
├── Runtime initialization (Python/Go/Node)   ~50-200ms
├── Global code execution (imports, setup)    ~50-300ms
└── First request handled                      varies
```

**Minimizing cold starts:**

1. **Keep containers warm** — Consistent traffic keeps containers alive
2. **Lazy initialization** — Defer expensive setup until needed
3. **Minimize dependencies** — Smaller images = faster starts
4. **Use connection pools** — Initialize once, reuse across requests

See [Execution Model](execution-model.md) for optimization patterns.

## Edge Network

Functions run on Telnyx's edge infrastructure across multiple locations:

| Region        | Location    | Status |
| ------------- | ----------- | ------ |
| North America | Atlanta     | ✅ Live |
| North America | New York    | ✅ Live |
| North America | Los Angeles | ✅ Live |
| Europe        | Frankfurt   | ✅ Live |
| Asia Pacific  | Sydney      | ✅ Live |

Requests are automatically routed to the nearest available location for lowest latency.

## Scaling

Edge Compute automatically scales based on traffic:

```
Traffic Pattern          Platform Response
─────────────────────    ─────────────────────
Low traffic         →    Fewer containers (may scale to zero)
Traffic spike       →    New containers start (cold starts)
Sustained load      →    Containers stay warm
Traffic drops       →    Containers gradually recycle
```

Each container handles **one request at a time**. The platform scales horizontally by adding containers as needed.

## Security

### Isolation

Each function runs in its own isolated container:

* **Network isolation** — Functions cannot communicate with each other directly
* **Filesystem isolation** — No shared filesystem between functions
* **Process isolation** — Separate process namespace

### Credentials

API credentials are never exposed in your code:

* [Bindings](bindings.md) inject credentials securely
* [Secrets](secrets.md) are encrypted at rest
* Credentials don't appear in logs

## Internal Architecture

For those curious about the internals:

| Component                  | Purpose                                               |
| -------------------------- | ----------------------------------------------------- |
| ECG (Edge Compute Gateway) | API gateway, function management, routing             |
| KNative                    | Serverless runtime, auto-scaling, revision management |
| Kourier                    | Ingress controller, TLS termination                   |
| Meter Reader               | Usage metering for billing                            |

Functions are deployed as KNative services on Kubernetes clusters at each edge location.

## Next Steps

* [Execution Model](execution-model.md) — Deep dive into function lifecycle
* [Limits](limits-2.md) — Resource constraints
* [Bindings](bindings.md) — Connect to Telnyx services


## Related Pages

- [Architecture](../runbooks/architecture-2.md)
