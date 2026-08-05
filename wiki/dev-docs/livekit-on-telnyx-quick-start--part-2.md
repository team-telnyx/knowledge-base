---
title: LiveKit on Telnyx Quick Start
summary: A step-by-step guide to deploying a working LiveKit voice agent on Telnyx
  infrastructure that can be called from a real phone number, covering CLI configuration,
  telephony setup, agent deployment, and testing.
sources:
- url: https://developers.telnyx.com/docs/livekit/quickstart
updated_at: 2026-08-05T13:48:00Z
---

# LiveKit on Telnyx Quick Start

*Part 2 of 2 — see also: [Part 1](livekit-on-telnyx-quick-start--part-1.md)*

A step-by-step guide to deploying a working LiveKit voice agent on Telnyx infrastructure that can be called from a real phone number, covering CLI configuration, telephony setup, agent deployment, and testing.

## Step 5: Call your agent

Pick up your phone and dial the number you purchased. You should hear:

> "Thanks for calling Bella's Kitchen!"

Try ordering some pasta. The agent handles the full conversation — browsing the menu, answering questions, and taking your order.

### Troubleshooting

- **Call doesn't connect** — Verify your SIP connection is pointed at the correct regional FQDN and your DID is assigned to it.
- **Agent doesn't pick up** — Run `lk agent status` to confirm the agent is running. Check logs with `lk agent logs`.
- **Audio quality issues** — Make sure you're using the region closest to you.

## Next steps

You've deployed your first agent. Here's where to go from here:

- [Build](build.md) — Write your own agent from scratch
- [Deploy](deploy.md) — Regions, scaling, secrets, and production deployment
- [Models](models.md) — STT, TTS, and LLM options available on Telnyx
- [Telephony](telephony.md) — Inbound/outbound calls, dispatch rules, multiple numbers
- [Compatibility](compatibility.md) — What's the same and different from LiveKit Cloud
