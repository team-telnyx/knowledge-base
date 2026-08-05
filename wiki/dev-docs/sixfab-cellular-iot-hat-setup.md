---
title: Sixfab Cellular IoT HAT Setup
summary: Step-by-step guide for setting up a Sixfab Raspberry Pi Cellular IoT HAT
  with a Telnyx SIM card to send and receive data over LTE-M cellular networks.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/sixfab-cellular-iot-hat
updated_at: 2026-08-05T13:47:22Z
---

# Sixfab Cellular IoT HAT Setup

Step-by-step guide for setting up a Sixfab Raspberry Pi Cellular IoT HAT with a Telnyx SIM card to send and receive data over LTE-M cellular networks.

## Overview

The Sixfab Raspberry Pi Cellular IoT HAT allows you to send or receive data over LTE-M cellular networks that the Telnyx SIM has access to without needing gateways. LTE-M (Cat M1) is well suited for Low Power Wide Area Network (LPWAN) applications, especially as some countries have begun shutting down 2G networks.

At the heart of the HAT is the Quectel BG96, an LTE Cat M1/Cat NB1/EGPRS module offering a maximum data rate of 375 Kbps downlink and uplink with worldwide coverage. The HAT also supports GNSS and GPS for location, navigation, tracking, mapping, and timing applications.

## Prerequisites

1. A Telnyx Portal account and an active Telnyx SIM card with a data plan. See the [Get Started with IoT SIM](get-started-with-iot-sim.md) quickstart guide to get set up.
2. A Raspberry Pi 3 Model B or Raspberry Pi 4 (this guide uses the Pi 4, but the steps are the same).
3. Make sure both the firmware and software are up to date on your Pi.
4. Install the Sixfab IoT HAT on the Pi using the 40-pin connector and connect the HAT to the Pi's USB port.

![Raspi_Sixfab_IoT_HAT](https://mintcdn.com/telnyx/piPv--L_2q5NFR4U/img/raspberry_pi_iot.png?fit=max&auto=format&n=piPv--L_2q5NFR4U&q=85&s=fdb664e44412bc14ce699fcb86ac0fce)

## Setup Instructions

1. Enable UART so you can communicate directly with the device using AT commands. Run `sudo raspi-config` and follow the prompts:
   - Choose **Interfacing Options (5)**.

   ![Sixfab setup 1](https://mintcdn.com/telnyx/33ANQJ-HKUTIlR5u/img/capture-1-.jpeg?fit=max&auto=format&n=33ANQJ-HKUTIlR5u&q=85&s=e547ae477a482a4e161a1559d7b37a38)

   - Choose **P6 Serial**.

   ![Sixfab setup 2](https://mintcdn.com/telnyx/33ANQJ-HKUTIlR5u/img/capture-2-.jpeg?fit=max&auto=format&n=33ANQJ-HKUTIlR5u&q=85&s=37f1138d61e31b0630b77fce2ae9057e)

   - Press **No** to the login shell prompt, then **Reboot**.

   ![Sixfab setup 3](https://mintcdn.com/telnyx/piPv--L_2q5NFR4U/img/screen_shot_2020-03-27_at_8.55.05_am.png?fit=max&auto=format&n=piPv--L_2q5NFR4U&q=85&s=b96a7be72382c3078dc837b8d27f7d9b)

2. Retrieve the necessary repository from Sixfab to begin the dependency installation:

   ```
   git clone https://github.com/sixfab/Sixfab_RPi_CellularIoT_Library.git
   ```

3. Navigate to the directory, take ownership of the script, and begin the installation:

   ```
   cd Sixfab_RPi_CellularIoT_Library
   sudo python3 setup.py install
   ```

4. Activate the module and specify the APN:

   ```
   wget https://raw.githubusercontent.com/sixfab/Sixfab_PPP_Installer/master/ppp_install_standalone.sh
   sudo chmod +x ppp_install_standalone.sh
   sudo ./ppp_install_standalone.sh
   ```

5. When prompted during installation, select the following options:
   - **Choose your HAT** — Cellular IoT HAT
   - **What is your carrier APN?** — `data00.telnyx`
   - **Does your carrier need a username or password?** — `n`
   - **What is your device communication PORT?** — `ttyUSB3`
   - **Would you like to reconnect automatically on boot?** — Optional. This guide selects `n`.

6. Once the Pi reboots, use the following commands to connect or disconnect from the internet. If you selected `y` for the reconnect prompt during configuration, your HAT will automatically connect to the network.

   - `sudo pon` to connect
   - `sudo poff` to disconnect

> The Telnyx SIM has access to all network types and many different operators. As a result, it can take a while to attach to a network for the first time. Once it connects to a network, that network will be added to the list of priority operators to ensure a fast connection going forward. The first attach can take up to 30 minutes.

## Troubleshooting

If you have issues with network connectivity, run `ifconfig` to see if the `ppp0` interface is visible (it should appear at the very bottom of the output).

- If you do not see this entry, repeat step 3 of the setup. Sixfab's script is designed to skip items when there is an error or a part does not run properly.
- If you see the `ppp0` interface but there is no data connection, try the following steps:

  1. Ping Google DNS at `8.8.8.8`.
  2. If that does not work, reboot the Pi and reset the interface:

     ```
     sudo reboot
     sudo ifconfig ppp0 down
     sudo ifconfig ppp0 up
     ```

  3. If this step fails, run steps 3 and 4 from the original setup again with a blank APN, then run the script again with the correct APN (`data00.telnyx`).
  4. Check the antenna connection — main and GPS. An improperly seated connection will cause the device to reboot.
  5. Check that the antenna supports your HAT model.
  6. Check the Pi's power supply. The HAT itself uses 2–6 watts of power, so make sure you are using a sufficient power supply for your Pi. The Raspberry Pi 3 requires at least 12 W of power, and the Raspberry Pi 4 requires at least 15 W of power.
  7. Slow internet may also cause issues. The theoretical maximum speed for this HAT is around 350 Kbps, which is the limitation of the Cat M1 network. This is normal.
