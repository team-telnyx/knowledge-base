---
title: Nordic Semiconductor nRF9160 DK Setup Guide
summary: Step-by-step instructions for updating firmware on the Nordic Semiconductor
  nRF9160 DK development kit and connecting it to a Telnyx SIM for LTE-M, NB-IoT,
  and GPS evaluation.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/nordic-semiconductor
updated_at: 2026-08-05T13:47:02Z
---

# Nordic Semiconductor nRF9160 DK Setup Guide

Step-by-step instructions for updating firmware on the Nordic Semiconductor nRF9160 DK development kit and connecting it to a Telnyx SIM for LTE-M, NB-IoT, and GPS evaluation.

The nRF9160 DK is an affordable, pre-certified single-board development kit for evaluation and development on the nRF9160 SiP for LTE-M, NB-IoT, and GPS. This guide walks through the steps required to connect a Telnyx SIM to the nRF9160 development kit.

## Updating the firmware of the nRF9160

1. Download the latest board and SiP modem firmware for this device from the [Nordic Semiconductor nRF9160 DK downloads page](https://www.nordicsemi.com/Products/Development-hardware/nrf9160-dk/download).
2. Once both firmwares are downloaded, open your file manager and extract the board firmware. The zip file has the file name `nrf9160dk_fw_0000-00-00_xxxxxxx.zip`. Do **not** extract the SiP modem firmware labeled `mfw_nrf9160_x.x.x.zip`.
3. Download and install the latest [nRF Connect for Desktop](https://www.nordicsemi.com/Products/Development-tools/nrf-connect-for-desktop/download#infotabs) application for your operating system.
4. Once installed, open the application and install the following modules:
   - LTE Link Monitor
   - Programmer
   - Trace Collector

   ![Install the following modules on your nRF9160](https://mintcdn.com/telnyx/VYiRDGy8TCRNJLEC/img/nordic_image_2.png?fit=max&auto=format&n=VYiRDGy8TCRNJLEC&q=85&s=0eaf1468993d22e71dce1eb090a6c368)

5. Look at the front of the device and make sure it is in debug mode as shown below.

   ![Ensure the nRF9160 device is in debug mode.](https://mintcdn.com/telnyx/M104dP2YWeqFiyN4/img/untitled_design__17_.jpg?fit=max&auto=format&n=M104dP2YWeqFiyN4&q=85&s=9ab43d8608d8e90c8087547989afc04d)

6. Connect the device to the computer via a microUSB cable and turn on the device using the power switch located at the bottom left corner of the device.
7. Open the `Programmer` application and select the device denoted `PCA10090`.
8. Drag and drop the firmware file into the file memory layout box, then select `Erase & write` to update the firmware. The left box will show patterns when the update is in progress. Once the update is complete, the left box will display a `Device is connected` message.

   ![The nRF9160 firmware update is complete](https://mintcdn.com/telnyx/VYiRDGy8TCRNJLEC/img/nordic_image_5.png?fit=max&auto=format&n=VYiRDGy8TCRNJLEC&q=85&s=30e9c14a1a517a8c22f902e4cc3fd221)

9. Next, update the modem firmware. Scroll the right toolbar to the bottom of the screen. Select `Update modem` under the Cellular Modem section and click on the SiP modem firmware that was downloaded in step 1. Then click `Write`.
   - The zip file has the following filename: `mfw_nrf9160_x.x.x.zip`.

   ![Update nRF9160 modem firmware](https://mintcdn.com/telnyx/VYiRDGy8TCRNJLEC/img/nordic_image_7.png?fit=max&auto=format&n=VYiRDGy8TCRNJLEC&q=85&s=c4200f4a5a00d0e0585808f7781f9c1e)

10. Once the modem updates are complete, turn off the device using the power switch located at the bottom left corner and disconnect the device from the computer.

## Connecting the nRF9160 device to your Telnyx SIM

1. Insert your Telnyx SIM card into the nRF9160 device (this device uses nano-SIM). Make sure to insert it in the correct orientation as notated on the development kit.

   ![Insert the Telnyx SIM card into the nRF9160 device.](https://mintcdn.com/telnyx/M104dP2YWeqFiyN4/img/untitled_design__18_.jpg?fit=max&auto=format&n=M104dP2YWeqFiyN4&q=85&s=486d660630ffe3c3472ea8b105abc53b)

2. Connect the nRF9160 device to the computer and power on the device.
3. Open the nRF Connect application and launch `LTE Link Monitor`.
4. In the `Select Device` dropdown menu, select `PCA10090`. The LTE Link Monitor display will update and run preselected AT commands. Allow 10–15 seconds for it to complete, and the device will automatically connect to the network. Verify connectivity in the information tab located on the right side of your display.

   ![Verify connectivity of your nRF9160 device.](https://mintcdn.com/telnyx/VYiRDGy8TCRNJLEC/img/nordic_image_8__1_.png?fit=max&auto=format&n=VYiRDGy8TCRNJLEC&q=85&s=e0ed3d848bc8ceed0769dfa84ef2e5d6)

That's it — you have connected the Telnyx SIM to the nRF9160 development kit.
