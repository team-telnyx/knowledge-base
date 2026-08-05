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

*Part 2 of 3 — see also: [Part 1](telnyx-global-iot-sims--part-1.md), [Part 3](telnyx-global-iot-sims--part-3.md)*

A consolidated reference for Telnyx IoT SIM cards covering ordering, registration, APN configuration, device-specific router setup, connectivity states, pricing and zone mapping, international coverage, troubleshooting, and portal/API observability features.

## Teltonika 4G/LTE Router Setup

Teltonika LTE routers are widely used in IoT, industrial, and remote networking applications.

### Initial Setup

1. Power off the router and insert the Telnyx SIM into the designated slot, ensuring it is securely seated.
2. Power on the router using the included adapter.
3. Connect the router's LAN port to a computer via Ethernet.

### Accessing the Web Interface

Open a browser to `http://192.168.2.1`. Default credentials are username `admin` and the password printed on the router label. A password change may be required on first login.

### Configuring the APN

1. Navigate to **Network > Interfaces**.
2. Click the pencil icon next to `mob1s1a1`.
3. Uncheck **Auto APN** and enter:
   - **APN:** `data00.telnyx`
   - **Username/Password:** leave blank unless instructed.
4. Click **Save & Apply**.

### Verifying Connectivity

Go to **Status > Network Information** and confirm a connected status, an assigned IP address, and usable signal strength.

### Auto-Reboot Watchdog

To recover from service interruptions, configure the auto-reboot watchdog under **System > Auto Reboot**:

1. Enable **Auto Reboot**.
2. Set **Reboot Conditions** to **Ping Reboot** with targets such as `8.8.8.8` and `1.1.1.1`.
3. Set the ping interval (e.g., 60 seconds) and retry count (e.g., 3 failures).
4. Optionally enable a **Scheduled Reboot** (e.g., daily at 3 AM).
5. Click **Save & Apply**.

### Teltonika RMS for Fleet Management

Teltonika RMS is a cloud-based management platform that provides real-time monitoring, remote firmware and configuration updates, command-line access, batch operations, VPN setup, firewall configuration, and alerting. For Telnyx SIM users, RMS enables centralized tracking of usage, signal, and uptime, remote troubleshooting, bulk APN and auto-reboot configuration, and automated health alerts. Sign up at [rms.teltonika-networks.com](https://rms.teltonika-networks.com) and register each device using its unique RMS code found under **System > RMS** in the web UI.

### Firmware and Security

- **Firmware updates:** **System > Firmware**
- **Firewall:** **Network > Firewall**
- **VPN:** **VPN** (OpenVPN, WireGuard, IPsec)

### Configuration Backup

Under **System > Backup**, click **Generate** and download the backup file for disaster recovery.

### Troubleshooting

- **No internet:** Confirm the SIM is active, the APN is correct, signal is sufficient, and auto-reboot is configured.
- **Weak signal:** Move the router or attach external antennas.

## Wireless Connectivity States (API)

The [SIM Connectivity Logs](sim-connectivity-logs.md) API exposes the following `state` values for wireless SIM sessions:

- **Opened:** A SIM initiates a new session to connect to a wireless network. Triggered immediately after an attached event when a device starts transmitting or receiving data.
- **Attached:** The SIM successfully connects to the local carrier network, receives an IP address, and can exchange data.
- **Closed:** The data session has ended. Triggered by loss of coverage, intentional session termination (e.g., scheduled IoT sessions), device power-off or airplane mode, or a switch to Wi-Fi.
- **Provisioned:** A newly provisioned SIM remains in this state until it first attaches to a cellular network. It may also appear after a SIM is transferred from a regular SIM group to a private wireless gateway SIM group.

A standard successful connection cycle is **Attached → Opened → Closed**. The API does not explicitly identify devices that have lost coverage; a lack of "Attached" events indicates the device has not connected.

## SIM Connectivity Logs

Connectivity logs are available in both the Mission Control Portal and the API. They are accessed by drilling into a SIM card in the [SIM cards view](https://portal.telnyx.com/#/wireless/sim-cards).

There are two log types:

- **Registration logs:** Generated when a SIM attaches to a network and authenticates with the Telnyx mobile core.
- **Data logs:** Generated once a SIM has authenticated and created a data session to run traffic.

Each log includes the country code (MCC) and provider code (MNC). The mapping of these codes to operators is available on the [Mobile country code](https://en.wikipedia.org/wiki/Mobile_country_code) Wikipedia page.

### Troubleshooting Patterns

1. **No logs at all:** Signaling from the attach attempt has not reached the Telnyx core, indicating a likely downstream issue. Contact Telnyx support.
2. **Many registration attempts without a data log:** The SIM is not authenticating with the Telnyx mobile core. The most common causes are data roaming not being enabled or the APN not set to `data00.telnyx`.
3. **No data logs:** The data session is not being created, typically due to roaming or APN configuration. Contact Telnyx support if the issue persists.
4. **Error logs / no logs at all:** Signaling is not reaching the mobile core. Possible causes include the SIM attempting to connect to an unsupported operator, roaming not being enabled, or the SIM being in a disabled state. Use a network scan to manually select a supported network, enable roaming and reboot, or check the SIM in the Mission Control Portal — it may have been disabled due to a data limit or balance issue.

## SIM Card Location and Device Details

An estimated SIM location is available in the Mission Control Portal and via the API. The location is derived from the cell tower to which the SIM is connected and is shown as a circle on a map; higher-power towers produce a larger error radius.

The `/sim_cards` API endpoint returns a nested `current_device_location` object:

```
"current_device_location": {
      "accuracy": 1250,
      "accuracy_unit": "m",
      "latitude": "41.143",
      "longitude": "-8.605"
    },
```

Device details exposed in the portal include device type, model name, and IMEI. The API additionally exposes brand name and operating system. The IMEI can be added to the authorized IMEIs field to lock the SIM to a specific device.

## SIM Card Actions

Every update to a SIM card is tracked as an action in the Mission Control Portal and the API. The actions section is found by drilling into a SIM card in the [SIM cards view](https://portal.telnyx.com/#/app/wireless/sim-cards) and scrolling to the bottom.

Each action is logged in chronological order with an associated status. As the status changes, the SIM card action resource is updated. Tracked operations include:

- Enable SIM card
- Disable SIM card
- Standby SIM card
- Data Limit exceeded
- Enable Standby SIM card

## International Coverage and Roaming

The Telnyx IoT SIM card has access to hundreds of networks in over 180 countries. Partner networks are listed on the [Telnyx Global Coverage](https://telnyx.com/iot-global-coverage) page.

Each country is mapped to a pricing zone, and each zone has a discrete per-MB data rate. There are 9 pricing zones in total. The [IoT data plans pricing page](https://telnyx.com/pricing/iot-data-plans) lists the zone per country and the available networks.
