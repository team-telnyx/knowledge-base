---
title: Private Wireless Gateways
summary: Route SIM traffic through your private network instead of the public internet.
sources:
  - url: https://developers.telnyx.com/docs/iot-sim/private-wireless-gateways/index
    content_hash: 841f88cfc106208e1e94a25dd825c1276c53e85b18347b0bda434d4c3b45ccb8
updated_at: 2026-04-10T00:00:00Z
---

# Private Wireless Gateways

Route SIM traffic through your private network instead of the public internet.

A Private Wireless Gateway (PWG) routes all SIM traffic through your own private network. SIMs connected via a PWG sit inside your private IP space — not on the public internet.

## Why PWG

* **Security** — SIMs are not directly exposed to the internet
* **Control** — route traffic through your own firewall or DLP platform
* **Direct access** — devices are addressable on your corporate network like any other host

## Architecture

PWGs connect to a VRF-defined network on Telnyx's MPLS backbone. Virtual Cross Connects (VXC) or WireGuard interfaces (Cloud VPNs) bridge this to your corporate network. All interfaces on the same VRF can see each other.

<img alt="Private Wireless Gateways" />

## API

| Action                                                                   | Endpoint                                 |
| :----------------------------------------------------------------------- | :--------------------------------------- |
| [List PWGs](https://developers.telnyx.com/api-reference/sim-cards/get-all-private-wireless-gateways)  | `GET /private_wireless_gateways`         |
| [Create PWG](https://developers.telnyx.com/api-reference/sim-cards/create-a-private-wireless-gateway) | `POST /private_wireless_gateways`        |
| [Get PWG](https://developers.telnyx.com/api-reference/sim-cards/get-a-private-wireless-gateway)       | `GET /private_wireless_gateways/{id}`    |
| [Delete PWG](https://developers.telnyx.com/api-reference/sim-cards/delete-a-private-wireless-gateway) | `DELETE /private_wireless_gateways/{id}` |

Assign a PWG to a SIM Card Group via [group actions](sim-card-groups.md). All SIMs in the group route through the PWG.

## APN-based IP Assignment

| APN             | IP Assignment                    |
| :-------------- | :------------------------------- |
| `data.net`      | Static — same IP across sessions |
| `data00.telnyx` | Dynamic — new IP each session    |

> **Warning:** To use a static IP, your device must connect using the `data.net` APN. Devices on `data00.telnyx` get dynamic IPs.

## Limitations

* **Region** — PWGs are currently only available in Ashburn, VA. More regions coming.
* **IP range** — Default `100.64.199.0/24` (254 concurrent SIMs). Custom ranges coming.
* **Internet access** — PWGs have no internet access by default. Contact support to open your VRF to the internet.

## Setup

See [Private Gateway Setup](../concepts/how-to-set-up-a-private-wireless-gateway.md) for step-by-step instructions.


## Related Pages

- [Private Wireless Gateway (PGW)](../runbooks/private-wireless-gateway-pgw.md)
- [How to set up a Private Wireless Gateway](../concepts/how-to-set-up-a-private-wireless-gateway.md)
