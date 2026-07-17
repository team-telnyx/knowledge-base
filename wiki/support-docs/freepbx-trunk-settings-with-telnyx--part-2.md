---
title: FreePBX Trunk Settings With Telnyx
summary: This page explains how to configure FreePBX (V13, V14, and V15) IP trunks
  with Telnyx using either Chan_SIP or PJSIP, covering installation, basic settings,
  SIP configuration, extensions, trunk setup, outbound and inbound routing, and Telnyx
  Noise Suppression options for SIP connections.
sources:
- url: https://support.telnyx.com/en/articles/1130620-freepbx-trunk-settings-with-telnyx
- url: https://support.telnyx.com/en/articles/3284736-freepbx-v14-ip-trunk-chansip
- url: https://support.telnyx.com/en/articles/5467232-freepbx-v15-ip-trunk-chansip-tutorial
- url: https://support.telnyx.com/en/articles/5619595-freepbx-v15-ip-trunk-pjsip
- url: https://support.telnyx.com/en/articles/9260287-key-configuration-notes-for-noise-suppression
updated_at: 2026-07-17T09:02:55Z
---

# FreePBX Trunk Settings With Telnyx

*Part 2 of 3 — see also: [Part 1](freepbx-trunk-settings-with-telnyx--part-1.md), [Part 3](freepbx-trunk-settings-with-telnyx--part-3.md)*

This page explains how to configure FreePBX (V13, V14, and V15) IP trunks with Telnyx using either Chan_SIP or PJSIP, covering installation, basic settings, SIP configuration, extensions, trunk setup, outbound and inbound routing, and Telnyx Noise Suppression options for SIP connections.

## Configure a Trunk

### Chan_SIP Trunk

1. Make your way to **Connectivity → Trunks → Add Trunk → Add New Chan SIP Trunk**. You'll now be located in the **General** tab.
2. Enter a Trunk name, your Outbound CID, and the maximum channels you'd like for this trunk.

   ![General tab interface for FreePBX configuration.](_images/55bc20917d2a241a.png)

   > **Note:** If you choose not to set an Outbound CID on your trunk, then you must set an Outbound CID on each relevant extension. If you do not set a caller ID on either the trunk or each extension, then your calls will reach our SIP proxy without a valid caller ID. You may instead choose to enable a Caller ID Override in your SIP Connection's Outbound Options from within the Telnyx Portal. Please review the [caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy) for accepted formats.

3. Proceed to the **Dialed Number Manipulation Rules** tab. Depending on your use case, use the simple dial patterns below.

   ![Dialed Number Manipulation Rules tab.](_images/c9ac27ed3e566a0b.png)

   **For US numbers:**
   1. prepend: `1`; match pattern: `NXXNXXXXXX`
   2. prepend: blank; match pattern: `1NXXNXXXXXX`

   **International:**
   1. prepend: Country Dialing prefix; match pattern: `NXXNXXXXXX`
   2. prepend: blank; match pattern: (Country Dialing prefix)`NXXNXXXXXX`

### PJSIP Trunk

1. Make your way to **Connectivity → Trunks → Add Trunk → Add New PJSIP Trunk**. You'll now be located in the **General** tab.
2. Enter a Trunk name, your Outbound CID, and the maximum channels you'd like for this trunk.

   ![Trunk editing page.](_images/61547513dae684da.png)

   > **Note:** If you choose not to set an Outbound CID on your trunk, then you must set an Outbound CID on each relevant extension. If you do not set a caller ID on either the trunk or each extension, then your calls will reach our SIP proxy without a valid caller ID. You may instead choose to enable a Caller ID Override in your SIP Connection's Outbound Options from within the Telnyx Portal. Please review the [caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy) for accepted formats.

3. Proceed to the **Dialed Number Manipulation Rules** tab. Depending on your use case, use the simple dial patterns below.

   ![Trunk Addition page.](_images/95b70071373bfb13.png)

   **For US numbers:**
   1. prepend: `1`; match pattern: `NXXNXXXXXX`
   2. prepend: blank; match pattern: `1NXXNXXXXXX`

   **International:**
   1. prepend: Country Dialing prefix; match pattern: `NXXNXXXXXX`
   2. prepend: blank; match pattern: (Country Dialing prefix)`NXXNXXXXXX`

## Configure Outbound and Inbound SIP Settings (Chan_SIP)

1. Still in the **Add Trunk** configuration tool, click on the **SIP Settings** tab and click on the **Outgoing** sub-tab. Specify:

   1. **type:** `friend`
   2. **qualify:** `yes`
   3. **insecure:** `port,invite`
   4. **host:** `sip.telnyx.com`
   5. **fromdomain:** `sip.telnyx.com`
   6. **disallow:** `all`
   7. **allow:** `ulaw`

   ![Add Trunk configuration interface.](_images/4e94976263b44777.png)

2. Now click on the **Incoming** sub-tab. Specify:

   1. **type:** `friend`
   2. **insecure:** `port,invite`
   3. **host:** `sip.telnyx.com`
   4. **dtmfmode:** `rfc2833`
   5. **disallow:** `all`
   6. **allow:** `ulaw`

   ![Incoming sub-tab interface.](_images/cd94128f1351ae95.png)

## Configure PJSIP Outbound Settings

![PJSIP settings in the trunk editing section.](_images/4f9b661b6021bab5.png)

1. Since you have created an IP-based SIP Connection in your Mission Control Portal account, no registration details are required. Specify:

   1. **Registration** — Select None.
   2. **SIP Server** — your preferred Telnyx SIP Proxy (`sip.telnyx.com` for USA).
   3. **SIP Server Port** — port 5060.

2. Click **Submit** and **Apply Config**.

3. You might see a warning: "This trunk is not used by any routes! This trunk will not be able to be used for outbound calls until a route is setup that uses it."

4. Click on **Outbound Routes** to set up routing.

## Configure Outbound Routing

1. Make your way to **Connectivity → Outbound Routes → Add Outbound Route**.
2. Enter the route name, route CID, and specify the Telnyx_IP trunk for this outbound route.

   ![Outbound Route configuration interface.](_images/620aef9e095761aa.png)

   ![Outbound routes section.](_images/34e92c720bf73f3a.png)

3. In **Route Settings**:

   1. Set the route name.
   2. Ensure the Telnyx Trunk is selected for the trunk sequence.

   ![Outbound routes for Telnyx trunk.](_images/53c0f62d4ea72728.png)

4. In **Dial Patterns**, use the dial pattern wizards to make all the dial patterns that apply to you.

   ![Dial patterns for Telnyx.](_images/7b531459708344c2.png)

5. Click **Generate Routes**, **Submit**, and **Apply Config**.

## Configure Inbound Routing

1. Make your way to **Connectivity → Inbound Routes → Add Inbound Route**.
2. Enter the route name description, DID associated with this route, and specify the extension that should be associated when calls are received to the DID.

   ![Inbound routes for incoming routes.](_images/8f92e36017b18b47.png)

3. Click **Submit** and **Apply Config**.

> **Note:** By default, when creating a SIP Connection in the Telnyx Mission Control Portal, the number formats for the ANI and DNIS will be set to E.164. This means Telnyx will send the dialled number in the SIP INVITE to your FreePBX system with 11 digits. As the [DID number](https://telnyx.com/resources/sip-did) above is in 11-digit format, the call will be accepted and routed to the extension. However, you can control the number formats as you desire — see [SIP Connection Number Formats](https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats) for more information.
