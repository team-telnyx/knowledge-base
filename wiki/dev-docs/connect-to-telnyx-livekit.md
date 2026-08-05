---
title: Connect to Telnyx LiveKit
summary: Connecting to the Telnyx LiveKit platform is a URL and credential swap —
  no code changes are required. This page covers retrieving credentials, verifying
  the connection, available regions, and SDK configuration for server SDKs.
sources:
- url: https://developers.telnyx.com/docs/livekit/connect
updated_at: 2026-08-05T13:47:30Z
---

# Connect to Telnyx LiveKit

Connecting to the Telnyx LiveKit platform is a URL and credential swap — no code changes are required. This page covers retrieving credentials, verifying the connection, available regions, and SDK configuration for server SDKs.

## Get your credentials

Complete [LiveKit Quickstart](livekit-quickstart.md) — Step 1 to set your environment variables and register with the platform. That one-time setup covers everything you need to connect.

If you are already set up, make sure the following environment variables are exported in your shell:

- `LIVEKIT_URL`
- `LIVEKIT_API_KEY`
- `LIVEKIT_API_SECRET`

Verify the connection by listing rooms:

```
lk room list
```

## Available regions

See [LiveKit Regions](livekit-regions.md) for all available platform and SIP endpoints.

## SDK configuration

Server SDKs (Python, Go, Node.js) only need the URL and credentials. For example, in Python:

```python
from livekit.api import LiveKitAPI

api = LiveKitAPI(
    url="https://nyc1.livekit-telnyx.com",
    api_key="<your-telnyx-api-key>",
    api_secret="<your-livekit-api-secret>",
)
```

If you are migrating from LiveKit Cloud or a self-hosted deployment, change the three environment variables and everything else stays the same.
