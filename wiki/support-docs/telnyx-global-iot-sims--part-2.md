---
title: Telnyx Global IoT SIMs
summary: Comprehensive guide to Telnyx IoT SIM and eSIM products covering ordering,
  registration, device configuration, pricing, global coverage, fleet management features,
  troubleshooting, and device-specific router setup instructions.
sources:
- url: https://support.telnyx.com/en/articles/10067533-manual-esim-activation-guide
- url: https://support.telnyx.com/en/articles/10164784-using-telnyx-sim-with-ubiquiti-unifi-lte-pro
- url: https://support.telnyx.com/en/articles/10511105-using-telnyx-sim-with-inrouter300-series-cellular-routers
- url: https://support.telnyx.com/en/articles/10511646-using-telnyx-sim-with-teltonika-4g-lte-routers
- url: https://support.telnyx.com/en/articles/11017501-understanding-wireless-connectivity-states-telnyx-api
- url: https://support.telnyx.com/en/articles/3269973-adding-the-telnyx-sim-apn-to-your-device
- url: https://support.telnyx.com/en/articles/3270106-international-iot-sim-coverage
- url: https://support.telnyx.com/en/articles/3270136-telnyx-global-sims-faqs
- url: https://support.telnyx.com/en/articles/3296669-iot-sim-card-pricing
- url: https://support.telnyx.com/en/articles/3371977-international-roaming-partners
- url: https://support.telnyx.com/en/articles/3403998-sim-data-limits-notifications
- url: https://support.telnyx.com/en/articles/3679913-sim-reporting-analytics
- url: https://support.telnyx.com/en/articles/4298710-sim-setup-and-configuration
- url: https://support.telnyx.com/en/articles/5666594-sim-connectivity-logs
- url: https://support.telnyx.com/en/articles/5761437-sim-card-theft-prevention
- url: https://support.telnyx.com/en/articles/5812302-sim-card-location-and-device-details
- url: https://support.telnyx.com/en/articles/5812328-sim-card-actions
- url: https://support.telnyx.com/en/articles/7966416-telnyx-iot-sim-data-usage-zone-mapping
- url: https://support.telnyx.com/en/articles/7984783-certificate-error-api-telnyx-com
- url: https://support.telnyx.com/en/articles/8117401-how-to-setup-a-telnyx-esim-via-qr-code
- url: https://support.telnyx.com/en/articles/9183726-manual-imsi-selection-on-telnyx-sim
- url: https://support.telnyx.com/en/collections/1895859-telnyx-global-iot-sims
updated_at: 2026-06-11T11:34:01Z
---

# Telnyx Global IoT SIMs

*Part 2 of 3 — see also: [Part 1](telnyx-global-iot-sims--part-1.md), [Part 3](telnyx-global-iot-sims--part-3.md)*

Comprehensive guide to Telnyx IoT SIM and eSIM products covering ordering, registration, device configuration, pricing, global coverage, fleet management features, troubleshooting, and device-specific router setup instructions.

## SIM Card Location and Device Details

An estimated SIM location is available in the portal (drill into a SIM card) and via the API. The location is based on the connected cell tower and displayed as a circle on a map — more powerful towers yield larger error radiuses.

The API returns location data in the `current_device_location` object with `latitude`, `longitude`, `accuracy`, and `accuracy_unit` fields. See the [Get SIM Card API](https://developers.telnyx.com/api-reference/sim-cards/get-sim-card).

Device details exposed in the portal include device type, model name, and IMEI. The API also provides brand name and operating system. The IMEI can be added to authorized IMEIs to lock the SIM to a specific device.

## SIM Card Actions

Every update to a SIM card is tracked as an action, visible at the bottom of the SIM card detail view in the portal and via the API. Actions are logged chronologically with associated statuses that update as the action progresses. Tracked operations include:

- Enable SIM card
- Disable SIM card
- Standby SIM card
- Data Limit exceeded
- Enable Standby SIM card

See the [SIM Lifecycle API documentation](https://developers.telnyx.com/docs/iot-sim/sim-lifecycle) for details.

## SIM Card Theft Prevention

Add up to 5 authorized IMEIs per SIM to restrict usage to your approved devices only. When an unauthorized IMEI is detected, the SIM is auto-disabled (allow up to 5 minutes for this to take effect) and an email alert is dispatched.

If no authorized IMEIs are configured, all devices are considered authorized — this is the default. Configure authorized IMEIs in the SIM card drill-down section of the portal.

## Wireless Connectivity States

The [Wireless Connectivity Logs API](https://developers.telnyx.com/api/wireless/get-wireless-connectivity-logs) returns these `state` values:

| State | Definition | Trigger |
|-------|-----------|---------|
| **Opened** | SIM initiates a new data session | After an Attached event, when data transmission begins |
| **Attached** | SIM successfully connects to the carrier network and receives an IP address | Successful network registration |
| **Closed** | Data session has ended | Loss of coverage, device power-off, airplane mode, Wi-Fi takeover, or intentional termination |
| **Provisioned** | SIM is registered but has not yet attached to a network | Initial provisioning or transfer between SIM groups |

A standard successful connection cycle is: **Attached → Opened → Closed**.

## Troubleshooting Connectivity

### Connectivity Logs

Connectivity logs (viewable per SIM in the portal and via the API) come in two types: `registration` and `data`. SIMs first authenticate with the Telnyx mobile core (registration log), then create a data session (data log). The MCC indicates the country and the MNC identifies the carrier network.

Common troubleshooting patterns:

1. **No logs at all:** Signaling hasn't reached the Telnyx core — likely a downstream issue. Contact support.
2. **Many registration attempts without data logs:** SIM is not authenticating. Most commonly, data roaming is not enabled or the APN is not set to `data00.telnyx`.
3. **No data logs:** Data session isn't being created — typically a roaming or APN issue. If persistent, contact support.
4. **Error logs / no logs:** The SIM may be trying to connect to an operator Telnyx doesn't support, roaming may be disabled, or the SIM may be in a disabled state (due to data limit or balance exhaustion). Try a network scan on the device to manually select a supported network, enable roaming, or check the SIM state in the portal.

### Manual IMSI Selection

⚠️ For engineering use only — perform only when instructed by Telnyx support.

Telnyx SIMs use Multi-IMSI technology to optimize global coverage. By default, the SIM automatically selects the best IMSI. Manual selection is available via the SIM Toolkit (STK) for advanced troubleshooting.

**Android:** Open the **Telnyx UICC** or **SIM Toolkit** app → Roaming Services/Telnyx → IMSI Selection Menu → select desired IMSI → wait a few minutes → return Selection Mode to **Automatic**.

**iOS:** Settings → Mobile Service/Cellular → SIM Applications → IMSI Selection Menu → select desired IMSI → wait a few minutes → return Selection Mode to **Automatic**.

Always switch back to Automatic after testing unless instructed otherwise. Failure to do so may result in loss of connectivity when the device moves geographically.

### First-Time Network Attachment

During the first connection attempt, it may take up to 30 minutes for the device to attach to a network. Once connected, the network is added to the priority operator list for faster future connections.

## Device-Specific Router Configuration

### Ubiquiti UniFi LTE Pro

1. **Insert SIM:** Place the Nano SIM into the card slot.
2. **Power On:** Connect to a PoE (802.3af) enabled Ubiquiti switch.
3. **Access Console:** Navigate to [unifi.ui.com](https://unifi.ui.com) and log in.
4. **Adopt Device:** Find the LTE Pro in your device list and click **Adopt**.
5. **Configure LTE Backup:** Settings → Internet → LTE Backup → Settings.
6. **Enter APN:** Set APN to `data00.telnyx`, Authentication Type to **NONE**, then click **Apply**.
7. **Verify Connection:** Check the Overview tab — Status should be **Ready** and Connected should be **Yes**.

If the device restarts or is re-provisioned and enters SIM-Activation mode, run the following CLI command:

```
qmicli -p -d /dev/cdc-wdm0 --wds-set-autoconnect-settings=enabled
```

### InRouter300 Series (IR300)

1. **Physical Setup:** Insert the Telnyx SIM into the SIM slot. Connect your computer to the LAN port via Ethernet. Power on.
2. **Access Web Interface:** Browse to `http://192.168.2.1`. Default credentials: username `adm`, password `123456`.
3. **Configure APN:** Network → Cellular → SIM Profiles → SIM Slot 1 → set APN to `data00.telnyx`, leave Username and Password blank → Apply.
4. **Optional Dual SIM:** Enable Dual SIM Mode and configure failover if using a secondary SIM.
5. **Verify Connectivity:** Status → Network Connection — check for an assigned IP address and successful signal/network registration.
6. **Optional:** Configure static IP (Network → WAN Settings), VPN (VPN → Settings for IPSec/OpenVPN/PPTP), or Firewall rules (Security → Firewall).
7. **Backup Config:** System → Config Management → Backup to generate a `.dat` file for future restores.

### Teltonika 4G/LTE Routers

1. **Insert SIM:** Power off, insert the Telnyx SIM, power on. Connect via Ethernet to the LAN port.
2. **Access Web Interface:** Browse to `http://192.168.2.1`. Default username: `admin`; default password is on the router label.
3. **Configure APN:** Network → Interfaces → edit `mob1s1a1` → uncheck **Auto APN** → set APN to `data00.telnyx`, leave Username/Password blank → Save & Apply.
4. **Verify Connectivity:** Status → Network Information — confirm Connected status, assigned IP, and usable signal strength.
5. **Configure Auto-Reboot (Recommended):** System → Auto Reboot → enable Auto Reboot → select **Ping Reboot** with targets like `8.8.8.8` and `1.1.1.1` → set ping interval and retry count → Save & Apply. This ensures automatic recovery from network outages.
6. **Optional — Teltonika RMS:** For centralized fleet management, sign up at [rms.teltonika-networks.com](https://rms.teltonika-networks.com). RMS provides real-time monitoring, remote firmware/config updates, CLI access, batch operations, VPN setup, and automated alerts. Register each device using the RMS code found in System → RMS.
7. **Firmware & Security:** Update firmware at System → Firmware. Configure firewall at Network → Firewall. Set up VPN under the VPN section (OpenVPN, WireGuard, IPsec supported).
8. **Backup Config:** System → Backup → Generate and download the backup file.
