---
title: Telnyx Device Configuration Guides
summary: Step-by-step instructions for configuring Telnyx SIP trunks on a range of
  supported devices, including the Ribbon EdgeMarc 6000 SBC, Snom M100 KLE base station,
  Mitel 5320E/5330E/5340E and 6800/6900 SIP phones, and Alcatel SD601/SD602 SIP door
  phones. Each guide covers prerequisites, device access, SIP server settings, and
  registration parameters required to connect the device to the Telnyx Mission Control
  Portal.
sources:
- url: https://support.telnyx.com/en/articles/4215031-ribbon-edgemarc-6000-setup
- url: https://support.telnyx.com/en/articles/5822823-snom-m100-kle-telnyx-setup
- url: https://support.telnyx.com/en/articles/6244551-mitel-5320e-5330e-5340e-sip
- url: https://support.telnyx.com/en/articles/6249691-mitel-6800-6900-sip
- url: https://support.telnyx.com/en/articles/6281943-alcatel-sd601-sd602-sip-door
updated_at: 2026-08-05T13:36:02Z
---

# Telnyx Device Configuration Guides

*Part 1 of 4 — see also: [Part 2](telnyx-device-configuration-guides--part-2.md), [Part 3](telnyx-device-configuration-guides--part-3.md), [Part 4](telnyx-device-configuration-guides--part-4.md)*

Step-by-step instructions for configuring Telnyx SIP trunks on a range of supported devices, including the Ribbon EdgeMarc 6000 SBC, Snom M100 KLE base station, Mitel 5320E/5330E/5340E and 6800/6900 SIP phones, and Alcatel SD601/SD602 SIP door phones. Each guide covers prerequisites, device access, SIP server settings, and registration parameters required to connect the device to the Telnyx Mission Control Portal.

## Overview

This page consolidates Telnyx setup guides for several SIP-capable devices and session border controllers. Each device follows a similar pattern: confirm the Telnyx Mission Control Portal is configured, obtain the device's IP address, log into its web interface, and enter the Telnyx SIP server details (`sip.telnyx.com`) along with authentication credentials. TLS encryption on port 5061 is recommended where supported.

## Common Prerequisites

Before configuring any device, ensure the following are in place on the Telnyx side:

- The [Telnyx Mission Control Portal](telnyx-mission-control-portal.md) account is set up correctly.
- A DID has been purchased and provisioned to a SIP connection.
- An outbound voice profile has been created.
- An IP authentication connection (with optional tech prefix) is configured.
- TLS encryption is recommended for traffic security.

## Ribbon EdgeMarc 6000 Setup

The [Ribbon EdgeMarc 6000](https://ribboncommunications.com/solutions/enterprise-solutions/secure-cloud-communications-solutions/microsoft-solutions-teams-direct-routing) is an Intelligent Edge device that acts as a flexible demarcation and service insertion point with physical telephony ports. It is designed for unified communications and can connect to digital and analog legacy systems. This configuration guide is also compatible with EdgeMarc VOS 15.7.

Additional resources: [EdgeMarc 6000 documentation](https://rbbn.my.site.com/Support/login), [EdgeMarc/Ribbon support](https://ribboncommunications.com/services/ribbon-support-portal), [EdgeMarc VoIP settings overview](https://rbbn.my.site.com/Partners/login).

### Configure SIP Settings

1. Log into EdgeMarc.
2. From the left-hand navigation, choose **VoIP > SIP** to open the **SIP Settings** page.
3. In the **SIP protocol settings** section, enter:
   - **SIP Server Address:** `sip.telnyx.com`
   - **SIP Server Port:** `5060`
   - **SIP Server Transport:** `UDP`
   - **Use Custom Domain:** Check the box
   - **SIP Server Domain:** `sip.telnyx.com`
   - **Limit Inbound to listed Proxies:** Check the box
   - **Limit Outbound to listed Proxies:** Check the box

![SIP settings page on the EdgeMarc.](_images/2671e9f8dd38e047.png)

### Define the SIP Trunk Registration

1. From the left-hand navigation, choose **VoIP > SIP > B2BUA**.
2. In the **Trunking Devices** section, click **New Row** and provide:
   - **Name:** Identifier for the trunking device
   - **Model:** Select the PBX from the drop-down list
   - **IP:** Select the IP radio button and enter the PBX's IP address
   - **Transport:** `TLS` if using TLS encryption, otherwise `UDP` or `TCP`
   - **Port:** `5060` (or `5061` for TLS)

![SIP trunk configuration page.](_images/6b86478ce7440b41.png)

3. Click **Update** to create the trunking device, then click **Submit** to push the configuration to the EdgeMarc.

### Configure Inbound Rules

1. From the left-hand navigation, choose **VoIP > SIP > B2BUA** and click the **Match** tab.
2. Click **New Row** and provide:
   - **Direction:** `Inbound`
   - **Mode:** `BothModes`
   - **Default:** Select the radio button
   - **Action:** `Inbound`

### Configure Outbound Rules

1. From the left-hand navigation, choose **VoIP > SIP > B2BUA** and click the **Match** tab.
2. Click **New Row** and provide:
   - **Direction:** `Outbound`
   - **Mode:** `BothModes`
   - **Pattern:** Select the radio button, then choose `Calling` from the drop-down
   - **Called/Calling Party:** Enter `.` to allow all callers, or pattern-match (e.g., `1312270X`)
   - **Source:** `Any`
   - **Action:** `Outbound`
3. Click **Update**, then **Submit** to send the configuration to EdgeMarc.

## Snom M100 KLE Base Station Setup

The [Snom M100 KLE SIP DECT 4-Line Base Station](https://www.snomamericas.com/en/pd/ip-phones/m-series/m-kle-series/m100-kle) supports key system emulation, allowing shared line appearances locally without provider-side configuration. The M100 base supports up to 10 Snom KLE DECT Series phones, including the M10, M10R handsets, and M18 deskset.

Key features include up to 8 SIP account registrations, 4 programmable line keys, up to 4 parallel outgoing calls, a 1,000-entry phonebook, 200-entry call history, XML/LDAP remote phonebook, DND, 3-way local conference, N-way network conference, call transfer between DECT phones, intercom, call barring, dial plan, and a three-year manufacturer warranty.

Additional documentation: [Product specs](https://www.snomamericas.com/en/pd/ip-phones/m-series/m-kle-series/m100-kle#specifications), [Product datasheet](https://www.snomamericas.com/assets/0a504990-0017-40bf-a8d4-692cca8e7bc6/snom_M100-KLE_datasheet_en.pdf), [Admin provisioning manual](https://www.snomamericas.com/assets/8cfc3c61-4d11-4e71-b70e-8a2f64da9d18/Snom_US_M100%20KLE_Admin_Provisioning_Manual.pdf), [Quick reference guide](https://www.snomamericas.com/assets/cbe43ee7-7695-416c-8881-f0ba88825ebf/Snom_US_M100_KLE_QIG(print-ready).pdf), [Snom support](https://www.snomamericas.com/support/contact/), [Snom service hub](https://service.snom.com/), [Snom helpdesk](https://jira.snom.com/servicedesk/customer/user/login).

### Get the Device IP Address and Log In

1. Press the **Menu** (or **Select**) button on the phone.
2. Scroll to **Status** and press **Menu/Select**.
3. Highlight **Network** and press **Menu/Select**. Note the IP address.
4. From a computer on the same network, open a browser and enter `http://` followed by the IP address.
5. Log in with default credentials:
   - **User:** `admin`
   - **Password:** `admin`

### Configure the Base Station

1. Click the **System** tab.
2. In **General Account Settings**, enter:
   - **User Identifier:** Main SIP account or Subaccount UserID (e.g., `100000` or `100000_sub`)
   - **Authentication Name:** Main SIP account or Subaccount UserID
   - **Authentication Password:** Password for the SIP account
3. In the **SIP Server** section, enter:
   - **Server address:** `sip.telnyx.com`
   - **Port:** `5060` (or `5061` if TLS is enabled)
4. In the **Registration** section, enter:
   - **Server Address:** `sip.telnyx.com`
   - **Port:** `5060` (or `5061` if TLS is enabled)

![General Account Settings section.](_images/b964630f862729d3.png)

5. Click the **Status** tab. The account status should display as `Registered`.

![Status tab](_images/ce31d008569d71c1.png)
