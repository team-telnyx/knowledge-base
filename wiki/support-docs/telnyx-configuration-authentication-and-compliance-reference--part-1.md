---
title: Telnyx Configuration, Authentication, and Compliance Reference
summary: This page consolidates Telnyx support guidance on whitelisting SIP signaling,
  media, and webhook IP addresses; IP authentication methods (tech prefix, X-Telnyx-Token,
  P-Charge-Info) including FreePBX configuration; multi-device registration limits;
  AI Assistant configuration with tools, handoffs, transfers, and MCP servers; UK
  TPS compliance for marketing calls; and the public Knowledge Agent bot-to-bot support
  API.
sources:
- url: https://support.telnyx.com/en/articles/10007243-whitelisting-telnyx-media-ip-addresses
- url: https://support.telnyx.com/en/articles/1130687-whitelisting-telnyx-ip-addresses
- url: https://support.telnyx.com/en/articles/1130715-register-multiple-devices-on-one-connection
- url: https://support.telnyx.com/en/articles/12232444-comprehensive-ai-assistants-configuration-walk-through
- url: https://support.telnyx.com/en/articles/12580765-configure-p-charge-info-for-private-pbx-example-freepbx
- url: https://support.telnyx.com/en/articles/12580952-configure-token-authentication-header-x-telnyx-token-in-freepbx
- url: https://support.telnyx.com/en/articles/15455646-bot-to-bot-support-api-ask-telnyx-knowledge-agent
- url: https://support.telnyx.com/en/articles/2602782-ip-authentication-with-tech-prefix
- url: https://support.telnyx.com/en/articles/4860170-ip-authentication-with-x-telnyx-token
- url: https://support.telnyx.com/en/articles/6136385-uk-tps-register-guidelines
- url: https://support.telnyx.com/en/collections/133094-general-telnyx-portal-account
- url: https://support.telnyx.com/en/collections/19623087-ai-assistant
updated_at: 2026-07-17T08:59:35Z
---

# Telnyx Configuration, Authentication, and Compliance Reference

*Part 1 of 4 — see also: [Part 2](telnyx-configuration-authentication-and-compliance-reference--part-2.md), [Part 3](telnyx-configuration-authentication-and-compliance-reference--part-3.md), [Part 4](telnyx-configuration-authentication-and-compliance-reference--part-4.md)*

This page consolidates Telnyx support guidance on whitelisting SIP signaling, media, and webhook IP addresses; IP authentication methods (tech prefix, X-Telnyx-Token, P-Charge-Info) including FreePBX configuration; multi-device registration limits; AI Assistant configuration with tools, handoffs, transfers, and MCP servers; UK TPS compliance for marketing calls; and the public Knowledge Agent bot-to-bot support API.

## Overview

Telnyx provides a range of SIP, voice, and AI services that require careful network and authentication configuration. This page consolidates guidance on whitelisting Telnyx IP addresses, IP authentication methods (tech prefix, X-Telnyx-Token, P-Charge-Info), multi-device registration, AI Assistant configuration, regulatory compliance (UK TPS), and the public Knowledge Agent support API.

## Whitelisting Telnyx IP Addresses

To ensure uninterrupted service, keep your firewall and security settings updated to allow traffic from Telnyx's media and signaling IP addresses. This is especially important if your network restricts inbound or outbound traffic based on IP ranges.

### SIP Signaling and Media Servers

If your network uses a firewall or ACL, add both Telnyx media and SIP signaling IP addresses to your firewall's whitelist. For the most up-to-date IP addresses, refer to [Telnyx IP Addresses](https://sip.telnyx.com).

### What are SIP Media IP Addresses?

[SIP (Session Initiation Protocol)](https://telnyx.com/resources/sip-trunking-explained) media IP addresses are the public IPs used to handle the actual audio (media) streams of a VoIP call. While SIP signaling (call setup, teardown, etc.) occurs over one set of IPs, the media stream — the voice conversation — occurs over a different range of IP addresses. Whitelisting these media stream IPs ensures that voice data packets are not blocked by your firewall.

The most up-to-date list of Telnyx media IP addresses is available at <https://sip.telnyx.com/#media>.

### Media IP Ranges

Whitelist the following media IP ranges to ensure uninterrupted media delivery:

- 36.255.198.128/25
- 50.114.136.128/25
- 50.114.144.0/21
- 64.16.226.0/24
- 64.16.227.0/24
- 64.16.228.0/24
- 64.16.229.0/24
- 64.16.230.0/24
- 64.16.248.0/24
- 64.16.249.0/24
- 103.115.244.128/25
- 185.246.41.128/25

### Network IP Address Assignments by Region

**AMER (North America)**

- Main Pools: 192.76.120.128/26 & 192.76.120.192/27
  - CH1 - US Central: 192.76.120.128/29
  - DC2 - US East: 192.76.120.136/29
  - SV1 - US West: 192.76.120.144/29
  - TR1 - Toronto: 192.76.120.160/29

**EMEA (Europe, Middle East, Africa)**

- Main Pool: 185.246.41.0/26
  - LD6 - London: 185.246.41.0/29
  - FR5 - Frankfurt: 185.246.41.8/29
  - AM6 - Amsterdam: 185.246.41.16/29

**APAC (Asia-Pacific)**

- Main Pool: 103.115.244.0/26
  - SY1 - Sydney: 103.115.244.0/29
  - SG1 - Singapore: 103.115.244.8/29

### Region-Specific SIP FQDNs and IPs

| Region | FQDN | Primary IP | Secondary IP |
| --- | --- | --- | --- |
| US | sip.telnyx.com | 192.76.120.10 | 64.16.250.10 |
| Europe | sip.telnyx.eu | 185.246.41.140 | 185.246.41.141 |
| Australia | sip.telnyx.com.au | 103.115.244.145 | 103.115.244.146 |
| Canada | sip.telnyx.ca | 192.76.120.31 | 64.16.250.13 |

### Webhook Delivery IPs

Telnyx programmable services — including TeXML, Fax, Messaging, and Call Control — deliver webhooks from the following regional IPs. These IPs also apply to WebSocket stream connections (typically initiated using the Dial and Start Stream APIs).

- **US**
  - CH1 (US-Central): 192.76.120.128/29
  - DC2 (US-East): 192.76.120.136/29
  - SV1 (US-West): 192.76.120.144/29
- **Europe**
  - LD6 (London, UK): 185.246.41.0/29
  - FR5 (Frankfurt, DE): 185.246.41.8/29
  - AM6 (Amsterdam, NL): 185.246.41.16/29
- **Asia-Pacific (APAC)**
  - SY1 (Sydney): 103.115.244.0/29
  - SG1 (Singapore): 103.115.244.8/29

### Why Telnyx Adds New Media IPs

Telnyx continuously expands its network to improve performance and redundancy. Adding new media IP ranges enhances the ability to provide seamless voice services, ensuring better connectivity and service quality during periods of high demand or network maintenance.

### Risk of Not Updating Firewalls

Without updating your firewall to allow traffic from new media IPs, voice service could be interrupted. Calls routed through the new IP range may be blocked for media, resulting in One Way Audio (OWA). Whitelisting the new IP addresses guarantees that voice traffic is allowed, keeping communication services running smoothly.
