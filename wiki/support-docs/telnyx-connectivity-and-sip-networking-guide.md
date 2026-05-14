---
title: Telnyx Connectivity and SIP Networking Guide
summary: 'A practical guide to getting Telnyx voice and programmable services working
  reliably on your network: which IPs and FQDNs to whitelist, how SIP media and signaling
  traverse your firewall, DNS/SRV behavior, supported transports, NAT traversal with
  STUN/TURN, private AWS interconnects, SIP Connection failover, and inbound/outbound
  number formatting controls. Always consult https://sip.telnyx.com for the latest
  IP addresses.'
sources:
- url: https://support.telnyx.com/en/articles/1130687-whitelisting-telnyx-ip-addresses
- url: https://support.telnyx.com/en/articles/10007243-whitelisting-telnyx-media-ip-addresses
- url: https://support.telnyx.com/en/articles/10666839-how-telnyx-handles-srv-records-for-sip-calls
- url: https://support.telnyx.com/en/articles/1371411-aws-virtual-cross-connect-setup
- url: https://support.telnyx.com/en/articles/1176364-sip-connection-failover-guide-ip-fqdn-based
- url: https://support.telnyx.com/en/articles/1130682-telnyx-stun-and-turn-server
- url: https://support.telnyx.com/en/articles/1130705-sip-protocols-that-telnyx-uses
- url: https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats
updated_at: 2026-05-14T11:29:44Z
---

# Telnyx Connectivity and SIP Networking Guide

A practical guide to getting Telnyx voice and programmable services working reliably on your network: which IPs and FQDNs to whitelist, how SIP media and signaling traverse your firewall, DNS/SRV behavior, supported transports, NAT traversal with STUN/TURN, private AWS interconnects, SIP Connection failover, and inbound/outbound number formatting controls. Always consult https://sip.telnyx.com for the latest IP addresses.

## Why and how to whitelist Telnyx IPs
If your firewall or ACL restricts traffic, you must allow both SIP signaling and RTP media, as well as webhook/WebSocket delivery IPs used by Telnyx programmable services. For the most up-to-date addresses, refer to https://sip.telnyx.com (see the Media section and regional endpoints). Failure to permit new or updated ranges can cause call failures or one-way audio.

## SIP signaling endpoints by region
Whitelist the following location-specific SIP FQDNs and IPs (use FQDNs where possible for resiliency):
- US: sip.telnyx.com — Primary 192.76.120.10, Secondary 64.16.250.10
- Europe: sip.telnyx.eu — Primary 185.246.41.140, Secondary 185.246.41.141
- Australia: sip.telnyx.com.au — Primary 103.115.244.145, Secondary 103.115.244.146
- Canada: sip.telnyx.ca — Primary 192.76.120.31, Secondary 64.16.250.13

## Media IP address ranges
Voice media streams (RTP/RTCP) are delivered from distinct IP ranges. Allow the following to prevent one-way audio and dropped media:
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
Note: Telnyx periodically adds media ranges to enhance capacity and redundancy. If media IPs are not whitelisted, calls may connect but have no audio. Check https://sip.telnyx.com/#media for changes.

## Webhook and WebSocket delivery IPs
Programmable services (TeXML, Fax, Messaging, Call Control) deliver webhooks—and establish WebSocket streams—via these regional ranges:
- US
  - CH1 (US-Central): 192.76.120.128/29
  - DC2 (US-East): 192.76.120.136/29
  - SV1 (US-West): 192.76.120.144/29
- Europe
  - LD6 (London): 185.246.41.0/29
  - FR5 (Frankfurt): 185.246.41.8/29
  - AM6 (Amsterdam): 185.246.41.16/29
- APAC
  - SY1 (Sydney): 103.115.244.0/29
  - SG1 (Singapore): 103.115.244.8/29

## Network IP address pools by region
Main assignment pools and site slices (useful for broader ACLs):
- AMER
  - Main: 192.76.120.128/26, 192.76.120.192/27
  - CH1: 192.76.120.128/29
  - DC2: 192.76.120.136/29
  - SV1: 192.76.120.144/29
  - TR1 (Toronto): 192.76.120.160/29
- EMEA
  - Main: 185.246.41.0/26
  - LD6: 185.246.41.0/29
  - FR5: 185.246.41.8/29
  - AM6: 185.246.41.16/29
- APAC
  - Main: 103.115.244.0/26
  - SY1: 103.115.244.0/29
  - SG1: 103.115.244.8/29

## Supported SIP transport protocols
Telnyx supports SIP over UDP, TCP, and TLS. For security, encrypt signaling with TLS and media with SRTP/ZRTP where possible.

## SRV records: how Telnyx resolves and routes
When routing SIP to external FQDNs or when your Connection FQDNs use SRV, Telnyx resolves based on R-URI and transport:
- If the R-URI includes a port (e.g., sip:+1234567890@sip.example.com:5060), Telnyx performs an A-record lookup and bypasses SRV.
- If no port is present (e.g., sip:+1234567890@sip.example.com), Telnyx performs an SRV lookup for the appropriate transport. If no SRV exists, it falls back to A-record and uses the default SIP port (5060 for UDP/TCP, 5061 for TLS).
- On SRV failure with SIP 503, Telnyx attempts the next target by priority/weight.
Best practices:
- Omit explicit ports in dial strings to leverage SRV load balancing and failover.
- Ensure SRV targets resolve to valid A records globally.
- If resolution fails, calls may return SIP 478 (Unresolvable Destination).

## NAT traversal with Telnyx STUN/TURN
For endpoints behind NAT:
- STUN: stun.telnyx.com:3478 helps clients discover public IP/port for direct media paths.
- TURN: turn.telnyx.com:3478 relays media when direct paths fail; request TURN credentials from Telnyx Support.
These services reduce NAT-related issues and improve call setup and media reliability.

## Private interconnect: AWS Virtual Cross Connect
A Telnyx–AWS VXC provides private, direct connectivity that bypasses the public internet, reducing latency, jitter, and exposure.
Prerequisites: AWS VPC, your 12‑digit AWS account number, target AWS region, desired bandwidth, and network name.
High-level steps:
1) In the Telnyx Mission Control Portal, submit a New VXC request (account number, region, bandwidth, name). Telnyx provisions 1–2 Direct Connect links (allow 1–3 days).
2) In AWS, create and attach a Virtual Private Gateway (VGW) to your VPC.
3) In AWS Direct Connect, accept the pending connection(s).
4) Create a Private Virtual Interface per circuit using parameters provided by Telnyx (peer IPs, BGP ASN, BGP key).
5) Enable route propagation on your VPC route tables so Telnyx prefixes appear via the VGW.
Once routes are visible, test IP reachability over the VXC.

## SIP Connection failover (IP/FQDN-based)
Configure inbound authentication endpoints with ordered priority to achieve failover:
- In Mission Control: Voice > SIP Connections > Add SIP Connection (Type: IP or FQDN).
- Add multiple IPs/FQDNs in desired order (Primary → Secondary → Tertiary).
- Save. Telnyx will route to backup endpoints automatically if the primary is unreachable or fails to respond.
Recommendation: test failover regularly to validate behavior.

## Inbound and outbound number format controls
Inbound formatting is configurable per SIP Connection for DNIS (dialed number) and ANI (caller ID):
- +E.164 — includes + prefix
- E.164 — no + prefix
- National (10 digits) — local 10-digit format (country-dependent)
- SIP Username (DNIS only, credential-based Connections)
- +E.164 / National (10 digits) — ANI auto-selects based on domestic vs international origin
- E.164 / National (10 digits) — ANI auto-selects based on origin
Outbound dialing supports all formats and optional localization, enabling local dialing patterns and exit codes per country when configured.
Special note for WebRTC apps: on credential-based Connections you can set DNIS to SIP Username and enable VP8/VP9 codecs in advanced inbound settings to support video.

## Operational tips and troubleshooting
- Always verify current signaling and media ranges at https://sip.telnyx.com before updating firewalls.
- Whitelist both signaling and media IPs; missing media ranges commonly cause one-way audio.
- For webhook-driven apps or Call Control streams, permit the regional webhook/WebSocket source IPs.
- Use TLS + SRTP/ZRTP where possible; prefer FQDNs to benefit from DNS-based resiliency.
- To leverage SRV failover, omit ports in SIP URIs; validate SRV/A records are globally resolvable.
- Default SIP ports: 5060 (UDP/TCP), 5061 (TLS).
- Behind NAT, use Telnyx STUN/TURN to improve connectivity.
- For consistent performance and security, consider a private AWS VXC interconnect.
