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

*Part 2 of 2 — see also: [Part 1](telnyx-iot-sim-wireless--part-1.md)*

Telnyx IoT SIM cards provide global cellular connectivity for IoT devices, supporting both physical triple-cut SIMs and over-the-air eSIMs. The platform offers API-managed resources for SIM lifecycle, data limits, bulk operations, voice features, and private networking via Wireless Gateways.

## Call Forwarding, Recording, and Screening

All settings below are configured via `PATCH /mobile_phone_numbers/{id}`.

### Call Forwarding

Set the `call_forwarding` object to route calls when the device is unavailable:

| Type | Behavior |
|---|---|
| `unconditional` | All calls forward immediately — device never rings |
| `no_answer` | Forward after timeout (device rings first) |
| `busy` | Forward when line is in use |

Forward to any number — landline, mobile, SIP connection, or Call Control application.

### Call Recording

Set `call_recording` to record inbound, outbound, or both. Recordings are accessible through the standard Telnyx Recordings API — same storage, retrieval, and webhooks as Call Control recordings.

### Inbound Call Screening

Inbound Call Screening automatically blocks or flags inbound calls based on caller reputation and SHAKEN/STIR attestation. The feature is free on any number.

Screening evaluates three factors:

| Factor | Description |
|---|---|
| **Number Reputation** | Cross-references caller identity against CallerAPI, Nomorobo, and YouMail databases |
| **Number Validation** | Checks whether the originating number is valid and exists |
| **SHAKEN/STIR Attestation** | Validates Caller ID authenticity — screens calls with Attestation C (unauthenticated) or Invalid (certificate error) |

Handling modes:

| Mode | Behavior |
|---|---|
| **Flag** | Call connects but displays "SPAM LIKELY" in the From and P-Asserted-ID headers. A custom SIP header carries the screening status for routing logic. |
| **Reject** | Call is blocked at the network level and never reaches your infrastructure. |

Enable via the Mission Control Portal (**My Numbers** → select number → **Edit** → **Voice** tab → **Inbound Call Screening**) or by setting the `inbound_call_screening` field via API. Enable webhooks to receive the `call_screening_result` field in the `call.initiated` webhook payload. Number reputation screening applies to US and Canada calls; SHAKEN/STIR screening applies to North America.

### Other Settings

| Setting | Description |
|---|---|
| `noise_suppression` | AI noise reduction for loud environments |

### Example Payload

```json
{
  "call_forwarding": {
    "forwarding_type": "no_answer",
    "forwarding_number": "+15551234567",
    "timeout_secs": 30
  },
  "call_recording": {
    "inbound": "enabled",
    "outbound": "disabled"
  },
  "noise_suppression": "enabled"
}
```

## Connectivity Troubleshooting

### Step 1: Check Device Configuration

Verify the APN, roaming, network mode, and firmware as described in the [#APN and Device Configuration](apn-and-device-configuration.md) section above.

### Step 2: Check Connectivity Logs

View logs via the [portal](https://portal.telnyx.com/#/app/wireless/sim-cards) (click SIM ICCID → Connectivity Logs) or API:

```
GET /sim_cards/{id}/wireless_connectivity_logs
```

The `type` column shows `Registration` or `Data`. MCC identifies the country, MNC identifies the carrier.

### Step 3: Diagnose Patterns

| Pattern | Likely Cause | Fix |
|---|---|---|
| No connectivity logs at all | Connection not reaching Telnyx; device on inaccessible network; misconfigured or deactivated SIM | Scan networks and manually select one. Verify device config. Check SIM status in portal — may be disabled due to data limit or billing. |
| Multiple registration attempts, no data | SIM not authenticating | Enable data roaming. Verify APN is `data00.telnyx`. |
| Registration succeeds but no data sessions | Data sessions not being created | Enable data roaming. Verify APN is `data00.telnyx`. |

If issues persist, contact support via the Mission Control Portal.

## Device Setup Guides

### Cradlepoint IBR200

The compact, semi-ruggedized IBR200 LTE router is designed for secure, cloud-managed IoT networking. A NetCloud Essentials Cloud subscription is required for full functionality, but basic connectivity does not require it.

Setup steps:

1. Insert the Telnyx SIM card (standard size — the largest from your SIM kit) into the Cradlepoint device.
2. Power on the device.
3. Open a browser and navigate to `192.168.0.1`. Default credentials: **Username** `admin`, **Password** = the serial number on the bottom label.
4. Click **Connection Manager** → **Add**.
5. Configure the WAN Interface Profile: **Profile name** `Telnyx SIM`, **Type** `Modem`, leave everything else unchecked.
6. On the next page, click **SIM/APN/Auth**: set **SIM Card Lock** to *No Pin Required*, **Access Point Name (APN)** to *Default Override*, and enter `data00.telnyx`.
7. Click **Save**. The device may take up to 30 minutes for the first network attach. Once connected, that network is added to the priority list for faster future connections.

### GL-MiFi 4G Smart Router

1. Insert the SIM card with the gold chip facing up.
2. Power on and connect via Ethernet or WiFi (default WiFi credentials are on the bottom label).
3. Navigate to `192.168.8.1` and log in (default password: `admin`).
4. Click **manual setup** in the Cellular Modem Overview section. Enter: **Device** `/dev/cdc-wdm0`, **APN** `data00.telnyx`, then click **Apply**.
5. Verify connectivity on the gateway overview page — it should show a Disconnect button, IP address, and data usage.

## Edge Deployment with Private Wireless Gateways

A Private Wireless Gateway (PWG) places SIMs on a private network (VRF) with no public internet access, enabling direct reachability from your cloud infrastructure. The following example deploys a Cradlepoint IBR200 at the edge of a corporate network in Digital Ocean.

### Architecture

A Digital Ocean Droplet connects to a VRF-defined network on the Telnyx MPLS backbone via a Wireguard client. A private packet gateway is spun up in the Telnyx mobile core for the SIM and added to the same VRF. The Cradlepoint device receives a private IP from the packet gateway, making it directly accessible from the cloud server.

### Setup Steps

1. **SIM Card Setup** — Order and register a Telnyx SIM. Set the APN to `data00.telnyx` in the Cradlepoint device.
2. **Cloud VPN Setup** — Configure a Wireguard client on a Digital Ocean Droplet to connect to a Cloud VPN on the Telnyx MPLS backbone. Verify by pinging the server endpoint on the Telnyx network.
3. **Cradlepoint IBR200 Setup** — Follow the [#Cradlepoint IBR200](cradlepoint-ibr200.md) setup guide above to establish basic internet connectivity first.
4. **Private Wireless Gateway Setup** — Create a PWG in the [portal](https://portal.telnyx.com/#/app/wireless/private-wireless-gateways) by selecting the Network resource used for the Cloud VPN. The PWG may take up to 15 minutes to provision. Once status is **provisioned**, associate the SIM Group with the PWG. SIMs in the group will lose public internet access and route through the private gateway. You can now ping the SIM's private IP from the Digital Ocean Droplet.
5. **Cradlepoint SSH Configuration** — Enable SSH access on the Cradlepoint via the Administration page: navigate to **System** → **Administration** → **Local Management** → check **Enable SSH Server**. For remote access from the corporate network, select **Remote Admin** and check **Allow Remote SSH Access**. If needed, enable **Allow Weak Cipher Support** under System > Administration > Local Management. Connect from the Linux server with `ssh admin@[SIM_CARD_IP]`.

> **Note:** By default, SIMs associated with a PWG lose access to the public internet.
