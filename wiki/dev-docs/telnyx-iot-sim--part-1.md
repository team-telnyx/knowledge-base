---
title: Telnyx IoT SIM
summary: Telnyx IoT SIMs provide global cellular connectivity for IoT devices with
  support for physical SIMs and eSIMs, fleet management through SIM Card Groups, private
  networking via Private Wireless Gateways, public static IPs, voice capabilities,
  and over-the-air updates. This page covers ordering, configuration, networking options,
  and device-specific setup guides.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/mikrotik-wap-lte
- url: https://developers.telnyx.com/docs/iot-sim/mobile-phone-numbers/index
- url: https://developers.telnyx.com/docs/iot-sim/nordic-semiconductor
- url: https://developers.telnyx.com/docs/iot-sim/ordering-sims/index
- url: https://developers.telnyx.com/docs/iot-sim/ota-updates
- url: https://developers.telnyx.com/docs/iot-sim/particle-boron-lte-kit
- url: https://developers.telnyx.com/docs/iot-sim/pepwave-max-br1-mini-lte
- url: https://developers.telnyx.com/docs/iot-sim/private-wireless-gateway-how-to/index
- url: https://developers.telnyx.com/docs/iot-sim/private-wireless-gateways
- url: https://developers.telnyx.com/docs/iot-sim/public-ips/index
- url: https://developers.telnyx.com/docs/iot-sim/sim-card-groups/index
updated_at: 2026-06-11T10:33:18Z
---

# Telnyx IoT SIM

*Part 1 of 3 — see also: [Part 2](telnyx-iot-sim--part-2.md), [Part 3](telnyx-iot-sim--part-3.md)*

Telnyx IoT SIMs provide global cellular connectivity for IoT devices with support for physical SIMs and eSIMs, fleet management through SIM Card Groups, private networking via Private Wireless Gateways, public static IPs, voice capabilities, and over-the-air updates. This page covers ordering, configuration, networking options, and device-specific setup guides.

## Getting SIMs

### Physical SIMs

Physical SIM orders go through [Mission Control](https://portal.telnyx.com/#/wireless/buy-sim-cards) — they cannot be ordered via API. Set quantity, add to cart, and check out. Telnyx ships triple-cut SIM cards (2FF/3FF/4FF) to your address.

Each physical SIM has a 10-digit registration code printed on the card. Register via the portal (manual or CSV) or the API (`POST /actions/register/sim_cards`). During registration you assign a SIM Card Group and optional tags. Once registered, activate the SIM on the network via `POST /sim_cards/{id}/actions/enable` or the portal.

### eSIMs

eSIMs are downloadable SIM profiles for consumer devices (phones, tablets, laptops) — not embedded SIM hardware. For eUICC hardware solutions, contact [Telnyx Sales](https://telnyx.com/contact-us).

Purchase through the portal or the API (`POST /actions/purchase/esims`). Portal purchases let you set quantity, assign a SIM Card Group, choose initial status, and add tags. There is a $0.70 activation fee per eSIM and no cart — purchase is immediate. Either way, you receive an activation code immediately. Provide it to the device via QR code or direct input for OTA provisioning. No shipping or registration step is required.

eSIM activation codes are one-time use. If the device loses the profile, you need a new eSIM purchase — you cannot re-download the same profile. After provisioning, eSIMs become the same SIM Card resource as physical SIMs; all API operations are identical.

## SIM Card Groups

Every SIM belongs to a group and inherits its settings. Set policy on the group instead of updating SIMs individually. Groups are ongoing policy — a SIM inherits its group's settings as long as it is a member. Bulk operations, by contrast, are one-time actions on an explicit list of SIMs.

Every account has a default group. SIMs that are not explicitly assigned land here. Deleting a group moves its SIMs back to the default group. Moving SIMs between groups after they are active can briefly interrupt connectivity.

### Group Settings

Configurable via `PATCH /sim_card_groups/{id}`:

| Setting | Description |
| --- | --- |
| `name` | Display name for the group |
| `data_limit` | Data cap (`amount` + `unit`). SIMs exceeding this enter `data_limit_exceeded` until the limit is raised or the billing cycle resets |

### Group Actions

Group actions are asynchronous — each returns an action ID. Track progress via `GET /sim_card_group_actions`.

| Action |
| --- |
| Assign Private Wireless Gateway |
| Remove Private Wireless Gateway |
| Assign Wireless Blocklist |
| Remove Wireless Blocklist |

## Public IPs

By default, SIMs get dynamic private IPs — reachable outbound only. A public static IP makes the SIM reachable from the internet at $3/mo per SIM.

| Action | Endpoint |
| --- | --- |
| Get Public IP | `GET /sim_cards/{id}/public_ip` |
| Set Public IP | `POST /sim_cards/{id}/actions/set_public_ip` |
| Remove Public IP | `POST /sim_cards/{id}/actions/remove_public_ip` |
| Bulk Set Public IPs | `POST /sim_cards/actions/bulk_set_public_ips` |

Use a public static IP when you need inbound access (SSH, remote management, server-initiated requests), a stable IP for firewall allowlists, or to run services on the device that external systems call into.

## Private Wireless Gateways

A Private Wireless Gateway (PWG) routes all SIM traffic through your own private network. SIMs connected via a PWG sit inside your private IP space — not on the public internet.

### Why PWG

- **Security** — SIMs are not directly exposed to the internet
- **Control** — route traffic through your own firewall or DLP platform
- **Direct access** — devices are addressable on your corporate network like any other host

### Architecture

PWGs connect to a VRF-defined network on Telnyx's MPLS backbone. Virtual Cross Connects (VXC) or WireGuard interfaces (Cloud VPNs) bridge this to your corporate network. All interfaces on the same VRF can see each other. Assign a PWG to a SIM Card Group via group actions; all SIMs in the group route through the PWG.

### PWG API

| Action | Endpoint |
| --- | --- |
| List PWGs | `GET /private_wireless_gateways` |
| Create PWG | `POST /private_wireless_gateways` |
| Get PWG | `GET /private_wireless_gateways/{id}` |
| Delete PWG | `DELETE /private_wireless_gateways/{id}` |

### APN-based IP Assignment

| APN | IP Assignment |
| --- | --- |
| `data.net` | Static — same IP across sessions |
| `data00.telnyx` | Dynamic — new IP each session |

To use a static IP, your device must connect using the `data.net` APN. Devices on `data00.telnyx` get dynamic IPs.

### PWG Limitations

- **Region** — PWGs are currently only available in Ashburn, VA (more regions coming)
- **IP range** — Default `100.64.199.0/24` (254 concurrent SIMs); custom ranges coming
- **Internet access** — PWGs have no internet access by default; contact support to open your VRF to the internet

### Setting Up a Private Wireless Gateway

1. **Set up Cloud VPN** — In the portal's Network section, create a network, add a VPN interface, wait for provisioning, add a peer, and store the private key safely.
2. **Create the PWG** — In the Wireless section of the portal, select "Create PWG Interface", name it, select the network from step 1 (region must match the VPN interface), accept the MRC charge, and wait for status to transition from Provisioning to Provisioned. Then create a SIM Group, edit it, click "Connect PWG" to assign the PWG, and add SIM cards.
3. **Configure routing** — The network default gateway must be set up by the Telnyx Network team manually. Contact support via the Mission Control Portal chat. Once configured, you can control which external destinations are reachable from devices connected through the PWG, and which are blocked.
