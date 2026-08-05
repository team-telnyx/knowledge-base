---
title: Configuring FreePBX with Telnyx Credentials-Based SIP Trunks
summary: This page explains how to configure FreePBX (versions 13, 14, and 15) to
  use Telnyx as a SIP provider with credentials-based authentication, covering both
  ChanSIP and PJSIP channel drivers. It walks through installing FreePBX, configuring
  SIP settings, creating extensions, setting up trunks, and defining inbound and outbound
  routes.
sources:
- url: https://support.telnyx.com/en/articles/1130648-configuring-a-freepbx-v13-credentials-trunk
- url: https://support.telnyx.com/en/articles/1277754-freepbx-v13-pjsip-credentials
- url: https://support.telnyx.com/en/articles/3284752-freepbx-v14-credentials-chansip
- url: https://support.telnyx.com/en/articles/5619597-freepbx-v15-credentials-pjsip
updated_at: 2026-08-05T13:30:16Z
---

# Configuring FreePBX with Telnyx Credentials-Based SIP Trunks

*Part 2 of 4 — see also: [Part 1](configuring-freepbx-with-telnyx-credentials-based-sip-trunks--part-1.md), [Part 3](configuring-freepbx-with-telnyx-credentials-based-sip-trunks--part-3.md), [Part 4](configuring-freepbx-with-telnyx-credentials-based-sip-trunks--part-4.md)*

This page explains how to configure FreePBX (versions 13, 14, and 15) to use Telnyx as a SIP provider with credentials-based authentication, covering both ChanSIP and PJSIP channel drivers. It walks through installing FreePBX, configuring SIP settings, creating extensions, setting up trunks, and defining inbound and outbound routes.

## Configure Extensions

1. Make your way to **Applications → Extensions → Add Extension → Add New Chan SIP Extension** (or **Add New Chan PJSIP Extension** for V15). The **Outbound CID** is the [number you purchased](https://portal.telnyx.com/#/app/numbers/my-numbers) from your Telnyx Mission Control Portal. The extension's secret may need to be populated under the **Other** tab.

   ***Note*** that if you do not set an Outbound CID for your extension, you will need to enable this on your trunk.

   ***Note*** that this device uses CHAN_SIP technology listening on Port 5160 (UDP — this is a NON STANDARD port). For PJSIP, the device uses PJSIP technology listening on Port 5060 (UDP).

   ![SIP Extension settings.](_images/02fd06b118aa7ac1.png)
2. Click **Submit** and **Apply Config**.

For testing purposes, you can now use your SIP client to register with FreePBX using the username, password/secret and local IP address of your FreePBX.
