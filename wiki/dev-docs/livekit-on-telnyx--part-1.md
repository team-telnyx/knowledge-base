---
title: LiveKit on Telnyx
summary: LiveKit on Telnyx is a platform for deploying real-time voice AI agents with
  integrated telephony, AI models (STT, TTS, LLM), and observability — all billed
  on a single Telnyx invoice with no third-party SIP fees.
sources:
- url: https://developers.telnyx.com/docs/livekit/models/index
- url: https://developers.telnyx.com/docs/livekit/models/llm
- url: https://developers.telnyx.com/docs/livekit/models/stt
- url: https://developers.telnyx.com/docs/livekit/models/tts
- url: https://developers.telnyx.com/docs/livekit/observability/index
- url: https://developers.telnyx.com/docs/livekit/pricing
- url: https://developers.telnyx.com/docs/livekit/quickstart
- url: https://developers.telnyx.com/docs/livekit/regions
- url: https://developers.telnyx.com/docs/livekit/telephony
updated_at: 2026-06-11T10:34:33Z
---

# LiveKit on Telnyx

*Part 1 of 2 — see also: [Part 2](livekit-on-telnyx--part-2.md)*

LiveKit on Telnyx is a platform for deploying real-time voice AI agents with integrated telephony, AI models (STT, TTS, LLM), and observability — all billed on a single Telnyx invoice with no third-party SIP fees.

## Quickstart

Go from zero to a working voice agent you can call from your phone. You'll need a [Telnyx account](https://portal.telnyx.com), a Telnyx API key, a secret key you create (your `LIVEKIT_API_SECRET`), Python ≥ 3.10, and the [LiveKit CLI](https://docs.livekit.io/home/cli/) (`lk`) version 2.16.0 or later.

### Configure the CLI

Set environment variables pointing at a Telnyx LiveKit region:

```bash
export TELNYX_API_KEY=<your-telnyx-api-key>
export LIVEKIT_URL=https://<region>.livekit-telnyx.com
export LIVEKIT_API_KEY=$TELNYX_API_KEY
export LIVEKIT_API_SECRET=<your-secret>
```

`LIVEKIT_API_KEY` is the same Telnyx API key used everywhere on the platform. Register your credentials with the platform (once per region):

```bash
curl -s -X POST "https://<region>.livekit-telnyx.com/provision" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "my-project",
    "api_key": "'$TELNYX_API_KEY'",
    "api_secret": "'$LIVEKIT_API_SECRET'"
  }'
```

### Set up telephony

Buy a phone number and create a SIP connection pointing at your region's SIP endpoint (see [#Regions](regions.md)). Telnyx is the carrier, so there are no third-party SIP fees. You can set up numbers and SIP connections via the API or the [Telnyx Portal](https://portal.telnyx.com).

Then register the number with the platform by creating an [inbound trunk](https://docs.livekit.io/telephony/accepting-calls/inbound-trunk/) and a [dispatch rule](https://docs.livekit.io/telephony/accepting-calls/dispatch-rule/). When creating the inbound trunk, restrict `allowed_addresses` to `192.76.120.0/22` (Telnyx's SIP network).

### Deploy and call

Clone the example agents repo and deploy:

```bash
git clone https://github.com/team-telnyx/telnyx-livekit-agent-examples.git
cd telnyx-livekit-agent-examples/restaurant
lk agent create .
lk agent deploy . --secrets TELNYX_API_KEY=$TELNYX_API_KEY
```

Verify with `lk agent status`, then dial your purchased number. Troubleshooting tips: verify your SIP connection FQDN and DID assignment if calls don't connect; check `lk agent status` and `lk agent logs` if the agent doesn't pick up; use the closest region for best audio quality.

## Regions

Choose the region closest to your users for the lowest latency.

### Platform endpoints

| Region | Endpoint |
|---|---|
| New York | `https://nyc1.livekit-telnyx.com` |
| San Francisco | `https://sfo3.livekit-telnyx.com` |
| Atlanta | `https://atl1.livekit-telnyx.com` |
| Sydney | `https://syd1.livekit-telnyx.com` |

### SIP endpoints

| Region | SIP Endpoint |
|---|---|
| New York | `nyc1.sip.livekit-telnyx.com` |
| San Francisco | `sfo3.sip.livekit-telnyx.com` |
| Atlanta | `atl1.sip.livekit-telnyx.com` |
| Sydney | `syd1.sip.livekit-telnyx.com` |

## Telephony

Telnyx is the carrier — buy a number, connect it to your agent with no third-party SIP trunk setup. Calls route on-net from Telnyx SIP directly to your agent.

### Inbound calls

Inbound calls are routed to your agent via SIP dispatch rules. When someone calls your DID, Telnyx forwards it to the LiveKit SIP service, which dispatches it based on your configured rules.

### Outbound calls

Use the `lk` CLI to place an outbound call into a room:

```bash
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

- **G.722** — Wideband audio at 16 kHz sample rate. Enabled by default on all Telnyx SIP connections.
- **Opus** — Wideband audio at 48 kHz sample rate. Requires SRTP encryption on both sides — enable OPUS in your Telnyx SIP connection's inbound codec list and set `media_encryption: ALLOW` on your LiveKit inbound trunk. Delivers the highest audio quality for voice AI agents.

Both codecs are negotiated automatically during SIP call setup. If the remote side supports Opus, it will be preferred over G.722.

### Not yet supported

Call transfers (REFER / warm transfer) require Enterprise SIP, which is on the roadmap.
