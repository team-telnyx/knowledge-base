---
title: Telnyx PBX and IP Phone Setup
summary: Consolidated Telnyx setup guides for Yeastar P-Series, Yeastar S-Series,
  Vodia Multi-Tenant PBX, Epygi QX IP PBX, Positron IP PBX, ScopTEL IP PBX, and Positron
  IP phones, plus a reference table of Cisco/Linksys star codes. Each section covers
  prerequisites, trunk creation, outbound routing, and inbound routing so the device
  can place and receive calls using Telnyx as the SIP provider.
sources:
- url: https://support.telnyx.com/en/articles/13375115-how-to-configure-yeastar-p-series
- url: https://support.telnyx.com/en/articles/3185933-vodia-multi-tenant-pbx-setup
- url: https://support.telnyx.com/en/articles/5724344-cisco-linksys-star-codes
- url: https://support.telnyx.com/en/articles/5728748-epygi-ip-pbx-telnyx-setup
- url: https://support.telnyx.com/en/articles/5748952-yeastar-s-series-telnyx-sip
- url: https://support.telnyx.com/en/articles/5790910-positron-ip-pbx
- url: https://support.telnyx.com/en/articles/5803103-scoptel-ip-pbx
- url: https://support.telnyx.com/en/articles/5811761-positron-ip-phone
updated_at: 2026-07-17T09:08:57Z
---

# Telnyx PBX and IP Phone Setup

*Part 1 of 4 — see also: [Part 2](telnyx-pbx-and-ip-phone-setup--part-2.md), [Part 3](telnyx-pbx-and-ip-phone-setup--part-3.md), [Part 4](telnyx-pbx-and-ip-phone-setup--part-4.md)*

Consolidated Telnyx setup guides for Yeastar P-Series, Yeastar S-Series, Vodia Multi-Tenant PBX, Epygi QX IP PBX, Positron IP PBX, ScopTEL IP PBX, and Positron IP phones, plus a reference table of Cisco/Linksys star codes. Each section covers prerequisites, trunk creation, outbound routing, and inbound routing so the device can place and receive calls using Telnyx as the SIP provider.

## Overview

This page consolidates Telnyx setup guides for several PBX platforms and IP phones. Each section walks through prerequisites, trunk creation, outbound routing, and inbound routing so that the device can place and receive calls using Telnyx as the SIP provider.

Common prerequisites across all platforms include:

- An active, properly configured Telnyx Mission Control Portal account (see the [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)).
- A provisioned Telnyx DID.
- The Telnyx SIP server hostname `sip.telnyx.com` and port `5060`.
- TLS encryption is recommended where supported.

## Yeastar P-Series

The Yeastar P-Series supports both a credentials-based Register Trunk and an IP-based Peer Trunk. Telnyx is a Yeastar-certified ITSP, so the P-Series includes a Telnyx template that pre-fills most parameters.

### Set up a SIP registration (credentials) trunk

1. In the Yeastar PBX, go to **Extension and Trunk > Trunk** and click **Add**.

   ![](_images/4bfa822aa1f9e78b.png)
2. In **Basic Configuration**:
   - **Name:** A descriptive name for the trunk.
   - **Select ITSP Template:** Choose the country, then select the Telnyx ITSP name. All parameters are embedded except the account registration information.
   - **Trunk Status:** Enabled.

   ![](_images/430f395bb9ab16d5.png)
3. In **Detailed Configuration**, the certified ITSP template embeds Trunk Type, Transport, Hostname, Port, and Domain. If you need to override them, refer to <https://sip.telnyx.com/> for Telnyx proxies, transport, and port information.
   - **Username:** Your Telnyx username.
   - **Password:** Your Telnyx password.
   - **Authentication Name:** Same as the username.
   - **Enable Outbound Proxy:** Same as hostname.

   ![](_images/94603c742e8ac425.png)
4. Click **Save and Apply**, then verify the trunk shows a connected status (checkmark).

### Set up a Peer/IP authentication trunk

1. Log in to the PBX web portal and go to **Extension and Trunk > Trunk**, then click **Add**.
2. In **Basic**:
   - **Name:** Descriptive trunk name.
   - **Trunk Status:** Enabled.
   - **Select ITSP Template:** General.
3. In **Detailed Configuration**:
   - **Trunk Type:** Peer Trunk (Port Based). The static IP address and port of the PBX will be displayed; these must be added in the Telnyx Mission Control Portal under **SIP Trunking > Edit the IP type connection > Authentication and routing > IP addresses**.
   - **Transport:** UDP / TCP / TLS.
   - **Hostname/IP:** Telnyx domain name or IP address.
   - **Port:** Telnyx SIP port.
   - **Domain:** Same as Hostname/IP (used in SIP URI headers such as From/To).

   ![](_images/65e7f7f6bf4a78dd.png)

### Set up outgoing calls

1. Go to **Call Control > Outbound Route** and click **Add**.

   ![](_images/86cba92fa95e76e5.png)
2. Configure the route. Yeastar compares the dialed number against each route in order; higher-positioned routes are matched first.

   ![](_images/9e226a9732119a7c.png)

   - **Name:** Descriptive route name.
   - **Role:** Role allowed to use this outbound route.
   - **Dial Pattern:** `8.` (prefix `8` before the dialed number).
   - **Strip:** `1`.
   - **Trunk:** Select the Telnyx SIP trunk.
   - **Outbound Route Password:** Optional password prompt.
   - **Extension/Extension Group:** Allowed extensions.
   - **Time condition:** Optional time-based restriction.

   ![](_images/7094e812559de429.png)
3. Click **Save and Apply**. To call `01234567`, dial `801234567`.

### Set up incoming calls

1. Go to **Call Control > Inbound Route** and click **Add**.

   ![](_images/19ea21bccfed3aff.png)
2. Configure:
   - **Name:** Descriptive route name.
   - **DID Pattern:** Pattern to match incoming DIDs.
   - **Caller ID Pattern:** Allowed caller IDs.
   - **Trunk:** Telnyx SIP trunk.
   - **Default Destination:** Destination or time-conditioned destination.

   ![](_images/ce0c0df36077e37e.png)
3. Click **Save and Apply**.

Additional documentation:

- [Yeastar Cloud PBX (PCE) administrator guide](https://help.yeastar.com/en/p-series-cloud-edition/administrator-guide/about-this-guide.html)
- [Linkus server administrator guide](https://help.yeastar.com/en/p-series-linkus-cloud-edition/linkus-server-admin-guide/linkus-overview.html)
- [Yeastar P-Series Self-hosted PBX (PSE) installation guide](https://help.yeastar.com/en/p-series-software-edition/software-installation-guide/about-this-guide.html)
- [Yeastar P-Series PSE administrator guide](https://help.yeastar.com/en/p-series-software-edition/administrator-guide/about-this-guide.html)

## Yeastar S-Series

The Yeastar S-Series (and Yeastar Cloud PBX) supports both Register and Peer trunks.

### Set up a Register trunk

1. Go to **Settings > PBX > Trunks** and click **Add Trunk**.

   ![](_images/21144a26c6e11a9b.png)
2. Configure:
   - **Name:** Trunk name.
   - **Select Country:** General.
   - **Trunk Type:** Register Trunk.
   - **Hostname/IP:** VoIP provider domain (e.g., `peer.sip.com`).
   - **Domain:** Same as Hostname/IP.
   - **Username:** Telnyx username.
   - **Password:** Telnyx password.
   - **Authentication Name:** Telnyx authentication name (contact Telnyx support if needed).
   - **From User:** Telnyx username.

   ![](_images/5847986568e18321.png)
3. If the trunk DID differs from the authentication name, click **Advanced**, enter the Telnyx DID(s), select the DNIS checkbox, and enter a DNIS display name. Click **+** to add more DIDs.
4. Configure additional [VoIP trunk settings](https://help.yeastar.com/en/s-series/topic/voip-trunk-settings.html#topic_pyd_f3t_2fb) as needed.
5. Click **Save** and **Apply**.
6. Verify the trunk status in **PBX Monitor**.

   ![](_images/198673aaf4e33c4a.png)
7. Set the registration time to 300. Go to **Settings > PBX > General > SIP** and set **Default Registration Time** to `300`.

   ![](_images/fb42a63d1a6b3164.png)

### Set up a Peer trunk

1. Go to **Settings > PBX > Trunks** and click **Add Trunk**.

   ![](_images/21144a26c6e11a9b.png)
2. Configure:
   - **Name:** Trunk name.
   - **Select Country:** General.
   - **Trunk Type:** Peer Trunk.
   - **Hostname/IP:** VoIP provider domain.
   - **Domain:** Same as Hostname/IP.
3. Configure additional [VoIP trunk settings](https://help.yeastar.com/en/s-series/topic/voip-trunk-settings.html#topic_pyd_f3t_2fb) as needed.
4. Click **Save** and **Apply**, then verify in **PBX Monitor**.

   ![](_images/198673aaf4e33c4a.png)

### Set up outgoing calls

1. Go to **Settings > PBX > Call Control** and click **Outbound Routes**.

   ![](_images/1a97f18d1c30896b.png)
2. Click **Add** and configure:
   - **Route Name:** Descriptive name.
   - **Dial Pattern:** `8` (prefix to dial out).
   - **Strip:** `1`.
   - **Member Extensions:** Allowed extensions.
   - **Member Trunks:** Telnyx trunk.

   ![](_images/7343c2d9d8ac1a2a.png)

### Set up incoming calls

1. Go to **Settings > PBX > Call Control** and click **Inbound Routes**.

   ![](_images/07a4c083cb059162.png)
2. Click **Add** and configure:
   - **Name:** Descriptive name.
   - **Member Trunks:** Telnyx trunk.
   - **Destination:** Where incoming calls should be routed.
3. Click **Save**, then **Apply**.

   ![](_images/144ff1170b9f85b1.png)

Additional documentation:

- [Yeastar Cloud PBX admin guide](https://help.yeastar.com/en/cloudpbx/topic/admin_guide.html)
- [Yeastar S-Series admin guide](https://help.yeastar.com/en/s-series/topic/admin_guide.html)
