---
title: IP Authentication Token
summary: The `X-Telnyx-Token` header distinguishes multiple SIP connections sharing the same IP address.
sources:
  - url: https://developers.telnyx.com/docs/voice/sip-trunking/authentication/ip-authentication-token/index
    content_hash: 690d391bbae460c04eca6934eb5d527e78527edf75f0d25d0e77f549914d62c2
updated_at: 2026-04-10T00:00:00Z
---

# IP Authentication Token

The `X-Telnyx-Token` header distinguishes multiple SIP connections sharing the same IP address.

## Token requirements

| Requirement | Value                                         |
| ----------- | --------------------------------------------- |
| Characters  | Alphanumeric (a-z, A-Z, 0-9) and hyphens      |
| Length      | 12-48 characters                              |
| Scope       | Globally unique across all Telnyx connections |

## SIP header format

```
X-Telnyx-Token: your-token-value
```

Include this header in all outbound SIP INVITE requests.

## Configuration

[PATCH /v2/ip\_connections/](https://developers.telnyx.com/api-reference/ip-connections/update-an-ip-connection)

```json theme={null}
{
  "outbound": {
    "outbound_voice_profile_id": "uuid",
    "ip_authentication_token": "your-token-value"
  }
}
```

## Authentication behavior

| Condition                            | Result        |
| ------------------------------------ | ------------- |
| IP matches + token matches           | Authenticated |
| IP matches + token missing/incorrect | Rejected      |
| IP mismatch + token matches          | Rejected      |

Both the source IP and `X-Telnyx-Token` value must match the connection configuration.


## Related Pages

- [SIP Authentication Methods](../runbooks/sip-authentication-methods.md)
- [API Authentication](../reference/api-authentication.md)
- [CLI Authentication](../reference/cli-authentication.md)
- [Authentication](../runbooks/authentication.md)
- [Legacy CLI Authentication](../reference/legacy-cli-authentication.md)
