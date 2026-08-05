---
title: LiveKit on Telnyx
summary: LiveKit on Telnyx is a managed hosting offering that lets developers build,
  deploy, and scale voice AI agents on Telnyx's global network, combining telephony,
  AI inference, and LiveKit's agent framework on a single platform with consolidated
  billing.
sources:
- url: https://developers.telnyx.com/docs/livekit
updated_at: 2026-08-05T13:47:30Z
---

# LiveKit on Telnyx

LiveKit on Telnyx is a managed hosting offering that lets developers build, deploy, and scale voice AI agents on Telnyx's global network, combining telephony, AI inference, and LiveKit's agent framework on a single platform with consolidated billing.

## Overview

LiveKit on Telnyx is a managed deployment of the LiveKit real-time media stack hosted on Telnyx infrastructure. It is designed for building, deploying, and scaling voice AI agents, and it integrates telephony, AI models, and LiveKit's agent framework into a single platform. Developers use the same LiveKit SDKs, CLI, and agent framework they already know, with Telnyx providing the underlying compute, GPU-accelerated inference, and SIP connectivity.

## Why LiveKit on Telnyx

LiveKit on Telnyx collapses the voice AI stack into a single platform with several distinguishing benefits:

- **Built-in Telephony, No Third-Party SIP Fees** — Telnyx is the carrier, so phone numbers, SIP configuration, and agent connectivity are all managed in one portal. There are no third-party SIP fees layered on top of usage.
- **Ultra-Low Latency AI on Telnyx GPUs** — STT, TTS, and LLM inference runs on Telnyx-owned GPUs colocated in every region, approximately 2ms from agents. This eliminates round-trips to external APIs and produces faster, more natural conversations.
- **Same LiveKit, Zero Migration Risk** — The SDKs, CLI, and agent framework are unchanged. Migrating requires swapping three environment variables and redeploying; existing agent code does not need to change.
- **One Platform, One Bill** — Compute, models, telephony, and phone numbers are billed together on a single Telnyx invoice, removing vendor sprawl.

## Not Ready to Migrate

Developers who are not ready to migrate can install the [Build](build.md) plugin on an existing LiveKit Cloud or self-hosted deployment. The same agent code and infrastructure continue to work, with the benefit of faster, colocated inference on Telnyx GPUs. See the [Plugin Reference](plugin-reference.md) for the available STT, TTS, and LLM options.

## Who It Is For

LiveKit on Telnyx is aimed at three primary audiences:

- **LiveKit Cloud users** who want to consolidate vendors or reduce latency by leveraging Telnyx's network.
- **Self-hosted LiveKit operators** who want to offload infrastructure management to a managed hosting provider.
- **New voice AI developers** who want a single platform that covers media, telephony, and AI.

## How It Works

The end-to-end workflow for using LiveKit on Telnyx follows four steps:

1. **Connect** — Configure the LiveKit client to point to Telnyx's LiveKit cluster using Telnyx credentials.
2. **Build** — Write agents using the LiveKit Agent framework together with Telnyx plugins for STT, TTS, and LLM.
3. **Deploy** — Deploy agents to Telnyx's managed infrastructure. Telephony connects via built-in SIP.
4. **Scale** — Telnyx handles the infrastructure while the developer manages agents and configuration.

## Comparison With LiveKit Cloud

| Feature | LiveKit on Telnyx | LiveKit Cloud |
| --- | --- | --- |
| SIP trunking | Built-in — no third-party SIP fees, HD voice (G.722 + Opus) | Third-party SIP fees on top of usage |
| AI models | Colocated on Telnyx GPUs (~2ms from agents) | LiveKit Inference or third-party APIs |
| Billing | Combined with Telnyx services | Separate |

## Next Steps

- [Quickstart](quickstart.md) — Get deployed in 5 minutes.
- [Connect](connect.md) — Configure the LiveKit client.
- [Telephony](telephony.md) — SIP and PSTN integration.
- [Plugin Reference](plugin-reference.md) — STT, TTS, and LLM options.
