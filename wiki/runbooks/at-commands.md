---
title: AT Commands
summary: Telnyx provides a comprehensive guide to AT commands for wireless devices.
sources:
  - url: https://developers.telnyx.com/docs/iot-sim/at-commands/index
    content_hash: c862a2bb13f357a70707d9a0d43985a61573c7e81aa29a40f3d39b926fba2047
updated_at: 2026-04-10T00:00:00Z
---

# AT Commands

Telnyx provides a comprehensive guide to AT commands for wireless devices. With this guide, you can quickly and easily configure your device to work with the Telnyx network.

> **Note:** **Original location:** Wireless > IoT > at-commands

This document contains some useful AT commands to interact with Raspberry Pi HAT cellular modules.

## Prerequisites to complete before running AT commands:

1. Make sure the raspberry Pi is up-to-date and the serial port is enabled. To enable the serial port run this command and then follow the prompts as shown:

* `sudo raspi-config`
* Choose Interfacing Options (5):
  ![SIM7600 Raspberry Pi 4G HAT setup - updating your raspberry pi](https://images.ctfassets.net/4b49ta6b3nwj/32lZLsQpn9op9PThdYrl6K/5829e3aee75954bcc6689d88a7c7fd7a/Capture.JPG)
* Choose P6 Serial: ![SIM7600 Raspberry Pi 4G HAT setup](https://images.ctfassets.net/4b49ta6b3nwj/1bBmYlMDoyZHeDHqdLdwBE/11a315fab3af636cbfc55305119dfa58/Capture.JPG)
* Press *No* to the prompt below then *Reboot*. ![wireless\_7600\_d](https://images.ctfassets.net/4b49ta6b3nwj/3mExSWu0Gr1FoT8BFXDRSl/26f1f110483a0617d6ef1be43d660e5d/Screen_Shot_2020-03-27_at_8.55.05_AM.png)

2. The package, `screen`, should be installed by default on your Linux distro. If not, you can install it via, `sudo apt or sudo yum install screen`. You may also use `minicom` if you want additional customization. `screen` defaults to ttyS0 unless otherwise specified.

* Sample Command: `screen ttyUSB3` or `screen ttyS0`
* To see which port your device is connected to, you can run `ls -l /dev`.
* Debian Repository for accessing specific versions:
  * [https://packages.debian.org/bullseye/screen](https://packages.debian.org/bullseye/screen)
  * [https://launchpad.net/ubuntu/+source/minicom](https://launchpad.net/ubuntu/+source/minicom)

Now that you know how to run AT commands on your device, here are some common commands that you can use.

<table>
  <tbody>
    <tr>
      <td>Commands</td>
      <td>What does it do?</td>
      <td>Sample Reponses</td>
    </tr>

    <tr>
      <td>AT</td>
      <td>Same thing as "Hey!" in real life. This is used to check if you are able to communicate with the device.</td>
      <td>OK</td>
    </tr>

    <tr>
      <td>AT+COPS=?</td>
      <td>To see all available carriers. This command will also filter out carriers that are not compatible with the SIM card.</td>
      <td>0, 1, "T-Mobile" or 0, 4, "AT\&T"</td>
    </tr>

    <tr>
      <td>AT+COPS = (#, #)</td>
      <td>Check the current network. Obtain two #'s from the above command. For example, if you want to connect to T-Mobile, you would do AT+COPS=(0,1).</td>
      <td>"T-Mobile" or "AT\&T"</td>
    </tr>

    <tr>
      <td>AT+CCID</td>
      <td>Check the SIM ID IMEI NUMBER</td>
      <td>OK</td>
    </tr>

    <tr>
      <td>AT+CREG?</td>
      <td>Network Registration Status. You can run the AT+CREG=? for available flags.(#, "Current Network Name", PLMN #)</td>
      <td>OK</td>
    </tr>

    <tr>
      <td>AT+COPS=?</td>
      <td>List of available networks. This response is valuable to switch carriers.</td>
      <td>(4, "Network Name", PLMN #), (2, "Network Name 2", PLMN #2) ...</td>
    </tr>

    <tr>
      <td>AT+COPS = 1, 0 "Carrier Name"</td>
      <td>Manually connect to a network. This is also known as PLMN selection.</td>
      <td>If all went well, you should get an OK response. If there is an error, it will reply back with CME ERROR. The error usually occurs if your provider's SIM does not support the carrier you are connecting to. Please check with your wireless provider on the list of providers that is supported in your area.</td>
    </tr>

    <tr>
      <td>AT+BANDS</td>
      <td>Manually select a cellular band. This shouldn't be used often unless you are having issues with network congestion. The numbers seen in the sample result is different for every device.</td>
      <td>OK 0100004000 B12 045000000 B5</td>
    </tr>
  </tbody>
</table>

## Troubleshooting issues with AT commands

Raspberry Pi 4 has intermittent issues recognizing which USB port to use for serial communication. Even if you specify ttyUSB3 or ttyS0, the Pi often thinks that there is a separate serial port located on the device. In order to fix this issue, we recommend using a bluetooth keyboard and mouse - this will mitigate the confusion the Pi goes through.


## Related Pages

- [Sending Commands](../runbooks/sending-commands.md)
