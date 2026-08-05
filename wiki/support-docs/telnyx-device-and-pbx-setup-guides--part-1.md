---
title: Telnyx Device and PBX Setup Guides
summary: Step-by-step instructions for configuring a range of SIP-capable devices
  and IP PBX systems to work with the Telnyx Mission Control Portal, including Mediatrix
  C7/4100 gateways, Positron IP PBX and IP phones, Synway UC-200, ScopTEL IP PBX,
  Flyingvoice IP phones, and Dinstar C60 series phones.
sources:
- url: https://support.telnyx.com/en/articles/5733572-mediatrix-c7-4100-telnyx-setup
- url: https://support.telnyx.com/en/articles/5790910-positron-ip-pbx
- url: https://support.telnyx.com/en/articles/5800399-synway-uc-200-telnyx-setup
- url: https://support.telnyx.com/en/articles/5803103-scoptel-ip-pbx
- url: https://support.telnyx.com/en/articles/5810663-flyingvoice-telnyx-setup
- url: https://support.telnyx.com/en/articles/5811761-positron-ip-phone
- url: https://support.telnyx.com/en/articles/6128321-dinstar-c60-setup-config
updated_at: 2026-08-05T13:36:04Z
---

# Telnyx Device and PBX Setup Guides

*Part 1 of 3 — see also: [Part 2](telnyx-device-and-pbx-setup-guides--part-2.md), [Part 3](telnyx-device-and-pbx-setup-guides--part-3.md)*

Step-by-step instructions for configuring a range of SIP-capable devices and IP PBX systems to work with the Telnyx Mission Control Portal, including Mediatrix C7/4100 gateways, Positron IP PBX and IP phones, Synway UC-200, ScopTEL IP PBX, Flyingvoice IP phones, and Dinstar C60 series phones.

## Overview

This page consolidates Telnyx setup guides for several SIP-capable devices and IP PBX systems. Each section walks through the prerequisites, network connection, and configuration steps required to register the device or PBX with the Telnyx Mission Control Portal using the SIP server `sip.telnyx.com`.

Common prerequisites across all setups include:

- A properly configured [Telnyx Mission Control Portal](telnyx-mission-control-portal.md) account.
- A provisioned DID (Direct Inward Dialing) number from Telnyx.
- The Telnyx SIP account or sub-account username and password.
- The device or PBX connected to the same local network as the configuration computer.
- Recommended: enabling TLS to encrypt SIP traffic.

## Mediatrix C7/4100 Gateway Setup

The [Mediatrix C7 Series](mediatrix-c7-series.md) gateways combine a VoIP analog adaptor and media gateway with FXS, FXO, and BRI interfaces. The setup criteria for the Mediatrix 4100 are the same as the C7 unless otherwise noted.

### Connect the device to the network

1. Connect the device to your router/network via the **ETH1** port (**WAN** on the 4100). It is set to obtain an IP address from DHCP.
2. The **ETH2** port (**LAN** on the 4100) has a default IP of `192.168.1.2` and is used for direct management via a web browser.
3. If the Power LED is on, connect a phone to a telephony port and dial `*#*0` to hear the device's IP address.
4. If the Power LED is off, verify the network cable, the router/switch port, or connect directly to a computer via ETH2/LAN.

### Access the Mediatrix GUI

1. From a computer on the same network, open a browser and enter the device's IP address.
2. Default login: **Username:** `public`, **Password:** (empty).

### Set the Telnyx server FQDN

1. Navigate to **SIP > Servers**.
2. Set **Registrar Host** and **Proxy Host** to `sip.telnyx.com`.
3. Click **Apply**.

### Restart required services

After applying, restart the required services from the prompt at the top of the screen or via the **Services Table**.

### Register telephony ports

1. Navigate to **SIP > Registrations**.
2. For each analog port to register, set:
   - **Username:** Telnyx account or sub-account username.
   - **Friendly Name:** Display name for outgoing calls.
   - **Register:** Enable.
3. Click **Apply**.

### Set Telnyx credentials

1. Navigate to **SIP > Authentications** and click **Edit All Entries**.
2. For each registered port, set:
   - **Criteria:** Endpoint.
   - **Endpoint:** Select the telephony port.
   - **Validate Realm:** Disable.
   - **Username:** Telnyx account/sub-account username.
   - **Password:** Telnyx account/sub-account password.
3. Click **Apply & Refresh Registration**.

### Configure auto-routing

1. Navigate to **Call Router > Auto-routing**.
2. Set **Auto-routing:** Enable and **Criteria Type:** SIP Username.
3. Click **Apply**.
4. Verify under **Call Router > Status** that auto routes are present.

### Disable G.711 a-law codec (North America only)

1. Navigate to **Media > Codecs**.
2. Disable **G.711 a-law** for both Voice and Data, then click **Apply**.
3. Restart required services.
4. Edit the **G.711 µ-Law** codec and set **Minimum Packetization:** 20ms and **Maximum Packetization:** 30ms.

### Set dial patterns (DTMF maps)

1. Navigate to **Telephony > DTMF Maps**.
2. In the second row, set **DTMF Map:** `*xx` and **Transformation:** `x`.
3. Click **Apply**.

### (Optional) Set a time server

1. Navigate to **Network > Host**.
2. In the **SNTP Configuration** table, set **SNTP Configuration Source:** Static and **Primary SNTP:** `pool.ntp.org` (or another reachable SNTP server).
3. Click **Apply**.

## Positron IP PBX Setup

Positron IP PBX Solutions offers small and medium-sized businesses VoIP phone systems that combine voice and data. Note that Positron PBX documentation is limited; the available guides are dated (2013) and primarily available to partners.

### Configure the Positron PBX trunk

1. Log into the Positron PBX portal and go to **PBX > Trunks/Lines > Trunks/Lines**.
2. Click **Add** and provide:
   - **Name:** e.g., `Telnyx`.
   - **IP Address/Domain:** `sip.telnyx.com`.
   - **Username:** Telnyx SIP account username.
   - **Password:** Telnyx SIP account password.
   - **Port:** `5060`.
3. Click **Save**, then **Edit** the new trunk and set:
   - **From User:** Remove the username.
   - **P-Asserted-Identity:** Select `Custom` and enter the provisioned DID.
4. Click **Save**, then **Apply**.

### Configure outbound rules

1. Go to **PBX > Trunks/Lines > Outgoing Line Groups** and create a new group linked to the Telnyx trunk.
2. Go to **PBX > Call Handling > Outgoing Call Rules** and assign the ruleset to extensions.

### Configure inbound rules

1. Go to **PBX > Trunks/Lines > Incoming Call Rules** and create a new group linked to the trunk.
2. Click **Edit**, enter the provisioned DID in the **DID** field, and choose the destination extension (IVR, ring group, or simple extension).

If using another SIP trunk alongside Telnyx, set the **SIP Registration Timer** to a minimum of 600 under **PBX > PBX Settings > SIP**.

## Synway UC-200 PBX Setup

The [Synway UC-200](synway-uc-200.md) is an IP PBX appliance supporting up to 500 registered users with no licensing fees. It is configured through a web browser interface.

### Log into the UC-200

1. From a PC on the same network, open Chrome 67, Firefox 60, or IE11 and navigate to `https://192.168.0.101`.
2. Default credentials: **Username:** `admin`, **Password:** `admin`. Change these immediately after first login.

### Configure network settings

1. Navigate to **System > Network Settings > Network Settings**.
2. On the **Basic Settings** tab, set **Default interface:** `LAN` and configure LAN settings as needed.

### Create the SIP trunk

1. Navigate to **PBX > Trunks > Create Trunk** and provide:
   - **Trunk Type:** `SIP`.
   - **Trunk Name:** A descriptive name.
   - **Transport:** `UDP`.
   - **Register:** `Yes`.
   - **Username:** Telnyx SIP username.
   - **Password:** Telnyx SIP password.
   - **RegFall Retry:** 30 seconds (default).
   - **Keep Inbound CallerID:** Use the registered account as the caller ID.
   - **Outbound CallerID Name:** Caller ID in CAPITAL LETTERS, no special characters, max 15 characters.
   - **Record:** `False` (default).
   - **Enabled:** `True` (default).
   - **Profile:** `LAN`.
   - **Trunk IP/Domain:** `sip.telnyx.com:5060`.

### Configure outbound route

1. Navigate to **PBX > Trunks > Outbound Routes** and click **Add**.
2. Provide:
   - **Name:** e.g., `Telnyx_outbound`.
   - **Dial/DID patterns:** Regex matching the desired dial pattern.
   - **Strip:** Number of digits to strip (e.g., 1 if users dial 9 to access an outside line).
   - **Prepend:** Optional digits to prepend (e.g., area code for 7-digit dialing).
   - **Member Extensions:** Extensions authorized to use this route (required).
   - **Member Gateways:** Select the Telnyx trunk (required).
   - **Password:** Optional, for safety.

### Configure inbound route

1. Navigate to **PBX > Trunks > Inbound Routes** and click **Add**.
2. Provide:
   - **Name:** e.g., `Telnyx_inbound`.
   - **Dial/DID patterns:** Regex matching the inbound pattern.
   - **Destination:** Default extension for incoming calls.
   - **Member Trunks:** Select the Telnyx trunk (required).

### Run a call test

1. Log into the Synway portal and dial extension `1000` to perform a ping call.
2. Verify the call appears under **CDR** in the left-hand navigation.
