---
title: WebRTC Voice SDKs
summary: The Telnyx WebRTC Voice SDKs enable client-side applications to instantiate
  and control Telnyx call legs from browsers and mobile devices. They translate between
  the WebRTC standard and Telnyx's SIP platform, providing worldwide PSTN coverage
  under the Programmable Voice API umbrella. This page covers SDK architecture, authentication
  options, the JS SDK client and call lifecycle, demo app setup, configuration interfaces,
  and Android push notifications.
sources:
- url: https://developers.telnyx.com/docs/voice/webrtc/architecture
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/credential-connections/index
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/jwt/index
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/telephony-credentials/index
- url: https://developers.telnyx.com/docs/voice/webrtc/fundamentals
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/anatomy
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/demo-app/index
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/interfaces/icalloptions
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/interfaces/iclientoptions
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/android
updated_at: 2026-08-05T14:08:20Z
---

# WebRTC Voice SDKs

*Part 2 of 7 — see also: [Part 1](webrtc-voice-sdks--part-1.md), [Part 3](webrtc-voice-sdks--part-3.md), [Part 4](webrtc-voice-sdks--part-4.md), [Part 5](webrtc-voice-sdks--part-5.md), [Part 6](webrtc-voice-sdks--part-6.md), [Part 7](webrtc-voice-sdks--part-7.md)*

The Telnyx WebRTC Voice SDKs enable client-side applications to instantiate and control Telnyx call legs from browsers and mobile devices. They translate between the WebRTC standard and Telnyx's SIP platform, providing worldwide PSTN coverage under the Programmable Voice API umbrella. This page covers SDK architecture, authentication options, the JS SDK client and call lifecycle, demo app setup, configuration interfaces, and Android push notifications.

## Authentication

The SDKs support three authentication strategies, all of which are based on a credential-based SIP connection.

### Credential SIP Connections

**Prerequisite:** A valid V2 API key.

Create a basic credential-based SIP connection:

```http
POST /v2/credential_connections HTTP/1.1
Host: api.telnyx.com
Content-Type: application/json
Authorization: Bearer XXX
Content-Length: 169

{
    "active": true,
    "password": "xxx",
    "user_name": "myagent01",
    "anchorsite_override": "Latency",
    "connection_name": "parent-sip-connection"
}
```

For call flows that use Pattern 1 (see [WebRTC Voice SDKs Fundamentals](webrtc-voice-sdks-fundamentals.md)), the following additional configuration is required:

```http
PATCH /v2/credential_connections/:id HTTP/1.1
Host: api.telnyx.com
Content-Type: application/json
Authorization: Bearer XXX
Content-Length: 169

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

For call flows that use Pattern 2, the following configuration is required:

```http
PATCH /v2/credential_connections/:id HTTP/1.1
Host: api.telnyx.com
Content-Type: application/json
Authorization: Bearer XXX
Content-Length: 169

{
   "sip_uri_calling_preference": "internal"
}
```

SDKs are authenticated with `user_name` and `password`.

**Limits:** The sum of the following may not exceed 10,000 for an account: credential connections, IP connections, FQDN connections, external connections, TeXML applications, and Call Control Applications.

See the [Credential SIP Connections API Reference](https://developers.telnyx.com/api-reference/credential-connections/create-a-credential-connection#create-a-credential-connection).

### Telephony Credentials

**Prerequisite:** An active credential-based SIP connection.

Create a telephony credential:

```http
POST /v2/telephony_credentials HTTP/1.1
Host: api.telnyx.com
Content-Type: application/json
Authorization: Bearer XXX
Content-Length: 75

{
  "connection_id": "1567510696929005999",
  "expires_at": "2024-09-18T00:00:00",
  "name": "contact-center-1",
  "tag": "sandbox"
}
```

- `connection_id` is required.
- `expires_at` is recommended for security, especially when many are expected to be created.
- `name` and `tag` are recommended for easy management.

Multiple telephony credentials can be created on a single connection.

Update a credential via the PATCH endpoint:

```http
PATCH /v2/telephony_credentials/:id HTTP/1.1
Host: api.telnyx.com
Content-Type: application/json
Authorization: Bearer XXX
Content-Length: 83

{
  "expires_at": "2024-09-11T21:07:00"
}
```

The following error is returned when trying to update an `expired` credential, since that state is terminal:

```json
{
    "errors": {
        "status": "can't update credentials in expired status"
    }
}
```

An expired credential can only be deleted.

Revoke a credential by removing it:

```http
DELETE /v2/telephony_credentials/:id HTTP/1.1
Host: api.telnyx.com
Content-Type: application/json
Authorization: Bearer XXX
```

Useful filters for managing many credentials:

- `filter[resource_id]` e.g. `filter[resource_id]=connection:1567510696929005999`. Note that `connection:` must be prepended to the connection ID.
- `filter[status]` e.g. `filter[status]=expired`
- `filter[tag]` e.g. `filter[tag]=sandbox`

```http
GET /v2/telephony_credentials?filter[status]=expired&filter[tag]=sandbox HTTP/1.1
Host: api.telnyx.com
Authorization: Bearer XXX
```

SDKs are authenticated with `sip_username` (which starts with `gencred`) and `sip_password`.

**Limits:** There is no limit on the count of telephony credentials on a connection, nor any limit on the aggregate count of telephony credentials on a single account.

### JWTs

**Prerequisite:** An active telephony credential.

Generate a JWT:

```http
POST /v2/telephony_credentials/:id/token HTTP/1.1
Host: api.telnyx.com
Authorization: Bearer XXX
```

The JWT is valid until 24 hours after its creation or until the parent telephony credential expires, whichever comes first.

SDKs are authenticated with the JWT.

**Limits:** There is no limit on the count of tokens on a telephony credential, nor any limit on the aggregate count of tokens on a single account.
