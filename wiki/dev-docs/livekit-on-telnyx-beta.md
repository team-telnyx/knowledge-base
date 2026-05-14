---
title: LiveKit on Telnyx (Beta)
summary: Run the same LiveKit you know on Telnyx’s global infrastructure with integrated
  telephony and colocated AI (STT, TTS, LLM) for ultra-low-latency voice agents—all
  on one platform and one bill.
sources:
- url: https://developers.telnyx.com/docs/livekit
  content_hash: 186bda4a8a85344ae27999f5e96f92b5d53014b810f072b662b7e9cfcb8254a8
updated_at: 2026-05-14T09:48:09Z
---

# LiveKit on Telnyx (Beta)

Run the same LiveKit you know on Telnyx’s global infrastructure with integrated telephony and colocated AI (STT, TTS, LLM) for ultra-low-latency voice agents—all on one platform and one bill.

## Key benefits
- Built-in telephony with no third‑party SIP fees: Buy numbers, configure SIP, and connect calls directly in Telnyx.
- Ultra‑low‑latency AI on Telnyx GPUs: STT, TTS, and LLM inference runs ~2ms from your agents in every region—no external API round trips.
- Same LiveKit, minimal migration: Keep the same SDKs, CLI, and agent framework. Swap a few environment variables and redeploy.
- One platform, one bill: Compute, models, telephony, and phone numbers consolidated on your Telnyx invoice.

## Who should use it
- LiveKit Cloud users seeking to consolidate vendors or reduce latency on Telnyx’s network.
- Self‑hosted LiveKit operators who want managed hosting without the infra burden.
- New voice AI builders who want media, telephony, and AI in a single platform.

## How LiveKit on Telnyx works
1. Connect: Point your LiveKit client to Telnyx’s LiveKit cluster using Telnyx credentials. See [Connect](connect.md).
2. Build: Create agents with the LiveKit Agent framework and Telnyx plugins for STT, TTS, and LLM. See [Build](build.md) and [Plugin Reference](plugin-reference.md).
3. Deploy: Run agents on Telnyx’s managed infrastructure; telephony integrates via built‑in SIP. See [Deploy](deploy.md).
4. Scale: Telnyx manages infrastructure; you manage agents and configuration.

## Migration and plugin options
- Not ready to move fully? Install the Telnyx plugin in your existing LiveKit Cloud or self‑hosted deployment for faster, colocated inference on Telnyx GPUs—no agent code changes. See [Plugin Reference](plugin-reference.md), [STT](stt.md), [TTS](tts.md), and [LLM](llm.md).
- Full migration guides: [From LiveKit Cloud](from-livekit-cloud.md) and [From Self-Hosted](from-self-hosted.md).

## What’s different from LiveKit Cloud
- SIP trunking
  - LiveKit on Telnyx: Built‑in, no third‑party SIP fees; HD voice (G.722 + Opus).
  - LiveKit Cloud: Requires third‑party SIP, adding fees on top of usage.
- AI models
  - LiveKit on Telnyx: STT/TTS/LLM colocated on Telnyx GPUs (~2ms from agents).
  - LiveKit Cloud: LiveKit Inference or third‑party APIs.
- Billing
  - LiveKit on Telnyx: Combined with Telnyx services.
  - LiveKit Cloud: Separate billing.

## Next steps and related docs
- Get started fast: [Quickstart](quickstart.md)
- Configure connectivity: [Connect](connect.md)
- Integrate telephony: [Telephony](telephony.md)
- Choose models and plugins: [Plugin Reference](plugin-reference.md) (see [STT](stt.md), [TTS](tts.md), [LLM](llm.md))
- Plan and operate: [Compatibility](compatibility.md), [Architecture](architecture.md), [Regions](regions.md), [Limits](limits.md), [Pricing](pricing.md), [Observability](observability.md), [Configuration](configuration.md), [Secrets](secrets.md), [Management & Access](management-access.md)

## Documentation index
For a full list of available documentation pages, fetch the index at: https://developers.telnyx.com/llms.txt
