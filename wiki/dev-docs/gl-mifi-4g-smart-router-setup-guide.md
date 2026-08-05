---
title: GL-MiFi 4G Smart Router Setup Guide
summary: Step-by-step instructions for pairing a GL-MiFi 4G Smart Router with a Telnyx
  SIM card, including SIM insertion, device access, and APN configuration.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/glmifi-router
updated_at: 2026-08-05T13:46:50Z
---

# GL-MiFi 4G Smart Router Setup Guide

Step-by-step instructions for pairing a GL-MiFi 4G Smart Router with a Telnyx SIM card, including SIM insertion, device access, and APN configuration.

## Prerequisites

Before you begin, make sure you have:

1. A Telnyx Portal account and an active Telnyx SIM card with a data plan. See the [IoT SIM Get Started](iot-sim-get-started.md) quickstart guide to get set up.
2. A GL-MiFi device.
3. A computer with a browser.

## Setup Instructions

1. Insert the SIM card into the device with the gold chip facing up, as shown below.
   ![Insert the Telnyx SIM into your GL-MiFi device](https://mintcdn.com/telnyx/33ANQJ-HKUTIlR5u/img/capture.jpeg?fit=max&auto=format&n=33ANQJ-HKUTIlR5u&q=85&s=b96b69bb05b2f9868bf1f7cdac90452b)
2. Power on the device and connect to it either via the Ethernet port or over WiFi. The default WiFi credentials are printed on a label on the bottom of the device.
3. Open a browser and navigate to the device's default gateway at `192.168.8.1`, then log in. You will be prompted to set an admin password; if you do not see the prompt, the default password is `admin`.
4. In the Cellular Modem Overview section, click **manual setup** and enter the following values, then click **Apply**:
   - Device: `/dev/cdc-wdm0`
   - APN: `data00.telnyx`
   ![Log into your GL-MiFi device](https://mintcdn.com/telnyx/33ANQJ-HKUTIlR5u/img/capture-1-.jpeg?fit=max&auto=format&n=33ANQJ-HKUTIlR5u&q=85&s=e547ae477a482a4e161a1559d7b37a38)
5. The device will attach to the Telnyx network. You can verify connectivity from the front page of the default gateway — the device will now display a **Disconnect** button along with an IP address and data usage information.
   ![Your GL-MiFi device will now connect to the Telnyx network](https://mintcdn.com/telnyx/qRGzozfyAtvPtPCw/img/aab9a2d6-1f3c-4bd4-9fe9-1ee3fd3ff718.png?fit=max&auto=format&n=qRGzozfyAtvPtPCw&q=85&s=5b7f0b705d35399c75657225870cc8fb)
6. As an additional connectivity check, look at the fourth icon from the left in the overview diagram. It should display `I TIM`.
   ![Check your connectivity to the Telnyx network on your GL-MiFi Router](https://mintcdn.com/telnyx/qRGzozfyAtvPtPCw/img/347d34e3-0ea7-42e0-a711-64427d017658.png?fit=max&auto=format&n=qRGzozfyAtvPtPCw&q=85&s=e6cc7d93f08b65b5878810be308b7ff3)

Once these steps are complete, your GL-MiFi 4G Smart Router is configured and connected to the Telnyx network.
