---
title: Configuring Softphones and SIP Endpoints with Telnyx
summary: Consolidated Telnyx setup guides for CounterPath Bria Solo (X-Lite), CounterPath
  Bria Teams, Grandstream Wave Lite on iOS and Android, and the Grandstream GDS3710
  video door system paired with Wave Lite. Each section walks through prerequisites,
  SIP account creation, call settings, codecs, and optional STUN or TLS configuration
  against Telnyx's SIP infrastructure.
sources:
- url: https://support.telnyx.com/en/articles/1130645-configuring-bria-solo-a-k-a-x-lite
- url: https://support.telnyx.com/en/articles/5772825-counterpath-bria-teams-setup
- url: https://support.telnyx.com/en/articles/6184748-grandstream-wave-lite-iphone
- url: https://support.telnyx.com/en/articles/6184897-grandstream-wave-lite-android
- url: https://support.telnyx.com/en/articles/6187273-grandstream-gds3710-wave-lite-android
- url: https://support.telnyx.com/en/articles/6187411-grandstream-gds3710-wave-lite-ios
updated_at: 2026-07-17T09:04:41Z
---

# Configuring Softphones and SIP Endpoints with Telnyx

*Part 2 of 3 — see also: [Part 1](configuring-softphones-and-sip-endpoints-with-telnyx--part-1.md), [Part 3](configuring-softphones-and-sip-endpoints-with-telnyx--part-3.md)*

Consolidated Telnyx setup guides for CounterPath Bria Solo (X-Lite), CounterPath Bria Teams, Grandstream Wave Lite on iOS and Android, and the Grandstream GDS3710 video door system paired with Wave Lite. Each section walks through prerequisites, SIP account creation, call settings, codecs, and optional STUN or TLS configuration against Telnyx's SIP infrastructure.

## Configuring Grandstream Wave Lite (iOS)

Wave Lite is a free Grandstream softphone that supports iOS 8.0 and higher.

### Configure a Telnyx SIP trunk on your device

1. Open the Wave Lite app on your iPhone or iPad.
2. Go to **Settings > Account Settings > Generic Account > SIP Account**. Do not use the VoIP Provider section — Telnyx is not on the provider list.
3. Fill in:
   - **Account Name:** e.g., `TelnyxTrunk`.
   - **SIP Server:** `sip.telnyx.com` (USA; see the [signaling addresses table](https://sip.telnyx.com/#signaling-addresses) for other countries).
   - **SIP User ID:** SIP connection username.
   - **SIP Authentication ID:** SIP connection username.
   - **SIP Password:** SIP connection password.

   ![SIP Account settings on the Wave Lite app.](_images/a8556e31ca1d8008.png)
   - **VoiceMail UserID:** Usually `*97`.
   - **Display Name:** Caller ID. Use capital letters, no special characters, max 15 characters, spaces allowed.

   ![SIP Account settings on the Wave Lite app.](_images/abbeead847b5839b.png)
4. Tap the checkmark at the top-right to connect to Telnyx.

### Configure call settings

1. Tap the new account and select **Call Settings**.
2. Set:
   - **SIP Port:** `5060` for TCP/UDP, `5061` for TLS.
   - **Transmission Protocol:** TCP or UDP, or TLS if encryption is enabled on the Telnyx portal.
3. Tap the checkmark at the top-right.

### Configure codecs

1. Tap the new SIP account and select **Network Setting Parameters**.
2. Set **Preferred Vocoder** for WiFi, 2G, 3G, and 4G. Telnyx supports:
   - Audio: `ulaw (g711u)`, `alaw (g711a)`, `g722`, `g729`
   - Video: `H264`

### (Optional) Configure your STUN server

1. Tap the new SIP account and select **Advanced Settings > General Settings**.
2. Set **STUN Server Settings:** `stun.telnyx.com:3478`.

## Configuring Grandstream Wave Lite (Android)

Wave Lite for Android supports Android 4.0 and higher.

### Configure a Telnyx SIP trunk on your device

1. Open the Wave Lite app on your Android device.
2. Go to **Settings > Account Settings > Generic Account > SIP Account**. Do not use the VoIP Provider section.
3. Fill in:
   - **Activate Account:** Toggle on to activate the account once created.
   - **Account Name:** e.g., `TelnyxTrunk`.
   - **SIP Server:** `sip.telnyx.com` (USA; see the [signaling addresses table](https://sip.telnyx.com/#signaling-addresses) for other countries).
   - **SIP User ID:** SIP connection username.
   - **SIP Authentication ID:** SIP connection username.
   - **SIP Password:** SIP connection password.
   - **VoiceMail UserID:** Usually `*97`.
   - **Display Name:** Caller ID. Use capital letters, no special characters, max 15 characters, spaces allowed.
4. Tap the checkmark at the top-right to connect to Telnyx.

### Configure call settings

1. Tap the new account and select **Call Settings**.
2. Set:
   - **SIP Port:** `5060` for TCP/UDP, `5061` for TLS.
   - **Transmission Protocol:** TCP or UDP, or TLS if encryption is enabled on the Telnyx portal.
3. Tap the checkmark at the top-right.

### Configure codecs

1. Tap the new SIP account and select **Network Setting Parameters**.
2. Set **Preferred Vocoder** for WiFi, 2G, 3G, and 4G. Telnyx supports:
   - Audio: `ulaw (g711u)`, `alaw (g711a)`, `g722`, `g729`
   - Video: `H264`

### (Optional) Configure your STUN server

1. Tap the new SIP account and select **Advanced Settings > General Settings**.
2. Set **STUN Server Settings:** `stun.telnyx.com:3478`.

## Configuring Grandstream GDS3710 with Wave Lite (Android)

The GDS3710 is a SIP-based video door system that streams 2-way audio/video to Wave Lite on Android. Requirements: GDS3710 firmware 1.0.1.19 or higher, Wave Lite 1.0.2.16 or higher, and access to the GDS3710 web GUI.

### Configure a Telnyx SIP trunk on your GDS3710

1. Log into the GDS3710 web GUI and go to **SIP Settings > SIP Basic Settings**.
2. Fill in:
   - **Account Name:** e.g., `Doorbell`.
   - **SIP Server:** `sip.telnyx.com` (USA; see the [signaling addresses table](https://sip.telnyx.com/#signaling-addresses) for other countries).
   - **SIP User ID:** SIP connection username.
   - **Authenticate ID:** SIP connection username.
   - **Authenticate Password:** SIP connection password.

   ![SIP Basic Settings section.](_images/315120cf602c05b1.png)

### Configure a Telnyx SIP trunk on the Wave Lite app

1. Open Wave Lite on your Android device.
2. Go to **Settings > Account Settings > Generic Account > SIP Account**. Do not use the VoIP Provider section.
3. Fill in:
   - **Activate Account:** Toggle on.
   - **Account Name:** e.g., `TelnyxTrunk`.
   - **SIP Server:** `sip.telnyx.com` (USA; see the [signaling addresses table](https://sip.telnyx.com/#signaling-addresses) for other countries).
   - **SIP User ID:** Your SIP account/sub-account ID.
   - **SIP Authentication ID:** Your SIP account/sub-account ID.
   - **SIP Password:** Your SIP account/sub-account password.
   - **VoiceMail UserID:** Usually `*97`.
   - **Display Name:** Caller ID. Use capital letters, no special characters, max 15 characters, spaces allowed.
4. Tap the checkmark at the top-right to connect to Telnyx.

### Configure Wave Lite call settings

1. Tap the new account and select **Call Settings**.
2. Set:
   - **SIP Port:** `5060` for TCP/UDP, `5061` for TLS.
   - **Transmission Protocol:** TCP or UDP, or TLS if encryption is enabled on the Telnyx portal.
3. Tap the checkmark at the top-right.

### Configure Wave Lite codecs

1. Tap the new SIP account and select **Network Setting Parameters**.
2. Set **Preferred Vocoder** for WiFi, 2G, 3G, and 4G. Telnyx supports:
   - Audio: `ulaw (g711u)`, `alaw (g711a)`, `g722`, `g729`
   - Video: `H264`

## Configuring Grandstream GDS3710 with Wave Lite (iOS)

The same GDS3710 setup applies when streaming to Wave Lite on iOS. Requirements: GDS3710 firmware 1.0.1.19 or higher, Wave Lite 1.0.2.16 or higher, and access to the GDS3710 web GUI.

### Configure a Telnyx SIP trunk on your GDS3710

1. Log into the GDS3710 web GUI and go to **SIP Settings > SIP Basic Settings**.
2. Fill in:
   - **Account Name:** e.g., `Doorbell`.
   - **SIP Server:** `sip.telnyx.com` (USA; see the [signaling addresses table](https://sip.telnyx.com/#signaling-addresses) for other countries).
   - **SIP User ID:** SIP connection username.
   - **Authenticate ID:** SIP connection username.
   - **Authenticate Password:** SIP connection password.

   ![SIP Basic Settings section.](_images/315120cf602c05b1.png)

### Configure a Telnyx SIP trunk on the Wave Lite app

1. Open Wave Lite on your iPhone or iPad.
2. Go to **Settings > Account Settings > Generic Account > SIP Account**. Do not use the VoIP Provider section.
3. Fill in:
   - **Account Name:** e.g., `TelnyxTrunk`.
   - **SIP Server:** `sip.telnyx.com` (USA; see the [signaling addresses table](https://sip.telnyx.com/#signaling-addresses) for other countries).
   - **SIP User ID:** SIP connection username.
   - **SIP Authentication ID:** SIP connection username.
   - **SIP Password:** SIP connection password.

   ![Generic Account section for adding new account.](_images/a8556e31ca1d8008.png)
   - **VoiceMail UserID:** Usually `*97`.
   - **Display Name:** Caller ID. Use capital letters, no special characters, max 15 characters, spaces allowed.

   ![Generic Account section.](_images/abbeead847b5839b.png)
4. Tap the checkmark at the top-right to connect to Telnyx.

### Configure Wave Lite call settings

1. Tap the new account and select **Call Settings**.
2. Set:
   - **SIP Port:** `5060` for TCP/UDP, `5061` for TLS.
   - **Transmission Protocol:** TCP or UDP, or TLS if encryption is enabled on the Telnyx portal.
3. Tap the checkmark at the top-right.

### Configure Wave Lite codecs

1. Tap the new SIP account and select **Network Setting Parameters**.
2. Set **Preferred Vocoder** for WiFi, 2G, 3G, and 4G. Telnyx supports:
   - Audio: `ulaw (g711u)`, `alaw (g711a)`, `g722`, `g729`
   - Video: `H264`
