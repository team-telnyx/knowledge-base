---
title: SIP Authentication Methods
summary: Telnyx SIP connections support multiple authentication methods based on network topology and security requirements.
sources:
  - url: https://developers.telnyx.com/docs/voice/sip-trunking/authentication/credential-types/index
    content_hash: 9e9aa609ab36fb8c477e66efa34d857341a4ac49d6fa4a4864e758facd41102e
updated_at: 2026-04-10T00:00:00Z
---

# SIP Authentication Methods

Telnyx SIP connections support multiple authentication methods based on network topology and security requirements.

## Methods

| Method                                                                        | Description                                | Details       |
| ----------------------------------------------------------------------------- | ------------------------------------------ | ------------- |
| Credential-based                                                              | Username/password for SIP registration     | See below     |
| [IP + Token](ip-authentication-token.md) | `X-Telnyx-Token` header with IP validation | Separate page |
| [IP + Tech Prefix](tech-prefix-authentication.md)       | 4-digit prefix prepended to dial string    | Separate page |
| IP + P-Charge-Info                                                            | Phone number in `P-Charge-Info` header     | See below     |
| FQDN                                                                          | Hostname-based inbound routing             | See below     |

## Credential-based authentication

Username and password for SIP registration.

[POST /v2/credential\_connections](https://developers.telnyx.com/api-reference/credential-connections/create-a-credential-connection)

```json theme={null}
{
  "connection_name": "my-connection",
  "user_name": "username",
  "password": "secure-password"
}
```

For WebRTC applications requiring dynamic credentials or JWT tokens, see [WebRTC Authentication](voice-sdk-authentication-via-credential-based-sip-connections.md).

## P-Charge-Info authentication

SIP header containing a phone number associated with the connection.

```
P-Charge-Info: <sip:+12125551234@sip.telnyx.com>
```

Requires E.164 format. The number must be assigned to the connection.

## FQDN authentication

Hostname-based inbound routing combined with credentials or IP authentication for outbound.

| Inbound | Outbound    |
| ------- | ----------- |
| FQDN    | Credentials |
| FQDN    | IP address  |

## Comparison

| Method             | Inbound | Outbound | Dynamic IP | Static IP |
| ------------------ | ------- | -------- | ---------- | --------- |
| Credentials        | ✓       | ✓        | ✓          | ✓         |
| IP + Tech prefix   | ✓       | ✓        | -          | ✓         |
| IP + Token         | ✓       | ✓        | -          | ✓         |
| IP + P-Charge-Info | ✓       | ✓        | -          | ✓         |
| FQDN + Credentials | ✓       | ✓        | ✓          | ✓         |
| FQDN + IP          | ✓       | ✓        | -          | ✓         |


## Related Pages

- [IP Authentication Token](../runbooks/ip-authentication-token.md)
- [API Authentication](../reference/api-authentication.md)
- [CLI Authentication](../reference/cli-authentication.md)
- [Authentication](../runbooks/authentication.md)
- [Voice SDK Authentication via JWTs](../runbooks/voice-sdk-authentication-via-jwts.md)
