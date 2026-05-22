---
title: Reference Architectures
summary: Reference architectures show how to combine Telnyx Edge Compute products
  to solve common problems, with diagrams, component breakdowns, and sample implementations.
  This guide summarizes four blueprints—Global API Gateway, Telecom Event Processor,
  Real-Time Media Pipeline, and IoT Data Ingestion—and notes upcoming framework support
  for deploying popular web frameworks with minimal changes.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/index
  content_hash: 7d7e65f9f9897d0f761c5dd5478fd6bf8118d3a2a13adfd6785108c43d89a51b
- url: https://developers.telnyx.com/docs/edge-compute/frameworks-support
  content_hash: 4bfb8d2f48a2bf25dc1cdf6c7ff3877f462bce399fa6cb6714fb6a01a799d61a
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/global-api-gateway
  content_hash: feb19f82c850c67839e62558955e8d490b00a9691878b900622e4a3de116ac15
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/iot-data-ingestion
  content_hash: e5a589bf41837d330bcd37a282528d74f0862208f56b05669a4f533667a68c65
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/real-time-media-pipeline
  content_hash: 64d024d16fda5f13581ce2e2d9cd85d7fd69a1e02b775f56b9b99b347466b5f9
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/telecom-event-processor
  content_hash: e2fca500731fca2b0229eed00d88f3455bdb35dbcdb780dcd923bdec983840f4
updated_at: 2026-05-20T08:18:53Z
---

# Reference Architectures

*Part 2 of 2 — see also: [Part 1](reference-architectures--part-1.md)*

Reference architectures show how to combine Telnyx Edge Compute products to solve common problems, with diagrams, component breakdowns, and sample implementations. This guide summarizes four blueprints—Global API Gateway, Telecom Event Processor, Real-Time Media Pipeline, and IoT Data Ingestion—and notes upcoming framework support for deploying popular web frameworks with minimal changes.

## Real-Time Media Pipeline
Ingest, transform, and route live media (video/audio) at the edge to storage, CDN, and real‑time distribution.

### Architecture
```
Media Source (Camera)
        │
        ▼
Telnyx Edge: Ingest → Transform → Route
        │
  ┌─────┴───────────────┬───────────────┐
  ▼                     ▼               ▼
Archive (S3)          CDN            LiveKit/SFU
```

### Sample implementation (Python-like pseudocode)
```python
import asyncio
from datetime import datetime

class MediaPipeline:
    async def handler(self, request):
        ctype = request.headers.get("Content-Type", "")
        if any(t in ctype for t in ("video", "audio")):
            return await self.process_media(request)
        if "application/json" in ctype:
            return await self.handle_control(request)
        return {"status": 400, "body": "Unsupported content type"}

    async def process_media(self, request):
        data = await request.bytes()
        stream_id = request.headers.get("X-Stream-ID")
        processed = await self.transform(data)
        await asyncio.gather(
            self.store_archive(stream_id, processed),
            self.push_to_cdn(stream_id, processed),
            self.forward_to_livekit(stream_id, processed)
        )
        return {"status": 200, "body": "OK"}

    async def transform(self, data):
        # e.g., transcode, watermark, thumbnails
        return data

    async def store_archive(self, sid, data):
        await self.s3.put_object(Bucket="media-archive", Key=f"{sid}/{datetime.utcnow().isoformat()}.webm", Body=data)

    async def push_to_cdn(self, sid, data):
        await fetch(f"{self.cdn_ingest_url}/{sid}", {"method": "POST", "body": data})

    async def forward_to_livekit(self, sid, data):
        await fetch(f"{self.livekit_url}/ingest/{sid}", {
            "method": "POST",
            "headers": {"Authorization": f"Bearer {self.livekit_token}"},
            "body": data
        })

    async def handle_control(self, request):
        body = await request.json()
        action, sid = body.get("action"), body.get("stream_id")
        if action == "start":
            return {"status": 200, "body": {"stream_id": sid, "status": "started"}}
        if action == "stop":
            return {"status": 200, "body": {"stream_id": sid, "status": "stopped"}}
        return {"status": 400, "body": {"error": "Unknown action"}}
```

### When to use
- Live streaming pipelines
- Video conferencing with edge transformations
- Surveillance and camera feed preprocessing

## IoT Data Ingestion
Collect sensor data globally with validation and light enrichment at the edge before central storage.

### Architecture
```
IoT Devices (Global) ──▶ Telnyx Edge: Validate + Parse → Aggregate/Enrich
                                   │
                                   ▼
                             Central Data Lake
```

### Sample implementation (JavaScript)
```js
export async function handler(request) {
  const data = await request.json();
  if (!isValid(data)) {
    return new Response(JSON.stringify({ error: "Invalid data" }), { status: 400 });
  }
  const enriched = {
    ...data,
    edge_pop: process.env.TELNYX_POP,
    received_at: Date.now(),
    device_id: request.headers.get("X-Device-ID")
  };
  const res = await fetch(process.env.DATA_LAKE_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ reading: enriched, edge_pop: process.env.TELNYX_POP })
  });
  if (!res.ok) {
    return new Response(JSON.stringify({ error: "Failed to store" }), { status: 502 });
  }
  return new Response(JSON.stringify({ received: true }));
}

function isValid(d) {
  return d.sensor_type && typeof d.value === "number" && d.timestamp;
}
```

### Operational notes
- For high‑volume ingestion and batching, buffer to an external durable queue (e.g., Kafka, Redis Streams). Avoid in‑memory buffers inside serverless functions due to cold starts and recycling.
- Enrich minimally at the edge (e.g., PoP, device ID, timestamp); perform heavy analytics in the data lake.

## Framework Support (Coming Soon)
Framework auto‑detection and adapters are in development to let you deploy popular web frameworks on Edge Compute with minimal changes. Until then, start from the examples above or see [Examples](examples.md) and [Local Development](local-development.md) to adapt your existing app.

## Related Resources
- [Quick Start](quick-start.md) — Deploy your first function
- [Examples](examples.md) — Common patterns and snippets
- [Runtime](runtime.md) and [Bindings](bindings.md) — Execution environment and integrations
- [Execution Model](execution-model.md) — Concurrency and lifecycle
- [Local Development](local-development.md) — Develop and test locally
- [Testing](testing.md) — Strategies and tooling
- [CI/CD](ci-cd.md) — Automate deployments
- [Edge Compute observability](edge-compute-observability.md) — Logs, metrics, traces
- [CLI Reference](cli-reference.md) — Commands and flags
- [Edge Compute architecture](edge-compute-architecture.md) — Platform internals
- [Edge Compute limits and quotas](edge-compute-limits-and-quotas.md) — Resource limits
