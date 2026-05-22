---
title: Telnyx Wireless IoT SIMs — Overview and Getting Started
summary: 'Learn how Telnyx Wireless gives API control over cellular connectivity for
  IoT: order and provision SIMs and eSIMs, manage lifecycle and multi-IMSI behavior,
  route data, enable VoLTE and messaging, control costs, automate bulk actions, monitor
  usage, and troubleshoot connectivity.'
sources:
- url: https://developers.telnyx.com/docs/iot-sim/wireless-overview/index
  content_hash: e723de2865dd8412703c42b93bc8dbb111d2ae01ce78fb04376d6a70dd79a675
- url: https://developers.telnyx.com/docs/iot-sim/get-started/index
  content_hash: 45e363f0a3060a760f09ae4f5e027f38f65d6cd59090e259899466a84a8449ce
- url: https://developers.telnyx.com/docs/iot-sim/ordering-sims/index
  content_hash: c071f171ac1923cf0adad5bb4a8efd621b4ad086c4fa641631a1873804f3a3fa
- url: https://developers.telnyx.com/docs/iot-sim/iot-pricing
  content_hash: d539997eabef21a5402eb993e42a9655aaff7e3e586fd638b3312e203022dc01
- url: https://developers.telnyx.com/docs/iot-sim/connectivity-troubleshooting/index
  content_hash: 6e8e5d0e5df5741ae626c8812ce5d420b804455b5afd28606f61567cfce20cb1
- url: https://developers.telnyx.com/docs/iot-sim/bulk-sim-actions/index
  content_hash: 2c36cef2e32059565e75d61bbec317f19136b8754db9beddf8e447595194f4ed
- url: https://developers.telnyx.com/docs/iot-sim/data-usage-notifications
  content_hash: 9a29e68a9d37cc9f5b305abafac5c5a57259ededa7fbf0b9112ce99594475d1c
updated_at: 2026-05-20T08:37:48Z
---

# Telnyx Wireless IoT SIMs — Overview and Getting Started

Learn how Telnyx Wireless gives API control over cellular connectivity for IoT: order and provision SIMs and eSIMs, manage lifecycle and multi-IMSI behavior, route data, enable VoLTE and messaging, control costs, automate bulk actions, monitor usage, and troubleshoot connectivity.

## What you can do with Telnyx Wireless
- API-manage cellular connectivity for IoT fleets: provision SIMs/eSIMs, group and configure at scale.
- Route data over the public internet, via Private Wireless Gateways, or assign public IPs for inbound access.
- Enable VoLTE and full Telnyx voice features; add SMS/MMS/RCS for a carrier-grade messaging experience.

## SIM types and core resources
- SIM types
  - Physical SIM card: triple-cut (2FF/3FF/4FF), shipped.
  - eSIM: downloadable profile for phones/tablets/laptops (not embedded hardware).
- Core resources (all API-managed)
  - SIM Card: the connectivity entity (ICCID, status, data settings, optional voice/messaging enablement). eSIMs become standard SIM Card resources after OTA provisioning.
  - SIM Card Group: set shared data limits, network preferences, Private Wireless Gateway configs, etc., for many SIMs at once. See [SIM Card Groups](sim-card-groups.md).
  - Mobile Phone Number (optional): created when you enable voice or messaging; controls call routing, caller ID, and messaging profile.

## Ordering physical SIMs
- Order in Mission Control Portal (not via API). Telnyx ships triple-cut SIMs.
- Register: use the 10‑digit registration code printed on the card. Register in Portal (single or CSV) or via API (POST /actions/register/sim_cards). Assign a SIM Card Group and optional tags.
- Enable: activate on network via Portal or API (POST /sim_cards/{id}/actions/enable).
- After registration, manage entirely through the SIM Card API and groups.

## Purchasing and activating eSIMs
- Buy in Portal or via API (POST /actions/purchase/esims). Purchase is immediate; assign group, set initial status, add tags. eSIM one-time activation fee applies; no shipping.
- You receive an activation code immediately; provision via QR code or manual entry on the device. No separate registration step.
- Activation codes are one-time use. If a profile is lost, purchase a new eSIM.
- After provisioning, eSIMs are standard SIM Card resources with identical API operations.
- For eUICC hardware solutions, contact Telnyx Sales.

## SIM lifecycle states
Typical flow: Order → Register → enabled → Active use → disabled/standby.
- registered: SIM is in your account (not yet attached to network). Incurs standard monthly charge.
- enabled: active on network and able to consume data.
- disabled or standby: off network at reduced monthly cost; retains configuration for quick re-enable.
See [SIM Lifecycle](sim-lifecycle.md) for state transitions and API operations.

## Multi‑IMSI and network selection
- Each SIM carries multiple IMSIs (e.g., Telnyx, Sparkle, BICS, T‑Mobile, US Cellular). An on‑SIM applet automatically selects the best IMSI per location for local attachment, lower latency, and better rates.
- Default is automatic selection. You can override to manual per‑SIM or per‑group via API for testing or regulatory needs.

## Data connectivity options
- Public internet with NAT.
- Private routing via Private Wireless Gateways for enterprise/private networks. See [Private Wireless Gateways](private-wireless-gateways.md) and [Private Wireless Gateway Setup](private-wireless-gateway-setup.md).
- Optional public IP assignment for inbound traffic to devices. See [Public IPs](public-ips.md).
- Fine-tune traffic with [Traffic Policy Profiles](traffic-policy-profiles.md) and protect fleets with [Wireless Blocklists](wireless-blocklists.md).

## Voice (VoLTE) and messaging
- Enable VoLTE to add a second line or use Telnyx voice features (Call Control, AI agents, recording, IVR) over cellular.
- Enable SMS/MMS/RCS for a full carrier-grade messaging experience.
- Enabling voice or messaging creates a Mobile Phone Number resource linked to the SIM.

## Pricing at a glance
- One-time charges (OTC)
  - Physical SIMs: per‑SIM fee; shipments outside the U.S. mainland incur an additional shipping charge.
  - eSIMs: $0.70 one‑time activation; delivered over the air (no shipping).
- Monthly recurring charges (MRC)
  - $2 per registered SIM (whether or not currently attached to the network).
  - Reduced to $0.20 per SIM when disabled/standby.
- Data usage
  - Billed for upload+download on a tiered basis by country zone and account‑level usage volume (9 zones).
  - See the full country‑to‑zone and rate breakdown: https://support.telnyx.com/en/articles/3296669-programmable-wireless-pricing
Also see [IoT Pricing](iot-pricing.md) for a structured overview.

## Bulk operations
- Use bulk actions for one‑time changes on explicit SIM lists (async submit + action ID + status polling). Ongoing policies should be applied via [SIM Card Groups](sim-card-groups.md).
- Available bulk actions include: enable/disable voice, set public IPs, and validate registration codes before bulk registration.
- Track progress and per‑SIM results via bulk action APIs. See [Bulk Operations](bulk-operations.md) for details.

## Monitoring usage and alerts
- Data limits
  - Group-level: set on a SIM Card Group; all SIMs share the limit. SIMs exceeding it enter data_limit_exceeded. Resets monthly.
  - Per‑SIM override: set data_limit on an individual SIM.
- Per‑SIM usage notifications: create threshold alerts (list/create/get/update/delete via SIM card data usage notifications APIs).
- Monitor consumption
  - Per group: GET /sim_card_groups/{id} (consumed_data) and Portal group settings.
  - Per SIM: usage in the SIM Card detail response.
See [Data Usage Notifications](data-usage-notifications.md) for workflows.

## Connectivity troubleshooting
- Device configuration checklist
  - Enable cellular data and roaming.
  - Network mode: allow 3G/LTE or 4G/LTE; initial registration may require at least 3G.
  - APN: Name Telnyx, APN data00.telnyx (leave other APN fields blank). On Android: Settings → Mobile Networks → Access Point Names; on iOS: Settings → Cellular → Mobile Data → APN.
  - Update device firmware, then reboot.
- Check connectivity logs
  - In Portal (SIM ICCID → Connectivity Logs) or via API: GET /sim_cards/{id}/wireless_connectivity_logs.
  - Log type shows Registration vs Data; MCC/MNC indicate country/carrier.
- Diagnose patterns
  - No logs at all: device not reaching Telnyx (unsupported network, misconfiguration, or SIM disabled). Scan and manually select a network; verify config; check SIM status and data limits/billing.
  - Multiple registrations, no data: likely authentication/roaming/APN issue. Enable data roaming and confirm APN data00.telnyx.
  - Registration succeeds, no data sessions: enable data roaming and confirm APN.
See [SIM Connectivity Troubleshooting](sim-connectivity-troubleshooting.md) and [Wireless Detail Records](wireless-detail-records.md) for deeper diagnostics, and [OTA Updates](ota-updates.md) for managing on‑device profiles.
