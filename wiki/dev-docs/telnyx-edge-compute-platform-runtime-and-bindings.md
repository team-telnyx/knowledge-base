---
title: 'Telnyx Edge Compute: Platform, Runtime, and Bindings'
summary: A serverless platform that runs your code in real Linux containers on Telnyx’s
  global edge. It delivers low latency, automatic scaling, and secure, built‑in access
  to Telnyx services via bindings—with simple, usage‑based pricing and a generous
  free tier.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/overview/index
  content_hash: 40b1535863157ed6898ce2ff010b078fa0d846c6888629341f2c79ac5a60586e
- url: https://developers.telnyx.com/docs/edge-compute/platform-overview/index
  content_hash: 84a7e22ec65304624462300a6ca97fd543b43e4c9f1a9eb28fddfb953d95dffa
- url: https://developers.telnyx.com/docs/edge-compute/products
  content_hash: cd26142c6ba038b6171f2f4fcb3bbbc7b14e6ec66b0ddc7163dd50c8773b0f06
- url: https://developers.telnyx.com/docs/edge-compute/reference/architecture
  content_hash: 59b1541e09f98b4a667d964ab8e10365f4e3055a1b603c281e67c02998107b29
- url: https://developers.telnyx.com/docs/edge-compute/runtime/index
  content_hash: ee86d887fc2630e2e0cc8f51c25f043cde1adec7b0ade592e48b73acd5fd7542
- url: https://developers.telnyx.com/docs/edge-compute/runtime/execution-model
  content_hash: f0f05f4bc0d9f946d6fd16c122c8a68b100d835ef82ed5697e6ef98b280a27cd
- url: https://developers.telnyx.com/docs/edge-compute/runtime/bindings
  content_hash: ac80d672861d0fa1cbbb9bc4ed6ff046550559b8ff0d436b27afb7369e5a3e8f
updated_at: 2026-05-19T19:36:53Z
---

# Telnyx Edge Compute: Platform, Runtime, and Bindings

A serverless platform that runs your code in real Linux containers on Telnyx’s global edge. It delivers low latency, automatic scaling, and secure, built‑in access to Telnyx services via bindings—with simple, usage‑based pricing and a generous free tier.

## What Is Telnyx Edge Compute
A globally distributed, serverless compute platform on Telnyx’s carrier‑grade network. You deploy functions; the platform handles scaling, routing to the nearest edge, and operations—no servers to manage.

- Deploy globally to edge locations closest to users
- Build in multiple languages (JavaScript/TypeScript, Python, Go, Java/Quarkus)
- Integrate natively with Telnyx Voice, Messaging, Numbers, Fax, Verify, and AI
- Autoscale (including scale-to-zero) without provisioning
- Usage-based pricing with a free tier

## Key Features and Use Cases
- API backends, webhooks, and microservices with automatic scaling
- Real-time event handling for voice, messaging, and AI with minimal latency
- Data transformation/validation/routing at the edge before storage
- Scheduled jobs via cron triggers (planned/rolling out)

## Infrastructure and Regions
Your code runs on the same infrastructure that powers Telnyx voice, messaging, and AI—purpose-built for real-time latency and resiliency.

- Low latency: Edge sites placed inside carrier facilities near end users
- High redundancy: Multiple independent sites per region, multi-provider, public cloud spillover for bursts
- Full control: Telnyx owns the metal and networking stack, eliminating hidden abstraction bottlenecks
- Live edge locations include: Atlanta, New York, Los Angeles, Frankfurt, Sydney (requests auto-route to the nearest available site)

See [Edge Compute architecture](edge-compute-architecture.md) for deeper internals.

## Containers vs Isolates
Edge Compute uses real Linux containers (not V8 isolates):

- Full POSIX environment with native runtimes and standard libraries
- Broad language support: Python, Go, Node.js, Java (Quarkus)
- Filesystem access and native dependencies supported
- Tradeoff: Cold starts are typically higher (~100–500 ms) than isolates, but enable more capability

Choose containers when you need native packages (ML, image processing), filesystem access, or to port existing server/serverless code without reimplementing web APIs.

## Request Lifecycle and Scaling
1) Routing: The nearest edge location terminates TLS and routes by URL to your function.
2) Container selection: A warm container handles the request immediately, or a new one starts (cold start).
3) Execution: Code runs with outbound networking, env vars/secrets, and service bindings.
4) Response: Returned to caller; the container remains warm for subsequent traffic.

Scaling behavior:
- One request per container at a time; platform scales horizontally by adding containers
- Spikes trigger new containers (expect cold starts); sustained load keeps containers warm
- Idle containers recycle over time; services can scale to zero

## Runtime Environment and Languages
- Runtimes: Python 3.11+, Node.js 18+, Go 1.25+, Java 17+ (Quarkus)
- Capabilities: POSIX APIs (file I/O, env, process), outbound HTTP/TCP/UDP, DNS
- Build with your preferred HTTP framework or standard libraries

See [Edge Compute runtime](edge-compute-runtime.md) for language details and examples.

## Configuration and Environment Variables
- Configure functions via environment variables (defined in func.toml) and secrets
- Bindings inject credentials and base URLs at runtime (e.g., TELNYX_API_KEY, TELNYX_BASE_URL)

Refer to [Edge Compute configuration](edge-compute-configuration.md) and [Edge Compute secrets management](edge-compute-secrets-management.md).

## Triggers and Timeouts
- HTTP requests: Public endpoints hosted on Telnyx Edge
- Webhooks: Invoke functions from Telnyx services (Messaging, Voice, etc.)
- Cron: Scheduled execution is planned/rolling out
- Timeouts: Default 30 s; Extended 60 s (configurable). Handle timeouts gracefully with client-side timeouts and partial results when appropriate.

See [Edge Compute execution model](edge-compute-execution-model.md) for lifecycle and performance guidance.

## Security and Isolation
- Network, filesystem, and process isolation per function
- Credentials are injected securely and do not appear in logs
- Secrets are encrypted at rest; use secrets for third-party keys and non‑Telnyx credentials

## Bindings: Secure Telnyx API Access
Bindings provide auto-authenticated access to Telnyx APIs without hardcoding API keys.

How it works:
- Your function receives TELNYX_API_KEY (JWT) and TELNYX_BASE_URL (binding proxy)
- Call Telnyx APIs via the proxy: ${TELNYX_BASE_URL}/v2/<api-path>
- Always include the /v2/ segment after the proxy URL
- Do not call https://api.telnyx.com directly with the binding JWT (will 401)

Available today: Voice, Messaging, Phone Numbers, Fax, Verify, Cloud Storage (S3-compatible endpoint). KV and SQL DB bindings are coming soon.

Manage with the CLI:
- Create/validate/update/delete an organization binding via telnyx-edge bindings commands

See [Bindings](bindings.md) for SDK usage, troubleshooting, and rotation practices.

## Cloud Storage Considerations
- The binding JWT does not authenticate S3-compatible Cloud Storage
- Cloud Storage endpoints require AWS SigV4-style auth; store a regular Telnyx API key as a secret and use it as the S3 access key
- The binding proxy covers api.telnyx.com routes (Voice, Messaging, etc.) only; S3 calls go directly to the storage endpoint

## Pricing
Edge Compute is billed on requests and CPU time; a free tier is included.

| Metric | Free Allowance | Rate |
| --- | --- | --- |
| Requests | 3.6M / month | $0.21 / million |
| CPU Time | 36M ms / month | $0.014 / million ms |

## Best Practices
- Initialize expensive resources globally so warm requests are fast
- Use lazy initialization for heavy assets (e.g., ML models)
- Minimize dependencies to improve cold start time
- Pool outbound HTTP and database connections
- Don’t rely on in-memory state; use KV or external storage for persistence
- Set conservative timeouts and handle platform timeouts gracefully
- Implement graceful shutdown handlers for clean recycling

## CLI and Next Steps
- Set up and validate bindings with telnyx-edge bindings create/validate/update
- Redeploy to pick up new credentials when rotating bindings

Explore:
- [Edge Compute architecture](edge-compute-architecture.md) for platform internals and components
- [Edge Compute execution model](edge-compute-execution-model.md) for lifecycle, concurrency, and cold starts
- [Edge Compute limits and quotas](edge-compute-limits-and-quotas.md) for timeouts and resource constraints
- [Edge Compute observability](edge-compute-observability.md) for logs, metrics, and tracing
- [Edge Compute CLI Reference](edge-compute-cli-reference.md) for full command details
