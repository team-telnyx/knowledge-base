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
