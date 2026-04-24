---
title: SIM7600-A Raspberry Pi 4G Hat Setup
summary: This DevDocs page provides a comprehensive tutorial on how to use the Sim7600A Raspberry Pi 4G Hat with Telnyx wireless services.
sources:
  - url: https://developers.telnyx.com/docs/iot-sim/sim7600-a-rasp-pui-hat/index
    content_hash: 788d6fa64fbaeb8222251a85f0d1c79a56f6dd7825151d339ea7afd0a747db7b
updated_at: 2026-04-10T00:00:00Z
---

# SIM7600-A Raspberry Pi 4G Hat Setup

This DevDocs page provides a comprehensive tutorial on how to use the Sim7600A Raspberry Pi 4G Hat with Telnyx wireless services.

> **Note:** **Original location:** Wireless > IoT > sim7600-a-rasp-pui-hat

The SIM7600A 4G HAT is a 4G communication and GNSS positioning module, which supports LTE CAT4 up to 150Mbps for downlink data transfer. It is pretty low power consumption and can be attached to a Raspberry Pi to empower connectivity for IoT applications.

You can also connect this 4G module with a computer to surf the Internet. It has functionality for sending SMS, global positioning, and high speed internet connections via 4G.

## Prerequisites to complete the SIM7600 4G HAT setup

1. Sign up for a [free Telnyx Portal account](https://telnyx.com/sign-up "Sign Up") and purchase an active Telnyx SIM card with data plan. Check out this [Quickstart Guide](sims-esims.md) to get set up.
2. Raspberry Pi 3 Model B or Raspberry Pi 4 (this guide will use 4 but the steps are the same).
3. Internet connection for initial setup and configuration.

Alright, let's get started!

***

## Preparation steps for the SIM7600 Raspberry Pi 4G HAT setup

First, we are going to start by updating the Raspberry Pi so let's run these commands:

* `sudo apt update -y`
* `sudo apt dist-upgrade -y`
* `sudo rpi-update`
* You may see a prompt like this. Press `Y` and press `enter`:
  <img alt="Preparation steps for the SIM7600 Raspberry Pi 4G HAT setup" />

Once all of the steps are complete, reboot your Pi using `sudo reboot` command.

With the updates out of the way, let's start on installing prerequisite software and libraries: *libqmi-utils* and *udhcpc* are first up. Install them by running this command: `sudo apt install libqmi-utils && udhcpc`

*libqmi-utils* installs libraries that allow you to interact with Qualcomm-based modems. SIM7600 comes with a Qualcomm MDM9607 chipset.
*udhcpc* is used for modem DHCP leasing. The cellular network gives a unique IP to the HAT and the Pi will have its own IP. This is used to solve IP addressing conflicts between the Pi and the HAT.

Now we will enable UART to communicate with the device. To do that, run this command and then follow the prompts as shown:

* `sudo raspi-config`
* Choose Interfacing Options (5):
  <img alt="SIM7600 Raspberry Pi 4G HAT setup - updating your raspberry pi" />
* Choose P6 Serial:
  <img alt="SIM7600 Raspberry Pi 4G HAT setup" />
* Press *No* to the prompt below then *Reboot*. <img alt="wireless_7600_d" />

## Configuration of the SIM7600 module

Next, we're going to configure the SIM7600A module. To turn on the module we will be using the qmicli commands which are used to control Qualcomm devices. This command will activate the device: `sudo qmicli -d /dev/cdc-wdm0 --dms-set-operating-mode='online'`

Now let's verify that the module is online. These are sample commands you can send to the device:

* `qmicli -d /dev/cdc-wdm0 --dms-get-operating-mode`
  * Response: Online or Offline
* `qmicli -d /dev/cdc-wdm0 --nas-get-signal-strength`
  * Response: Signal strength and signal quality values
* `qmicli -d /dev/cdc-wdm0 --nas-get-home-network`
  * Response: Carrier name or carrier PLMN

You should now see a WWAN0 interface in net-stats (`ifconfig`). Unless specified by user, WWAN0 is the default interface this device uses.

We're now going to configure the module to use raw-ip protocol with the following commands:

* `sudo ip link set wwan0 down`
* `echo 'Y' | sudo tee /sys/class/net/wwan0/qmi/raw_ip`
* `sudo ip link set wwan0 up`

And connecting to a mobile network:

```bash theme={null}
sudo qmicli --device=/dev/cdc-wdm0 --device-open-proxy --wds-start-network="ip-type=4,apn=data00.telnyx" --client-no-release-cid
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

Finally, let's set the default route and IP using udhcpc: `sudo udhcpc -i wwan0`
And tell the udhcpc library to receive a DHCP lease from the network using WWAN0: `ip a s wwan0`

> The Telnyx SIM has access to all network types and many different operators. As a result, it can take them a while to attach to a network for the first time. Once it connects to a network, that network will be added to the list of priority operators so as to ensure a fast connection going forward. Please note that the first attach can take up to 30 minutes.

You are connected to the Internet! Open up your web browser and browse away!

***

Make sure to [sign up for a free Telnyx account ](https://telnyx.com/sign-up "Sign Up")to get started with SIM7600-A Raspberry Pi 4G!


## Related Pages

- [Sixfab Raspberry Pi 3G/4G Hat](../runbooks/sixfab-raspberry-pi-3g-4g-hat.md)
