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

*Part 1 of 6 — see also: [Part 2](wireless--part-2.md), [Part 3](wireless--part-3.md), [Part 4](wireless--part-4.md), [Part 5](wireless--part-5.md), [Part 6](wireless--part-6.md)*

Telnyx Wireless provides API-driven cellular connectivity for IoT and mobile devices. This page covers SIM and eSIM provisioning, lifecycle management, SIM Card Groups, bulk operations, data routing (public IPs, Private Wireless Gateways, Traffic Policy Profiles, Wireless Blocklists), data usage monitoring and notifications, Wireless Detail Records, OTA updates, VoLTE with mobile phone numbers and call features, IoT pricing, connectivity troubleshooting, AT commands, and step-by-step setup guides for a range of supported devices including Raspberry Pi HATs, Particle Boron, Nordic nRF9160, Cradlepoint IBR200, Pepwave Max BR1 Mini, GL-MiFi, and Mikrotik wAP LTE.

## SIMs & eSIMs

Telnyx Wireless gives you API control over cellular connectivity. Provision SIMs, route data through private networks, enable VoLTE calling, and send SMS — all programmable, all on one platform.

### SIM Types

All Telnyx SIMs are eUICC-enabled. Three form factors are available:

| Type | Form Factor | Delivery | Use Case |
| --- | --- | --- | --- |
| **SIM Card** | Triple-cut plastic (2FF/3FF/4FF) | Shipped | Routers, gateways, traditional devices |
| **eSIM** | Software profile | Over-the-air download | Phones, tablets, laptops — no physical SIM needed |

### Resource Model

Three core resources, all API-managed:

- **SIM Card** — the connectivity entity. Has an ICCID, status, data settings, optional voice flag. Covers both physical SIMs and eSIMs (eSIMs are purchased via a separate endpoint but become the same SIM Card resource with an activation code for OTA provisioning). Everything starts here.
- **SIM Card Group** — bulk management. Apply data limits, network preferences, and Private Wireless Gateway configs to all SIMs in a group at once.
- **Mobile Phone Number** — optional. Created when you enable voice or messaging on a SIM. Controls call forwarding, caller ID, messaging profile.

### Multi-IMSI

Every Telnyx SIM carries multiple IMSIs (Telnyx, Sparkle, BICs, T-Mobile, US Cellular). An on-SIM applet automatically selects the best IMSI per location — local network attachment instead of roaming, lower latency, better rates. Default is automatic selection. You can override to manual per-SIM or per-group via API if you need to pin a specific IMSI for regulatory or testing purposes.

### Pricing

Three cost components:

| Component | Cost |
| --- | --- |
| **SIM purchase** | $1/SIM, $0.70/eSIM. $10 shipping outside US mainland. |
| **Monthly** | $2/active SIM, $0.20/disabled or standby |
| **Data** | Tiered by zone and volume. [Full breakdown](https://support.telnyx.com/en/articles/3296669-programmable-wireless-pricing) |

## Getting SIMs

### Physical SIMs

Physical SIM orders go through [Mission Control](https://portal.telnyx.com/#/wireless/buy-sim-cards) — you can't order them via API.

1. **Order** — Set quantity, add to cart, and check out. Telnyx ships triple-cut SIM cards (2FF/3FF/4FF) to your address.
2. **Register** — Each physical SIM has a 10-digit registration code printed on the card. Register via the portal ([Register SIM Cards](https://portal.telnyx.com/#/wireless/buy-sim-cards) tab, manual or CSV) or the API ([`POST /actions/register/sim_cards`](/api-reference/sim-cards/register-sim-cards)). During registration you assign a SIM Card Group and optional tags.
3. **Enable** — Once registered, activate the SIM on the network via [`POST /sim_cards/{id}/actions/enable`](/api-reference/sim-cards/request-a-sim-card-enable) or the portal.

After registration, the SIM appears as a standard SIM Card resource. All further management is via the API.

### eSIMs

eSIMs are downloadable SIM profiles for consumer devices (phones, tablets, laptops) — not embedded SIM hardware. For eUICC hardware solutions, contact [Sales](https://telnyx.com/contact-us).

Purchase through [Mission Control](https://portal.telnyx.com/#/wireless/buy-esims) or the API (`POST /actions/purchase_esims`):

- **Portal** — Set quantity, assign a SIM Card Group, choose initial status, add tags. $0.70 activation fee per eSIM. No cart — purchase is immediate.
- **API** — [`POST /actions/purchase/esims`](/api-reference/sim-cards/purchase-esims). Same parameters, same instant provisioning.

Either way, you get an activation code immediately. Provide it to the device via QR code or direct input for OTA provisioning. No shipping, no registration step.

eSIM activation codes are one-time use. If the device loses the profile, you need a new eSIM purchase — you can't re-download the same profile.

After provisioning, eSIMs become the same SIM Card resource as physical SIMs. All API operations are identical.

## SIM Lifecycle

Every SIM follows the same state machine regardless of type (physical or eSIM).

### Status

**User-Controlled**

| Status | On Network | Passes Traffic | Notes |
| --- | --- | --- | --- |
| `enabled` | Yes | Yes | Active on the network. |
| `disabled` | No | No | Off the network. IP released. $0.20/mo holding fee. |
| `standby` | No | No | Off the network. IP preserved. $0.20/mo. |

**`disabled` vs `standby`** — the only difference is IP preservation. If your application depends on a stable IP (e.g., firewall allowlists, IoT platforms that register by IP), use `standby`. Otherwise `disabled` is fine.

**Transitional**

All transitions are asynchronous. While in progress, the SIM reports a transitional status.

| Status | Target |
| --- | --- |
| `registering` | → `enabled` (initial setup) |
| `enabling` | → `enabled` |
| `disabling` | → `disabled` |
| `setting_standby` | → `standby` |

Track progress via [SIM Card Actions](/api-reference/sim-card-actions/list-sim-card-actions).

All state changes return `202` with a SIM Card Action — they are not instant. Poll the action status or list actions to confirm completion.

**System-Imposed**

Set by Telnyx, not by API calls. The SIM cannot transition while in these states.

| Status | Meaning | How to Exit |
| --- | --- | --- |
| `data_limit_exceeded` | SIM exceeded its group's data limit. | Raise the data limit via [`PATCH /sim_card_groups/{id}`](/api-reference/sim-card-groups/update-a-sim-card-group) (group level) or [`PATCH /sim_cards/{id}`](/api-reference/sim-cards/update-a-sim-card) (SIM level), or wait for billing cycle reset. Auto-transitions to `intended_status`. |
| `unauthorized_imei` | SIM is in a device not on its `authorized_imeis` list. | Update `authorized_imeis` via [`PATCH /sim_cards/{id}`](/api-reference/sim-cards/update-a-sim-card) to add the current IMEI or clear the list. Then re-enable with [`POST /sim_cards/{id}/actions/enable`](/api-reference/sim-cards/request-a-sim-card-enable). |
| `blocked` | Account-level service interruption (billing). | Resolve account billing issue. Auto-syncs back to intended state. |
| `abolished` | Account-level service interruption (billing). | Resolve account billing issue. Auto-syncs back to intended state. |

### What Puts a SIM Into Each Status

The SIM must have a `sim_card_group_id` before you can enable it or set it to standby.

| Target Status | What Triggers It |
| --- | --- |
| `enabled` | [Enable SIM](/api-reference/sim-cards/request-a-sim-card-enable) — from `registered`, `disabled`, or `standby` |
| `disabled` | [Disable SIM](/api-reference/sim-cards/request-a-sim-card-disable) — from `enabled` |
| `standby` | [Set Standby](/api-reference/sim-cards/request-setting-a-sim-card-to-standby) — from `enabled` |
| `data_limit_exceeded` | System — SIM exceeded its group or SIM-level data limit. Adjust via [Update Group](/api-reference/sim-card-groups/update-a-sim-card-group) or [Update SIM](/api-reference/sim-cards/update-a-sim-card). |
| `unauthorized_imei` | System — SIM inserted into a device not in its `authorized_imeis` list. Fix via [Update SIM](/api-reference/sim-cards/update-a-sim-card). |
| `blocked` / `abolished` | System — account-level billing interruption. Resolve with Telnyx support. |

### Deletion

[`DELETE /sim_cards/{id}`](/api-reference/sim-cards/deletes-a-sim-card) permanently deregisters the SIM. This is irreversible:

- **Physical SIMs** — the plastic is now waste. You'd need to order and register a new one.
- **eSIMs** — the profile is gone. You'd need to purchase a new eSIM.

Prefer disable or standby if there's any chance you'll need the SIM again.

For eSIMs that can't be uninstalled from a device, pass `report_lost=true` — this is irreversible and the eSIM cannot be re-registered.
