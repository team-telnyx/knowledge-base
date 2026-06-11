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

*Part 2 of 3 — see also: [Part 1](configuring-softphones-and-devices-with-telnyx--part-1.md), [Part 3](configuring-softphones-and-devices-with-telnyx--part-3.md)*

A comprehensive guide to configuring a wide range of SIP softphones, team communication platforms, and hardware devices with Telnyx using credentials-based connections, covering common settings such as SIP domain, codecs, caller ID conventions, TLS/SRTP encryption, and device-specific setup steps.

## Softphone Client Configuration

### Bria Solo (a.k.a. X-Lite)

Bria Solo (formerly X-Lite) by CounterPath is a softphone for **Windows and Mac only**.

1. Open Bria Solo and go to **Softphone > Account Settings**.
2. Fill in the fields:
   - **Account Name:** A label of your choice.
   - **Protocol:** SIP (read-only).
   - **User ID:** Your Telnyx SIP username.
   - **Domain:** `sip.telnyx.com`
   - **Password:** Your Telnyx SIP password.
   - **Display Name:** Your caller ID name (see Caller ID Conventions above).
   - **Authorization Name:** Only fill this in if Telnyx provided a specific authorization name.
3. In the **Domain Proxy** section:
   - Check **Register with domain and receive calls** to accept inbound calls. Clear this if your service level does not include inbound.
   - **Send outbound via:** Select only if Telnyx directs traffic through a domain-discovered proxy, and fill in the IP address Telnyx provides.
4. Click **OK** to register. A successful registration is indicated in the UI.

For vendor documentation, see the [Bria Solo/X-Lite technical documentation](https://www.counterpath.com/x-lite/) and [support](https://support.counterpath.com/hc/en-us/categories/360002425273-Bria-Solo).

### Linphone

Linphone is an open-source VoIP softphone supporting audio, video, and instant messaging.

**Basic configuration:**

1. Open Linphone and click **Account Assistant**.
2. Select **Use a SIP Account**.
3. Fill in:
   - **Username:** Your Telnyx SIP auth username.
   - **Display Name:** Your caller ID (must comply with Telnyx policy; see Caller ID Conventions).
   - **SIP Domain:** `sip.telnyx.com`
   - **Password:** Your Telnyx SIP auth password.
   - **Transport:** UDP or TCP.
4. Click **Use** to register.

**Encrypted configuration (TLS/SRTP):**

Follow the basic steps above with these changes:
- **SIP Domain:** `sip.telnyx.com:5061`
- **Transport:** TLS

Then go to **Preferences > Call and Chat** and enable **SRTP**.

For vendor documentation, see the [Linphone wiki](https://wiki.linphone.org/xwiki/wiki/public/view/Linphone/) and [support](https://www.linphone.org/contact).

### Zoiper 5 Pro

Zoiper 5 is a cross-platform softphone (Windows, Mac, Linux) with companion apps for iOS and Android. The Pro license unlocks advanced features.

**Account creation:**

1. Activate your Pro license when prompted (or continue as a free user).
2. In the account creation wizard, select your country, filter providers by typing "Telnyx", and select Telnyx.
3. The wizard auto-detects protocols — click **Next** to proceed.
4. After authentication, configure sound, video, and microphone settings as needed.

**Advanced — Network settings:**

From **Account Settings > Advanced > Network Related**:
- **Registration expire mode:** Custom
- **Registration expiry:** 300
- **NAT keep alive time-out:** Custom
- **Keep alive custom interval:** 30

**Advanced — Call encryption (TLS/SRTP):**

1. Enable **Encrypted SIP Traffic** on your Telnyx SIP connection (or sub-account advanced options).
2. In **Advanced > SIP Credentials**: set Domain to `sip.telnyx.com` with your username and password.
3. In **Network Related**: set **Transport** to TLS.
4. In the **Encryption** section: set **SRTP Key Negotiation** to SDES.

A green padlock icon next to the call profile confirms the call is secured.

**Offline activation:** If you cannot reach the Zoiper server, click **Activate offline** from the login screen. Send the generated `Zoiper<ComputerName>.certificate` file to [register5@shop.zoiper.com](mailto:register5@shop.zoiper.com), then save the returned certificate in the same folder.

For the vendor user guide, see the [Zoiper 5 user guide (PDF)](https://www.zoiper.com/pdf/User%20Guide%20Zoiper%205%20v.1.0.7.pdf).

### Zoiper 3 (Mac and Linux)

Zoiper 3 is an earlier version of the cross-platform Zoiper softphone.

1. Download, install, and run Zoiper 3.
2. If you have a business license, activate it (online or offline) when prompted. For offline activation, send the generated certificate to [register4@shop.zoiper.com](mailto:register4@shop.zoiper.com).
3. Go to **Settings > Create a new account**.
4. Select **SIP** as the account type (Telnyx does not support IAX or XMPP).
5. Enter your Telnyx credentials; set **Domain/outbound proxy** to `sip.telnyx.com`.
6. Provide an account name of your choice and click **Next**. Zoiper will attempt to connect automatically.

**Troubleshooting:** If auto-configuration fails, verify the server hostname, username/password, and that no firewall is blocking access. You can select **"I know what I am doing, save this information anyway"** to save and complete configuration manually.

For vendor documentation, see the [Zoiper 3 installation and configuration manuals](https://www.zoiper.com/en/support/home/article/34/Installation_%26_configuration_manuals_Zoiper_3).

### Zoiper Communicator

Zoiper Communicator is a free IAX & SIP softphone for Windows.

1. Start Zoiper Communicator and select **Settings > Create New Account**.
2. Enter an account name and click **OK**.
3. On the **SIP Account Options** page:
   - **Domain:** `sip.telnyx.com`
   - **Username:** Your Telnyx account or sub-account username.
   - **Password:** Your Telnyx account or sub-account password.
   - **Caller ID Name:** Follow the Caller ID Conventions above.
4. Click **OK** to complete.

For vendor help, see [Zoiper support](https://www.zoiper.com/en/support/questions).

### MicroSIP

MicroSIP is an open-source, portable SIP softphone for **Windows only** with a minimal footprint.

1. Run MicroSIP, click the arrow at the top-right, and select **Edit Account**.
2. Provide:
   - **Account Name:** Your choice.
   - **SIP Server:** `sip.telnyx.com`
   - **SIP Proxy:** `sip.telnyx.com`
   - **Username / Login:** Your Telnyx SIP username.
   - **Domain:** `sip.telnyx.com`
   - **Password:** Your Telnyx SIP password.
   - **Display Name:** Your caller ID (see Caller ID Conventions).
   - **Media Encryption:** Disabled for UDP/TCP; **Mandatory SRTP (RTP/SAVP)** for TLS.
   - **Transport:** Auto (UDP/TCP) or TLS.

**Optional — Encrypt calls:**

Go to **MicroSIP > Settings** and set:
- **Source Port:** 5061
- **RTP Ports:** 10001–20000

**Audio settings:**

Go to **MicroSIP > Settings**, select Telnyx-supported codecs, and check the **EC** (echo cancellation) box.

For vendor resources, see [MicroSIP downloads](https://www.microsip.org/downloads/current) and [help](https://www.microsip.org/help).

### Acrobits Softphone / Groundwire

Acrobits Softphone and Acrobits Groundwire are SIP clients for **iOS and Android**. Note that SIP/Simple (required for SMS/MMS) is not supported by Telnyx, so Acrobits can only be used for voice calling.

1. Open the Acrobits app and tap the settings gear > **SIP Accounts** > **New SIP Account**.
2. Select Telnyx from the provider list (or add it manually if not present).
3. Enter:
   - **Title:** e.g., "Telnyx"
   - **Username:** Your Telnyx account username.
   - **Password:** Your Telnyx account password.
   - **Domain:** `sip.telnyx.com`
4. Tap **Save**.

**Optional — Caller ID display name:** In advanced settings, set a display name following the Caller ID Conventions above.

For vendor resources, see the [Acrobits official site](https://acrobits.net/).

### Grandstream Wave Lite (iOS and Android)

Wave Lite is a free softphone app for iOS (8.0+) and Android (4.0+).

1. Open Wave Lite and go to **Settings > Account Settings > Generic Account > SIP Account**. Do **not** use the VoIP Provider section.
2. Fill in:
   - **Account Name:** e.g., "TelnyxTrunk"
   - **SIP Server:** `sip.telnyx.com`
   - **SIP User ID / SIP Authentication ID:** Your SIP connection username.
   - **SIP Password:** Your SIP connection password.
   - **VoiceMail UserID:** `*97`
   - **Display Name:** Your caller ID (see Caller ID Conventions).
3. Tap the checkmark to connect.

**Call settings:**

Tap the account > **Call Settings**:
- **SIP Port:** 5060 (UDP/TCP) or 5061 (TLS).
- **Transmission Protocol:** TCP/UDP, or TLS if encrypting.

**Codec configuration:**

Tap the account > **Network Setting Parameters > Preferred Vocoder** and select Telnyx-supported codecs (see Supported Audio and Video Codecs above).

**Optional — STUN server:**

Tap the account > **Advanced Settings > General Settings**:
- **STUN Server Settings:** `stun.telnyx.com:3478`
