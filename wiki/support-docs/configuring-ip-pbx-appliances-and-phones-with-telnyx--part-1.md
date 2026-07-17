---
title: Configuring IP PBX Appliances and Phones with Telnyx
summary: This page provides step-by-step instructions for configuring several popular
  IP PBX appliances and IP phones to work with Telnyx as the SIP carrier, including
  the Grandstream UCM6202 (using both Registration and IP authentication), the broader
  Grandstream UCM6xxx series, the Synway UC-200, and the Cisco 68xx/88xx series IP
  phones. Each section covers logging into the device's web UI, creating a SIP trunk,
  configuring inbound and outbound routes, and setting an outbound caller ID where
  applicable.
sources:
- url: https://support.telnyx.com/en/articles/1295514-grandstream-umc6202-auth-setup
- url: https://support.telnyx.com/en/articles/2950523-grandstream-ip-auth-setup
- url: https://support.telnyx.com/en/articles/5748258-grandstream-ucm6xxx-sip-trunks
- url: https://support.telnyx.com/en/articles/5800399-synway-uc-200-telnyx-setup
- url: https://support.telnyx.com/en/articles/5820309-cisco-68xx-88xx-setup
updated_at: 2026-07-17T09:08:00Z
---

# Configuring IP PBX Appliances and Phones with Telnyx

*Part 1 of 3 — see also: [Part 2](configuring-ip-pbx-appliances-and-phones-with-telnyx--part-2.md), [Part 3](configuring-ip-pbx-appliances-and-phones-with-telnyx--part-3.md)*

This page provides step-by-step instructions for configuring several popular IP PBX appliances and IP phones to work with Telnyx as the SIP carrier, including the Grandstream UCM6202 (using both Registration and IP authentication), the broader Grandstream UCM6xxx series, the Synway UC-200, and the Cisco 68xx/88xx series IP phones. Each section covers logging into the device's web UI, creating a SIP trunk, configuring inbound and outbound routes, and setting an outbound caller ID where applicable.

## Overview

This page covers how to configure several popular IP PBX appliances and IP phones to work with Telnyx as the SIP carrier. The devices covered include the Grandstream UCM6202 (using both Registration and IP authentication), the broader Grandstream UCM6xxx series, the Synway UC-200, and the Cisco 68xx/88xx series IP phones. Each section walks through logging into the device's web UI, creating a SIP trunk, configuring inbound and outbound routes, and (where applicable) setting an outbound caller ID.

Before starting any of these configurations, ensure that your Telnyx Mission Control Portal is set up correctly, you have purchased and provisioned a DID, and you have created a SIP connection (credentials-based or IP-based) and an outbound voice profile. It is also recommended that you enable TLS to encrypt your traffic.

## Grandstream UCM6202: Registration (User/Pass) Setup

The Grandstream UCM6202 is part of Grandstream's UCM6200 series IP PBX line, which combines enterprise-grade voice, video, data, and mobility features in a single appliance with no licensing fees.

### Pre-requisites

- Telnyx Mission Control Portal configured properly
- A DID purchased and provisioned to a SIP connection
- An outbound voice profile created
- A credentials connection created in Mission Control Portal
- Grandstream device running the latest firmware
- TLS encryption enabled (recommended)

### Log into the Grandstream Web UI

1. The IP address used to access the web UI depends on where your computer is connected:
   - If connected to the same switch/router as the UCM6200 WAN port, browse to the WAN IP shown on the device's LCD.
   - If connected to the LAN side, browse to the default IP `192.168.2.1`.
2. Default credentials are `admin` / `admin`. Units manufactured after January 2017 have a unique random password printed on a sticker on the back of the unit. Change the default password after first login.

### Configure the SIP Trunk

1. In the left-hand navigation, expand **Extension/Trunk** and click **VoIP Trunks**.
2. Click **Add SIP trunk** and fill in the required fields:
   - **Type:** Register SIP Trunk
   - **Provider Name:** Telnyx
   - **Host Name:** `sip.telnyx.com`
   - **Username:** Your Telnyx SIP username
   - **Password:** Your Telnyx SIP password
3. Click **Save**.

If you have issues using a hostname, you can use Telnyx's primary IP address `192.76.120.10` instead.

### Create an Inbound Route

1. Expand **Extension/Trunk** and click **Inbound Routes**.
2. Select the trunk and click **Add** under Inbound Routes.
3. Enter the patterns that apply to this inbound rule (see [Asterisk dialplan patterns](https://www.voip-info.org/asterisk-dialplan-patterns/) for formatting).
4. In default mode, set the default destination to **Extension**.
5. Click **Save**.

### Create an Outbound Route

1. Expand **Extension/Trunk** and click **Outbound Routes**.
2. Name the calling rule and add the number pattern.
3. Set the privilege level to match the service plan in your Telnyx portal's outbound settings.
4. Select your trunk in the **Use Trunk** section.

### Configure an Outbound Caller ID

Grandstream offers three ways to configure an outbound caller ID:

- **Global outbound CID:** Expand **PBX Settings** and click **General Settings**.
- **Per-extension CID:** Expand **Extension/Trunk**, click **Extensions**, select the extension, and enter the caller ID in the **CallerID Number** field.
- **Per-route CID:** Expand **Extension/Trunk**, click **Outbound Routes**, and set the caller ID in the **Outbound Route CID** field.

Caller ID naming conventions: use capital letters, no special characters (spaces are allowed), and keep the name under 15 characters for compatibility with Canadian providers. Review Telnyx's caller ID number policy before configuring.

## Grandstream UCM6202: IP Authentication Setup

The IP authentication setup follows the same overall flow as the registration setup, with the key difference being how the SIP trunk is configured.

### Pre-requisites

Same as the registration setup, except you must create an **IP connection** (rather than a credentials connection) in Mission Control Portal.

### Configure the SIP Trunk

1. Expand **Extension/Trunk** and click **VoIP Trunks**.
2. Click **Add SIP trunk** and fill in:
   - **Type:** Register SIP Trunk
   - **Provider Name:** Telnyx
   - **Host Name:** `192.76.120.10`
3. Click **Save**.

The remaining steps (inbound route, outbound route, outbound caller ID) are identical to the registration setup described above.
