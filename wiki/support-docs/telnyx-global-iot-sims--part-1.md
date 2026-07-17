---
title: Telnyx Global IoT SIMs
summary: Telnyx Global IoT SIMs provide data-only cellular connectivity across 180+
  countries on hundreds of networks. This page covers ordering, registration, APN
  configuration, router integration (InRouter300 and Teltonika), SIM lifecycle management,
  location and device details, international coverage, and tiered zone-based pricing.
sources:
- url: https://support.telnyx.com/en/articles/10511105-using-telnyx-sim-with-inrouter300-series-cellular-routers
- url: https://support.telnyx.com/en/articles/10511646-using-telnyx-sim-with-teltonika-4g-lte-routers
- url: https://support.telnyx.com/en/articles/1130664-countries-that-telnyx-offers-termination-in
- url: https://support.telnyx.com/en/articles/1424680-international-coverage
- url: https://support.telnyx.com/en/articles/3269600-how-to-set-up-a-telnyx-sim-card
- url: https://support.telnyx.com/en/articles/3269973-adding-the-telnyx-sim-apn-to-your-device
- url: https://support.telnyx.com/en/articles/3270106-international-iot-sim-coverage
- url: https://support.telnyx.com/en/articles/3270136-telnyx-global-sims-faqs
- url: https://support.telnyx.com/en/articles/3296669-iot-sim-card-pricing
- url: https://support.telnyx.com/en/articles/3371977-international-roaming-partners
- url: https://support.telnyx.com/en/articles/4298710-sim-setup-and-configuration
- url: https://support.telnyx.com/en/articles/5812302-sim-card-location-and-device-details
- url: https://support.telnyx.com/en/articles/5812328-sim-card-actions
- url: https://support.telnyx.com/en/articles/7966416-telnyx-iot-sim-data-usage-zone-mapping
- url: https://support.telnyx.com/en/collections/1895859-telnyx-global-iot-sims
updated_at: 2026-07-17T08:59:59Z
---

# Telnyx Global IoT SIMs

*Part 1 of 2 — see also: [Part 2](telnyx-global-iot-sims--part-2.md)*

Telnyx Global IoT SIMs provide data-only cellular connectivity across 180+ countries on hundreds of networks. This page covers ordering, registration, APN configuration, router integration (InRouter300 and Teltonika), SIM lifecycle management, location and device details, international coverage, and tiered zone-based pricing.

## Overview

Telnyx Global IoT SIMs provide cellular connectivity for Internet of Things (IoT) and industrial deployments. The Telnyx SIM card is data-only, supports two-way SMS via AT commands, and works internationally across hundreds of networks in over 180 countries. SIMs are available as triple-cut plastic cards, embedded MFF2 chips, and over-the-air eSIMs.

## Ordering and Registering a SIM

Order SIMs through the Mission Control Portal under the **Wireless** section. Allow 3–5 business days for delivery within the US; international orders may take longer than 7 business days. Orders under 50 SIMs ship via USPS; for larger orders, contact the sales team to discuss expedited shipping.

Before registering new SIMs, ensure the account has a minimum balance of $2 USD. To register:

1. Navigate to **Wireless > Register SIM Cards** in the portal.
2. Enter the 10-digit registration code printed on the SIM card. Multiple codes can be added at once, separated by commas.
3. Optionally assign tags or a SIM card group.
4. Click **Register SIM**.

Registration can also be performed programmatically via the API:

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

See the [SIM Setup and Configuration](https://support.telnyx.com/en/articles/4298710-sim-setup-and-configuration) article for full details.

## Configuring the APN on a Device

After inserting the SIM, configure the device's APN with the following values:

- **Name:** `Telnyx`
- **APN:** `data00.telnyx`

Leave all other fields unmodified (even if blank), save the new APN, and ensure it is selected as the active one. Enable data roaming on the device. Some devices may require a reboot for the changes to take effect.

APN entry locations by platform:

- **Android:** Settings > Connections > Mobile Networks > Access Point Names > Add
- **iOS:** Settings > Cellular > Mobile Data > APN

**Important:** Some providers no longer allow first-time registrations over 2G or 3G. Complete the initial registration over 4G/LTE; the SIM will then be usable on 2G and 3G.

## Router and Modem Configuration

### InRouter300 Series (IR300)

The InRouter300 Series from InHand Networks is an industrial 4G LTE router for IoT and remote networking.

**Prerequisites:**

- InRouter300 Series router (e.g., IR302)
- Active Telnyx SIM with a valid data plan
- Computer with Ethernet port, Ethernet cable, power adapter
- Default credentials: IP `http://192.168.2.1`, username `adm`, password `123456`

**Setup steps:**

1. Insert the Telnyx SIM into the router's SIM slot.
2. Connect a computer to the router's LAN port via Ethernet.
3. Power on the router and wait for boot.
4. Open `http://192.168.2.1` and log in.
5. Navigate to **Network > Cellular** and select the SIM slot.
6. Enter APN `data00.telnyx` with blank username and password, then click **Apply**.
7. (Optional) Enable Dual SIM Mode and configure failover for redundancy.

**Verifying connectivity:** Go to **Status > Network Connection** and confirm an IP address has been assigned, signal strength is adequate, and network registration is successful.

**Optional configurations:**

- **Static IP:** Under **Network > WAN Settings**, change Connection Type to `Static IP` and enter the provided IP, subnet mask, and gateway.
- **VPN:** Under **VPN > Settings**, select IPSec, OpenVPN, or PPTP and enter authentication details.
- **Firewall:** Under **Security > Firewall**, enable protection and configure custom rules.

**Backup and restore:** Under **System > Config Management**, click **Backup** to generate a `.dat` file. To restore, click **Browse**, select the file, click **Import**, and restart the router.

**Troubleshooting:**

- *No internet:* Verify the SIM is active, APN is `data00.telnyx` with no credentials, and test the SIM in another device.
- *Poor signal:* Reposition the router or attach an external 4G LTE antenna.
- *Settings not saving:* Ensure changes are Applied and Saved before rebooting; reset to factory defaults if needed.

### Teltonika 4G/LTE Routers

Teltonika LTE routers are widely used in IoT, industrial, and remote networking applications.

**Initial setup:**

1. Power off the router and insert the Telnyx SIM into the designated slot.
2. Power on the router and connect a computer to the LAN port via Ethernet.
3. Open `http://192.168.2.1` in a browser.
4. Log in with username `admin` and the password printed on the router label (you may be prompted to change it on first login).

**APN configuration:**

1. Navigate to **Network > Interfaces**.
2. Click the pencil icon next to `mob1s1a1`.
3. Uncheck **Auto APN** and enter APN `data00.telnyx` with blank username and password.
4. Click **Save & Apply**.

**Verifying connectivity:** Go to **Status > Network Information** and confirm a connected status, assigned IP address, and usable signal strength.

**Auto-reboot for network recovery (recommended):**

1. Navigate to **System > Auto Reboot**.
2. Enable **Auto Reboot** and select **Ping Reboot** with targets such as `8.8.8.8` and `1.1.1.1`.
3. Set ping interval (e.g., 60 seconds) and retry count (e.g., 3 failures).
4. Optionally enable **Scheduled Reboot** (e.g., daily at 3 AM).
5. Click **Save & Apply**.

**Teltonika RMS for fleet management:** Teltonika RMS is a cloud-based platform for centralized management of large router fleets. It provides real-time monitoring, remote firmware and configuration updates, command-line access, batch operations, VPN setup, and alerts. Sign up at rms.teltonika-networks.com and register each device using the unique RMS code found under **System > RMS** in the web UI.

**Firmware and security:**

- Update firmware under **System > Firmware**.
- Configure firewall under **Network > Firewall**.
- VPN support (OpenVPN, WireGuard, IPsec) is available under **VPN**.

**Backup:** Under **System > Backup**, click **Generate** and download the backup file.

**Troubleshooting:**

- *No internet:* Confirm the SIM is active, APN is correct, signal is sufficient, and auto-reboot is configured.
- *Weak signal:* Move the router or attach external antennas.

## SIM Card Actions and Lifecycle

Every update to a SIM card is tracked as an action in the Mission Control Portal and API. The actions section is found by drilling into a SIM card in the SIM cards view and scrolling to the bottom. Each action is logged in chronological order with an associated status.

Tracked operations include:

- Enable SIM card
- Disable SIM card
- Standby SIM card
- Data Limit exceeded
- Enable Standby SIM card

SIM state can be changed via the Portal or the [Get SIM Cards API endpoint](https://developers.telnyx.com/api/wireless/get-sim-cards). There are no additional fees for changing SIM state.

## SIM Location and Device Details

An estimate of a SIM card's location can be viewed in the Mission Control Portal and via the API. Location is derived from the cell tower to which the SIM is connected and is shown as a circle on a map; more powerful towers produce a larger error radius.

The API `/sim_cards` endpoint returns a nested object:

```
"current_device_location": {
      "accuracy": 1250,
      "accuracy_unit": "m",
      "latitude": "41.143",
      "longitude": "-8.605"
    },
```

Device details exposed in the portal include device type, model name, and IMEI. The API additionally exposes brand name and operating system. The IMEI can be added to the authorized IMEIs field to lock the SIM to a specific device.
