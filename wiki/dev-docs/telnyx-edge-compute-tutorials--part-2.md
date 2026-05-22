---
title: Telnyx Edge Compute Tutorials
summary: Learn Telnyx Edge by building real applications. This guide curates four
  end‑to‑end demos (REST API, SMS webhook, voice call router, image resizer), plus
  patterns you’ll reuse across projects and links to quickstarts and references.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/demos/index
  content_hash: 5ea65ece207f150aff2863d1253518a472c63bd2dc715d4c7b3a7e12794df16a
- url: https://developers.telnyx.com/docs/edge-compute/demos/build-a-rest-api
  content_hash: e765fba7ddff7436cd737dcdd5023e103d29f768abc3dbaf48ddc656651e115a
- url: https://developers.telnyx.com/docs/edge-compute/demos/image-resizer
  content_hash: ec0c36e94f27fff4cef95fbb395e5640b645b7c56ec90a8ee62f8568407a2caa
- url: https://developers.telnyx.com/docs/edge-compute/demos/sms-webhook-handler
  content_hash: 28105ddde5f22d2415da1b661df668558d597ef0f292a1a00529acc2ffd1b7d5
- url: https://developers.telnyx.com/docs/edge-compute/demos/voice-call-router
  content_hash: 753a96661329d8b0d80ded53a20dc50c27c0bda083510a0683a02a3ef759941e
- url: https://developers.telnyx.com/docs/edge-compute/examples/index
  content_hash: c5e15adaa65fb24f03323d1311b2fa9cc0cd3ae66d5e1e42d276ecaf7319d485
updated_at: 2026-05-20T08:25:26Z
---

# Telnyx Edge Compute Tutorials

*Part 2 of 2 — see also: [Part 1](telnyx-edge-compute-tutorials--part-1.md)*

Learn Telnyx Edge by building real applications. This guide curates four end‑to‑end demos (REST API, SMS webhook, voice call router, image resizer), plus patterns you’ll reuse across projects and links to quickstarts and references.

## Image Resizer (20 min · Intermediate)
Resize and optimize images on‑the‑fly from URL parameters, with caching.

1) Create a function and add dependencies

```
telnyx-edge new-func -l=python -n=image-resizer
cd image-resizer
echo -e "pillow>=10.0.0\nhttpx>=0.27.0" > requirements.txt
```

2) Implement src/main.py

```python
from PIL import Image
from io import BytesIO
from urllib.parse import urlparse, parse_qs
import base64, httpx

class Function:
    def __init__(self):
        self.client = httpx.AsyncClient()

    async def handler(self, request):
        params = parse_qs(urlparse(request.url).query)
        image_url = params.get("url", [None])[0]
        width = int(params.get("w", [0])[0]) or None
        height = int(params.get("h", [0])[0]) or None
        quality = int(params.get("q", [85])[0])
        if not image_url:
            return {"status": 400, "body": "Missing url parameter"}
        response = await self.client.get(image_url)
        if response.status_code != 200:
            return {"status": 404, "body": "Image not found"}
        img = Image.open(BytesIO(response.content))
        if width or height:
            if width and height:
                img = img.resize((width, height), Image.LANCZOS)
            elif width:
                ratio = width / img.width
                img = img.resize((width, int(img.height * ratio)), Image.LANCZOS)
            else:
                ratio = height / img.height
                img = img.resize((int(img.width * ratio), height), Image.LANCZOS)
        out = BytesIO()
        img.save(out, format="JPEG", quality=quality, optimize=True)
        return {
            "status": 200,
            "headers": {"Content-Type": "image/jpeg", "Cache-Control": "public, max-age=86400"},
            "body": base64.b64encode(out.getvalue()).decode()
        }
```

3) Deploy and test

```
telnyx-edge ship
```
Example request:

```
https://image-resizer-{orgId}.telnyxcompute.com/?url=https://example.com/photo.jpg&w=400&q=80
```

## Common patterns you’ll use
Reapply these snippets and concepts (see full coverage in [Edge Compute Examples](edge-compute-examples.md)):

- Return JSON and HTML: consistent status codes and Content-Type headers
- Parse query parameters: URL parsing (for example, Python’s urllib.parse)
- Handle HTTP methods: route by request.method with 405 for unsupported verbs
- Read request bodies safely: validate JSON and required fields
- Use environment variables and secrets: configure with telnyx-edge secrets add; access via process.env or os.environ
- KV storage (coming soon): low‑latency key‑value access via Telnyx Storage APIs
- Cron triggers (coming soon): scheduled invocations with X-Telnyx-Cron headers
- Connection reuse: initialize HTTP clients once per module for better performance

## More tutorials on the way
- Authentication middleware (JWT validation)
- Rate limiter (sliding windows)
- A/B testing (traffic splitting)
- Webhook validator (signature verification)

## Related resources
- [Edge Compute Quickstart](edge-compute-quickstart.md) — deploy your first function
- [Edge Compute Examples](edge-compute-examples.md) — bite‑sized patterns across languages
- [Edge Compute CLI Reference](edge-compute-cli-reference.md) — full command documentation
- [Reference Architectures](reference-architectures--part-1.md) — Global API Gateway, Telecom Event Processor, Real‑Time Media Pipeline, IoT Ingestion
