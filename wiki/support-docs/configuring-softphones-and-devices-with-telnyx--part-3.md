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

*Part 3 of 4 — see also: [Part 1](configuring-softphones-and-devices-with-telnyx--part-1.md), [Part 2](configuring-softphones-and-devices-with-telnyx--part-2.md), [Part 4](configuring-softphones-and-devices-with-telnyx--part-4.md)*

Step-by-step instructions for configuring Bria Solo (X-Lite), Grandstream Wave Lite (iOS and Android), the Grandstream GDS3710 video door system with Wave Lite, and the Grandstream GXV3370 IP video phone to work with Telnyx SIP trunks, plus an overview of the HD Voice number feature and its codec requirements.

## Grandstream GDS3710 with Wave Lite (iOS)

The same GDS3710 video door system can be paired with Wave Lite on iOS devices for remote monitoring and 2-way audio/video streaming.

Additional resources include the [GDS3710 datasheet (English)](https://www.grandstream.com/hubfs/Product_Documentation/datasheet_gds3710_english.pdf), [GDS3710 resources](https://www.grandstream.com/support/resources?title=GDS3710), [GDS3710 user manual](https://www.grandstream.com/hubfs/Product_Documentation/GDS3710_UserManual.pdf), [GDSManager user guide](https://www.grandstream.com/hubfs/Product_Documentation/GDSManager_User_Guide.pdf), and the [Wave Lite iOS user manual](https://documentation.grandstream.com/knowledge-base/wave-lite-ios-user-manual/).

### Prerequisites

- Ensure your GDS3710 is on [firmware version 1.0.1.19 or higher](https://www.grandstream.com/support/firmware).
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

1. From your iPhone or iPad, open the Wave Lite app.
2. Navigate to **Settings** > **Account Settings** > **Generic Account** > **SIP Account**.

   > Do not use the VoIP Provider section, as Telnyx has not yet been added to the provider list.

3. Fill out the following fields:
   - **Account Name:** A meaningful name (for example, `TelnyxTrunk`).
   - **SIP Server:** `sip.telnyx.com` (for USA; for other countries, see the [signaling addresses table](https://sip.telnyx.com/#signaling-addresses)).
   - **SIP User ID:** The SIP connection username. See [SIP Connection Types](sip-connection-types.md) for details.
   - **SIP Authentication ID:** The SIP connection username.
   - **SIP Password:** The SIP connection password.

   ![Generic Account section for adding new account.](_images/a8556e31ca1d8008.png)
   - **VoiceMail UserID:** The voicemail portal access number (typically `*97`).
   - **Display Name:** Your caller ID. Use capital letters, no special characters (spaces are allowed), and keep it under 15 characters for compatibility with some Canadian providers.

   ![Generic Account section.](_images/abbeead847b5839b.png)
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

## Grandstream GXV3370

The [GXV3370 IP Video Phone](https://www.grandstream.com/products/ip-video-telephony/ip-video-phones-android/product/gxv3370) for Android combines a 16-line IP video phone with a multi-platform video conferencing solution and the functionality of an Android tablet. It features a 7" 1024×600 capacitive touch screen TFT LCD, camera, dual gigabit ports with PoE/PoE+, HD audio and video, integrated Wi-Fi (802.11a/b/g/n) and Bluetooth, and rich peripheral interfaces.

Additional resources include the [GXV3370 user manual](https://documentation.grandstream.com/knowledge-base/gxv3370-user-guide/), [GS Affinity user manual](https://documentation.grandstream.com/knowledge-base/gs-affinity-user-guide/), [GXV3370 administration guide](https://documentation.grandstream.com/knowledge-base/gxv3370-administration-guide/), [firmware upgrade guide](https://documentation.grandstream.com/knowledge-base/firmware-upgrade-guide/), and [all other GXV3370 reference material](https://documentation.grandstream.com/article-categories/gxv3370/).

### Prerequisites

- Ensure your device is on the [latest firmware](https://documentation.grandstream.com/knowledge-base/firmware-upgrade-guide/).
- Use the phone's base or handset to find the device IP address, which links to the web portal where configuration is completed. See the [Provisioning section of the Admin Guide](https://documentation.grandstream.com/knowledge-base/gxv3370-administration-guide/#upgrade-and-provisioning-configuration) for details.

### Configure a Telnyx SIP trunk on your device

1. [Log into the Web GUI](https://documentation.grandstream.com/knowledge-base/gxv3370-administration-guide/#upgrade-and-provisioning-configuration).
2. Navigate to **Account** > **General Settings**. In the **On Register** section, provide the following:
   - **Account Active:** Switch to determine if the account becomes active once created. Default for the first account is `Yes`.
   - **Account Name:** A meaningful name (for example, `TelnyxTrunk`).
   - **SIP Server:** `sip.telnyx.com` (for USA; for other countries, see the [signaling addresses table](https://sip.telnyx.com/#signaling-addresses)).
   - **SIP User ID:** Your SIP account or sub-account ID.
   - **SIP Authentication ID:** The SIP connection username. See [SIP Connection Types](sip-connection-types.md) for details.
   - **SIP Password:** The SIP connection password.
   - **Display Name:** Your caller ID. Use capital letters, no special characters (spaces are allowed), and keep it under 15 characters for compatibility with some Canadian providers.
   - **VoiceMail Access Number:** The voicemail portal access number (typically `*97`).
   - **Outbound Proxy:** `sip.telnyx.com`
3. Still on the **Account** screen, go to **SIP Settings** > **SIP Basic Settings** and provide:
   - **SIP registration:** Leave enabled to send SIP Register messages to the proxy/server.
   - **SIP transport:** Default is `UDP`. Choose `TLS/TCP` if you have [configured your Telnyx portal to encrypt data](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication).
   - **Local SIP port:** `5060` for UDP; `5061` for TLS/TCP.

### Configure codecs

1. Still on the **Account** screen, go to **Codec Settings** > **Preferred Vocoder** and provide:
   - **Preferred Vocoder:** Select codecs for WiFi, 2G, 3G, and 4G. Telnyx supports:
     - **Audio:** `ulaw (g711u)`, `alaw (g711a)`, `g722`, `g729`
   - **DTMF:** `RFC2833`
2. In the **Preferred Video Codec** section, set **Preferred Video Codec** to `H264`.
