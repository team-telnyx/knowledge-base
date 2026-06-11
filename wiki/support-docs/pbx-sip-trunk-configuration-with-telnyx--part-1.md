---
title: PBX SIP Trunk Configuration with Telnyx
summary: Comprehensive guide for configuring FreePBX (V13–V15) and Elastix (V4–V5)
  PBX systems with Telnyx SIP trunks, covering IP-based and credentials-based authentication,
  ChanSIP and PJSIP drivers, trunk settings, dial patterns, and call routing.
sources:
- url: https://support.telnyx.com/en/articles/1130620-freepbx-trunk-settings-with-telnyx
  content_hash: d05ae939bac98cd660ab00f58760eaefb83a95abc85f43855b6b886814a3d42c
- url: https://support.telnyx.com/en/articles/1130622-configuring-an-elastix-4-pbx-ip-trunk
  content_hash: ad092ba4bc22ac53effad563b3946c8a4a7e2ddd8ca37297b5851363fc6ef05a
- url: https://support.telnyx.com/en/articles/1130648-configuring-a-freepbx-v13-credentials-trunk
  content_hash: 4a974423f69e2e328abd9bba5d548cf03d44c6ca0a93cd6930ec37c2e5cb793e
- url: https://support.telnyx.com/en/articles/1130654-configuring-an-elastix-4-pbx-trunk
  content_hash: 28b430d0c2f291395e77f38540343d7f72163f9a5470a026864404be6f6425ff
- url: https://support.telnyx.com/en/articles/1277754-freepbx-v13-pjsip-credentials
  content_hash: d6b82b3b26113648aba80d412932763b0688d0d5fef4f6111b643e7b81934cba
- url: https://support.telnyx.com/en/articles/3284033-elastix-5-fqdn-trunk-setup
  content_hash: 1e12535102d44c5a74872c1b760b80a8ab79427a6da2fc4cf94c3d7ba32a0e57
- url: https://support.telnyx.com/en/articles/3284164-elastix-5-credentials-trunk
  content_hash: 1c955a0cbcda6901892717a3feda78787cf8252182aa2550494141091b6992fb
- url: https://support.telnyx.com/en/articles/3284736-freepbx-v14-ip-trunk-chansip
  content_hash: abb0a2a3d845c440534538acb07afaf3afd806cb3f0106f589c371bc8f4f62d8
- url: https://support.telnyx.com/en/articles/3284752-freepbx-v14-credentials-chansip
  content_hash: ea0381ca75d15af69d9eb3fbb979fa6c049988e8d3d245fa1cfbc629397630ca
- url: https://support.telnyx.com/en/articles/5464056-setting-up-freepbx-v15-with-telnyx-api
  content_hash: 0abcba9e57b50ae65f4cdd8406ea4200a34267053564c8f80b31b6f96626a76c
- url: https://support.telnyx.com/en/articles/5467232-freepbx-v15-ip-trunk-chansip-tutorial
  content_hash: 2b74396965cfb1e0032b9ee1c046f7f349888d53fc2584f460ae0596f38217bf
- url: https://support.telnyx.com/en/articles/5619595-freepbx-v15-ip-trunk-pjsip
  content_hash: 97b84e426a7723c6dfdebed50c1dab66c1472af46eb3a3fe7980873d27fc3fa7
- url: https://support.telnyx.com/en/articles/5619597-freepbx-v15-credentials-pjsip
  content_hash: aad8fbb7d6b97e9fb886e76ae600137003847f5647255021a87404ed6b59df5c
updated_at: 2026-06-11T11:25:15Z
---

# PBX SIP Trunk Configuration with Telnyx

*Part 1 of 3 — see also: [Part 2](pbx-sip-trunk-configuration-with-telnyx--part-2.md), [Part 3](pbx-sip-trunk-configuration-with-telnyx--part-3.md)*

Comprehensive guide for configuring FreePBX (V13–V15) and Elastix (V4–V5) PBX systems with Telnyx SIP trunks, covering IP-based and credentials-based authentication, ChanSIP and PJSIP drivers, trunk settings, dial patterns, and call routing.

## Prerequisites

Before configuring any PBX with Telnyx, complete the following in the [Telnyx Mission Control Portal](https://portal.telnyx.com):

- Configure your account ([Get Started with a Mission Control Account](get-started-with-a-mission-control-account.md))
- Purchase and provision a DID (assign it to a SIP connection)
- Create a SIP connection — either an **IP-based connection** or a **credentials-based connection**
- Create an outbound voice profile and assign your DID to it
- **Recommended:** [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)

For credentials-based trunks you will need your SIP username and password from the connection settings (available under the "show password" link in the portal). For IP-based trunks, ensure your PBX's public IP is registered in the connection.

---

## FreePBX Configuration

FreePBX is a web-based open-source GUI that controls and manages Asterisk. It is recommended to use **PJSIP** instead of the legacy Chan_SIP driver, as PJSIP is actively maintained and provides more future-proof options. You can learn more about PJSIP at [pjsip.org](https://www.pjsip.org/about.htm).

### FreePBX Installation

1. Download the FreePBX ISO from [freepbx.org](https://www.freepbx.org/downloads/) and load it onto your server or virtual machine.
2. Select **Full Install** (via the appropriate Asterisk version for your FreePBX release — Asterisk 13 for V13, Asterisk 16 for V14/V15).
3. Confirm network settings, set your root password, and wait for packages to install.
4. After reboot, log in at the Linux console as `root` and note the displayed IP address.
5. Enter the IP address into a web browser. On first access, create the admin username and password (these are separate from the root password and are used only for the FreePBX web interface).
6. Complete the activation wizard: select **FreePBX Administration**, activate the system, choose default locales, and configure firewall settings as desired.

### SIP Settings and Network Configuration

1. Navigate to **Settings → Asterisk SIP Settings**.
2. Populate the **External** and **Local** network addresses under **General SIP Settings**.
3. For ChanSIP trunks, also populate the addresses under **Chan SIP Settings**. For PJSIP trunks, populate them under **PJSIP Settings**.
4. Click **Submit** and then **Apply Config**.

### Extensions

1. Navigate to **Applications → Extensions → Add Extension**.
2. Choose **Add New Chan SIP Extension** (for ChanSIP) or **Add New Chan PJSIP Extension** (for PJSIP).
3. Set the **Outbound CID** to the number you purchased from Telnyx. If you do not set an Outbound CID on the extension, you must set one on the trunk instead.
4. Populate the extension secret/password under the **Other** tab if needed.
5. **ChanSIP note:** Chan_SIP extensions listen on port 5160 (UDP), which is a non-standard port.
6. **PJSIP note:** PJSIP extensions listen on port 5060 (UDP).
7. Click **Submit** and **Apply Config**.

### ChanSIP Trunk Configuration

#### IP-Based (No Registration)

1. Navigate to **Connectivity → Trunks → Add Trunk → Add New Chan SIP Trunk**.
2. **General tab:** Enter a trunk name, Outbound CID, and maximum channels.
3. **Dialed Number Manipulation Rules tab:** See the [Dial Patterns](#dial-patterns) section below.
4. **SIP Settings → Outgoing sub-tab:**
   - `type`: friend
   - `qualify`: yes
   - `insecure`: port,invite
   - `host`: sip.telnyx.com
   - `fromdomain`: sip.telnyx.com
   - `disallow`: all
   - `allow`: ulaw
5. **SIP Settings → Incoming sub-tab:**
   - `type`: friend
   - `insecure`: port,invite
   - `host`: sip.telnyx.com
   - `dtmfmode`: rfc2833
   - `disallow`: all
   - `allow`: ulaw
6. Click **Submit** and **Apply Config**.

#### Credentials-Based (With Registration)

1. Follow the same steps as the IP-based trunk above, but add the following:
2. **SIP Settings → Outgoing sub-tab** — additionally set:
   - `username`: Your Telnyx SIP credentials username
   - `secret`: Your Telnyx SIP credentials password
   - `allow`: ulaw&alaw
3. **SIP Settings → Incoming sub-tab** — additionally set:
   - `username`: Your Telnyx SIP credentials username
   - `secret`: Your Telnyx SIP credentials password
   - `fromdomain`: sip.telnyx.com
   - `allow`: ulaw&alaw
   - `Register String`: `username:password@sip.telnyx.com/username`

     Example: `dillin1234:mypassword123@sip.telnyx.com/dillin1234`
4. Click **Submit** and **Apply Config**.

### PJSIP Trunk Configuration

#### IP-Based (No Registration)

1. Navigate to **Connectivity → Trunks → Add Trunk → Add SIP (chan_pjsip)**.
2. **General Settings tab:** Enter a trunk name (e.g., `Telnyx_userAuth`), Outbound CallerID, and CID Options: *Allow Any CID*.
3. **Dialed Number Manipulation Rules tab:** See the [Dial Patterns](#dial-patterns) section below.
4. **PJSIP Settings → General sub-tab:**
   - `Registration`: None
   - `SIP Server`: sip.telnyx.com
   - `SIP Server Port`: 5060
5. **PJSIP Settings → Advanced sub-tab:**
   - `From Domain`: sip.telnyx.com
6. **PJSIP Settings → Codecs sub-tab:** Select ulaw, alaw, gsm, g722, g729, and Opus. Uncheck all others. For video, Telnyx supports H264.
7. Click **Submit** and **Apply Config**.

#### Credentials-Based (With Registration)

1. Follow the same steps as the PJSIP IP-based trunk above, but configure the following in **PJSIP Settings → General sub-tab**:
   - `Username`: Your Telnyx SIP credentials username
   - `Auth Username`: Your Telnyx SIP credentials username
   - `Secret`: Your Telnyx SIP credentials password
   - `Authentication`: Outbound
   - `Registration`: Send
   - `SIP Server`: sip.telnyx.com
   - `SIP Server Port`: 5060 (for UDP/TCP) or 5061 (for TLS)
   - `Context`: from-pstn
   - `Transport`: UDP or TCP (or TLS/TCP if TLS is enabled)
2. **PJSIP Settings → Advanced sub-tab:**
   - `From Domain`: sip.telnyx.com
3. **PJSIP Settings → Codecs sub-tab:** Select ulaw, alaw, gsm, g722, g729, and Opus.
4. Click **Submit** and **Apply Config**.

---
