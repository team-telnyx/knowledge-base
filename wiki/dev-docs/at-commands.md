---
title: AT Commands
summary: A reference guide for using AT commands to interact with Raspberry Pi HAT
  cellular modules, covering prerequisites, common commands for network and SIM management,
  and troubleshooting tips.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/at-commands/index
updated_at: 2026-08-05T13:46:38Z
---

# AT Commands

A reference guide for using AT commands to interact with Raspberry Pi HAT cellular modules, covering prerequisites, common commands for network and SIM management, and troubleshooting tips.

## Prerequisites to complete before running AT commands

Before running AT commands, ensure the Raspberry Pi is up-to-date and the serial port is enabled.

1. Enable the serial port by running `sudo raspi-config` and following the prompts:
   - Choose **Interfacing Options (5)**:
     ![SIM7600 Raspberry Pi 4G HAT setup - updating your raspberry pi](https://images.ctfassets.net/4b49ta6n3nwj/32lZLsQpn9op9PThdYrl6K/5829e3aee75954bcc6689d88a7c7fd7a/Capture.JPG)
   - Choose **P6 Serial**:
     ![SIM7600 Raspberry Pi 4G HAT setup](https://images.ctfassets.net/4b49ta6n3nwj/1bBmYlMDoyZHeDHqdLdwBE/11a315fab3af636cbfc55305119dfa58/Capture.JPG)
   - Press **No** to the login shell prompt, then **Reboot**:
     ![wireless_7600_d](https://images.ctfassets.net/4b49ta6n3nwj/3mExSWu0Gr1FoT8BFXDRSl/26f1f110483a0617d6ef1be43d660e5d/Screen_Shot_2020-03-27_at_8.55.05_AM.png)

2. Install a serial terminal tool. The `screen` package is usually installed by default on most Linux distributions. If not, install it with `sudo apt` or `sudo yum install screen`. You may also use `minicom` if you want additional customization. `screen` defaults to `ttyS0` unless otherwise specified.
   - Sample command: `screen ttyUSB3` or `screen ttyS0`
   - To see which port your device is connected to, run `ls -l /dev`.
   - Debian repository for accessing specific versions:
     - [screen (Debian Bullseye)](https://packages.debian.org/bullseye/screen)
     - [minicom (Launchpad)](https://launchpad.net/ubuntu/+source/minicom)

## Common AT commands

Once the serial connection is established, the following AT commands can be used to interact with the cellular module.

| Command | Description | Sample Response |
| --- | --- | --- |
| `AT` | A basic connectivity check, equivalent to saying "Hey!" to verify communication with the device. | `OK` |
| `AT+COPS=?` | Lists all available carriers. Filters out carriers that are not compatible with the inserted SIM card. | `0, 1, "T-Mobile"` or `0, 4, "AT&T"` |
| `AT+COPS = (#, #)` | Checks the current network. Use the two `#` values returned by `AT+COPS=?`. For example, to connect to T-Mobile use `AT+COPS=(0,1)`. | `"T-Mobile"` or `"AT&T"` |
| `AT+CCID` | Returns the SIM ID / IMEI number. | `OK` |
| `AT+CREG?` | Reports the network registration status. Run `AT+CREG=?` for available flags. | `(#, "Current Network Name", PLMN #)` |
| `AT+COPS=?` | Lists available networks. Useful when switching carriers. | `(4, "Network Name", PLMN #), (2, "Network Name 2", PLMN #2) …` |
| `AT+COPS = 1, 0 "Carrier Name"` | Manually connects to a network (PLMN selection). | `OK` on success, or `CME ERROR` if the SIM does not support the selected carrier. |
| `AT+BANDS` | Manually selects a cellular band. Use only when troubleshooting network congestion. The numeric values vary per device. | `OK 0100004000 B12 045000000 B5` |

## Troubleshooting issues with AT commands

The Raspberry Pi 4 has intermittent issues recognizing which USB port to use for serial communication. Even when `ttyUSB3` or `ttyS0` is specified, the Pi often detects a separate serial port on the device. To mitigate this, use a Bluetooth keyboard and mouse so the Pi does not confuse the serial device with an input device.
