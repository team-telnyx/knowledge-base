---
source_url: https://support.telnyx.com/en/articles/1130648-configuring-a-freepbx-v13-credentials-trunk
scraped: 2026-07-08
content_hash: f77bfd1e316e5148dc2fbc85c8201b0393d964c1b99964c54790f38dc771b1b0
---

Configuring a FreePBX V13 Credentials Trunk | Telnyx Help Center

[Skip to main content](#main-content)

# Configuring a FreePBX V13 Credentials Trunk

In this article we will explain how to configure a FreePBX V13 Credentials trunk with Telnyx.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_17c13cc9ea)

[FreePBX](https://www.freepbx.org/) is a web-based open source GUI (graphical user interface) that controls and manages Asterisk (PBX), an open source communication server. FreePBX is licensed under the GNU General Public License (GPL), an open source license. FreePBX can be installed manually or as part of the pre-configured FreePBX Distro that includes the system OS, Asterisk, FreePBX GUI and assorted dependencies.

You'll need to have created a [Credentials based connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal account, assigned this connection to a DID and outbound profile in order to make and receive calls.

Additional documentation and resources:

* [FreePBX documentation](https://wiki.freepbx.org/#all-updates) (This is useful for any configuration instructions that don't involve Telnyx and are maintained solely by FreePBX)
* [FreePBX community](https://community.freepbx.org/)
* [FreePBX support](https://www.freepbx.org/support/)
* [FreePBX videos](https://www.freepbx.org/videos/)

---

# Instructions to Configure a FreePBX ChanSIP V13

|  |
| --- |
| ***Note:*** *By default, when creating a SIP Connection in the Telnyx Mission Control Portal, the number formats for the ANI and DNIS will be set to E.164. This means Telnyx will send the dialled number in the SIP INVITE to your FreePBX system with 11 digits. As the DID number above is in 11 digit format, the call will be accepted and routed to the extension. However, you can control the number formats as you desire and can read more about it [here](https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats).* |

In this activity you will:

1. [Install FreePBX](#h_ea2f45011a) (You can also follow [instructions provided by FreePBX](https://www.freepbx.org/get-started/))
2. [Configure your SIP trunk](#h_fcc442afae)
3. [Configure outbound routes](#h_dd9fe089e1)
4. [Configure inbound routes](#h_517263a05b)

**Pre-requisites**

* [Set up and configure your Telnyx Mission Control Portal](https://support.telnyx.com/en/articles/5717957-zoiper-5-pro-telnyx-setup#h_dc5df9cfdf)
* Have created a [credentials based connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal account, assigned this connection to a DID and outbound profile in order to make and receive calls.
* [Download](https://www.freepbx.org/downloads/) and [install](https://www.freepbx.org/get-started/) FreePBX. You can also see [our installation guide](#h_ea2f45011a) below.
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)

**Video walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

Configuring your Telnyx SIP trunk with FreePBX

## 1. Install FreePBX

Once you've loaded the FreePBX ISO onto your server or virtual machine, you'll have a few options to select for installation. We'll be doing a full install via asterisk 13. So go ahead and run the installer.

### **Steps:**

1. #### Select **Full Install**.

   ![FreePBX installation portal. ](_images/9bb9534c01512c79.png)
2. #### Confirm your network settings.

   ![Network settings confirmation portal. ](_images/521980f2990f58e4.png)
3. #### Confirm your **root** password.

   ![Root password confirmation portal. ](_images/7fd40a8757cf47ea.png)
4. #### Wait for all the necessary packages to be installed.

   ![Package installation interface. ](_images/4e9f624cbc7e062e.png)
5. #### More modules will be updated after successful internet tests.

   ![Internet test portal for modules uploads. ](_images/b48a8e70d4370eca.png)
6. #### Enter **root** and the password you created from step 2.

   ![Local host credential input interface. ](_images/7ca4ee3478ff63d8.png)

   ####
7. #### You'll now be provided with the URL to access the FreePBX web interface.

   ![A picture showing URL provision for FreePBX access. ](_images/a58d723836f225b2.png)
8. #### You'll be brought to the initial setup and must enter in the username, password and admin email address to create your account.

   ![Account creation portal. ](_images/47c0dbc8e27d4323.png)
9. #### Once you've created your account, you'll be brought to the dashboard. Select **FreePBX Administration,** enter your username and password.

   ![FreePBX administration credentials portal. ](_images/1ee60f283a09fce4.png)
10. #### Follow the process to activate your FreePBX V13.

    ![FreePBX activation interface. ](_images/7845b20c6aa50373.png)
11. #### Select your default locales.

    ![default locale selection page. ](_images/37dbf640f658de04.png)

    ####
12. #### You'll be presented with some firewall details and other suggestions. You are welcome to set this up based on your requirements.

[Back to Top](#h_17c13cc9ea)

## 2. Configure your SIP trunk

In this section, you'll set up and configure your [SIP trunk](https://telnyx.com/products/sip-trunks) and connect Telnyx to FreePBX.  
​

### **Tab: General SIP Settings**

1. Make your way to **Settings > Asterisk SIP Settings** in order to confirm your network settings.
2. You'll want to ensure you populate the **external** and **local** network addresses under **General SIP Settings** and **Chan SIP Settings**.
3. Once you've completed this, click **Submit** and then **Apply Config.**

   ![General SIP settings interface 1. ](_images/55db9cb34da2bcff.png)
4. Now go to **Applications -> Extensions > Add Extension > Add New Chan SIP Extension.** The **Outbound CID** is the [number you purchased](https://portal.telnyx.com/#/app/numbers/my-numbers) from your Telnyx Mission Control Portal. The extensions secret may need to be populated under the **Other** tab.  
   ​  
   ​***Note that*** *if you do not set an Outbound CID for your Extension, you must enable this on your trunk. See the [Pre-requisites](#h_534d80f29a) section.*  
   ​  
   ​***Note:*** *This device uses CHAN\_SIP technology listening on Port 5160 (UDP - this is a NON STANDARD port).*  
   ​
5. Click **Submit** and **Apply Config.**

   ![General SIP settings interface 2. ](_images/02fd06b118aa7ac1.png)

   For testing purposes, you can now use your SIP client to register with FreePBX using the username, password/secret and local IP address of your FreePBX.
6. Now we'll set up your trunk. Go to **Connectivity -> Trunks -> Add Trunk -> Add New Chan SIP Trunk.** You'll now be located in the **General** tab. Provide the following information:

   1. **Trunk Name:** Your Outbound CID and the maximum channels you'd like for this trunk.

      ![General SIP settings interface 3.](_images/6c893f0c13e5cc55.png)

      ​***Note:*** *Enter a Trunk name, your Outbound CID and the maximum channels you'd like for this trunk. If you choose not to set an Outbound CID on your trunk, then you must set an Outbound CID on each relevant extension. If you do not set a caller ID on either the trunk or each extension, then your calls will reach our SIP proxy without a valid caller ID. You may instead choose to enable a Caller ID Override in your SIP Connection’s Outbound Options from within the Telnyx Portal. Please review our [caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy) for accepted formats.*  
      ​

   ### **Tab: Dialed Number Manipulation Rules**

   Click on the **Dialed Number Manipulation Rules** tab. You can leave this entire section in its default state, but you can also enter dial patterns here:

   1. **For US numbers:**

      * prepend:*1*; match pattern: *NXXNXXXXXX*
      * prepend: blank; match pattern: *1NXXNXXXXXX*
   2. **For international numbers:**

      * prepend: Country Dialing prefix; match pattern: *NXXNXXXXXX*
      * prepend:blank; match pattern: (Country Dialing prefix)*NXXNXXXXXX*
   3. ![Dialed Number Manipulation Rules tab. ](_images/8433bb072b1f57dd.png)

      ​

      ### **Tab: sip Settings**
7. Click on the **Settings** tab and on the **General** sub-tab, provide the following:

   1. **Username :** Your Telnyx account username
   2. **Secret :** The password for your Telnyx trunk found under the connection → "show password" link in your Telnyx portal
   3. **Authentication :** *Outbound*
   4. **Registration :** *Send*
   5. **Language Code :** *English* (or the language you wish to conduct calls in)
   6. **SIP Server :** *sip.telnyx.com*
   7. **SIP Server Port :** *5060* if you have not enabled TLS encryption. If you have, choose *5061*.
   8. **Context :** *from-pstn*
   9. **Transport :** *UDP* or *TCP* if you have not enabled TLS encryption. If you have, choose *TLS/TCP*.

      ![SIP settings page 1. ](_images/ac0d66844410d360.png)
8. Open the **Settings > Advanced** sub-tab and adjust the following:

   1. **From Domain:** *sip.telnyx.com*

      ![SIP settings page 2. ](_images/8b4bd3929e4ed549.png)
9. Open the **SIP Settings > Codecs** sub-tab and adjust the following:

   1. Select *ulaw, alaw, gsm, g722, g729, Opus*. All other boxes should be unchecked, as these are the Telnyx-supported codecs.
   2. If you plan to do any video communication, Telnyx supports the H264 video codec.
10. Proceed to the **SIP Settings** tab. In the sub tabs **outgoing and incoming.**
11. Outgoing settings for your SIP trunk:

    1. **username:** Your Telnyx SIP credentials username
    2. **secret:** Your Telnyx SIP credentials password
    3. **type:** *friend*
    4. **qualify:** *Yes*
    5. **insecure:** *port,invite*
    6. **Host:** *sip.telnyx.com*
    7. **Fromdomain:** *sip.telnyx.com*
    8. **disallow:** *all*
    9. **allow***: ulaw&alaw*

       ![SIP settings page 3.](_images/4e94976263b44777.png)
12. Inbound settings for your SIP trunk:

    1. **username:** Your Telnyx SIP credentials username
    2. **secret:** Your Telnyx SIP credentials password
    3. **fromdomain:** *sip.telnyx.com*
    4. **host:** *sip.telnyx.com*
    5. **type:** *friend*
    6. **insecure:** *port,invite*
    7. **qualify:** *yes*
    8. **disallow:** *all*
    9. **allow:** *ulaw&alaw*
    10. **dtmfmode:** *rfc2833*
    11. **Register String:** Your Telnyx SIP credentials username:Your Telnyx SIP credentials password*@sip.telnyx.com/*Your Telnyx SIP credentials username

        **Example:** dillin1234:[mypassword123@sip.telnyx.com](mailto:mypassword123@sip.telnyx.com)/dillin1234

        ![SIP settings page 4.](_images/cd94128f1351ae95.png)

[Back to Top](#h_17c13cc9ea)

## 3. Configure outbound routes

Outbound routing is a set of rules that tells FreePBX which Telnyx trunk to use for any given outbound call. Having multiple trunks allows you to control cost by routing calls over the least costly trunk for a particular call. Outbound routes are used to specify what numbers are allowed to go out a particular route.

You will want to make sure you define routes for all types of calls. Not defining a route can leave your users frustrated when they need to make an important call.

Navigate to **Connectivity -> Outbound Routes.**

1. Create a new outbound route and provide the following on the **Route Settings** tab:

   1. **Route Name:** Something distinct that makes sense for your route purpose.
   2. **Trunk Sequence for Matched Routes:** Select the trunk you just created in [section 2](#h_fcc442afae).
   3. **Route Name :** *Outbound\_Telnyx*
   4. **Route CID :**  Number you purchased on the Telnyx portal.
   5. **Trunk Sequence for Matched Routes :** Select the trunk you just created in [section 2](#h_fcc442afae).

      ![Outbound routes configuration tab 1.](_images/03a0db6e3b8b108c.png)
2. Now select the **Dial Patterns** tab to the right of the **Route Settings** tab and enter dial patterns exactly as you see in the following image. This pattern allows you to dial 10 Digits (U.S. Calling), 11 Digits (North American Calling).   
   ​  
   ​*If you need dial patterns for a region outside North America, please contact Telnyx support.*

   ![Inbound routes configuration tab. ](_images/b1b53778bd839984.png)

   ***Note*** *that our current documentation portal shrinks screenshots, making some detail difficult to see. Right-click on the image above and select "Open image in new tab" from the context menu. This will open the image in a new tab and display it at its full size and resolution.*  
   ​
3. Click **Submit**, then **Apply Config**.

[Back to Top](#h_17c13cc9ea)

## 4. Configure inbound routes

When a call comes in from the outside, it'll need to be directed from sip.telnyx.com to the phone extension you ultimately want it to go, such as a user extension or an IVR extension.   
​

In this section, we'll configure our own inbound routes.

1. Make your way to **Connectivity -> Inbound Routes** and open the **General** tab.
2. The following image demonstrates an inbound route that will send *ANY* call to a certain extension.   
   ​  
   To direct a specific number to a specific extension you would create a route and set the "[DID Number](https://telnyx.com/resources/sip-did)" field to your 11 digit DID with sip.telnyx.com (for instance : [12172031700](http://#)).

![Inbound routes configuration tab. ](_images/1a1b59fcbfca0746.png)

|  |
| --- |
| ***Note:*** *By default, when creating a SIP Connection in the Telnyx Mission Control Portal, the number formats for the ANI and DNIS will be set to E.164. This means Telnyx will send the dialled number in the SIP INVITE to your FreePBX system with 11 digits. As the DID number above is in 11 digit format, the call will be accepted and routed to the extension. However, you can control the number formats as you desire and can read more about it [here](https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats).* |

That's it, you've now completed the configuration of FreePBX ChanSIP V13 Credentials Trunk and can now make and receive calls by using Telnyx as your SIP provider.

[Back to Top](#h_17c13cc9ea)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally, you can check out:

* [FreePBX documentation](https://wiki.freepbx.org/#all-updates)
* [FreePBX community](https://community.freepbx.org/)
* [FreePBX support](https://www.freepbx.org/support/)
* [FreePBX videos](https://www.freepbx.org/videos/)

---

Related Articles

[FreePBX V13: PJSIP Credentials](https://support.telnyx.com/en/articles/1277754-freepbx-v13-pjsip-credentials)[FreePBX V14: IP Trunk - ChanSIP](https://support.telnyx.com/en/articles/3284736-freepbx-v14-ip-trunk-chansip)[FreePBX V14: Credentials - ChanSIP](https://support.telnyx.com/en/articles/3284752-freepbx-v14-credentials-chansip)[FreePBX V15 IP Trunk - ChanSIP Tutorial](https://support.telnyx.com/en/articles/5467232-freepbx-v15-ip-trunk-chansip-tutorial)[FreePBX V15: IP Trunk - PJSIP](https://support.telnyx.com/en/articles/5619595-freepbx-v15-ip-trunk-pjsip)

Did this answer your question?

😞😐😃

Table of contents
