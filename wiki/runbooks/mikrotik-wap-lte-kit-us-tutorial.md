---
title: Mikrotik wAP LTE Kit - US Tutorial
summary: Telnyx's Mikrotik WAP LTE tutorial is a great resource for anyone looking to get started with wireless networking using Mikrotik hardware.
sources:
  - url: https://developers.telnyx.com/docs/iot-sim/mikrotik-wap-lte/index
    content_hash: f16e32acb0c33a4e83815cb106f6ce2502637cc264ea3a54501f7e4fb1302fa8
updated_at: 2026-04-10T00:00:00Z
---

# Mikrotik wAP LTE Kit - US Tutorial

Telnyx's Mikrotik WAP LTE tutorial is a great resource for anyone looking to get started with wireless networking using Mikrotik hardware. The tutorial provides configuration examples for both basic and advanced scenarios, making it a valuable resource for any level of user.

> **Note:** **Original location:** Wireless > IoT > mikrotik-wap-lte

This guide will walk you through configuring the Mikrotik LTE Kit US router using a Telnyx SIM.

## Prerequisites to Set Up Mikrotik wAP LTE kit

1. An active Telnyx SIM card
2. Mikrotik LTE kit router
3. A computer
4. Latest routerOS firmware, which you can obtain [here.](https://mikrotik.com/product/wap_lte_kit_us#fndtn-downloads "Mikrotik Downloads")

## Setting Up Mikrotik wAP LTE kit

Note: Please insert the SIM card into router only when instructed to do so.

### Part I: Firmware Update

* We will begin by updating the routerOS firmware to the latest version (6.48 as of 2.4.21).
* Remove the SIM card from the device.
* Connect your computer to the device via either the WiFi or the Ethernet interface and log into the default gateway at 192.168.88.1. The default username and password are shown below.
  * Username: admin
  * Password: (blank)
* Once you log in, you will see the admin console as shown below.

<img alt="Mikrotik RouterOS" />

* Click on Files → Browse and upload the .npk firmware file.

<img alt="Mikrotik Tutorial - Image 2 " />

* Reboot the device by clicking System → Reboot.
  * The device will apply the latest firmware automatically during the booting procedure.

### Part II (Router Configuration)

* Navigate to Interface → LTE.

<img alt="Mikrotik Router Configuration" />

* Click LTE APNs → Add New.
  * Name: Telnyx
  * APN: data00.telnyx
  * IP Type: IPv4
  * Use Peer DNS: Check
  * Add Default Route: Check
  * Leave all other settings as their default values.

<img alt="Mikrotik Router Settings" />

* Click Apply then OK.
* Go back to the LTE tab under Interfaces and click on the LTE module.
  Apply the APN created above using the dropdown menu and enable roaming by checking the Allow Roaming box.

<img alt="Roaming options Mikrotik" />

* Press Apply then OK.
* Insert the Telnyx SIM card. After roughly 45 seconds, the device will attach to the network. You can verify connectivity by going to Interfaces → LTE → Click on the LTE module then scroll down to registration status. It will display “roaming”.

<img alt="Roaming Mikrotik" />
