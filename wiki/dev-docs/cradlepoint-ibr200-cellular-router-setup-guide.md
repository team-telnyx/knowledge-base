---
title: Cradlepoint IBR200 Cellular Router Setup Guide
summary: Step-by-step instructions for configuring a Cradlepoint IBR200 LTE router
  with a Telnyx Wireless SIM card, including prerequisites, default gateway access,
  and APN configuration.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/cradlepoint-ibr200-cellular/index
updated_at: 2026-08-05T13:46:48Z
---

# Cradlepoint IBR200 Cellular Router Setup Guide

Step-by-step instructions for configuring a Cradlepoint IBR200 LTE router with a Telnyx Wireless SIM card, including prerequisites, default gateway access, and APN configuration.

## Overview

The compact, semi-ruggedized IBR200 LTE router is designed for secure, cloud-managed IoT networking. The IBR200 enables use of low-cost M2M/IoT data plans via the Telnyx Wireless SIM, and with NetCloud Perimeter, addresses the biggest gap in IoT: security. It comes with NetCloud Perimeter and advanced security for PCI-compliant networking of vulnerable IoT devices.

This guide walks through how to set up the Cradlepoint IBR200 cellular router with a Telnyx SIM card.

## Prerequisites

1. A Telnyx Portal account and an active Telnyx SIM card with a data plan. See the [Get Started with Telnyx SIM](get-started-with-telnyx-sim.md) quickstart guide to get set up.
2. The Cradlepoint IBR200 device.
3. A NetCloud Essentials Cloud subscription is required for full functionality of this Cradlepoint modem. Without it, many features will be disabled. This guide, however, covers basic connectivity which does **not** require the subscription.

![Cradlepoint IBR200](https://mintcdn.com/telnyx/piPv--L_2q5NFR4U/img/rtaimage.jpg?fit=max&auto=format&n=piPv--L_2q5NFR4U&q=85&s=26b60e7d7ed727a037217f1dc0a13c78)

## Setup Instructions

1. Insert the Telnyx SIM card into the Cradlepoint device. The device only accepts the standard SIM card (the largest size from your Telnyx SIM card kit).
2. Power on the device by connecting it to its charging adapter.
3. Open a web browser and navigate to `192.168.0.1`. This is the router's default gateway. You will be prompted to log in using the default credentials:
   - **Username:** `admin`
   - **Password:** the serial number located on the label at the bottom of the device.

   ![Cradlepoint login screen](https://mintcdn.com/telnyx/d2AUJO5qdne_WnZI/img/cradlepoint1.png?fit=max&auto=format&n=d2AUJO5qdne_WnZI&q=85&s=24d2b45e0c1854334df057b00568ac97)

4. Click the **Connection Manager** tab.

   ![Cradlepoint IBR200 Connection Manager](https://mintcdn.com/telnyx/33ANQJ-HKUTIlR5u/img/capture.jpeg?fit=max&auto=format&n=33ANQJ-HKUTIlR5u&q=85&s=b96b69bb05b2f9868bf1f7cdac90452b)

5. Click **Add**.

   ![Adding a new connection](https://mintcdn.com/telnyx/33ANQJ-HKUTIlR5u/img/capture-1-.jpeg?fit=max&auto=format&n=33ANQJ-HKUTIlR5u&q=85&s=e547ae477a482a4e161a1559d7b37a38)

6. Specify the WAN Interface Profile with the following settings:
   - **Profile name:** Telnyx SIM
   - **Type:** Modem
   - Leave everything else unchecked.

   ![WAN Interface Profile configuration](https://mintcdn.com/telnyx/d2AUJO5qdne_WnZI/img/capture3.png?fit=max&auto=format&n=d2AUJO5qdne_WnZI&q=85&s=45637f7123acc931c9706b7d9cadff59)

7. On the next page, click **SIM/APN/Auth** and configure the APN to use with the Telnyx SIM card:
   - **SIM Card Lock:** No Pin Required
   - **Access Point Name (APN):** Default Override — `data00.telnyx`

   ![SIM/APN/Auth configuration](https://mintcdn.com/telnyx/d2AUJO5qdne_WnZI/img/capture8.png?fit=max&auto=format&n=d2AUJO5qdne_WnZI&q=85&s=c83fb2d7730dd8a9e4d75840ed281b69)

8. Click **Save**. It will take a few minutes for the device to receive a connection. Verify connectivity by returning to the **Connection Manager** tab.

   ![Verifying connectivity in Connection Manager](https://mintcdn.com/telnyx/33ANQJ-HKUTIlR5u/img/capture-2-.jpeg?fit=max&auto=format&n=33ANQJ-HKUTIlR5u&q=85&s=37f1138d61e31b0630b77fce2ae9057e)

> The Telnyx SIM has access to all network types and many different operators. As a result, it can take a while to attach to a network for the first time. Once it connects to a network, that network will be added to the list of priority operators to ensure a fast connection going forward. The first attach can take up to 30 minutes.

Once connected, the Cradlepoint IBR200 cellular router is fully set up with a Telnyx SIM card.
