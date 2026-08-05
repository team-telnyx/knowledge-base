---
title: SIM7600-A Raspberry Pi 4G HAT Setup
summary: Step-by-step guide for assembling, configuring, and connecting a SIM7600A
  4G HAT to a Raspberry Pi using a Telnyx IoT SIM card, including prerequisite installation,
  UART configuration, and qmicli-based network setup.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/sim7600-a-rasp-pui-hat/index
updated_at: 2026-08-05T13:47:21Z
---

# SIM7600-A Raspberry Pi 4G HAT Setup

Step-by-step guide for assembling, configuring, and connecting a SIM7600A 4G HAT to a Raspberry Pi using a Telnyx IoT SIM card, including prerequisite installation, UART configuration, and qmicli-based network setup.

## Overview

The SIM7600A 4G HAT is a 4G communication and GNSS positioning module that supports LTE CAT4 up to 150 Mbps for downlink data transfer. It has low power consumption and can be attached to a Raspberry Pi to empower connectivity for IoT applications. The HAT can also be connected to a computer to access the internet, and provides functionality for sending SMS, global positioning, and high-speed internet connections via 4G.

## Prerequisites

1. Sign up for a free Telnyx Portal account and purchase an active Telnyx SIM card with a data plan. See the [Get Started with IoT SIM](get-started-with-iot-sim.md) quickstart guide to get set up.
2. Raspberry Pi 3 Model B or Raspberry Pi 4 (this guide uses the Pi 4, but the steps are the same).
3. Internet connection for initial setup and configuration.

## Preparation

Start by updating the Raspberry Pi with the following commands:

- `sudo apt update -y`
- `sudo apt dist-upgrade -y`
- `sudo rpi-update`

If prompted, press `Y` and then `enter`:

![Preparation steps for the SIM7600 Raspberry Pi 4G HAT setup](https://mintcdn.com/telnyx/33ANQJ-HKUTIlR5u/img/capture.jpeg?fit=max&auto=format&n=33ANQJ-HKUTIlR5u&q=85&s=b96b69bb05b2f9868bf1f7cdac90452b)

Once the updates are complete, reboot the Pi with `sudo reboot`.

With the updates out of the way, install the prerequisite software and libraries `libqmi-utils` and `udhcpc`:

`sudo apt install libqmi-utils && udhcpc`

- `libqmi-utils` installs libraries that allow you to interact with Qualcomm-based modems. The SIM7600 comes with a Qualcomm MDM9607 chipset.
- `udhcpc` is used for modem DHCP leasing. The cellular network gives a unique IP to the HAT and the Pi will have its own IP. This is used to solve IP addressing conflicts between the Pi and the HAT.

Next, enable UART to communicate with the device. Run the following command and follow the prompts:

- `sudo raspi-config`
- Choose **Interfacing Options (5)**:

  ![SIM7600 Raspberry Pi 4G HAT setup - updating your raspberry pi](https://mintcdn.com/telnyx/33ANQJ-HKUTIlR5u/img/capture-1-.jpeg?fit=max&auto=format&n=33ANQJ-HKUTIlR5u&q=85&s=e547ae477a482a4e161a1559d7b37a38)

- Choose **P6 Serial**:

  ![SIM7600 Raspberry Pi 4G HAT setup](https://mintcdn.com/telnyx/33ANQJ-HKUTIlR5u/img/capture-2-.jpeg?fit=max&auto=format&n=33ANQJ-HKUTIlR5u&q=85&s=37f1138d61e31b0630b77fce2ae9057e)

- Press **No** to the login shell prompt, then **Yes** to enable the serial port, and finally **Reboot**:

  ![Enabling the serial port on the Raspberry Pi](https://mintcdn.com/telnyx/piPv--L_2q5NFR4U/img/screen_shot_2020-03-27_at_8.55.05_am.png?fit=max&auto=format&n=piPv--L_2q5NFR4U&q=85&s=b96a7be72382c3078dc837b8d27f7d9b)

## Configuring the SIM7600 Module

Turn on the module using `qmicli`, which is used to control Qualcomm devices. Activate the device with:

`sudo qmicli -d /dev/cdc-wdm0 --dms-set-operating-mode='online'`

Verify that the module is online using these sample commands:

- `qmicli -d /dev/cdc-wdm0 --dms-get-operating-mode`
  - Response: `Online` or `Offline`
- `qmicli -d /dev/cdc-wdm0 --nas-get-signal-strength`
  - Response: Signal strength and signal quality values
- `qmicli -d /dev/cdc-wdm0 --nas-get-home-network`
  - Response: Carrier name or carrier PLMN

A `wwan0` interface should now appear in network statistics (`ifconfig`). Unless specified by the user, `wwan0` is the default interface this device uses.

Configure the module to use the raw-ip protocol:

- `sudo ip link set wwan0 down`
- `echo 'Y' | sudo tee /sys/class/net/wwan0/qmi/raw_ip`
- `sudo ip link set wwan0 up`

Connect to a mobile network:

```
sudo qmicli --device=/dev/cdc-wdm0 --device-open-proxy --wds-start-network="ip-type=4,apn=data00.telnyx" --client-no-release-cid
```

After pasting the command, check and remove any new line that may have been added.

Set the default route and IP using `udhcpc`:

`sudo udhcpc -i wwan0`

Confirm that the `udhcpc` library received a DHCP lease from the network on `wwan0`:

`ip a s wwan0`

> The Telnyx SIM has access to all network types and many different operators. As a result, it can take a while to attach to a network for the first time. Once it connects to a network, that network will be added to the list of priority operators to ensure a fast connection going forward. Please note that the first attach can take up to 30 minutes.

You are now connected to the internet. Open a web browser and browse away.

## Next Steps

Sign up for a free [Telnyx account](https://telnyx.com/sign-up) to get started with the SIM7600-A Raspberry Pi 4G HAT.
