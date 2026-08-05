---
title: Wireless Blocklists
summary: Wireless Blocklists let you restrict which networks your SIMs can attach
  to. Assign a blocklist to a SIM Card Group and every SIM in that group is blocked
  from the listed networks.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/wireless-blocklists
updated_at: 2026-08-05T13:47:23Z
---

# Wireless Blocklists

Wireless Blocklists let you restrict which networks your SIMs can attach to. Assign a blocklist to a SIM Card Group and every SIM in that group is blocked from the listed networks.

## Blocklist Types

| Type | Blocks By | Example Value | Use Case |
| --- | --- | --- | --- |
| **country** | ISO country code | `US`, `CN`, `RU` | Geo-fencing — keep devices in allowed regions |
| **mcc** | Mobile Country Code | `310` (US), `234` (UK) | Block all carriers in a country |
| **plmn** | MCC + MNC pair | `31026` (T-Mobile US) | Block a specific carrier |

Use `GET /wireless_blocklist_values` to retrieve all valid values for a given type.

## How It Works

1. **Create a blocklist** — `POST /wireless_blocklists` with a `name`, `type`, and `values` array.
2. **Assign to a SIM Card Group** — Set `wireless_blocklist_id` on the group via `PATCH /sim_card_groups/{id}`.
3. All SIMs in that group are now blocked from the listed networks.

One blocklist per group. Changing the blocklist on a group affects all SIMs in it immediately.

## Common Patterns

**Geo-fencing:** Create a `country` blocklist with countries where your devices shouldn't operate. Useful for compliance, cost control, or preventing stolen device use.

**Carrier avoidance:** Create a `plmn` blocklist to steer SIMs away from expensive or unreliable carriers in a region. The SIM's multi-IMSI applet will select the next best available network.

**Security lockdown:** Block all networks except your target deployment region. Combined with [Private Wireless Gateways](private-wireless-gateways.md), this creates a fully controlled connectivity path.
