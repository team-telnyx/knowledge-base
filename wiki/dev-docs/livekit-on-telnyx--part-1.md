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

*Part 1 of 6 — see also: [Part 2](livekit-on-telnyx--part-2.md), [Part 3](livekit-on-telnyx--part-3.md), [Part 4](livekit-on-telnyx--part-4.md), [Part 5](livekit-on-telnyx--part-5.md), [Part 6](livekit-on-telnyx--part-6.md)*

Telnyx LiveKit is a managed platform for deploying voice AI agents at scale, combining LiveKit's agent framework with built-in telephony, colocated AI inference on Telnyx GPUs, and managed infrastructure across multiple regions. This page covers architecture, compatibility, regions, quickstart, build, deploy, models (STT/TTS/LLM), telephony, observability, limits, pricing, and migration from LiveKit Cloud or self-hosted.

## Overview

Telnyx LiveKit is a managed platform for deploying voice AI agents at scale. You ship agent code; the platform handles containers, scaling, SIP, and AI inference — colocated in each region. It collapses the voice AI stack into a single platform: built-in telephony with no third-party SIP fees, ultra-low latency AI on Telnyx GPUs, the same LiveKit SDKs and CLI, and a single Telnyx invoice for compute, models, telephony, and phone numbers.

The platform is aimed at LiveKit Cloud users looking to consolidate vendors or reduce latency, self-hosted LiveKit operators wanting managed hosting, and new voice AI developers who want a single platform for media, telephony, and AI.

## Architecture

Each agent you deploy is an isolated worker. Deploy as many as you need — a restaurant bot, a support agent, a scheduling assistant — each running independently under your account. Agents are deployed per-account with full namespace isolation; rooms, SIP trunks, and dispatch rules are scoped to your API key and never visible to other tenants.

The platform watches active room load and scales agent workers up and down automatically. You don't configure `load_fnc` or `load_threshold` — the platform manages this:

- **Scale up** — new workers spin up as concurrent calls increase
- **Scale down** — idle workers are drained and removed
- **Health checks** — unhealthy containers are replaced automatically with rolling deploys

The inbound call flow is on-net because Telnyx is both the carrier and the platform:

```
Caller → PSTN → Telnyx SIP → LiveKit SIP Bridge → Room → Agent Worker
```

STT, TTS, and LLM inference runs on Telnyx GPUs colocated with the agent runtime — approximately 2ms from your agent. No round-trips to external APIs on the hot path. You can also bring your own provider keys (OpenAI, Anthropic, etc.) — those route externally.

Each region is a full stack: SFU, SIP, agent runtime, and AI inference. See [Regions](regions.md) for available endpoints.

## Compatibility

The LiveKit agent framework is 100% portable — your agent code does not change. Everything in LiveKit works identically on Telnyx. Notable LiveKit docs sections that apply unchanged:

- **Agent Framework** — [docs.livekit.io/agents](https://docs.livekit.io/agents)
- **SIP / Phone** — [docs.livekit.io/sip](https://docs.livekit.io/sip)
- **API Reference** — [docs.livekit.io/api](https://docs.livekit.io/api)
- **Cloud Deployment** — [docs.livekit.io/cloud](https://docs.livekit.io/cloud)
- **Egress / Ingress** — [docs.livekit.io/egress](https://docs.livekit.io/egress)

Features that work differently on Telnyx compared to LiveKit Cloud:

- **STT / TTS / LLM** — LiveKit Cloud requires third-party AI providers. On Telnyx, hosted models are available out of the box via [`livekit-plugins-telnyx`](https://github.com/team-telnyx/telnyx-livekit-plugin). Prefer your own provider? Bring any API key.
- **SIP trunking** — On other platforms, you pay third-party SIP fees on top of your usage. On Telnyx, those are gone entirely — SIP is built-in because you're already on the carrier. BYOT also supported if you prefer your existing provider.
- **HD Voice** — G.722 (16 kHz) and Opus (48 kHz) codecs for wideband audio on SIP calls. G.722 is enabled by default. Opus requires SRTP — see [Telephony](telephony.md) for setup.
- **Phone numbers** — Telnyx numbers in 140+ countries instead of LiveKit Phone (US only)
- **Agent deployment** — Same `lk agent deploy` command. Just swap the URL: `lk agent deploy . --url <region>.livekit.telnyx.com`

Not supported:

- **Ingress (RTMP/WHIP)** — importing external streams into a room
- **Sandbox** — quick-start dev environments

Coming soon (roadmap subject to change):

- **Egress** — Call recording, room recording, cloud storage export
- **Observability** — Cloud Dashboard with session timeline (transcripts, traces, logs, audio playback)
- **Agent Tooling** — Playground, Agent Builder
- **Security & Compliance** — E2E encryption, SSO, RBAC, HIPAA
- **Enterprise SIP** — Call transfers (REFER/warm transfer), and advanced SIP features
- **Media** — Enhanced noise cancellation (Krisp/BVC)

## Regions

Each region is a full stack: SFU, SIP, agent runtime, and AI inference. Choose the region closest to your users for the lowest latency.

Platform endpoints:

| Region | Endpoint |
| --- | --- |
| New York | `https://nyc1.livekit-telnyx.com` |
| San Francisco | `https://sfo3.livekit-telnyx.com` |
| Atlanta | `https://atl1.livekit-telnyx.com` |
| Sydney | `https://syd1.livekit-telnyx.com` |

SIP endpoints:

| Region | SIP Endpoint |
| --- | --- |
| New York | `nyc1.sip.livekit-telnyx.com` |
| San Francisco | `sfo3.sip.livekit-telnyx.com` |
| Atlanta | `atl1.sip.livekit-telnyx.com` |
| Sydney | `syd1.sip.livekit-telnyx.com` |
