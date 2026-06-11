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

*Part 1 of 3 — see also: [Part 2](telnyx-webrtc-voice-sdk--part-2.md), [Part 3](telnyx-webrtc-voice-sdk--part-3.md)*

The Telnyx WebRTC Voice SDK enables client-side applications to instantiate and control a Telnyx call leg using native WebRTC APIs, eliminating the need for traditional SIP UAs. Available for JavaScript, iOS, Android, and Flutter, the SDKs handle signaling via JSON-RPC over Secure WebSocket and media via SRTP, authenticating through credential-based SIP connections or JWTs and leveraging Telnyx's full Programmable Voice platform for call orchestration.

## Fundamentals

The WebRTC Voice SDKs let developers embed native voice capabilities directly into client-side applications. Instead of relying on inflexible SIP UAs such as PBX, Asterisk, or Zoiper, developers gain end-to-end visibility and control of the user experience.

The SDKs:

- Utilize the native client-end (browser or device) WebRTC API for cross-browser/device compatibility.
- Adhere to the WebRTC standard where media is transported via RTP over DTLS (SRTP/DTLS-SRTP).
- Implement WebRTC session negotiation (signaling) via JSON-RPC messages over Secure WebSocket (WSS).

### Availability

| SDK | Repository |
|---|---|
| JavaScript SDK | [GitHub](https://github.com/team-telnyx/webrtc) |
| Native iOS SDK | [GitHub](https://github.com/team-telnyx/telnyx-webrtc-ios) |
| Native Android SDK | [GitHub](https://github.com/team-telnyx/telnyx-webrtc-android) |
| Flutter SDK | [GitHub](https://github.com/team-telnyx/flutter-voice-sdk) |

## Architecture

The WebRTC Voice SDKs sit between client applications and Telnyx's core SIP platform. The gateway `rtc.telnyx.com` acts as a translation layer: on the SDK-facing side it adheres to the WebRTC standard, and on the SIP-facing side it speaks SIP protocol. To the core SIP platform, `rtc.telnyx.com` is merely another SIP UA.

Key implications of this architecture:

- **The SDKs cannot be used on their own for calling.** They lower the barrier for incorporating voice functionalities (i.e., instantiating a call leg), but all methods of authenticating an SDK client are based on a [Telnyx SIP Connection](telnyx-sip-connection.md). This setup avails the SDKs worldwide PSTN calling coverage and places those calls under the umbrella of the Programmable Voice API.
- **The SDKs cannot be used on their own to orchestrate call flow.** They allow local control (un/hold, un/mute, sending DTMF digits), but to orchestrate call flow or manipulate audio, TeXML or [Call Control API](call-control-api.md) must be used. For example, a prepaid calling app that announces remaining minutes before placing a call requires: (1) the SDK call leg parked via a SIP connection setting, (2) the user's backend responding to Telnyx webhooks, injecting custom TTS audio, placing an outbound PSTN leg (or hanging up due to insufficient balance), and bridging the WebRTC leg with the PSTN leg.

The SDKs' role in the Telnyx Voice Product Suite is to:

- Bring Telnyx voice infrastructure closer to end users, freeing developers from maintaining their own voice infrastructure.
- Lower the barrier to accessing worldwide PSTN coverage without requiring SIP knowledge.
- Unify all crucial CPaaS building blocks under the Telnyx umbrella, reducing multi-vendor integrations.

## Authentication

All SDK authentication methods are rooted in a credential-based SIP connection. Three authentication strategies are available.

### Credential-Based SIP Connection

Create a credential-based SIP connection with a `POST` to `/v2/credential_connections`:

```json
{
  "active": true,
  "password": "xxx",
  "user_name": "myagent01",
  "anchorsite_override": "Latency",
  "connection_name": "parent-sip-connection"
}
```

For call flows using **Pattern 1** (parked calls with webhook-driven call control), additionally configure:

```json
{
  "webhook_event_url": "https://mywebhook.com/primary",
  "webhook_event_failover_url": "https://mywebhook.com/backup",
  "webhook_api_version": "2",
  "webhook_timeout_secs": 25,
  "outbound": {
    "call_parking_enabled": true,
    "outbound_voice_profile_id": "123412415234124"
  }
}
```

For call flows using **Pattern 2** (direct SIP URI calling), configure:

```json
{
  "sip_uri_calling_preference": "internal"
}
```

SDKs authenticate with the `user_name` and `password` from the connection.

**Limits:** The combined count of credential connections, IP connections, FQDN connections, external connections, TeXML applications, and Call Control applications may not exceed 10,000 per account.

### Telephony Credentials

Multiple telephony credentials can be created on a single SIP connection. Create one with a `POST` to `/v2/telephony_credentials`:

```json
{
  "connection_id": "1567510696929005999",
  "expires_at": "2024-09-18T00:00:00",
  "name": "contact-center-1",
  "tag": "sandbox"
}
```

- `connection_id` is required.
- `expires_at` is recommended for security, especially when many credentials are expected.
- `name` and `tag` are recommended for management.

**Updating:** Use `PATCH /v2/telephony_credentials/:id`. An expired credential cannot be updated (expired is a terminal state); it can only be deleted.

**Revoking:** Delete a credential with `DELETE /v2/telephony_credentials/:id` to revoke a client's voice capabilities.

**Managing:** Filter credentials with query parameters:
- `filter[resource_id]` — prepend `connection:` to the connection ID (e.g., `filter[resource_id]=connection:1567510696929005999`).
- `filter[status]` — e.g., `expired`.
- `filter[tag]` — e.g., `sandbox`.

SDKs authenticate with the credential's `sip_username` (which starts with `gencred`) and `sip_password`.

**Limits:** No limit on the count of telephony credentials per connection or per account.

### JWT Authentication

Given an active telephony credential, generate a JWT with `POST /v2/telephony_credentials/:id/token`. The JWT is valid until 24 hours after creation or until the parent telephony credential expires, whichever comes first.

SDKs authenticate with the JWT token directly. This is the recommended authentication strategy.

**Limits:** No limit on token count per credential or aggregate token count per account.
