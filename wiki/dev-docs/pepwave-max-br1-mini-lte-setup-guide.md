---
title: Pepwave MAX BR1 Mini LTE Setup Guide
summary: A standalone setup guide for configuring the Pepwave MAX BR1 Mini industrial-grade
  4G LTE router with a Telnyx Wireless SIM card, without using the InControl Cloud
  Controller.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/pepwave-max-br1-mini-lte
updated_at: 2026-08-05T13:47:08Z
---

# Pepwave MAX BR1 Mini LTE Setup Guide

A standalone setup guide for configuring the Pepwave MAX BR1 Mini industrial-grade 4G LTE router with a Telnyx Wireless SIM card, without using the InControl Cloud Controller.

## Overview

The Pepwave MAX BR1 Mini is the latest industrial-grade, 4G LTE router from Peplink. This capable router is heavy on features while keeping a lightweight, small footprint, suitable for installation just about anywhere. Whether the BR1 Mini is installed in a vehicle, used in M2M deployments, or provides cellular backup or Out of Band Management to a home or office, it has great performance and works seamlessly with Telnyx Wireless SIMs.

This guide walks you through how to set up the Pepwave MAX BR1 Mini LTE cellular router with a Telnyx SIM card. It is a standalone setup guide and does not utilize the InControl Cloud Controller.

## Prerequisites

1. A Telnyx Portal account and active Telnyx SIM card with data plan. See the [Get Started with IoT SIM](get-started-with-iot-sim.md) quickstart guide to get set up.
2. The Pepwave MAX BR1 Mini LTE device.
3. A computer.
4. The latest firmware, which can be obtained from the [Peplink downloads page](https://www.peplink.com/support/downloads).

![Pepwave Max BR1 Mini](https://mintcdn.com/telnyx/qRGzozfyAtvPtPCw/img/31jymm9lhnl._ac_.jpg?fit=max&auto=format&n=qRGzozfyAtvPtPCw&q=85&s=7131b74b51aa78ec8ff2fb6e0ce5ad3e)

## Setup Instructions

1. Insert the Telnyx SIM card into either SIM A or SIM B slot on the device and power on the device. The device only accepts the standard size SIM card (the largest SIM card included in the kit).
2. Connect to the device either via the WiFi credentials listed on the unit below the device or via the WAN/LAN Ethernet port located on the back of the device.
3. Navigate to `192.168.50.1`, which is the default gateway of the device. Log in using the default username and password, both of which are `admin`.

   ![Pepwave MAX BR1 Mini LTE login screen](https://mintcdn.com/telnyx/33ANQJ-HKUTIlR5u/img/capture.jpeg?fit=max&auto=format&n=33ANQJ-HKUTIlR5u&q=85&s=b96b69bb05b2f9868bf1f7cdac90452b)

4. Update the device firmware by navigating to `System`, then `Firmware`, and uploading the firmware file. This may take up to 8 minutes.

   ![Updating the Pepwave Max BR1 Mini LTE Device firmware](https://mintcdn.com/telnyx/VYiRDGy8TCRNJLEC/img/pepwave2.png?fit=max&auto=format&n=VYiRDGy8TCRNJLEC&q=85&s=41c3a1db4dff63429f45efc972ca6f96)

5. Once the update process is complete, you'll be directed to the `Dashboards` tab. Click on `Details` under WAN Connection Status. Then, scroll down to `Cellular Settings` and make the following modifications:
   - **SIM Card:** Specified in Step 1 of this guide
   - **LTE/3G:** Auto
   - **Band Selection:** Auto
   - **Data Roaming:** Checked, Any Countries
   - **APN:** Custom, `data00.telnyx`
   - **Username:** Leave blank
   - **Password:** Leave blank

   ![Update the cellular settings of your Pepwave Max BR1 Mini LTE device.](https://mintcdn.com/telnyx/VYiRDGy8TCRNJLEC/img/pepwave5.png?fit=max&auto=format&n=VYiRDGy8TCRNJLEC&q=85&s=81bf82848405f18c68c61c9371f27bc2)

6. Scroll down to the end of the page and press `Save and Apply`.
7. It will take about 2 minutes to connect. Verify connectivity by checking the `WAN Connection Status` under the `Dashboards` tab. This will show that you are connected to Telecom Italia Mobile.

   ![Verify the connectivity of your Pepwave MAX BR1 Mini](https://mintcdn.com/telnyx/33ANQJ-HKUTIlR5u/img/capture-1-.jpeg?fit=max&auto=format&n=33ANQJ-HKUTIlR5u&q=85&s=e547ae477a482a4e161a1559d7b37a38)

That's it! You have just set up your Pepwave MAX BR1 Mini LTE cellular router with a Telnyx SIM card.
