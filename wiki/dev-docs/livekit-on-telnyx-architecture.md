---
title: LiveKit on Telnyx architecture
summary: Telnyx LiveKit is a managed platform for deploying voice AI agents at scale,
  handling containers, scaling, SIP, and AI inference colocated in each region. This
  page describes the platform's architecture, including agents, autoscaling, inbound
  call flow, AI inference, and regional deployment.
sources:
- url: https://developers.telnyx.com/docs/livekit/architecture
updated_at: 2026-08-05T13:47:27Z
---

# LiveKit on Telnyx architecture

Telnyx LiveKit is a managed platform for deploying voice AI agents at scale, handling containers, scaling, SIP, and AI inference colocated in each region. This page describes the platform's architecture, including agents, autoscaling, inbound call flow, AI inference, and regional deployment.

## Agents

Each agent you deploy is an isolated worker. Deploy as many as you need — a restaurant bot, a support agent, a scheduling assistant — each running independently under your account.

```
lk agent deploy .   →   isolated worker, autoscaled, managed containers
```

Agents are deployed per-account with full namespace isolation. Your rooms, SIP trunks, and dispatch rules are scoped to your API key and never visible to other tenants.

## Autoscaling

The platform watches active room load and scales your agent workers up and down automatically. You don't configure `load_fnc` or `load_threshold` — the platform manages this.

- **Scale up** — new workers spin up as concurrent calls increase
- **Scale down** — idle workers are drained and removed
- **Health checks** — unhealthy containers are replaced automatically with rolling deploys

## Inbound call flow

```
Caller → PSTN → Telnyx SIP → LiveKit SIP Bridge → Room → Agent Worker
```

Because Telnyx is both the carrier and the platform, the SIP leg is on-net — no external SIP trunk hop, no PSTN egress to a third party. The call lands directly in a LiveKit room where your agent is waiting.

## AI inference

STT, TTS, and LLM inference runs on Telnyx GPUs colocated with the agent runtime — approximately 2ms from your agent. No round-trips to external APIs on the hot path.

```
Agent ──2ms──▶ Telnyx STT / TTS / LLM
```

You can also bring your own provider keys (OpenAI, Anthropic, etc.) — those route externally.

## Regions

Each region is a full stack: SFU, SIP, agent runtime, and AI inference. See [Regions](regions.md) for available endpoints.
