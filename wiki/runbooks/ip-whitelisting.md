---
title: IP Whitelisting
summary: Firewall and ACL configuration for Telnyx SIP signaling, media transport, and webhook delivery.
sources:
  - url: https://developers.telnyx.com/docs/voice/sip-trunking/network-configuration/ip-whitelisting/index
    content_hash: 411395c0b3fb0e066bb4ac6f067d4eb79997c52568664915fbecdba8fe1d29fd
updated_at: 2026-04-10T00:00:00Z
---

# IP Whitelisting

Firewall and ACL configuration for Telnyx SIP signaling, media transport, and webhook delivery.

## SIP signaling and media

For current SIP signaling addresses, media IP ranges, supported codecs, and regional FQDNs, see [sip.telnyx.com](https://sip.telnyx.com).

## Port requirements

| Service             | Ports       | Protocol |
| ------------------- | ----------- | -------- |
| SIP signaling       | 5060        | UDP/TCP  |
| SIP signaling (TLS) | 5061        | TCP      |
| RTP media           | 16384-32768 | UDP      |
| Webhooks            | 443         | TCP      |

## Webhook IP addresses

Whitelist these CIDR blocks to receive webhook notifications.

### North America

| Region           | CIDR Block          |
| ---------------- | ------------------- |
| US-Central (CH1) | `192.76.120.128/29` |
| US-East (DC2)    | `192.76.120.136/29` |
| US-West (SV1)    | `192.76.120.144/29` |

### Europe

| Region          | CIDR Block         |
| --------------- | ------------------ |
| London (LD6)    | `185.246.41.0/29`  |
| Frankfurt (FR5) | `185.246.41.8/29`  |
| Amsterdam (AM6) | `185.246.41.16/29` |

### Asia-Pacific

| Region          | CIDR Block         |
| --------------- | ------------------ |
| Sydney (SY1)    | `103.115.244.0/29` |
| Singapore (SG1) | `103.115.244.8/29` |

These ranges also apply to WebSocket stream connections.
