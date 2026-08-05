---
title: Private Wireless Gateways
summary: A Private Wireless Gateway (PWG) routes all SIM traffic through your own
  private network, keeping SIMs inside your private IP space rather than exposing
  them to the public internet. PWGs connect to a VRF-defined network on Telnyx's MPLS
  backbone and can be bridged to your corporate network via Virtual Cross Connects
  (VXC) or WireGuard Cloud VPNs.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/private-wireless-gateways
updated_at: 2026-08-05T13:47:08Z
---

# Private Wireless Gateways

A Private Wireless Gateway (PWG) routes all SIM traffic through your own private network, keeping SIMs inside your private IP space rather than exposing them to the public internet. PWGs connect to a VRF-defined network on Telnyx's MPLS backbone and can be bridged to your corporate network via Virtual Cross Connects (VXC) or WireGuard Cloud VPNs.

## Why PWG

A Private Wireless Gateway (PWG) routes all SIM traffic through your own private network. SIMs connected via a PWG sit inside your private IP space — not on the public internet.

- **Security** — SIMs are not directly exposed to the internet.
- **Control** — Route traffic through your own firewall or DLP platform.
- **Direct access** — Devices are addressable on your corporate network like any other host.

## Architecture

PWGs connect to a VRF-defined network on Telnyx's MPLS backbone. Virtual Cross Connects (VXC) or WireGuard interfaces (Cloud VPNs) bridge this to your corporate network. All interfaces on the same VRF can see each other.

![Private Wireless Gateways](https://mintcdn.com/telnyx/Iu93-l5Bj6hMoe-q/img/edge_device_deployment__1_.svg?fit=max&auto=format&n=Iu93-l5Bj6hMoe-q&q=85&s=8741828382ea5747a8e6ffc471695d36)

## API

| Action | Endpoint |
| --- | --- |
| List PWGs | `GET /private_wireless_gateways` |
| Create PWG | `POST /private_wireless_gateways` |
| Get PWG | `GET /private_wireless_gateways/{id}` |
| Delete PWG | `DELETE /private_wireless_gateways/{id}` |

Assign a PWG to a [SIM Card Group](sim-card-groups.md) via group actions. All SIMs in the group route through the PWG.

## APN-based IP Assignment

| APN | IP Assignment |
| --- | --- |
| `data.net` | Static — same IP across sessions |
| `data00.telnyx` | Dynamic — new IP each session |

To use a static IP, your device must connect using the `data.net` APN. Devices on `data00.telnyx` get dynamic IPs.

## Limitations

- **Region** — PWGs are currently only available in Ashburn, VA. More regions coming.
- **IP range** — Default `100.64.199.0/24` (254 concurrent SIMs). Custom ranges coming.
- **Internet access** — PWGs have no internet access by default. Contact support to open your VRF to the internet.

## Setup

See [Private Gateway Setup](private-gateway-setup.md) for step-by-step instructions.
