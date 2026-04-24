---
title: WebRTC Voice SDKs Fundamentals
summary: These SDKs enable client-side applications to instantiate and control a Telnyx call leg.
sources:
  - url: https://developers.telnyx.com/docs/voice/webrtc/fundamentals/index
    content_hash: d369b4abb9c0cda52bcf6475e933dd4f0f49c56e36a7261a4efff467db307f8a
updated_at: 2026-04-10T00:00:00Z
---

# WebRTC Voice SDKs Fundamentals

## What & Why

These SDKs enable client-side applications to instantiate and control a Telnyx call leg.

As a result, developers of applications integrated with Telnyx voice platform are no longer constrained to working with inflexible and uncustomizable SIP UAs such as PBX, Asterisk, Zoiper etc.

Instead they can embed native voice capabilities client-side to work seamlessly with their voice application and achieve end to end visibility and control of the user experience.

## How

These SDKs

* Utilize the native client-end (browser or device) WebRTC API for cross browser/device compatibility, …
* Adhere to the WebRTC standardization where Media is transported via RTP over DTLS, aka SRTP, aka DTLS-SRTP, … and
* Implements the WebRTC session negotiation, aka signaling, via JSON-RPC messages over Secure WebSocket (WSS).

## Availability

The following SDKs are offered

* [Javascript SDK](https://github.com/team-telnyx/webrtc)
* [Native iOS SDK](https://github.com/team-telnyx/telnyx-webrtc-ios)
* [Native Android SDK](https://github.com/team-telnyx/telnyx-webrtc-android)
* [Flutter SDK](https://github.com/team-telnyx/flutter-voice-sdk)


## Related Pages

- [WebRTC Voice SDKs Debug Data](../runbooks/webrtc-voice-sdks-debug-data.md)
- [WebRTC Voice SDKs Commonalities](../runbooks/webrtc-voice-sdks-commonalities.md)
- [WebRTC Voice SDKs Call Detail Records](../runbooks/webrtc-voice-sdks-call-detail-records.md)
- [WebRTC Voice SDKs Architecture](../runbooks/webrtc-voice-sdks-architecture.md)
- [Interpreting WebRTC Voice SDKs Debug Data](../runbooks/interpreting-webrtc-voice-sdks-debug-data.md)
