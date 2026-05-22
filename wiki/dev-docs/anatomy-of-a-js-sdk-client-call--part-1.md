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

*Part 1 of 2 — see also: [Part 2](anatomy-of-a-js-sdk-client-call--part-2.md)*

A practical walkthrough of the Telnyx WebRTC JS SDK lifecycle: how the client connects and authenticates, how an outbound call is negotiated end‑to‑end, the most important client/call options, how to get hands‑on with the demo app, and how mobile push notifications keep inbound calls reliable on Android, iOS, React Native, and Flutter.

## Overview

The Telnyx WebRTC SDK maintains a signaling channel and a media session:

- A persistent WebSocket to rtc.telnyx.com exchanges signaling (login, invite, ringing, media, answer).
- A WebRTC peer connection transports audio/video with ICE, DTLS-SRTP, and device media capture.

Core browser APIs:
- WebSocket API (signaling): https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API
- WebRTC API (peer connection): https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API
- Media Capture and Streams API (mic/camera): https://developer.mozilla.org/en-US/docs/Web/API/Media_Capture_and_Streams_API

## Client lifecycle and authentication

A typical JS client does the following:

1) Instantiate the SDK client with credentials or a JWT.
2) Connect to open the WebSocket and authenticate (login). When registration completes, the SDK emits telnyx.ready and the client can make/receive calls.

Key behaviors surfaced in the demo tooling logs:
- After socket open, the client sends a login request. The platform replies with “logged in” and then a telnyx_rtc.clientReady event.
- The SDK queries gateway state; a REGED state maps to the telnyx.ready event.

Authentication options (from WebRTC JS Client Options): see [WebRTC JS Client Options](webrtc-js-client-options.md). Highlights:
- login and password: SIP credential auth (e.g., telephony credentials or credential-based SIP Connections).
- login_token: JWT-based auth (recommended).
- anonymous_login: target an AI assistant by ID (ai_assistant target_type), optionally with target_params forwarded as SIP headers.

Operational options worth knowing:
- iceServers, prefetchIceCandidates, trickleIce, forceRelayCandidate, region
- ringtoneFile, ringbackFile
- debug and debugOutput (collect WebRTC stats/logs)
- callReportInterval and enableCallReports (automatic post-call stats to voice-sdk-proxy)
- mediaPermissionsRecovery (guided retry flow for inbound-call getUserMedia failures)
- keepConnectionAliveOnSocketClose (attempt to keep the peer connection if the socket drops unexpectedly)

Related setup and auth pages: [Credential Connections](credential-connections.md), [Telephony Credentials](telephony-credentials.md), [JWTs](jwts.md), [SDK Commonalities](sdk-commonalities.md).

## Outbound call flow (offer/answer and ICE)

When you place a call, the SDK executes the standard WebRTC negotiation before it ever sends a SIP/JSON-RPC INVITE over the WebSocket:

1) Create RTCPeerConnection.
2) Prompt for and capture local media (getUserMedia) per your audio/video constraints.
3) Add tracks/transceivers; negotiationneeded fires.
4) Create an SDP offer and set it as the local description; ICE gathering begins.
5) When candidates are gathered (or trickled), the SDK includes them with the INVITE (telnyx_rtc.invite) sent over the WebSocket.
6) The platform responds with ringing, then sends a media (answer) message with its SDP.
7) The SDK setRemoteDescription(answer); the connectionState moves to connected and media flows (typically UDP via the selected ICE candidate).

This flow is visible in chrome://webrtc-internals alongside SDK debug logs.

## Key JS client options

See full reference in [WebRTC JS Client Options](webrtc-js-client-options.md). Commonly used fields:
- Authentication: login, password, login_token; or anonymous_login { target_type: "ai_assistant", target_id, target_params, target_version_id }
- Networking/ICE: iceServers, prefetchIceCandidates (default true), trickleIce, forceRelayCandidate, region, useCanaryRtcServer
- Media/user experience: ringtoneFile, ringbackFile, mutedMicOnStart
- Diagnostics: debug, debugOutput, callReportInterval (default 5000 ms), enableCallReports (default true)
- Resilience: keepConnectionAliveOnSocketClose, rtcIp/rtcPort (custom signaling)
- Inbound media recovery: mediaPermissionsRecovery { enabled, timeout, onSuccess, onError }

## Key call options

See full reference in [WebRTC JS Call Options](webrtc-js-call-options.md). Notable fields when calling:
- destinationNumber: E.164 number or SIP URI
- callerName, callerNumber: outbound caller ID (PSTN requires a valid number)
- audio/video: booleans or MediaTrackConstraints; useStereo
- Device and elements: micId, camId, speakerId, localElement, remoteElement, localStream/remoteStream
- ICE and codecs per call: iceServers, prefetchIceCandidates, trickleIce, forceRelayCandidate, preferred_codecs
- Signaling/customization: customHeaders[], onNotification, id (custom callID)
- Call Control integration: clientState (base64), telnyxCallControlId, telnyxLegId, telnyxSessionId

## Using the JS SDK demo app

The hosted demo at webrtc.telnyx.com is the fastest way to verify your setup. See [JS SDK Demo App](js-sdk-demo-app.md) for step-by-step API-first provisioning. Condensed prerequisites:
- Fund account balance.
- Create an Outbound Voice Profile (OVP) whitelisting destination countries.
- Create a Credential-Based SIP Connection and associate it with the OVP.
- Purchase a phone number and assign it to the connection.

In the demo app configure:
- Authentication: Credential
- SIP Username/Password: from your telephony credential
- Caller ID Name/Number: the purchased number (E.164)

You should see registered after Connect. To place a call, dial an E.164 destination that’s allowed by your OVP. To receive a call, register a second client and dial gencred_username@sip.telnyx.com from the other client, or call the assigned phone number. See [SDK Commonalities](sdk-commonalities.md) for “Dialing registered clients.”

## Push notifications (Android, iOS, React Native, Flutter)

Why pushes matter: mobile apps can’t keep a WebSocket open when backgrounded or terminated. Telnyx registers a platform push token (FCM/APNS) during login so that, on inbound call, a push wakes the app, which then reconnects and receives the real invitation.

- Multidevice: up to 5 active push tokens per user across platforms; adding a 6th evicts the least-recently-used.
- Portal setup: create Mobile Push Credentials (Android: FCM service account JSON; iOS: VoIP APNS cert/key PEMs) and attach them to your SIP Connection’s WebRTC tab.

Platform guides and key notes:
- [Android Push Notifications](android-push-notifications.md): provide FCM token to the SDK on connect; handle a FirebaseMessagingService to display incoming call UI; Android 14 requires POST_NOTIFICATIONS and foreground service permissions; optional decline flow via a short-lived connect-with-decline.
- [iOS Push Notifications](ios-push-notifications.md): VoIP pushes via PushKit; pass APNS token to the client; you must report every VoIP push to CallKit on iOS 13+ or the OS will terminate the app; ensure APNS environment (sandbox vs production) matches your build.
- [React Native Push Notifications](react-native-push-notifications.md): combine FCM (Android) and PushKit (iOS); ensure manifest/services and Xcode capabilities are configured; always reconnect after a push to receive the invitation.
- [Flutter Push Notifications](flutter-push-notifications.md): wire background handlers for FCM, create a high-importance notification channel, integrate CallKit/Incoming UI; on iOS follow the same PushKit/CallKit requirements.

API: Mobile Push Credentials can be managed programmatically via the Telnyx API.
