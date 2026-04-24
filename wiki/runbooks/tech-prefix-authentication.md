---
title: Tech Prefix Authentication
summary: A 4-digit identifier prepended to outbound calls to differentiate multiple SIP connections sharing the same IP address.
sources:
  - url: https://developers.telnyx.com/docs/voice/sip-trunking/authentication/tech-prefix/index
    content_hash: 47a48327d8a18d20cf4e733ca2c14254607139acd14013b94e468d41ca4e60dd
updated_at: 2026-04-10T00:00:00Z
---

# Tech Prefix Authentication

A 4-digit identifier prepended to outbound calls to differentiate multiple SIP connections sharing the same IP address.

## Dial string format

```
[tech_prefix][destination_number]
```

Example: Tech prefix `1234` + destination `+18005678912` = `123418005678912`

## Use cases

* Multiple SIP connections from the same IP address
* Granular call routing and billing per connection
* Traffic stream separation

## Configuration

[PATCH /v2/ip\_connections/](https://developers.telnyx.com/api-reference/ip-connections/update-an-ip-connection)

```json theme={null}
{
  "inbound": {
    "sip_subdomain_receive_settings": "from_anyone"
  },
  "outbound": {
    "tech_prefix_enabled": true
  }
}
```

Tech prefix value is assigned by Telnyx and visible in the connection settings.

## Phone system setup

The PBX or SIP client must prepend the tech prefix to all outbound calls on the trunk.

## Authentication behavior

| Condition                    | Result                              |
| ---------------------------- | ----------------------------------- |
| Correct tech prefix included | Call authenticated                  |
| Missing or incorrect prefix  | `407 Proxy Authentication Required` |

## Alternative authentication methods

For connections sharing an IP address:

| Method                  | Description                  |
| ----------------------- | ---------------------------- |
| Tech prefix             | 4-digit prepended identifier |
| IP authentication token | Token-based validation       |
| P-Charge-Info header    | SIP header-based routing     |


## Related Pages

- [API Authentication](../reference/api-authentication.md)
- [CLI Authentication](../reference/cli-authentication.md)
- [Legacy CLI Authentication](../reference/legacy-cli-authentication.md)
- [Authentication](../runbooks/authentication.md)
- [IP Authentication Token](../runbooks/ip-authentication-token.md)
