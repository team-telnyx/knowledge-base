---
title: Configuring Softphones and Devices with Telnyx
summary: A comprehensive guide to configuring a wide range of SIP softphones, team
  communication platforms, and hardware devices with Telnyx using credentials-based
  connections, covering common settings such as SIP domain, codecs, caller ID conventions,
  TLS/SRTP encryption, and device-specific setup steps.
sources:
- url: https://support.telnyx.com/en/articles/1130645-configuring-bria-solo-a-k-a-x-lite
  content_hash: 715c1767298dfd34f9de4aa7ccdc1fbbe3dff961c57a8c2026be07019deb4500
- url: https://support.telnyx.com/en/articles/1130674-configuring-linphone-with-telnyx
  content_hash: 94fa539b1fe2e4fa024745fa69ce40c63aa9053dbf037eecf031c128dc910ad0
- url: https://support.telnyx.com/en/articles/5717957-zoiper-5-pro-telnyx-setup
  content_hash: 09a46469b9366387ac4f7c53cdd9e92e47ad725ad980278285990b2d734636ac
- url: https://support.telnyx.com/en/articles/5720999-zoiper-3-telnyx-setup-mac
  content_hash: 07dff517a144626edb69478b062d07420323a364698a3eb2919754027bccfcc3
- url: https://support.telnyx.com/en/articles/5721766-zoiper-3-telnyx-setup-linux
  content_hash: 7edc2fa7abdd67cbd99f66ce6518e05e39e6a6b611ba5ea081dea2a144b37289
- url: https://support.telnyx.com/en/articles/5761112-acrobits-softphone
  content_hash: f2b2bbfaa9c4bb59034093ea8987a4233233c8a27cee580503ccebac41dd1e04
- url: https://support.telnyx.com/en/articles/5772825-counterpath-bria-teams-setup
  content_hash: 1687b49e78afc40ff34dfdbe8a54d89392c56be38d593126f732d13a938d005b
- url: https://support.telnyx.com/en/articles/5807979-konftel-300wx-telnyx-setup
  content_hash: ee9ad29b8d22624f13d9b9f8f41b4844ed0e1939a28a580f423d301e8a491a19
- url: https://support.telnyx.com/en/articles/5820183-plantronics-polycom-obi300-setup
  content_hash: 8ef74aceb7307a50d29f1d76291860422a5cb6d66121780f96ca1d64b24f2c2a
- url: https://support.telnyx.com/en/articles/6133145-microsip-setup-with-telnyx
  content_hash: 099c5f4bb532847138f710b1c676a9a24220a3d646540dfb1e8877d37d5ac5fd
- url: https://support.telnyx.com/en/articles/6133517-zoiper-communicator
  content_hash: d94de24a45beed31c1e5581dc3e5bad3e4b06195ffef6662f1ed2ce2f1170926
- url: https://support.telnyx.com/en/articles/6184748-grandstream-wave-lite-iphone
  content_hash: a585bed323d8201aa893f33e7394bd4c259483f5da8293f214486b62115d774e
- url: https://support.telnyx.com/en/articles/6184897-grandstream-wave-lite-android
  content_hash: c262c545cbf2f68d9663820d17994869b4607951a92f4287ba7edd3e9d396138
- url: https://support.telnyx.com/en/articles/6187273-grandstream-gds3710-wave-lite-android
  content_hash: d992630ed2dddf042bb062e72b4bfcac9b30c54ed2a8b1717a8a3320130e04c1
- url: https://support.telnyx.com/en/articles/6187411-grandstream-gds3710-wave-lite-ios
  content_hash: ed7c59987079659094e333f8345c6eff7710460dade2309723b7a10c8a957b32
- url: https://support.telnyx.com/en/articles/6187576-grandstream-gxv3370
  content_hash: f75a754a6be7b66b4e892021cab6bf25785af6a4ab92b7982205bb1a2d62ab26
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
