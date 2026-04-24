---
title: Telephony
summary: Connect phone numbers to your LiveKit agents on Telnyx.
sources:
  - url: https://developers.telnyx.com/docs/livekit/telephony
    content_hash: c56c5d3e9279c3e7a1a1f97cc6e5dee9fac7cd441d337ccc45b3faa0c62947df
updated_at: 2026-04-10T00:00:00Z
---

# Telephony

Connect phone numbers to your LiveKit agents on Telnyx.

Telnyx is the carrier. Buy a number, connect it to your agent — no third-party SIP trunk setup, no FQDN auth dance. Calls route on-net from Telnyx SIP directly to your agent.

For setup steps, see the [Quick Start](../tutorial/quick-start.md).

## Supported

### Inbound calls

Inbound calls are routed to your agent via SIP dispatch rules. When someone calls your DID, Telnyx forwards it to the LiveKit SIP service, which dispatches it to your agent based on the rules you configure.

### Outbound calls

Use the `lk` CLI to place an outbound call into a room:

```bash theme={null}
lk sip participant create \
  --room "my-room" \
  --trunk "" \
  --call "+15551234567" \
  --identity "outbound-caller"
```

### DTMF

DTMF tones are supported via RFC 2833/4733. Tones are forwarded to your agent as events and can be handled in code.

### SIP headers

Pass call metadata through to your agent using `headers_to_attributes`. Header values are mapped to LiveKit participant attributes, available in your agent at runtime.

### HD voice (G.722)

Telnyx supports HD voice using the G.722 codec for higher-quality audio on SIP calls. This is enabled by default on Telnyx SIP connections.

## Not yet supported

These features require [Enterprise SIP](compatibility.md#coming-soon), which is on the roadmap.

* **Call transfers (REFER / warm transfer)**
