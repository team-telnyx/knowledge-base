---
title: Sixfab Raspberry Pi 3G/4G HAT
summary: Setup guide for the Sixfab 3G/4G & LTE Base HAT on a Raspberry Pi using a
  Telnyx SIM, including initial installation, network connection, and troubleshooting
  steps.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/sixfab-rasp-pi-hat
updated_at: 2026-08-05T13:47:17Z
---

# Sixfab Raspberry Pi 3G/4G HAT

Setup guide for the Sixfab 3G/4G & LTE Base HAT on a Raspberry Pi using a Telnyx SIM, including initial installation, network connection, and troubleshooting steps.

## Overview

The Sixfab 3G/4G & LTE Base HAT provides a simple interface bridge between mini PCIe cellular modems and a Raspberry Pi (or any 40-pin Pi compatible single-board computer). It is well suited for IoT applications such as location tracking, global device deployments, remote-controllable LTE Wi-Fi hotspots, and high-speed GPS tracking. The HAT supports a range of cellular modules, from low-power LTE-M to ultra-high-speed LTE-Advanced mini PCIe cards, and exposes both UART and USB communication with the modem.

This guide assumes a fresh installation of Raspbian OS. Some portions are adapted from [Sixfab's official tutorial website](https://sixfab.com/shop/).

## Initial Setup

1. Update the Raspberry Pi and install the required kernel headers, then reboot:

```
sudo apt update && sudo apt upgrade
sudo apt dist-upgrade
sudo apt install raspberrypi-kernel-headers
reboot
```

2. Download the Sixfab quickstart script:

```
wget https://raw.githubusercontent.com/sixfab/Sixfab_RPi_3G-4G-LTE_Base_Shield/master/tutorials/QMI_tutorial/qmi_install.sh
```

3. Make the script executable and run it. When prompted for an APN, enter `data00.telnyx`:

```
chmod +x qmi_install.sh
sudo ./qmi_install.sh
```

4. Reboot the device.

5. Change into the connection manager directory:

```
cd /files/quectel-CM
```

6. Bring the device online. This sends the initial "online" status message to the network; once acknowledged, the device receives a valid IP address and an internet connection is established:

```
sudo ./quectel-CM -s internet
```

> The Telnyx SIM has access to all network types and many different operators. As a result, the first network attach can take up to 30 minutes. Once connected, the network is added to the priority list so subsequent connections are faster.

## Troubleshooting

If the device fails to connect to the internet, it usually means the APN is incorrect or the Raspberry Pi is having trouble communicating with the modem. In that case, configure the auto-connect/reconnect service:

1. Confirm the Sixfab HAT is connected.
2. Download the auto-connect script:

```
wget https://raw.githubusercontent.com/sixfab/Sixfab_RPi_3G-4G-LTE_Base_Shield/master/tutorials/QMI_tutorial/install_auto_connect.sh
```

3. Make the script executable and run it:

```
chmod +x install_auto_connect.sh
sudo ./install_auto_connect.sh
```

4. When prompted for an APN, double-check the value — a typo here can prevent connectivity.
5. Verify the module is active and online:

```
sudo systemctl status qmi_reconnect.service
```
