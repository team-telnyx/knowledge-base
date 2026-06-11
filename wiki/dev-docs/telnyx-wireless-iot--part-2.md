---
title: Telnyx Wireless IoT
summary: Telnyx Wireless provides API-controlled cellular connectivity for IoT devices
  — provisioning SIMs, routing data through private or public networks, filtering
  traffic, blocking networks, enabling VoLTE, sending SMS, and generating granular
  usage reports, all programmable from one platform.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/sim-lifecycle
- url: https://developers.telnyx.com/docs/iot-sim/sim7600-a-rasp-pui-hat/index
- url: https://developers.telnyx.com/docs/iot-sim/sixfab-cellular-iot-hat
- url: https://developers.telnyx.com/docs/iot-sim/sixfab-rasp-pi-hat
- url: https://developers.telnyx.com/docs/iot-sim/traffic-policy-profiles
- url: https://developers.telnyx.com/docs/iot-sim/voice-enabled-iot/index
- url: https://developers.telnyx.com/docs/iot-sim/wireless-blocklists
- url: https://developers.telnyx.com/docs/iot-sim/wireless-detail-records
- url: https://developers.telnyx.com/docs/iot-sim/wireless-overview/index
updated_at: 2026-06-11T10:34:44Z
---

# Telnyx Wireless IoT

*Part 2 of 2 — see also: [Part 1](telnyx-wireless-iot--part-1.md)*

Telnyx Wireless provides API-controlled cellular connectivity for IoT devices — provisioning SIMs, routing data through private or public networks, filtering traffic, blocking networks, enabling VoLTE, sending SMS, and generating granular usage reports, all programmable from one platform.

## Wireless Detail Records

Wireless Detail Records (WDRs) provide granular, per-session usage data for your SIM fleet. Each record captures a single data session — when it started, how long it lasted, bytes transferred, and which network was used.

### Generating Reports

WDR reports are asynchronous. Request one, poll for completion, and download when ready.

1. **Create** — `POST /wireless/detail/records/reports` with a time range.
2. **Poll** — `GET /wireless/detail/records/reports/{id}` until `status` is `complete`.
3. **Download** — The `report_url` field contains a pre-signed URL to the report file.

### Report Fields

Each record includes:

| Field | Description |
|---|---|
| `sim_card_id` | Which SIM |
| `start_time` / `stop_time` | Session duration |
| `radio_access_technology` | LTE, 3G, etc. |
| `mobile_country_code` + `mobile_network_code` | Which carrier |
| `apn` | Access Point Name used |
| `ipv4` / `ipv6` | IP assigned during session |
| `cell_id` | Cell tower |

### Connectivity Logs

For real-time session visibility (not batch reports), use connectivity logs: `GET /sim_cards/{id}/wireless_connectivity_logs`. Returns recent sessions for a specific SIM, including IMSI, IMEI, radio technology, and connection state. Useful for debugging why a device cannot connect or which network it attached to.

### WDR Use Cases

- **Billing reconciliation** — match data usage against your invoices
- **Anomaly detection** — spot SIMs consuming unexpected data volumes
- **Coverage analysis** — see which carriers your devices attach to by region
- **Troubleshooting** — correlate connectivity issues with specific cells or networks

## Voice-Enabled IoT (VoLTE)

VoLTE is currently in beta. It allows you to add a real phone number to any eSIM-capable device — no second phone, no SIP client, no app required — just a native cellular line with full API control. API reference and detailed configuration docs are coming soon.

## Hardware Setup Guides

The following guides cover connecting Telnyx SIMs to common IoT hardware platforms. For all setups, you need a Telnyx Portal account and an active Telnyx SIM card with a data plan.

### SIM7600-A Raspberry Pi 4G HAT

The SIM7600A 4G HAT is a 4G communication and GNSS positioning module supporting LTE CAT4 up to 150 Mbps downlink. It uses a Qualcomm MDM9607 chipset and can be attached to a Raspberry Pi for IoT connectivity.

**Prerequisites:** Raspberry Pi 3 Model B or Raspberry Pi 4, and an internet connection for initial setup.

**Setup steps:**

1. Update the Pi: `sudo apt update -y`, `sudo apt dist-upgrade -y`, `sudo rpi-update`, then reboot.
2. Install prerequisites: `sudo apt install libqmi-utils && udhcpc` (`libqmi-utils` for Qualcomm modem interaction, `udhcpc` for DHCP leasing).
3. Enable UART via `sudo raspi-config` → Interfacing Options (5) → P6 Serial → No to login shell → Reboot.
4. Activate the module: `sudo qmicli -d /dev/cdc-wdm0 --dms-set-operating-mode='online'`
5. Verify with `qmicli` commands (`--dms-get-operating-mode`, `--nas-get-signal-strength`, `--nas-get-home-network`).
6. Configure raw-ip protocol: set `wwan0` down, write `Y` to `/sys/class/net/wwan0/qmi/raw_ip`, set `wwan0` up.
7. Connect to mobile network: `sudo qmicli --device=/dev/cdc-wdm0 --device-open-proxy --wds-start-network="ip-type=4,apn=data00.telnyx" --client-no-release-cid`
8. Set default route and IP: `sudo udhcpc -i wwan0`, then verify with `ip a s wwan0`.

The first network attach can take up to 30 minutes as the SIM explores available operators.

### Sixfab Raspberry Pi 3G/4G & LTE Base HAT

The Sixfab 3G/4G & LTE Base HAT provides an interface bridge between mini PCIe cellular modems and a Raspberry Pi. It supports low-power LTE-M through ultra-high-speed LTE-Advanced cards, with both UART and USB communication.

**Setup steps:**

1. Update the Pi: `sudo apt update && sudo apt upgrade`, `sudo apt dist-upgrade`, `sudo apt install raspberrypi-kernel-headers`, then reboot.
2. Download the QMI install script: `wget https://raw.githubusercontent.com/sixfab/Sixfab_RPi_3G-4G-LTE_Base_Shield/master/tutorials/QMI_tutorial/qmi_install.sh`
3. Make executable and run: `chmod +x qmi_install.sh && sudo ./qmi_install.sh` — enter `data00.telnyx` as the APN when prompted.
4. Reboot, then navigate to `/files/quectel-CM` and run `sudo ./quectel-CM -s internet` to connect.

**Troubleshooting:** If the device does not connect, set up auto-connect by downloading `install_auto_connect.sh` from the same Sixfab repository, running it, and verifying the service with `sudo systemctl status qmi_reconnect.service`.

### Sixfab Raspberry Pi Cellular IoT HAT

The Sixfab Cellular IoT HAT uses the Quectel BG96 module (LTE Cat M1 / Cat NB1 / EGPRS) with up to 375 Kbps data rate and worldwide coverage. It also supports GNSS/GPS for location, navigation, and tracking applications.

**Prerequisites:** Raspberry Pi 3 Model B or 4 with up-to-date firmware/software, and the HAT installed on the Pi's 40-pin connector and connected via USB.

**Setup steps:**

1. Enable UART via `sudo raspi-config` → Interfacing Options (5) → P6 Serial → No to login shell → Reboot.
2. Clone the Sixfab library: `git clone https://github.com/sixfab/Sixfab_RPi_CellularIoT_Library.git`
3. Install: `cd Sixfab_RPi_CellularIoT_Library && sudo python3 setup.py install`
4. Download and run the PPP installer: `wget https://raw.githubusercontent.com/sixfab/Sixfab_PPP_Installer/master/ppp_install_standalone.sh`, then `sudo chmod +x ppp_install_standalone.sh && sudo ./ppp_install_standalone.sh`
5. During installation, select: Cellular IoT HAT, APN `data00.telnyx`, no username/password, port `ttyUSB3`, and optionally auto-reconnect on boot.
6. After reboot, use `sudo pon` to connect and `sudo poff` to disconnect.

**Troubleshooting:**

- Check `ifconfig` for the PPP0 interface. If missing, repeat the installation.
- If PPP0 exists but there is no data, try pinging `8.8.8.8`, or reboot and reset the interface (`sudo ifconfig ppp0 down` then `up`).
- If that fails, re-run setup with a blank APN first, then again with `data00.telnyx`.
- Check antenna connections (main and GPS) — an improperly seated antenna causes reboots.
- Verify the antenna matches the HAT model and that the power supply is sufficient (12W for Pi 3, 15W for Pi 4; the HAT uses 2–6 W).
- CAT-M1 speeds max out around 350 Kbps — slow speeds on this HAT are normal.

All three hardware setups use the APN `data00.telnyx`. The first network attach can take up to 30 minutes as the SIM discovers and prioritizes available operators.
