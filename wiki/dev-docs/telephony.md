---
title: Telephony
summary: Telnyx acts as the carrier for LiveKit voice agents, routing calls on-net
  from Telnyx SIP directly to your agent without third-party SIP trunk setup. This
  page covers supported telephony features (inbound, outbound, DTMF, SIP headers,
  HD voice) and current limitations.
sources:
- url: https://developers.telnyx.com/docs/livekit/telephony
updated_at: 2026-08-05T13:47:46Z
---

# Telephony

Telnyx acts as the carrier for LiveKit voice agents, routing calls on-net from Telnyx SIP directly to your agent without third-party SIP trunk setup. This page covers supported telephony features (inbound, outbound, DTMF, SIP headers, HD voice) and current limitations.

## Overview

Telnyx is the carrier. Buy a number, connect it to your agent — no third-party SIP trunk setup, no FQDN auth dance. Calls route on-net from Telnyx SIP directly to your agent. For setup steps, see the [Quick Start](quick-start.md).

## Supported

### Inbound calls

Inbound calls are routed to your agent via SIP dispatch rules. When someone calls your DID, Telnyx forwards it to the LiveKit SIP service, which dispatches it to your agent based on the rules you configure.

### Outbound calls

Use the `lk` CLI to place an outbound call into a room:

```
lk sip participant create \
  --room "my-room" \
  --trunk "<SIP_TRUNK_ID>" \
  --call "+15551234567" \
  --identity "outbound-caller"
```

### DTMF

DTMF tones are supported via RFC 2833/4733. Tones are forwarded to your agent as events and can be handled in code.

### SIP headers

Pass call metadata through to your agent using `headers_to_attributes`. Header values are mapped to LiveKit participant attributes, available in your agent at runtime.

### HD voice

Telnyx supports two HD voice codecs for higher-quality audio on SIP calls:

- **G.722** — Wideband audio at 16 kHz sample rate. Enabled by default on all Telnyx SIP connections. No additional configuration needed.
- **Opus** — Wideband audio at 48 kHz sample rate. Requires SRTP encryption on both sides — enable OPUS in your Telnyx SIP connection's inbound codec list and set `media_encryption: ALLOW` on your LiveKit inbound trunk. Delivers the highest audio quality for voice AI agents.

Both codecs are negotiated automatically during SIP call setup. If the remote side supports Opus, it will be preferred over G.722.

## Not yet supported

These features require [Enterprise SIP](compatibility.md), which is on the roadmap.

- **Call transfers (REFER / warm transfer)**
