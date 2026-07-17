---
title: Wireless
summary: Telnyx Wireless provides API-driven cellular connectivity for IoT and mobile
  devices. This page covers SIM and eSIM provisioning, lifecycle management, SIM Card
  Groups, bulk operations, data routing (public IPs, Private Wireless Gateways, Traffic
  Policy Profiles, Wireless Blocklists), data usage monitoring and notifications,
  Wireless Detail Records, OTA updates, VoLTE with mobile phone numbers and call features,
  IoT pricing, connectivity troubleshooting, AT commands, and step-by-step setup guides
  for a range of supported devices including Raspberry Pi HATs, Particle Boron, Nordic
  nRF9160, Cradlepoint IBR200, Pepwave Max BR1 Mini, GL-MiFi, and Mikrotik wAP LTE.
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
- url: https://developers.telnyx.com/docs/iot-sim/sim-lifecycle
- url: https://developers.telnyx.com/docs/iot-sim/sim7600-a-rasp-pui-hat/index
- url: https://developers.telnyx.com/docs/iot-sim/sixfab-cellular-iot-hat
- url: https://developers.telnyx.com/docs/iot-sim/sixfab-rasp-pi-hat
- url: https://developers.telnyx.com/docs/iot-sim/traffic-policy-profiles
- url: https://developers.telnyx.com/docs/iot-sim/voice-enabled-iot/index
- url: https://developers.telnyx.com/docs/iot-sim/wireless-blocklists
- url: https://developers.telnyx.com/docs/iot-sim/wireless-detail-records
- url: https://developers.telnyx.com/docs/iot-sim/wireless-overview/index
updated_at: 2026-07-17T09:19:06Z
---

# Wireless

*Part 2 of 6 — see also: [Part 1](wireless--part-1.md), [Part 3](wireless--part-3.md), [Part 4](wireless--part-4.md), [Part 5](wireless--part-5.md), [Part 6](wireless--part-6.md)*

Telnyx Wireless provides API-driven cellular connectivity for IoT and mobile devices. This page covers SIM and eSIM provisioning, lifecycle management, SIM Card Groups, bulk operations, data routing (public IPs, Private Wireless Gateways, Traffic Policy Profiles, Wireless Blocklists), data usage monitoring and notifications, Wireless Detail Records, OTA updates, VoLTE with mobile phone numbers and call features, IoT pricing, connectivity troubleshooting, AT commands, and step-by-step setup guides for a range of supported devices including Raspberry Pi HATs, Particle Boron, Nordic nRF9160, Cradlepoint IBR200, Pepwave Max BR1 Mini, GL-MiFi, and Mikrotik wAP LTE.

## SIM Card Groups

**Groups vs Bulk Operations** — Groups are ongoing policy; a SIM inherits its group's settings as long as it's a member. Bulk operations are one-time actions on an explicit list of SIMs.

Every SIM belongs to a group and inherits its settings. Set policy on the group instead of updating SIMs individually.

### Default Group

Every account has a default group. SIMs that aren't explicitly assigned land here. Deleting a group moves its SIMs back to default. Moving SIMs between groups after they're active can briefly interrupt connectivity.

### Group Settings

Configurable via [`PATCH /sim_card_groups/{id}`](/api-reference/sim-card-groups/update-a-sim-card-group):

| Setting | Description |
| --- | --- |
| `name` | Display name for the group. |
| `data_limit` | Data cap (`amount` + `unit`). SIMs exceeding this enter `data_limit_exceeded` until the limit is raised or the billing cycle resets. |

### Group Actions

These are async — each returns an action ID. Track progress via [`GET /sim_card_group_actions`](/api-reference/sim-card-group-actions/list-sim-card-group-actions).

| Action |
| --- |
| [Assign Private Wireless Gateway](/api-reference/sim-card-groups/request-private-wireless-gateway-assignment-for-sim-card-group) |
| [Remove Private Wireless Gateway](/api-reference/sim-card-groups/request-private-wireless-gateway-removal-from-sim-card-group) |
| [Assign Wireless Blocklist](/api-reference/sim-card-groups/request-wireless-blocklist-assignment-for-sim-card-group) |
| [Remove Wireless Blocklist](/api-reference/sim-card-groups/request-wireless-blocklist-removal-from-sim-card-group) |

## Bulk Operations

**Bulk vs Group** — Bulk actions are one-time operations on an explicit list of SIM IDs. Nothing persists. For ongoing policy that applies to current and future SIMs, use [SIM Card Groups](sim-card-groups.md).

All actions are async — submit a list of SIM IDs, get back an action ID, poll for status.

| Action |
| --- |
| [Bulk Enable Voice](/api-reference/sim-cards/request-bulk-enabling-voice-on-sim-cards) |
| [Bulk Disable Voice](/api-reference/sim-cards/request-bulk-disabling-voice-on-sim-cards) |
| [Bulk Set Public IPs](/api-reference/sim-cards/request-bulk-setting-sim-card-public-ips) |
| [Validate Registration Codes](/api-reference/sim-cards/validate-sim-cards-registration-codes) |

Track progress via [List Bulk SIM Card Actions](/api-reference/sim-card-actions/list-bulk-sim-card-actions). Per-SIM results are included — some may succeed while others fail.

For bulk registration, validate codes first with the validation endpoint. This dry-run catches typos and invalid codes before you commit to a large batch.
