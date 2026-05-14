---
title: Telnyx Edge Compute — Developer Guide
summary: 'A concise, end-to-end guide to Telnyx Edge Compute: architecture, setup,
  configuration, runtime model, bindings, KV storage, best practices, CI/CD, limits,
  and what’s coming next.'
sources:
- url: https://developers.telnyx.com/docs/edge-compute/best-practices
- url: https://developers.telnyx.com/docs/edge-compute/configuration
- url: https://developers.telnyx.com/docs/edge-compute/configuration/cron-triggers
- url: https://developers.telnyx.com/docs/edge-compute/configuration/environment-variables
- url: https://developers.telnyx.com/docs/edge-compute/configuration/routing
- url: https://developers.telnyx.com/docs/edge-compute/configuration/secrets
- url: https://developers.telnyx.com/docs/edge-compute/configuration/versions
- url: https://developers.telnyx.com/docs/edge-compute/demos
- url: https://developers.telnyx.com/docs/edge-compute/demos/build-a-rest-api
- url: https://developers.telnyx.com/docs/edge-compute/demos/image-resizer
- url: https://developers.telnyx.com/docs/edge-compute/demos/sms-webhook-handler
- url: https://developers.telnyx.com/docs/edge-compute/demos/voice-call-router
- url: https://developers.telnyx.com/docs/edge-compute/deploy
- url: https://developers.telnyx.com/docs/edge-compute/development
- url: https://developers.telnyx.com/docs/edge-compute/examples
- url: https://developers.telnyx.com/docs/edge-compute/frameworks
- url: https://developers.telnyx.com/docs/edge-compute/frameworks-support
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/global-api-gateway
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/iot-data-ingestion
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/real-time-media-pipeline
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/telecom-event-processor
- url: https://developers.telnyx.com/docs/edge-compute/kv/api-reference
- url: https://developers.telnyx.com/docs/edge-compute/kv/cli
- url: https://developers.telnyx.com/docs/edge-compute/kv/pricing
- url: https://developers.telnyx.com/docs/edge-compute/kv/quick-start
- url: https://developers.telnyx.com/docs/edge-compute/kv/ttl-and-metadata
- url: https://developers.telnyx.com/docs/edge-compute/kv/use-cases
- url: https://developers.telnyx.com/docs/edge-compute/network
- url: https://developers.telnyx.com/docs/edge-compute/observability
- url: https://developers.telnyx.com/docs/edge-compute/overview
- url: https://developers.telnyx.com/docs/edge-compute/platform-overview
- url: https://developers.telnyx.com/docs/edge-compute/products
- url: https://developers.telnyx.com/docs/edge-compute/quickstart
- url: https://developers.telnyx.com/docs/edge-compute/reference/architecture
- url: https://developers.telnyx.com/docs/edge-compute/reference/cli
- url: https://developers.telnyx.com/docs/edge-compute/reference/limits
- url: https://developers.telnyx.com/docs/edge-compute/runtime
- url: https://developers.telnyx.com/docs/edge-compute/runtime/bindings
- url: https://developers.telnyx.com/docs/edge-compute/runtime/execution-model
- url: https://developers.telnyx.com/docs/edge-compute/sqldb
- url: https://developers.telnyx.com/docs/edge-compute/testing
updated_at: 2026-05-14T09:47:40Z
---

# Telnyx Edge Compute — Developer Guide

*Part 2 of 2 — see also: [Part 1](telnyx-edge-compute-developer-guide--part-1.md)*

A concise, end-to-end guide to Telnyx Edge Compute: architecture, setup, configuration, runtime model, bindings, KV storage, best practices, CI/CD, limits, and what’s coming next.

## Tutorials and examples
- [Build a REST API](build-a-rest-api.md): CRUD routing, JSON parsing, proper status codes.
- [SMS Webhook Handler](sms-webhook-handler.md): process Telnyx Messaging webhooks; send replies (use Bindings or Secrets for API auth).
- [Voice Call Router](voice-call-router.md): return TeXML with time/geography-based routing.
- [Image Resizer](image-resizer.md): fetch, resize, and serve optimized images with caching.
- [Examples](examples.md): bite-sized patterns (headers, methods, request body, env vars, secrets, service-to-service, connection reuse, etc.).
- Reference architectures: [Global API Gateway](global-api-gateway.md), [Telecom Event Processor](telecom-event-processor.md), [Real-Time Media Pipeline](real-time-media-pipeline.md), [IoT Data Ingestion](iot-data-ingestion.md).

## Roadmap and coming soon
- [Cron Triggers](cron-triggers.md) (scheduled jobs)
- Custom domains and region placement
- Platform [Observability](observability.md) (logs, metrics, traces)
- [Framework Support](framework-support.md) (auto-detection/adapters)
- SQL DB ([SQL DB](sql-db.md)) and KV bindings in runtime
- WebSocket handling patterns and private networking docs ([Network](network.md))
- Local dev quality-of-life for secrets and per-environment secret sets

## Quick checklist
- Use Secrets and Bindings; never hardcode credentials
- Set outbound timeouts and add retry with exponential backoff
- Reuse connections and lazily initialize heavy resources
- Cache with KV when appropriate (respect TTL)
- Return structured errors and include a request ID
- Monitor latency, error rates, and cold start frequency (as observability features roll out)
