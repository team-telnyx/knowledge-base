---
title: Compatibility
summary: Overview of how the LiveKit agent framework and related features behave on
  Telnyx compared to LiveKit Cloud, including what is identical, what differs, what
  is not yet supported, and what is on the roadmap.
sources:
- url: https://developers.telnyx.com/docs/livekit/compatibility
updated_at: 2026-08-05T13:47:31Z
---

# Compatibility

Overview of how the LiveKit agent framework and related features behave on Telnyx compared to LiveKit Cloud, including what is identical, what differs, what is not yet supported, and what is on the roadmap.

## What's the Same

The LiveKit agent framework is 100% portable — your agent code does not change. Everything in LiveKit works identically on Telnyx.

Notable sections from LiveKit docs:

- **Agent Framework** — [docs.livekit.io/agents](https://docs.livekit.io/agents)
- **SIP / Phone** — [docs.livekit.io/sip](https://docs.livekit.io/sip)
- **API Reference** — [docs.livekit.io/api](https://docs.livekit.io/api)
- **Cloud Deployment** — [docs.livekit.io/cloud](https://docs.livekit.io/cloud)
- **Egress / Ingress** — [docs.livekit.io/egress](https://docs.livekit.io/egress)

## What's Different

These features work differently on Telnyx compared to LiveKit Cloud:

- **STT / TTS / LLM** — LiveKit Cloud requires third-party AI providers. On Telnyx, hosted models are available out of the box via [`livekit-plugins-telnyx`](https://github.com/team-telnyx/telnyx-livekit-plugin). Prefer your own provider? Bring any API key.
- **SIP trunking** — On other platforms, you pay third-party SIP fees on top of your usage. On Telnyx, those are gone entirely — SIP is built-in because you're already on the carrier. BYOT is also supported if you prefer your existing provider.
- **HD Voice** — G.722 (16 kHz) and Opus (48 kHz) codecs for wideband audio on SIP calls. G.722 is enabled by default. Opus requires SRTP — see [Telephony](telephony.md) for setup.
- **Phone numbers** — Telnyx numbers in 140+ countries instead of LiveKit Phone (US only).
- **Agent deployment** — Same `lk agent deploy` command. Just swap the URL: `lk agent deploy . --url <region>.livekit.telnyx.com`

Available regions are `nyc1`, `sfo3`, `atl1`, and `syd1`. See the [Regions](regions.md) page for details.

## What's Not Supported

- **Ingress (RTMP/WHIP)** — importing external streams into a room.
- **Sandbox** — quick-start dev environments.

## Coming Soon

This roadmap is subject to change.

- **Egress** — Call recording, room recording, cloud storage export.
- **Observability** — Cloud Dashboard with session timeline (transcripts, traces, logs, audio playback).
- **Agent Tooling** — Playground, Agent Builder.
- **Security & Compliance** — E2E encryption, SSO, RBAC, HIPAA.
- **Enterprise SIP** — Call transfers (REFER/warm transfer), and advanced SIP features.
- **Media** — Enhanced noise cancellation (Krisp/BVC).
