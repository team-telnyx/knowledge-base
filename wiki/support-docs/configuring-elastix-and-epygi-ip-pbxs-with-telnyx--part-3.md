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

*Part 3 of 5 — see also: [Part 1](configuring-elastix-and-epygi-ip-pbxs-with-telnyx--part-1.md), [Part 2](configuring-elastix-and-epygi-ip-pbxs-with-telnyx--part-2.md), [Part 4](configuring-elastix-and-epygi-ip-pbxs-with-telnyx--part-4.md), [Part 5](configuring-elastix-and-epygi-ip-pbxs-with-telnyx--part-5.md)*

This page consolidates Telnyx support documentation for configuring Elastix 4 (IP and credentials trunks), Elastix 5 (FQDN and credentials trunks), and Epygi QX-series IP PBXs to interoperate with Telnyx as a SIP provider. It covers prerequisites, installation, SIP trunk creation, and inbound/outbound routing for each platform.

## Elastix 5 FQDN Trunk

Use this configuration when authenticating the Elastix 5 PBX to Telnyx by IP or FQDN rather than by SIP credentials.

### Create a Telnyx SIP trunk

1. From the left-hand navigation, click **SIP Trunks**.
2. Click **+ Add SIP Trunk**.
3. In the pop-up, enter:
   - **Select Country:** `Worldwide`.
   - **Select Provider in your Country:** `Telnyx LLC`.
   - **Main Trunk No:** the [Telnyx number](https://portal.telnyx.com/#/app/numbers/my-numbers) you purchased.

   ![SIP Trunk/VoIP Provider tab.](_images/2e0700ca6ed799ee.png)
4. Click **OK** to open the trunk configuration window.
5. On the **General** tab, in **Trunk Details**, provide:
   - **Enter name of Trunk:** `Telnyx LLC`.
   - **Registrar/Server/Gateway Hostname or IP:** `sip-anycast1.telnyx.com:5060` or `sip.telnyx.com:5060`.
   - **Outbound Proxy:** `sip.telnyx.com`.
   - **Number of SIM Calls:** your preferred number of simultaneous calls.

   ![Trunk configuration window.](_images/f97c44de921a899b.jpg)
6. In the **Authentication** section, provide:
   - **Type of Authentication:** `Do not require - IP Based`.
   - **Authentication ID (aka SIP user ID):** the [Telnyx number](https://portal.telnyx.com/#/app/numbers/my-numbers) you purchased.
   - **Authentication Password:** leave blank.

   ![Authentication section in 3CX.](_images/57b141d2cd35fc13.png)
7. In the **Route calls to** section, provide:
   - **Main Trunk number:** the default number (cross-verify with the Telnyx portal).
   - **Destination for calls during the office hours:** based on your requirement.
   - **Destination for calls outside the office hours:** based on your requirement.

   !["Route Calls To" section.](_images/c7052e225eea6d5a.png)
8. On the **Options** tab:
   - **Require registration for:** `Do not require`.
   - Remove `GSM-FR` from **Assigned Codecs**.
9. Click **Apply**.
10. On the **Outbound Parameters** tab, in **SIP Field**:
    - **Contact User Part:** `Custom Field` (leave the custom value blank).

    ![Options tab of the setup.](_images/ea6dfcbcc4a19821.png)
11. Click **Apply**, then **OK** at the top of the page.
12. The IP trunk is now live.

    ![Live IP trunk dashboard.](_images/520d4eff9d33c299.png)

### Create inbound rules

1. From the left-hand navigation, click **Inbound Rules**.
2. Click **+Add DID Rule**.
3. In the **General** section, provide:
   - **Name:** a meaningful name for the rule.
   - **DID/DDI:** one of the DIDs you provisioned from Telnyx.

   ![Inbound Rules settings section.](_images/798d2c7d44d9c5ce.png)
4. In the **Route calls to** section, provide:
   - **Main Trunk number:** the default number (cross-verify with the Telnyx portal).
   - **Destination for calls during the office hours:** based on your requirement.
   - **Destination for calls outside the office hours:** based on your requirement.

   !["Route Calls To" section.](_images/c7052e225eea6d5a.png)

### Create outbound rules

1. From the left-hand navigation, click **Outbound Rules**.
2. Click **+Add**.
3. In the **General** section, provide:
   - **Rule Name:** a meaningful name.

   !["Create Outbound Rules" section.](_images/5121e05b9b086dbc.png)
4. In the **Apply this rule to these calls** section, provide:
   - **Calls to numbers starting with prefix:** leave empty.
   - **Calls from extension(s):** your extension numbers (e.g. `000`).
   - **Calls to numbers with a length of:** leave empty.

   !["Apply this rule to these calls" section.](_images/ecdf9290b2733687.png)
5. In the **Make outbound calls on** section, configure up to three routes. The first is the primary route; the second and third are backups. For each route, digits can be stripped or added. Strip 0 digits on Route 1 and 1 digit on the remaining two routes.

   This is one of the ways an outbound caller ID can be applied within 3CX. If applied on the outbound route, it applies to all calls through that route.

   !["Make outbound calls" section.](_images/4bdab2a0eca89da6.png)

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
