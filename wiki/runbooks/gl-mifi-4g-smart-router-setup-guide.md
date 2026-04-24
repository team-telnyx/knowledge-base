---
title: GL-MiFi 4G Smart Router Setup Guide
summary: Telnyx's GLMifi Router provides an easy way to get started with using LTE for your Internet connection.
sources:
  - url: https://developers.telnyx.com/docs/iot-sim/glmifi-router/index
    content_hash: 263fca1f91e3bac429ce24a1c3b26aeb0c423c157ccdfc9c103387469ed5c576
updated_at: 2026-04-10T00:00:00Z
---

# GL-MiFi 4G Smart Router Setup Guide

Telnyx's GLMifi Router provides an easy way to get started with using LTE for your Internet connection. With this router, you can quickly and easily set up a wireless network in your home or office.

> **Note:** **Original location:** Wireless > IoT > glmifi-router

This guide will walk you through how to pair a GL-MiFi 4G Smart Router with a Telnyx SIM Card.

## Prerequisites to complete the GL-MiFi 4G Smart Router setup:

1. A Telnyx Portal account and active Telnyx SIM card with data plan. Check out this [Quickstart Guide](sims-esims.md) to get set up.
2. GL-MiFi device.
3. A computer with a browser.

Alright, let's get started!

***

## Instructions for setting up your GL-MiFi 4G device:

1. First, insert the SIM card into the device. Look at the picture below for the proper placement of the SIM card, the gold chip should be facing up.

   <img alt="Insert the Telnyx SIM into your GL-MiFi device" />

2. Power on the device and connect either via the Ethernet port or WiFi connection.The default WiFi credentials are located on a label at the bottom of the device.

3. Navigate to the device’s default gateway at `192.168.8.1` and log into the device. You'll be prompted to set an admin password but if you don't see the prompt, the default password is `admin`.

4. Once you’ve logged in, click on `manual setup` located in the Cellular Modem Overview section. Enter the following details as shown below and click `Apply`.

   * Device: `/dev/cdc-wdm0`
   * APN: `data00.telnyx`

   <img alt="Log into your GL-MiFi device" />

5. The device will now attach to the Telnyx network. You can verify the connectivity by checking the front page of the default gateway as shown below. You'll notice that the device now shows a `Disconnect` button as well as IP address and data usage.

   <img alt="Your GL-MiFi device will now connect to the Telnyx network" />

6. To check your connectivity, you can also check the fourth icon on the left of the overview diagram. It will indicate `I TIM`.

   <img alt="Check your connectivity to the Telnyx network on your GL-MiFi Router" />

That's it! Your GL-MiFi 4G Smart Router is all set up with a Telnyx SIM card.


## Related Pages

- [Cradlepoint IBR200 Cellular Router Setup Guide](../runbooks/cradlepoint-ibr200-cellular-router-setup-guide.md)
