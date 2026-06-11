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

*Part 2 of 3 — see also: [Part 1](pbx-sip-trunk-configuration-with-telnyx--part-1.md), [Part 3](pbx-sip-trunk-configuration-with-telnyx--part-3.md)*

Comprehensive guide for configuring FreePBX (V13–V15) and Elastix (V4–V5) PBX systems with Telnyx SIP trunks, covering IP-based and credentials-based authentication, ChanSIP and PJSIP drivers, trunk settings, dial patterns, and call routing.

## Elastix Configuration

Elastix 4 is a CentOS-based PBX. Elastix 5 is powered by 3CX and uses a different configuration approach. Elastix 4 ISOs are no longer available from the original provider; Telnyx hosts a copy.

### Elastix 4 IP-Based Trunk

1. Install Elastix 4 from the ISO. Set root password, SQL root password, and admin password during installation.
2. Access the GUI via the displayed URL.
3. **Network settings:** Go to **PBX → Tools → Asterisk File Editor**, filter for `sip_nat.conf`, and set:
   - `localnet=` your local network subnet
   - `externip=` your external IP
   - Click **Save**, then **Reload Asterisk**.
4. **Extensions:** Go to **PBX → PBX Configurations → Extensions → Add SIP Extension**. Set the extension number, display name, Outbound CID (your Telnyx number), secret, DTMFmode (`RFC 2833`), and NAT (`No - RFC 3581`). Click **Submit**, then **Apply Config**.
5. **Trunk:** Go to **PBX → PBX Configurations → Trunks** and configure:

   **Outgoing SIP Settings:**
   - `Host`: sip.telnyx.com
   - `Type`: peer
   - `Qualify`: Yes
   - `Disallow`: All
   - `Allow`: ulaw & alaw

   **Incoming SIP Settings:**
   - `Host`: sip.telnyx.com
   - `Type`: friend
   - `Insecure`: port,invite
   - `Disallow`: All
   - `Allow`: ulaw
   - `DTMFmode`: RFC 2833
   - `NAT`: force_rport,comedia
   - `Registration string`: Leave blank (IP-based, no registration needed)
   - `Dialed number manipulation rules`: prepend `1`; match pattern `NXXNXXXXXX` and prepend blank; match pattern `1NXXNXXXXXX`

6. Click **Submit** and **Apply Config**.

### Elastix 4 Credentials-Based Trunk

Follow the same steps as the IP-based trunk, but add the following:

**Outgoing SIP Settings** — additionally set:
- `Username`: Your Telnyx account username
- `Secret`: Your Telnyx account password
- `Type`: friend
- `Insecure`: port, invite

**Incoming SIP Settings** — additionally set:
- `Username`: Your Telnyx account username
- `Secret`: Your Telnyx account password
- `Fromdomain`: sip.telnyx.com
- `Registration string`: `your_username:your_password@sip.telnyx.com`

### Elastix 5 (3CX-Based) Configuration

Elastix 5 requires a license key and is powered by 3CX. The initial setup wizard configures FQDN, certificates, extensions, and network settings.

1. After installation, use the provided URL to access the 3CX Management Console in your browser.
2. Complete the setup wizard: enter your license key, configure public IP (static or dynamic), set management console ports, select the network adapter, generate FQDN and certificates, set extension digit count, enter admin email, select country/time zone, create an operator extension, and choose preferred language.
3. **Network confirmation:** Go to **Settings → Network**. On the **Ports** tab, set SIP Port to `5060`. On the **Public IP** tab, verify your public IP and network interface. Ensure the connection IP on the Telnyx Portal matches your static public IP (you can use FQDN for inbound and IP for outbound).
4. **SIP Trunk:** Click **SIP Trunks → + Add SIP Trunk**:
   - **Select Country:** Worldwide
   - **Select Provider:** Telnyx LLC
   - **Main Trunk No:** Your purchased Telnyx number
5. In the trunk configuration window, **General tab → Trunk Details**:
   - `Enter name of Trunk`: Telnyx LLC
   - `Registrar/Server/Gateway Hostname or IP`: sip-anycast1.telnyx.com:5060 or sip.telnyx.com:5060
   - `Outbound Proxy`: sip.telnyx.com
   - `Number of SIM Calls`: set as desired
6. **Authentication section:**
   - For **IP-based (FQDN) trunk:** Type of Authentication: *Do not require - IP Based*; Authentication ID: your purchased Telnyx number; Authentication Password: leave blank.
   - For **Credentials trunk:** Type of Authentication: *Register/Account based*; Authentication ID: your Telnyx username; Authentication Password: your Telnyx password.
7. **Route calls to section:** Set main trunk number and office hours/out-of-hours destinations as desired.
8. **Options tab:** Set *Require registration for* to *Do not require*. Remove **GSM-FR** from Assigned Codecs.
9. **Outbound Parameters tab → SIP Field section:** Set Contact User Part to *Custom Field* (leave the custom value blank).
10. Click **Apply**, then **OK**. The trunk will go live.

---

## Call Routing

### FreePBX Outbound Routes

1. Navigate to **Connectivity → Outbound Routes → Add Outbound Route**.
2. Set the **Route Name** (e.g., `Outbound_Telnyx`) and **Route CID** (your Telnyx number).
3. In **Trunk Sequence for Matched Routes**, select the Telnyx trunk.
4. On the **Dial Patterns** tab, enter appropriate patterns. For US/North American calling, use patterns for 10-digit and 11-digit dialing.
5. Click **Submit** and **Apply Config**.

### FreePBX Inbound Routes

1. Navigate to **Connectivity → Inbound Routes → Add Inbound Route**.
2. Set a description and the **DID Number** (in 11-digit E.164 format, e.g., `12172031700`).
3. Specify the destination extension for calls received on this DID.
4. Click **Submit** and **Apply Config**.

### Elastix 4 Outbound Routes

1. Go to **PBX → PBX Configurations → Outbound Routes → Add Route**.
2. Set the **Route Name**, **Route CID** (your Telnyx number), **Dial Patterns**, and set the trunk sequence to *Telnyx*.
3. Click **Submit** and **Apply Config**.

### Elastix 4 Inbound Routes

1. Go to **PBX → PBX Configurations → Inbound Routes → Add Incoming Route**.
2. Set a **Description**, the **DID Number** (your Telnyx number), and the target **Extensions**.
3. Click **Submit** and **Apply Config**.

### Elastix 5 Outbound Rules

1. Click **Outbound Rules → +Add**.
2. Set the **Rule Name**.
3. Under **Apply this rule to these calls**, specify extensions (e.g., `000`).
4. Under **Make outbound calls on**, configure up to 3 routes (primary and backups). Set **Strip Digits** to 0 on Route 1 and 1 on backup routes.
5. You can apply an outbound caller ID on the route (it will apply to all calls through that route). If you do not set one here, apply it per user or extension.
6. Click **OK**.

### Elastix 5 Inbound Rules

1. Click **Inbound Rules → +Add DID Rule**.
2. Set a **Name** and the **DID/DDI** (one of your provisioned Telnyx numbers).
3. Configure the **Route calls to** section with the main trunk number and office hours/out-of-hours destinations.
4. Click **OK**.

---

## Dial Patterns

The following dial patterns are commonly used for US/North American calling:

**US Numbers:**

| Prepend | Match Pattern |
|----------|---------------|
| 1 | NXXNXXXXXX |
| (blank) | 1NXXNXXXXXX |

**International Numbers:**

| Prepend | Match Pattern |
|----------|-------------------------------|
| Country dialing prefix | NXXNXXXXXX |
| (blank) | (Country dialing prefix)NXXNXXXXXX |

For regions outside North America, contact Telnyx support for appropriate dial patterns.

---

## Caller ID Configuration

- If you do not set an **Outbound CID** on the trunk, you must set one on each relevant extension.
- If you do not set a caller ID on either the trunk or each extension, your calls will reach the Telnyx SIP proxy without a valid caller ID.
- You may instead enable a **Caller ID Override** in your SIP Connection's Outbound Options within the Telnyx Portal.
- Review the [Telnyx Caller ID Number Policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy) for accepted formats.

For Elastix 5 / 3CX outbound caller ID names:
- Use **capital letters** for better visibility on devices.
- Do **not** use special characters (they will not be displayed).
- Some Canadian providers show no more than **15 characters**.
- Spaces are allowed.

---
