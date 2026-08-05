---
title: Configuring Softphones and Devices with Telnyx
summary: Step-by-step instructions for configuring Bria Solo (X-Lite), Grandstream
  Wave Lite (iOS and Android), the Grandstream GDS3710 video door system with Wave
  Lite, and the Grandstream GXV3370 IP video phone to work with Telnyx SIP trunks,
  plus an overview of the HD Voice number feature and its codec requirements.
sources:
- url: https://support.telnyx.com/en/articles/1130645-configuring-bria-solo-a-k-a-x-lite
- url: https://support.telnyx.com/en/articles/6184748-grandstream-wave-lite-iphone
- url: https://support.telnyx.com/en/articles/6184897-grandstream-wave-lite-android
- url: https://support.telnyx.com/en/articles/6187273-grandstream-gds3710-wave-lite-android
- url: https://support.telnyx.com/en/articles/6187411-grandstream-gds3710-wave-lite-ios
- url: https://support.telnyx.com/en/articles/6187576-grandstream-gxv3370
- url: https://support.telnyx.com/en/articles/8394071-hd-voice-number-feature
updated_at: 2026-08-05T13:30:00Z
---

# Configuring Softphones and Devices with Telnyx

*Part 1 of 4 — see also: [Part 2](configuring-softphones-and-devices-with-telnyx--part-2.md), [Part 3](configuring-softphones-and-devices-with-telnyx--part-3.md), [Part 4](configuring-softphones-and-devices-with-telnyx--part-4.md)*

Step-by-step instructions for configuring Bria Solo (X-Lite), Grandstream Wave Lite (iOS and Android), the Grandstream GDS3710 video door system with Wave Lite, and the Grandstream GXV3370 IP video phone to work with Telnyx SIP trunks, plus an overview of the HD Voice number feature and its codec requirements.

## Overview

This page consolidates Telnyx configuration guidance for several popular softphones and Grandstream devices, along with the HD Voice number feature. Each device section covers the prerequisites, SIP trunk setup, call settings, and codec configuration needed to make and receive calls through Telnyx.

Before configuring any device, ensure your Telnyx Mission Control Portal is set up correctly and you have created a credentials-based SIP connection, purchased a DID, provisioned the number, and created an outbound voice profile. Enabling TLS to encrypt traffic is recommended.

## Bria Solo (X-Lite)

[Bria Solo](https://www.counterpath.com/) (also known as X-Lite) is a softphone client created by CounterPath for Windows and Mac that helps users transition to VoIP. It can be used on Windows or Mac OS platforms only.

For additional documentation, see the [Bria Solo/X-Lite technical documentation](https://www.counterpath.com/x-lite/) and [CounterPath support](https://support.counterpath.com/hc/en-us/categories/360002425273-Bria-Solo).

### Set up a SIP account on Bria Solo

1. Open Bria Solo/X-Lite.
2. From the main menu, choose **Softphone > Account Settings**.

   ![An interface to set up a SIP account on Bria Solo.](_images/5ec7ffe7b25e7f7f.png)
3. From the Accounts window, fill out the following fields:

   - **Account Name section:**
     - **Account Name:** Used to identify the account. Make it something meaningful to you.
     - **Protocol:** Read-only and always SIP.
   - **Allow this Account For section:**
     - **Calls** (Windows) or **Used for Call** (Mac): Check to allow outbound calls.
     - **IM/Presence** (Windows) or **Presence** (Mac): Check to share online presence and send IMs.
   - **User Details section:**
     - **User ID:** The account ID for the softphone, provided by Telnyx.
     - **Domain:** `sip.telnyx.com`
     - **Password:** The password for the softphone, provided by Telnyx.
     - **Display Name:** The name displayed in the Bria title bar and seen by remote parties.
     - **Authorization Name:** Complete only if Telnyx provided one. Typically not required unless you need to allow user IDs that are easy to guess.
   - **Domain Proxy section:**
     - **Register with domain and receive calls:** Check to receive incoming calls. Clear this if your service does not include inbound calling, otherwise registration may fail.
     - **Send outbound via:** Select if Telnyx requires traffic to be directed to proxies discovered via the domain. If selected, complete the Address field with the IP address provided by Telnyx.
   - **Dial Plan section:** Read-only information about numbers used by Telnyx.

   ![A picture of Dial Plan section during SIP account setup.](_images/a6eb7a639a966e9c.png)
4. Click **OK** to register the softphone with `sip.telnyx.com`. If everything is correct, the account will be enabled successfully.

   ![A picture of an ideal SIP account setup.](_images/3715f2ac83a0eae1.png)

## Grandstream Wave Lite (iPhone)

The [Grandstream Wave Lite softphone app](https://www.grandstream.com/support/product-archive) is a free softphone that supports Apple iOS 8.0 or higher and is compatible with most iOS mobile phones and tablets. It allows users to connect to SIP accounts from anywhere in the world.

Additional resources include the [Wave Lite iOS user manual](https://documentation.grandstream.com/knowledge-base/wave-lite-ios-user-manual/), [Grandstream FAQ](https://blog.grandstream.com/faq), [Grandstream user forum](https://forums.grandstream.com/), and [Helpdesk](https://helpdesk.grandstream.com/).

### Configure a Telnyx SIP trunk on your device

1. From your iPhone or iPad, open the Wave Lite app.
2. Navigate to **Settings** > **Account Settings** > **Generic Account** > **SIP Account**.

   > Do not use the VoIP Provider section, as Telnyx has not yet been added to the provider list.

3. Fill out the following fields:
   - **Account Name:** A meaningful name for the connection (for example, `TelnyxTrunk`).
   - **SIP Server:** `sip.telnyx.com` (for USA; for other countries, see the [signaling addresses table](https://sip.telnyx.com/#signaling-addresses)).
   - **SIP User ID:** The SIP connection username. See [SIP Connection Types](sip-connection-types.md) for details.
   - **SIP Authentication ID:** The SIP connection username.
   - **SIP Password:** The SIP connection password.

   ![SIP Account settings on the Wave Lite app.](_images/a8556e31ca1d8008.png)
   - **VoiceMail UserID:** The voicemail portal access number (typically `*97`).
   - **Display Name:** Your caller ID. Use capital letters, no special characters (spaces are allowed), and keep it under 15 characters for compatibility with some Canadian providers.

   ![SIP Account settings on the Wave Lite app.](_images/abbeead847b5839b.png)
4. Tap the checkmark at the top-right to connect to Telnyx.

### Configure call settings

1. Tap the new account and select **Call Settings**.
2. Configure:
   - **SIP Port:** `5060` for TCP or UDP; `5061` for TLS.
   - **Transmission Protocol:** `TCP` or `UDP` unless you have set up encryption on your Telnyx portal, in which case choose `TLS`.
3. Tap the checkmark at the top-right to save.

### Configure codecs

1. Tap your new SIP account and select **Network Setting Parameters**.
2. Set **Preferred Vocoder** for WiFi, 2G, 3G, and 4G. Telnyx supports the following codecs:
   - **Audio:** `ulaw (g711u)`, `alaw (g711a)`, `g722`, `g729`
   - **Video:** `H264`

### (Optional) Configure your STUN server

1. Tap your new SIP account and select **Advanced Settings** > **General Settings**.
2. Set **STUN Server Settings** to `stun.telnyx.com:3478`.
