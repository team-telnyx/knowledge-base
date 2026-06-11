---
title: Telnyx LiveKit
summary: Telnyx LiveKit is a managed platform for building, deploying, and scaling
  voice AI agents on Telnyx infrastructure. It combines the LiveKit agent framework
  with built-in SIP trunking, colocated GPU inference for STT/TTS/LLM, and automatic
  autoscaling — collapsing the voice AI stack into a single platform with one bill.
sources:
- url: https://developers.telnyx.com/docs/livekit/architecture
  content_hash: 562050b8d5fdf2d99199f841e1961cc03fc56ccb86847d7eba54813caac25818
- url: https://developers.telnyx.com/docs/livekit/build/index
  content_hash: 92796d9b98ce443a5da4f326451546f47053454df2a8cc0dd915b250b5b99e23
- url: https://developers.telnyx.com/docs/livekit/compatibility
  content_hash: bd35a5a936b53a502201d69456d718670eebf75d3618174239d207f3b36afff1
- url: https://developers.telnyx.com/docs/livekit/connect
  content_hash: d24764bd1616fbeda8910d52efa872444cff475e7856aa10651bf6a5a6bd0e16
- url: https://developers.telnyx.com/docs/livekit/deploy/configuration
  content_hash: 797c9f219444fa8b824f4e90623062a708003dafc04f6b05a076777b7140b3ad
- url: https://developers.telnyx.com/docs/livekit/deploy/index
  content_hash: 72ff72efab2f35776214a62ba465220ae36d5ff7291406a42860b32e94e480cf
- url: https://developers.telnyx.com/docs/livekit/deploy/management
  content_hash: 4eb1b7a2b5817de9fcd692e7fc3bcf0304ef75ea36615e220515b9de9b0a548b
- url: https://developers.telnyx.com/docs/livekit/deploy/secrets
  content_hash: 2597f80347b016f50c8255672c0124f7d1247d79cc6f28c2d7748a831c1dda93
- url: https://developers.telnyx.com/docs/livekit/index
  content_hash: b7e94750be216371a58fbe786c152745786650511a3e1015876958da4f78795f
- url: https://developers.telnyx.com/docs/livekit/limits
  content_hash: c2c8b617e59a313d5d92d1069a3a157439ff9799db77da96d220376db2e576bd
- url: https://developers.telnyx.com/docs/livekit/migration/from-livekit-cloud
  content_hash: 5a955282223665b430dc7d6dff8e8fc84e1a3cf8ed86b2a2da44e5a5d2218058
- url: https://developers.telnyx.com/docs/livekit/migration/from-self-hosted
  content_hash: d9ed98fdfc4c4af8e83e472c11fb446e88d6bd636a8c5500d5516c10eb22b0ed
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
