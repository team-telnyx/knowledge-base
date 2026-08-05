---
title: Particle Boron LTE Kit Setup Guide
summary: Step-by-step instructions for pairing a Particle Electron Boron LTE Kit with
  a Telnyx SIM card, including prerequisites, mobile app setup, DFU mode configuration,
  and CLI commands to enable third-party SIM capability.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/particle-boron-lte-kit
updated_at: 2026-08-05T13:47:06Z
---

# Particle Boron LTE Kit Setup Guide

Step-by-step instructions for pairing a Particle Electron Boron LTE Kit with a Telnyx SIM card, including prerequisites, mobile app setup, DFU mode configuration, and CLI commands to enable third-party SIM capability.

## Overview

The Boron is a powerful LTE Cat M1 or 2G/3G enabled development kit that supports cellular networks and Bluetooth LE (BLE). It is based on the Nordic nRF52840 and has built-in battery charging circuitry, making it easy to connect a Li-Po battery and deploy a local network in minutes. This guide walks through pairing a Particle Electron Boron LTE Kit with a Telnyx SIM Card.

![Particle Boron LTE CAT-M1 Starter Kit](https://mintcdn.com/telnyx/33ANQJ-HKUTIlR5u/img/boron-lte-kit-min_600x.jpg?fit=max&auto=format&n=33ANQJ-HKUTIlR5u&q=85&s=053c01d5b5d7efcbd85303779ef061ff)

## Prerequisites

Before starting the setup, ensure you have the following:

1. A Telnyx Portal account and an active Telnyx SIM card with a data plan. See the [IoT SIM Card Quickstart](iot-sim-card-quickstart.md) to get set up.
2. An Android or iOS device with internet access.
3. The Particle Electron Boron device.
4. A computer with a command-line interface (CLI).

## Setup Instructions

1. Connect the LTE antenna to the port on the front of the Particle Electron Boron device, then connect the device to power. The device will automatically enter pairing mode.
2. Download and install the Particle mobile application on your [Android](https://docs.particle.io/quickstart/boron/) or [iOS](https://apps.apple.com/us/app/particle-iot/id991459054) device.
3. Open the Particle Mobile Application and follow the on-screen instructions:
   - Tap **Get Started**.
   - Log into your Particle.io account or create a new account.
   - Press the **+** button at the top right of the page and select the device name (e.g., `boron-ij3`). The device will activate its eSIM and become visible in [console.particle.io](https://console.particle.io). Particle.io offers a 3-month free trial with limited free data.
4. Enable third-party SIM capability on the device by inserting the Telnyx SIM card into the device.
5. Set up the CLI environment on your computer using the [Particle CLI guide](https://docs.particle.io/tutorials/developer-tools/cli).
6. Place the device in DFU (Device Firmware Upgrade) mode. This mode allows the device to be interacted with via a computer.
7. Press and hold the **Mode** button, then press the **Reset** button once. Continue holding the **Mode** button until the device flashes yellow.
8. Connect the device to the computer using the provided micro-USB cable, then run the following commands in the CLI environment:
   - `particle update` — Updates the device's firmware (1.5.2 as of this guide).
   - `particle flash --usb tinker` — By default, the device receives commands from the Particle Cloud via a network connection. This command allows the computer to control the device instead of the cloud.
9. Repeat step 6 to place the device back into DFU mode.
10. Download the [TelnyxSIM.cpp file](https://assets.ctfassets.net/4b49ta6b3nwj/2UDzHa6KD1Uf6OkKidxtxD/a620b9e24f5c0997be7e593ae39180ec/TelnyxSIM.cpp) and navigate to the saved location. Then run the following commands:
    - `particle compile boron` — Compiles the `.cpp` file into a binary file.
    - `particle compile boron TelnyxSIM.cpp --saveTo firmware.bin` — Creates a `firmware.bin` file that instructs the device to use the Telnyx SIM card.
    - `particle flash --usb firmware.bin` — Flashes the `firmware.bin` onto the device. The device will start using the Telnyx SIM card the next time it reboots.
11. Repeat step 6 to place the device into DFU mode again, then run the following command to restore cloud control:
    - `particle flash --usb tinker`
12. Once the device is connected to a power adapter, it will connect to the Telnyx network. It may take up to 2 minutes for network connectivity to be reflected. Connectivity can also be verified by clicking on the device name in [console.particle.io](https://console.particle.io).

The Particle Electron Boron LTE device is now set up with a Telnyx SIM card.
