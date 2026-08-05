---
title: Configuring Elastix and Epygi IP PBXs with Telnyx
summary: This page consolidates Telnyx support documentation for configuring Elastix
  4 (IP and credentials trunks), Elastix 5 (FQDN and credentials trunks), and Epygi
  QX-series IP PBXs to interoperate with Telnyx as a SIP provider. It covers prerequisites,
  installation, SIP trunk creation, and inbound/outbound routing for each platform.
sources:
- url: https://support.telnyx.com/en/articles/1130622-configuring-an-elastix-4-pbx-ip-trunk
- url: https://support.telnyx.com/en/articles/1130654-configuring-an-elastix-4-pbx-trunk
- url: https://support.telnyx.com/en/articles/3284033-elastix-5-fqdn-trunk-setup
- url: https://support.telnyx.com/en/articles/3284164-elastix-5-credentials-trunk
- url: https://support.telnyx.com/en/articles/5728748-epygi-ip-pbx-telnyx-setup
- url: https://support.telnyx.com/en/articles/6966381-use-wal-g-with-telnyx-storage
updated_at: 2026-08-05T13:28:08Z
---

# Configuring Elastix and Epygi IP PBXs with Telnyx

*Part 4 of 5 — see also: [Part 1](configuring-elastix-and-epygi-ip-pbxs-with-telnyx--part-1.md), [Part 2](configuring-elastix-and-epygi-ip-pbxs-with-telnyx--part-2.md), [Part 3](configuring-elastix-and-epygi-ip-pbxs-with-telnyx--part-3.md), [Part 5](configuring-elastix-and-epygi-ip-pbxs-with-telnyx--part-5.md)*

This page consolidates Telnyx support documentation for configuring Elastix 4 (IP and credentials trunks), Elastix 5 (FQDN and credentials trunks), and Epygi QX-series IP PBXs to interoperate with Telnyx as a SIP provider. It covers prerequisites, installation, SIP trunk creation, and inbound/outbound routing for each platform.

## Elastix 5 Credentials Trunk

Use this configuration when authenticating the Elastix 5 PBX to Telnyx with SIP credentials.

### Create a Telnyx SIP trunk

1. From the left-hand navigation, click **SIP Trunks**.
2. Click **+ Add SIP Trunk**.
3. In the pop-up, enter:
   - **Select Country:** `Worldwide`.
   - **Select Provider in your Country:** `Telnyx LLC`.
   - **Main Trunk No:** the [Telnyx number](https://portal.telnyx.com/#/app/numbers/my-numbers) you purchased.

   ![SIP Trunk/VoIP Provider interface.](_images/2e0700ca6ed799ee.png)
4. Click **OK** to open the trunk configuration window.
5. On the **General** tab, in **Trunk Details**, provide:
   - **Enter name of Trunk:** `Telnyx LLC`.
   - **Registrar/Server/Gateway Hostname or IP:** `sip-anycast1.telnyx.com:5060` or `sip.telnyx.com:5060`.
   - **Outbound Proxy:** `sip.telnyx.com`.
   - **Number of SIM Calls:** your preferred number of simultaneous calls.

   ![3CX Dashboard.](_images/f97c44de921a899b.jpg)
6. In the **Authentication** section, provide:
   - **Type of Authentication:** `Register/Account based`.
   - **Authentication ID (aka SIP user ID):** your Telnyx account username.
   - **Authentication Password:** your Telnyx account password.

   ![Authentication dashboard on 3CX.](_images/57b141d2cd35fc13.png)
7. In the **Route calls to** section, provide:
   - **Main Trunk number:** the default number (cross-verify with the Telnyx portal).
   - **Destination for calls during the office hours:** based on your requirement.
   - **Destination for calls outside the office hours:** based on your requirement.

   !["Route calls to" section on 3CX.](_images/c7052e225eea6d5a.png)
8. On the **Options** tab:
   - **Require registration for:** `Do not require`.
   - Remove `GSM-FR` from **Assigned Codecs**.
9. Click **Apply**.
10. On the **Outbound Parameters** tab, in **SIP Field**:
    - **Contact User Part:** `Custom Field` (leave the custom value blank).

    ![Outbound procedures field.](_images/ea6dfcbcc4a19821.png)
11. Click **Apply**, then **OK** at the top of the page.
12. The IP trunk is now live.

    ![SIP Trunks section.](_images/520d4eff9d33c299.png)

### Create inbound rules

1. From the left-hand navigation, click **Inbound Rules**.
2. Click **+Add DID Rule**.
3. In the **General** section, provide:
   - **Name:** a meaningful name for the rule.
   - **DID/DDI:** one of the DIDs you provisioned from Telnyx.

   ![Inbound rules section.](_images/798d2c7d44d9c5ce.png)
4. In the **Route calls to** section, provide:
   - **Main Trunk number:** the default number (cross-verify with the Telnyx portal).
   - **Destination for calls during the office hours:** based on your requirement.
   - **Destination for calls outside the office hours:** based on your requirement.

   !["Route calls to" section.](_images/c7052e225eea6d5a.png)

### Create outbound rules

1. From the left-hand navigation, click **Outbound Rules**.
2. Click **+Add**.
3. In the **General** section, provide:
   - **Rule Name:** a meaningful name.

   !["Add outbound rule" section.](_images/5121e05b9b086dbc.png)
4. In the **Apply this rule to these calls** section, provide:
   - **Calls to numbers starting with prefix:** leave empty.
   - **Calls from extension(s):** your extension numbers (e.g. `000`).
   - **Calls to numbers with a length of:** leave empty.

   !["Apply this rule to these calls" section.](_images/ecdf9290b2733687.png)
5. In the **Make outbound calls on** section, configure up to three routes. The first is the primary route; the second and third are backups. For each route, digits can be stripped or added. Strip 0 digits on Route 1 and 1 digit on the remaining two routes.

   This is one of the ways an outbound caller ID can be applied within 3CX. If applied on the outbound route, it applies to all calls through that route.

   !["Make outbound calls on" section.](_images/4bdab2a0eca89da6.png)

   !["User information" section.](_images/d38be91cb38f2c04.png)

   > Before configuring an outbound caller ID, observe these naming conventions:
   > - Use **capital letters** for the Caller ID Name for clearer display on some devices.
   > - Do **not** use special characters.
   > - Some Canadian providers display no more than 15 characters — shorten or adapt your caller ID accordingly.
   > - **Spaces are allowed** in a caller ID name.
   > - Be familiar with [Telnyx's caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy).
   >
   > If you do not add an outbound caller ID on the outbound route, you can apply it per user or extension instead.

6. Click **OK**.

## Epygi IP PBX Setup

The Epygi QX VoIP Carrier Wizard guides you through configuring your account. After completing the wizard, QX extensions can place and receive calls. The wizard supports both IP-based authentication and SIP registration; this guide uses SIP registration.

> This is a generic configuration for all QX models: QX20, QX50, QX200, QX500, QX2000, QX3000, QX5000, QXISDN4+, ecQX, UC20, and UC80.

### Register the Epygi QX device

1. From a computer on the same LAN as the Epygi QX, open a browser and navigate to `http://172.30.0.1`.
2. Log in. Default credentials (update immediately):
   - **Username:** `admin`
   - **Password:** `19`
3. In the left-hand menu, select **Telephony** to open the VoIP carrier wizard:
   - **VoIP Carrier:** `Manual`.
   - **Description:** `Telnyx` (suggested).
4. Click **Next**.

   ![VoIP Carrier Wizard.](_images/c0575928a3ca7a02.png)
5. Configure the carrier settings:
   - **Account Name:** your Telnyx account username.
   - **Password:** your Telnyx account password.
   - **SIP Registrar:** `sip.telnyx.com`.
   - **SIP Server Port:** `5060`.
   - **Use RTP Proxy:** Enabled.
6. Click **Next**.

   ![VoIP Carrier Wizard carrier settings.](_images/565946d7aa7ca511.png)
7. Define call routing:
   - **Access Code:** (e.g. `011`) defines how to make outgoing calls through Telnyx and the QX extension that will receive all incoming calls from Telnyx [SIP trunks](https://telnyx.com/products/sip-trunks).
   - **Emergency code:** (e.g. `911` or `999`) defines where to send emergency calls.
   - **Route Incoming Calls To:** the extension to which all incoming calls will be routed. The default routes to the auto-attendant extension; you may choose another.

   ![VoIP Carrier Wizard access code.](_images/5e8033cdde23f766.png)
8. Click **Next**.
9. Review the settings and click **Finish**.

### Place a call

Reference for typical call patterns:

- **Internal extensions:** dial the extension.
- **External call:** `9` + 10-digit number.
- **Emergency call:** the emergency number configured in the wizard (e.g. `911`).

### Additional features

**Voicemail features**

![Voicemail features section.](_images/793a93e4135c2e25.png)

**Star codes**

![Star codes in the PBX features section.](_images/4b7bb0990bf36150.png)
