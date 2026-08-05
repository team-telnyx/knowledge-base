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

*Part 4 of 6 — see also: [Part 1](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-1.md), [Part 2](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-2.md), [Part 3](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-3.md), [Part 5](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-5.md), [Part 6](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-6.md)*

Step-by-step guidance for connecting Thirdlane and 3CX (V18 and V20) IP-PBX systems to Telnyx as a SIP trunk provider, including trunk creation, inbound/outbound routing, extension setup, and SMS gateway configuration, along with notes on 3CX and Telnyx compatibility.

## 3CX V18 PBX Setup

### 3CX V18 Pre-requisites

- [Set up and configure your Telnyx Mission Control Portal](https://support.telnyx.com/en/articles/5717957-zoiper-5-pro-telnyx-setup#h_dc5df9cfdf).
- Have created a credentials-based or IP-based [SIP connection](https://portal.telnyx.com/#/voice/connections) on Telnyx, assigned to a DID and outbound profile.
- Have created a [messaging profile](https://portal.telnyx.com/#/programmable-messaging/profiles) on Telnyx, assigned to a DID.
- [Download](https://www.3cx.com/phone-system/download-links/) and [install](https://www.3cx.com/docs/manual/) 3CX. During installation, 3CX provides a username and password for the web interface.

> **Note:** 3CX detects your public IP and lets you specify whether it is static or dynamic. You can configure 3CX with an FQDN (3CX provides one to ensure it resolves to your public IP and to generate certificates). Choose your default network adapter and decide whether extensions use the local IP or FQDN. Finally, choose your preferred HTTP/HTTPS ports for accessing the 3CX web interface.

### Perform the Basic Setup

1. Log into 3CX with the credentials provided during installation.

![3CX Sign in screen](_images/49fc0a3e188e39f2.png)

2. On the **Extension Length** tab, specify the extension length (default is 3). This cannot be changed later.

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
10. On the **Allowed Countries** tab, select regions permitted for outgoing calls.

![Allowed countries setup](_images/c16effdb5a2378ef.png)

11. Click **Next**.
12. On the **Prompt set** tab, select the language for automated prompts.

![Prompt set selection](_images/c2685775cfd9b22f.png)

13. Click **Next**.
14. On the **Registration** tab, enter your personal details to register your setup.

### Confirm Network Settings

1. Click the **Ports** tab and ensure the SIP port is set to `5060`.
2. Click the **Public IP** tab and verify your public IP and selected network card interface.
3. Click **Settings > Network Settings > Public IP** and ensure the connection IP on the portal matches your static public IP.

### Create a Telnyx SIP Trunk (V18)

1. Click **SIP Trunks** in the left-hand navigation.
2. Click **Import Provider** near the top of the screen.
3. In the pop-up:
   - Upload the `telnyx.pv.xml` file (available at the end of the source article; try incognito mode or another browser if you cannot access it, or contact Telnyx support).
   - Enter the main trunk number.

![Creating the SIP trunk](_images/d4212588dbd8c3b2.png)

4. Click **OK** to open the trunk configuration window.
5. On the **General** tab, under **Trunk Details**:
   - **Enter name of Trunk:** `Telnyx LLC`
   - **Registrar/Server/Gateway Hostname or IP:** `sip-anycast1.telnyx.com:5060` or `sip.telnyx.com:5060`
   - **Outbound Proxy:** Leave blank unless using a proxy.
   - **Number of SIM Calls:** Set your preferred simultaneous call count.

![Number of SIM calls](_images/b7323767118acb5b.png)

6. **Authentication** section:
   - **Register/Account based:**
     - **Authentication ID:** Username from the Telnyx connection.
     - **Authentication Password:** Password from the Telnyx connection.
     - **3 Way Authentication:** Do not enable.

![Authentication section](_images/57b141d2cd35fc13.png)

   - **IP based (Do not require):**
     - Use this to send/receive calls from the public IP of your 3CX instance.
     - Leave **Authentication ID** and **Authentication Password** empty.
     - Do not enable 3 Way Authentication.

7. **Route calls to** section:
   - **Main Trunk number:** Verify against the number purchased on the Telnyx portal.
   - **Destination for calls during office hours / outside office hours:** Set per your requirements.

![Routing calls example](_images/c7052e225eea6d5a.png)

8. Other sub-tabs are pre-populated with Telnyx-recommended settings from the XML file. Click **OK** when satisfied.
9. In the **SMS** sub-tab:
   - **API Key:** Generate at [Telnyx API Keys](https://portal.telnyx.com/#/api-keys) and paste.
   - **Provider URL:** `https://api.telnyx.com/v2/messages`
   - **Copy webhook URL:** Copy from [Telnyx Programmable Messaging Profiles](https://portal.telnyx.com/#/programmable-messaging/profiles) and paste into your messaging profile.

![Copying webhook URL](_images/f472da8798c3951d.png)

10. Click **OK**. Your Telnyx trunk is now live.

![Confirmation SIP trunk is live](_images/520d4eff9d33c299.png)

### Configure Inbound Rule (V18)

1. Click **Inbound Rules** in the left navigation.
2. Click **+Add DID Rule**.
3. **General** section:
   - **Name:** `IB_Telnyx` (or any identifying name).

![Configuring inbound rule](_images/e9ba986026e805cb.png)

4. **Route calls to** section:
   - **Destination for calls during office hours:** `Extension` and select your desired extension (commonly `000`).

![Routing calls view](_images/53a09717d8ad937a.png)

### Configure Outbound Rule (V18)

1. Click **Outbound Rules** in the left navigation.
2. Click **+Add**.
3. **General** section:
   - **Name:** `OB_Telnyx` (or any identifying name).

![Configure outbound rule](_images/5121e05b9b086dbc.png)

4. **Apply this rule to these calls** section:
   - **Calls to numbers starting with prefix:** Leave empty.
   - **Calls from extension(s):** Enter the extension numbers (e.g., `000`).
   - **Calls to Numbers with a length of:** Leave empty.

![Applying rules to calls](_images/ecdf9290b2733687.png)

5. **Make outbound calls on:** Configure up to 3 routes. Strip 0 digits on Route 1 and 1 digit on Routes 2 and 3. Apply an outbound caller ID here to apply it to all calls on this route.

![Outbound call routing](_images/ee0936a031c45464.png)

> **Note:** If you do not set an outbound caller ID on the route, you can apply it per user/extension. If no caller ID is set, calls may reach Telnyx without one — apply a Caller ID Override from your SIP Connection's outbound options in the Telnyx Portal, or calls will be rejected. See the [caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy).

![User information section](_images/04f247d3750b4881.png)

For more on dialing format rules, see [3CX's outbound rules guide](https://www.3cx.com/blog/voip-howto/outbound-rules-a-complete-example/). Click **OK** when finished.

### Outbound Rule Example: 911 Emergency Calls

The outbound rule feature supports complex routing, including backup routes and number-type-specific routing. Example for 911:

![General outbound rule example](_images/e179bafbbb8bc8e0.png)

![Applying rules to calls](_images/b4656299a564c3bd.png)

![Making outbound calls on specific routes](_images/8a5ed7ff003bef44.png)

See [3CX's outbound rules support article](https://www.3cx.com/blog/voip-howto/outbound-rules-a-complete-example/) for additional examples.

### Configure Extension for Messaging (V18)

1. In the **Users** section, add or edit an extension (e.g., 101) associated with one of your configured DIDs.

![Configuring extensions](_images/f23b27b104c4339d.png)

2. On the **General** tab, scroll to the bottom and assign the DID to the extension. (In V18 Update 5 and later, you no longer need to enable SMS on the associated DID separately.)

![Web authentication and DIDs](_images/6002d671302a01f9.png)

3. Click **OK** at the top of the page to make inbound and messaging live for the extension.

### Test the 3CX Webclient (V18)

1. During initial setup, you received an email from 3CX with a link to the webclient and the extension's username and password.
2. Visit the link and log in.
3. In the **Contacts** section, click the `+` icon to add a contact (name and mobile number), then save.

![Native 3CX client](_images/e34163097c6144da.png)

4. In the **Chat** section, click `+` then **Send SMS**.

![Sending SMS](_images/c90322766beb93ed.png)

5. Choose the contact, type your message, and press Enter.

![Choosing a contact](_images/e627cda8a9a5cd68.png)

6. Replies appear in the chat.

![Receiving a response](_images/809bbdd66945ce7d.png)
