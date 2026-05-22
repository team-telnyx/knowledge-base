---
title: SIM Card Groups
summary: 'SIM Card Groups let you define ongoing, inherited policy for all SIMs in
  a fleet: data caps, network access via Private Wireless Gateways, traffic filtering
  with Traffic Policy Profiles, and more. Actions are asynchronous, integrate with
  the SIM lifecycle, and can be tracked via action endpoints.'
sources:
- url: https://developers.telnyx.com/docs/iot-sim/sim-card-groups/index
  content_hash: c0b440d25855adda1798d0411f914fcf2a0b96843e58bea4ce1b0d7000d2542d
- url: https://developers.telnyx.com/docs/iot-sim/sim-lifecycle
  content_hash: 8a6c0f9993cb4673e35b3ab8631e531d7343ef5b1b7f21ee555c0db026fc30fa
- url: https://developers.telnyx.com/docs/iot-sim/messaging-settings/index
  content_hash: 531afd3a440bc703aedadf8ac6625d2082563dfa1450d562af82dbd3358a56be
- url: https://developers.telnyx.com/docs/iot-sim/traffic-policy-profiles
  content_hash: b56a212634e2b2b34c813cf6d8c0820043867fb3509bd77db93eea79246da74a
- url: https://developers.telnyx.com/docs/iot-sim/ota-updates
  content_hash: a1f969f94f63eccdd719bdd716c1d522cc70502403c56ec49f3ede85fa9edcb2
- url: https://developers.telnyx.com/docs/iot-sim/voice-enabled-iot/index
  content_hash: 5105983b368e344bca9bb439f00de92957621a17397ed21c51290f694e0492d7
- url: https://developers.telnyx.com/docs/iot-sim/edge-deployment/index
  content_hash: 5cabb7080540e087099d3a6b9f1267a157bd3cf720f971466970969ef2a67011
updated_at: 2026-05-20T08:42:56Z
---

# SIM Card Groups

SIM Card Groups let you define ongoing, inherited policy for all SIMs in a fleet: data caps, network access via Private Wireless Gateways, traffic filtering with Traffic Policy Profiles, and more. Actions are asynchronous, integrate with the SIM lifecycle, and can be tracked via action endpoints.

## Why groups (and not bulk operations)
Groups are ongoing policy containers: a SIM inherits its group’s settings as long as it remains a member. Bulk operations are one-time changes applied to an explicit list of SIMs. Use groups to centralize policy and reduce per‑SIM updates.

## Default group behavior and membership changes
- Every account has a default group; SIMs without an explicit assignment land there.
- Deleting a non-default group automatically moves its SIMs back to the default group.
- Moving active SIMs between groups can briefly interrupt connectivity while network configuration updates apply.

## Configuring group policy
Configure a group with PATCH /sim_card_groups/{id}.
- name — Display name for the group.
- data_limit — A cap defined by amount and unit (for example, 500 MB, 2 GB). When a SIM exceeds this limit it enters the data_limit_exceeded state until you increase the limit or the billing cycle resets.

Tip: Pair data limits with fleet notifications in [Data Usage Notifications](data-usage-notifications.md) so you can raise limits intentionally rather than reactively.

## Group-level network assignments
These assignments are made at the SIM Card Group level to control how member SIMs access networks and what traffic is allowed.
- Private Wireless Gateway (PWG): Assign or remove to steer traffic through a dedicated packet gateway and private network. See [Private Wireless Gateways](private-wireless-gateways.md) and [Private Wireless Gateway Setup](private-wireless-gateway-setup.md).
- Wireless Blocklist: Assign or remove to restrict network elements or roaming per your policy. See [Wireless Blocklists](wireless-blocklists.md).
- Traffic Policy Profiles: Create via POST /traffic/policy/profiles, then reference the profile on the group to filter traffic at the network edge. See [Traffic Policy Profiles](traffic-policy-profiles.md). Profile types include:
  - whitelist — Only listed traffic is allowed; everything else is blocked.
  - blacklist — Listed traffic is blocked; everything else is allowed.
  - throttling — Traffic is allowed but bandwidth-limited (limit_bw_kbps).
  Filter criteria can include services (from GET /traffic/policy/profiles/services), IP ranges (CIDR), and domains; provide at least one criterion when creating a profile.

Note: Assigning or removing PWGs and blocklists are asynchronous group actions (see next section). Profile creation is immediate, but applying the profile to a group propagates across the network and may briefly affect connectivity.

## Operations are asynchronous and traceable
Group-level network changes return an action ID and complete asynchronously.
- Track group actions with GET /sim_card_group_actions.
- Action categories include requesting assignment or removal of a Private Wireless Gateway and a Wireless Blocklist.
For per‑SIM status changes (enable/disable/standby), Telnyx returns 202 with a SIM Card Action; track via the SIM Card Actions endpoints. See [SIM Lifecycle](sim-lifecycle.md).

## Lifecycle prerequisites and status interactions
- A SIM must have a sim_card_group_id before it can be enabled or set to standby.
- User-controlled statuses:
  - enabled — On network; passes traffic.
  - disabled — Off network; IP released; $0.20/mo holding fee.
  - standby — Off network; IP preserved; $0.20/mo. Choose standby if your app depends on a stable IP.
- Transitional statuses (registering, enabling, disabling, setting_standby) reflect in‑progress, asynchronous changes; poll actions to confirm completion.
- System‑imposed statuses you may encounter due to group policy or account conditions:
  - data_limit_exceeded — Triggered when the SIM exceeds its group or SIM‑level data cap. Resolve by raising the limit via PATCH /sim_card_groups/{id} or PATCH /sim_cards/{id}, or wait for the billing cycle to reset. The SIM auto‑returns to its intended_status after resolution.
  - unauthorized_imei — Device IMEI not in the SIM’s authorized_imeis list. Update the SIM and then re‑enable.
  - blocked / abolished — Account-level billing interruption; resolve the account issue to restore service.
See details in [SIM Lifecycle](sim-lifecycle.md).

## Data caps and cost control best practices
- Define data_limit at the group level for consistent enforcement across a fleet; override at the SIM level only for exceptions.
- Use [Traffic Policy Profiles](traffic-policy-profiles.md) to whitelist required destinations and reduce accidental overages.
- Subscribe to alerts in [Data Usage Notifications](data-usage-notifications.md) before devices reach their caps.

## Managing membership, deletion, and safety
- Prefer moving SIMs between groups to change policy en masse; schedule moves during maintenance windows to avoid brief connectivity blips.
- Deleting a group is safe for SIMs (they fall back to default policy), but review differences between the source group and default to prevent unexpected access changes.

## Example: segment a device behind a Private Wireless Gateway
A common pattern is to isolate a router or gateway behind a PWG and reach it over your private network. The high‑level flow (adapted from [Edge Deployment](edge-deployment.md)):
1) Bring a SIM online in the device (for example, a Cradlepoint IBR200). Set the APN to data00.telnyx if the device requires manual APN entry.
2) Establish private connectivity from your cloud or data center (for example, a WireGuard client into Telnyx Cloud VPN) and attach it to a Telnyx Network/VRF.
3) Create a Private Wireless Gateway associated with that Network and wait until it is provisioned.
4) Assign your SIM’s group to the PWG. By default, SIMs in that group lose direct public internet access and receive an IP on your private network.
5) Verify reachability by pinging the SIM’s private IP from your cloud host, then enable remote management (for example, SSH) on the device as needed.
This pattern allows device management via private IP without exposing the fleet to the public internet.

## OTA updates context for fleet changes
Some SIM‑level network behaviors are delivered via OTA (Over‑The‑Air) updates to the on‑card applet. You can:
- List updates with GET /ota_updates and fetch details with GET /ota_updates/{id}.
- Expect delivery the next time the device attaches; there is no way to force immediate delivery for sleeping devices.
Common OTA operations include IMSI profile updates and preference changes. See [OTA Updates](ota-updates.md).

## Voice and messaging features
- VoLTE for IoT is in beta and enables assigning a mobile phone number to an eSIM‑capable device with API control. See [VoLTE](volte.md).
- Messaging configuration documentation is forthcoming. See [Messaging Settings](messaging-settings.md).
These features are configured alongside, not instead of, your group policy; group membership continues to govern data policy and network access.

## Related pages
- [Private Wireless Gateways](private-wireless-gateways.md)
- [Private Wireless Gateway Setup](private-wireless-gateway-setup.md)
- [Traffic Policy Profiles](traffic-policy-profiles.md)
- [Wireless Blocklists](wireless-blocklists.md)
- [Data Usage Notifications](data-usage-notifications.md)
- [Connectivity Troubleshooting](connectivity-troubleshooting.md)
- [Wireless Detail Records](wireless-detail-records.md)
- [OTA Updates](ota-updates.md)
- [SIM Lifecycle](sim-lifecycle.md)
- [Edge Deployment](edge-deployment.md)
