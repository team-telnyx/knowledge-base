---
title: Migrate to Telnyx LiveKit
summary: Step-by-step guides for moving LiveKit workloads to Telnyx, whether you are
  coming from LiveKit Cloud or a self-hosted deployment. Both paths require no agent
  code changes — you swap credentials, redeploy, and gain built-in telephony, managed
  autoscaling, and ultra-low-latency AI on Telnyx GPUs.
sources:
- url: https://developers.telnyx.com/docs/livekit/migration/from-livekit-cloud
- url: https://developers.telnyx.com/docs/livekit/migration/from-self-hosted
updated_at: 2026-08-05T13:47:41Z
---

# Migrate to Telnyx LiveKit

Step-by-step guides for moving LiveKit workloads to Telnyx, whether you are coming from LiveKit Cloud or a self-hosted deployment. Both paths require no agent code changes — you swap credentials, redeploy, and gain built-in telephony, managed autoscaling, and ultra-low-latency AI on Telnyx GPUs.

## Overview

Migrating to Telnyx LiveKit is designed to be a zero-code-change operation. Whether you are coming from LiveKit Cloud or a self-hosted LiveKit deployment, your agent code, SDK usage, `lk` CLI commands, Dockerfiles, room management, and dispatch rules all stay the same. You swap credentials, redeploy, and Telnyx takes over the infrastructure.

## What Changes

The migration is driven by environment variable changes. The table below shows the values that differ between LiveKit Cloud and Telnyx:

| Variable | LiveKit Cloud | Telnyx |
| --- | --- | --- |
| `LIVEKIT_URL` | `https://your-project.livekit.cloud` | `https://nyc1.livekit-telnyx.com` |
| `LIVEKIT_API_KEY` | LiveKit Cloud key | Telnyx API key |
| `LIVEKIT_API_SECRET` | LiveKit Cloud secret | Your LiveKit API secret |

For self-hosted migrations, point your agent at `https://nyc1.livekit-telnyx.com` (or your [preferred region](connect.md)) instead of your existing LiveKit server URL.

## What Telnyx Replaces (Self-Hosted)

When migrating from a self-hosted deployment, Telnyx absorbs the operational components you would otherwise have to run yourself:

- LiveKit SFU server
- SIP service / Otel SIP
- TURN/STUN servers
- Container orchestration / autoscaling
- TLS termination and load balancing
- Monitoring infrastructure

## Migration Steps

The migration flow is the same for both Cloud and self-hosted sources, with a few extra steps for self-hosted.

1. **Create a Telnyx account** at [portal.telnyx.com](https://portal.telnyx.com).
2. **Generate a Telnyx API key** in the portal.
3. **Register with the platform** (one-time):

   ```
   curl -s -X POST "https://<region>.livekit-telnyx.com/provision" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "my-project",
       "api_key": "'$TELNYX_API_KEY'",
       "api_secret": "'$LIVEKIT_API_SECRET'"
     }'
   ```
4. **Update your environment variables** with the Telnyx values shown above.
5. **Deploy to Telnyx:**

   ```
   lk agent deploy . --secrets TELNYX_API_KEY=<your-key>
   ```

   For self-hosted migrations, pass any additional secrets your agent needs in the same flag, for example:

   ```
   lk agent deploy . --secrets TELNYX_API_KEY=<your-key>,OTHER_SECRET=<value>
   ```
6. **Verify** connectivity with `lk room list`.

### Additional Steps for Self-Hosted Migrations

If you are coming from a self-hosted deployment, complete these steps after the core flow above:

- **Re-create dispatch rules** on the Telnyx platform.
- **Update SIP configuration** to point at Telnyx [SIP endpoints](telephony.md).
- **Decommission** your self-hosted infrastructure (Kubernetes, TURN, Redis, etc.).

### Optional Add-Ons

After the core migration, you can optionally:

- Install the [Telnyx plugin](build.md) for on-prem STT, TTS, and LLM.
- [Buy a Telnyx number](telephony.md) for built-in telephony.

## What You Gain

Migrating to Telnyx unlocks a set of platform-level benefits that are not available on LiveKit Cloud or in a self-hosted setup:

- **No infra management** — No Kubernetes, no TURN, no Redis for multi-region.
- **Managed autoscaling** — The platform handles container lifecycle.
- **Built-in telephony, no third-party SIP fees** — On other platforms, you pay third-party SIP fees on top of your usage. On Telnyx, those are gone entirely.
- **Ultra-low latency AI on Telnyx GPUs** — STT, TTS, and LLM colocated in every region ~2ms from your agents. No round-trips to external APIs.
- **One platform, one bill** — Compute, models, telephony, and phone numbers on a single Telnyx invoice. No vendor sprawl.

## Rolling Back

Rolling back is just a matter of environment variables. Point them back at LiveKit Cloud (or your previous self-hosted endpoint) and redeploy.
