---
title: 'Telnyx Device Setup: NCH Express Talk and Fanvil IP Phones'
summary: Consolidated Telnyx setup guides for the NCH Express Talk softphone and several
  Fanvil IP phone families (X4G, X2C/X2P/X2CP, X7/X7C/X7A, V67/V65/V64/V62, X-series,
  and XU series), covering product overviews, prerequisites, SIP trunk configuration,
  codec selection, and optional TLS certificate setup.
sources:
- url: https://support.telnyx.com/en/articles/5807457-nch-express-talk
- url: https://support.telnyx.com/en/articles/5811487-fanvil-x4g-telnyx-setup
- url: https://support.telnyx.com/en/articles/6206756-fanvil-x2cp-x2c-x2p-call-center-ip
- url: https://support.telnyx.com/en/articles/6209215-fanvil-x7-series-ip-phones
- url: https://support.telnyx.com/en/articles/6209862-fanvil-v-series-ip-phones
- url: https://support.telnyx.com/en/articles/6209971-fanvil-x-series-ip-phone
- url: https://support.telnyx.com/en/articles/6210147-fanvil-xu-series-ip-phone
updated_at: 2026-07-17T09:10:45Z
---

# Telnyx Device Setup: NCH Express Talk and Fanvil IP Phones

*Part 3 of 7 — see also: [Part 1](telnyx-device-setup-nch-express-talk-and-fanvil-ip-phones--part-1.md), [Part 2](telnyx-device-setup-nch-express-talk-and-fanvil-ip-phones--part-2.md), [Part 4](telnyx-device-setup-nch-express-talk-and-fanvil-ip-phones--part-4.md), [Part 5](telnyx-device-setup-nch-express-talk-and-fanvil-ip-phones--part-5.md), [Part 6](telnyx-device-setup-nch-express-talk-and-fanvil-ip-phones--part-6.md), [Part 7](telnyx-device-setup-nch-express-talk-and-fanvil-ip-phones--part-7.md)*

Consolidated Telnyx setup guides for the NCH Express Talk softphone and several Fanvil IP phone families (X4G, X2C/X2P/X2CP, X7/X7C/X7A, V67/V65/V64/V62, X-series, and XU series), covering product overviews, prerequisites, SIP trunk configuration, codec selection, and optional TLS certificate setup.

## Fanvil X7 Series (X7 / X7C / X7A)

The [Fanvil X7 IP phone](https://www.fanvil.com/Product/info/id/93.html) is a high-end enterprise phone for business users who need immediate access to all of their important information. In addition to a 7-inch capacitive touch screen for up to 127 DSS key entries, the telephone features 20 SIP lines, HD audio with Opus support, built-in Bluetooth, Wi-Fi connectivity, and more.

**X7 features:** 20 lines, HD audio, 7" color display, built-in Bluetooth, 127 DSS keys, WiFi connectivity.

The [Fanvil X7C IP phone](https://www.fanvil.com/Product/info/id/94.html) is a high-end enterprise IP phone for business users who need immediate access to all of their important information. In addition to a 5-inch high-resolution color screen, the telephone features 20 SIP lines, HD audio with Opus support, up to 60 DSS keys (12 physical), built-in Bluetooth, Wi-Fi connectivity, and more.

**X7C features:** 20 lines, HD audio, 5" color display, built-in Bluetooth, 60 DSS keys, WiFi connectivity.

The [Fanvil X7A IP phone](https://www.fanvil.com/Product/info/id/124.html) runs Android 9.0 OS and provides a more intelligent and smoother touch operation experience. 112 DSS keys on the 7-inch color touch screen, built-in WiFi, and built-in Bluetooth make daily communication smarter and simpler. With an optional USB camera (Fanvil CM60), the X7A can deliver superb audio and video for group conferences.

**X7A features:** Android 9.0 OS, 20 SIP lines, HD audio, 7" color touchscreen, built-in Bluetooth, 112 DSS keys, built-in 2.4G/5G WiFi.

**Pre-requisites:**

- Ensure that your Telnyx Mission Command Portal is configured properly
- Recommended: Enable TLS to encrypt your traffic
- Make sure your phone is running the [latest firmware](https://www.fanvil.com/Support/download/id/122.html)
- Make sure you can log into the web GUI (refer to the Web Management section of your phone's user manual)

### Configure a line with a Telnyx SIP trunk

1. Log into your web GUI and navigate to **Line > SIP**.
2. Use the **Line** dropdown to select a SIP line to configure.
3. In the **Register Settings** section, provide the following:
   1. **Username:** The SIP connection username (see the Credentials Connection Setup section of SIP connection types).
   2. **Display Name:** Your caller ID. Follow these naming conventions:
      1. Caller ID Name should be in capital letters for clearer display on some devices.
      2. Do not use special characters (they will not be displayed). Spaces are allowed.
      3. Some Canadian providers will not show more than 15 characters — consider shortening your caller ID.
   3. **Realm:** Enter the name of the realm to which the SIP interface is connected.
   4. **Authentication Name:** The SIP connection username.
   5. **Authentication Password:** The SIP connection password.
   6. **Server Name:** `sip.telnyx.com` (for international, see the [signaling addresses document](https://sip.telnyx.com/#signaling-addresses)).
4. In the **SIP Server 1** sub-section:
   1. **Server Address:** `sip.telnyx.com` (for international, see the [signaling addresses document](https://sip.telnyx.com/#signaling-addresses)).
   2. **Server Port:** `5060` for TCP/UDP transport, `5061` for TLS transport.
   3. **Transport Protocol:** Choose `TCP` or `UDP` unless you are encrypting traffic and have set up encryption on your Telnyx portal — in that case, choose `TLS`.

   ![Register Settings section of the web GUI.](_images/4824a0b4d660ea0c.png)
5. You can now configure the **SIP Server 2** section if you want.

### Configure voice and video settings

1. From the line you configured, expand the **Codecs Settings** section.
2. Set the priority and availability of audio and video codecs by adding or removing them from the list. Telnyx supports the following codecs:

   **Audio:**
   - `ulaw(g711u)`
   - `alaw(g711a)`
   - `g722`
   - `g729`

   **Video:**
   - `H264`

### (Optional) Upload a TLS certificate

If you are encrypting traffic with TLS, you'll need to upload a TLS certificate.

1. In the **Lines > SIP** section, find the **Advanced Settings** sub-section:
   1. **DTMF Type:** `RFC 2833`
   2. **Transportation Protocol:** Choose `TCP` or `UDP` unless you are encrypting traffic and have set up encryption on your Telnyx portal — in that case, choose `TLS`. If you are encrypting traffic, go into **Lines > Dial Peer** and make sure the **Port** setting is changed to `5061`.
   3. **RTP Encryption:** (Optional) Enable this if you're using TLS.
   4. **RTP Encryption Key:** (Optional) Obtain a key from [crt.sh](https://crt.sh/?id=1199354).
2. Navigate to **Line > Basic Settings** and find the **STUN Settings** section and set:
   1. **TLS Certification File:** Obtain a certificate from [crt.sh](https://crt.sh/?id=1199354).

**Additional resources:**

- Firmware: [X7](http://fanvil.com/Support/download/id/93.html), [X7C](https://www.fanvil.com/Support/download/id/94.html), [X7A](https://www.fanvil.com/Support/download/id/124.html), [X7A (with camera)](https://www.fanvil.com/Support/download/id/125.html)
- User manuals: [X7](https://www.fanvil.com/Uploads/Temp/download/20210106/5ff5946b8b78e.pdf), [X7C](https://www.fanvil.com/Uploads/Temp/download/20210106/5ff594a2412cf.pdf), [X7A](https://www.fanvil.com/Uploads/Temp/download/20210112/5ffd956d5a486.pdf), [X7A (with camera)](https://www.fanvil.com/Uploads/Temp/download/20210112/5ffd95117fb3f.pdf)
- [Fanvil FAQ](https://www.fanvil.com/Support/index.html)
- [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html)
- [Fanvil support](https://www.fanvil.com/Support/ticket.html)
