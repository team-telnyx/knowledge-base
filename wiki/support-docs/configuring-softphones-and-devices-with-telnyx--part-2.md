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

*Part 2 of 4 — see also: [Part 1](configuring-softphones-and-devices-with-telnyx--part-1.md), [Part 3](configuring-softphones-and-devices-with-telnyx--part-3.md), [Part 4](configuring-softphones-and-devices-with-telnyx--part-4.md)*

Step-by-step instructions for configuring Bria Solo (X-Lite), Grandstream Wave Lite (iOS and Android), the Grandstream GDS3710 video door system with Wave Lite, and the Grandstream GXV3370 IP video phone to work with Telnyx SIP trunks, plus an overview of the HD Voice number feature and its codec requirements.

## Grandstream Wave Lite (Android)

The [Grandstream Wave Lite softphone app](https://www.grandstream.com/support/product-archive) supports Android 4.0 and higher and is compatible with most Android mobile phones and tablets.

Additional resources include the [Wave Lite Android user manual](https://documentation.grandstream.com/knowledge-base/wave-lite-android-user-manual/#custom-settings), [Grandstream FAQ](https://blog.grandstream.com/faq), [Grandstream user forum](https://forums.grandstream.com/), and [Helpdesk](https://helpdesk.grandstream.com/).

### Configure a Telnyx SIP trunk on your device

1. From your Android device, open the Wave Lite app.
2. Navigate to **Settings** > **Account Settings** > **Generic Account** > **SIP Account**.

   > Do not use the VoIP Provider section, as Telnyx has not yet been added to the provider list.

3. Fill out the following fields:
   - **Activate Account:** Switch on to activate the account once created.
   - **Account Name:** A meaningful name for the connection (for example, `TelnyxTrunk`).
   - **SIP Server:** `sip.telnyx.com` (for USA; for other countries, see the [signaling addresses table](https://sip.telnyx.com/#signaling-addresses)).
   - **SIP User ID:** The SIP connection username. See [SIP Connection Types](sip-connection-types.md) for details.
   - **SIP Authentication ID:** The SIP connection username.
   - **SIP Password:** The SIP connection password.
   - **VoiceMail UserID:** The voicemail portal access number (typically `*97`).
   - **Display Name:** Your caller ID. Use capital letters, no special characters (spaces are allowed), and keep it under 15 characters for compatibility with some Canadian providers.
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

## Grandstream GDS3710 with Wave Lite (Android)

The [Grandstream GDS3710 video door system](https://www.grandstream.com/products/facility-management/facility-access-systems/product/gds3710) is designed for high-quality door monitoring, remote communication with visitors, property protection, and facility operations. The GDS3710 supports 2-way audio/video streaming and a SIP-based security mechanism that lets you stream calls from the GDS3710 to your Android device via Wave Lite.

Additional resources include the [GDS3710 datasheet (English)](https://www.grandstream.com/hubfs/Product_Documentation/datasheet_gds3710_english.pdf), [GDS3710 resources](https://www.grandstream.com/support/resources?title=GDS3710), [GDS3710 user manual](https://www.grandstream.com/hubfs/Product_Documentation/GDS3710_UserManual.pdf), [GDSManager user guide](https://www.grandstream.com/hubfs/Product_Documentation/GDSManager_User_Guide.pdf), and the [Wave Lite Android user manual](https://documentation.grandstream.com/knowledge-base/wave-lite-android-user-manual/#custom-settings).

### Prerequisites

- Ensure your GDS3710 is on firmware version 1.0.1.19 or higher.
- Ensure Wave Lite is on software version 1.0.2.16 or higher.
- Confirm you can log into the GDS3710 web GUI. The default address is `192.168.1.168`, the default username is `admin`, and the default random password is on the sticker on the GDS3710.

### Configure a Telnyx SIP trunk on your GDS3710

1. Log into the GDS3710 web GUI and navigate to **SIP Settings** > **SIP Basic Settings**.
2. Provide the following:
   - **Account Name:** A meaningful name (for example, `Doorbell`).
   - **SIP Server:** `sip.telnyx.com` (for USA; for other countries, see the [signaling addresses table](https://sip.telnyx.com/#signaling-addresses)).
   - **SIP User ID:** The SIP connection username. See [SIP Connection Types](sip-connection-types.md) for details.
   - **Authenticate ID:** The SIP connection username.
   - **Authenticate Password:** The SIP connection password.

   ![SIP Basic Settings section.](_images/315120cf602c05b1.png)

### Configure a Telnyx SIP trunk on the Wave Lite app

1. From your Android device, open the Wave Lite app.
2. Navigate to **Settings** > **Account Settings** > **Generic Account** > **SIP Account**.

   > Do not use the VoIP Provider section, as Telnyx has not yet been added to the provider list.

3. Fill out the following fields:
   - **Activate Account:** Switch on to activate the account once created.
   - **Account Name:** A meaningful name (for example, `TelnyxTrunk`).
   - **SIP Server:** `sip.telnyx.com` (for USA; for other countries, see the [signaling addresses table](https://sip.telnyx.com/#signaling-addresses)).
   - **SIP User ID:** Your SIP account or sub-account ID.
   - **SIP Authentication ID:** Your SIP account or sub-account ID.
   - **SIP Password:** Your SIP account or sub-account password.
   - **VoiceMail UserID:** The voicemail portal access number (typically `*97`).
   - **Display Name:** Your caller ID. Use capital letters, no special characters (spaces are allowed), and keep it under 15 characters for compatibility with some Canadian providers.
4. Tap the checkmark at the top-right to connect to Telnyx.

### Configure Wave Lite call settings

1. Tap the new account and select **Call Settings**.
2. Configure:
   - **SIP Port:** `5060` for TCP or UDP; `5061` for TLS.
   - **Transmission Protocol:** `TCP` or `UDP` unless you have set up encryption on your Telnyx portal, in which case choose `TLS`.
3. Tap the checkmark at the top-right to save.

### Configure Wave Lite codecs

1. Tap your new SIP account and select **Network Setting Parameters**.
2. Set **Preferred Vocoder** for WiFi, 2G, 3G, and 4G. Telnyx supports the following codecs:
   - **Audio:** `ulaw (g711u)`, `alaw (g711a)`, `g722`, `g729`
   - **Video:** `H264`
