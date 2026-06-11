---
title: Telnyx LiveKit Architecture
summary: Telnyx LiveKit is a managed platform for deploying voice AI agents at scale—you
  ship agent code while Telnyx manages containers, autoscaling, SIP connectivity,
  and GPU-accelerated AI inference that’s colocated with your agent runtime in each
  region.
sources:
- url: https://developers.telnyx.com/docs/livekit/architecture
  content_hash: 8d61c59788b7bc7cae2381344aea167974a79a3bded1b48abba94a0e7f7b63e5
updated_at: 2026-05-08T13:15:36Z
---

# Telnyx LiveKit Architecture

Telnyx LiveKit is a managed platform for deploying voice AI agents at scale—you ship agent code while Telnyx manages containers, autoscaling, SIP connectivity, and GPU-accelerated AI inference that’s colocated with your agent runtime in each region.

## Platform overview
Telnyx LiveKit provides a full-stack, regionalized runtime for real-time voice AI. The platform manages container orchestration, SIP ingress, selective forwarding (SFU), and on-net access to AI services (STT, TTS, LLM) close to your agents, minimizing latency and operational overhead.

## Agents
Each deployed agent is an isolated worker that runs independently under your account. You can deploy multiple agents (for example, a restaurant bot, support agent, or scheduling assistant) and the platform will manage them as separate workers. A typical deploy looks like: `lk agent deploy .` resulting in a managed, autoscaled container per agent.

## Tenancy and isolation
Agents are deployed per account with full namespace isolation. Your rooms, SIP trunks, and dispatch rules are scoped to your API key and are never visible to other tenants.

## Autoscaling
The platform automatically monitors active room load and scales your agent workers without requiring custom load functions or thresholds.
- Scale up: New workers spin up as concurrent calls increase.
- Scale down: Idle workers are drained and removed.
- Health checks: Unhealthy containers are replaced automatically using rolling deploys.

## Inbound call flow
Caller → PSTN → Telnyx SIP → LiveKit SIP Bridge → Room → Agent Worker

Because Telnyx is both the carrier and the application platform, the SIP leg stays on-net—there’s no external SIP hop or PSTN egress to a third party. Calls land directly in a LiveKit room where your agent is available.

## AI inference
Speech-to-text (STT), text-to-speech (TTS), and LLM inference run on Telnyx GPUs that are colocated with the agent runtime, with approximately ~2 ms latency from your agent to the inference services. You may also bring your own provider keys (e.g., OpenAI, Anthropic); those requests route externally instead of remaining on-net.

## Regions
Each region includes the full stack: SFU, SIP, agent runtime, and AI inference. See the list of available endpoints on the Regions page: [Regions](https://developers.telnyx.com/docs/livekit/regions).
