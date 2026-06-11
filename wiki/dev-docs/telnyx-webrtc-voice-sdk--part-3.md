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
  content_hash: a20cf2e0017be75557f539450f3307da21b333eaa69b19901a406792c273c340
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/credential-connections/index
  content_hash: d5122454a935a6f66dc3bca7c52b827bf79906760903329a55c7ae77ffe5ae66
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/jwt/index
  content_hash: 0f89bb14200552b1757f7b62bb905e776b38e88b0861eb22297dd7b2cecfe663
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/telephony-credentials/index
  content_hash: f9f2779f91ed142de73ba21f93d4b638726bd0675429abe044eab961f693e2a9
- url: https://developers.telnyx.com/docs/voice/webrtc/fundamentals/index
  content_hash: 558510f753a7aef85ef5f15594fd69d50143a71163b2a1adac63fc86faf65f76
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/anatomy
  content_hash: cb3264b1749b10af10d23377c69d453990fb6d1291e53872057acde9e204f2d1
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/demo-app/index
  content_hash: bfd76acc4b34a7590bd2702802b269ed003d0c92a97bd57845f4648964f6ebd9
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/interfaces/icalloptions
  content_hash: c8f9211d1a43523b96396c4c93c266a7fd4d94d3c64b3ebbfbd5f8c34d5f7acd
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/interfaces/iclientoptions
  content_hash: 6fefede6a564650b14f58e86da93837144eda430de72f694c109a311e8dc58c8
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
