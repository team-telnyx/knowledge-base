---
title: Public IPs
summary: Assign public static IPs to SIM cards for inbound connectivity.
sources:
  - url: https://developers.telnyx.com/docs/iot-sim/public-ips/index
    content_hash: 17b629b4fcf8166230eb2e6cc388b95df63b16e7acca43d17044f62c483d04cc
updated_at: 2026-04-10T00:00:00Z
---

# Public IPs

Assign public static IPs to SIM cards for inbound connectivity.

By default, SIMs get dynamic private IPs — reachable outbound only. A public static IP makes the SIM reachable from the internet (\$3/mo per SIM).

## Actions

| Action                                                                                   | Endpoint                                        |
| :--------------------------------------------------------------------------------------- | :---------------------------------------------- |
| [Get Public IP](https://developers.telnyx.com/api-reference/sim-cards/get-sim-card-public-ip-definition)              | `GET /sim_cards/{id}/public_ip`                 |
| [Set Public IP](https://developers.telnyx.com/api-reference/sim-cards/request-setting-a-sim-card-public-ip)           | `POST /sim_cards/{id}/actions/set_public_ip`    |
| [Remove Public IP](https://developers.telnyx.com/api-reference/sim-cards/request-removing-a-sim-card-public-ip)       | `POST /sim_cards/{id}/actions/remove_public_ip` |
| [Bulk Set Public IPs](https://developers.telnyx.com/api-reference/sim-cards/request-bulk-setting-sim-card-public-ips) | `POST /sim_cards/actions/bulk_set_public_ips`   |

## When to Use

* **Inbound access** — connect *to* your SIM from anywhere (SSH, remote management, server-initiated requests)
* **Firewall allowlists** — stable IP for access control rules
* **Device-as-server** — run services on the device that external systems call into
