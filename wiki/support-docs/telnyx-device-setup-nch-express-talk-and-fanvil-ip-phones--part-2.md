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

*Part 2 of 7 — see also: [Part 1](telnyx-device-setup-nch-express-talk-and-fanvil-ip-phones--part-1.md), [Part 3](telnyx-device-setup-nch-express-talk-and-fanvil-ip-phones--part-3.md), [Part 4](telnyx-device-setup-nch-express-talk-and-fanvil-ip-phones--part-4.md), [Part 5](telnyx-device-setup-nch-express-talk-and-fanvil-ip-phones--part-5.md), [Part 6](telnyx-device-setup-nch-express-talk-and-fanvil-ip-phones--part-6.md), [Part 7](telnyx-device-setup-nch-express-talk-and-fanvil-ip-phones--part-7.md)*

Consolidated Telnyx setup guides for the NCH Express Talk softphone and several Fanvil IP phone families (X4G, X2C/X2P/X2CP, X7/X7C/X7A, V67/V65/V64/V62, X-series, and XU series), covering product overviews, prerequisites, SIP trunk configuration, codec selection, and optional TLS certificate setup.

## Fanvil X2CP / X2C / X2P (Call Center IP)

The [Fanvil X2CP call center IP phone](https://www.fanvil.com/Product/info/id/96.html) offers an intuitive, clean design and rich features at a cost-effective price. The backlit high-resolution display allows users to access key information at a glance. Effective call monitoring, LED function keys for mute/hold/auto answering/headset, and a foot pedal switch improve the productivity of call center staff. PoE is integrated and rich extension functions of call center headset support, EHS wireless headset support provides more convenience.

**X2CP features:** 2 lines, HD voice, EHS, Supervision, LED button, Pedal switch.

The [Fanvil X2P/X2C call center IP phone](https://www.fanvil.com/Product/info/id/64.html) offers a high cost/performance ratio and provides a unique foot pedal answer option. It has a 2.8 inch 320x240 color LCD, dual 10/100 Mbps network ports with integrated PoE, ideal for extended network use. The X2P supports 2 lines plus SRTP/HTTPS/TLS, VLAN and QoS. It includes RJ9 and 3.5mm ports and EHS headset use and supervision.

**X2P/X2C features:** Color screen, HD voice, EHS, Supervision, LED button, Pedal switch.

**Pre-requisites:**

- Ensure that your Telnyx Mission Command Portal is configured properly
- Recommended: Enable TLS to encrypt your traffic
- Make sure your phone is running the latest firmware
- Make sure you can log into the web GUI (refer to the Web Portal section of your phone's user manual)

### Configure a line with a Telnyx SIP trunk

1. Log into your web GUI and navigate to **Line > SIP**.
2. Use the **Line** dropdown to select a SIP line to configure.
3. In the **Basic Settings** section, provide the following:
   1. **Username:** The SIP connection username (see the Credentials Connection Setup section of SIP connection types).
   2. **Display Name:** Your caller ID. Follow these naming conventions:
      1. Caller ID Name should be in capital letters for clearer display on some devices.
      2. Do not use special characters (they will not be displayed). Spaces are allowed.
      3. Some Canadian providers will not show more than 15 characters — consider shortening your caller ID.
   3. **Authentication Name:** The SIP connection username.
   4. **Authentication Password:** The SIP connection password.
   5. **SIP Proxy Server Address:** `sip.telnyx.com` (for international, see the [signaling addresses document](https://sip.telnyx.com/#signaling-addresses)). This also serves as the outbound proxy server address and the backup proxy server address.
   6. **SIP Proxy Server Port:** `5060` for TCP/UDP transport, `5061` for TLS transport.
   7. **Outbound Proxy Address:** `sip.telnyx.com` (for international, see the [signaling addresses document](https://sip.telnyx.com/#signaling-addresses)).
   8. **Outbound Proxy Port:** `5060` for TCP/UDP transport, `5061` for TLS transport.
   9. **Realm:** Enter the name of the realm to which the SIP interface is connected.

### Configure voice and video

1. In the **Codecs Settings** section, set the priority and availability of audio and video codecs by adding or removing them from the list. Telnyx supports the following codecs:

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

- Firmware: [X2CP](https://www.fanvil.com/Support/download/id/96.html), [X2C/X2P](https://www.fanvil.com/Support/download/id/64.html)
- User manuals: [X2CP](https://www.fanvil.com/Uploads/Temp/download/20200109/5e16c3554c22d.pdf), [X2C/X2P](https://www.fanvil.com/Uploads/Temp/download/20200109/5e16c31bac331.pdf)
- [Fanvil FAQ](https://www.fanvil.com/Support/index.html)
- [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html)
- [Fanvil support](https://www.fanvil.com/Support/ticket.html)
