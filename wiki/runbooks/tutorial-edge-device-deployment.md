---
title: 'Tutorial: Edge Device Deployment'
summary: Telnyx's edge deployment guide is the perfect resource for businesses looking to get the most out of their private wireless gateway.
sources:
  - url: https://developers.telnyx.com/docs/iot-sim/edge-deployment/index
    content_hash: c56eded64510dcf2007350e387942822be5fcb75ae78b1d8b3248160cc48f1db
updated_at: 2026-04-10T00:00:00Z
---

# 'Tutorial: Edge Device Deployment'

Telnyx's edge deployment guide is the perfect resource for businesses looking to get the most out of their private wireless gateway. With this guide, you'll learn how to configure and manage your edge device for optimal performance.

> **Note:** **Original location:** Wireless > IoT > edge-deployment

In this tutorial, we are going to deploy a Cradlepoint IBR200 to the edge of our corporate network in Digital Ocean. We will then open the Cradlepoint device up for SSH access via a private IP address from within our network.

For this tutorial, the SIM card in the Cradlepoint device will only have access to our corporate network in Digital Ocean and will not have access to the public internet directly. In a follow-up tutorial, we will showcase how to open the SIM up to the public internet.

<hr />

There are 5 main steps in the setup of this deployment:

1. [SIM card setup](#sim-card-setup)

2. [Cloud VPN setup](#cloud-vpn-setup)

3. [Cradlepoint IBR200 setup](#cradlepoint-ibr200-setup)

4. [Private Wireless Gateway setup](#private-wireless-gateway-setup)

5. [Cradlepoint SSH configuration](#cradlepoint-ssh-configuration)

Before we jump into the steps, let's explore the design of this system first. Below is a diagram of our final setup.

<img alt="Edge Device Deployment with Private Wireless Gateways" />

To ensure that we have direct access to the Cradlepoint device via a private IP address in our corporate network, we are going to connect a Digital Ocean Droplet (a Linux server) to a VRF-defined network on the Telnyx MPLS backbone via a Wireguard client. We will then spin up a private packet gateway in the Telnyx mobile core just for this SIM card and add that packet gateway to the same VRF-defined network that the Wireguard client is connected to. We will finally configure the Cradlepoint device to accept SSH access and connect directly into our Cradlepoint CLI via the private IP address that the packet gateway gives the SIM on our VRF-defined network.

## SIM Card Setup

Our first step is to order and register a Telnyx SIM card. SIM cards can be ordered in the mission Control portal and registered via the registration flow in the wireless section. You can learn more about registering a SIM card in our [quickstart guide](sims-esims.md).

When the SIM is inserted into the Cradlepoint device, the only custom configuration that is required to connect the SIM is to set the APN to `data00.telnyx`.

## Cloud VPN Setup

Next, we will configure a Wireguard client in a Digital Ocean Droplet to connect into a Cloud VPN on the Telnyx MPLS backbone. Follow the steps in our Digital Ocean Ubuntu Server to Cloud VPN tutorial.

When you can successfully ping the server endpoint on the Telnyx network, you can move to the next step.

## Cradlepoint IBR200 Setup

Before we create and configure a Private Wireless Gateway we will connect our Telnyx SIM card to the internet in our Cradlepoint device. Follow the steps in our [Cradlepoint IBR200 Cellular Router Setup Guide](cradlepoint-ibr200-cellular-router-setup-guide.md).

When you can successfully access the public internet via a connected device to the Cradlepoint network, you can move to the next step.

## Private Wireless Gateway Setup

A Private Wireless Gateway (PWG) must be associated with a Network resource in the portal. The PWG can be created in the [Private Wireless Gateways subsection](https://portal.telnyx.com/#/app/wireless/private-wireless-gateways) in the Wireless section of the portal.

Click the Create PWG button, enter a name and select the Network resource that you used for your Cloud VPN from [step 2](#cloud-vpn-setup).

<img alt="Create a Private Wireless Gateway using an existing Network" />

The PWG may take up to 15 minutes to create. This is due to the number of automated network configurations that are required to deploy an entirely new Dockerized PGW instance into our wireless mobile core.

When the PWG status changes to **provisioned**, we can associate our SIM Group. This can be done by navigating to the relevant SIM Group and setting the PWG to the one we just created. For the sake of this tutorial, it is best to associate a SIM group with just the SIM that you have inserted into your Cradlepoint device. By default, the SIMs in this SIM group will lose access to the public internet when added to the new PGW in our wireless mobile core.

Now that you have your SIM card associated with a new packet gateway via the PWG resource that you created on the same network as your Cloud VPN we can ping the IP of our SIM card from the Digital Ocean Droplet. Log into your Digital Ocean Ubuntu Server and ping the IP that your SIM is showing in the portal. The SIM card IP address can be viewed in the drill-down view for that SIM. When you have a successful ping working between your Digital Ocean server and SIM card in your Cradlepoint device, you can move on to the next step.

## Cradlepoint SSH Configuration

The final step is to enable SSH access on your Cradlepoint device. This is done via the Administration page in the Cradlepoint configuration console.

Connect to your Cradlepoint WiFi network and enter the LAN IP address or hostname of the router (assuming you are connecting from the LAN side) into a web browser's location field. By default, the LAN IP address is `192.168.0.1` and the router's hostname is `cp`:

Next, navigate to the **System** section on the left nav menu, and then select **Administration**.

Select **Local Management** from the drop-down menu.

Then check the **Enable SSH Server** entry box.

To access the CLI from your corporate network, select **Remote Admin** from the **Administration** drop-down menu, and check **Allow Remote SSH Access**.

Click **Save** *(if using Local Management)* or **Submit** *( if using Remote Admin)*.

<Callout type="info">
  *Allow Weak Cipher Support* is off by default. You may need to enable this depending on the SSH version and encryption algorithm that you are using on your server. It can be enabled by navigating to **System > Administration > Local Management > Allow Weak Cipher Support**.

Now that you have enabled SSH on the Cradlepoint device, you should be able to access the device from your Digital Ocean server.

From your Linux server run:

```bash theme={null}
ssh admin@[SIM_CARD_IP]
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

Enter the password that you used to access the Cradlepoint management console.

You should now have access to the Cradlepoint CLI without any internet access.
