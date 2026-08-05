---
title: How to set up a Private Wireless Gateway
summary: A step-by-step guide for provisioning a Telnyx Private Wireless Gateway (PWG),
  covering Cloud VPN setup, PWG interface creation, and routing configuration.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/private-wireless-gateway-how-to/index
updated_at: 2026-08-05T13:47:06Z
---

# How to set up a Private Wireless Gateway

A step-by-step guide for provisioning a Telnyx Private Wireless Gateway (PWG), covering Cloud VPN setup, PWG interface creation, and routing configuration.

## Overview

A Private Wireless Gateway (PWG) lets you route traffic from your cellular SIMs through a private network you control. Setting one up involves three main stages: creating a Cloud VPN network, provisioning the PWG interface, and configuring routing.

## Step 1: Set up Cloud VPN

1. Navigate to the **Network** section in the [Telnyx portal](https://portal.telnyx.com/#/app/next/networking/networks) and select **Create Network**.
2. Set the network name and click **Create**.
3. Add a VPN Interface, give it a name, and click **Create**.
4. Wait for provisioning to complete, then click **Next Step**.
5. Add a peer for the VPN — choose a name and click **Create Peer**.
6. Store the **Private Key** safely.
7. Skip **Buy global IP** if it is not needed.

![Private Wireless Gateways 1](https://mintcdn.com/telnyx/LhS1wAkFZcPBTrZO/img/pwg-stepbystep-1.svg)

## Step 2: Create a Private Wireless Gateway

1. In the **Wireless** section of the portal, select **Create PWG Interface**.
2. Name the interface and select the network created in Step 1. The region must match the VPN interface.
3. Accept the MRC charge.
4. Wait for the status to transition from **Provisioning** to **Provisioned**.
5. Create a SIM Group, then edit it and click **Connect PWG** to assign the PWG.
6. Add SIM cards to the group — individually or via the bulk action **Manage SIM Cards Setting**.

![Private Wireless Gateways 1](https://mintcdn.com/telnyx/LhS1wAkFZcPBTrZO/img/pwg-stepbystep-3.svg)

## Step 3: Configure routing

The network default gateway must be set up by the Telnyx Network team manually. Contact support via the Mission Control Portal chat to request this configuration.

Once configured, you can control which external destinations are reachable from devices connected through the PWG, and which are blocked.

![Private Wireless Gateways 1](https://mintcdn.com/telnyx/LhS1wAkFZcPBTrZO/img/pwg-stepbystep-4.svg)
