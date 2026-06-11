---
title: Telnyx Edge Compute
summary: Telnyx Edge Compute is a serverless platform for deploying code across Telnyx's
  carrier-grade infrastructure, offering low latency, global distribution, and no
  infrastructure to manage. Functions run in real Linux containers with native language
  runtimes (Python, Go, Node.js, Java/Quarkus, TypeScript) and integrate directly
  with Telnyx Voice, Messaging, AI, and Storage services.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/network/index
- url: https://developers.telnyx.com/docs/edge-compute/observability/index
- url: https://developers.telnyx.com/docs/edge-compute/overview/index
- url: https://developers.telnyx.com/docs/edge-compute/platform-overview/index
- url: https://developers.telnyx.com/docs/edge-compute/products
- url: https://developers.telnyx.com/docs/edge-compute/quickstart/index
- url: https://developers.telnyx.com/docs/edge-compute/reference/architecture
- url: https://developers.telnyx.com/docs/edge-compute/reference/cli
- url: https://developers.telnyx.com/docs/edge-compute/reference/limits
- url: https://developers.telnyx.com/docs/edge-compute/runtime/bindings
- url: https://developers.telnyx.com/docs/edge-compute/runtime/execution-model
- url: https://developers.telnyx.com/docs/edge-compute/runtime/index
- url: https://developers.telnyx.com/docs/edge-compute/sqldb/index
- url: https://developers.telnyx.com/docs/edge-compute/testing/index
updated_at: 2026-06-11T10:27:59Z
---

# Telnyx Edge Compute

*Part 1 of 3 — see also: [Part 2](telnyx-edge-compute--part-2.md), [Part 3](telnyx-edge-compute--part-3.md)*

Telnyx Edge Compute is a serverless platform for deploying code across Telnyx's carrier-grade infrastructure, offering low latency, global distribution, and no infrastructure to manage. Functions run in real Linux containers with native language runtimes (Python, Go, Node.js, Java/Quarkus, TypeScript) and integrate directly with Telnyx Voice, Messaging, AI, and Storage services.

## Overview and Key Features

Edge Compute lets you deploy globally with functions running on edge nodes closest to your users, build in any supported language, integrate directly with Telnyx services, scale automatically with no provisioning or cold-start tuning, and pay only for what you use.

| Metric | Free Allowance | Rate |
|---|---|---|
| Requests | 3.6 M / month | $0.21 / million |
| CPU Time | 36 M ms / month | $0.014 / million ms |

The platform supports several use cases including API backends (REST APIs, webhooks, microservices), real-time processing (voice, messaging, AI events), data transformation (validate and route data at the edge), and scheduled jobs (background tasks with cron triggers — coming soon).

## Purpose-Built Infrastructure

Your code runs on the same infrastructure that powers Telnyx voice, messaging, and AI services — bare metal up.

- **Low latency** — Real-time voice demands single-digit millisecond latency. Telnyx pushes infrastructure into carrier facilities as close to end users as possible, not generic cloud availability zones, but sites inside the networks your traffic already traverses.
- **High redundancy** — Every region is backed by multiple independent sites hosted across different providers, with public cloud spillover for burst capacity. If a site goes down, traffic shifts automatically. No single facility, no single provider, no single point of failure.
- **Full control** — Telnyx owns the bare metal and controls the networking. No abstraction layers, no shared tenancy that can't be isolated, no vendor bottlenecks that can't be routed around.

## Quick Start

### Prerequisites

- A Telnyx account with API access ([sign up](https://telnyx.com/sign-up))
- Command line familiarity (Terminal on macOS/Linux or Command Prompt on Windows)
- Approximately 5 minutes

### Install the CLI

Download the latest release from the [edge-compute repo releases page](https://github.com/team-telnyx/edge-compute/releases):

```bash
# Download and extract
tar -xzf telnyx-edge-*.tar.gz

# Install to system PATH
sudo mv telnyx-edge /usr/local/bin/

# Verify installation
telnyx-edge --help
```

On macOS you can also use Homebrew:

```bash
brew tap telnyx/tap
brew install telnyx-edge
```

### Authenticate

**OAuth (recommended):**

```bash
telnyx-edge auth login
```

**API key:**

```bash
telnyx-edge auth api-key set YOUR_API_KEY
```

Verify authentication:

```bash
telnyx-edge auth status
```

### Create a Function

```bash
telnyx-edge new-func --language=go --name=hello-world
```

Supported languages: `go`, `js`, `ts`, `python`, `quarkus`. This creates a directory with a `func.toml` configuration file, dependency file, and starter handler code.

### Deploy the Function

```bash
cd hello-world
telnyx-edge ship
```

The CLI validates the function structure, checks authentication, packages files, uploads to Telnyx Edge infrastructure, and deploys across edge locations. You'll receive a function ID and status confirmation.

### Test the Function

Functions are accessible at URLs following the pattern `https://{funcName}-{orgId}.telnyxcompute.com`:

```bash
curl https://hello-world-abc123.telnyxcompute.com \
  -H "Content-Type: application/json" \
  -d '{"test": "data"}'
```

## Function Anatomy

Every Edge Compute function consists of three components:

1. **Function code** — The main application code that handles HTTP requests and responses.
2. **Runtime dependencies** — Language-specific dependency files (`go.mod`, `package.json`, `pyproject.toml`, `pom.xml`).
3. **Function configuration** — The `func.toml` file that defines deployment and runtime settings:

```toml
[edge_compute]
func_id = "func-abc123def456"
func_name = "hello-world"

[env_vars]
MY_KEY = "VAL"
```

### Handler Patterns by Language

| Language | Pattern | Entry Point |
|---|---|---|
| Go | `package function` with `Handle(w http.ResponseWriter, r *http.Request)` | `handler.go` |
| JavaScript | Raw `http.createServer` on port 8080 | `index.js` |
| TypeScript | Raw `http.createServer` on port 8080 | `index.ts` |
| Python | ASGI factory: `new()` returns a `Function` with `async handle(self, scope, receive, send)` | `function/__init__.py` |
| Java (Quarkus) | Quarkus Funqy with `@Funq` annotation and Input/Output beans | `src/main/java/` |

JavaScript and TypeScript functions must handle `/health/liveness` and `/health/readiness` endpoints for Knative probes.

## Architecture

Edge Compute runs your code in real Linux containers on Telnyx's global edge network — not V8 isolates. You get a full POSIX environment with native language runtimes.

### Containers vs Isolates

| Feature | V8 Isolates | Containers (Telnyx) |
|---|---|---|
| Languages | JavaScript/WASM only | Python, Go, Node.js, Java |
| Runtime | Reimplemented web APIs | Native runtimes, full stdlib |
| File system | None | Full POSIX filesystem |
| Cold start | ~5 ms | ~100–500 ms |
| Dependencies | Limited, bundled | Any native packages |
| Process model | Single-threaded | Multi-process capable |

Choose containers when you need native packages (ML libraries, image processing), are porting existing server code, require language-specific features not available in V8, or need filesystem access.

### Request Lifecycle

1. **Routing** — The request hits the nearest edge location. TLS is terminated and the request is routed to your function based on the URL pattern.
2. **Container selection** — A warm container handles the request immediately (~1–5 ms routing overhead), or a cold start initializes a new container (~100–500 ms).
3. **Execution** — Your function code runs with full network access, injected environment variables and secrets, and bindings for Telnyx services.
4. **Response** — The response is returned to the caller. The container stays warm for subsequent requests.

### Internal Components

| Component | Purpose |
|---|---|
| ECG (Edge Compute Gateway) | API gateway, function management, routing |
| KNative | Serverless runtime, auto-scaling, revision management |
| Kourier | Ingress controller, TLS termination |
| Meter Reader | Usage metering for billing |

Functions are deployed as KNative services on Kubernetes clusters at each edge location.

### Edge Locations

| Region | Location | Status |
|---|---|---|
| North America | Atlanta | ✅ Live |
| North America | New York | ✅ Live |
| North America | Los Angeles | ✅ Live |
| Europe | Frankfurt | ✅ Live |
| Asia Pacific | Sydney | ✅ Live |

Requests are automatically routed to the nearest available location for lowest latency.
