---
title: Telnyx Network, Webhook, and Push Notification Configuration
summary: This page consolidates Telnyx guidance on whitelisting SIP signaling, media,
  and webhook IP addresses; configuring and verifying webhooks (including signature
  rotation); setting up iOS and Android push notifications for the WebRTC SDK; and
  accessing support resources such as the status page, bug reporting, and the Bot-to-Bot
  Knowledge Agent API.
sources:
- url: https://support.telnyx.com/en/articles/10007243-whitelisting-telnyx-media-ip-addresses
- url: https://support.telnyx.com/en/articles/1130687-whitelisting-telnyx-ip-addresses
- url: https://support.telnyx.com/en/articles/15455646-bot-to-bot-support-api-ask-telnyx-knowledge-agent
- url: https://support.telnyx.com/en/articles/4283906-bug-reports-guide
- url: https://support.telnyx.com/en/articles/4334722-how-to-leverage-webhooks
- url: https://support.telnyx.com/en/articles/6707731-telnyx-status-page
- url: https://support.telnyx.com/en/articles/8268140-android-push-notification-setup
- url: https://support.telnyx.com/en/articles/8268170-how-to-setup-ios-push-notifications
- url: https://support.telnyx.com/en/articles/8370064-update-webhook-sign-key-guide
- url: https://support.telnyx.com/en/collections/133094-general-telnyx-portal-account
- url: https://support.telnyx.com/en/collections/5782829-webrtc-voice-sdk
updated_at: 2026-08-05T13:24:23Z
---

# Telnyx Network, Webhook, and Push Notification Configuration

*Part 1 of 5 — see also: [Part 2](telnyx-network-webhook-and-push-notification-configuration--part-2.md), [Part 3](telnyx-network-webhook-and-push-notification-configuration--part-3.md), [Part 4](telnyx-network-webhook-and-push-notification-configuration--part-4.md), [Part 5](telnyx-network-webhook-and-push-notification-configuration--part-5.md)*

This page consolidates Telnyx guidance on whitelisting SIP signaling, media, and webhook IP addresses; configuring and verifying webhooks (including signature rotation); setting up iOS and Android push notifications for the WebRTC SDK; and accessing support resources such as the status page, bug reporting, and the Bot-to-Bot Knowledge Agent API.

## Overview

Telnyx operates a global communications platform that exposes SIP signaling, media, webhook delivery, and WebRTC mobile SDK endpoints from a set of regional IP ranges. To keep services running reliably, customers must whitelist the appropriate Telnyx IP ranges in their firewalls and ACLs, configure webhook endpoints to acknowledge events quickly, and (for mobile WebRTC clients) provision platform-specific push credentials. This page consolidates the IP whitelisting, webhook, push notification, and support resources needed to operate Telnyx services.

## Whitelisting Telnyx IP Addresses

To ensure optimal performance of Telnyx services, customers should whitelist Telnyx IP addresses by region and purpose. If your network uses a firewall or ACL, add both the media and SIP signaling IP addresses to your firewall's whitelist. For the most up-to-date IP addresses, refer to [Telnyx IP Addresses](https://sip.telnyx.com).

### SIP Signaling and Media Servers

SIP signaling (call setup, teardown, etc.) occurs over one set of IPs, while the media stream (the voice conversation) occurs over a different range of IP addresses. Both must be allowed through the firewall.

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

### Media IP Addresses

To ensure uninterrupted media delivery, whitelist the following media IP ranges:

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

The most current list is maintained at <https://sip.telnyx.com/#media>. Telnyx continuously expands its network to improve performance and redundancy, so new media IP ranges may be introduced over time. Failure to whitelist new IPs can lead to service disruptions, including One Way Audio (OWA), because the system may block voice traffic.

### Region-Specific SIP FQDNs and IP Addresses

For location-specific SIP connections, whitelist the following FQDNs and IPs:

| Region | FQDN | Primary IP Address | Secondary IP Address |
| --- | --- | --- | --- |
| US | sip.telnyx.com | 192.76.120.10 | 64.16.250.10 |
| Europe | sip.telnyx.eu | 185.246.41.140 | 185.246.41.141 |
| Australia | sip.telnyx.com.au | 103.115.244.145 | 103.115.244.146 |
| Canada | sip.telnyx.ca | 192.76.120.31 | 64.16.250.13 |
