---
title: Private Wireless Gateways
summary: Private Wireless Gateways (PWG) route all IoT SIM traffic through your own
  private network so devices live inside your IP space—not on the public internet.
  This page explains why and how to use PWG, architecture, setup, limits, how it compares
  to Public IPs, and related controls for access, monitoring, and voice features.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/private-wireless-gateways
  content_hash: b1d6c0c6e436050f2643149f815c3b89f0747b70de9e3ceb9397d6966b669d08
- url: https://developers.telnyx.com/docs/iot-sim/private-wireless-gateway-how-to/index
  content_hash: e6edc5c59aa7e3fb5a29725cb30d5d10e5f03df52494eb613d138e73802bd88c
- url: https://developers.telnyx.com/docs/iot-sim/public-ips/index
  content_hash: 28e1c919251b38a0ce9d5ae404f2879e312bff54cc74141ca71cfc28d5a4c8d1
- url: https://developers.telnyx.com/docs/iot-sim/mobile-phone-numbers/index
  content_hash: e860d2e4770c7a739277c16237ea3d21f62124eeaf59024552335fb0114ba091
- url: https://developers.telnyx.com/docs/iot-sim/wireless-blocklists
  content_hash: 12675d7d445bace0a4159ab804c845f29b5c1957159dfdefbe91866347dd60f4
- url: https://developers.telnyx.com/docs/iot-sim/wireless-detail-records
  content_hash: 3a759c1b08155ad57278e24f9dd76bf9db982ab60bc5620f2430d52d1b180c83
- url: https://developers.telnyx.com/docs/iot-sim/call-forwarding-recording
  content_hash: c92538102d3053cfd1663283512a1498ccb7bcc4efe553e1aab827546e82307d
updated_at: 2026-05-20T08:39:23Z
---

# Private Wireless Gateways

Private Wireless Gateways (PWG) route all IoT SIM traffic through your own private network so devices live inside your IP space—not on the public internet. This page explains why and how to use PWG, architecture, setup, limits, how it compares to Public IPs, and related controls for access, monitoring, and voice features.

## Overview and benefits
A Private Wireless Gateway routes SIM data through a private VRF so your devices are addressed on your corporate network. Benefits:
- Security: devices aren’t directly exposed to the internet
- Control: route through your firewall/DLP and define egress
- Direct access: address devices like any internal host

## Network architecture
PWGs terminate into a VRF on Telnyx’s MPLS backbone. You bridge that VRF to your network using either:
- Virtual Cross Connect (VXC), or
- Cloud VPN (WireGuard interface)

All interfaces bound to the same VRF can reach each other.

## IP assignment via APNs
- data.net: Static IP per device (persists across sessions)
- data00.telnyx: Dynamic IP (new each session)
Devices must connect with the appropriate APN to receive the desired assignment.

## Setup workflow in Mission Control
1) Set up Cloud VPN
- Create a Network, then add a VPN Interface and a Peer; store the generated private key. Buying a global IP is optional.

2) Create and attach a PWG
- In Wireless, create a PWG Interface, name it, and select the same Network and Region as the VPN interface; accept the MRC. Wait for Provisioned.
- Create a SIM Card Group, then Connect PWG to that group. Add SIMs to the group (individually or bulk). All SIMs in the group route via the PWG.

3) Configure routing
- The network default gateway for the VRF must be configured by Telnyx Network manually; contact support via the Mission Control Portal chat.
- Once set, you can control which destinations are reachable from devices. See also [Traffic Policy Profiles](traffic-policy-profiles.md) and [Private Gateway Setup](private-gateway-setup.md).

## PWG API endpoints
- List: GET `/private_wireless_gateways`
- Create: POST `/private_wireless_gateways`
- Retrieve: GET `/private_wireless_gateways/{id}`
- Delete: DELETE `/private_wireless_gateways/{id}`
Assign a PWG to SIMs by attaching it to a SIM Card Group via group actions (see [SIM Card Groups](sim-card-groups.md)).

## Limits and region availability
- Region: currently available in Ashburn, VA (more regions coming)
- IP range: default `100.64.199.0/24` (~254 concurrent SIMs); custom ranges coming
- Internet access: disabled by default; contact support to open the VRF to the internet if needed

## PWG vs. Public IPs
By default, SIMs receive dynamic private IPs with outbound-only reachability. Public IPs assign a static, internet-routable IP to a SIM (billed per SIM) so you can initiate inbound connections. Use cases for Public IPs include inbound management (SSH, device-as-server) and firewall allowlists. PWG instead keeps traffic private and steers it through your network. Choose based on whether you need direct internet exposure or a private routed path. See [Public IPs](public-ips.md).

## Network access control with Wireless Blocklists
Restrict where SIMs can attach by assigning a blocklist to a SIM Card Group (applies to all SIMs in the group):
- country (ISO code, e.g., US, CN, RU) — geo-fencing
- mcc (e.g., 310 US, 234 UK) — block all carriers in a country
- plmn (MCC+MNC, e.g., 31026) — block a specific carrier
One blocklist per group; changes take effect immediately. Common patterns: geo-fencing, carrier avoidance, and security lockdown. Combining blocklists with PWG yields a tightly controlled connectivity path. See [Wireless Blocklists](wireless-blocklists.md).

## Monitoring and usage visibility
Wireless Detail Records (WDRs) provide per-session data (start/stop times, bytes, RAT, MCC/MNC, APN, IPs, cell ID).
- Create report: POST `/wireless/detail/records/reports` with a start_time and end_time
- Poll status: GET `/wireless/detail/records/reports/{id}` until complete
- Download: use the returned pre-signed report_url
For real-time visibility on a SIM, use connectivity logs: GET `/sim_cards/{id}/wireless_connectivity_logs` (shows recent sessions, IMSI/IMEI, radio tech, connection state). See [Wireless Detail Records](wireless-detail-records.md).

## Voice on IoT SIMs: numbers, connections, and call features
If you enable voice on a SIM, Telnyx assigns a real +E.164 Mobile Phone Number; inbound calls ring the device and outbound calls present that number.
- Enable/disable per SIM: POST `/sim_cards/{id}/actions/enable_voice` (optionally include `connection_id`), and `/sim_cards/{id}/actions/disable_voice`; bulk variants available
- Manage numbers: GET `/mobile_phone_numbers`, GET `/mobile_phone_numbers/{id}`, PATCH `/mobile_phone_numbers/{id}`
Configurable number settings include `call_forwarding`, `call_recording`, `caller_id_name_enabled`, `cnam_listing`, `noise_suppression`, `inbound_call_screening`, `connection_id`, `customer_reference`, `tags`, and directional routing (`inbound`/`outbound`).
Mobile Voice Connections define application behavior (webhooks, routing, API version): list/create/retrieve/update/delete via `/mobile_voice_connections` endpoints. See [Mobile Phone Numbers](mobile-phone-numbers.md).

Call features (configured via PATCH `/mobile_phone_numbers/{id}`):
- Call Forwarding: unconditional, no_answer (with timeout), busy — forward to PSTN, SIP, or an application
- Call Recording: record inbound, outbound, or both; recordings use the standard Telnyx Recordings API
- Inbound Call Screening: free feature assessing number reputation, number validity, and SHAKEN/STIR attestation
  - Modes: Flag (connects with spam indicator headers) or Reject (blocked at network)
  - Enable in the portal or via `inbound_call_screening` on the number; webhook payloads include `call_screening_result`
  - Reputation applies to US/CA; SHAKEN/STIR applies in North America
See [Call Forwarding, Recording & Screening](call-forwarding-recording-screening.md).
