---
title: Public IPs
summary: Public static IPs make SIMs reachable from the public internet, in contrast
  to the default dynamic private IPs that are outbound-only. This page covers the
  available actions for managing public IPs and the scenarios in which they are useful.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/public-ips
updated_at: 2026-08-05T13:47:09Z
---

# Public IPs

Public static IPs make SIMs reachable from the public internet, in contrast to the default dynamic private IPs that are outbound-only. This page covers the available actions for managing public IPs and the scenarios in which they are useful.

## Overview

By default, SIMs are assigned dynamic private IPs that are reachable outbound only. A public static IP makes the SIM reachable from the public internet and is billed at $3 per month per SIM.

## Actions

| Action | Endpoint |
| --- | --- |
| Get Public IP | `GET /sim_cards/{id}/public_ip` |
| Set Public IP | `POST /sim_cards/{id}/actions/set_public_ip` |
| Remove Public IP | `POST /sim_cards/{id}/actions/remove_public_ip` |
| Bulk Set Public IPs | `POST /sim_cards/actions/bulk_set_public_ips` |

## When to Use

- **Inbound access** — connect *to* your SIM from anywhere (SSH, remote management, server-initiated requests).
- **Firewall allowlists** — stable IP for access control rules.
- **Device-as-server** — run services on the device that external systems call into.
