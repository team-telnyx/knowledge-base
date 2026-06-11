---
title: Telnyx WebRTC Voice SDKs
summary: Comprehensive guide to the Telnyx WebRTC Voice SDKs covering architecture,
  authentication, push notifications across all platforms, call states, dialing, use
  cases, debugging, and costs.
sources:
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/android
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/flutter
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/index
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/ios
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/react-native
- url: https://developers.telnyx.com/docs/voice/webrtc/sdk-commonalities
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/debug-logs
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/detail-records/index
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/interpreting-debug-data/index
- url: https://developers.telnyx.com/docs/voice/webrtc/use-cases/contact-center/index
- url: https://developers.telnyx.com/docs/voice/webrtc/use-cases/outbound-dialer
updated_at: 2026-06-11T10:49:57Z
---

# Telnyx WebRTC Voice SDKs

*Part 1 of 4 — see also: [Part 2](telnyx-webrtc-voice-sdks--part-2.md), [Part 3](telnyx-webrtc-voice-sdks--part-3.md), [Part 4](telnyx-webrtc-voice-sdks--part-4.md)*

Comprehensive guide to the Telnyx WebRTC Voice SDKs covering architecture, authentication, push notifications across all platforms, call states, dialing, use cases, debugging, and costs.

## SDK Architecture and Commonalities

Across all Telnyx WebRTC SDKs there are two main classes:

- **Client** — represents the session, encapsulating the WebSocket connection used for signaling and the active call. It offers methods to instantiate outbound calls, register/unregister callback handlers for events, and control input/output devices.
- **Call** — represents a WebRTC media connection. It offers methods to answer, hang up, and emit DTMF digits.

Three categories of events are exposed:

- WebSocket changes (connected, disconnected)
- Client changes (ready to make/receive calls)
- Call changes (answered, etc.)

Two common usage patterns are supported:

1. **Client-driven** — A client-end application initiates a call, which is temporarily parked by Telnyx. A webhook event is sent to the user's backend, which performs additional processing (Voice API, TeXML, Conferencing) and may bridge a second call leg or queue the initial leg.
2. **Inbound-driven** — Telnyx receives an external call (e.g. PSTN), processes it via TeXML or Voice API, places it into a queue or conference, and the user's backend initiates a second call leg toward a client application. The two legs are eventually joined.

## Authentication

A Client instance must be authenticated before making or receiving calls. Three methods are supported:

- [Basic credential-based SIP connection](https://developers.telnyx.com/docs/voice/webrtc/auth/credential-connections)
- [Telephony credential](https://developers.telnyx.com/docs/voice/webrtc/auth/telephony-credentials)
- [JWT](https://developers.telnyx.com/docs/voice/webrtc/auth/jwt)

For contact-center and multi-agent scenarios, Telnyx recommends generating on-demand telephony credentials per agent, stored in a database and associated with the user login. An authentication token is then created from those credentials for the WebRTC client:

```js
const { data: telephonyCredentials } = await telnyx.telephonyCredentials.create({
  "connection_id": "1234567890",
  "name": "My-new-credential",
  "expires_at": EXPIRATION_DATE
});

const accessToken = await telnyx.telephonyCredentials
  .generateAccessTokenFromCredential('CREDENTIAL_ID');
```

## Call States

Every SDK exposes a set of call states describing where a call is in its lifecycle, sharing a common state machine. iOS and Android add **RECONNECTING** and **DROPPED** (with an associated reason) for network-recovery scenarios. Flutter and Android add an **ERROR** state for unrecoverable failures.

## Dialing Registered Clients

| Auth method | Dial target | Example |
|---|---|---|
| Basic credential SIP connection | SIP user name on the connection object | `john1234@sip.telnyx.com` |
| Basic credential SIP connection | Phone number on the connection* | `+13128889999` |
| Telephony credential | SIP user name on the telephony credential object | `gencredXXXYYY@sip.telnyx.com` |
| JWT | SIP user name on the parent telephony credential object | `gencredxXxYyY@sip.telnyx.com` |

\* Dialing by phone number requires "Destination Number Format" set to "SIP Username" on the Inbound settings of the same connection.

It is recommended to stick to one authentication method and not mix them. When multiple credentials share the same SIP username (e.g., a telephony credential and its JWTs), the last client to register receives calls — the result is indeterminate.
