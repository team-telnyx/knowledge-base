---
title: SIP Phone and Device Configuration with Telnyx
summary: A consolidated guide for configuring SIP endpoints from multiple manufacturers—including
  Algo, Panasonic, FortiFone, Flyingvoice, Fanvil, Positron, Gigaset, Snom, AudioCodes,
  Konftel, Vtech, Mitel, Alcatel, and BuddyTalk—to register with Telnyx's SIP infrastructure.
  Covers common prerequisites, the shared SIP parameter set, device-specific web portal
  navigation, TLS/SRTP encryption, codec selection, and troubleshooting.
sources:
- url: https://support.telnyx.com/en/articles/5790092-algo-8xxx-telnyx-endpoints
- url: https://support.telnyx.com/en/articles/5807663-panasonic-kx-tgp-550
- url: https://support.telnyx.com/en/articles/5808185-buddytalk-bt110-bt120
- url: https://support.telnyx.com/en/articles/5810226-fortifone-fon-570
- url: https://support.telnyx.com/en/articles/5810663-flyingvoice-telnyx-setup
- url: https://support.telnyx.com/en/articles/5811487-fanvil-x4g-telnyx-setup
- url: https://support.telnyx.com/en/articles/5811545-fortifone-setup-fon-375-175-h25
- url: https://support.telnyx.com/en/articles/5811761-positron-ip-phone
- url: https://support.telnyx.com/en/articles/5814406-panasonic-kx-hdv-telnyx-setup
- url: https://support.telnyx.com/en/articles/5815209-gigaset-a510-telnyx-setup
- url: https://support.telnyx.com/en/articles/5815678-snom-c520-telnyx-setup
- url: https://support.telnyx.com/en/articles/5819923-audiocodes-400hd
- url: https://support.telnyx.com/en/articles/5822579-konftel-300ipx-telnyx-setup
- url: https://support.telnyx.com/en/articles/5822706-snom-d7xx-telnyx-setup
- url: https://support.telnyx.com/en/articles/5822823-snom-m100-kle-telnyx-setup
- url: https://support.telnyx.com/en/articles/5822901-vtech-vcs754-telnyx-setup
- url: https://support.telnyx.com/en/articles/6060646-gigaset-a690-as690
- url: https://support.telnyx.com/en/articles/6244551-mitel-5320e-5330e-5340e-sip
- url: https://support.telnyx.com/en/articles/6249691-mitel-6800-6900-sip
- url: https://support.telnyx.com/en/articles/6281943-alcatel-sd601-sd602-sip-door
updated_at: 2026-06-11T11:33:51Z
---

# SIP Phone and Device Configuration with Telnyx

*Part 2 of 3 — see also: [Part 1](sip-phone-and-device-configuration-with-telnyx--part-1.md), [Part 3](sip-phone-and-device-configuration-with-telnyx--part-3.md)*

A consolidated guide for configuring SIP endpoints from multiple manufacturers—including Algo, Panasonic, FortiFone, Flyingvoice, Fanvil, Positron, Gigaset, Snom, AudioCodes, Konftel, Vtech, Mitel, Alcatel, and BuddyTalk—to register with Telnyx's SIP infrastructure. Covers common prerequisites, the shared SIP parameter set, device-specific web portal navigation, TLS/SRTP encryption, codec selection, and troubleshooting.

## Device-Specific Configuration

### Algo 8xxx

1. In the web portal, go to **Basic Settings → SIP**.
2. Set **SIP Domain (Proxy Server)** to `sip.telnyx.com`.
3. Enter your **Base/Page Extension**, **Authentication ID**, and **Authentication Password** with your Telnyx SIP credentials.
4. Set **Display Name** to your outbound Caller ID.
5. Each additional extension (ringing, paging, emergency alerting) requires unique SIP credentials.
6. To enable G.722, go to **Basic Settings → Features** and enable **G-722 Support** in the Inbound Page Settings section.

### Panasonic KX-TGP 550

1. Register handsets: dock the handset, **Menu → Initial Settings → Registration → Register Handset**, then hold the **ALL** button on the base for 4 seconds and press **OK**.
2. Enable the embedded web portal: **Menu → IP Service → Network Setting → Embedded Web → On**.
3. In the web portal **VoIP** tab, set **Registrar Server Address** and **Proxy Server Address** to `sip.telnyx.com`, port `5060`.
4. Enter **Line ID**, **Authentication ID**, and **Authentication Password** with your Telnyx credentials.
5. Set **Service Domain** to `sip.telnyx.com` and **Keep Alive Interval** to approximately 15.

### Panasonic KX-HDV (130/230/330)

1. In the web portal, go to **VoIP → SIP Settings → Line 1**.
2. Set **Registrar Server Address**, **Proxy Server Address**, **Presence Server Address**, **Outbound Proxy Server Address** all to `sip.telnyx.com` with the appropriate port.
3. Set **Service Domain** to `sip.telnyx.com`.
4. Enter **Authentication ID** and **Authentication Password**.
5. In the **Advanced** section, set **REGISTER Expires Timer** to `300`, **Transport Protocol** to UDP or TLS, and **TLS Mode** to `SIP-TLS` (if using TLS).
6. For TLS, also configure **VoIP Settings → Line 1 → Advanced → SRTP Mode** to `SRTP`.
7. Configure codecs under **VoIP → VoIP Settings → Line 1**.

### BuddyTalk BT110/BT120

1. Use the BuddyTalk Setup App (Android or iOS).
2. On the **Setup Telephony** screen, enter your **Account ID**, **Auth ID**, and **Password** from Telnyx.
3. Set **Domain** to `sip.telnyx.com`, enable **Outbound Proxy** and set to `sip.telnyx.com`.
4. Set **Local SIP Port** to `5060` and **Preferred Transport** to `UDP` (or `TLS` if encrypting).
5. After registration, the phone icon turns green and the device LED transitions from red to green to off.
6. To enable TLS: log into the [BuddyTalk Web Console](https://www.innomedia.com/buddytalk-product-family/), go to **Telephony → Profile Config**, set **Preferred Transport Protocol** to `TLS`. Then go to **Port Config**, edit the profile, and set **Secure RTP** to `SDES`.

### FortiFone FON-570

1. In the web portal, go to **Account → Register**.
2. Set **Line Active** to Enabled, enter a **Label**, and set **Display Name** (Caller ID).
3. Enter **Register Name**, **User Name**, and **Password** with your Telnyx credentials.
4. Set **Server Host** to `sip.telnyx.com` and **Port** to `5060` (UDP) or `5061` (TLS).
5. Set **Transport** to `UDP` or `TLS` as appropriate.
6. Set **Server Expires** to `300`.
7. For TLS: go to **Advanced** and set **RTP Encryption (SRTP)** to `Compulsory`.
8. Configure date/time under **Settings → Date and Time**.

### FortiFone FON-375/175/H25

1. In the web portal, go to **Line → SIP**.
2. Enter **Username**, **Display Name**, **Authentication Name**, and **Authentication Password**.
3. Set **Server Name** and **Register Address** to `sip.telnyx.com` with the appropriate port.
4. Check **Activate**.
5. In the **Advanced** section, set **Transportation Protocol** to `UDP` or `TLS`.
6. For TLS: set **Transportation Protocol** to `TCP` and check **RTP Encryption**.

### Flyingvoice

1. In the web portal, go to **SIP Account → Line 1**.
2. Set **Line Enable** to Enable, enter **Display Name** (Caller ID), **Phone Number**, **Account**, and **Password**.
3. Set **Proxy Server** to `sip.telnyx.com` with the appropriate port.
4. Set **Transport** to `UDP` or `TLS`.
5. Set **Voice Mailbox Numbers** to `*97`, **Register Refresh Interval** to `180`, and **RTP Port** range as needed.
6. Optionally configure line keys under **Phone → Line Key**.
7. You can also configure directly on the phone: **Menu → Advanced → Accounts → Line 1**.

### Fanvil X4G

1. In the web portal, go to **Lines → SIP**.
2. Enter **Username**, **Display Name**, **Authentication Name**, and **Authentication Password**.
3. Set **Server Name**, **Register Address**, **Proxy Server Address**, and **Backup Proxy Server Address** to `sip.telnyx.com` with the appropriate ports.
4. Check **Activate**.
5. Click **Apply** and refresh the page to verify registration.

### Positron IP Phone (IP304/IP408/IP410)

Configuration can be done via the web portal or directly on the phone.

**Web portal:** Go to **Account → Basic**, set **Primary SIP Server** to `sip.telnyx.com`, **SIP Transport** to UDP or TLS, and enter **SIP User ID**, **Authentication ID**, and **Authentication Password**. Click **Save**.

**Phone:** Go to **Menu → Settings → Advanced Settings → Accounts**, enter the same parameters and set **Account Active** to On.

To import a TLS certificate: **Management → TLS Certs**.

**Recommended:** Change the default admin password via **Menu → Settings → Advanced Settings → Password → Phone Settings → Set Password**.

### Gigaset A510 IP

1. In the web portal, go to **Settings → Telephony → Connections** and click **Edit** next to the line to configure.
2. Enter **Authentication Name**, **Authentication Password**, **Username**, **Display Name**.
3. Set **Domain**, **Proxy Server Address**, **Registration Server**, and **Outbound Server Address** all to `sip.telnyx.com` with appropriate ports.
4. Set **Registration Refresh Time** to `300`, **STUN Enabled** to `No`, **Outbound Proxy Mode** to `Always`.
5. Set **Select Network Protocol** to `UDP` or `TLS`.
6. Under **Number Assignment**, check the line for both outgoing and incoming calls.

### Gigaset A690/AS690 IP

1. Ensure the device is running the latest firmware (manual check: **Menu → Settings → System → Base Update**; default PIN `0000`).
2. Optionally enable automatic firmware updates: **Menu → Settings → Firmware Update → Automatic Check**.
3. Access the web portal (press the paging button on the base to display the IP; default PIN `0000`).
4. Use the **Quick Start Wizard** on the **Home** tab, selecting **Other Provider** if Telnyx is not listed.
5. Configure telephony settings identically to the A510 (see above).

### Snom C520

1. In the web portal, go to **System → SIP Account Management** and select the account.
2. In **General**: set **Account Label**, **Display Name** (Caller ID), **User Identifier**, **Authentication Name**, and **Authentication Password**.
3. In **SIP Server**: set **Server Address** to `sip.telnyx.com` with the appropriate port.
4. In **Registration**: set **Server Address** to `sip.telnyx.com`, **Expiration** to `300`, **Registration Freq** to `10`.
5. In **Outbound Proxy**: set **Server Address** to `sip.telnyx.com` with the appropriate port.
6. For TLS: fill in **Backup Outbound Proxy** with `sip.telnyx.com:5061`.
7. In **Audio**: set codec priority. In **Signaling Settings**: set **Local SIP Port** and **Transport** appropriately.

### Snom D7xx (D120/D717/D735/D785)

1. In the web portal, click **Identity 1**.
2. On the **Login** tab: set **Displayname** (Caller ID), **Account** (Telnyx ID), **Password**, **Registrar** (`sip.telnyx.com` or `sip.telnyx.com:5061` for TLS), **Outbound Proxy** (same as Registrar), **Authentication Username**, and **Mailbox** (`*97`).
3. On the **SIP** tab: set **Dial-Plan String** to `^.$`, **Proposed Expiry** to `300`, **Subscription Expiry** to `300`.
4. Configure codecs in RTP Identity Settings. For TLS: set **RTP Encryption** to `on` and **RTP/SAVP** to `Mandatory`.

### Snom M100 KLE

1. In the web portal, go to **System** tab.
2. In **General Account Settings**: enter **User Identifier** and **Authentication Name** (your SIP account username) and **Authentication Password**.
3. In **SIP Server**: set **Server Address** to `sip.telnyx.com` with the appropriate port.
4. In **Registration**: set **Server Address** to `sip.telnyx.com` with the appropriate port.
5. Check the **Status** tab to confirm registration shows as *Registered*.

### AudioCodes 400HD

1. In the web portal, go to **Configuration → Quick Setup**.
2. In **SIP Proxy and Registrar**: enable **Use SIP Proxy**, set **Proxy IP Address** to `sip.telnyx.com`, port `5060` (or `5061` for TLS), enable **Use SIP Proxy IP and Port for Registration**, disable **Use SIP Registrar**.
3. In **Line Settings**: set **Line Number** to 1, enable the line, enter **Display Name**, **User ID**, **Authentication User Name**, and **Authentication Password**.
4. For TLS: go to **Voice Over IP → Signaling Protocols**, set **SIP Transport Protocol** to `TLS`, **TLS Port** to `5061`, **SIP Local Port** to `5081`. Then go to **Voice Over IP → Media Streaming** and set **SRTP Encryption and Authentication** to `REQUIRE ENCRYPTION`, **Method** to `AES_CM_128_ALL_METHODS`, **Negotiation Mode** to `Basic`.
5. Configure NAT keep-alive: **Voice Over IP → Signaling Protocols**: enable **Registrar Keep Alive** with period `50` seconds, **Registration Expires** `300` seconds.
6. Configure codecs under **Voice Over IP → Media Streaming**.

### Konftel 300IPx

1. In the web portal, go to **Settings → SIP** and click **Edit** on the profile.
2. In **Account 1**: enable the account, enter **User** (Telnyx ID), **Registrar** (`sip.telnyx.com`), **Proxy** (blank or `sip.telnyx.com`), enable **Keep Alive**, enter **Authentication Name** and **Password**, set **Registration Interval** to `300`.
3. In **Transport**: set **Protocol** to UDP/TCP or TLS, **Local Port** to `5060` or `5061`.
4. Verify status under **Status → SIP**.

### Vtech VCS754

1. In the web portal, go to **System** tab and select the account.
2. In **General Account Settings**: set **Account Label**, **Display Name** (Caller ID), **User Identifier**, **Authentication Name**, **Authentication Password**, and **Dial Plan** (`x+P`).
3. In **SIP Server**: set **Server Address** to `sip.telnyx.com` with the appropriate port.
4. Copy the same values into **Registration**, **Outbound Proxy**, and **Backup Outbound Proxy** sections.
5. In **Audio**: set codec priority. Check **Enable Voice Encryption (SRTP)** if using TLS.
6. In **Signaling Settings**: set **Local SIP Port** and **Transport** appropriately.

### Mitel 5320E/5330E/5340E

1. Access the Web Configuration Tool (see IP address method in the table above).
2. Go to **Admin Tools → User List Config**.
3. Enter **User ID or Extension**, **User Display Name**, **SIP Authentication User Name**, **SIP Authentication Password**.
4. Set **Line Type** to `SIP`.
5. Set **SIP Proxy Server**, **SIP Registry Server**, and **SIP Outbound Server** all to `sip.telnyx.com` with the appropriate port and scheme (UDP/TCP/TLS).

### Mitel 6800/6900

Configuration can be done via the Mitel Web UI, the IP Phone UI, or configuration files (`startup.cfg`, `<model>.cfg`, or `<mac>.cfg`).

**Web UI:** Go to **Advanced Settings → Global SIP** for global parameters or **Advanced Settings → <Line>** for per-line parameters.

Key parameters (web UI name → config file parameter):

- **Screen Name** → `sip screen name`: Your Telnyx username
- **Phone Number** → `sip user name`: Your Telnyx username
- **Caller ID** → `sip display name`: Your Caller ID
- **Authentication Name** → `sip auth name`: Your Telnyx username
- **Password** → `sip password`: Your Telnyx password
- **Proxy Server** → `sip proxy ip`: `sip.telnyx.com`
- **Proxy Port** → `sip proxy port`: `5060` or `5061`
- **Outbound Proxy Server** → `sip outbound proxy`: `sip.telnyx.com`
- **Backup Outbound Proxy** → `sip backup outbound proxy`: `sip.telnyx.com`

For per-line parameters, prefix with `sip lineN` (e.g., `sip lineN user name`).

For TLS configuration, specify **Transport Protocol** as `TLS`, upload Root/Intermediate Certificates, Local Certificate, Private Key, and Trusted Certificate files. See [TLS and SRTP](https://support.telnyx.com/en/articles/4404575-tls-and-srtp) for certificate details and the Mitel Administrator Manual for device requirements.

### Alcatel SD601/SD602

1. Power on the door phone and hold `#` for 3 seconds to hear the IP address.
2. Access the web portal (default credentials: admin/admin).
3. Go to **SYSTEM → SIP Accounts**.
4. Enter **Phone Number** (your Telnyx DID), **Display Name**, **Authentication Name**, **Authentication Password**.
5. Set **SIP Proxy Server Address** to `sip.telnyx.com` and **SIP Proxy Server Port** to `5060`.
6. Check **Activate**.
