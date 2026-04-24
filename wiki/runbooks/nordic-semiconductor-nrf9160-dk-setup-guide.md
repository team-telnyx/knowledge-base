---
title: Nordic Semiconductor nRF9160 DK Setup Guide
summary: Nordic Semiconductor’s nRF9160 is a powerful Bluetooth Low Energy (BLE) SoC that enables the development of ultra-low power, connected products.
sources:
  - url: https://developers.telnyx.com/docs/iot-sim/nordic-semiconductor/index
    content_hash: 1cdf8bc7cecab12e4554550e36abf1c9f76656d7a12a435248357c9f47a4b059
updated_at: 2026-04-10T00:00:00Z
---

# Nordic Semiconductor nRF9160 DK Setup Guide

Nordic Semiconductor’s nRF9160 is a powerful Bluetooth Low Energy (BLE) SoC that enables the development of ultra-low power, connected products. This comprehensive tutorial provides everything you need to get started with the nRF9160, including a step-by-step guide to creating your first BLE peripheral or central device.

> **Note:** **Original location:** Wireless > IoT > nordic-semiconductor

The nRF9160 DK is an affordable, pre-certified single-board development kit for evaluation and development on the nRF9160 SiP for LTE-M, NB-IoT and GPS. This guide will walk through the steps to take in order to connect a Telnyx SIM to the nRF9160 development kit.

## Updating the firmware of the nRF9160:

1. Download the latest board and SIP modem firmware for this device [here](https://www.nordicsemi.com/Products/Development-hardware/nrf9160-dk/download).

2. Once both firmwares are downloaded, open up your file manager and extract the board firmware. The zip file has the file name: `nrf9160dk_fw_0000-00-00_xxxxxxx.zip.` Do NOT extract the SIP modem firmware labeled `mfw_nrf9160_x.x.x.zip.`

3. Download and install the latest nRF Connect application for your operating system [here](https://www.nordicsemi.com/Products/Development-tools/nrf-connect-for-desktop/download#infotabs).

4. Once installed, open up the application and install the following modules:

* LTE Link Monitor
* Programmer
* Trace Collector

<img alt="Install the following modules on your nRF9160" />

5. Look at the front of the device and make sure it's in debug mode as shown below.

<img alt="Ensure the nRF9160 device is in debug mode." />

6. Connect the device to the computer via a microUSB cable and turn on the device using the power switch located at the bottom left corner of the device.

7. Open up the `Programmer` application and select the device denoted `PCA10090`.

8. Drag and drop the firmware file into the file memory layout box then select `Erase & write` to update the firmware. The left box will show patterns when the update is in progress. Once the update is complete, the left box will display a `Device is connected` message.

<img alt="The nRF9160 firmware update is complete" />

9. Now, we'll update the modem firmware. Scroll the right toolbar to the bottom of the screen. Select `Update modem` under the Cellular Modem section and click on the SIP modem firmware that was downloaded in step 1. Then click `Write`.

* The zip file has the following filename: `mfw_nrf9160_x.x.x.zip.`

<img alt="Update nRF9160 modem firmware" />

10. Once the modem updates are complete, turn off the device by using the power switch located at the bottom left corner and disconnect the device from the computer.

## Connecting the nRF9160 device to your Telnyx SIM:

1. Insert your Telnyx SIM card into the nRF9160 device (this device uses nano-sim). Make sure to insert in the correct orientation as notated on the development kit.

<img alt="Insert the Telnyx SIM card into the nRF9160 device." />

2. Connect the nRF9160 device to the computer and power on the device.

3. Open up the nRF Connect application and launch `LTE Link Monitor`.

4. In the `Select Device` dropdown menu, select `PCA10090`. The LTE Link Monitor display will update and run preselected AT commands. Allow 10-15 seconds for it to complete and the device will automatically connect to the network.
   Verify connectivity in the information tab located on the right side of your display.

<img alt="Verify connectivity of your nRF9160 device." />

That's it! You've connected the Telnyx SIM to the nRF9160 development kit.
