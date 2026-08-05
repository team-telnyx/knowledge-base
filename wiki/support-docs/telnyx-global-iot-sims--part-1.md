---
title: Telnyx Global IoT SIMs
summary: A consolidated reference for Telnyx IoT SIM cards covering ordering, registration,
  APN configuration, device-specific router setup, connectivity states, pricing and
  zone mapping, international coverage, troubleshooting, and portal/API observability
  features.
sources:
- url: https://support.telnyx.com/en/articles/10164784-using-telnyx-sim-with-ubiquiti-unifi-lte-pro
- url: https://support.telnyx.com/en/articles/10511105-using-telnyx-sim-with-inrouter300-series-cellular-routers
- url: https://support.telnyx.com/en/articles/10511646-using-telnyx-sim-with-teltonika-4g-lte-routers
- url: https://support.telnyx.com/en/articles/11017501-understanding-wireless-connectivity-states-telnyx-api
- url: https://support.telnyx.com/en/articles/3269600-how-to-set-up-a-telnyx-sim-card
- url: https://support.telnyx.com/en/articles/3269973-adding-the-telnyx-sim-apn-to-your-device
- url: https://support.telnyx.com/en/articles/3270106-international-iot-sim-coverage
- url: https://support.telnyx.com/en/articles/3296669-iot-sim-card-pricing
- url: https://support.telnyx.com/en/articles/3371977-international-roaming-partners
- url: https://support.telnyx.com/en/articles/4298710-sim-setup-and-configuration
- url: https://support.telnyx.com/en/articles/5666594-sim-connectivity-logs
- url: https://support.telnyx.com/en/articles/5812302-sim-card-location-and-device-details
- url: https://support.telnyx.com/en/articles/5812328-sim-card-actions
- url: https://support.telnyx.com/en/articles/7966416-telnyx-iot-sim-data-usage-zone-mapping
- url: https://support.telnyx.com/en/collections/1895859-telnyx-global-iot-sims
updated_at: 2026-08-05T13:24:07Z
---

# Telnyx Global IoT SIMs

*Part 1 of 3 — see also: [Part 2](telnyx-global-iot-sims--part-2.md), [Part 3](telnyx-global-iot-sims--part-3.md)*

A consolidated reference for Telnyx IoT SIM cards covering ordering, registration, APN configuration, device-specific router setup, connectivity states, pricing and zone mapping, international coverage, troubleshooting, and portal/API observability features.

## Overview

Telnyx IoT SIM cards provide cellular connectivity for Internet of Things, industrial, and remote networking deployments. The SIMs are programmable, support private LTE, and are accessible through the Mission Control Portal and the Telnyx API. This page consolidates guidance on ordering, registering, configuring, monitoring, and troubleshooting Telnyx SIMs, as well as device-specific setup for supported routers and modems.

## Ordering and Registering a SIM

In the Mission Control Portal, navigate to the **Wireless** section to order a SIM card. Delivery typically takes 3–5 business days; contact [support@telnyx.com](mailto:support@telnyx.com) or use online chat to inquire about an order.

Before registering new SIMs, ensure the account has a minimum balance of $2 USD. From the **Wireless** section, open **Register SIM Cards** and enter the 10-digit registration code printed on each SIM. Multiple codes can be added at once, separated by commas. Tags and a SIM card group can be assigned during registration. Click **Register SIM** to complete the process.

Registration can also be performed programmatically:

```
curl --request POST \
  --url https://api.telnyx.com/v2/actions/register/sim_cards \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "registration_codes": [
    "0000000001",
    "0000000002",
    "0000000003"
  ],
  "sim_card_group_id": "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
  "tags": [
    "personal",
    "customers",
    "active-customers"
  ],
  "status": "enabled"
}
'
```

See the [SIM Cards API Reference](https://developers.telnyx.com/api-reference/sim-cards/register-sim-cards) for additional details.

## Configuring the APN

After inserting the SIM into the device, configure the Access Point Name (APN). On Android, APN settings are located at **Settings > Connections > Mobile Networks > Access Point Names > Add**. On iOS, they are at **Settings > Cellular > Mobile Data > APN**.

Create a new APN with the following values:

- **Name:** `Telnyx`
- **APN:** `data00.telnyx`

Leave all other fields unmodified, even if blank, and save the new APN. Enable data roaming on the device. Some devices require a reboot for the changes to take effect.

> **Important:** Some providers no longer allow first-time registrations over 2G or 3G. Complete the initial registration over 4G/LTE; the SIM will remain usable on 2G and 2G/3G thereafter.

## Ubiquiti UniFi LTE Pro Setup

The Ubiquiti UniFi LTE Pro provides backup cellular internet for a UniFi WAN network. It supports 4G LTE and WCDMA bands across the EU, US, and CA regions and includes a Nano SIM slot.

1. **Insert the SIM.** Place the Nano SIM (smallest size from the Telnyx SIM kit) into the Nano SIM slot.
2. **Power on the device.** Connect the UniFi LTE Pro to a PoE (802.3af) enabled Ubiquiti network switch.
3. **Access the UniFi console.** Open a browser and navigate to [https://unifi.ui.com](https://unifi.ui.com), then log in.
4. **Adopt the device.** Locate the UniFi LTE Pro in the device list and click **Adopt**.
5. **Configure LTE backup.** Go to **Settings > Internet > LTE Backup**, then click **Settings** in the configuration panel.
6. **Enter Telnyx APN settings.**
   - **APN:** `data00.telnyx`
   - **Authentication Type:** `NONE`
   - Click **Apply**.
7. **Verify connection.** On the **Overview** tab, confirm the **Status** is **Ready** and **Connected** is **Yes**.

### First-Time Network Attachment

Telnyx SIMs support multiple network types and operators. The first connection attempt may take up to 30 minutes to attach to a network. Once connected, the network is added to the priority operator list for faster future connections.

### Device Restart or Re-provisioning

If the device is restarted or re-provisioned, it may enter SIM-Activation mode. Resolve this by running the following command in the UniFi CLI:

```
qmicli -p -d /dev/cdc-wdm0 --wds-set-autoconnect-settings=enabled
```

## InRouter300 Series Setup

The InRouter300 (IR300) Series from InHand Networks is an industrial 4G LTE router for IoT, automation, and remote networking.

### Prerequisites

- InRouter300 Series router (e.g., IR302)
- Active Telnyx SIM with a valid data plan
- Computer with an Ethernet port
- Ethernet cable
- Power adapter
- Default credentials: IP `http://192.168.2.1`, username `adm`, password `123456`

### Physical Setup

1. Insert the Telnyx SIM into the router's SIM slot.
2. Connect the computer to the router's LAN port via Ethernet.
3. Power on the router and wait for it to boot.
4. Open a browser to `http://192.168.2.1` and log in with the default credentials.

### Cellular Configuration

1. Navigate to **Network > Cellular** and open **SIM Profiles**.
2. Select **SIM Slot 1** (or Slot 2 for a secondary SIM).
3. Enter the APN settings:
   - **APN:** `data00.telnyx`
   - **Username:** leave blank
   - **Password:** leave blank
4. Click **Apply**.

For dual-SIM redundancy, enable **Dual SIM Mode**, configure the second SIM with its carrier's APN, and set **Failover Mode** for automatic switching.

### Verifying Connectivity

Navigate to **Status > Network Connection** and confirm the router has obtained an IP address from the Telnyx network, with adequate signal strength and successful network registration. Test by opening a website or pinging an external server.

### Optional Configurations

- **Static IP:** Under **Network > WAN Settings**, change the connection type to `Static IP` and enter the provided IP, subnet mask, and gateway.
- **VPN:** Under **VPN > Settings**, select a protocol (IPSec, OpenVPN, or PPTP) and enter authentication details.
- **Firewall:** Under **Security > Firewall**, enable protection and configure custom rules.

### Configuration Backup

Under **System > Config Management**, click **Backup** to generate a `.dat` file. To restore, click **Browse**, select the file, click **Import**, and restart the router.

### Troubleshooting

- **No internet:** Confirm the SIM is active with a valid plan, verify the APN is `data00.telnyx` with no username/password, restart the router, and test the SIM in another device.
- **Poor signal:** Reposition the router or attach an external 4G LTE antenna.
- **Settings not saving:** Apply and save changes before rebooting; if needed, reset to factory defaults and reconfigure.
