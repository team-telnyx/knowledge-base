---
title: WebRTC Voice SDKs - Flutter to Index
summary: A consolidated reference for the Telnyx WebRTC Voice SDKs covering shared
  concepts (client/call classes, call states, authentication, multi-client registration,
  common call-flow patterns, and pricing), platform-specific push notification setup
  for iOS, Android, Flutter, and React Native, and troubleshooting tools including
  call detail records and debug data interpretation.
sources:
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/flutter
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/index
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/ios
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/react-native
- url: https://developers.telnyx.com/docs/voice/webrtc/sdk-commonalities
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/debug-logs
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/detail-records/index
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/interpreting-debug-data/index
- url: https://developers.telnyx.com/docs/voice/webrtc/use-cases/contact-center/index
updated_at: 2026-08-05T14:08:06Z
---

# WebRTC Voice SDKs - Flutter to Index

*Part 1 of 5 — see also: [Part 2](webrtc-voice-sdks-flutter-to-index--part-2.md), [Part 3](webrtc-voice-sdks-flutter-to-index--part-3.md), [Part 4](webrtc-voice-sdks-flutter-to-index--part-4.md), [Part 5](webrtc-voice-sdks-flutter-to-index--part-5.md)*

A consolidated reference for the Telnyx WebRTC Voice SDKs covering shared concepts (client/call classes, call states, authentication, multi-client registration, common call-flow patterns, and pricing), platform-specific push notification setup for iOS, Android, Flutter, and React Native, and troubleshooting tools including call detail records and debug data interpretation.

## Overview

The Telnyx WebRTC Voice SDKs provide a cross-platform way to embed real-time voice into web and mobile applications. A client maintains a WebSocket connection to the Telnyx platform for signaling and media, and registers a platform-specific push token (FCM for Android, APNS for iOS) so that incoming calls can wake a backgrounded or terminated app. When a push arrives, the device wakes the app, the client reconnects to the socket, and the actual call invitation is delivered.

```
Caller ──▶ Telnyx Platform ──▶ FCM / APNS ──▶ Device
                                                 │
                                          App wakes up
                                                 │
                                     Reconnects WebSocket
                                                 │
                                   Receives call invitation
```

## Classes, Methods, and Events

Across all SDKs there are two main classes:

- **Client** — represents the session and encapsulates the WebSocket connection used for signaling and the active call. It exposes methods to instantiate an outbound call, register/unregister callback handlers for events, and control input/output devices.
- **Call** — represents a WebRTC media connection. It exposes methods to perform actions on a call such as answering, hanging up, and emitting DTMF digits.

Events fall into three categories:

- Changes to the WebSocket (e.g. connected, disconnected)
- Changes to the client (e.g. ready to make and receive calls)
- Changes to the call (e.g. answered)

## Call States

Every SDK exposes a common set of call states describing where a call is in its lifecycle. Some platforms add extra states:

- **iOS and Android** add `RECONNECTING` and `DROPPED` (with an associated reason) for network-recovery scenarios.
- **Flutter and Android** add an `ERROR` state for unrecoverable failures.

## Authentication

A Client instance must be authenticated before a call can be made or received. Supported methods:

- [Credential Connections](credential-connections.md) — basic credential-based SIP connection
- [Telephony Credentials](telephony-credentials.md)
- [JWT Authentication](jwt-authentication.md)

It is recommended to stick to one method of authentication and not mix and match unless there is a compelling use case.

## Dialing Registered Clients

| Auth method | Addressable as |
| --- | --- |
| Basic credential-based SIP connection | SIP username on the connection object, e.g. `john1234@sip.telnyx.com` |
| Basic credential-based SIP connection | Phone number on the connection (requires "Destination Number Format" set to "SIP Username" on the Inbound setting), e.g. `+13128889999` |
| Telephony credential | SIP username on the telephony credential object, e.g. `gencredXXXYYY@sip.telnyx.com` |
| JWT | SIP username on the parent telephony credential object, e.g. `gencredxXxYyY@sip.telnyx.com` |

## Multi-Client Registration Behavior

When multiple credentials and tokens are attached to a single SIP connection, dialing the SIP username resolves to a single client, while dialing a telephony credential or JWT username resolves to the last client to register under that credential.

Example: a connection with SIP username `john1234` has telephony credential `gencred1` (with JWT `token1_1`) and telephony credential `gencred2` (with JWTs `token2_1` and `token2_2`).

| Address | Resolves to |
| --- | --- |
| `john1234@sip.telnyx.com` | `client_a` |
| `gencred1@sip.telnyx.com` | Indeterminate — the last client to register between `client_b` and `client_c` |
| `gencred2@sip.telnyx.com` | Indeterminate — the last client to register between `client_d`, `client_e`, and `client_f` |

## Common Usage Patterns

Two primitive patterns can be combined to build richer call flows.

### Client-driven pattern

- A client-end application (web or mobile) initiates a call.
- The call is temporarily parked by Telnyx.
- Telnyx issues a webhook event to the user's backend service.
- The backend performs additional processing using the Telnyx Voice API, TeXML, or Conferencing API.
- Depending on business logic, a second call leg may be initiated by the backend and bridged to the initial leg, or the initial leg may be placed into a queue or conference until bridged.

### Network-driven pattern

- Telnyx receives a call from outside the network (e.g. PSTN).
- Telnyx processes the call via TeXML instructions or Voice API commands.
- That call leg is placed into a queue or conference room.
- The user's backend initiates a second call leg toward a client-end application.
- The two legs are joined via a bridge command or conference join.

## Costs

WebRTC call legs are billed at $0.002/minute. Other voice legs and add-on features are charged separately and independently according to the user's price plan.
