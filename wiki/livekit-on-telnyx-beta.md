---
title: LiveKit on Telnyx (Beta)
summary: LiveKit on Telnyx is the same LiveKit you know, hosted on Telnyx’s global
  infrastructure with built‑in telephony and colocated AI models—so you can build,
  deploy, and scale voice AI agents with lower latency, simpler operations, and a
  single bill.
sources:
- url: https://developers.telnyx.com/docs/livekit
  content_hash: 186bda4a8a85344ae27999f5e96f92b5d53014b810f072b662b7e9cfcb8254a8
updated_at: 2026-05-08T13:08:15Z
---

# LiveKit on Telnyx (Beta)

LiveKit on Telnyx is the same LiveKit you know, hosted on Telnyx’s global infrastructure with built‑in telephony and colocated AI models—so you can build, deploy, and scale voice AI agents with lower latency, simpler operations, and a single bill.

## Key benefits

- Built-in telephony with no third-party SIP fees: Telnyx is the carrier, so you can buy numbers, configure SIP, and connect calls in one place. HD voice support (G.722 and Opus).
- Ultra-low latency AI on Telnyx GPUs: STT, TTS, and LLM inference run on Telnyx-owned GPUs colocated ~2 ms from your agents—no external API round-trips, faster responses, and more natural conversations.
- Same LiveKit, zero migration risk: Same SDKs, CLI, and agent framework. Swap a few environment variables and redeploy—your agent code stays the same.
- One platform, one bill: Compute, models, telephony, and numbers consolidated on your Telnyx invoice.

## Ideal users

- LiveKit Cloud users who want to consolidate vendors or cut latency via Telnyx’s network.
- Self-hosted LiveKit operators who want managed hosting without infrastructure overhead.
- New voice AI developers seeking a single platform for media, telephony, and AI.

## Workflow at a glance

1. Connect: Point your LiveKit client at Telnyx’s LiveKit cluster with your Telnyx credentials.
2. Build: Create agents using the LiveKit Agent framework and Telnyx plugins for STT, TTS, and LLM.
3. Deploy: Run agents on Telnyx’s managed infrastructure; telephony integrates via built-in SIP.
4. Scale: Telnyx manages infra and regions; you manage agents and configuration.

## How it compares to LiveKit Cloud

- SIP trunking: Built-in on Telnyx (no third-party SIP fees, HD voice) vs. external SIP costs on top of usage.
- AI models: Telnyx-hosted, colocated inference near agents vs. LiveKit Inference or third-party APIs.
- Billing: Combined with Telnyx services vs. separate bills.

## Try the plugin without migrating

Not ready to switch hosting? Install the Telnyx plugin on your existing LiveKit Cloud or self-hosted setup to get faster, colocated inference on Telnyx GPUs with the same agent code and infrastructure. See the installation step in Build and the Plugin Reference for available STT, TTS, and LLM options:

- Install the plugin: [Build → Install the plugin](https://developers.telnyx.com/docs/livekit/build#1-install-the-plugin)
- Plugin reference: [Models (STT, TTS, LLM)](https://developers.telnyx.com/docs/livekit/models)

## What to do next

- Get started in minutes: [Quickstart](https://developers.telnyx.com/docs/livekit/quickstart)
- Point your client at Telnyx: [Connect](https://developers.telnyx.com/docs/livekit/connect)
- Wire up PSTN and SIP: [Telephony](https://developers.telnyx.com/docs/livekit/telephony)
- Choose AI models: [Plugin Reference](https://developers.telnyx.com/docs/livekit/models)
