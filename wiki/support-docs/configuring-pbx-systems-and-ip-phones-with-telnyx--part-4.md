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

*Part 4 of 4 — see also: [Part 1](configuring-pbx-systems-and-ip-phones-with-telnyx--part-1.md), [Part 2](configuring-pbx-systems-and-ip-phones-with-telnyx--part-2.md), [Part 3](configuring-pbx-systems-and-ip-phones-with-telnyx--part-3.md)*

Comprehensive guide for configuring a wide range of PBX platforms and IP phones to interoperate with Telnyx SIP trunks, covering authentication, trunk creation, inbound and outbound routing, caller ID, SMS, and version-specific considerations for systems including 3CX, Thirdlane, GOautodial, Grandstream, Yeastar, Vodia, Bicom, and Gigaset.

## 3CX

[3CX](https://www.3cx.com/) is an open-standards IP PBX with unified communications. Telnyx configuration varies between V18, V20, and newer versions.

### 3CX and Telnyx Compatibility

- Telnyx is **no longer a supported carrier** on 3CX. 3CX has shut down support for third-party carriers in some versions.
- Existing Telnyx SIP trunks on previous 3CX versions will continue to function with future updates.
- If a SIP trunk is deleted, it can be recreated using the **3CX Generic VoIP Provider** template (not available on 3CX Hosted, FREE, PRO, ENT licences, or 3CX StartUP — only on dedicated/self-hosted systems).
- The generic template works with the Telnyx Messaging API and basic calls, but full compatibility with all call scenarios is not guaranteed and may require adjustments.
- Customers using the Telnyx Messaging API must switch to the generic template.

### 3CX Basic Setup (V18 and V20)

During initial setup, configure:
1. **Extension Length**: Number of digits (cannot be changed later).
2. **Admin Email**: For system notifications.
3. **Timezone**.
4. **Operator**: Default operator extension for inbound calls and voicemail.
5. **Allowed Countries**: Regions permitted for outgoing calls.
6. **Prompt Set**: Language for automated prompts.
7. **Registration**: Personal registration details.

### 3CX Network Settings

- Ensure the SIP port is set to 5060.
- Verify the **Public IP** and network card interface.
- In **External IP Configuration**, ensure the connection IP matches your static public IP.
- For V20, whitelist Telnyx SIP Signaling and Media IP addresses under **Admin > Advanced > IP Blacklist** (a `.json` import file is available from Telnyx).

### 3CX V18 — SIP Trunk via XML Import

1. Go to **SIP Trunks** and click **Import Provider**.
2. Upload the `telnyx.pv.xml` file (available from Telnyx support or the Telnyx help article).
3. Enter the main trunk number.
4. On the **General** tab:
   - **Registrar/Server/Gateway**: `sip-anycast1.telnyx.com:5060` or `sip.telnyx.com:5060`
   - **Number of SIM Calls**: As needed.
5. **Authentication**:
   - *Register/Account based*: Enter your Telnyx connection username and password.
   - *IP based*: Select **Do not require**; leave authentication fields empty.
6. Under **Route calls to**, configure office-hours and after-hours destinations.
7. On the **SMS** sub-tab:
   - **API Key**: Generate at `https://portal.telnyx.com/#/api-keys`.
   - **Provider URL**: `https://api.telnyx.com/v2/messages`
   - **Copy Webhook URL**: Paste this into your Telnyx messaging profile.

### 3CX V20 — SIP Trunk via Generic Provider

1. Go to **Admin > Voice & Chat** and click **Add SIP Trunk > Add Trunk**.
2. Enter a trunk name and default route.
3. Under **VoIP Provider**:
   - **Country**: US, Europe, Australia, or Canada.
   - **Provider**: Generic VoIP Provider.
4. Enter the **Main Trunk Number** (your Telnyx DID).
5. For credentials-based authentication:
   - **Authentication ID / Password**: Your Telnyx SIP credentials.
   - **Type of Authentication**: Register/Account Based.
   - **Server**: `sip.telnyx.com` (or `sip.telnyx.ca`, `sip.telnyx.com.au`, `sip.telnyx.eu` as appropriate), port 5060.
6. The trunk should appear in green (the "Untested provider" warning can be disregarded).
7. Add additional DIDs under the **DID Numbers** tab.

### 3CX V20 — SMS Configuration

1. In the trunk's **SMS** tab:
   - **API Key**: Generate from the Telnyx portal.
   - **Provider URL**: `https://api.telnyx.com/v2/messages`
   - Copy the webhook URL and paste it into your Telnyx messaging profile.
2. Click **Save**.

### 3CX Users and DID Assignment

1. Go to **Admin > Users** and click **Add User**.
2. Enter the user's name; they will receive an email with account details if an email is provided.
3. Edit the user and assign a DID for inbound and outbound calls and messages.

### 3CX Inbound Rules

1. Go to **Inbound Rules** and click **+Add DID Rule**.
2. Set a name (e.g., `IB_Telnyx`) and configure the **Route calls to** destination for office hours and after hours.

### 3CX Outbound Rules

1. Go to **Outbound Rules** and click **+Add**.
2. Set a name (e.g., `OB_Telnyx`).
3. Configure **Calls from extension(s)** and optional prefix/length filters.
4. Under **Make outbound calls on**, select the Telnyx trunk as Route 1 (strip 0 digits). Configure backup routes with appropriate strip settings.
5. Optionally set an **Outbound Caller ID** on the route (applies to all calls through this route).

**Important notes for outbound calls:**
- If no caller ID is set through 3CX, calls may arrive at Telnyx without a caller ID and could be rejected. Apply a Caller ID Override from your Telnyx SIP Connection's outbound options if needed.
- 3CX typically requires numbers in +E.164 format. Ensure your Telnyx SIP Connection inbound ANI/DNIS number formats are set to +E.164.
- For international dialing, 3CX WebRTC may convert `+` to `001`. Create an outbound rule to strip `00` and prepend `+` as needed.

### 3CX Messaging

1. Use the 3CX WebClient or mobile app.
2. Go to **Chats**, click the compose icon, and select **Compose SMS**.
3. Select a contact, type your message, and send.
4. Inbound messages appear in the chat; replies are also visible in the Telnyx Messaging Report.

## Additional Resources

- [Mission Control Portal](mission-control-portal.md) getting started guide
- [Thirdlane documentation](https://www.thirdlane.com/docs/platform/introduction) | [Support](https://www.thirdlane.com/support) | [REST API](https://www.thirdlane.com/docs/platform/api)
- [GOautodial documentation](https://goautodial.org/projects/goautodialce/wiki) | [Forums](https://goautodial.org/projects/goautodialce/boards) | [GitHub](https://goautodial.org/)
- [Grandstream firmware updates](https://www.grandstream.com/support/firmware) | [FAQ](https://blog.grandstream.com/faq) | [Forums](https://forums.grandstream.com/)
- [Yeastar Cloud PBX Admin Guide](https://help.yeastar.com/en/cloudpbx/topic/admin_guide.html) | [S-Series Admin Guide](https://help.yeastar.com/en/s-series/topic/admin_guide.html)
- [Vodia documentation](https://doc.vodia.com/) | [Forums](https://forum.vodia.com/) | [Portal](https://portal.vodia.com/)
- [Bicom support](https://www.bicomsystems.com/support/)
- [3CX help](https://www.3cx.com/support/) | [3CX V20 updates](https://www.3cx.com/blog/releases/)
- [Gigaset DX800a user manual](https://gse.gigaset.com/fileadmin/legacy-assets/Gigaset%20DX800A%20all%20in%20one_Web_en_GBR.pdf)
