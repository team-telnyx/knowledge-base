---
title: Telnyx IoT SIM / Wireless
summary: Telnyx IoT SIM cards provide global cellular connectivity for IoT devices,
  supporting both physical triple-cut SIMs and over-the-air eSIMs. The platform offers
  API-managed resources for SIM lifecycle, data limits, bulk operations, voice features,
  and private networking via Wireless Gateways.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/at-commands/index
- url: https://developers.telnyx.com/docs/iot-sim/bulk-sim-actions/index
- url: https://developers.telnyx.com/docs/iot-sim/call-forwarding-recording
- url: https://developers.telnyx.com/docs/iot-sim/connectivity-troubleshooting/index
- url: https://developers.telnyx.com/docs/iot-sim/cradlepoint-ibr200-cellular/index
- url: https://developers.telnyx.com/docs/iot-sim/data-usage-notifications
- url: https://developers.telnyx.com/docs/iot-sim/edge-deployment/index
- url: https://developers.telnyx.com/docs/iot-sim/get-started/index
- url: https://developers.telnyx.com/docs/iot-sim/glmifi-router
- url: https://developers.telnyx.com/docs/iot-sim/iot-pricing
- url: https://developers.telnyx.com/docs/iot-sim/messaging-settings/index
updated_at: 2026-06-11T10:32:17Z
---

# Telnyx IoT SIM / Wireless

*Part 1 of 2 — see also: [Part 2](telnyx-iot-sim-wireless--part-2.md)*

Telnyx IoT SIM cards provide global cellular connectivity for IoT devices, supporting both physical triple-cut SIMs and over-the-air eSIMs. The platform offers API-managed resources for SIM lifecycle, data limits, bulk operations, voice features, and private networking via Wireless Gateways.

## SIM Types and Form Factors

All Telnyx SIMs are eUICC-enabled and come in two form factors:

| Type | Form Factor | Delivery | Use Case |
|---|---|---|---|
| **SIM Card** | Triple-cut plastic (2FF/3FF/4FF) | Shipped | Routers, gateways, traditional devices |
| **eSIM** | Software profile | Over-the-air download | Phones, tablets, laptops — no physical SIM needed |

## Resource Model

Three core resources, all API-managed:

- **SIM Card** — the connectivity entity. Has an ICCID, status, data settings, and optional voice flag. Covers both physical SIMs and eSIMs (eSIMs are purchased via a separate endpoint but become the same SIM Card resource with an activation code for OTA provisioning).
- **SIM Card Group** — bulk management. Apply data limits, network preferences, and Private Wireless Gateway configs to all SIMs in a group at once.
- **Mobile Phone Number** — optional. Created when you enable voice or messaging on a SIM. Controls call forwarding, caller ID, and messaging profile.

## SIM Lifecycle

```
Order → Register → enabled → [Active Use] → disabled / standby
```

| Status | MRC | Data | Description |
|---|---|---|---|
| **Registered** | $2/mo | No | SIM exists in your account, not yet on network |
| `enabled` | $2/mo | Yes | Active on network, consuming data |
| `disabled` | $0.20/mo | No | Off network, reduced cost, retains config |
| `standby` | $0.20/mo | No | Same as disabled, ready for quick re-enable |

## Multi-IMSI

Every Telnyx SIM carries multiple IMSIs (Telnyx, Sparkle, BICs, T-Mobile, US Cellular). An on-SIM applet automatically selects the best IMSI per location, enabling local network attachment instead of roaming for lower latency and better rates. The default is automatic selection. You can override to manual per-SIM or per-group via API if you need to pin a specific IMSI for regulatory or testing purposes.

## Pricing

Pricing has three components:

| Component | Cost |
|---|---|
| **One-time charge (OTC)** | $1/SIM card; $0.70/eSIM. $10 shipping outside US mainland |
| **Monthly recurring (MRC)** | $2/active SIM; $0.20/disabled or standby SIM |
| **Data usage** | Tiered by zone and volume — determined by country of usage (MCC) across 9 zones |

For a full cost breakdown mapping each country to its zone, see the [Programmable Wireless Pricing](https://support.telnyx.com/en/articles/3296669-programmable-wireless-pricing) article.

## Bulk SIM Actions

Bulk actions are one-time operations on an explicit list of SIM IDs. They are asynchronous — submit a list of SIM IDs, receive an action ID, and poll for status. For ongoing policy that applies to current and future SIMs, use [SIM Card Groups](sim-card-groups.md) instead.

Available bulk actions:

- Bulk Enable Voice
- Bulk Disable Voice
- Bulk Set Public IPs
- Validate Registration Codes

Track progress via the List Bulk SIM Card Actions endpoint. Per-SIM results are included — some may succeed while others fail. For bulk registration, validate codes first with the validation endpoint; this dry-run catches typos and invalid codes before committing to a large batch.

## Data Limits and Monitoring

### Setting Limits

| Level | Set Via | Scope |
|---|---|---|
| **Group** | `PATCH /sim_card_groups/{id}` | All SIMs in the group share the limit. SIMs exceeding it enter `data_limit_exceeded`. Resets monthly. |
| **SIM** | `PATCH /sim_cards/{id}` | Per-SIM `data_limit` override |

### Per-SIM Usage Notifications

Set a threshold on individual SIMs to get notified before they hit their limit. Notification endpoints include listing, creating, getting, updating, and deleting notifications via the `/sim_card_data_usage_notifications` API.

### Monitoring Consumption

- **Per group** — `GET /sim_card_groups/{id}` returns `consumed_data`.
- **Per SIM** — visible in the SIM card detail response.
- **Portal** — Settings page shows real-time consumption per group.

## APN and Device Configuration

All Telnyx SIMs require the APN to be set to **`data00.telnyx`** (leave all other APN fields blank). Additional device configuration steps:

1. Enable cellular data
2. Set network to 3G/LTE or 4G/LTE only (first registration requires at least 3G)
3. Enable roaming
4. Set APN to `data00.telnyx`
5. Update firmware, then reboot

**Android:** Settings → Mobile Networks → Access Point Names → Add
**iOS:** Settings → Cellular → Mobile Data → APN

## AT Commands

AT commands are useful for interacting with cellular modules (e.g., Raspberry Pi HAT). Before running AT commands, ensure the Raspberry Pi is up-to-date and the serial port is enabled:

1. Run `sudo raspi-config`, choose **Interfacing Options (5)**, then **P6 Serial**, press *No* to the serial login prompt, then reboot.
2. Install `screen` (`sudo apt install screen`) or `minicom`. Use `screen ttyUSB3` or `screen ttyS0` to connect. Run `ls -l /dev` to identify the correct port.

Common AT commands:

| Command | Purpose | Sample Response |
|---|---|---|
| `AT` | Check communication with device | OK |
| `AT+COPS=?` | List all available carriers (filters out incompatible ones) | `0, 1, "T-Mobile"` or `0, 4, "AT&T"` |
| `AT+COPS=(#, #)` | Check current network | `"T-Mobile"` or `"AT&T"` |
| `AT+CCID` | Check SIM ID / IMEI number | OK |
| `AT+CREG?` | Network registration status | OK |
| `AT+COPS=1,0,"Carrier Name"` | Manually connect to a network (PLMN selection). Returns CME ERROR if the SIM does not support the carrier. | OK |
| `AT+BANDS` | Manually select a cellular band (use sparingly) | `OK 0100004000 B12 045000000 B5` |

> **Troubleshooting:** Raspberry Pi 4 has intermittent issues recognizing which USB port to use for serial communication. Using a Bluetooth keyboard and mouse mitigates this confusion.
