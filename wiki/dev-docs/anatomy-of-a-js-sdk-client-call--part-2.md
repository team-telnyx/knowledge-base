---
title: Anatomy of a JS SDK Client & Call
summary: 'A practical walkthrough of the Telnyx WebRTC JS SDK lifecycle: how the client
  connects and authenticates, how an outbound call is negotiated end‑to‑end, the most
  important client/call options, how to get hands‑on with the demo app, and how mobile
  push notifications keep inbound calls reliable on Android, iOS, React Native, and
  Flutter.'
sources:
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/anatomy
  content_hash: 15d250d3d5361916bcdbc07e63fdfdd822aa512a681bc4e5dadf107ab9948678
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/demo-app/index
  content_hash: cd615358f5ec6c38ad6149d2445b193e813c04645a07393483bffb5d22f72212
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/interfaces/icalloptions
  content_hash: f08ff1e7bba29686ef27ad9119e51638930e8afb3bc23654315572641f349bd8
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/interfaces/iclientoptions
  content_hash: a028396a0cc2eedae3d3da91a1becd9e77f36719892fdbd72d3aec1048153f12
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/index
  content_hash: 8fccb538b7af5ab4d8cdcb5c3e9523b841b8b320af7ec5afe9e347a25336b15f
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/android
  content_hash: b8e4114b1261350dce3d7ce6b937155d2d331273bad0ff78829ecb2dca246a98
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/ios
  content_hash: f14fd32114cdb7d173e333aea9992a1df47d03fcde7fadb5fd7da9c7a63abf4d
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/react-native
  content_hash: 85da9e8282d1215648728563748ab975f3276a76395d12e49f7209ca3eb36fee
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/flutter
  content_hash: 9a99adbc8ea444f6bf049eb034ddab958ba13bef5478b4401b23116e80525815
updated_at: 2026-05-20T10:24:32Z
---

# Anatomy of a JS SDK Client & Call

*Part 2 of 2 — see also: [Part 1](anatomy-of-a-js-sdk-client-call--part-1.md)*

A practical walkthrough of the Telnyx WebRTC JS SDK lifecycle: how the client connects and authenticates, how an outbound call is negotiated end‑to‑end, the most important client/call options, how to get hands‑on with the demo app, and how mobile push notifications keep inbound calls reliable on Android, iOS, React Native, and Flutter.

## Troubleshooting tips

- Registration never reaches ready: confirm credentials, OVP country whitelist, SIP Connection assignment, and network reachability to rtc.telnyx.com.
- Outbound call fails early: verify microphone permissions and getUserMedia grants; use chrome://webrtc-internals and SDK debug logs.
- Media one-way or no audio: try forceRelayCandidate, verify ICE servers and firewall/NAT, and inspect selected candidate pair.
- Push arrived but no call UI: your app must reconnect the SDK client after receiving the push so the pending invitation can be delivered.
- iOS app killed on push: ensure every VoIP push is reported to CallKit.

Related guides: [Call Detail Records](call-detail-records.md), [Debug Logs](debug-logs.md), [Interpreting Debug Data](interpreting-debug-data.md).

## References and next steps

- Demo and anatomy walkthroughs: [JS SDK Demo App](js-sdk-demo-app.md) and this page.
- Full option references: [WebRTC JS Client Options](webrtc-js-client-options.md) and [WebRTC JS Call Options](webrtc-js-call-options.md).
- Push overviews and platform guides: [Push Notifications](push-notifications.md), [Android Push Notifications](android-push-notifications.md), [iOS Push Notifications](ios-push-notifications.md), [React Native Push Notifications](react-native-push-notifications.md), [Flutter Push Notifications](flutter-push-notifications.md).
- External API references (examples):
  - Outbound Voice Profiles API: https://developers.telnyx.com/api-reference/outbound-voice-profiles/create-an-outbound-voice-profile
  - Credential Connections API: https://developers.telnyx.com/api-reference/credential-connections/create-a-credential-connection
  - Number Search API: https://developers.telnyx.com/api-reference/phone-number-search/list-available-phone-numbers
  - Number Orders API: https://developers.telnyx.com/api-reference/phone-number-orders/create-a-number-order
