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

*Part 3 of 6 — see also: [Part 1](wireless--part-1.md), [Part 2](wireless--part-2.md), [Part 4](wireless--part-4.md), [Part 5](wireless--part-5.md), [Part 6](wireless--part-6.md)*

Telnyx Wireless provides API-driven cellular connectivity for IoT and mobile devices. This page covers SIM and eSIM provisioning, lifecycle management, SIM Card Groups, bulk operations, data routing (public IPs, Private Wireless Gateways, Traffic Policy Profiles, Wireless Blocklists), data usage monitoring and notifications, Wireless Detail Records, OTA updates, VoLTE with mobile phone numbers and call features, IoT pricing, connectivity troubleshooting, AT commands, and step-by-step setup guides for a range of supported devices including Raspberry Pi HATs, Particle Boron, Nordic nRF9160, Cradlepoint IBR200, Pepwave Max BR1 Mini, GL-MiFi, and Mikrotik wAP LTE.

## Data

### Public IPs

By default, SIMs get dynamic private IPs — reachable outbound only. A public static IP makes the SIM reachable from the internet ($3/mo per SIM).

| Action | Endpoint |
| --- | --- |
| [Get Public IP](/api-reference/sim-cards/get-sim-card-public-ip-definition) | `GET /sim_cards/{id}/public_ip` |
| [Set Public IP](/api-reference/sim-cards/request-setting-a-sim-card-public-ip) | `POST /sim_cards/{id}/actions/set_public_ip` |
| [Remove Public IP](/api-reference/sim-cards/request-removing-a-sim-card-public-ip) | `POST /sim_cards/{id}/actions/remove_public_ip` |
| [Bulk Set Public IPs](/api-reference/sim-cards/request-bulk-setting-sim-card-public-ips) | `POST /sim_cards/actions/bulk_set_public_ips` |

**When to Use**

- **Inbound access** — connect *to* your SIM from anywhere (SSH, remote management, server-initiated requests)
- **Firewall allowlists** — stable IP for access control rules
- **Device-as-server** — run services on the device that external systems call into

### Private Wireless Gateways

A Private Wireless Gateway (PWG) routes all SIM traffic through your own private network. SIMs connected via a PWG sit inside your private IP space — not on the public internet.

**Why PWG**

- **Security** — SIMs are not directly exposed to the internet
- **Control** — route traffic through your own firewall or DLP platform
- **Direct access** — devices are addressable on your corporate network like any other host

**Architecture**

PWGs connect to a VRF-defined network on Telnyx's MPLS backbone. Virtual Cross Connects (VXC) or WireGuard interfaces (Cloud VPNs) bridge this to your corporate network. All interfaces on the same VRF can see each other.

![Private Wireless Gateways](https://mintcdn.com/telnyx/Iu93-l5Bj6hMoe-q/img/edge_device_deployment__1_.svg?fit=max&auto=format&n=Iu93-l5Bj6hMoe-q&q=85&s=8741828382ea5747a8e6ffc471695d36)

**API**

| Action | Endpoint |
| --- | --- |
| [List PWGs](/api-reference/sim-cards/get-all-private-wireless-gateways) | `GET /private_wireless_gateways` |
| [Create PWG](/api-reference/sim-cards/create-a-private-wireless-gateway) | `POST /private_wireless_gateways` |
| [Get PWG](/api-reference/sim-cards/get-a-private-wireless-gateway) | `GET /private_wireless_gateways/{id}` |
| [Delete PWG](/api-reference/sim-cards/delete-a-private-wireless-gateway) | `DELETE /private_wireless_gateways/{id}` |

Assign a PWG to a SIM Card Group via [SIM Card Groups](sim-card-groups.md). All SIMs in the group route through the PWG.

**APN-based IP Assignment**

| APN | IP Assignment |
| --- | --- |
| `data.net` | Static — same IP across sessions |
| `data00.telnyx` | Dynamic — new IP each session |

To use a static IP, your device must connect using the `data.net` APN. Devices on `data00.telnyx` get dynamic IPs.

**Limitations**

- **Region** — PWGs are currently only available in Ashburn, VA. More regions coming.
- **IP range** — Default `100.64.199.0/24` (254 concurrent SIMs). Custom ranges coming.
- **Internet access** — PWGs have no internet access by default. Contact support to open your VRF to the internet.

### Setting Up a Private Wireless Gateway

**Step 1: Set up Cloud VPN**

1. Navigate to the [Network section](https://portal.telnyx.com/#/app/next/networking/networks) in the portal. Select "Create Network".
2. Set the network name and click "Create".
3. Add a VPN Interface, create a name, click "Create".
4. Wait for provisioning to complete, click "Next Step".
5. Add a peer for the VPN — choose a name, click "Create Peer".
6. Store the Private Key safely.
7. Skip "Buy global IP" if not needed.

**Step 2: Create a Private Wireless Gateway**

1. Select "Create PWG Interface" in the Wireless section of the portal.
2. Name it and select the network from Step 1. Region must match the VPN interface.
3. Accept the MRC charge.
4. Wait for status to transition from Provisioning to Provisioned.
5. Create a SIM Group, then edit it and click "Connect PWG" to assign the PWG.
6. Add SIM cards to the group — individually or via bulk action "Manage SIM Cards Setting".

**Step 3: Configure routing**

The network default gateway must be set up by the Telnyx Network team manually. Contact support via the Mission Control Portal chat.

Once configured, you can control which external destinations are reachable from devices connected through the PWG, and which are blocked.

### Traffic Policy Profiles

Traffic Policy Profiles define what network traffic your SIMs are allowed (or denied). Assign a profile to filter traffic at the network level before it reaches your devices.

**Profile Types**

| Type | Behavior |
| --- | --- |
| **whitelist** | Only listed traffic is allowed. Everything else is blocked. |
| **blacklist** | Listed traffic is blocked. Everything else is allowed. |
| **throttling** | Traffic is allowed but bandwidth-limited to `limit_bw_kbps`. |

**Filter Criteria**

Each profile can include one or more of:

- **services** — PCEF service IDs (predefined traffic categories). Use `GET /traffic/policy/profiles/services` to list available services.
- **ip_ranges** — CIDR notation (`10.0.0.0/8`, `203.0.113.0/24`). Block or allow specific IP ranges.
- **domains** — Domain names (`example.com`, `*.internal.corp`). DNS-level filtering.

At least one of `services`, `ip_ranges`, or `domains` is required when creating a profile.

**Example: IoT Device Lockdown**

Whitelist-only profile that restricts a fleet of sensors to your backend servers:

```
{
  "type": "whitelist",
  "ip_ranges": ["10.100.0.0/16"],
  "domains": ["api.yourcompany.com", "telemetry.yourcompany.com"]
}
```

Devices can only reach your internal network and two API endpoints. All other traffic is dropped.

**Example: Bandwidth Throttling**

Limit data-hungry devices to prevent runaway costs:

```
{
  "type": "throttling",
  "limit_bw_kbps": 256
}
```

Profiles are assigned at the SIM Card Group level. Create the profile via `POST /traffic/policy/profiles`, then reference its ID when configuring the group.

### Wireless Blocklists

Wireless Blocklists let you restrict which networks your SIMs can attach to. Assign a blocklist to a SIM Card Group and every SIM in that group is blocked from the listed networks.

**Blocklist Types**

| Type | Blocks By | Example Value | Use Case |
| --- | --- | --- | --- |
| **country** | ISO country code | `US`, `CN`, `RU` | Geo-fencing — keep devices in allowed regions |
| **mcc** | Mobile Country Code | `310` (US), `234` (UK) | Block all carriers in a country |
| **plmn** | MCC + MNC pair | `31026` (T-Mobile US) | Block a specific carrier |

Use `GET /wireless_blocklist_values` to retrieve all valid values for a given type.

**How It Works**

1. **Create a blocklist** — `POST /wireless_blocklists` with a `name`, `type`, and `values` array.
2. **Assign to a SIM Card Group** — Set `wireless_blocklist_id` on the group via `PATCH /sim_card_groups/{id}`.
3. All SIMs in that group are now blocked from the listed networks.

One blocklist per group. Changing the blocklist on a group affects all SIMs in it immediately.

**Common Patterns**

- **Geo-fencing:** Create a `country` blocklist with countries where your devices shouldn't operate. Useful for compliance, cost control, or preventing stolen device use.
- **Carrier avoidance:** Create a `plmn` blocklist to steer SIMs away from expensive or unreliable carriers in a region. The SIM's multi-IMSI applet will select the next best available network.
- **Security lockdown:** Block all networks except your target deployment region. Combined with Private Wireless Gateways, this creates a fully controlled connectivity path.

### Data Usage Notifications

**Data Limits**

Limits can be set at two levels:

| Level | Set Via | Scope |
| --- | --- | --- |
| **Group** | [`PATCH /sim_card_groups/{id}`](/api-reference/sim-card-groups/update-a-sim-card-group) | All SIMs in the group share the limit. SIMs exceeding it enter `data_limit_exceeded`. Resets monthly. |
| **SIM** | [`PATCH /sim_cards/{id}`](/api-reference/sim-cards/update-a-sim-card) | Per-SIM `data_limit` override. |

**Per-SIM Usage Notifications**

Set a threshold on individual SIMs to get notified before they hit their limit.

| Action | Endpoint |
| --- | --- |
| [List Notifications](/api-reference/sim-cards/list-sim-card-data-usage-notifications) | `GET /sim_card_data_usage_notifications` |
| [Create Notification](/api-reference/sim-cards/create-a-new-sim-card-data-usage-notification) | `POST /sim_card_data_usage_notifications` |
| [Get Notification](/api-reference/sim-cards/get-a-single-sim-card-data-usage-notification) | `GET /sim_card_data_usage_notifications/{id}` |
| [Update Notification](/api-reference/sim-cards/updates-information-for-a-sim-card-data-usage-notification) | `PATCH /sim_card_data_usage_notifications/{id}` |
| [Delete Notification](/api-reference/sim-cards/delete-sim-card-data-usage-notifications) | `DELETE /sim_card_data_usage_notifications/{id}` |

**Monitoring Consumption**

- **Per group** — `GET /sim_card_groups/{id}` returns `consumed_data`.
- **Per SIM** — visible in the SIM card detail response.
- **Portal** — Settings page shows real-time consumption per group.

### Wireless Detail Records

Wireless Detail Records (WDRs) provide granular, per-session usage data for your SIM fleet. Each record captures a single data session — when it started, how long it lasted, bytes transferred, and which network was used.

**Generating Reports**

WDR reports are async. Request one, poll for completion, download when ready.

1. **Create** — `POST /wireless/detail/records/reports` with a time range:

   ```
   {
     "start_time": "2026-04-01T00:00:00Z",
     "end_time": "2026-04-07T00:00:00Z"
   }
   ```
2. **Poll** — `GET /wireless/detail/records/reports/{id}` until `status` is `complete`.
3. **Download** — The `report_url` field contains a pre-signed URL to the report file.

**What's in a Report**

Each record includes:

| Field | Description |
| --- | --- |
| `sim_card_id` | Which SIM |
| `start_time` / `stop_time` | Session duration |
| `radio_access_technology` | LTE, 3G, etc. |
| `mobile_country_code` + `mobile_network_code` | Which carrier |
| `apn` | Access Point Name used |
| `ipv4` / `ipv6` | IP assigned during session |
| `cell_id` | Cell tower |

**Connectivity Logs**

For real-time session visibility (not batch reports), use connectivity logs:
`GET /sim_cards/{id}/wireless_connectivity_logs`
Returns recent sessions for a specific SIM, including IMSI, IMEI, radio technology, and connection state. Useful for debugging why a device can't connect or which network it attached to.

**Use Cases**

- **Billing reconciliation** — match data usage against your invoices
- **Anomaly detection** — spot SIMs consuming unexpected data volumes
- **Coverage analysis** — see which carriers your devices attach to by region
- **Troubleshooting** — correlate connectivity issues with specific cells or networks

### OTA Updates

OTA (Over-The-Air) updates let Telnyx push configuration changes to your SIMs remotely. No physical access needed — updates are delivered to the SIM's on-card applet the next time the device connects.

**What Gets Updated**

OTA updates handle SIM-level configuration: IMSI profile switches, network preference changes, and applet settings. These are not firmware updates for the device itself — they modify the SIM card's internal state. The `type` field on each update indicates the operation source and what changed.

**Tracking Updates**

List updates for your fleet:

```
GET /ota_updates
```

Or check a specific update:

```
GET /ota_updates/{id}
```

Each update includes:

| Field | Description |
| --- | --- |
| `sim_card_id` | Target SIM |
| `type` | Operation type — relates to the source of the request |
| `status` | Current state of the update |
| `settings` | JSON object with the specific changes applied |
| `created_at` | When the update was initiated |

**How It Works**

1. Telnyx queues the update for the target SIM.
2. The next time the device attaches to the network, the SIM's applet receives the update.
3. The update applies automatically. Status transitions from pending to complete (or failed).

There's no way to force immediate delivery — it depends on when the device next connects. For always-on devices this is near-instant. For devices that sleep or power cycle, it happens on next wake.

**Multi-IMSI Context**

The most common OTA operation is IMSI profile switching. Telnyx SIMs carry multiple IMSIs, and the on-card applet auto-selects the best one per location. OTA updates can override this selection or push updated IMSI profiles when Telnyx adds new carrier partnerships.
