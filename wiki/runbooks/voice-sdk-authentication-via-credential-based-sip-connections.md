---
title: Voice SDK Authentication via Credential Based SIP Connections
summary: The following API request will create a basic credential based SIP connection.
sources:
  - url: https://developers.telnyx.com/docs/voice/webrtc/auth/credential-connections/index
    content_hash: c6707851bc92df02807a4cd4be0f81d20ceac7e961634fd1392fc84a38e042fa
updated_at: 2026-04-10T00:00:00Z
---

# Voice SDK Authentication via Credential Based SIP Connections

## Prerequisites

* A valid V2 API key

## Creating a Credential Based SIP Connection

The following API request will create a basic credential based SIP connection.

```http theme={null}
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

For call flows that make use of Pattern 1 (See [Common Usage Patterns](https://developers.telnyx.com/docs/voice/webrtc/fundamentals#common-usage-patterns)), the following additional configuration is required.

```
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

For call flows that make use of Pattern 2 (See [Common Usage Patterns](https://developers.telnyx.com/docs/voice/webrtc/fundamentals#common-usage-patterns)), the following configuration is required.

```
PATCH /v2/credential_connections/:id HTTP/1.1
Host: api.telnyx.com
Content-Type: application/json
Authorization: Bearer XXX
Content-Length: 169

{
   "sip_uri_calling_preference": "internal"
}
```

## SDK Authentication

SDKs are authenticated with

* `user_name`
* `password`

## Limits

Sum of the following may not exceed 10,000 for an account.

* Count of credential connection
* Count of IP connection
* Count of FQDN connection
* Count of external connection
* Count of TeXML application
* Count of Call Control Application

## Additional Resources

* [Credential SIP Connections API Reference](https://developers.telnyx.com/api-reference/credential-connections/create-a-credential-connection#create-a-credential-connection)


## Related Pages

- [Voice SDK Authentication via Telephony Credentials](../runbooks/voice-sdk-authentication-via-telephony-credentials.md)
- [Voice SDK Authentication via JWTs](../runbooks/voice-sdk-authentication-via-jwts.md)
