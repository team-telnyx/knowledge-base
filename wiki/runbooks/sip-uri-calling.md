---
title: SIP URI Calling
summary: SIP URI calling enables inbound calls to a SIP username, eliminating the need for a traditional phone number.
sources:
  - url: https://developers.telnyx.com/docs/voice/sip-trunking/features/sip-uri-calling/index
    content_hash: f40e51f1bdf55b65fefe52c7e7d0c16ff421a85dbbae4034114c5e5224e33638
updated_at: 2026-04-10T00:00:00Z
---

# SIP URI Calling

SIP URI calling enables inbound calls to a SIP username, eliminating the need for a traditional phone number. This feature allows direct communication using SIP addresses in the format `username@sip.telnyx.com`.

## Prerequisites

* Active SIP connection with credential authentication
* SIP device or softphone registered with connection credentials
* Feature enabled on the connection's inbound settings

<Callout type="info">
  SIP URI calling is disabled by default and must be explicitly enabled for each connection.

## SIP URI format

Calls are placed to the SIP username using the standard SIP URI format:

```
username@sip.telnyx.com
```

**Username requirements:**

* Must begin with a non-numeric character
* This restriction prevents number spoofing and unauthorized dialing

Example valid usernames:

* `support@sip.telnyx.com`
* `pbx-main@sip.telnyx.com`
* `alice123@sip.telnyx.com`

Example invalid usernames:

* `123456@sip.telnyx.com` (starts with numeric character)

## Configuration

### Access control options

Configure SIP URI calling access using one of three modes:

| Mode         | Value          | Description                                                           | Use case                                                |
| ------------ | -------------- | --------------------------------------------------------------------- | ------------------------------------------------------- |
| Disabled     | `disabled`     | Blocks all SIP URI calls                                              | Default security posture                                |
| Unrestricted | `unrestricted` | Allows calls from anyone on the internet                              | Public-facing services, customer support lines          |
| Internal     | `internal`     | Allows calls only from SIP connections within the same Telnyx account | Private inter-office communication, internal extensions |

### Configure via API

[PATCH /v2/ip\_connections/](https://developers.telnyx.com/api-reference/ip-connections/update-an-ip-connection) with the `sip_uri_calling_preference` parameter:

```json theme={null}
{
  "sip_uri_calling_preference": "unrestricted"
}
```

Set to `disabled`, `unrestricted`, or `internal` based on security requirements.

## Making SIP URI calls

### From Telnyx SIP connections

Dial directly to the SIP URI from any registered SIP endpoint:

```
INVITE sip:username@sip.telnyx.com SIP/2.0
```

### From external systems

When configured as `unrestricted`, external SIP systems can place calls:

```
INVITE sip:username@sip.telnyx.com SIP/2.0
From: <sip:caller@external-domain.com>
```

## Receiving SIP URI calls

Configure the SIP endpoint to accept incoming calls:

1. Register the SIP device using the connection credentials
2. Enable SIP URI calling with the appropriate access control
3. Configure the dial plan or routing rules to handle incoming calls

The call will arrive with the From header containing the caller's SIP URI or phone number.

## Billing

### Identifiable sources

Calls from Telnyx SIP connections use standard rate deck pricing based on the originating connection's pricing plan.

### Unidentifiable sources

When SIP URI calling is set to `unrestricted`, calls from external or unidentifiable sources are billed at **\$0.002/minute** to the connection owner.

<Callout type="warning">
  Monitor usage when enabling unrestricted access to prevent unexpected charges from public internet traffic.

## Security considerations

1. **Username validation**: Non-numeric username requirements prevent unauthorized number spoofing
2. **Access control**: Use `internal` mode for private communications within the organization
3. **Rate monitoring**: Track call volumes and sources when using `unrestricted` mode
4. **Authentication**: Credential-based connections provide secure endpoint registration

## Troubleshooting

If SIP URI calls fail, verify:

1. SIP URI calling is enabled on the connection
2. Username begins with a non-numeric character
3. Access control mode permits the calling source
4. SIP endpoint is properly registered with valid credentials
5. Firewall rules allow SIP traffic to/from Telnyx infrastructure
