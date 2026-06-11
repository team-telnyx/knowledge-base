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
