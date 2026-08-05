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

*Part 4 of 4 — see also: [Part 1](configuring-freepbx-with-telnyx-credentials-based-sip-trunks--part-1.md), [Part 2](configuring-freepbx-with-telnyx-credentials-based-sip-trunks--part-2.md), [Part 3](configuring-freepbx-with-telnyx-credentials-based-sip-trunks--part-3.md)*

This page explains how to configure FreePBX (versions 13, 14, and 15) to use Telnyx as a SIP provider with credentials-based authentication, covering both ChanSIP and PJSIP channel drivers. It walks through installing FreePBX, configuring SIP settings, creating extensions, setting up trunks, and defining inbound and outbound routes.

## Configure Outbound Routes

Outbound routing is a set of rules that tells FreePBX which Telnyx trunk to use for any given outbound call. Having multiple trunks allows you to control cost by routing calls over the least costly trunk for a particular call. Outbound routes are used to specify what numbers are allowed to go out a particular route.

You will want to make sure you define routes for all types of calls. Not defining a route can leave your users frustrated when they need to make an important call.

1. Navigate to **Connectivity → Outbound Routes**.
2. Create a new outbound route and provide the following on the **Route Settings** tab:
   - **Route Name:** Something distinct that makes sense for your route purpose (e.g., *Outbound_Telnyx*).
   - **Route CID:** Number you purchased on the Telnyx portal.
   - **Trunk Sequence for Matched Routes:** Select the Telnyx trunk you just created.

   ![Outbound routes configuration tab 1.](_images/03a0db6e3b8b108c.png)
3. Now select the **Dial Patterns** tab to the right of the **Route Settings** tab and enter dial patterns exactly as you see in the following image. This pattern allows you to dial 10 Digits (U.S. Calling), 11 Digits (North American Calling).

   *If you need dial patterns for a region outside North America, please contact Telnyx support.*

   ![Inbound routes configuration tab.](_images/b1b53778bd839984.png)

   ***Note*** that our current documentation portal shrinks screenshots, making some detail difficult to see. Right-click on the image above and select "Open image in new tab" from the context menu. This will open the image in a new tab and display it at its full size and resolution.

4. Click **Submit**, then **Apply Config**.

## Configure Inbound Routes

When a call comes in from the outside, it'll need to be directed from sip.telnyx.com to the phone extension you ultimately want it to go, such as a user extension or an IVR extension.

1. Make your way to **Connectivity → Inbound Routes** and open the **General** tab.
2. The following image demonstrates an inbound route that will send *ANY* call to a certain extension.

   To direct a specific number to a specific extension you would create a route and set the "[DID Number](https://telnyx.com/resources/sip-did)" field to your 11 digit DID with sip.telnyx.com (for instance: 12172031700).

   ![Inbound routes configuration tab.](_images/1a1b59fcbfca0746.png)
3. Enter the route name description, DID associated with this route and specify the **extension** that should be associated when calls are received to the DID.
4. Click **Submit** and **Apply Config**.

***Note:*** *By default, when creating a SIP Connection in the Telnyx Mission Control Portal, the number formats for the ANI and DNIS will be set to E.164. This means Telnyx will send the dialled number in the SIP INVITE to your FreePBX system with 11 digits. As the DID number above is in 11 digit format, the call will be accepted and routed to the extension. However, you can control the number formats as you desire and can read more about it [here](https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats).*

That's it, you've now completed the configuration of FreePBX with a Telnyx Credentials Trunk and can now make and receive calls by using Telnyx as your SIP provider.

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally, you can check out:
- [FreePBX documentation](https://wiki.freepbx.org/#all-updates)
- [FreePBX community](https://community.freepbx.org/)
- [FreePBX support](https://www.freepbx.org/support/)
- [FreePBX videos](https://www.freepbx.org/videos/)
