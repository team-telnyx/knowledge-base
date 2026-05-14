---
title: 'Telnyx Wireless IoT: Complete Guide'
summary: Plan, deploy, and operate Telnyx IoT SIM fleets — from ordering SIMs and
  configuring devices, to routing traffic with Private Wireless Gateways, enabling
  VoLTE voice, enforcing policies, monitoring usage, and troubleshooting connectivity.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/at-commands
- url: https://developers.telnyx.com/docs/iot-sim/bulk-sim-actions
- url: https://developers.telnyx.com/docs/iot-sim/call-forwarding-recording
- url: https://developers.telnyx.com/docs/iot-sim/connectivity-troubleshooting
- url: https://developers.telnyx.com/docs/iot-sim/cradlepoint-ibr200-cellular
- url: https://developers.telnyx.com/docs/iot-sim/data-usage-notifications
- url: https://developers.telnyx.com/docs/iot-sim/edge-deployment
- url: https://developers.telnyx.com/docs/iot-sim/get-started
- url: https://developers.telnyx.com/docs/iot-sim/glmifi-router
- url: https://developers.telnyx.com/docs/iot-sim/messaging-settings
- url: https://developers.telnyx.com/docs/iot-sim/mikrotik-wap-lte
- url: https://developers.telnyx.com/docs/iot-sim/mobile-phone-numbers
- url: https://developers.telnyx.com/docs/iot-sim/nordic-semiconductor
- url: https://developers.telnyx.com/docs/iot-sim/ordering-sims
- url: https://developers.telnyx.com/docs/iot-sim/ota-updates
- url: https://developers.telnyx.com/docs/iot-sim/particle-boron-lte-kit
- url: https://developers.telnyx.com/docs/iot-sim/pepwave-max-br1-mini-lte
- url: https://developers.telnyx.com/docs/iot-sim/private-wireless-gateway-how-to
- url: https://developers.telnyx.com/docs/iot-sim/private-wireless-gateways
- url: https://developers.telnyx.com/docs/iot-sim/public-ips
- url: https://developers.telnyx.com/docs/iot-sim/sim-card-groups
- url: https://developers.telnyx.com/docs/iot-sim/sim-lifecycle
- url: https://developers.telnyx.com/docs/iot-sim/sim7600-a-rasp-pui-hat
- url: https://developers.telnyx.com/docs/iot-sim/sixfab-cellular-iot-hat
- url: https://developers.telnyx.com/docs/iot-sim/sixfab-rasp-pi-hat
- url: https://developers.telnyx.com/docs/iot-sim/traffic-policy-profiles
- url: https://developers.telnyx.com/docs/iot-sim/voice-enabled-iot
- url: https://developers.telnyx.com/docs/iot-sim/wireless-blocklists
- url: https://developers.telnyx.com/docs/iot-sim/wireless-detail-records
- url: https://developers.telnyx.com/docs/iot-sim/wireless-overview
updated_at: 2026-05-14T09:52:56Z
---

# Telnyx Wireless IoT: Complete Guide

*Part 1 of 2 — see also: [Part 2](telnyx-wireless-iot-complete-guide--part-2.md)*

Plan, deploy, and operate Telnyx IoT SIM fleets — from ordering SIMs and configuring devices, to routing traffic with Private Wireless Gateways, enabling VoLTE voice, enforcing policies, monitoring usage, and troubleshooting connectivity.

## Platform overview
Telnyx Wireless gives API control over cellular connectivity for IoT: provision SIMs and eSIMs, route data over the public internet or private networks, enable VoLTE calling, and manage messaging — all in one platform. See [Wireless Overview](wireless-overview.md).

## SIMs and eSIMs
- Types: physical triple‑cut SIM cards and downloadable eSIM profiles (all eUICC‑enabled). See [SIMs & eSIMs](sims-esims.md).
- Ordering: physical SIMs via the Mission Control Portal; register using the 10‑digit code (portal or API), then enable on network. eSIMs are purchased via portal or API and provisioned OTA with an activation code — no shipping or registration. See [SIM Cards](sim-cards.md).
- Resource model: SIM Card (connectivity entity), SIM Card Group (fleet policy), optional Mobile Phone Number (created when you enable voice/messaging). See [SIMs & eSIMs](sims-esims.md).
- Multi‑IMSI: each SIM carries multiple IMSIs; an on‑SIM applet auto‑selects the best profile per location for lower latency and better rates. You can override selection per SIM or group.
- Lifecycle: enable, disable, or set standby (preserves IP while off‑network). Transitions are async and return SIM Card Actions for polling. System‑imposed states include data_limit_exceeded, unauthorized_imei, and billing holds. See [SIM Lifecycle](sim-lifecycle.md).
- Pricing highlights: one‑time SIM/eSIM fees, monthly $2/active SIM, $0.20/disabled or standby, and data billed by zone/volume. Full details: https://support.telnyx.com/en/articles/3296669-programmable-wireless-pricing

## Device configuration basics
- APN: use data00.telnyx unless otherwise noted. Leave username/password blank.
- Enable data, roaming, and 3G/LTE or LTE‑only modes; keep device firmware current and reboot after changes.
- First network attach can take up to 30 minutes as the SIM discovers optimal operators.

## Groups vs bulk operations
- Groups: ongoing policy that all member SIMs inherit (data limits, PWG, blocklists, traffic policies). Moving SIMs between groups can briefly interrupt connectivity. See [SIM Card Groups](sim-card-groups.md).
- Bulk: one‑time async actions on an explicit SIM list (e.g., enable/disable voice, set public IPs, validate registration codes). Track via bulk action IDs. See [Bulk Operations](bulk-operations.md).

## Network routing options
- Default (NAT private IP): outbound internet only with dynamic private IPs per session.
- Public static IPs: make devices reachable from the internet; set or remove per SIM (async actions). $3/month per SIM. See [Public IPs](public-ips.md).
- Private Wireless Gateways (PWG): route SIM traffic through your own private IP network (VRF on Telnyx MPLS) via WireGuard Cloud VPN or VXC; devices are addressable like any internal host. Assign at the group level. See [Private Wireless Gateways](private-wireless-gateways.md).
  - APN‑based IP assignment: data.net gives a static IP across sessions; data00.telnyx gives dynamic IPs.
  - Current limitations: region availability (Ashburn, VA), default IP range 100.64.199.0/24, no internet access by default (request to open as needed).
  - Setup: create a Network (Cloud VPN), create PWG in the same region, assign the PWG to a SIM Group, and coordinate default gateway routing with Telnyx Support. See [How to set up a Private Wireless Gateway](how-to-set-up-a-private-wireless-gateway.md).
- Traffic Policy Profiles: network‑level allow/deny/throttle by services, IP ranges, or domains; assign per group. See [Traffic Policy Profiles](traffic-policy-profiles.md).
- Wireless Blocklists: restrict network attachment by country, MCC, or specific PLMN; assign one blocklist per group. See [Wireless Blocklists](wireless-blocklists.md).

## Edge and private access example
A common pattern is placing a Cradlepoint device at the edge with a Telnyx SIM, bridging it into your cloud VPC over WireGuard, and assigning a PWG so the SIM only has private access. You can then SSH to the device over its private SIM IP without any public internet exposure. Step‑by‑step: [Tutorial: Edge Device Deployment](tutorial-edge-device-deployment.md).

## Voice on IoT (VoLTE) and phone numbers
- Enabling voice: trigger per‑SIM actions to enable/disable voice (optionally associate a Mobile Voice Connection). Voice assigns a real +E.164 Mobile Phone Number; inbound rings the device natively and outbound presents your caller ID. See [Mobile Phone Numbers](mobile-phone-numbers.md).
- Manage number settings via PATCH on the Mobile Phone Number resource: caller ID, tags, inbound/outbound routing, and more. See [Mobile Phone Numbers](mobile-phone-numbers.md).
- Call features: configure call forwarding (unconditional, no‑answer with timeout, busy), call recording (inbound/outbound/both), and inbound call screening (flag or reject based on reputation, number validity, and SHAKEN/STIR). Screened results are included in webhooks. See [Call Forwarding, Recording & Screening](call-forwarding-recording-screening.md).
- Mobile Voice Connection: controls webhooks, failover URL, timeouts, and routing logic for numbers. See [Mobile Phone Numbers](mobile-phone-numbers.md).
- VoLTE note: currently in beta with expanded docs coming. See [VoLTE](volte.md).

## Messaging
Messaging (SMS/MMS/RCS) on cellular numbers is part of the platform; IoT messaging configuration docs are forthcoming. See [Messaging](messaging.md).

## Usage limits, monitoring, and telemetry
- Data limits: set monthly caps at group level (shared) or override per SIM. Exceeding places SIMs into data_limit_exceeded until the limit is raised or the cycle resets. See [Data Usage Notifications](data-usage-notifications.md) and [SIM Card Groups](sim-card-groups.md).
- Per‑SIM usage notifications: create threshold alerts via API; list, get, update, and delete as needed. See [Data Usage Notifications](data-usage-notifications.md).
- Connectivity logs: per‑SIM recent events (registration and data sessions) via portal or API — includes IMSI/IMEI, RAT, MCC/MNC, and state. Useful for real‑time debugging. See [SIM Connectivity Troubleshooting](sim-connectivity-troubleshooting.md).
- Wireless Detail Records (WDRs): async reports with per‑session start/stop, bytes, carrier (MCC/MNC), APN, IPs, radio tech, and cell ID; download via pre‑signed URL. See [Wireless Detail Records](wireless-detail-records.md).
- OTA updates: Telnyx can push SIM‑level changes (e.g., IMSI profile switches) to your fleet; updates apply on next attach and expose status/metadata via API. See [OTA Updates](ota-updates.md).

## Connectivity troubleshooting
1) Check device config
- Enable cellular data and roaming; set network to 3G/LTE or LTE‑only.
- APN: data00.telnyx (name: Telnyx). Leave other APN fields blank.
- Update device firmware and reboot.

2) Check connectivity logs
- In portal: Wireless > SIM Cards > select ICCID > Connectivity Logs; or via API for the SIM. Inspect registration/data attempts and MCC/MNC.

3) Diagnose patterns
- No logs at all: device isn’t reaching Telnyx — scan and manually select a compatible network, verify APN/roaming, and confirm SIM status/billing/limits.
- Multiple registration attempts, no data: enable roaming and confirm APN.
- Registration succeeds, no data sessions: same as above; ensure data session creation.

If issues persist, contact Support via the Mission Control Portal. See [SIM Connectivity Troubleshooting](sim-connectivity-troubleshooting.md).
