---
title: Telnyx Voice API, TeXML, and Device Setup Guide
summary: A consolidated reference covering Telnyx account basics, Voice API and TeXML
  application configuration, debugging tools, conference calling, and step-by-step
  setup instructions for several SIP desk and conference phones.
sources:
- url: https://support.telnyx.com/en/articles/1130644-do-i-have-to-sign-a-contract
- url: https://support.telnyx.com/en/articles/1130677-does-telnyx-support-conference-calls
- url: https://support.telnyx.com/en/articles/13386198-texml-bin-simple-voicemail-and-call-forwarding
- url: https://support.telnyx.com/en/articles/4304872-telnyx-debugging-tools
- url: https://support.telnyx.com/en/articles/4374050-configuring-call-control-texml-applications-voice-api
- url: https://support.telnyx.com/en/articles/5807663-panasonic-kx-tgp-550
- url: https://support.telnyx.com/en/articles/5807979-konftel-300wx-telnyx-setup
- url: https://support.telnyx.com/en/articles/5814406-panasonic-kx-hdv-telnyx-setup
- url: https://support.telnyx.com/en/articles/5822579-konftel-300ipx-telnyx-setup
- url: https://support.telnyx.com/en/articles/8118086-texml-and-telnyx-voice-api-compatibility
- url: https://support.telnyx.com/en/collections/133140-voice-api-essentials
- url: https://support.telnyx.com/en/collections/17907095-texml-tutorials
updated_at: 2026-08-05T13:29:28Z
---

# Telnyx Voice API, TeXML, and Device Setup Guide

*Part 3 of 3 — see also: [Part 1](telnyx-voice-api-texml-and-device-setup-guide--part-1.md), [Part 2](telnyx-voice-api-texml-and-device-setup-guide--part-2.md)*

A consolidated reference covering Telnyx account basics, Voice API and TeXML application configuration, debugging tools, conference calling, and step-by-step setup instructions for several SIP desk and conference phones.

## Device Setup

The following sections describe how to configure common SIP desk and conference phones with Telnyx. In each case, ensure your Telnyx Mission Control Portal is configured and you have provisioned a DID from Telnyx.

### Panasonic KX-TGP 550

The Panasonic KX-TGP 550 is a 2-in-1 device with a phone and cordless handset, supporting up to 3 simultaneous network conversations and up to 8 SIP registrations. This guide also covers the KX-TGP 500 and KX-TGP 551.

1. **Register your handset(s).** For each handset, dock it, press the center button, select **Menu > Initial Settings > Registration > Register Handset**, then press and hold the **ALL** button on the base for 4 seconds and press **OK** on the handset.
2. **Obtain your device's IP address.** From the handset, press the center button, select **IP Service > Network Setting > IP Setting** to view the IP address. Enable **Embedded Web** from the same menu, then enter the IP address in a browser. Default credentials: Username `admin`, Password `adminpass`.
3. **Configure your KX-TGP 550 to connect to Telnyx.** From the configuration panel, click the VoIP tab and configure:
   - **Phone number:** The DID for this device
   - **Line ID:** Your Telnyx SIP account username
   - **Registrar Server Address:** `sip.telnyx.com`
   - **Registrar Server Port:** `5060`
   - **Proxy Server Address:** `sip.telnyx.com`
   - **Proxy Server Port:** `5060`
   - **Presence Server Port:** `5060`
   - **Service domain:** `sip.telnyx.com`
   - **Source Port:** `5060`
   - **Authentication ID:** Your Telnyx SIP account username
   - **Authentication Password:** Your Telnyx SIP account password
   - **Keep Alive Interval:** ~15

If you do not see an IP address, ensure the phone is connected to the network and a DHCP server is available, then repeat the registration process.

### Konftel 300Wx

The Konftel 300Wx is a wireless DECT conference phone with more than 60 hours of call time per charge and expandable microphone capability.

1. **Obtain your device's IP address.** From the device, go to **Status > Network** and note the IP address. Open a browser and enter `http://` followed by the IP address. Default credentials: Username `admin`, Password `admin`.
2. **Add a SIP server in the Konftel web portal.** Click **Server > Add Server** and configure:
   - **Server Alias:** A name for your server
   - **NAT Adaption:** Enabled
   - **Registrar:** `sip.telnyx.com`
   - **Outbound Proxy:** `sip.telnyx.com`
   - **Reregistration Time (s):** `300`
   - **SIP Transport:** `TCP`
   - **Keep Alive:** Enabled
   - **Codec Priority:** `ulaw(g711u)`, `alaw(g711a)`, `g722`, `g729`
   - **Secure RTP / Secure RTP Auth:** Enabled (if using TLS)
3. **Add an extension.** Click **Extensions > Add Extension** and configure:
   - **Extension:** Your Telnyx DID
   - **Authentication Username:** Your Telnyx SIP username
   - **Authentication Password:** Your Telnyx SIP password
   - **Server:** The server created in step 2
   - Select the device to use for this extension.
4. **Verify that your server is running.** Under **Extensions**, check that the new server's **State** field shows `SIP Registered`.

### Panasonic KX-HDV

This guide applies to the KX-HDV130, KX-HDV230, and KX-HDV330. Enabling TLS to encrypt traffic is recommended.

1. **Get your device's IP address and log into the phone's web portal.** From the phone, go to **Basic Settings > Other Options > Embedded Web** and select **On**. Then go to **System Settings > Status > IPv4 Settings > IP Address** and note the IP address. Enter `http://` followed by the IP address in a browser. Default credentials: Username `admin`, Password `adminpass`.
2. **Configure your SIP profile.** Click the **VoIP** tab, then **SIP Settings > Line 1**, and enter:
   - **Phone Number:** Your Telnyx SIP main account or sub-account
   - **Registrar Server Address:** `sip.telnyx.com`
   - **Registrar Server Port:** `5060` (UDP) or `5061` (TLS)
   - **Proxy Server Address:** `sip.telnyx.com`
   - **Proxy Server Port:** `5060` (UDP) or `5061` (TLS)
   - **Presence Server Address:** `sip.telnyx.com`
   - **Presence Server Port:** `5060` (UDP) or `5061` (TLS)
   - **Outbound Proxy Server Address:** `sip.telnyx.com`
   - **Outbound Proxy Server Port:** `5060` (UDP) or `5061` (TLS)
   - **Service Domain:** `sip.telnyx.com`
   - **Authentication ID:** Your Telnyx SIP main account or sub-account
   - **Authentication Password:** Your Telnyx SIP main account or sub-account password

   In the **Advanced** section:
   - **REGISTER Expires Timer:** `300`
   - **Transport Protocol:** `UDP` by default; choose `TLS` if encryption is enabled.
   - **TLS Mode:** `SIPS` by default; choose `SIP-TLS` if encryption is enabled.

   If using TLS, go to **VoIP Settings > Line 1 > Advanced** and set **SRTP Mode** to `SRTP`.

   ![Sip settings section.](_images/530aaba9a4a97e35.png)

3. **Configure audio codecs.** Under **VoIP > VoIP Settings > Line 1**, enable the Telnyx-supported codecs (`ulaw(g711u)`, `alaw(g711a)`, `g722`, `g729`) and disable others.

   ![VoIP settings section.](_images/f38fb874bb32e75c.png)

   Verify registration under **Status > VoIP Status**.

### Konftel 300IPx

The Konftel 300IPx is an IP conference phone that pairs with the Konftel Unite app. Enabling TLS to encrypt traffic is recommended.

1. **Get your device's IP address and log into the phone's web portal.** From the phone, go to **Menu > Status > Network** and note the IP address. Enter `http://` followed by the IP address in a browser. Default credentials: Username `ADMIN`, Password `1234`.
2. **Configure a SIP extension.** Click **Settings > SIP**, then **Edit** next to the profile to configure. In the **Account 1** section, set:
   - **Enable Account:** Yes
   - **Account Name:** Display name for the account
   - **User:** Your Telnyx account ID
   - **Registrar:** `sip.telnyx.com`
   - **Proxy:** Blank or `sip.telnyx.com`
   - **Enable Keep Alive:** Yes
   - **Realm:** Blank or `sip.telnyx.com`
   - **Authentication Name:** Your Telnyx account ID
   - **Password:** Your Telnyx account password
   - **Registration Interval:** `300`

   ![Settings section.](_images/aa5b9b39e47bd4e4.png)

   In the **Transport** section:
   - **Protocol:** `UDP` or `TCP` (no TLS); `TLS` if encryption is enabled.
   - **Local port:** `5060` (no TLS); `5061` (TLS).

   ![Transport section.](_images/93fcb22c2f8aaf01.png)

3. **Verify the status of your new SIP account.** Click **Status > SIP** and confirm everything looks good.

   ![Status section.](_images/af3294d63d9b4e3e.png)

## Voice API Essentials Collections

The Voice API Essentials collection groups related articles into three sub-collections:

- **Call Control / TeXML:** Configuring Call Control/TeXML Applications, TeXML and Voice API compatibility, and Real-Time Transcription.
- **Guide to Telnyx E911 Services:** E911 setup, registering E911 addresses, and testing E911 service.
- **General Voice API Help:** UK TPS guidelines, Google Verified Calls, STIR/SHAKEN, Caller ID vs CNAM, distinguishing outbound profiles and DIDs, US local call completion, the Robocall Mitigation Database, CLI & CLD validation, and Canadian STIR/SHAKEN implementation.

The TeXML tutorials collection includes the TeXML Bin Simple Voicemail and Call Forwarding guide and the Twilio TwiML Conference on Telnyx migration guide.
