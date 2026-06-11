---
title: Edge Compute Development Guide
summary: A comprehensive guide to building, testing, and deploying serverless functions
  on Telnyx Edge Compute — covering local development workflows, step-by-step tutorials
  for common applications, reusable code snippets across multiple languages, production-grade
  reference architectures, and CI/CD deployment pipelines.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/demos/build-a-rest-api
- url: https://developers.telnyx.com/docs/edge-compute/demos/image-resizer
- url: https://developers.telnyx.com/docs/edge-compute/demos/index
- url: https://developers.telnyx.com/docs/edge-compute/demos/sms-webhook-handler
- url: https://developers.telnyx.com/docs/edge-compute/demos/voice-call-router
- url: https://developers.telnyx.com/docs/edge-compute/deploy
- url: https://developers.telnyx.com/docs/edge-compute/development
- url: https://developers.telnyx.com/docs/edge-compute/examples/index
- url: https://developers.telnyx.com/docs/edge-compute/frameworks-support
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/global-api-gateway
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/index
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/iot-data-ingestion
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/real-time-media-pipeline
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/telecom-event-processor
updated_at: 2026-06-11T10:26:49Z
---

# Edge Compute Development Guide

*Part 2 of 3 — see also: [Part 1](edge-compute-development-guide--part-1.md), [Part 3](edge-compute-development-guide--part-3.md)*

A comprehensive guide to building, testing, and deploying serverless functions on Telnyx Edge Compute — covering local development workflows, step-by-step tutorials for common applications, reusable code snippets across multiple languages, production-grade reference architectures, and CI/CD deployment pipelines.

## Code Examples

Self-contained snippets for common edge function patterns, available in JavaScript, TypeScript, Go, Python, and Java.

### Return JSON

Return a JSON response with a `Content-Type: application/json` header. All examples also include health check endpoints at `/health/liveness` and `/health/readiness`.

### Return HTML and Binary

Return HTML pages with `Content-Type: text/html`, or binary data (e.g., images fetched from S3) with the appropriate MIME type.

### Parse Query Parameters

Extract query string values from the request URL. For example, read a `name` parameter and default to "World" if absent.

### Handle HTTP Methods

Route logic based on the HTTP method (GET, POST, etc.) and return a 405 status for unsupported methods.

### Read Request Body

Parse a JSON request body, validate required fields, and handle `JSONDecodeError` / malformed input with a 400 response.

### Use Environment Variables

Read configuration from environment variables (e.g., `process.env.GREETING` in JavaScript, `os.Getenv("GREETING")` in Go) with sensible defaults.

### Access Secrets

Secrets are injected as environment variables but stored encrypted. Use them for API keys and credentials — check for their presence and return a 500 if unconfigured.

### KV Read/Write

**Coming Soon** — KV storage access via the Telnyx API (`/v2/storage/kvs/{kvId}/keys/{key}`). Use `GET` to read and `PUT` to write values with optional TTL. Store the KV store ID and API key as environment variables.

### Cron Trigger

**Coming Soon** — Native cron triggers. Detect cron invocations via the `X-Telnyx-Cron: true` and `X-Telnyx-Cron-Schedule` headers. Until native support lands, use an external scheduler (GitHub Actions, AWS EventBridge) to call the function's HTTP endpoint.

### WebSocket Handling

**Coming Soon** — WebSocket support is planned. The expected pattern uses connection upgrade, message echo, and JSON framing.

### Service-to-Service Calls

Call other edge functions or external services with proper error handling and timeouts (5-second default). Use `AbortController` in JavaScript, `http.Client` with `Timeout` in Go, and `httpx.AsyncClient` with `timeout` in Python. Return 504 on timeout.

### Connection Reuse

Initialize HTTP clients once at the module/package level to reuse connections across requests. This avoids the overhead of creating a new client per invocation.

## Reference Architectures

Production-grade architectures that combine Edge Compute with other Telnyx products to solve real-world problems.

### Global API Gateway

A globally distributed API gateway providing authentication, rate limiting, and caching for backend services. The pipeline is:

1. **Auth Middleware** — JWT validation using a stored secret
2. **Rate Limiter** — Per-user distributed counters in KV (configurable, default 100 req/min)
3. **Cache Layer** — Response caching in KV with TTL
4. **Router** — Path-based routing to backend services

Use cases: microservices gateway, third-party API proxy, multi-region deployment.

### Telecom Event Processor

Process voice calls, SMS messages, and fax events in real-time with low latency. A unified handler routes by `event_type`:

- **Voice events** (`call.initiated`, `call.answered`, `call.hangup`) — Log to analytics, look up caller in CRM, generate TeXML for VIP routing
- **SMS events** (`message.received`, `message.sent`) — TCPA-compliant keyword handling (STOP, UNSUBSCRIBE, CANCEL, QUIT for opt-out; HELP, START for opt-in)
- **Fax events** (`fax.received`, `fax.sent`) — Log metadata and download/store received fax media

Downstream destinations include CRM systems, analytics platforms, and alerting services.

Use cases: contact center routing, SMS marketing with opt-in/out, two-factor authentication.

### Real-Time Media Pipeline

Transform and route media streams for video, audio, and real-time communication. The pipeline stages are ingest, transform (transcode, watermark, thumbnails), and route to multiple destinations (S3 archive, CDN, LiveKit SFU) in parallel.

The handler also accepts JSON control messages to start/stop streams.

Use cases: live streaming, video conferencing, surveillance camera feeds.

### IoT Data Ingestion

Collect sensor data from IoT devices globally with edge validation and enrichment. Each PoP validates incoming data, enriches it with edge metadata (PoP identifier, timestamp, device ID from headers), and forwards it to a central data lake.

For high-volume ingestion, use an external persistent queue (Kafka, Redis Streams) to buffer data reliably — in-memory buffers in serverless functions risk data loss on cold starts or process recycling.

Use cases: fleet management, smart buildings, industrial IoT.
