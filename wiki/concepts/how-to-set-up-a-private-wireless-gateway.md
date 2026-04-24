---
title: How to set up a Private Wireless Gateway
summary: Once configured, you can control which external destinations are reachable from devices connected through the PWG, and which are blocked.
sources:
  - url: https://developers.telnyx.com/docs/iot-sim/private-wireless-gateway-how-to/index
    content_hash: 2af13c576a18f1639bc8ebf11b3b72f72632f16bea942c94b1dfb8ab8a434d44
updated_at: 2026-04-10T00:00:00Z
---

# How to set up a Private Wireless Gateway

<img alt="Private Wireless Gateways 1" />

## Step 1: Set up Cloud VPN

1. Navigate to the [Network section](https://portal.telnyx.com/#/app/next/networking/networks) in the portal. Select "Create Network".
2. Set the network name and click "Create".
3. Add a VPN Interface, create a name, click "Create".
4. Wait for provisioning to complete, click "Next Step".
5. Add a peer for the VPN — choose a name, click "Create Peer".
6. Store the Private Key safely.
7. Skip "Buy global IP" if not needed.

## Step 2: Create a Private Wireless Gateway

<img alt="Private Wireless Gateways 1" />

1. Select "Create PWG Interface" in the Wireless section of the portal.
2. Name it and select the network from Step 1. Region must match the VPN interface.
3. Accept the MRC charge.
4. Wait for status to transition from Provisioning to Provisioned.
5. Create a SIM Group, then edit it and click "Connect PWG" to assign the PWG.
6. Add SIM cards to the group — individually or via bulk action "Manage SIM Cards Setting".

## Step 3: Configure routing

<img alt="Private Wireless Gateways 1" />

> **Warning:** The network default gateway must be set up by the Telnyx Network team manually. Contact support via the Mission Control Portal chat.

Once configured, you can control which external destinations are reachable from devices connected through the PWG, and which are blocked.


## Related Pages

- [Private Wireless Gateways](../runbooks/private-wireless-gateways.md)
- [Private Wireless Gateway (PGW)](../runbooks/private-wireless-gateway-pgw.md)
