---
title: Configuring Thirdlane and 3CX PBXs with Telnyx
summary: This page covers how to configure Telnyx as a SIP provider for Thirdlane
  and 3CX (V18 and V20) PBX systems, including trunk creation, inbound/outbound routing,
  caller ID, SMS gateway setup, and compatibility considerations between 3CX and Telnyx.
sources:
- url: https://support.telnyx.com/en/articles/1130631-how-to-configure-a-thirdlane-pbx
- url: https://support.telnyx.com/en/articles/6161111-3cx-configuring-a-3cx-v18-pbx
- url: https://support.telnyx.com/en/articles/7829412-3cx-and-telnyx-compatibility
- url: https://support.telnyx.com/en/articles/8683996-3cx-configuring-a-3cx-v20-pbx-20-0-update-5-build-20-0-5-551-march-2025-update
updated_at: 2026-07-17T09:04:30Z
---

# Configuring Thirdlane and 3CX PBXs with Telnyx

*Part 4 of 6 — see also: [Part 1](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-1.md), [Part 2](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-2.md), [Part 3](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-3.md), [Part 5](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-5.md), [Part 6](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-6.md)*

This page covers how to configure Telnyx as a SIP provider for Thirdlane and 3CX (V18 and V20) PBX systems, including trunk creation, inbound/outbound routing, caller ID, SMS gateway setup, and compatibility considerations between 3CX and Telnyx.

## 3CX V18 PBX Configuration

### Pre-requisites

- [Set up and configure your Telnyx Mission Control Portal](https://support.telnyx.com/en/articles/5717957-zoiper-5-pro-telnyx-setup#h_dc5df9cfdf)
- Create a credentials-based or IP-based [SIP connection](https://portal.telnyx.com/#/voice/connections) on your Telnyx Mission Control Portal account, assigned to a DID and outbound profile
- Create a [messaging profile](https://portal.telnyx.com/#/programmable-messaging/profiles) on your Telnyx Mission Control Portal account, assigned to a DID
- [Download](https://www.3cx.com/phone-system/download-links/) and [install](https://www.3cx.com/docs/manual/) 3CX. During installation, 3CX provides a username and password for the web interface.

> **Note:** 3CX detects your public IP address and you can specify whether it is static or dynamic. You can configure 3CX with an FQDN (3CX provides one to ensure it resolves to your public IP and for generating certificates). You'll choose your default network adapter and decide whether extensions use the local IP of your PBX or the FQDN. At the end, choose your preferred HTTP/HTTPS port numbers for accessing the 3CX web interface via your FQDN or public IP.

### Basic Setup

1. Log into 3CX with the credentials provided during installation.

![3CX Sign in screen](_images/49fc0a3e188e39f2.png)

2. On the **Extension Length** tab, specify your extension length (default is 3). This **cannot** be changed later.

![Extension length tab](_images/4a43d9f7f30080bf.png)

3. Click **Next**.
4. On the **Admin Email** tab, enter an email for system notifications.

![admin email tab](_images/76a101991e81e556.png)

5. Click **Next**.
6. On the **Timezone** tab, set your timezone.

![timezone tab](_images/b974c9dc2da69f2b.png)

7. Click **Next**.
8. On the **Operator** tab, specify a default operator extension (default destination for inbound calls and voicemail).

![operator tab](_images/931880e6406ab3a9.png)

9. Click **Next**.
10. On the **Allowed Countries** tab, select all regions permitted for outgoing calls.

![Allowed countries setup](_images/c16effdb5a2378ef.png)

11. Click **Next**.
12. On the **Prompt set** tab, select the language for automated prompts.

![Prompt set selection](_images/c2685775cfd9b22f.png)

13. Click **Next**.
14. On the **Registration** tab, enter your personal details to register your setup.

### Configure Network Settings

1. Click the **Ports** tab and ensure your SIP port is set to `5060`.
2. Click the **Public IP** tab and ensure your public IP is correct and the proper network card interface is selected.
3. Click the **Settings** tab, then **Network Settings**, then the **Public IP** tab. In the **External IP Configuration** section, ensure the connection IP on the portal matches the static public IP.

### Create a Telnyx SIP Trunk

1. Click **SIP Trunks** in the left-hand navigation menu.
2. Click **Import Provider** near the top of the screen.
3. In the pop-up:
   - Upload the `telnyx.pv.xml` file (attached at the end of the source article). If you can't access it, try incognito mode, clear cache/cookies, or contact Telnyx support.
   - Enter the main trunk number.

![Creating the SIP trunk](_images/d4212588dbd8c3b2.png)

4. Click **OK** to open the trunk configuration window.
5. On the **General** tab, find **Trunk Details**:
   - **Enter name of Trunk:** `Telnyx LLC`
   - **Registrar/Server/Gateway Hostname or IP:** `sip-anycast1.telnyx.com:5060` or `sip.telnyx.com:5060`
   - **Outbound Proxy:** Leave blank unless using a proxy
   - **Number of SIM Calls:** Set your preferred simultaneous call count

![Number of SIM calls](_images/b7323767118acb5b.png)

6. **Authentication** section:
   - **Register/Account based:**
     - **Authentication ID:** Username from the connection created in the Telnyx portal
     - **Authentication Password:** Password from the connection created in the Telnyx portal
     - **3 Way Authentication:** Do not enable

![Authentication section](_images/57b141d2cd35fc13.png)

   - **Do not require - IP based:**
     - Select this option to send/receive calls from the public IP of your 3CX instance
     - **Authentication ID:** Leave empty
     - **Authentication Password:** Leave empty
     - **3 Way Authentication:** Do not enable

7. **Route calls to** section:
   - **Main Trunk number:** Cross-verify with the number purchased on the Telnyx portal
   - **Destination for calls during office hours:** Based on your requirement
   - **Destination for calls outside office hours:** Based on your requirement

![Routing calls example](_images/c7052e225eea6d5a.png)

8. Other sub-tabs are pre-populated with Telnyx-recommended settings from the XML file. Click **OK** when satisfied.
9. The **SMS sub tab** is also pre-populated:
   - **API Key:** Generate at [Telnyx API Keys](https://portal.telnyx.com/#/api-keys) and paste in
   - **Provider URL:** `https://api.telnyx.com/v2/messages`
   - **Copy webhook URL:** Copy from [Telnyx Programmable Messaging Profiles](https://portal.telnyx.com/#/programmable-messaging/profiles) and paste into your messaging profile to allow inbound and outbound messaging

![Copying webhook URL](_images/f472da8798c3951d.png)

10. Click **OK**. Your Telnyx trunk is now live.

![Confirmation SIP trunk is live](_images/520d4eff9d33c299.png)

### Configure Inbound Rule

1. Click **Inbound Rules** in the left navigation menu.
2. Click **+Add DID Rule** near the top of the screen.
3. In the **General** section:
   - **Name:** `IB_Telnyx` (or any identifying name)

![Configuring inbound rule](_images/e9ba986026e805cb.png)

4. In the **Route calls to** section:
   - **Destination for calls during office hours:** `Extension` and select your desired extension (usually `000`)

![Routing calls view](_images/53a09717d8ad937a.png)

### Configure Outbound Rule

1. Click **Outbound Rules** in the left navigation menu.
2. Click **+Add** near the top of the screen.
3. In the **General** section:
   - **Name:** `OB_Telnyx` (or any identifying name)

![Configure outbound rule](_images/5121e05b9b086dbc.png)

4. In the **Apply this rule to these calls** section:
   - **Calls to numbers starting with prefix:** Leave empty
   - **Calls from extension(s):** Enter the extension numbers (e.g., `000`)
   - **Calls to Numbers with a length of:** Leave empty

![Applying rules to calls](_images/ecdf9290b2733687.png)

5. In the **Make outbound calls on** section, configure up to 3 routes (the second and third are backups). For each route, digits can be stripped or added. Strip 0 digits on Route 1 and strip 1 digit for the remaining 2 routes.

This is also one of the ways an outbound caller ID can be applied within 3CX. If applied to the outbound route, it applies to all calls through that route.

![Outbound call routing](_images/ee0936a031c45464.png)

> **Note:** If you don't add an outbound caller ID on the outbound route, you can apply it per user or extension. If a caller ID is not set through 3CX, calls may reach Telnyx without a caller ID. In that case, apply a Caller ID Override from your SIP Connection's outbound options in the Telnyx Portal, otherwise calls will be rejected. See the [caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy) for accepted formats.

![User information section](_images/04f247d3750b4881.png)

For specific dialing format rules, see 3CX's [outbound rules overview](https://www.3cx.com/blog/voip-howto/outbound-rules-a-complete-example/). Click **OK** when finished.

### Outbound Rule Example: 911 Emergency Calls

The outbound rule feature in 3CX allows complex rules, including backup routes and different route sets depending on the type of number being dialed. Example for 911 emergency calls:

![General outbound rule example](_images/e179bafbbb8bc8e0.png)

![Applying rules to calls](_images/b4656299a564c3bd.png)

![Making outbound calls on specific routes](_images/8a5ed7ff003bef44.png)

For additional outbound rule examples, see 3CX's [support article](https://www.3cx.com/blog/voip-howto/outbound-rules-a-complete-example/).

### Configure Extension for Inbound and Outbound Messaging

1. An existing extension/user is created during initial setup. Visit the **Users** section to add more or edit existing extensions.
2. Click into an extension (e.g., 101) to enable messaging on the extension associated with one of the numbers configured in inbound routes.

![Configuring extensions](_images/f23b27b104c4339d.png)

3. On the **General** tab, scroll to the end and assign the DID to the extension. **Previously in V18 Update 5 you would have had to enable SMS on the associated DID, but this is no longer a requirement.**

![Web authentication and DIDs](_images/6002d671302a01f9.png)

4. Click **OK** at the top of the page to make inbound and messaging live for the extension.

### Access 3CX Native WebClient

1. During extension creation, you receive an email from 3CX titled "Your User Account on your New 3CX System" with a link to the webclient and the extension's username and password.
2. Visit the link and log in. This web app is used for making and receiving calls/SMS for each extension.
3. Once logged in, visit the **Contacts** section:
   - Click the `+` icon to add a contact
   - Enter the name and mobile number
   - Click the save icon on the top right

![Native 3CX client](_images/e34163097c6144da.png)

4. Visit the **Chat** section:
   - Click the `+` symbol, then **Send SMS**

![Sending SMS](_images/c90322766beb93ed.png)

   - Choose the contact to send an SMS to

![Choosing a contact](_images/e627cda8a9a5cd68.png)

   - Type your message and press Enter to send
   - The destination's response appears in the chat

![Receiving a response](_images/809bbdd66945ce7d.png)
