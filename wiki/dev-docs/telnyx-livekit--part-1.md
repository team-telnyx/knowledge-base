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

*Part 1 of 3 — see also: [Part 2](telnyx-livekit--part-2.md), [Part 3](telnyx-livekit--part-3.md)*

Telnyx LiveKit is a managed platform for building, deploying, and scaling voice AI agents on Telnyx infrastructure. It combines the LiveKit agent framework with built-in SIP trunking, colocated GPU inference for STT/TTS/LLM, and automatic autoscaling — collapsing the voice AI stack into a single platform with one bill.

## Overview

LiveKit on Telnyx collapses your voice AI stack into a single platform:

- **Built-in telephony, no third-party SIP fees** — Telnyx is the carrier. Buy numbers, configure SIP, and connect to agents all in one portal. On other platforms, you pay third-party SIP fees on top of usage; on Telnyx, those are gone entirely.
- **Ultra-low latency AI on Telnyx GPUs** — STT, TTS, and LLM run on Telnyx-owned GPUs, colocated in every region ~2 ms from your agents. No round-trips to external APIs on the hot path.
- **Same LiveKit, zero migration risk** — Same SDKs, same CLI, same agent framework. Swap three environment variables and redeploy — your code doesn't change.
- **One platform, one bill** — Compute, models, telephony, and phone numbers on a single Telnyx invoice.

If you're not ready to migrate, you can install the Telnyx plugin on your existing LiveKit Cloud or self-hosted setup to get faster, colocated inference on Telnyx GPUs.

**Who is this for?**

- LiveKit Cloud users looking to consolidate vendors or reduce latency
- Self-hosted LiveKit operators who want managed hosting
- New voice AI developers who want a single platform for media, telephony, and AI

## Architecture

### Agents

Each agent you deploy is an isolated worker. Deploy as many as you need — a restaurant bot, a support agent, a scheduling assistant — each running independently under your account.

```
lk agent deploy .   →   isolated worker, autoscaled, managed containers
```

Agents are deployed per-account with full namespace isolation. Your rooms, SIP trunks, and dispatch rules are scoped to your API key and never visible to other tenants.

### Autoscaling

The platform watches active room load and scales your agent workers up and down automatically. You don't configure `load_fnc` or `load_threshold` — the platform manages this.

- **Scale up** — new workers spin up as concurrent calls increase
- **Scale down** — idle workers are drained and removed
- **Health checks** — unhealthy containers are replaced automatically with rolling deploys

### Inbound call flow

```
Caller → PSTN → Telnyx SIP → LiveKit SIP Bridge → Room → Agent Worker
```

Because Telnyx is both the carrier and the platform, the SIP leg is on-net — no external SIP trunk hop, no PSTN egress to a third party. The call lands directly in a LiveKit room where your agent is waiting.

### AI inference

STT, TTS, and LLM inference runs on Telnyx GPUs colocated with the agent runtime — approximately 2 ms from your agent. No round-trips to external APIs on the hot path.

```
Agent ──2ms──▶ Telnyx STT / TTS / LLM
```

You can also bring your own provider keys (OpenAI, Anthropic, etc.) — those route externally.

### Regions

Each region is a full stack: SFU, SIP, agent runtime, and AI inference. Available regions are `nyc1`, `sfo3`, `atl1`, and `syd1`. See [Telnyx LiveKit Regions](telnyx-livekit-regions.md) for available platform and SIP endpoints.

## Compatibility

### What's the same

The LiveKit agent framework is 100% portable — your agent code does not change. Everything in LiveKit works identically on Telnyx. Notable sections from the LiveKit docs:

- **Agent Framework** — [docs.livekit.io/agents](https://docs.livekit.io/agents)
- **SIP / Phone** — [docs.livekit.io/sip](https://docs.livekit.io/sip)
- **API Reference** — [docs.livekit.io/api](https://docs.livekit.io/api)
- **Cloud Deployment** — [docs.livekit.io/cloud](https://docs.livekit.io/cloud)
- **Egress / Ingress** — [docs.livekit.io/egress](https://docs.livekit.io/egress)

### What's different

| Feature | LiveKit on Telnyx | LiveKit Cloud |
|---|---|---|
| SIP trunking | Built-in — no third-party SIP fees, HD voice (G.722 + Opus) | Third-party SIP fees on top of usage |
| AI models | Colocated on Telnyx GPUs (~2 ms from agents) via `livekit-plugins-telnyx` | LiveKit Inference or third-party APIs |
| Phone numbers | Telnyx numbers in 140+ countries | LiveKit Phone (US only) |
| Agent deployment | Same `lk agent deploy` command, just swap the URL: `lk agent deploy . --url <region>.livekit.telnyx.com` | Standard LiveKit Cloud deployment |
| Billing | Combined with Telnyx services | Separate |

HD Voice supports G.722 (16 kHz) and Opus (48 kHz) codecs for wideband audio on SIP calls. G.722 is enabled by default. Opus requires SRTP — see [Telnyx LiveKit Telephony](telnyx-livekit-telephony.md) for setup.

### What's not supported

- **Ingress (RTMP/WHIP)** — importing external streams into a room
- **Sandbox** — quick-start dev environments

### Coming soon

*This roadmap is subject to change.*

- **Egress** — call recording, room recording, cloud storage export
- **Observability** — cloud dashboard with session timeline (transcripts, traces, logs, audio playback)
- **Agent Tooling** — playground, agent builder
- **Security & Compliance** — E2E encryption, SSO, RBAC, HIPAA
- **Enterprise SIP** — call transfers (REFER/warm transfer), and advanced SIP features
- **Media** — enhanced noise cancellation (Krisp/BVC)

## Connecting and SDK Configuration

Connecting to the Telnyx LiveKit platform is a URL and credential swap — no code changes. Make sure `LIVEKIT_URL`, `LIVEKIT_API_KEY`, and `LIVEKIT_API_SECRET` are exported in your shell, then verify:

```
lk room list
```

Server SDKs (Python, Go, Node.js) just need the URL and credentials:

```python
from livekit.api import LiveKitAPI

api = LiveKitAPI(
    url="https://nyc1.livekit-telnyx.com",
    api_key="<your-telnyx-api-key>",
    api_secret="<your-livekit-api-secret>",
)
```

If you're migrating from LiveKit Cloud or self-hosted, change the three environment variables and everything else stays the same.
