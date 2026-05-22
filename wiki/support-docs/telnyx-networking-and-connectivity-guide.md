---
title: Telnyx Networking and Connectivity Guide
summary: 'A single reference for building private, secure, and resilient network paths
  to Telnyx: required IP whitelisting for SIP/media and webhooks, NAT traversal with
  STUN/TURN, private interconnects (VXC) for AWS/Azure/GCP and Megaport, plus Telnyx
  Global Edge Router setup and best practices.'
sources:
- url: https://support.telnyx.com/en/articles/10007243-whitelisting-telnyx-media-ip-addresses
  content_hash: 0eb0936b375412c628f7f735150fd40d2dfb0312e29264d11fe29d29aed75898
- url: https://support.telnyx.com/en/articles/1130682-telnyx-stun-and-turn-server
  content_hash: 1cd0314b9b936f524b5a5c4c970ec44fadc709d0dd19cea88383153bc680ef72
- url: https://support.telnyx.com/en/articles/1130687-whitelisting-telnyx-ip-addresses
  content_hash: 71e9e1af6659418862cc205553a3921dfa4d63b3c23886b7d7f48e9f7779ea7e
- url: https://support.telnyx.com/en/articles/1371411-aws-virtual-cross-connect-setup
  content_hash: c388836c115f095ebcdab284c8855957ff84c2e2f2e283e5c7ae944cb7902ecd
- url: https://support.telnyx.com/en/articles/2239446-azure-virtual-cross-connect
  content_hash: c13e4e8b297a01107490aed529df6e9dde481201cf8c6974b3de46ba8a57da1b
- url: https://support.telnyx.com/en/articles/2239449-google-vpc-telnyx-integration
  content_hash: 025c57c59f880c77c3d8c632d4e59acaf6fd5439e0875fc9f64ce1541bb03ab1
- url: https://support.telnyx.com/en/articles/2964210-megaport-configuration-with-telnyx
  content_hash: 3352b1a8a051e721dd051afb1c7bebf776fb411b84612900c0c4d7eab2bb1bdf
- url: https://support.telnyx.com/en/articles/8002565-how-to-configure-global-edge-router-with-telnyx
  content_hash: 242f743d1c29464428ed6fd057c87935eacbc2c9070f3199052104f3b293d705
- url: https://support.telnyx.com/en/articles/8103257-global-ip-edge-routing
  content_hash: 5eae451813916c2239a71ac12056626f757820e7e992a7ad7f929c2f0e48c5e7
- url: https://support.telnyx.com/en/articles/8126141-intro-to-telnyx-edge-router
  content_hash: 1cf44ddc0f2f9ba9e78881cbfc6a51544651e87f2ad46710954012e3ecc6cdbb
- url: https://support.telnyx.com/en/collections/5317581-networking-using-telnyx
  content_hash: 0af3ca0db429c4473c803b0d3607b608fb5c077ad33f20ff1ff987de0e9b94df
updated_at: 2026-05-20T15:20:29Z
---

# Telnyx Networking and Connectivity Guide

A single reference for building private, secure, and resilient network paths to Telnyx: required IP whitelisting for SIP/media and webhooks, NAT traversal with STUN/TURN, private interconnects (VXC) for AWS/Azure/GCP and Megaport, plus Telnyx Global Edge Router setup and best practices.

## Keep voice flowing: IP whitelisting and endpoints
To avoid call failures and one-way audio, keep firewalls/ACLs current for both SIP signaling and RTP media. Telnyx periodically adds media IPs as the network scales; update rules whenever ranges change.

- Where to find live IPs
  - For the most up-to-date SIP signaling and media info, consult https://sip.telnyx.com (media section: https://sip.telnyx.com/#media).

- Media IP ranges (whitelist all):
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

- Region-specific SIP FQDNs and IPs (use FQDNs where possible; IPs for ACLs/failover):
  - US: sip.telnyx.com → Primary 192.76.120.10, Secondary 64.16.250.10
  - Europe: sip.telnyx.eu → Primary 185.246.41.140, Secondary 185.246.41.141
  - Australia: sip.telnyx.com.au → Primary 103.115.244.145, Secondary 103.115.244.146
  - Canada: sip.telnyx.ca → Primary 192.76.120.31, Secondary 64.16.250.13

- Webhook and WebSocket delivery IPs (for TeXML, Fax, Messaging, Call Control webhooks and WebSocket streams initiated by Dial/Start Stream APIs):
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

- Network IP address assignments by region (for planning/allow-listing):
  - AMER main pools: 192.76.120.128/26, 192.76.120.192/27
    - CH1 192.76.120.128/29, DC2 192.76.120.136/29, SV1 192.76.120.144/29, TR1 192.76.120.160/29
  - EMEA main pool: 185.246.41.0/26
    - LD6 185.246.41.0/29, FR5 185.246.41.8/29, AM6 185.246.41.16/29
  - APAC main pool: 103.115.244.0/26
    - SY1 103.115.244.0/29, SG1 103.115.244.8/29

- What happens if you don’t update ACLs?
  - New media paths may be blocked, causing media failures like One Way Audio (OWA). Keep rules aligned with the ranges above and monitor https://sip.telnyx.com for updates.

## NAT traversal: Telnyx STUN and TURN
- STUN server: stun.telnyx.com:3478 (helps clients discover their public IP/port behind NAT for direct RTP paths).
- TURN server: turn.telnyx.com:3478 (relays media when direct paths fail). Request username/password from Telnyx Support.
- When to use:
  - Prefer STUN for symmetric performance; fall back to TURN for restrictive NATs/firewalls to ensure call media reliability.

## Private interconnect with Telnyx (Virtual Cross Connect)
A Virtual Cross Connect (VXC) gives you private, direct connectivity between your cloud VPC/VNet and Telnyx, bypassing the public internet to reduce hops, jitter, and exposure. For SIP workloads over VXC, encrypt signaling/media with TLS & Z/SRTP to mitigate man-in-the-middle risk. See: https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication

### AWS Direct Connect via VXC (summary)
- Prerequisites: AWS VPC; 12‑digit AWS account number; AWS region; requested bandwidth; network name.
- Step 1: In Mission Control → Networking, create a new VXC and submit preferences (Telnyx provisions 1–2 Direct Connect connections; allow 1–3 days).
- Step 2: In AWS, create and attach a Virtual Private Gateway (VGW) to your VPC.
- Step 3: Accept the pending Direct Connect connection(s) in AWS.
- Step 4: Create a Private Virtual Interface per circuit. Use peer IPs, BGP ASN, and auth key provided by Telnyx Support.
- Step 5: Enable route propagation on your VPC route tables so Telnyx prefixes populate automatically.

### Azure ExpressRoute via VXC (summary)
- Step 1: In Azure Portal, create an ExpressRoute circuit. Provider must be Equinix (do not enable Classic operations). Microsoft ASN is typically 12076.
- Step 2: In Mission Control → Networking, create a Network and Site, then Create VXC. Enter your Azure Service Key and ASN. Submit to Telnyx Network team.
- Important: Do not enable routing until coordinated with Telnyx; premature enablement can blackhole voice traffic.
- Step 3: In a maintenance window with Telnyx, turn up routing and confirm Telnyx public ranges are preferred via ExpressRoute.

### Google Cloud Partner Interconnect via VXC (summary)
- Prerequisites: GCP VPC in the same region you’ll interconnect.
- Step 1: In GCP, create Partner Interconnect VLAN attachments (redundant pair recommended). Copy pairing key(s).
- Step 2: In Mission Control → Networking, Create VXC for Google Cloud. Provide primary (and optional secondary) pairing keys; choose bandwidth.
- Step 3: In GCP, Activate each VLAN attachment and Configure BGP. Use Telnyx peer ASN 63440. Copy Cloud Router IPs.
- Step 4: In Telnyx, supply the Cloud Router IPs, await order approval, then Enable routing (brief traffic disruption as routes shift from internet to private VXC). Ensure cloud hosts have appropriate public IPs configured to receive Telnyx traffic as advised.

### Megaport with Telnyx (summary)
- In Megaport: +Connection → Enter Service Key (from Telnyx) → confirm populated details.
- Set: connection name, rate limit, and unique A-End VLAN (2–4093). Add VXC to cart and place Order.
- Telnyx approves the request, establishing the private VXC between your Megaport and Telnyx environments.

## Telnyx Global Edge Router and Global IP
Global Edge Router uses WireGuard-based Cloud VPN at 25+ PoPs with BGP Anycast to advertise a single Global IP for your services. Benefits include instant failover, multi-cloud/hybrid flexibility, and reduced egress-related costs.

- Quick start (WireGuard):
  - Create a Network in Mission Control.
  - Cloud VPN → Create WireGuard interface (choose region/network) and wait to provision.
  - Add a WireGuard Peer; copy the returned private key.
  - Acquire a Global IP, then assign the WireGuard Peer to it.
  - Apply the rendered WireGuard config (private key, allowed IPs, endpoint) to your VM/device to bring the tunnel up.

- Important availability note
  - As of October 16, 2025, “Global IP for customers is currently disabled” with no near-term plan to re-enable. Check your portal and contact Telnyx Support for current status and alternatives.

- Typical uses
  - Multi-cloud or hybrid failover and migrations; M&A platform meshing; consolidating siloed lines of business; IoT backhaul control using Telnyx wireless; mid-market cost control with resilient performance.

- Pricing model
  - Flat monthly charge by bandwidth tier with no data caps. See https://telnyx.com/pricing/global-edge-router for current pricing.

## Best practices and operational tips
- Security
  - Encrypt SIP signaling via TLS and media via SRTP or ZRTP (Z/SRTP) when possible.
  - Restrict by region where feasible and keep ACLs aligned with the media, webhook, and regional IPs listed above.
- Change management
  - For Azure and other route turn-ups, coordinate maintenance with Telnyx Network Engineering to prevent traffic blackholes.
  - Expect a brief disruption when shifting traffic from internet to private interconnects.
- NAT traversal
  - Prefer STUN; fall back to TURN with Telnyx credentials when direct media paths fail.
- Source of truth
  - Re-verify ranges and endpoints at https://sip.telnyx.com (especially before firewall changes or scheduled upgrades).
- Support
  - For TURN credentials, VXC provisioning details (BGP ASN/keys/peer IPs), or Global Edge Router status, contact Telnyx Support.
