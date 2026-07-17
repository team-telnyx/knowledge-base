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

*Part 4 of 7 — see also: [Part 1](telnyx-device-setup-nch-express-talk-and-fanvil-ip-phones--part-1.md), [Part 2](telnyx-device-setup-nch-express-talk-and-fanvil-ip-phones--part-2.md), [Part 3](telnyx-device-setup-nch-express-talk-and-fanvil-ip-phones--part-3.md), [Part 5](telnyx-device-setup-nch-express-talk-and-fanvil-ip-phones--part-5.md), [Part 6](telnyx-device-setup-nch-express-talk-and-fanvil-ip-phones--part-6.md), [Part 7](telnyx-device-setup-nch-express-talk-and-fanvil-ip-phones--part-7.md)*

Consolidated Telnyx setup guides for the NCH Express Talk softphone and several Fanvil IP phone families (X4G, X2C/X2P/X2CP, X7/X7C/X7A, V67/V65/V64/V62, X-series, and XU series), covering product overviews, prerequisites, SIP trunk configuration, codec selection, and optional TLS certificate setup.

## Fanvil V-Series (V67 / V65 / V64 / V62)

The [V67 Smart Video phone](https://www.fanvil.com/Product/info/id/157.html) is more than an efficient telephone but also a delicate work of art, providing a more intelligent and elegant office operation experience for executives, managers, and teleworkers. With a brand new design, V67 features an adjustable touch screen and a keypad with colorful light effect that improve the beauty and comfort of office desktop.

**V67 features:** Antibacterial surface protection, adjustable 7" color touchscreen, colorful light-up keypad, HD audio, Opus support, HD video, 10-party audio conferencing, built-in 2.4G/5G WiFi, built-in Bluetooth, Miracast.

The [V65 Prime Business phone](https://www.fanvil.com/Product/info/id/158.html) is more than an efficient telephone but a delicate work of art, providing a smart and smooth business communication experience for executives and managers. As the prime business phone featuring an adjustable screen and built-in Bluetooth 4.2 and 2.4G/5G Wi-Fi, V65 is a perfect combination of elegant outside and powerful inside.

**V65 features:** Antibacterial surface protection, adjustable 4.3" color touchscreen, HD audio, Opus support, HD video, 6-party audio conferencing, built-in 2.4G/5G WiFi, built-in Bluetooth, USB, link with security products.

The [V64 Prime Business phone](https://www.fanvil.com/Product/info/id/159.html) is more than an efficient telephone but a delicate work of art, providing a smart and smooth business communication experience for enterprises. As the prime business phone featuring a color LCD screen and built-in Bluetooth 4.2 and 2.4G/5G Wi-Fi, V64 is a perfect combination of elegant outside and powerful inside.

**V64 features:** 3.5" color LCD screen, HD audio, Opus support, 6-party audio conferencing, built-in 2.4G/5G WiFi, built-in Bluetooth, USB, link with security products, dual gigabit ports with integrated PoE.

The [V62 Essential Business phone](https://www.fanvil.com/Product/info/id/160.html) is more than an efficient telephone but a delicate work of art, providing a smart and smooth business communication experience for enterprises. As the essential business phone featuring a graphical dot-matrix screen with backlight and necessary VoIP features and other extended features, V62 is a great combination of elegant outside and powerful inside.

**V62 features:** HD audio, Opus support, 6-party audio conferencing, WiFi dongle, support EHS/Bluetooth wireless headset, USB, link with security products, dual gigabit ports with integrated PoE.

**Pre-requisites:**

- Ensure that your Telnyx Mission Command Portal is configured properly
- Recommended: Enable TLS to encrypt your traffic
- Make sure your phone is running the latest firmware
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

   ![Register Settings section of the Web GUI.](_images/4824a0b4d660ea0c.png)
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

- Firmware: V67 (see section 10.7.5, page 90 of the [user manual](https://www.fanvil.com/Uploads/Temp/download/20220310/6229a2f42d58f.pdf)), V65 (see section 10.7.5, page 104 of the [user manual](https://www.fanvil.com/Uploads/Temp/download/20220412/62555c3e41d94.pdf)), [V64](https://www.fanvil.com/Support/download/id/159.html), [V62](https://www.fanvil.com/Support/download/id/160.html)
- User manuals: [V67](https://www.fanvil.com/Uploads/Temp/download/20220310/6229ab6b347e3.pdf), [V64/V65](https://www.fanvil.com/Uploads/Temp/download/20220412/62555c3e41d94.pdf), [V62](https://www.fanvil.com/Uploads/Temp/download/20220310/6229ab6b347e3.pdf)
- [Fanvil FAQ](https://www.fanvil.com/Support/index.html)
- [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html)
- [Fanvil support](https://www.fanvil.com/Support/ticket.html)
