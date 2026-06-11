---
title: Telnyx WebRTC Voice SDKs
summary: Comprehensive guide to the Telnyx WebRTC Voice SDKs covering architecture,
  authentication, push notifications across all platforms, call states, dialing, use
  cases, debugging, and costs.
sources:
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/android
  content_hash: 3fedfc040ba32d2fc260b1a579cd1f8ac4753568e8ff8a2992a62e3f40868e8f
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/flutter
  content_hash: 37576f7c51e98e804c53c696f71d04a1f423e306cb42ed16c04b94bdce9c7194
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/index
  content_hash: 42c36618bb0701822e5ea49792d6cc08326c19f09163f9661402976d2af85313
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/ios
  content_hash: a73f480aea535097057ca6c987ba62346ec058988dd0e032c1fb8e89f67ad638
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/react-native
  content_hash: a36b6cda308b54ac45a958bb0c47227e939f9cbb33579b5d4751525710f2be46
- url: https://developers.telnyx.com/docs/voice/webrtc/sdk-commonalities
  content_hash: cdd95e464a79746264328e70ea199bf2fff9aa2aad036d53cd27a72e4fecc817
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/debug-logs
  content_hash: 2ca56f8d180406798028958d59f4592bbcdb16c001fed0275c36663b4f85f4f0
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/detail-records/index
  content_hash: b87a3806edb676bb6f754a9a871f8bfde50507fff598e77ca7624259d53a0a25
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/interpreting-debug-data/index
  content_hash: f616744b0e7b693486449482bb769ac7c549642a4e62508f710b7821435b7967
- url: https://developers.telnyx.com/docs/voice/webrtc/use-cases/contact-center/index
  content_hash: ab112fd87bff5aee9d8cc7bd8252fd42b4e2f1dce43fd3a6ec95ebba4a288fc8
- url: https://developers.telnyx.com/docs/voice/webrtc/use-cases/outbound-dialer
  content_hash: 9ef961c8750a0649f790a594d6b1b232f1e5d0e191fccd8f4d8678f237474526
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
