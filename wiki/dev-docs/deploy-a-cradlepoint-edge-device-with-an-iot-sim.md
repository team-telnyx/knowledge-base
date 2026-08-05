---
title: Deploy a Cradlepoint Edge Device with an IoT SIM
summary: Tutorial for deploying a Cradlepoint IBR200 cellular router at the edge of
  a corporate network in Digital Ocean, exposing it for SSH access over a private
  IP address via a Telnyx IoT SIM, Cloud VPN, and Private Wireless Gateway.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/edge-deployment/index
updated_at: 2026-08-05T13:46:53Z
---

# Deploy a Cradlepoint Edge Device with an IoT SIM

Tutorial for deploying a Cradlepoint IBR200 cellular router at the edge of a corporate network in Digital Ocean, exposing it for SSH access over a private IP address via a Telnyx IoT SIM, Cloud VPN, and Private Wireless Gateway.

## Overview

This tutorial walks through deploying a Cradlepoint IBR200 to the edge of a corporate network hosted in Digital Ocean. The Cradlepoint device is exposed for SSH access via a private IP address from within the corporate network. The SIM card in the Cradlepoint device is restricted to the corporate network in Digital Ocean and does not have direct access to the public internet. A follow-up tutorial covers opening the SIM up to the public internet.

![Edge Device Deployment with Private Wireless Gateways](https://mintcdn.com/telnyx/Iu93-l5Bj6hMoe-q/img/edge_device_deployment__1_.svg?fit=max&auto=format&n=Iu93-l5Bj6hMoe-q&q=85&s=8741828382ea5747a8e6ffc471695d36)

The deployment consists of five main steps:

1. SIM card setup
2. Cloud VPN setup
3. Cradlepoint IBR200 setup
4. Private Wireless Gateway setup
5. Cradlepoint SSH configuration

## Architecture

To provide direct access to the Cradlepoint device via a private IP address inside the corporate network, a Digital Ocean Droplet (Linux server) is connected to a VRF-defined network on the Telnyx MPLS backbone via a Wireguard client. A private packet gateway is then spun up in the Telnyx mobile core for the SIM card and added to the same VRF-defined network as the Wireguard client. Finally, the Cradlepoint device is configured to accept SSH access, allowing direct connection into the Cradlepoint CLI via the private IP address that the packet gateway assigns to the SIM on the VRF-defined network.

## SIM Card Setup

Order and register a Telnyx SIM card through the Mission Control portal using the registration flow in the Wireless section. See the [IoT SIM Quickstart](iot-sim-quickstart.md) guide for details on registering a SIM card.

When the SIM is inserted into the Cradlepoint device, the only custom configuration required to connect the SIM is to set the APN to `data00.telnyx`.

## Cloud VPN Setup

Configure a Wireguard client on a Digital Ocean Droplet to connect into a Cloud VPN on the Telnyx MPLS backbone. Follow the steps in the Digital Ocean Ubuntu Server to Cloud VPN tutorial. Once the server endpoint on the Telnyx network can be successfully pinged, proceed to the next step.

## Cradlepoint IBR200 Setup

Before creating and configuring a Private Wireless Gateway, connect the Telnyx SIM card to the internet through the Cradlepoint device. Follow the steps in the [Cradlepoint IBR200 Cellular Router Setup Guide](cradlepoint-ibr200-cellular-router-setup-guide.md). Once a connected device on the Cradlepoint network can successfully access the public internet, proceed to the next step.

## Private Wireless Gateway Setup

A Private Wireless Gateway (PWG) must be associated with a Network resource in the portal. Create the PWG in the [Private Wireless Gateways subsection](https://portal.telnyx.com/#/app/wireless/private-wireless-gateways) of the Wireless section of the portal.

Click **Create PWG**, enter a name, and select the Network resource used for the Cloud VPN from the Cloud VPN Setup step.

![Create a Private Wireless Gateway using an existing Network](https://mintcdn.com/telnyx/d2AUJO5qdne_WnZI/img/create-pwg-details.png?fit=max&auto=format&n=d2AUJO5qdne_WnZI&q=85&s=229d6e6cd710006da28a29980411402a)

The PWG may take up to 15 minutes to create because of the automated network configurations required to deploy an entirely new Dockerized PGW instance into the wireless mobile core.

When the PWG status changes to **provisioned**, associate the SIM Group by navigating to the relevant SIM Group and setting the PWG to the newly created one. For this tutorial, it is best to associate a SIM group with only the SIM inserted into the Cradlepoint device. By default, the SIMs in this SIM group will lose access to the public internet when added to the new PGW in the wireless mobile core.

With the SIM card now associated with a new packet gateway via the PWG resource on the same network as the Cloud VPN, the SIM card's IP can be pinged from the Digital Ocean Droplet. Log into the Digital Ocean Ubuntu Server and ping the IP that the SIM is showing in the portal. The SIM card IP address is available in the drill-down view for that SIM. Once a successful ping is established between the Digital Ocean server and the SIM card in the Cradlepoint device, proceed to the next step.

## Cradlepoint SSH Configuration

The final step is to enable SSH access on the Cradlepoint device through the Administration page in the Cradlepoint configuration console.

Connect to the Cradlepoint WiFi network and enter the LAN IP address or hostname of the router (assuming connection from the LAN side) into a web browser's location field. By default, the LAN IP address is `192.168.0.1` and the router's hostname is `cp`.

Next, navigate to the **System** section in the left nav menu, then select **Administration**.

Select **Local Management** from the drop-down menu, then check the **Enable SSH Server** entry box.

To access the CLI from the corporate network, select **Remote Admin** from the **Administration** drop-down menu and check **Allow Remote SSH Access**.

Click **Save** (if using Local Management) or **Submit** (if using Remote Admin).

*Allow Weak Cipher Support* is off by default. It may need to be enabled depending on the SSH version and encryption algorithm used on the server. It can be enabled by navigating to **System > Administration > Local Management > Allow Weak Cipher Support**.

With SSH enabled on the Cradlepoint device, the device can be accessed from the Digital Ocean server. From the Linux server, run:

```
ssh admin@[SIM_CARD_IP]
```

Enter the password used to access the Cradlepoint management console. The Cradlepoint CLI is now accessible without any internet access.
