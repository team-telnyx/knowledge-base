---
title: Telnyx IoT SIM
summary: Telnyx IoT SIMs provide global cellular connectivity for IoT devices with
  support for physical SIMs and eSIMs, fleet management through SIM Card Groups, private
  networking via Private Wireless Gateways, public static IPs, voice capabilities,
  and over-the-air updates. This page covers ordering, configuration, networking options,
  and device-specific setup guides.
sources:
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
updated_at: 2026-06-11T10:33:18Z
---

# Telnyx IoT SIM

*Part 3 of 3 — see also: [Part 1](telnyx-iot-sim--part-1.md), [Part 2](telnyx-iot-sim--part-2.md)*

Telnyx IoT SIMs provide global cellular connectivity for IoT devices with support for physical SIMs and eSIMs, fleet management through SIM Card Groups, private networking via Private Wireless Gateways, public static IPs, voice capabilities, and over-the-air updates. This page covers ordering, configuration, networking options, and device-specific setup guides.

## Device Setup Guides

### Mikrotik wAP LTE Kit

**Prerequisites:** Active Telnyx SIM, Mikrotik LTE kit router, a computer, and the [latest RouterOS firmware](https://mikrotik.com/product/wap_lte_kit_us#fndtn-downloads). Do not insert the SIM card until instructed.

**Part I — Firmware Update:**

1. Remove the SIM card from the device.
2. Connect your computer via WiFi or Ethernet and log into the default gateway at `192.168.88.1` (username: `admin`, password: blank).
3. Click Files → Browse and upload the `.npk` firmware file.
4. Reboot the device by clicking System → Reboot. The firmware applies automatically during boot.

**Part II — Router Configuration:**

1. Navigate to Interface → LTE.
2. Click LTE APNs → Add New and configure:
   - Name: `Telnyx`
   - APN: `data00.telnyx`
   - IP Type: IPv4
   - Use Peer DNS: Checked
   - Add Default Route: Checked
3. Click Apply then OK.
4. Go back to the LTE tab, click the LTE module, apply the APN via the dropdown, and enable roaming by checking Allow Roaming.
5. Click Apply then OK.
6. Insert the Telnyx SIM card. After roughly 45 seconds the device will attach to the network. Verify connectivity under Interfaces → LTE → LTE module → registration status, which should display "roaming".

### Nordic Semiconductor nRF9160 DK

The nRF9160 DK is a pre-certified single-board development kit for LTE-M, NB-IoT, and GPS evaluation.

**Firmware Update:**

1. Download the latest board and SIP modem firmware from [Nordic's site](https://www.nordicsemi.com/Products/Development-hardware/nrf9160-dk/download).
2. Extract the board firmware zip (`nrf9160dk_fw_...zip`). Do NOT extract the SIP modem firmware (`mfw_nrf9160_x.x.x.zip`).
3. Download and install [nRF Connect for Desktop](https://www.nordicsemi.com/Products/Development-tools/nrf-connect-for-desktop/download#infotabs).
4. Install the LTE Link Monitor, Programmer, and Trace Collector modules.
5. Ensure the device is in debug mode (check the front of the device).
6. Connect via microUSB and power on.
7. Open the Programmer app, select the `PCA10090` device, drag and drop the firmware file, and select Erase & Write.
8. Update the modem firmware: scroll to the Cellular Modem section, select Update modem, choose the SIP modem firmware zip, and click Write.
9. Power off and disconnect.

**Connecting the SIM:**

1. Insert the Telnyx nano-SIM card in the correct orientation.
2. Connect to the computer and power on.
3. Open nRF Connect and launch LTE Link Monitor.
4. Select `PCA10090` from the dropdown. The monitor will run AT commands and automatically connect to the network within 10–15 seconds. Verify connectivity in the information tab.

### Particle Boron LTE Kit

The Boron is an LTE Cat M1 or 2G/3G development kit based on the Nordic nRF52840 with built-in battery charging circuitry.

**Prerequisites:** Telnyx Portal account with active SIM and data plan, an Android or iOS device with internet access, the Particle Boron device, and a computer with CLI.

**Setup:**

1. Connect the LTE antenna and power on. The device enters pairing mode automatically.
2. Download the [Particle mobile app](https://docs.particle.io/quickstart/boron/) (Android) or [iOS app](https://apps.apple.com/us/app/particle-iot/id991459054) and follow the on-screen instructions to activate the device's eSIM.
3. Insert the Telnyx SIM card.
4. Set up the [Particle CLI](https://docs.particle.io/tutorials/developer-tools/cli) on your computer.
5. Place the device in DFU mode: hold the Mode button, press Reset once, keep holding Mode until the device flashes yellow.
6. Connect via micro-USB and run:
   - `particle update` — updates device firmware
   - `particle flash --usb tinker` — allows computer control instead of cloud
7. Re-enter DFU mode. Download the [TelnyxSIM.cpp](https://assets.ctfassets.net/4b49ta6b3nwj/2UDzHa6KD1Uf6OkKidxtxD/a620b9e24f5c0997be7e593ae39180ec/TelnyxSIM.cpp) file and run:
   - `particle compile boron TelnyxSIM.cpp --saveTo firmware.bin`
   - `particle flash --usb firmware.bin`
8. Re-enter DFU mode and run `particle flash --usb tinker` to restore normal device control.
9. Power on the device — it will connect to the Telnyx network within approximately 2 minutes. Verify in console.particle.io.

### Pepwave MAX BR1 Mini LTE

The Pepwave MAX BR1 Mini is an industrial-grade 4G LTE router suitable for vehicles, M2M deployments, or cellular backup. This setup is standalone (does not use InControl Cloud Controller).

**Prerequisites:** Telnyx Portal account with active SIM and data plan, the Pepwave device, a computer, and the [latest firmware](https://www.peplink.com/support/downloads).

**Setup:**

1. Insert the Telnyx SIM (standard size) into SIM A or SIM B slot and power on.
2. Connect via WiFi (credentials on the unit) or the WAN/LAN Ethernet port.
3. Navigate to `192.168.50.1` and log in (default username and password are both `admin`).
4. Update firmware via System → Firmware → Upload (may take up to 8 minutes).
5. On the Dashboards tab, click Details under WAN Connection Status, then scroll to Cellular Settings and configure:
   - SIM Card: as inserted in step 1
   - LTE/3G: Auto
   - Band Selection: Auto
   - Data Roaming: Checked, Any Countries
   - APN: Custom, `data00.telnyx`
   - Username: Blank
   - Password: Blank
6. Click Save and Apply. Wait about 2 minutes, then verify connectivity under Dashboards → WAN Connection Status.

## Common APN Reference

Most device setup guides use the `data00.telnyx` APN for dynamic IP assignment. For static IP assignment (e.g., with a Private Wireless Gateway), use the `data.net` APN instead. See [Public IPs](public-ips.md) and [Private Wireless Gateways](private-wireless-gateways.md) for details.
