---
title: LiveKit on Telnyx
summary: Telnyx LiveKit is a managed platform for deploying voice AI agents at scale,
  combining LiveKit's agent framework with built-in telephony, colocated AI inference
  on Telnyx GPUs, and managed infrastructure across multiple regions. This page covers
  architecture, compatibility, regions, quickstart, build, deploy, models (STT/TTS/LLM),
  telephony, observability, limits, pricing, and migration from LiveKit Cloud or self-hosted.
sources:
- url: https://developers.telnyx.com/docs/livekit/architecture
- url: https://developers.telnyx.com/docs/livekit/build/index
- url: https://developers.telnyx.com/docs/livekit/compatibility
- url: https://developers.telnyx.com/docs/livekit/connect
- url: https://developers.telnyx.com/docs/livekit/deploy/configuration
- url: https://developers.telnyx.com/docs/livekit/deploy/index
- url: https://developers.telnyx.com/docs/livekit/deploy/management
- url: https://developers.telnyx.com/docs/livekit/deploy/secrets
- url: https://developers.telnyx.com/docs/livekit/index
- url: https://developers.telnyx.com/docs/livekit/limits
- url: https://developers.telnyx.com/docs/livekit/migration/from-livekit-cloud
- url: https://developers.telnyx.com/docs/livekit/migration/from-self-hosted
- url: https://developers.telnyx.com/docs/livekit/models/index
- url: https://developers.telnyx.com/docs/livekit/models/llm
- url: https://developers.telnyx.com/docs/livekit/models/stt
- url: https://developers.telnyx.com/docs/livekit/models/tts
- url: https://developers.telnyx.com/docs/livekit/observability/index
- url: https://developers.telnyx.com/docs/livekit/pricing
- url: https://developers.telnyx.com/docs/livekit/quickstart
- url: https://developers.telnyx.com/docs/livekit/regions
- url: https://developers.telnyx.com/docs/livekit/telephony
updated_at: 2026-07-17T09:14:35Z
---

# LiveKit on Telnyx

*Part 6 of 6 — see also: [Part 1](livekit-on-telnyx--part-1.md), [Part 2](livekit-on-telnyx--part-2.md), [Part 3](livekit-on-telnyx--part-3.md), [Part 4](livekit-on-telnyx--part-4.md), [Part 5](livekit-on-telnyx--part-5.md)*

Telnyx LiveKit is a managed platform for deploying voice AI agents at scale, combining LiveKit's agent framework with built-in telephony, colocated AI inference on Telnyx GPUs, and managed infrastructure across multiple regions. This page covers architecture, compatibility, regions, quickstart, build, deploy, models (STT/TTS/LLM), telephony, observability, limits, pricing, and migration from LiveKit Cloud or self-hosted.

## Migration

### From LiveKit Cloud

Zero code changes. Swap your credentials, redeploy, done.

What changes:

|  | LiveKit Cloud | Telnyx |
| --- | --- | --- |
| `LIVEKIT_URL` | `https://your-project.livekit.cloud` | `https://nyc1.livekit-telnyx.com` |
| `LIVEKIT_API_KEY` | LiveKit Cloud key | Telnyx API key |
| `LIVEKIT_API_SECRET` | LiveKit Cloud secret | Your LiveKit API secret |

What doesn't change:

- Your agent code
- SDK usage
- `lk` CLI commands
- Dockerfiles
- Room management, dispatch rules

Steps:

1. **Create a Telnyx account** at [portal.telnyx.com](https://portal.telnyx.com)
2. **Generate a Telnyx API key** in the portal
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
4. **Update your environment variables** with the values above
5. **Deploy to Telnyx:**

   ```
   lk agent deploy . --secrets TELNYX_API_KEY=<your-key>
   ```
6. **Verify:** `lk room list` to confirm connectivity
7. **(Optional)** Install the [Telnyx plugin](build.md) for on-prem STT, TTS, and LLM
8. **(Optional)** Buy a Telnyx number for built-in telephony

What you gain:

- **Built-in telephony, no third-party SIP fees** — On other platforms, you pay third-party SIP fees on top of your usage. On Telnyx, those are gone entirely.
- **Ultra-low latency AI on Telnyx GPUs** — STT, TTS, and LLM colocated in every region ~2ms from your agents. No round-trips to external APIs.
- **One platform, one bill** — Compute, models, telephony, and phone numbers on a single Telnyx invoice. No vendor sprawl.

Rolling back is just environment variables. Point them back at LiveKit Cloud and redeploy.

### From self-hosted

Keep your agents, ditch the infrastructure. No more managing Kubernetes clusters, TURN servers, SIP services, or autoscaling.

What Telnyx replaces:

- LiveKit SFU server
- SIP service / Otel SIP
- TURN/STUN servers
- Container orchestration / autoscaling
- TLS termination and load balancing
- Monitoring infrastructure

What stays the same:

- Your agent code
- SDK calls
- Room management logic
- Dispatch rules

Steps:

1. **Create a Telnyx account** at [portal.telnyx.com](https://portal.telnyx.com)
2. **Generate a Telnyx API key** in the portal
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
4. **Update your agent** to point at `https://nyc1.livekit-telnyx.com` (or your preferred region)
5. **Move secrets** to the platform:

   ```
   lk agent deploy . --secrets TELNYX_API_KEY=<your-key>,OTHER_SECRET=<value>
   ```
6. **Re-create dispatch rules** on the Telnyx platform
7. **Update SIP configuration** to point at Telnyx SIP endpoints
8. **Verify** your agent is running: `lk room list`
9. **Decommission** your self-hosted infrastructure

What you gain:

- **No infra management** — No Kubernetes, no TURN, no Redis for multi-region.
- **Built-in SIP, no third-party SIP fees** — On other platforms, you pay third-party SIP fees on top of your usage. On Telnyx, those are gone entirely.
- **Managed autoscaling** — Platform handles container lifecycle.
- **Ultra-low latency AI on Telnyx GPUs** — STT, TTS, and LLM colocated in every region ~2ms from your agents. No round-trips to external APIs.
