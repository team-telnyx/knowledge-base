---
title: Voice SDK Authentication via Telephony Credentials
summary: The following API request will create a telephony credential.
sources:
  - url: https://developers.telnyx.com/docs/voice/webrtc/auth/telephony-credentials/index
    content_hash: 2ac23a9f9b0239b1991ce8f07341ed27e348b5cf05aa26446d77c155b1962017
updated_at: 2026-04-10T00:00:00Z
---

# Voice SDK Authentication via Telephony Credentials

## Prerequisites

* An active credential based SIP connection

## Create a Credential

The following API request will create a telephony credential.

```http theme={null}
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

* `connection_id` is required
* `expires_at` is recommended for security especially when many are expected to be created
* `name` and `tag` are recommended for easy management

Multiple telephony credentials can be created on a single connection.

## Updating a Credential

After a credential's creation, it may be updated via the PATCH endpoint.

```http theme={null}
PATCH /v2/telephony_credentials/:id HTTP/1.1
Host: api.telnyx.com
Content-Type: application/json
Authorization: Bearer XXX
Content-Length: 83

{
  "expires_at": "2024-09-11T21:07:00"
}
```

The following error will be returned when trying to perform updates on an `expired` credential since that state is terminal.

```http theme={null}
{
    "errors": {
        "status": "can't update credentials in expired status"
    }
}
```

An expired credential can only be deleted.

## Revoking a Credential

A client-side application’s voice capabilities can be revoked by removing the corresponding credential.

```http theme={null}
DELETE /v2/telephony_credentials/:id HTTP/1.1
Host: api.telnyx.com
Content-Type: application/json
Authorization: Bearer XXX
```

## Managing Credentials

The following filters are useful when managing many credentials.

* `filter[resource_id]` e.g. `filter[resource_id]=connection:1567510696929005999`. Note that `connection:` must be prepended to the connection ID.
* `filter[status]` e.g. `filter[status]=expired`
* `filter[status]` e.g. `filter[tag]=sandbox`

```http theme={null}
GET /v2/telephony_credentials?filter[status]=expired&filter[tag]=sandbox HTTP/1.1
Host: api.telnyx.com
Authorization: Bearer XXX
```

## SDK Authentication

SDKs are authenticated with

* `sip_username` which starts with `gencred`
* `sip_password`

## Limits

Currently, there exists

* No limit on count of telephony credentials on a connection,
* Nor any limit on the aggregate count of telephony credentials on a single account.

## Additional Resources

* [Telephony Credentials API Reference](https://developers.telnyx.com/docs/voice/webrtc/auth/telephony-credentials/index#create-a-credential)


## Related Pages

- [Voice SDK Authentication via JWTs](../runbooks/voice-sdk-authentication-via-jwts.md)
- [Voice SDK Authentication via Credential Based SIP Connections](../runbooks/voice-sdk-authentication-via-credential-based-sip-connections.md)
