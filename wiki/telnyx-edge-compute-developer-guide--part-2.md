---
title: Telnyx Edge Compute — Developer Guide
summary: A concise, end-to-end guide to building, configuring, deploying, and operating
  serverless functions on Telnyx’s global edge. Covers runtime and execution model,
  configuration (env vars, secrets, bindings), routing, performance and reliability
  patterns, security guidance, KV storage, CI/CD, limits, tutorials, and upcoming
  features.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/best-practices
  content_hash: 7b3fb7e4f5524b7cba6e9e0530959a8f9873ae82c5f0923b90029f018b887453
- url: https://developers.telnyx.com/docs/edge-compute/configuration
  content_hash: a35cf8fc926cd34c587123eaac411cfc2376d8d35bf79a7182b5ea4bc46b4c7d
- url: https://developers.telnyx.com/docs/edge-compute/configuration/cron-triggers
  content_hash: f526ae7609d9936069ab66a27aaee1e73642156e31daa909b506fe3d87395958
- url: https://developers.telnyx.com/docs/edge-compute/configuration/environment-variables
  content_hash: f4c4fbf7795dd1c9c65271cf25ede227bd1916ef8d1804cd1581003a11c2a69d
- url: https://developers.telnyx.com/docs/edge-compute/configuration/routing
  content_hash: f557e78257201cad46963554f836b7e413aced35a02b8abaf28ca2b9b141ff18
- url: https://developers.telnyx.com/docs/edge-compute/configuration/secrets
  content_hash: fc928e535154be6661b93daee6902d5b5506c57bc9a6f2189ff7a2bbfc74c6ce
- url: https://developers.telnyx.com/docs/edge-compute/configuration/versions
  content_hash: ac0f646bf3a335ac7e1c95a79f29844a83b15e0f2f55e030bcb1f17d8af15ffb
- url: https://developers.telnyx.com/docs/edge-compute/demos
  content_hash: 5ea65ece207f150aff2863d1253518a472c63bd2dc715d4c7b3a7e12794df16a
- url: https://developers.telnyx.com/docs/edge-compute/demos/build-a-rest-api
  content_hash: e765fba7ddff7436cd737dcdd5023e103d29f768abc3dbaf48ddc656651e115a
- url: https://developers.telnyx.com/docs/edge-compute/demos/image-resizer
  content_hash: ec0c36e94f27fff4cef95fbb395e5640b645b7c56ec90a8ee62f8568407a2caa
- url: https://developers.telnyx.com/docs/edge-compute/demos/sms-webhook-handler
  content_hash: 28105ddde5f22d2415da1b661df668558d597ef0f292a1a00529acc2ffd1b7d5
- url: https://developers.telnyx.com/docs/edge-compute/demos/voice-call-router
  content_hash: 753a96661329d8b0d80ded53a20dc50c27c0bda083510a0683a02a3ef759941e
- url: https://developers.telnyx.com/docs/edge-compute/deploy
  content_hash: 7e1e9f5abaa01d2a8c01013e934c94a791d74b86ccbbb98556d3ba89a7a33478
- url: https://developers.telnyx.com/docs/edge-compute/development
  content_hash: de8bd0104bbdd2920ddd2521e75dfbedd39e50cf8e628e0592b646e3a4df5797
- url: https://developers.telnyx.com/docs/edge-compute/examples
  content_hash: 0edaaa0b78f2afcc1c6cf202c7693658243394d6a191a96a582f9466ca11daa4
- url: https://developers.telnyx.com/docs/edge-compute/frameworks
  content_hash: 7d7e65f9f9897d0f761c5dd5478fd6bf8118d3a2a13adfd6785108c43d89a51b
- url: https://developers.telnyx.com/docs/edge-compute/frameworks-support
  content_hash: a589c5f6ddc27e3e08fe75cbd247172dc89ba136ec295da1fea1fcdc8d889839
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/global-api-gateway
  content_hash: feb19f82c850c67839e62558955e8d490b00a9691878b900622e4a3de116ac15
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/iot-data-ingestion
  content_hash: e5a589bf41837d330bcd37a282528d74f0862208f56b05669a4f533667a68c65
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/real-time-media-pipeline
  content_hash: 64d024d16fda5f13581ce2e2d9cd85d7fd69a1e02b775f56b9b99b347466b5f9
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/telecom-event-processor
  content_hash: e2fca500731fca2b0229eed00d88f3455bdb35dbcdb780dcd923bdec983840f4
- url: https://developers.telnyx.com/docs/edge-compute/kv/api-reference
  content_hash: 9e592a2bf61e4d9097ca597d57622db0fcb1d4ca7d81f123f073e614ff3d5faa
- url: https://developers.telnyx.com/docs/edge-compute/kv/cli
  content_hash: cef46af7e62fcf59bff692b0708a78fa50b344b7d9d65142cc094c29760737fa
- url: https://developers.telnyx.com/docs/edge-compute/kv/pricing
  content_hash: aceb7fbcdcd8fc828cb4e8d0fb48e1e8c2b30c7e799c3eb4ddc47ccba2ce4be5
- url: https://developers.telnyx.com/docs/edge-compute/kv/quick-start
  content_hash: 6ac32f6799480ec2a8b2f156f813bd0551b12ec529fbc22c48cdf8bdf4e08204
- url: https://developers.telnyx.com/docs/edge-compute/kv/ttl-and-metadata
  content_hash: 5bcc7143f0bb8c933d6f9ac581c9f46ff0a614b988fc4e90b9bc33183c903762
- url: https://developers.telnyx.com/docs/edge-compute/kv/use-cases
  content_hash: 8ac2275f85cf764b9da32880e0369003695489e081a7b4a30494763c2c8ef79c
- url: https://developers.telnyx.com/docs/edge-compute/network
  content_hash: 6cb6dc9923a84ff85600c722a2659ccf843c4629973c777d97863266be5900aa
- url: https://developers.telnyx.com/docs/edge-compute/observability
  content_hash: 4eaee9817259a0b7da73dbbe24d2f4fceae0b43c9a86c8bcce8aedea7fee73e9
- url: https://developers.telnyx.com/docs/edge-compute/overview
  content_hash: 2b963aed72f0fddd44f3d0f9a698af6838f905f15eb77ab55453e25fc2a477ce
- url: https://developers.telnyx.com/docs/edge-compute/platform-overview
  content_hash: 84a7e22ec65304624462300a6ca97fd543b43e4c9f1a9eb28fddfb953d95dffa
- url: https://developers.telnyx.com/docs/edge-compute/products
  content_hash: cd26142c6ba038b6171f2f4fcb3bbbc7b14e6ec66b0ddc7163dd50c8773b0f06
- url: https://developers.telnyx.com/docs/edge-compute/quickstart
  content_hash: c5a6cf625195a1f599c110e3fba52f196e91c830ae16b853fbc52d3148ad3177
- url: https://developers.telnyx.com/docs/edge-compute/reference/architecture
  content_hash: b54771dd5fac92eba49cabe366712956b5a829deba47500b91e9d97f58c86d4b
- url: https://developers.telnyx.com/docs/edge-compute/reference/cli
  content_hash: 49aae6d4a62af4c43683e58a13f2ce1d2a6869de3d9f41425418a52b394526cd
- url: https://developers.telnyx.com/docs/edge-compute/reference/limits
  content_hash: 25e024949cb9051b3a8289f1b56910872db0fad2d742aba7317126c21902c513
- url: https://developers.telnyx.com/docs/edge-compute/runtime
  content_hash: 31622c04a8e1fa69b21ad762e43fef34048cddc891adbce8d25d78c9f939c6d8
- url: https://developers.telnyx.com/docs/edge-compute/runtime/bindings
  content_hash: d45211d6d9ea48f8a717d2f8a4b0b7083376b9afb921e4a659ec98ecf7caf8c5
- url: https://developers.telnyx.com/docs/edge-compute/runtime/execution-model
  content_hash: 6e86826e8fbacef6c19a57672d90da01d08644a571e433481527ff992f720b6d
- url: https://developers.telnyx.com/docs/edge-compute/sqldb
  content_hash: 0d230cd6514b60d5fff971d6c9b516c9f5cc70679482b6bd2caa35be9a33b147
- url: https://developers.telnyx.com/docs/edge-compute/testing
  content_hash: 5315563a13131f228a0834769a288c98e7b41a6f7e5f695a5ca45a7633de5564
updated_at: 2026-05-08T13:07:32Z
---

# Telnyx Edge Compute — Developer Guide

*Part 2 of 2 — see also: [Part 1](telnyx-edge-compute-developer-guide--part-1.md)*

A concise, end-to-end guide to building, configuring, deploying, and operating serverless functions on Telnyx’s global edge. Covers runtime and execution model, configuration (env vars, secrets, bindings), routing, performance and reliability patterns, security guidance, KV storage, CI/CD, limits, tutorials, and upcoming features.

## Tutorials and reference architectures
- Quickstarts and demos: Build a REST API, SMS webhook handler, voice call router, and an image resizer in minutes.
- Reference architectures: Global API Gateway (auth, rate limiting, caching), Telecom Event Processor (voice/SMS/fax webhooks), Real-Time Media Pipeline, IoT Data Ingestion.

## Roadmap and “coming soon”
- Cron triggers (use an external scheduler like GitHub Actions until available).
- Custom domains and region pinning for routing and residency.
- Version history and rollback commands in CLI.
- Framework auto-detection/adapters, WebSockets, Observability suite.
- SQL DB (serverless, SQLite-compatible) and KV/SQL bindings.
- Edge networking docs and advanced private networking.

## Best-practice checklist
- Configuration
  - Use env vars for non-sensitive settings; secrets for credentials.
  - Name functions and routes clearly; set explicit, conservative timeouts.
- Performance
  - Reuse HTTP/DB clients; lazy-load heavy code; keep handlers focused.
  - Cache with KV where appropriate and set TTLs.
- Reliability & security
  - Validate inputs; set outbound timeouts and retries with backoff.
  - Return structured errors and include a request ID; use HTTPS only.
  - Don’t log secrets/PII.
- Delivery
  - Automate with CI/CD; run tests before deploy; add a health check step.
  - Plan Git-based rollbacks; monitor latency/error rates after deploy.
- Limits
  - Stream large data, avoid unbounded caches, and keep under size/time/memory caps.

For deeper dives, see the linked pages for configuration, bindings, KV, CI/CD, architecture, and limits.
