---
title: Real-Time Media Pipeline
summary: Transform and route media streams at the edge.
sources:
  - url: https://developers.telnyx.com/docs/edge-compute/frameworks/real-time-media-pipeline
    content_hash: f27f29f383c308c6cab043555a8919058113a409bcbbad13ce6f0c3d7271551d
updated_at: 2026-04-10T00:00:00Z
---

# Real-Time Media Pipeline

Transform and route media streams at the edge.

Transform and route media streams for video, audio, and real-time communication.

## Architecture Diagram

```
┌─────────────┐      ┌─────────────────────────────────────────┐
│   Media     │      │           Telnyx Edge                    │
│   Source    │─────▶│  ┌──────────┐  ┌──────────┐  ┌────────┐ │
│  (Camera)   │      │  │ Ingest   │→ │Transform │→ │ Route  │ │
└─────────────┘      │  └──────────┘  └──────────┘  └────────┘ │
                     └─────────────────────────────────────────┘
                                        │
                     ┌──────────────────┼──────────────────┐
                     ▼                  ▼                  ▼
               ┌──────────┐      ┌──────────┐      ┌──────────┐
               │ Storage  │      │  CDN     │      │ LiveKit  │
               │ (S3)     │      │ Delivery │      │ Stream   │
               └──────────┘      └──────────┘      └──────────┘
```

## Implementation

```python theme={null}
import asyncio
from datetime import datetime

class MediaPipeline:
    async def handler(self, request):
        content_type = request.headers.get("Content-Type", "")

        if "video" in content_type or "audio" in content_type:
            return await self.process_media(request)
        elif "application/json" in content_type:
            return await self.handle_control(request)
        else:
            return {"status": 400, "body": "Unsupported content type"}

    async def process_media(self, request):
        media_data = await request.bytes()
        stream_id = request.headers.get("X-Stream-ID")

        # Transform (e.g., transcode, watermark)
        processed = await self.transform(media_data)

        # Route to destinations
        await asyncio.gather(
            self.store_archive(stream_id, processed),
            self.push_to_cdn(stream_id, processed),
            self.forward_to_livekit(stream_id, processed)
        )

        return {"status": 200, "body": "OK"}

    async def transform(self, media_data):
        # Apply transformations
        # - Resize/transcode
        # - Add watermark
        # - Extract thumbnails
        return media_data

    async def store_archive(self, stream_id, data):
        await self.s3.put_object(
            Bucket="media-archive",
            Key=f"{stream_id}/{datetime.utcnow().isoformat()}.webm",
            Body=data
        )

    async def push_to_cdn(self, stream_id, data):
        await fetch(f"{self.cdn_ingest_url}/{stream_id}", {
            "method": "POST",
            "body": data
        })

    async def forward_to_livekit(self, stream_id, data):
        # Forward to LiveKit SFU for real-time distribution
        await fetch(f"{self.livekit_url}/ingest/{stream_id}", {
            "method": "POST",
            "headers": {"Authorization": f"Bearer {self.livekit_token}"},
            "body": data
        })

    async def handle_control(self, request):
        # Handle control messages (start/stop stream, change settings)
        body = await request.json()
        action = body.get("action")
        stream_id = body.get("stream_id")

        if action == "start":
            # Initialize stream resources
            return {"status": 200, "body": {"stream_id": stream_id, "status": "started"}}
        elif action == "stop":
            # Clean up stream resources
            return {"status": 200, "body": {"stream_id": stream_id, "status": "stopped"}}
        else:
            return {"status": 400, "body": {"error": "Unknown action"}}
```

## Use Cases

* **Live streaming** — Ingest and distribute live video
* **Video conferencing** — Real-time media processing
* **Surveillance** — Edge processing for camera feeds
