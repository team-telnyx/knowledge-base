---
title: Configuring Softphones and Devices with Telnyx
summary: A comprehensive guide to configuring a wide range of SIP softphones, team
  communication platforms, and hardware devices with Telnyx using credentials-based
  connections, covering common settings such as SIP domain, codecs, caller ID conventions,
  TLS/SRTP encryption, and device-specific setup steps.
sources:
- url: https://support.telnyx.com/en/articles/1130645-configuring-bria-solo-a-k-a-x-lite
- url: https://support.telnyx.com/en/articles/1130674-configuring-linphone-with-telnyx
- url: https://support.telnyx.com/en/articles/5717957-zoiper-5-pro-telnyx-setup
- url: https://support.telnyx.com/en/articles/5720999-zoiper-3-telnyx-setup-mac
- url: https://support.telnyx.com/en/articles/5721766-zoiper-3-telnyx-setup-linux
- url: https://support.telnyx.com/en/articles/5761112-acrobits-softphone
- url: https://support.telnyx.com/en/articles/5772825-counterpath-bria-teams-setup
- url: https://support.telnyx.com/en/articles/5807979-konftel-300wx-telnyx-setup
- url: https://support.telnyx.com/en/articles/5820183-plantronics-polycom-obi300-setup
- url: https://support.telnyx.com/en/articles/6133145-microsip-setup-with-telnyx
- url: https://support.telnyx.com/en/articles/6133517-zoiper-communicator
- url: https://support.telnyx.com/en/articles/6184748-grandstream-wave-lite-iphone
- url: https://support.telnyx.com/en/articles/6184897-grandstream-wave-lite-android
- url: https://support.telnyx.com/en/articles/6187273-grandstream-gds3710-wave-lite-android
- url: https://support.telnyx.com/en/articles/6187411-grandstream-gds3710-wave-lite-ios
- url: https://support.telnyx.com/en/articles/6187576-grandstream-gxv3370
updated_at: 2026-06-11T11:29:23Z
---

# Configuring Softphones and Devices with Telnyx

*Part 3 of 3 — see also: [Part 1](configuring-softphones-and-devices-with-telnyx--part-1.md), [Part 2](configuring-softphones-and-devices-with-telnyx--part-2.md)*

A comprehensive guide to configuring a wide range of SIP softphones, team communication platforms, and hardware devices with Telnyx using credentials-based connections, covering common settings such as SIP domain, codecs, caller ID conventions, TLS/SRTP encryption, and device-specific setup steps.

## Team Communication and Hardware Device Configuration

### CounterPath Bria Teams

Bria Teams is a team-communication solution with voice, messaging, presence, and screen sharing, manageable from a central dashboard.

**Link Bria Portal with Telnyx:**

1. In the Bria Portal, go to **Voice and Video** and click **Add Voice Configuration** (or the + icon).
2. Click **Configure SIP Settings** (Telnyx is not in the pre-configured list).
3. Fill in the **New Voice Configuration**:
   - **Service Label:** A label of your choice.
   - **Domain:** `sip.telnyx.com`
   - **Port:** 5060
   - **Register with domain and receive calls:** Checked
   - **Transport:** Automatic
   - **Keep Alive:** Enabled
   - **Voicemail Number:** `*97`
   - **Service Options — requires authorization username:** Checked
   - **Firewall Method:** STUN (optional)
   - **Firewall Server URL:** `stun.telnyx.com:3478`
4. Click **Save and Close**.

**Optional — Security and encryption:**

Edit the voice configuration and change:
- **Port:** 5061
- **Transport:** TLS
- **SRTP:** Enabled
- **Register with Domain and Receive Calls:** Checked

**Audio and video codecs:**

Go to **Settings and Preferences > Configure Codecs** and prioritize Telnyx-supported codecs.

**Link a team member to a SIP profile:**

1. Go to **Team Members** and add a new member by email.
2. Click the phone icon to assign a SIP profile:
   - **Voice Service:** Select the Telnyx voice service.
   - **SIP Username/Call Extension:** Team member's Telnyx username.
   - **SIP/Voice Password:** Team member's Telnyx password.
   - **Call Display:** Outbound caller ID name (see Caller ID Conventions).

For vendor documentation, see the [Bria Portal user docs](https://docs.counterpath.com/docs/PortalUG/Resources/TitlePages/TeamsTitlePage.htm) and [Counterpath support](https://support.counterpath.com/hc/en-us).

### Konftel 300Wx

The Konftel 300Wx is a wireless DECT conference phone with a web-based configuration portal.

1. **Obtain the device IP:** On the device, go to **Status > Network** and note the IP address. Open `http://<IP>` in a browser; default login is admin/admin.
2. **Add a SIP server:** Go to **Server > Add Server**:
   - **Server Alias:** Your choice.
   - **NAT Adaption:** Enabled
   - **Registrar:** `sip.telnyx.com`
   - **Outbound Proxy:** `sip.telnyx.com`
   - **Reregistration Time (s):** 300
   - **SIP Transport:** TCP
   - **Keep Alive:** Enabled
   - **Codec Priority:** Telnyx-supported codecs in your preferred order.
   - **Secure RTP / Secure RTP Auth:** Enabled (if using TLS)
3. **Add an extension:** Go to **Extensions > Add Extension**:
   - **Extension:** Your Telnyx DID.
   - **Authentication Username / Password:** Your Telnyx SIP credentials.
   - **Server:** Select the server created above.
4. **Verify registration:** Under **Extensions**, the State should read **SIP Registered**.

For vendor documentation, see [Konftel support](https://www.konftel.com/en/support).

### Poly OBi300

The Poly OBi300 is a VoIP adapter that connects an analog phone or fax machine to up to four VoIP services.

1. **Get the IP address:** Dial `***` on the connected phone and press 1. Open `http://<IP>` in a browser; default login is admin/admin.
2. **Disable auto-provisioning:** Under **System Management > Auto Provisioning**, disable Auto Firmware Update, ITSP Provisioning, and OBiTALK Provisioning. Under **Voice Services > OBiTALK Service**, uncheck Enable.
3. **Configure the ITSP profile:** Under **Service Providers > [Profile] > General**:
   - **Name:** Your Telnyx account ID.
   - **DigitMap:** Replace the "555" placeholder digits with your area code.
4. **Configure the SIP profile:** Under **Service Providers > [Profile] > SIP**:
   - **AuthUserName:** Your Telnyx account ID.
   - **AuthPassword:** Your Telnyx password.
   - **ProxyServerPort / RegistrarServerPort / OutboundProxyPort:** 5060 (unencrypted) or 5061 (TLS).
   - **ProxyServerTransport / X_OutboundProxyTransport:** UDP/TCP (unencrypted) or TLS/TCP (encrypted).
   - **RegisterExpires:** 300
   - If using TLS, under **Voice Services**: set **X_KeepAliveServerPort** to 5061 and **X_SRTP** to **Use SRTP Only**.
5. **Configure codecs:** Expand **Codecs** and set Telnyx-supported codecs in priority order.

For vendor support, see [Poly support](https://support.hp.com/us-en/poly).

### Grandstream GXV3370

The GXV3370 is an Android-based IP video phone with a 7-inch touchscreen.

1. Log into the web GUI and navigate to **Account > General Settings > On Register**:
   - **Account Active:** Yes
   - **Account Name:** e.g., "TelnyxTrunk"
   - **SIP Server:** `sip.telnyx.com`
   - **SIP User ID / SIP Authentication ID:** Your SIP connection username.
   - **SIP Password:** Your SIP connection password.
   - **Display Name:** Your caller ID (see Caller ID Conventions).
   - **VoiceMail Access Number:** `*97`
   - **Outbound Proxy:** `sip.telnyx.com`
2. Under **Account > SIP Settings > SIP Basic Settings**:
   - **SIP registration:** Enabled
   - **SIP transport:** UDP (default) or TLS/TCP (if encrypting).
   - **Local SIP port:** 5060 (UDP) or 5061 (TLS/TCP).
3. Under **Account > Codec Settings**:
   - **Preferred Vocoder:** Select Telnyx-supported audio codecs.
   - **DTMF:** RFC2833
   - **Preferred Video Codec:** H264

For vendor documentation, see the [GXV3370 administration guide](https://documentation.grandstream.com/knowledge-base/gxv3370-administration-guide/).

### Grandstream GDS3710 with Wave Lite

The GDS3710 is a video door system that streams calls to a mobile device via Wave Lite (iOS or Android).

**Configure the GDS3710:**

Log into the GDS3710 web GUI and go to **SIP Settings > SIP Basic Settings**:
- **Account Name:** e.g., "Doorbell"
- **SIP Server:** `sip.telnyx.com`
- **SIP User ID / Authenticate ID:** Your SIP connection username.
- **Authenticate Password:** Your SIP connection password.

**Configure Wave Lite on your mobile device:**

Follow the same Wave Lite setup described in the [Grandstream Wave Lite](#grandstream-wave-lite-ios-and-android) section above, using a second set of Telnyx SIP credentials for the mobile app account.

Ensure the GDS3710 is on firmware 1.0.1.19+ and Wave Lite is on version 1.0.2.16+.

For vendor documentation, see the [GDS3710 user manual (PDF)](https://www.grandstream.com/hubfs/Product_Documentation/GDS3710_UserManual.pdf) and [Wave Lite user manual](https://documentation.grandstream.com/knowledge-base/wave-lite-android-user-manual/).

## Troubleshooting

Common issues and resolutions across all softphones and devices:

- **Registration failure:** Verify the SIP server hostname is `sip.telnyx.com` (check spelling), confirm your username and password are correct, and ensure no firewall is blocking SIP traffic.
- **403 error on outbound calls:** Usually caused by an invalid or missing caller ID. Verify your caller ID is a Telnyx number or a verified number, and that it is correctly formatted. If the softphone does not pass the caller ID in the required header, set a **caller ID override** in the outbound settings of your SIP connection in the Telnyx Portal.
- **Error 488 (Not Acceptable Here):** If you have enabled Encrypted SIP Traffic on the Portal but your device is sending unencrypted UDP/TCP or plain RTP, the call will be rejected. Ensure your device's transport and media encryption settings match the Portal configuration.
- **One-way audio or no audio:** Check codec compatibility (use Telnyx-supported codecs), verify NAT/firewall settings, and consider configuring the STUN server (`stun.telnyx.com:3478`).
- **Zoiper offline activation:** If a firewall blocks online activation, use the offline method and email the generated certificate to the Zoiper registration address.
