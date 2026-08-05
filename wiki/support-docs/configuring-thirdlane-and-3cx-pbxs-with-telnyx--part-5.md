---
title: Configuring Thirdlane and 3CX PBXs with Telnyx
summary: Step-by-step guidance for connecting Thirdlane and 3CX (V18 and V20) IP-PBX
  systems to Telnyx as a SIP trunk provider, including trunk creation, inbound/outbound
  routing, extension setup, and SMS gateway configuration, along with notes on 3CX
  and Telnyx compatibility.
sources:
- url: https://support.telnyx.com/en/articles/1130631-how-to-configure-a-thirdlane-pbx
- url: https://support.telnyx.com/en/articles/6161111-3cx-configuring-a-3cx-v18-pbx
- url: https://support.telnyx.com/en/articles/7829412-3cx-and-telnyx-compatibility
- url: https://support.telnyx.com/en/articles/8683996-3cx-configuring-a-3cx-v20-pbx-20-0-update-5-build-20-0-5-551-march-2025-update
updated_at: 2026-08-05T13:29:24Z
---

# Configuring Thirdlane and 3CX PBXs with Telnyx

*Part 5 of 6 — see also: [Part 1](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-1.md), [Part 2](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-2.md), [Part 3](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-3.md), [Part 4](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-4.md), [Part 6](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-6.md)*

Step-by-step guidance for connecting Thirdlane and 3CX (V18 and V20) IP-PBX systems to Telnyx as a SIP trunk provider, including trunk creation, inbound/outbound routing, extension setup, and SMS gateway configuration, along with notes on 3CX and Telnyx compatibility.

## 3CX V20 PBX Setup (Build 20.0.5.551, March 2025 Update)

### 3CX V20 Pre-requisites

- [Set up and configure your Telnyx Mission Control Portal](https://support.telnyx.com/en/articles/5717957-zoiper-5-pro-telnyx-setup#h_dc5df9cfdf).
- Have created a credentials-based, IP-based, or FQDN-based [SIP connection](https://portal.telnyx.com/#/app/connections) on Telnyx, assigned to DIDs and an outbound profile.
- Have created a [messaging profile](https://portal.telnyx.com/#/app/programmable-messaging/profiles) on Telnyx, assigned to DIDs.
- [Download](https://www.3cx.com/phone-system/download-links/) and [install](https://www.3cx.com/docs/manual/) 3CX.

> **Note:** V20 has an entirely new management console called **Admin Console**, integrated into the 3CX client. Users can switch to the admin console directly from the 3CX client without a separate login or URL.

### Perform the Basic Setup (V20)

The basic setup mirrors V18 (extension length, admin email, timezone, operator, allowed countries, prompt set, registration). See the V18 basic setup section above for details. You can also configure allowed country codes later via **Admin > Advanced > Allowed Country Codes**.

### Confirm Admin > Advanced Settings (V20)

1. Click the admin cog in the bottom-left corner and select **Advanced**.
2. On the **IP Blacklist** tab, allow the appropriate Telnyx [SIP Signaling](https://sip.telnyx.com/#signaling-addresses) and [Media IP Addresses](https://sip.telnyx.com/#media). A `Whitelisted Telnyx IPs.json` file is available at the end of the source article for bulk import.
3. On the **Network** tab:
   - Choose the default internet-facing IP (default gateway) for the **Network Interface Card**.
   - Set the **External IP Configuration** with a static or dynamic IP/FQDN. This is required for your Telnyx [SIP Connection](https://support.telnyx.com/en/articles/4245868-sip-connection-types).
   - Hosted instances have these settings preconfigured.

### Create Users (V20)

1. Click the admin cog and select **Users**.
2. Click **Add User**, enter first and last name on the **General** tab, and click **Save**.

![3CX Admin Console](_images/254deffb8762580c.jpg)

3. The user is assigned an extension (e.g., 101). If an email is included, the user receives an email with account details.

![Account details tab.](_images/33a2d27834e8d5c1.png)

### Create a Telnyx SIP Trunk (V20)

1. Click the admin cog and select **Voice & Chat**.
2. Click **Add SIP Trunk > Add Trunk**.
3. In the pop-up:
   - **Name:** Enter the trunk name.
   - **Default Route:** Defaults to the 3CX Owner; change as needed.
4. Under **VoIP Provider**:
   - **Country:** Select US, Europe, Australia, or Canada.
   - **Provider:** Choose **Generic VoIP Provider**.
5. **Main Trunk Number:** Enter the Telnyx number for your 3CX instance.
6. For credential-based authentication:
   - **Authentication ID:** Trunk username.
   - **Authentication Password:** Trunk password.
7. **Type of Authentication:** **Register/Account Based**.
8. **Server Details:**
   - **Server:** `sip.telnyx.com` (or `sip.telnyx.ca`, `sip.telnyx.com.au`, `sip.telnyx.eu` based on your signaling region).
   - **Port:** `5060`.

![3CX trunk configuration](_images/fba6c2f76961d08c.png)

> **Note:** After configuration, the trunk should appear in green. A warning such as "Untested provider: Quality and reliability not guaranteed" can be safely disregarded.

### Add DIDs (V20)

1. Click the **DID Numbers** tab.

![DID Numbers tab](_images/073d7bd8a78f45bb.png)

2. Import numbers via file or enter them manually. The trunk number is automatically added once you save your first DID. (You cannot add a DID equal to the main trunk number.)

### Configure SMS on the Trunk (V20)

1. Click the **SMS** tab.
2. **Enable Messaging:** Enter your Telnyx API key.
3. **Copy Webhook URL:** Copy from [Telnyx Programmable Messaging Profiles](https://portal.telnyx.com/#/app/programmable-messaging/profiles) and paste into your messaging profile.
4. **Provider URL:** `https://api.telnyx.com/v2/messages`.
5. Click **Save**.
6. Return to **Users** and assign the DID to your user.

![User DID assignment](_images/7b81220f377d4a0c.jpg)

![User with DID assigned](_images/86e8eacf7ee708a5.jpg)

7. Back in **Voice & Chat**, the Telnyx trunk should be registered in green and ready.

### Configure Outbound Rules (V20)

1. Click the **Admin** cog and select **Outbound Rules**.
2. **Calls to numbers starting with prefix:** Leave empty.
3. **Calls from extension(s):** Enter the extension numbers (e.g., `100, 101`).
4. **Calls to Numbers with a length of:** Leave empty.
5. **Make outbound calls on:** Configure up to 5 routes. Route 1 strips 0 digits; Routes 2 and 3 strip 1 digit. Adjust per your dialing needs.
6. **Outbound Caller ID:** Apply here to use it for all calls on this route.

![Outbound Rules section.](_images/ffd41170aab00b86.png)

7. Click **Save**.

### Outbound Call Example (V20)

1. In **Contacts**, create a contact with the number in +E.164 format.

![Contacts section](_images/bc0379dc09e2bcaf.png)

2. Use 3CX's built-in WebRTC calling and click the phone icon. Allow microphone/speaker access.

![WebRTC functionality example](_images/dc27f3cdfd7b16fe.png)

3. 3CX WebRTC may convert `+` to `001` as the international exit code. If you see errors like `Call or Registration to 0017266002345@(Ln.10000@Telnyx LLC) has failed`, add an outbound rule that strips the first two digits (`00`) and replaces them with `+`.

![Advanced -> Event Logs section.](_images/391f133f0a030705.png)

### Outbound Call Important Notes (V20)

- If you do not set an outbound caller ID on the route, apply it at the user level.
- If no caller ID is set, calls may reach Telnyx without one — apply a Caller ID Override from your SIP Connection's outbound options in the Telnyx Portal, or calls will be rejected. See the [caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy).
- 3CX typically requires +E.164 format. Ensure your SIP Connection's inbound [ANI/DNIS number formats](https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats) are set to +E.164 to avoid inbound rejection.
- See [3CX's outbound rules support article](https://www.3cx.com/blog/voip-howto/outbound-rules-a-complete-example/) for more examples.

### Inbound Call Example (V20)

1. For testing, use User extension 100.
2. Download the 3CX iOS app and open it.
3. In the management console, click the **QR Code** icon next to the phone icon in the top-right (or find each user's QR code in the **Users** section).

![User extension 100.](_images/77261cf805a32798.png)

4. In the app, scan the QR code and allow camera access.
5. In **Users**, assign the main trunk number to your user and save.
6. Call the main trunk number — the call should ring on the 3CX app.

![3CX Incoming Call being received on management console](_images/2a1be3ca1e3b2374.jpg)

![Incoming call being received in 3CX mobile app](_images/4c789598074f9fff.jpg)

Missed calls are directed to voicemail, and the user receives an email if one is configured.

### Send and Receive Messages Example (V20)

1. On the mobile app, open **Chats** and click the pencil-square icon.
2. Choose **Compose SMS**.
3. Add user extension 101 as a contact (or allow 3CX to access your phone's contacts).
4. Compose and send the message.

![Compose SMS](_images/85531f1d300fef10.jpg)

5. Messages also appear in the [Messaging Report](https://portal.telnyx.com/#/app/debugging/detail-records-search) section of your Telnyx account.

![Messaging Report](_images/4ae8b9a3b5d78f95.jpg)

6. Log in as user extension 101 in the management console (using the email-received credentials and 2FA) to view and reply to messages.

![3CX fluid conversation](_images/8b09f2368aed6828.jpg)
