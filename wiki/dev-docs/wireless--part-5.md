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

*Part 5 of 6 — see also: [Part 1](wireless--part-1.md), [Part 2](wireless--part-2.md), [Part 3](wireless--part-3.md), [Part 4](wireless--part-4.md), [Part 6](wireless--part-6.md)*

Telnyx Wireless provides API-driven cellular connectivity for IoT and mobile devices. This page covers SIM and eSIM provisioning, lifecycle management, SIM Card Groups, bulk operations, data routing (public IPs, Private Wireless Gateways, Traffic Policy Profiles, Wireless Blocklists), data usage monitoring and notifications, Wireless Detail Records, OTA updates, VoLTE with mobile phone numbers and call features, IoT pricing, connectivity troubleshooting, AT commands, and step-by-step setup guides for a range of supported devices including Raspberry Pi HATs, Particle Boron, Nordic nRF9160, Cradlepoint IBR200, Pepwave Max BR1 Mini, GL-MiFi, and Mikrotik wAP LTE.

## SIM Connectivity Troubleshooting

### Step 1: Check device configuration

1. Enable cellular data
2. Set network to 3G/LTE or 4G/LTE only (first registration requires at least 3G)
3. Enable roaming
4. Set APN: **Name:** `Telnyx` **APN:** `data00.telnyx` (leave all other fields blank)
5. Update firmware, then reboot

**Android:** Settings → Mobile Networks → Access Point Names → Add
**iOS:** Settings → Cellular → Mobile Data → APN

### Step 2: Check connectivity logs

View logs via [portal](https://portal.telnyx.com/#/app/wireless/sim-cards) (click SIM ICCID → Connectivity Logs) or API:

```
GET /sim_cards/{id}/wireless_connectivity_logs
```

The `type` column shows `Registration` or `Data`. MCC identifies the country, MNC identifies the carrier.

### Step 3: Diagnose patterns

**No connectivity logs at all**

- Connection isn't reaching Telnyx. Device may be on a network Telnyx can't access, misconfigured, or SIM is deactivated.
- **Fix:** Scan networks and manually select one. Verify device config (Step 1). Check SIM status in portal — may be disabled due to data limit or billing.

**Multiple registration attempts, no data**

- SIM isn't authenticating.
- **Fix:** Enable data roaming. Verify APN is `data00.telnyx`.

**Registration succeeds but no data sessions**

- Data sessions not being created.
- **Fix:** Enable data roaming. Verify APN is `data00.telnyx`.

If issues persist, contact support via the Mission Control Portal.

## AT Commands

This document contains some useful AT commands to interact with Raspberry Pi HAT cellular modules.

### Prerequisites to complete before running AT commands:

1. Make sure the raspberry Pi is up-to-date and the serial port is enabled. To enable the serial port run this command and then follow the prompts as shown:

- `sudo raspi-config`
- Choose Interfacing Options (5):
  ![SIM7600 Raspberry Pi 4G HAT setup - updating your raspberry pi](https://images.ctfassets.net/4b49ta6b3nwj/32lZLsQpn9op9PThdYrl6K/5829e3aee75954bcc6689d88a7c7fd7a/Capture.JPG)
- Choose P6 Serial: ![SIM7600 Raspberry Pi 4G HAT setup](https://images.ctfassets.net/4b49ta6b3nwj/1bBmYlMDoyZHeDHqdLdwBE/11a315fab3af636cbfc55305119dfa58/Capture.JPG)
- Press *No* to the prompt below then *Reboot*. ![wireless_7600_d](https://images.ctfassets.net/4b49ta6b3nwj/3mExSWu0Gr1FoT8BFXDRSl/26f1f110483a0617d6ef1be43d660e5d/Screen_Shot_2020-03-27_at_8.55.05_AM.png)

2. The package, `screen`, should be installed by default on your Linux distro. If not, you can install it via, `sudo apt or sudo yum install screen`. You may also use `minicom` if you want additional customization. `screen` defaults to ttyS0 unless otherwise specified.

- Sample Command: `screen ttyUSB3` or `screen ttyS0`
- To see which port your device is connected to, you can run `ls -l /dev`.
- Debian Repository for accessing specific versions:
  - <https://packages.debian.org/bullseye/screen>
  - <https://launchpad.net/ubuntu/+source/minicom>

Now that you know how to run AT commands on your device, here are some common commands that you can use.

| Commands | What does it do? | Sample Reponses |
| --- | --- | --- |
| AT | Same thing as "Hey!" in real life. This is used to check if you are able to communicate with the device. | OK |
| AT+COPS=? | To see all available carriers. This command will also filter out carriers that are not compatible with the SIM card. | 0, 1, "T-Mobile" or 0, 4, "AT&T" |
| AT+COPS = (#, #) | Check the current network. Obtain two #'s from the above command. For example, if you want to connect to T-Mobile, you would do AT+COPS=(0,1). | "T-Mobile" or "AT&T" |
| AT+CCID | Check the SIM ID IMEI NUMBER | OK |
| AT+CREG? | Network Registration Status. You can run the AT+CREG=? for available flags.(#, "Current Network Name", PLMN #) | OK |
| AT+COPS=? | List of available networks. This response is valuable to switch carriers. | (4, "Network Name", PLMN #), (2, "Network Name 2", PLMN #2) … |
| AT+COPS = 1, 0 "Carrier Name" | Manually connect to a network. This is also known as PLMN selection. | If all went well, you should get an OK response. If there is an error, it will reply back with CME ERROR. The error usually occurs if your provider's SIM does not support the carrier you are connecting to. Please check with your wireless provider on the list of providers that is supported in your area. |
| AT+BANDS | Manually select a cellular band. This shouldn't be used often unless you are having issues with network congestion. The numbers seen in the sample result is different for every device. | OK 0100004000 B12 045000000 B5 |

### Troubleshooting issues with AT commands

Raspberry Pi 4 has intermittent issues recognizing which USB port to use for serial communication. Even if you specify ttyUSB3 or ttyS0, the Pi often thinks that there is a separate serial port located on the device. In order to fix this issue, we recommend using a bluetooth keyboard and mouse - this will mitigate the confusion the Pi goes through.
