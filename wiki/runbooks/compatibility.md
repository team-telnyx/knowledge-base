---
title: Compatibility
summary: What works, what's different, and what's not available when using LiveKit on Telnyx vs LiveKit Cloud or self-hosted.
sources:
  - url: https://developers.telnyx.com/docs/livekit/compatibility
    content_hash: 758198449e3cdfb7330b292e1b3c9ada2959573eba69e6ddd3bf59c191010fb8
updated_at: 2026-04-10T00:00:00Z
---

# Compatibility

What works, what's different, and what's not available when using LiveKit on Telnyx vs LiveKit Cloud or self-hosted.

## What's the Same

The LiveKit agent framework is 100% portable — your agent code does not change. Everything in LiveKit works identically on Telnyx.

Notable sections from LiveKit docs:

* **Agent Framework** — [docs.livekit.io/agents](https://docs.livekit.io/agents)
* **SIP / Phone** — [docs.livekit.io/sip](https://docs.livekit.io/sip)
* **API Reference** — [docs.livekit.io/api](https://docs.livekit.io/api)
* **Cloud Deployment** — [docs.livekit.io/cloud](https://docs.livekit.io/cloud)
* **Egress / Ingress** — [docs.livekit.io/egress](https://docs.livekit.io/egress)

## What's Different

These features work differently on Telnyx compared to LiveKit Cloud:

* **STT / TTS / LLM** — LiveKit Cloud requires third-party AI providers. On Telnyx, hosted models are available out of the box via [`livekit-plugins-telnyx`](https://github.com/team-telnyx/telnyx-livekit-plugin). Prefer your own provider? Bring any API key.
* **SIP trunking** — On other platforms, you pay third-party SIP fees on top of your usage. On Telnyx, those are gone entirely — SIP is built-in because you're already on the carrier. BYOT also supported if you prefer your existing provider.
* **Phone numbers** — Telnyx numbers in 140+ countries instead of LiveKit Phone (US only)
* **Agent deployment** — Same `lk agent deploy` command. Just swap the URL: `lk agent deploy . --url <region>.livekit.telnyx.com`

*Note: Available regions are nyc1, sfo3, atl1, and syd1. See the [Regions](regions.md) page for details.*

## What's Not Supported

* **Ingress (RTMP/WHIP)** — importing external streams into a room
* **Sandbox** — quick-start dev environments

## Coming Soon

*This roadmap is subject to change.*

* **Egress** — Call recording, room recording, cloud storage export
* **Observability** — Cloud Dashboard with session timeline (transcripts, traces, logs, audio playback)
* **Agent Tooling** — Playground, Agent Builder
* **Security & Compliance** — E2E encryption, SSO, RBAC, HIPAA
* **Enterprise SIP** — Call transfers (REFER/warm transfer), and advanced SIP features
* **Media** — Enhanced noise cancellation (Krisp/BVC)


## Related Pages

- [Compatibility Matrix](../runbooks/compatibility-matrix.md)
- [Compatibility with AWS S3](../runbooks/compatibility-with-aws-s3.md)
- [TeXML and TwiML Compatibility](../runbooks/texml-and-twiml-compatibility.md)
