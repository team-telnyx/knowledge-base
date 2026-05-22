---
title: 'Telnyx SIP Trunking: Authentication Methods, Profiles, and Network Setup'
summary: 'A practical guide to setting up Telnyx SIP trunking: how SIP Connections
  and Outbound Voice Profiles fit together, which authentication methods to choose
  (credentials, IP + token, tech prefix, P-Charge-Info, FQDN), required firewall/ACL
  ports and webhook IPs to allowlist, and when to use UAC connections for Telnyx-initiated
  registration to your PBX.'
sources:
- url: https://developers.telnyx.com/docs/voice/sip-trunking/get-started/index
  content_hash: f4fedec981858f3636d6b8d0530d253de4c1d3235d1cb1be37356df98e80dc5d
- url: https://developers.telnyx.com/docs/voice/sip-trunking/authentication/credential-types/index
  content_hash: 25f86281a3ebea807cec851893cf7030defb54f199eab13e5102535bb29b60d8
- url: https://developers.telnyx.com/docs/voice/sip-trunking/authentication/ip-authentication-token
  content_hash: ed68d98852df597e3462bc4811ff65be7c2fff7af6c410e443b8023ab67f43db
- url: https://developers.telnyx.com/docs/voice/sip-trunking/authentication/tech-prefix
  content_hash: 44d59a75228319bf69146e4d7c46c3c99124f99feb785fa484c61781ed476119
- url: https://developers.telnyx.com/docs/voice/sip-trunking/network-configuration/ip-whitelisting/index
  content_hash: 57744e24d234bee6340a665ed812d3c4b67b357c9e55876023cf76dd9ded57ec
- url: https://developers.telnyx.com/docs/voice/uac-connections/index
  content_hash: 50f2704b77755ca0010c603c2122437c6786a27c53e89713fa7df0e3f2eb9835
updated_at: 2026-05-20T09:44:49Z
---

# Telnyx SIP Trunking: Authentication Methods, Profiles, and Network Setup

A practical guide to setting up Telnyx SIP trunking: how SIP Connections and Outbound Voice Profiles fit together, which authentication methods to choose (credentials, IP + token, tech prefix, P-Charge-Info, FQDN), required firewall/ACL ports and webhook IPs to allowlist, and when to use UAC connections for Telnyx-initiated registration to your PBX.

## How Telnyx SIP trunking is organized
- SIP Connections: authenticate traffic with Telnyx SIP proxies and define inbound call handling (assign numbers, choose Anchorsite PoP for media optimization).
- Outbound Voice Profiles (OVPs): control outbound routing, allowed destinations/service plan, rate limits, and daily spend caps; associate one or more SIP Connections to an OVP for outbound calls.

## Authentication methods at a glance
Choose based on your network and security posture:
- Credential-based (username/password registration): works with static or dynamic IPs; simple for many PBXs and SBCs.
- IP + Token (X-Telnyx-Token): for static IPs where multiple SIP Connections share the same IP; adds a unique token header for unambiguous routing and security.
- IP + Tech Prefix: for static IPs with multiple connections on one IP; PBX prepends a 4‑digit identifier to each dialed number.
- IP + P‑Charge‑Info header: authenticate/route using a Telnyx number in the P‑Charge‑Info SIP header; number must belong to the connection.
- FQDN-based inbound routing: route inbound traffic by hostname; combine with credentials or IP auth for outbound.

Dynamic IP note: Use credential-based (or FQDN + credentials) when your egress IP can change. IP-based methods require known static source IPs.

## IP Authentication Token (X‑Telnyx‑Token)
Use when multiple SIP Connections originate from the same source IP and you want token-enforced selection and authentication.
- Requirements:
  - Characters: a–z, A–Z, 0–9, hyphens only
  - Length: 12–48 characters
  - Scope: must be globally unique across all Telnyx connections
- SIP header to send on every outbound INVITE:
  - X-Telnyx-Token: your-token-value
- Authentication behavior:
  - Source IP matches AND token matches: accepted
  - Source IP matches but token missing/incorrect: rejected
  - Token matches but source IP mismatch: rejected
- Configuration: set the IP authentication token on the relevant IP-based SIP Connection and ensure your PBX/SBC inserts the header on all calls.

## Tech Prefix authentication
A Telnyx-assigned 4‑digit identifier prepended to the destination number to distinguish connections sharing an IP.
- Dial string: [tech_prefix][destination_number]
  - Example: 1234 + +18005678912 → 123418005678912
- Use cases: per-connection routing/billing, traffic separation when multiple trunks originate from one IP.
- PBX requirement: configure the trunk or dial plan to prepend the tech prefix on all outbound calls using that connection.
- Authentication behavior:
  - Correct prefix: call authenticated
  - Missing/incorrect prefix: 407 Proxy Authentication Required

## P‑Charge‑Info header authentication
Authenticate/route using a number you own on the connection.
- Header example (E.164 format required):
  - P-Charge-Info: <sip:+12125551234@sip.telnyx.com>
- The phone number must be assigned to the SIP Connection.

## FQDN‑based inbound routing
Route inbound traffic by hostname and pair with your preferred outbound auth:
- Inbound FQDN + Outbound credentials
- Inbound FQDN + Outbound IP authentication

## Outbound Voice Profiles
Use OVPs to govern how outbound calls are routed and controlled.
- Associate an OVP to your SIP Connection(s) for outbound.
- Configure allowed destinations/service plan and any applicable rate limits.
- Set daily spend limits to cap exposure.
- See also: [Outbound Voice Profiles for SIP trunking](outbound-voice-profiles-for-sip-trunking.md).

## Network and firewall requirements
Allow Telnyx signaling/media and webhook delivery through your firewall/ACLs.
- SIP signaling and media IPs, regional FQDNs, and codec details: see sip.telnyx.com (https://sip.telnyx.com)
- Port requirements:
  - SIP signaling: UDP/TCP 5060
  - SIP over TLS: TCP 5061
  - RTP media: UDP 16384–32768
  - Webhooks: TCP 443
- Consider anchoring media to a regional PoP for optimal jitter/latency (see [AnchorSite configuration](anchorsite-configuration.md)).

## Webhook source IPs to allowlist
Whitelist these CIDR blocks to receive webhooks (also applies to WebSocket streams).
- North America
  - US‑Central (CH1): 192.76.120.128/29
  - US‑East (DC2): 192.76.120.136/29
  - US‑West (SV1): 192.76.120.144/29
- Europe
  - London (LD6): 185.246.41.0/29
  - Frankfurt (FR5): 185.246.41.8/29
  - Amsterdam (AM6): 185.246.41.16/29
- Asia‑Pacific
  - Sydney (SY1): 103.115.244.0/29
  - Singapore (SG1): 103.115.244.8/29

## UAC SIP connections (Telnyx registers to your PBX)
Use a UAC (User Agent Client) Connection when you need Telnyx to register outbound to your PBX (e.g., your PBX can’t register to Telnyx or you want Telnyx to maintain registration).
- Creation: provide a connection name; credentials can be supplied or auto‑generated.
- External settings (Telnyx → your PBX):
  - proxy: SIP server your PBX exposes (e.g., sip:pbx.example.com:5060)
  - username/password: credentials Telnyx will use to register
  - transport: UDP, TCP, or TLS
- Internal settings (your PBX → Telnyx apps):
  - destination_uri format: <extension>@<applicationFQDN>.sip.telnyx.com
  - Examples:
    - 1006@assistant-abc123.sip.telnyx.com → AI Assistant instance abc123
    - 2000@cc-app-xyz789.sip.telnyx.com → Call Control app xyz789
- Management: list, fetch, update, and delete UAC connections via the Telnyx API.

## See also
- [SIP Trunking Overview](sip-trunking-overview.md)
- [SIP Authentication Methods](sip-authentication-methods.md)
- [IP Authentication Token](ip-authentication-token.md)
- [Tech Prefix Authentication](tech-prefix-authentication.md)
- [P-Charge-Info](p-charge-info.md)
- [IP Whitelisting](ip-whitelisting.md)
- [Failover & Retries](failover-retries.md)
- [Round Robin Routing](round-robin-routing.md)
- [Response Codes](response-codes.md)
