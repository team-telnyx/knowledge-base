---
title: Cradlepoint IBR200 Cellular Router Setup Guide
summary: Telnyx's Cradlepoint IBR200 Cellular Tutorial provides all the information you need to get started using cellular with your Cradlepoint router.
sources:
  - url: https://developers.telnyx.com/docs/iot-sim/cradlepoint-ibr200-cellular/index
    content_hash: 78e6b34a74cc6d74a704b0bd174278bc97845394c1bbb57dcc61fc3278b38c03
updated_at: 2026-04-10T00:00:00Z
---

# Cradlepoint IBR200 Cellular Router Setup Guide

Telnyx's Cradlepoint IBR200 Cellular Tutorial provides all the information you need to get started using cellular with your Cradlepoint router. The tutorial includes step-by-step instructions for configuring your device and troubleshooting any issues.

> **Note:** **Original location:** Wireless > IoT > cradlepoint-ibr200-cellular

The compact, semi-ruggedized IBR200 LTE router is designed for secure, cloud-managed IoT networking. The IBR200 enables use of low-cost M2M/IoT data plans via the Telnyx Wireless SIM, and with NetCloud Perimeter, addresses the biggest gap in IoT: security. It comes with NetCloud Perimeter and advanced security for PCI-compliant networking of vulnerable IoT devices.

This guide will walk you through how to set up the CradlePoint IBR200 cellular router with a Telnyx SIM Card.

## Prerequisites to complete the Cradlepoint IBR200 Cellular Router setup

1. A Telnyx Portal account and active Telnyx SIM card with data plan. Check out this [Quickstart Guide](sims-esims.md) to get set up.
2. The Cradlepoint IBR200 device (as shown below).
3. A Netcloud Essentials Cloud subscription is required for full functionality of this Cradlepoint modem. Without this, many of its features will be disabled. This guide, however, will walk you through basic connectivity which does NOT require the subscription.

<img alt="Cradlepoint IBR200" />

Alright, let's get started!

***

## Instructions for setting up your Cradlepoint IBR200 Cellular Router:

1. First, insert the Telnyx SIM card into your Cradlepoint device. The device only accepts the standard SIM card (the largest size from your Telnyx SIM card kit).

2. Power on the device by connecting the device to its charging adapter.

3. Open up your preferred web browser and navigate to 192.168.0.1. This is the router's default gateway. You'll be prompted to log into the device. The default credentials are:

   * Username: admin
   * Password: the serial number located on the label at the bottom of the device.

   <img alt="Cradlepoint1" />

4. Click on "Connection Manager" tab.

   <img alt="Cradlepoint IBR200 Cellular Router" />

5. Click "Add".

<img alt="Configuring your Cradlepoint IBR200 Cellular Router" />

6. In this step you'll specify the WAN Interface Profile. Configure the profile as shown below:

   * Profile name: Telnyx SIM
   * Type: Modem
   * Leave everything else unchecked

   <img alt="Cradlepoint4" />

7. On the next page, click on "SIM/APN/Auth". In this step, you'll specify the APN to use with the Telnyx SIM Card. Configure the items as shown below:

   * SIM Card Lock: No Pin Required
   * Access Point Name (APN): Default Override
   * data00.telnyx

   <img alt="Cradlepoint6" />

8. Once you hit "Save" it'll take a few minutes for your device to receive connection. You can verify connectivity by heading to "Connection Manager" tab.

<img alt="CradlePoint IBR200 cellular router setup" />

> The Telnyx SIM has access to all network types and many different operators. As a result, it can take them a while to attach to a network for the first time. Once it connects to a network, that network will be added to the list of priority operators so as to ensure a fast connection going forward. Please note that the first attach can take up to 30 minutes.

That's it! Your CradlePoint IBR200 cellular router is all set up with a Telnyx SIM card.


## Related Pages

- [GL-MiFi 4G Smart Router Setup Guide](../runbooks/gl-mifi-4g-smart-router-setup-guide.md)
