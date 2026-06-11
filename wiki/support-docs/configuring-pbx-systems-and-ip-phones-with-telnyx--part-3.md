---
title: Configuring PBX Systems and IP Phones with Telnyx
summary: Comprehensive guide for configuring a wide range of PBX platforms and IP
  phones to interoperate with Telnyx SIP trunks, covering authentication, trunk creation,
  inbound and outbound routing, caller ID, SMS, and version-specific considerations
  for systems including 3CX, Thirdlane, GOautodial, Grandstream, Yeastar, Vodia, Bicom,
  and Gigaset.
sources:
- url: https://support.telnyx.com/en/articles/1130631-how-to-configure-a-thirdlane-pbx
  content_hash: af727a609a21abb2fad484e314bbc95660464ee8206d14d79f17e16cc336febc
- url: https://support.telnyx.com/en/articles/1130649-configuring-a-goautodial-pbx-ip-trunk
  content_hash: 683a746651d6a1a9241238b9c66b1dbe18d9b53a2900aee27ca13e7c9c62a15d
- url: https://support.telnyx.com/en/articles/1130694-configuring-a-goautodial-pbx-sip-trunk
  content_hash: 77509400a237e7b85db2421dd1ac8cc5e1a687b31ef86b934ceff1a7953ef37c
- url: https://support.telnyx.com/en/articles/1295514-grandstream-umc6202-auth-setup
  content_hash: cf77d8aaa180f925b31a82b23a4c7eb70057da0a6f88fd7b797eed5b302878a1
- url: https://support.telnyx.com/en/articles/3185933-vodia-multi-tenant-pbx-setup
  content_hash: 0cc35194932f4a1ebad169593f7728ccb04f2ca34e956d6fda6687cef8f1e747
- url: https://support.telnyx.com/en/articles/5138185-bicom-pbxware-setup
  content_hash: 5823afdb88ed10b43e9dfd8308ba43b5cdf7649d7a186696cb540eb50c75525b
- url: https://support.telnyx.com/en/articles/5748258-grandstream-ucm6xxx-sip-trunks
  content_hash: c62d9390c98a6f79fc1eefae42cc2dd48b77b6836fdae184e4cccab7b3bc0567
- url: https://support.telnyx.com/en/articles/5748952-yeastar-s-series-telnyx-sip
  content_hash: d46fcc4c49d0fe409776a4bc9a445f6eae549a9d1d4c23a237d831827450f0b3
- url: https://support.telnyx.com/en/articles/6161111-3cx-configuring-a-3cx-v18-pbx
  content_hash: dd458459be6221c26ba610460e53ae764a9e9fed92b809c6641b58eaf11dbe7e
- url: https://support.telnyx.com/en/articles/6167480-gigaset-configuring-the-gigaset-dx800a
  content_hash: 636e1c103d54c81b15909f867bb1a7762328c93413e66030dfd9c9628055b960
- url: https://support.telnyx.com/en/articles/6184147-grandstream-grp2612-sip-trunk
  content_hash: 9b9f42c71ba239b0f983b8e8725f32a9f2a07b616cf53fc7fddae9953448fba1
- url: https://support.telnyx.com/en/articles/6184520-grandstream-gxp1700-sip-trunk
  content_hash: 86abea91de77be48b943eb0a05856f490ef21cef43bab421d52e3762b75f1ec8
- url: https://support.telnyx.com/en/articles/7829412-3cx-and-telnyx-compatibility
  content_hash: 5a84022998015a0a424d0863ca842a777e3795064eeb5935acf83b084c5c26c6
- url: https://support.telnyx.com/en/articles/8683996-3cx-configuring-a-3cx-v20-pbx-20-0-update-5-build-20-0-5-551-march-2025-update
  content_hash: 88a39c4e53a4089c21480412c2a8a73d9585bb87af11a8f3c17c97eba66b66fa
updated_at: 2026-06-11T11:29:02Z
---

# Configuring PBX Systems and IP Phones with Telnyx

*Part 3 of 4 — see also: [Part 1](configuring-pbx-systems-and-ip-phones-with-telnyx--part-1.md), [Part 2](configuring-pbx-systems-and-ip-phones-with-telnyx--part-2.md), [Part 4](configuring-pbx-systems-and-ip-phones-with-telnyx--part-4.md)*

Comprehensive guide for configuring a wide range of PBX platforms and IP phones to interoperate with Telnyx SIP trunks, covering authentication, trunk creation, inbound and outbound routing, caller ID, SMS, and version-specific considerations for systems including 3CX, Thirdlane, GOautodial, Grandstream, Yeastar, Vodia, Bicom, and Gigaset.

## Yeastar S-Series and Cloud PBX

Yeastar supports two trunk types: **Register Trunk** (credentials-based) and **Peer Trunk** (IP-based).

### Yeastar Register Trunk

1. Go to **Settings > PBX > Trunks** and click **Add Trunk**.
2. Configure:
   - **Select Country**: General
   - **Trunk Type**: Register Trunk
   - **Hostname/IP / Domain**: `sip.telnyx.com`
   - **Username / Password**: Your Telnyx SIP credentials
   - **Authentication Name**: Provided by Telnyx support if needed
   - **From User**: Your Telnyx username
3. Click **Advanced** to set DID numbers if different from the authentication name. Add DNIS names for display.
4. Click **Save** and **Apply**. Check status in **PBX Monitor**.
5. Set **Default Registration Time** to `300` under **Settings > PBX > General > SIP**.

### Yeastar Peer Trunk

1. Go to **Settings > PBX > Trunks** and click **Add Trunk**.
2. Configure:
   - **Select Country**: General
   - **Trunk Type**: Peer Trunk
   - **Hostname/IP / Domain**: `sip.telnyx.com`
3. Click **Save** and **Apply**. Check status in **PBX Monitor**.

### Yeastar Outbound Route

1. Go to **Settings > PBX > Call Control > Outbound Routes** and click **Add**.
2. Configure:
   - **Route Name**: Descriptive name
   - **Dial Patterns**: Prefix (e.g., `8`) and **Strip** (`1` to remove the prefix).
   - **Member Extensions**: Allowed extensions.
   - **Member Trunks**: Select the Telnyx trunk.

### Yeastar Inbound Route

1. Go to **Settings > PBX > Call Control > Inbound Routes** and click **Add**.
2. Configure:
   - **Name**: Descriptive name
   - **Member Trunks**: Select the Telnyx trunk.
   - **Destination**: Where incoming calls should route.
3. Click **Save** and **Apply**.

## Vodia Multi-Tenant PBX

[Vodia PBX](https://web.vodia.com/) runs on Windows, Linux, or macOS and supports automatic provisioning for major SIP phone brands.

1. Log into Vodia PBX, navigate to your Domain, and go to **TRUNKS > VoIP Providers**.
2. Click **Add** and select *Telnyx* from the **Provider** dropdown.
3. Enter your Telnyx username and password, then click **Create**.
4. Vodia has a built-in Telnyx template, so the SIP outbound proxy, trunk headers, and a default dial plan are configured automatically.

### Vodia Inbound Routing

1. Navigate to your Telnyx trunk and scroll to **Routing/Redirection**.
2. Choose an inbound method:
   - Send all to the destination request URL
   - Send all calls to a specific account
   - Send to a 10-digit DID
   - Match extension after a prefix
   - Use a list of expression
3. For multiple DIDs, switch to Admin mode and navigate to **DID Management** to assign DIDs to specific extensions.
4. For multiple numbers, set routing to **Send all to the destination request URL**.

## Bicom PBXware

[Bicom Systems PBXware](https://www.bicomsystems.com/) supports Telnyx as an SMS provider. Bicom Systems has created a [detailed custom integration document for Telnyx](https://go.telnyx.com/rs/telnyx/images/Content_Guide_BicomPBXwareTelnyxconfiguration.pdf). If you experience difficulty, contact Telnyx support.

Prerequisites include porting your number to Telnyx and setting up hosted SMS.

## Gigaset DX800a

The Gigaset DX800a (legacy device) is a hybrid multiline desktop phone.

1. Access the web portal using the phone's IP address. The default system PIN is `0000`.
2. Go to **Settings > Telephony**, click **Edit** next to the connection, then click **Show Advanced Settings**:
   - **Authentication Name / Username**: Your Telnyx SIP username
   - **Authentication Password**: Your Telnyx SIP password
   - **Display Name**: Your caller ID
   - **Domain / Proxy Server Address / Registration Address / Outbound Server Address**: `sip.telnyx.com`
   - **Proxy Server Port / Outbound Server Port**: 5060 (UDP/TCP) or 5061 (TLS)
   - **Registration Refresh Time**: 600
   - **STUN enabled**: Yes (recommended); **STUN Server**: `stun.telnyx.com:3478`
   - **Outbound proxy mode**: Always
3. Click **Set** to save.

### Gigaset Audio Settings

Go to **Settings > Audio**, click **Show Advanced Settings**, and add only Telnyx-supported codecs: ulaw, alaw, g722, g729.

### Gigaset Call Routing

Go to **Settings > Number Assignment** and select the Telnyx account for both incoming and outgoing calls.

### Gigaset Dial Plan

Go to **Settings > Dialing Plans** and add rules:
- **Phone number**: Emergency code (e.g., `911`)
- **Connection**: The Telnyx connection
- **Active**: Checked
