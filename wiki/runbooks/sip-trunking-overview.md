---
title: SIP Trunking Overview
summary: Telnyx SIP trunking uses **SIP Connections** for inbound traffic and authentication, and **Outbound Voice Profiles** for outbound call routing.
sources:
  - url: https://developers.telnyx.com/docs/voice/sip-trunking/get-started/index
    content_hash: 2cdfaa6273a18dd9ccf96743d3f712328744c6383dd7eb5a56615be0d755cb1b
updated_at: 2026-04-10T00:00:00Z
---

# SIP Trunking Overview

Telnyx SIP trunking uses **SIP Connections** for inbound traffic and authentication, and **Outbound Voice Profiles** for outbound call routing.

## SIP Connections

SIP connections authenticate traffic with Telnyx SIP proxies and configure inbound call handling.

| Component      | Description                                   |
| -------------- | --------------------------------------------- |
| Authentication | Credentials, IP address, or FQDN-based        |
| Anchorsite     | Regional PoP selection for media optimization |
| Phone numbers  | Assigned to connection for inbound routing    |

See [Authentication Methods](sip-authentication-methods.md) for configuration details.

## Outbound Voice Profiles

Outbound voice profiles control outbound call routing, destinations, and spending limits.

| Component         | Description                              |
| ----------------- | ---------------------------------------- |
| SIP Connection    | Associated connection for outbound calls |
| Service plan      | Allowed destinations and rate limits     |
| Daily spend limit | Maximum daily spend cap                  |

## Network configuration

For SIP signaling addresses, media IP ranges, and port requirements, see [sip.telnyx.com](https://sip.telnyx.com).

## Related pages

* [Authentication Methods](sip-authentication-methods.md)
* [IP Whitelisting](ip-whitelisting.md)
* [Routing Configuration](failover-and-retries.md)
