---
title: Telnyx Wireless IoT
summary: Telnyx Wireless provides API-controlled cellular connectivity for IoT devices
  — provisioning SIMs, routing data through private or public networks, filtering
  traffic, blocking networks, enabling VoLTE, sending SMS, and generating granular
  usage reports, all programmable from one platform.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/sim-lifecycle
- url: https://developers.telnyx.com/docs/iot-sim/sim7600-a-rasp-pui-hat/index
- url: https://developers.telnyx.com/docs/iot-sim/sixfab-cellular-iot-hat
- url: https://developers.telnyx.com/docs/iot-sim/sixfab-rasp-pi-hat
- url: https://developers.telnyx.com/docs/iot-sim/traffic-policy-profiles
- url: https://developers.telnyx.com/docs/iot-sim/voice-enabled-iot/index
- url: https://developers.telnyx.com/docs/iot-sim/wireless-blocklists
- url: https://developers.telnyx.com/docs/iot-sim/wireless-detail-records
- url: https://developers.telnyx.com/docs/iot-sim/wireless-overview/index
updated_at: 2026-06-11T10:34:44Z
---

# Telnyx Wireless IoT

*Part 1 of 2 — see also: [Part 2](telnyx-wireless-iot--part-2.md)*

Telnyx Wireless provides API-controlled cellular connectivity for IoT devices — provisioning SIMs, routing data through private or public networks, filtering traffic, blocking networks, enabling VoLTE, sending SMS, and generating granular usage reports, all programmable from one platform.

## Overview

Telnyx Wireless gives you API control over cellular connectivity. Provision SIMs, route data through private networks, enable VoLTE calling, and send SMS — all programmable, all on one platform. Key capabilities include:

- **SIMs & eSIMs** — Order, activate, and manage SIM cards. Group operations, bulk provisioning, and eSIM profiles.
- **Data** — Cellular data with flexible routing: public internet, Private Wireless Gateways, or public IPs for inbound connections.
- **VoLTE** — A second line on one phone, or the full Telnyx voice stack on cellular — Call Control, AI agents, recording, IVR.
- **Messaging** — SMS, MMS, and RCS on cellular numbers. A real messaging experience — same as any carrier line.

## SIM Lifecycle and Status

Every SIM follows the same state machine regardless of type (physical or eSIM). A SIM must have a `sim_card_group_id` before it can be enabled or set to standby.

### User-Controlled Statuses

| Status | On Network | Passes Traffic | Notes |
|---|---|---|---|
| `enabled` | Yes | Yes | Active on the network. |
| `disabled` | No | No | Off the network. IP released. $0.20/mo holding fee. |
| `standby` | No | No | Off the network. IP preserved. $0.20/mo. |

**`disabled` vs `standby`** — the only difference is IP preservation. If your application depends on a stable IP (e.g., firewall allowlists, IoT platforms that register by IP), use `standby`. Otherwise `disabled` is fine.

### Transitional Statuses

All transitions are asynchronous. While in progress, the SIM reports a transitional status.

| Status | Target |
|---|---|
| `registering` | → `enabled` (initial setup) |
| `enabling` | → `enabled` |
| `disabling` | → `disabled` |
| `setting_standby` | → `standby` |

Track progress via SIM Card Actions. All state changes return `202` with a SIM Card Action — they are not instant. Poll the action status or list actions to confirm completion.

### System-Imposed Statuses

Set by Telnyx, not by API calls. The SIM cannot transition while in these states.

| Status | Meaning | How to Exit |
|---|---|---|
| `data_limit_exceeded` | SIM exceeded its group's data limit. | Raise the data limit via `PATCH /sim_card_groups/{id}` (group level) or `PATCH /sim_cards/{id}` (SIM level), or wait for billing cycle reset. Auto-transitions to `intended_status`. |
| `unauthorized_imei` | SIM is in a device not on its `authorized_imeis` list. | Update `authorized_imeis` via `PATCH /sim_cards/{id}` to add the current IMEI or clear the list. Then re-enable with `POST /sim_cards/{id}/actions/enable`. |
| `blocked` | Account-level service interruption (billing). | Resolve account billing issue. Auto-syncs back to intended state. |
| `abolished` | Account-level service interruption (billing). | Resolve account billing issue. Auto-syncs back to intended state. |

### Status Triggers

| Target Status | What Triggers It |
|---|---|
| `enabled` | Enable SIM — from `registered`, `disabled`, or `standby` |
| `disabled` | Disable SIM — from `enabled` |
| `standby` | Set Standby — from `enabled` |
| `data_limit_exceeded` | System — SIM exceeded its group or SIM-level data limit. Adjust via Update Group or Update SIM. |
| `unauthorized_imei` | System — SIM inserted into a device not in its `authorized_imeis` list. Fix via Update SIM. |
| `blocked` / `abolished` | System — account-level billing interruption. Resolve with Telnyx support. |

## SIM Deletion

`DELETE /sim_cards/{id}` permanently deregisters the SIM. This is irreversible:

- **Physical SIMs** — the plastic is now waste. You would need to order and register a new one.
- **eSIMs** — the profile is gone. You would need to purchase a new eSIM.

Prefer disable or standby if there is any chance you will need the SIM again. For eSIMs that cannot be uninstalled from a device, pass `report_lost=true` — this is irreversible and the eSIM cannot be re-registered.

## Traffic Policy Profiles

Traffic Policy Profiles define what network traffic your SIMs are allowed (or denied). Assign a profile to filter traffic at the network level before it reaches your devices.

### Profile Types

| Type | Behavior |
|---|---|
| **whitelist** | Only listed traffic is allowed. Everything else is blocked. |
| **blacklist** | Listed traffic is blocked. Everything else is allowed. |
| **throttling** | Traffic is allowed but bandwidth-limited to `limit_bw_kbps`. |

### Filter Criteria

Each profile can include one or more of:

- **services** — PCEF service IDs (predefined traffic categories). Use `GET /traffic/policy/profiles/services` to list available services.
- **ip_ranges** — CIDR notation (e.g., `10.0.0.0/8`, `203.0.113.0/24`). Block or allow specific IP ranges.
- **domains** — Domain names (e.g., `example.com`, `*.internal.corp`). DNS-level filtering.

At least one of `services`, `ip_ranges`, or `domains` is required when creating a profile.

### Example: IoT Device Lockdown

Whitelist-only profile that restricts a fleet of sensors to your backend servers:

```json
{
  "type": "whitelist",
  "ip_ranges": ["10.100.0.0/16"],
  "domains": ["api.yourcompany.com", "telemetry.yourcompany.com"]
}
```

Devices can only reach your internal network and two API endpoints. All other traffic is dropped.

### Example: Bandwidth Throttling

Limit data-hungry devices to prevent runaway costs:

```json
{
  "type": "throttling",
  "limit_bw_kbps": 256
}
```

### Assigning Profiles

Profiles are assigned at the SIM Card Group level. Create the profile via `POST /traffic/policy/profiles`, then reference its ID when configuring the group.

## Wireless Blocklists

Wireless Blocklists let you restrict which networks your SIMs can attach to. Assign a blocklist to a SIM Card Group and every SIM in that group is blocked from the listed networks.

### Blocklist Types

| Type | Blocks By | Example Value | Use Case |
|---|---|---|---|
| **country** | ISO country code | `US`, `CN`, `RU` | Geo-fencing — keep devices in allowed regions |
| **mcc** | Mobile Country Code | `310` (US), `234` (UK) | Block all carriers in a country |
| **plmn** | MCC + MNC pair | `31026` (T-Mobile US) | Block a specific carrier |

Use `GET /wireless_blocklist_values` to retrieve all valid values for a given type.

### How Blocklists Work

1. **Create a blocklist** — `POST /wireless_blocklists` with a `name`, `type`, and `values` array.
2. **Assign to a SIM Card Group** — Set `wireless_blocklist_id` on the group via `PATCH /sim_card_groups/{id}`.
3. All SIMs in that group are now blocked from the listed networks.

One blocklist per group. Changing the blocklist on a group affects all SIMs in it immediately.

### Common Blocklist Patterns

- **Geo-fencing:** Create a `country` blocklist with countries where your devices should not operate. Useful for compliance, cost control, or preventing stolen device use.
- **Carrier avoidance:** Create a `plmn` blocklist to steer SIMs away from expensive or unreliable carriers in a region. The SIM's multi-IMSI applet will select the next best available network.
- **Security lockdown:** Block all networks except your target deployment region. Combined with [Private Wireless Gateway](private-wireless-gateway.md), this creates a fully controlled connectivity path.
