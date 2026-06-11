---
title: Telnyx WebRTC Voice SDK
summary: The Telnyx WebRTC Voice SDK enables client-side applications to instantiate
  and control a Telnyx call leg using native WebRTC APIs, eliminating the need for
  traditional SIP UAs. Available for JavaScript, iOS, Android, and Flutter, the SDKs
  handle signaling via JSON-RPC over Secure WebSocket and media via SRTP, authenticating
  through credential-based SIP connections or JWTs and leveraging Telnyx's full Programmable
  Voice platform for call orchestration.
sources:
- url: https://developers.telnyx.com/docs/voice/webrtc/architecture
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/credential-connections/index
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/jwt/index
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/telephony-credentials/index
- url: https://developers.telnyx.com/docs/voice/webrtc/fundamentals/index
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/anatomy
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/demo-app/index
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/interfaces/icalloptions
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/interfaces/iclientoptions
updated_at: 2026-06-11T10:48:20Z
---

# Telnyx WebRTC Voice SDK

*Part 3 of 3 — see also: [Part 1](telnyx-webrtc-voice-sdk--part-1.md), [Part 2](telnyx-webrtc-voice-sdk--part-2.md)*

The Telnyx WebRTC Voice SDK enables client-side applications to instantiate and control a Telnyx call leg using native WebRTC APIs, eliminating the need for traditional SIP UAs. Available for JavaScript, iOS, Android, and Flutter, the SDKs handle signaling via JSON-RPC over Secure WebSocket and media via SRTP, authenticating through credential-based SIP connections or JWTs and leveraging Telnyx's full Programmable Voice platform for call orchestration.

## Demo App Setup

A JS SDK demo app is available at [webrtc.telnyx.com](https://webrtc.telnyx.com). To set it up:

### Prerequisites

1. **Account Balance** — Sign up and top up with credit (e.g., $5).
2. **Outbound Voice Profile** — Create one with whitelisted destinations:

```json
{ "name": "webrtc", "whitelisted_destinations": ["US"] }
```

3. **Credential-Based SIP Connection** — Create one, referencing the OVP:

```json
{
  "active": true,
  "password": "xxx",
  "user_name": "xxx",
  "anchorsite_override": "Latency",
  "connection_name": "sample-connection",
  "sip_uri_calling_preference": null,
  "outbound": { "outbound_voice_profile_id": "<ovp_id>" }
}
```

4. **Phone Number** — Search available numbers, then place an order with the `connection_id`. US or CA numbers are easiest to activate (no regulatory delays). Poll the order status until `success`.

### Configuring the Demo App

1. Create a telephony credential on the SIP connection.
2. In the demo app, set:
   - Authentication → Credential
   - SIP Username → from the telephony credential
   - Password → from the telephony credential
   - Caller ID Name/Number → purchased phone number in +E164 format
3. Click **Connect**; you should see `registered` in the log.

### Making a Call

Enter the destination phone number in +E164 format. Ensure the destination country is in the OVP's `whitelisted_destinations`.

### Receiving a Call

Register another client in a separate tab and dial `[sip_username]@sip.telnyx.com` (where `sip_username` starts with `gencred`). Alternatively, register the SIP connection credentials and dial the phone number from a mobile device.

## API References

- [Credential SIP Connections API](https://developers.telnyx.com/api-reference/credential-connections/create-a-credential-connection)
- [Telephony Credentials API](https://developers.telnyx.com/docs/voice/webrtc/auth/telephony-credentials)
- [JWT API](https://developers.telnyx.com/docs/voice/webrtc/auth/jwt)
- [Outbound Voice Profiles API](https://developers.telnyx.com/api-reference/outbound-voice-profiles/create-an-outbound-voice-profile)
- [Phone Number Search API](https://developers.telnyx.com/api-reference/phone-number-search/list-available-phone-numbers)
- [Number Order API](https://developers.telnyx.com/api-reference/phone-number-orders/create-a-number-order)
