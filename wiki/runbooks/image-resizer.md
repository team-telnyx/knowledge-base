---
title: Image Resizer
summary: Resize and optimize images on-the-fly at the edge.
sources:
  - url: https://developers.telnyx.com/docs/edge-compute/demos/image-resizer
    content_hash: dc40eebd448c5209d622b3c71f4866eb08667eeaf21abf6002832bd2bc7bb111
updated_at: 2026-04-10T00:00:00Z
---

# Image Resizer

Resize and optimize images on-the-fly at the edge.

Resize and optimize images on-the-fly based on URL parameters.

**What you'll learn:**

* Processing binary data
* Query parameter handling
* Caching strategies

## Step 1: Create the Function

```bash theme={null}
telnyx-edge new-func -l=python -n=image-resizer
cd image-resizer
```

## Step 2: Add Dependencies

Create or update `requirements.txt`:

```txt theme={null}
pillow>=10.0.0
httpx>=0.27.0
```

## Step 3: Implement the Resizer

```python theme={null}
from PIL import Image
from io import BytesIO
from urllib.parse import urlparse, parse_qs
import base64
import httpx

class Function:
    def __init__(self):
        self.client = httpx.AsyncClient()

    async def handler(self, request):
        params = parse_qs(urlparse(request.url).query)

        # Get parameters
        image_url = params.get("url", [None])[0]
        width = int(params.get("w", [0])[0]) or None
        height = int(params.get("h", [0])[0]) or None
        quality = int(params.get("q", [85])[0])

        if not image_url:
            return {"status": 400, "body": "Missing url parameter"}

        # Fetch original image
        response = await self.client.get(image_url)
        if response.status_code != 200:
            return {"status": 404, "body": "Image not found"}

        # Process image
        img = Image.open(BytesIO(response.content))

        # Resize if dimensions provided
        if width or height:
            if width and height:
                img = img.resize((width, height), Image.LANCZOS)
            elif width:
                ratio = width / img.width
                img = img.resize((width, int(img.height * ratio)), Image.LANCZOS)
            else:
                ratio = height / img.height
                img = img.resize((int(img.width * ratio), height), Image.LANCZOS)

        # Convert to bytes
        output = BytesIO()
        img.save(output, format="JPEG", quality=quality, optimize=True)

        return {
            "status": 200,
            "headers": {
                "Content-Type": "image/jpeg",
                "Cache-Control": "public, max-age=86400"
            },
            "body": base64.b64encode(output.getvalue()).decode()
        }
```

## Step 4: Deploy and Test

```bash theme={null}
telnyx-edge ship
```

Test with:

```
https://image-resizer-{orgId}.telnyxcompute.com/?url=https://example.com/photo.jpg&w=400&q=80
```
