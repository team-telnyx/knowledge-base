---
title: Sixfab Raspberry Pi 3G/4G Hat
summary: Telnyx's SixFax Raspberry Pi Hat is the perfect way to send and receive faxes on your Raspberry Pi.
sources:
  - url: https://developers.telnyx.com/docs/iot-sim/sixfab-rasp-pi-hat/index
    content_hash: d5cbde3666b97d8595ee02b1993a3663fb7f93c5ac28b087804a9c2854dff419
updated_at: 2026-04-10T00:00:00Z
---

# Sixfab Raspberry Pi 3G/4G Hat

Telnyx's SixFax Raspberry Pi Hat is the perfect way to send and receive faxes on your Raspberry Pi. This hat allows you to hook up a standard fax machine to your Raspberry Pi, and send and receive faxes using your Pi's internet connection.

> **Note:** **Original location:** Wireless > IoT > sixfab-rasp-pi-hat

The Sixfab 3G/4G & LTE Base HAT grants your Raspberry Pi or 40-pin Pi compatible single-board-computer a super-simple interface bridge between mini PCIe cellular modems. If you’re looking for a Raspberry Pi LTE HAT for IoT applications like location tracking or global device deployments this is a great device. This add-on also board allows you to create a remote controllable LTE Wi-Fi Hotspot, high-speed GPS tracking and more.

From low-power consumption LTE-M to ultra-high-speed LTE-Advanced mini PCIe cards supported by this HAT. Both UART and USB communication with modules are available on the shield.

This guide assumes that you have a fresh installation of Raspbian OS. Some parts of this guide were obtained from [Sixfab's official tutorial website](https://sixfab.com/shop/).

## Instructions for setting up your Sixfab Raspberry Pi 3G/4G HAT

1. First, let's make sure that the Raspberry Pi is up to date. You can do that by running the below commands:

<Callout type="info">
  After pasting the below content, Kindly check and remove any new line added

```bash theme={null}
sudo apt update && sudo apt upgrade
sudo apt dist-upgrade
sudo apt install raspberrypi-kernel-headers
reboot
```

2. Next, we're going to obtain the required repository from the Sixfab quickstart script: `wget https://raw.githubusercontent.com/sixfab/Sixfab_RPi_3G-4G-LTE_Base_Shield/master/tutorials/QMI_tutorial/qmi_install.sh`

3. Now let's take ownership of the script and install it. In this step, you may be prompted to enter an APN. Enter `data00.telnyx` as the APN and you are good to go!

```bash theme={null}
chmod +x qmi_install.sh
sudo ./qmi_install.sh
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

4. Reboot your device and then let's get connected.

5. To get connected to the internet, navigate to the following directory: `cd /files/quectel-CM`

6. Then mark the device as "online" with the below command. This tells the device to relay its initial "online" status message to the network. Once the network acknowledges the message, your device should obtain a valid IP address from the network; thus, have an internet connection.

```bash theme={null}
sudo ./quectel-CM -s internet
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

> The Telnyx SIM has access to all network types and many different operators. As a result, it can take them a while to attach to a network for the first time. Once it connects to a network, that network will be added to the list of priority operators so as to ensure a fast connection going forward. Please note that the first attach can take up to 30 minutes.

***

## Troubleshooting your Sixfab Raspberry Pi 3G/4G HAT

If the device doesn't connect to the internet, this means that the device either doesn't know which APN to use or the Raspberry Pi has trouble communicating with the device. In this case, we are going to let the device handle the disconnect/reconnect process automatically.

To set up this auto-connect process follow this steps:

1. Make sure the sixfab hat is connected.
2. Obtain required repository: `wget https://raw.githubusercontent.com/sixfab/Sixfab_RPi_3G-4G-LTE_Base_Shield/master/tutorials/QMI_tutorial/install_auto_connect.sh`
3. Take ownership of the script and install.

```bash theme={null}
chmod +x install_auto_connect.sh
sudo ./install_auto_connect.sh
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

4. Now, it will ask for an APN. Please make sure to double check the APN as a misspelling in this step may cause connectivity issues.
5. Verify that the module is active and online: `sudo systemctl status qmi_reconnect.service`


## Related Pages

- [SIM7600-A Raspberry Pi 4G Hat Setup](../runbooks/sim7600-a-raspberry-pi-4g-hat-setup.md)
