---
title: Configuring PBX Systems and IP Phones with Telnyx
summary: Comprehensive guide for configuring a wide range of PBX platforms and IP
  phones to interoperate with Telnyx SIP trunks, covering authentication, trunk creation,
  inbound and outbound routing, caller ID, SMS, and version-specific considerations
  for systems including 3CX, Thirdlane, GOautodial, Grandstream, Yeastar, Vodia, Bicom,
  and Gigaset.
sources:
- url: https://support.telnyx.com/en/articles/1130631-how-to-configure-a-thirdlane-pbx
- url: https://support.telnyx.com/en/articles/1130649-configuring-a-goautodial-pbx-ip-trunk
- url: https://support.telnyx.com/en/articles/1130694-configuring-a-goautodial-pbx-sip-trunk
- url: https://support.telnyx.com/en/articles/1295514-grandstream-umc6202-auth-setup
- url: https://support.telnyx.com/en/articles/3185933-vodia-multi-tenant-pbx-setup
- url: https://support.telnyx.com/en/articles/5138185-bicom-pbxware-setup
- url: https://support.telnyx.com/en/articles/5748258-grandstream-ucm6xxx-sip-trunks
- url: https://support.telnyx.com/en/articles/5748952-yeastar-s-series-telnyx-sip
- url: https://support.telnyx.com/en/articles/6161111-3cx-configuring-a-3cx-v18-pbx
- url: https://support.telnyx.com/en/articles/6167480-gigaset-configuring-the-gigaset-dx800a
- url: https://support.telnyx.com/en/articles/6184147-grandstream-grp2612-sip-trunk
- url: https://support.telnyx.com/en/articles/6184520-grandstream-gxp1700-sip-trunk
- url: https://support.telnyx.com/en/articles/7829412-3cx-and-telnyx-compatibility
- url: https://support.telnyx.com/en/articles/8683996-3cx-configuring-a-3cx-v20-pbx-20-0-update-5-build-20-0-5-551-march-2025-update
updated_at: 2026-06-11T11:29:02Z
---

# Configuring PBX Systems and IP Phones with Telnyx

*Part 2 of 4 — see also: [Part 1](configuring-pbx-systems-and-ip-phones-with-telnyx--part-1.md), [Part 3](configuring-pbx-systems-and-ip-phones-with-telnyx--part-3.md), [Part 4](configuring-pbx-systems-and-ip-phones-with-telnyx--part-4.md)*

Comprehensive guide for configuring a wide range of PBX platforms and IP phones to interoperate with Telnyx SIP trunks, covering authentication, trunk creation, inbound and outbound routing, caller ID, SMS, and version-specific considerations for systems including 3CX, Thirdlane, GOautodial, Grandstream, Yeastar, Vodia, Bicom, and Gigaset.

## Grandstream UCM6xxx Series

The [Grandstream UCM6200/UCM6300 series](https://www.grandstream.com/products/ip-pbxs/ucm-series-ip-pbxs/product/ucm6200-series) IP PBX appliances deliver enterprise-grade voice, video, data, and mobility features without licensing fees.

> **Firmware Notice:** Firmware 1.0.18.x is the last supported version for UCM61xx. Upgrade all UCM devices to the latest official firmware for security and lifespan improvements.

### UCM6xxx Login

1. Power on the UCM device and note the IP address on its LCD.
2. Browse to `https://<ip-address>:8089` (default HTTPS port).
3. Default credentials: Username `admin`, Password `admin` (units from January 2017 have a unique password on the back sticker).

### UCM6xxx SIP Trunk Creation

1. Navigate to **Extension/Trunk > VoIP Trunks** and click **Add SIP Trunk**.
2. On the **Basic Settings** tab:
   - **Type**: Register SIP Trunk
   - **Provider Name**: Telnyx
   - **Host Name**: `sip.telnyx.com` (append `:5061` if TLS is enabled)
   - **From Domain**: `sip.telnyx.com`
   - **Username / Password**: Your Telnyx SIP credentials
   - **Transport**: UDP or TCP (or TLS if encryption is configured)
   - **Keep Trunk CID**: Enable if the trunk should send its own CID; disable if extensions send their own.
   - **Caller ID Name**: Follow standard naming conventions (capitals, no special characters).
3. On the **Advanced Settings** tab:
   - **Codec Preference**: ulaw, alaw, g722, g729 only.
   - **Send PPI Header** or **Send PAI Header**: Enable one (not both) for caller ID functionality.
   - **Passthrough PAI Header**: Enable if Send PAI Header is disabled but you want to preserve PAI headers.
   - **DTMF Mode**: Default (RFC2833).
   - **Enable Heartbeat Detection**: Checked; **Heartbeat Frequency**: 60.
   - **SRTP**: *Enabled and forced* if using TLS.
4. Click **Save** then **Apply Changes**.
5. Verify registration under **System Status > Dashboard**. If status is *Rejected*, check network reachability and credentials.

### UCM6xxx Outbound Routes

1. Go to **Extension/Trunk > Outbound Routes** and click **+Add**.
2. Configure:
   - **Calling Rule Name**: Descriptive name.
   - **Pattern**: Dial pattern (prefix dial-out codes after `_`, e.g., `_9NXXXXXXXXX`).
   - **Trunk**: Select the Telnyx trunk.
   - **Privilege Level**: Match your Telnyx outbound profile.
   - **Strip**: Number of prefix digits to remove (e.g., `1` to strip a leading `9`).

### UCM6xxx Inbound Routes

1. Go to **Extension/Trunk > Inbound Routes** and click **Add**.
2. Configure:
   - **Trunks**: Select the Telnyx trunk.
   - **Patterns**: Your Telnyx DID prefixed with `_`.
   - **Default Destination**: Extension, IVR, etc.

### UCM6xxx Outbound Caller ID

Three methods are available:

1. **Global outbound CID**: Go to **PBX Settings > General Settings**.
2. **Per-extension CID**: Go to **Extension/Trunk > Extensions**, edit the extension, and fill the **CallerID Number** field.
3. **Per-outbound-route CID**: Go to **Extension/Trunk > Outbound Routes** and set the **Outbound Route CID** field.

### UCM6xxx Optional Features

- **Time Conditions**: Set time-based routing on inbound/outbound rules under the **Time Condition** section.
- **Trunk Groups** (firmware 1.0.20.17+): Create VoIP Trunk Groups to apply settings to multiple accounts under **Extension/Trunk > VoIP Trunks**.
- **Failover Routes**: In outbound routes, click **Click to add failover trunk** to configure a backup trunk that activates on no response (32 s), SIP error responses (403/407/408/503/603), or disabled primary trunk.

## Grandstream UMC6202 (Registration Auth)

This covers the UMC6202 specifically with credentials-based authentication.

1. Access the web UI via the device IP (WAN IP or default LAN IP `192.168.2.1`). Default credentials: `admin` / `admin` (or the unique password on newer units).
2. Go to **Extension/Trunk > VoIP Trunks** and click **Add SIP Trunk**:
   - **Type**: Register SIP Trunk
   - **Provider Name**: Telnyx
   - **Select Host Name**: `sip.telnyx.com`
   - **Username / Password**: Your Telnyx SIP credentials
3. Create inbound routes under **Extension/Trunk > Inbound Routes** — select the trunk, add patterns, and set the default destination.
4. Create outbound routes under **Extension/Trunk > Outbound Routes** — name the rule, add patterns, set privilege level, and select the Telnyx trunk.
5. Configure outbound caller ID using the three methods described in the UCM6xxx section above.

> If hostname resolution causes issues, use the primary IP address `192.76.120.10`.

## Grandstream GRP2612 / GRP261x/262x/263x Series

1. Log into the Grandstream web portal.
2. Navigate to **Account** settings and configure:

   **Account Register:**
   - **Account Active**: Yes
   - **Account Name**: Descriptive name
   - **SIP Server**: `sip.telnyx.com`
   - **Secondary SIP Server**: `64.16.250.10`
   - **Outbound Proxy**: `sip.telnyx.com`
   - **SIP User ID / SIP Authentication ID**: Your Telnyx SIP username
   - **SIP Authentication Password**: Your Telnyx SIP password

   **Account Dial Plan:**
   - **Name**: Your caller ID (follow naming conventions)
   - **Rule / Type**: Configure as needed (pattern, block, dial now, prefix, second tone).

   **Network Settings:**
   - **DNS Mode**: A Record (default), SRV, NATPTR/SRV, or Use Configured IP.

   **SIP Settings > Basic Settings:**
   - **SIP Registration**: Enabled
   - **Local SIP Port**: 5060 (UDP) or 5061 (TLS/TCP)
   - **SIP Transport**: UDP (default) or TLS/TCP if encrypting
   - **SIP Listening Mode**: Transport Only, Dual, Dual (Secured), or Dual (BLF Enforced)

3. Check account status on the **Status** page.

## Grandstream GXP1700 Series

1. Log into the Grandstream web portal.
2. Navigate to **Account > General Settings**:
   - **Account Active**: Yes
   - **Account Name**: Descriptive name
   - **SIP Server**: `sip.telnyx.com`
   - **Secondary SIP Server**: `64.16.250.10`
   - **Outbound Proxy**: `sip.telnyx.com`
   - **SIP User ID / Authenticate ID**: Your Telnyx SIP username
   - **Authenticate Password**: Your Telnyx SIP password
   - **Name**: Caller ID (follow naming conventions)
3. In **Account > Network Settings**, configure DNS mode as needed.
4. In **Account > SIP Settings > Basic Settings**:
   - **SIP Registration**: Enabled
   - **Local SIP Port**: 5060 (UDP) or 5061 (TLS/TCP)
   - **SIP Transport**: UDP or TLS/TCP
   - **SIP Listening Mode**: As needed
5. In **Account > Audio Settings**, set **Preferred Vocoder** to Telnyx-supported codecs only (ulaw, alaw, g722, g729).
6. In **Settings > General Settings**, set **STUN Server** to `stun.telnyx.com:3478`.
