---
title: Connect to Telnyx
summary: Point your LiveKit CLI and SDKs at the Telnyx platform.
sources:
  - url: https://developers.telnyx.com/docs/livekit/connect
    content_hash: 917d5ca7044b770a9a4615d318d562d4d35c32b61787d3f62d2b0b1f28c01e72
updated_at: 2026-04-10T00:00:00Z
---

# Connect to Telnyx

Point your LiveKit CLI and SDKs at the Telnyx platform.

Connecting to the Telnyx LiveKit platform is a URL and credential swap. No code changes.

## Get your credentials

Complete [Quickstart — Step 1](../tutorial/quick-start.md#step-1-configure-the-cli) to set your environment variables and register with the platform. That one-time setup covers everything you need to connect.

> **Note:** Already set up? Just make sure your `LIVEKIT_URL`, `LIVEKIT_API_KEY`, and `LIVEKIT_API_SECRET` are exported in your shell.

Verify the connection:

```bash theme={null}
lk room list
```

## Available regions

See [Regions](regions.md) for all available platform and SIP endpoints.

## SDK configuration

Server SDKs (Python, Go, Node.js) just need the URL and credentials:

```python theme={null}
from livekit.api import LiveKitAPI

api = LiveKitAPI(
    url="https://nyc1.livekit-telnyx.com",
    api_key="<your-telnyx-api-key>",
    api_secret="<your-livekit-api-secret>",
)
```

If you're migrating from LiveKit Cloud or self-hosted, change the three environment variables and everything else stays the same.
