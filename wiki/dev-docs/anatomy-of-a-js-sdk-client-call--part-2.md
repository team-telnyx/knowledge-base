---
title: Anatomy of a JS SDK Client & Call
summary: 'A practical walkthrough of the Telnyx WebRTC JS SDK lifecycle: how the client
  connects and authenticates, how an outbound call is negotiated end‑to‑end, the most
  important client/call options, how to get hands‑on with the demo app, and how mobile
  push notifications keep inbound calls reliable on Android, iOS, React Native, and
  Flutter.'
sources:
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/anatomy
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/demo-app/index
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/interfaces/icalloptions
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/interfaces/iclientoptions
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/index
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/android
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/ios
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/react-native
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/flutter
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
