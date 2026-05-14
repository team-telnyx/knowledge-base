---
title: LiveKit Architecture
summary: Telnyx LiveKit is a managed, regionalized platform for deploying voice AI
  agents at scale. You ship agent code, while Telnyx handles container orchestration,
  autoscaling, on‑net SIP call delivery, and colocated STT/TTS/LLM inference within
  each region.
sources:
- url: https://developers.telnyx.com/docs/livekit/architecture
updated_at: 2026-05-14T09:53:24Z
---

# LiveKit Architecture

Telnyx LiveKit is a managed, regionalized platform for deploying voice AI agents at scale. You ship agent code, while Telnyx handles container orchestration, autoscaling, on‑net SIP call delivery, and colocated STT/TTS/LLM inference within each region.

## Platform overview
LiveKit on Telnyx (Beta) provides a fully managed runtime for real‑time voice AI. The platform runs your agent containers, connects calls over Telnyx’s own SIP network, and executes speech and language inference on GPUs located in the same region as your agents to minimize latency.

## Agents and isolation
- Each agent is an isolated worker you deploy and scale independently (for example, a restaurant bot, a support agent, or a scheduling assistant).
- Deploy with your tooling and the Telnyx CLI (for example, `lk agent deploy .`).
- Strong multi‑tenant isolation: rooms, SIP trunks, and dispatch rules are scoped to your account/API key and are never visible to other tenants.

## Autoscaling and reliability
- The platform automatically scales workers up and down based on active room load; you do not configure `load_fnc` or `load_threshold`.
- Scale up as concurrent calls increase; scale down by draining idle workers.
- Built‑in health checks; unhealthy containers are replaced with rolling deploys for continuity.

## Inbound call flow
Caller → PSTN → Telnyx SIP → LiveKit SIP Bridge → Room → Agent Worker

Because Telnyx is both the carrier and the platform, the SIP leg is on‑net. There’s no external SIP trunk hop or PSTN egress to a third party, so calls land directly in a LiveKit room where your agent is waiting.

## AI inference architecture
- STT, TTS, and LLM inference run on Telnyx GPUs colocated with the agent runtime, with approximately 2 ms network distance from your agent.
- No round‑trips to external APIs are required on the hot path.
- You can bring your own model provider keys (for example, OpenAI or Anthropic); those requests route externally when used.

## Regional topology
Each region is a complete stack: SFU, SIP, agent runtime, and AI inference. See [LiveKit Regions](livekit-regions.md) for available regional endpoints and deployment guidance.

## Related pages
- [LiveKit Quick Start](livekit-quick-start.md)
- [LiveKit Deploy](livekit-deploy.md)
- [LiveKit Telephony](livekit-telephony.md)
- [LiveKit Observability](livekit-observability.md)
- [LiveKit Regions](livekit-regions.md)
- [LiveKit Limits](livekit-limits.md)
- [LiveKit Pricing](livekit-pricing.md)
