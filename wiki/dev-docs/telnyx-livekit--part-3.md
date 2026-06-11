---
title: Telnyx LiveKit
summary: Telnyx LiveKit is a managed platform for building, deploying, and scaling
  voice AI agents on Telnyx infrastructure. It combines the LiveKit agent framework
  with built-in SIP trunking, colocated GPU inference for STT/TTS/LLM, and automatic
  autoscaling — collapsing the voice AI stack into a single platform with one bill.
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
updated_at: 2026-06-11T10:35:15Z
---

# Telnyx LiveKit

*Part 3 of 3 — see also: [Part 1](telnyx-livekit--part-1.md), [Part 2](telnyx-livekit--part-2.md)*

Telnyx LiveKit is a managed platform for building, deploying, and scaling voice AI agents on Telnyx infrastructure. It combines the LiveKit agent framework with built-in SIP trunking, colocated GPU inference for STT/TTS/LLM, and automatic autoscaling — collapsing the voice AI stack into a single platform with one bill.

## Migration

### From LiveKit Cloud

Zero code changes. Swap your credentials, redeploy, done.

| Variable | LiveKit Cloud | Telnyx |
|---|---|---|
| `LIVEKIT_URL` | `https://your-project.livekit.cloud` | `https://nyc1.livekit-telnyx.com` |
| `LIVEKIT_API_KEY` | LiveKit Cloud key | Telnyx API key |
| `LIVEKIT_API_SECRET` | LiveKit Cloud secret | Your LiveKit API secret |

**Steps:**

1. Create a Telnyx account at [portal.telnyx.com](https://portal.telnyx.com)
2. Generate a Telnyx API key in the portal
3. Register with the platform (one-time):

   ```bash
   curl -s -X POST "https://<region>.livekit-telnyx.com/provision" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "my-project",
       "api_key": "'$TELNYX_API_KEY'",
       "api_secret": "'$LIVEKIT_API_SECRET'"
     }'
   ```

4. Update your environment variables with the values above
5. Deploy: `lk agent deploy . --secrets TELNYX_API_KEY=<your-key>`
6. Verify: `lk room list`
7. (Optional) Install the Telnyx plugin for on-prem STT, TTS, and LLM
8. (Optional) Buy a Telnyx number for built-in telephony

What doesn't change: your agent code, SDK usage, `lk` CLI commands, Dockerfiles, room management, and dispatch rules.

Rolling back is just environment variables — point them back at LiveKit Cloud and redeploy.

### From self-hosted

Keep your agents, ditch the infrastructure. No more managing Kubernetes clusters, TURN servers, SIP services, or autoscaling.

**What Telnyx replaces:** LiveKit SFU server, SIP service / Otel SIP, TURN/STUN servers, container orchestration / autoscaling, TLS termination and load balancing, monitoring infrastructure.

**What stays the same:** your agent code, SDK calls, room management logic, dispatch rules.

**Steps:**

1. Create a Telnyx account at [portal.telnyx.com](https://portal.telnyx.com)
2. Generate a Telnyx API key in the portal
3. Register with the platform (one-time) using the same `curl` provision command as above
4. Update your agent to point at `https://nyc1.livekit-telnyx.com` (or your preferred region)
5. Move secrets to the platform: `lk agent deploy . --secrets TELNYX_API_KEY=<your-key>,OTHER_SECRET=<value>`
6. Re-create dispatch rules on the Telnyx platform
7. Update SIP configuration to point at Telnyx SIP endpoints
8. Verify your agent is running: `lk room list`
9. Decommission your self-hosted infrastructure

## Platform Limits

| Limit | Value |
|---|---|
| Build timeout | 10 minutes |
| Build context size | 1 GB |
| Max concurrent agents | Contact us |
| Max concurrent sessions per agent | Contact us |
| Max concurrent calls | Contact us |

For specific limit increases, contact your Telnyx account team.
