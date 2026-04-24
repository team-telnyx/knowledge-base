---
title: Edge Compute
summary: Serverless functions on Telnyx's global edge network.
sources:
  - url: https://developers.telnyx.com/docs/edge-compute/overview/index
    content_hash: ae350dffeed669497e5f3aa615f250b9287b99d1366248732349ca2ba08f23f3
updated_at: 2026-04-10T00:00:00Z
---

# Edge Compute

Serverless functions on Telnyx's global edge network

A serverless platform for deploying code across Telnyx's carrier-grade infrastructure — low latency, global distribution, no infrastructure to manage.

With Telnyx Edge Compute, you can:

* **Deploy globally** — Functions run on edge nodes closest to your users
* **Build in any language** — JavaScript, TypeScript, Python, Go, and Java (Quarkus)
* **Integrate with Telnyx** — Direct access to Voice, Messaging, and AI APIs
* **Scale automatically** — No provisioning, no cold start tuning
* **Pay for what you use** — Free tier included, simple usage-based pricing

  - [Quick Start](../tutorial/edge-compute-quick-start.md) — Deploy your first function in 5 minutes

  - [Examples](../runbooks/examples.md) — Copy-paste code snippets for common patterns

***

## Build with Edge Compute

  - [API Backends](#) — Build REST APIs, webhooks, and microservices with automatic scaling

  - [Real-Time Processing](#) — Process voice, messaging, and AI events with minimal latency

  - [Data Transformation](#) — Transform, validate, and route data at the edge before storage

  - [Scheduled Jobs](#) — Run background tasks on a schedule with cron triggers

***

## Integrate with Edge Compute

Connect to storage and services via bindings — configured in `func.toml`, available at runtime:

**Storage**

  - [KV](https://developers.telnyx.com/docs/edge-compute/kv) — Low-latency key-value storage for caching and session data

  - [SQL DB](../runbooks/sql-db.md) — Serverless SQL database with SQLite compatibility

  - [Object Storage](../runbooks/quick-start.md) — S3-compatible storage for files and media

**Telnyx Services**

  - [Voice API](#) — Handle calls, transcribe audio, build IVRs

  - [Messaging API](#) — Send and receive SMS/MMS with custom logic

  - [AI APIs](#) — Transcription, inference, and embeddings at the edge

***

## Pricing

Edge Compute is billed based on requests and CPU time. Free tier included.

| Metric   | Free Allowance | Rate                 |
| -------- | -------------- | -------------------- |
| Requests | 3.6M / month   | \$0.21 / million     |
| CPU Time | 36M ms / month | \$0.014 / million ms |

***

## Resources

  - [CLI Reference](https://developers.telnyx.com/docs/edge-compute/reference/cli) — Complete CLI command reference

  - [Architecture](../runbooks/architecture.md) — How Edge Compute works under the hood

  - [Limits](../runbooks/limits-2.md) — Request limits, timeouts, and quotas

  - [Discord Community](https://discord.gg/telnyx) — Get help from the community


## Related Pages

- [Edge Compute Quick Start](../tutorial/edge-compute-quick-start.md)
