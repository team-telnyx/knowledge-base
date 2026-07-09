---
source_url: https://support.telnyx.com/en/articles/5800399-synway-uc-200-telnyx-setup
scraped: 2026-07-08
content_hash: f0c8d387b62d7159281ee84e30b6405e14416fb860a454fa65931f2e626aac3a
---

Synway UC-200: Telnyx Setup | Telnyx Help Center

[Skip to main content](#main-content)

# Synway UC-200: Telnyx Setup

Discover the future of VoIP with Synway's UC-200. Our guide takes you through configuring this powerful IP PBX with Telnyx.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_7459c11e35)

[Synway](https://www.synway.net/index.php) is a leading security and VoIP provider and creator of the UC-200, an IP PBX appliance designed to bring enterprise-grade unified communications and security protection to your business, for a good price and without any licensing fees, costs-per-feature, or recurring fees. The UC-200 supports such technologies as comprehensive voice, fax, calling, conferencing, video/audio surveillance, data tools, security surveillance, mobility, and facility access management.  
​  
The UC200's advanced hardware and software can support up to 500 registered users and can be set up through a convenient web-browser user interface. Besides auto-discovery of diverse endpoints and auto-provisioning, the UC-200 series offers great features like customizable call-routing, multi-level IVRs, call queues, auto-attendant, call detail records (CDR), multi-site peering, voicemail/fax forwarding to email and more.  
​

Additional documentation:

* [Synway user documentation](https://wiki.synway.net/index.php/User_Manual)
* [Synway hardware documentation](https://wiki.synway.net/index.php/Hardware_Manual)
* [Synway developer documentation](https://wiki.synway.net/index.php/Programmer_Manual)
* [Download drivers](https://wiki.synway.net/index.php/Drivers_Download)
* [Demo and other tools](https://wiki.synway.net/index.php/Demos_&_Tools)
* [Synway contact/support](https://www.synway.net/messagea/Product_Inquiry.html)

---

# Instructions for configuring a Synway UC-200 PBX to work with Telnyx

In this activity you will:

1. [Log into your Synway UC-200](#h_10a49151a0)
2. [Configure your network settings](#h_81fc7ae5e6)
3. [Create your SIP trunk](#h_ab3decc1dd)
4. [Configure outbound route](#h_f944ed662e)
5. [Configure inbound route](#h_eeeb5cd2b6)
6. [Run a call test](#h_9a11393f87)

**Pre-requisites**

* Ensure your [Telnyx Mission Control Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* [Provision a DID from Telnyx](https://portal.telnyx.com/#/app/numbers/search-numbers) ([How do I do this?](https://support.telnyx.com/en/articles/3562148-requesting-numbers))

**Video walkthrough**

Setting up your Telnyx Mission Control Portal to make/receive calls:

Configuring your Synway UC-200:

## 1. Log into your Synway

In this activity, you will log into your UC-200 for the first time.

1. From a PC connected on the same network segment as your UC-200, open a browser (Chrome 67, Firefox 60, or IE11 recommended) and enter the default IP of the IPPBX: *`https://192.168.0.101`*
2. You'll be asked to log in. If this is your first time logging into your device, use the following credentials:

   1. **Username:** *admin*
   2. **Password:** *admin*
3. Once logging in, it is ***STRONGLY*** recommended that you first change the username and password.

[Back to Top](#h_7459c11e35)

## 2. Configure your network settings

In this activity, you will configure your network settings in your UC-200. DNS must be configured to analyze the domain if your UC-200 is on your local network.

1. From the left-hand navigation, click on **System** and expand **Network Settings** and click **Network Settings** in the submenu.
2. On the Basic Settings tab, enter the following:

   1. **Default interface:** *LAN*
   2. Configure LAN settings in the LAN section below.

[Back to Top](#h_7459c11e35)

## 3. Create your SIP trunk

In this activity, you will create a [SIP trunk](https://telnyx.com/products/sip-trunks) from your UC-200 and configure it to connect to Telnyx.

1. From the left-hand navigation menu, click on **PBX** and expand **Trunks** and click **Create Trunk** in the submenu.
2. Enter/confirm the following:

   1. **Trunk Type:** *SIP* (Should be the only option)
   2. **Trunk Name:** Choose a name that makes sense for you - a combination of numbers and letters is allowed.
   3. **Transport:** *UDP*
   4. **Register:** *Yes*
   5. **Username:** Your Telnyx SIP username
   6. **Password:** Your Telnyx SIP password
   7. **RegFall Retry:** Default is 30 seconds
   8. **Keep Inbound CallerID:** Use the registered account as the caller ID
   9. **Outbound CallerID Name:** The Caller ID you wish to use. Note the following Caller ID naming conventions:

      1. It should be in CAPITAL LETTERS, as this is more clearly visible on some devices
      2. It cannot contain special characters (such as, but not limited to @, $, \*, &). Spaces are allowed.
      3. It should have a max of 15 characters, as some providers will not show more than 15 characters.
   10. **Record:** Whether or not to save recording data. Default setting is *False*.
   11. **Enabled:** This enables or disables the trunk. Default setting is *True*.
   12. **Profile:** *LAN*
   13. **Trunk IP/Domain:** *sip.telnyx.com:5060*

[Back to Top](#h_7459c11e35)

## 4. Configure outbound route

In this step, you will configure your outbound route. Most of the field defaults in the outbound route wizard won't need to be changed, but there are a few exceptions you may want to consider:

1. From the left-hand navigation menu, click on **PBX** and expand **Trunks** and click **Outbound Routes** in the submenu.
2. Click **Add** and enter the following:

   1. **Name:** *Telnyx\_outbound*  or something similar
   2. **Dial/DID patterns:** Use a regex (Regular expression) to match the dial pattern you want to use. See page 27 of the [Synway user manual](https://www.synway.net/Download/Manual/UserManual/IPPBX_User_ManualV1.8.0.pdf) for examples.  
      ​  
      Use the **Strip** box to specify *how many digits* to strip from the dialed number before placing the call. For example, if your organization requires outbound callers to hit 9 before dialing out, then the **Strip** field should contain 1, as that one number (9) will need to be removed for the dialed number to be recognized.  
      ​  
      The **Prepend** box is also optional, but useful. This box will prepend digits on the front of a dialed number before placing the call. *For example, if a trunk requires 10-digit-dialing, but users are more comfortable dialing only 7 under certain circumstances, the 3-digit area code can be prepended to the beginning of the number before the call is placed.*
   3. **Member Extensions:** Add member extensions for controlling the outbound call authority. Only those extensions selected have the authority to use this route. It must be filled in; otherwise the configuration will fail to be saved.
   4. **Member Gateways:** Select the trunk you just configured in step 3 (or if you have another trunk you wish to use, select that. You can also select multiple trunks). This must be filled in, otherwise the configuration will fail to save.
   5. **Password:** For safety, if necessary.

[Back to Top](#h_7459c11e35)

## 5. Configure inbound route

In this step, you will configure your inbound route. Most of the field defaults in the inbound route wizard won't need to be changed, but there are a few exceptions you may want to consider:

1. From the left-hand navigation menu, click on **PBX** and expand **Trunks** and click **Inbound Routes** in the submenu.
2. Click **Add** and enter the following:

   1. **Name:** *Telnyx\_inbound*  or something similar
   2. **Dial/DID patterns:** Use a regex (Regular expression) to match the dial pattern you want to use. See page 25 of the [Synway user manual](https://www.synway.net/Download/Manual/UserManual/IPPBX_User_ManualV1.8.0.pdf) for examples.
   3. **Destination:** The extension incoming calls will default-route to
   4. **Member Trunks:** Select the trunk you just configured in step 3 (or if you have another trunk you wish to use, select that. You can also select multiple trunks). This must be filled in, otherwise the configuration will fail to save.

[Back to Top](#h_7459c11e35)

## 6. Run a call test

In this step, we're going to run a test to make sure everything is working properly.

1. Log into your Synway portal and dial extension **1000**. This will essentially do a "ping" call, from your UC-200 to Telnyx, and back to your UC-200.
2. From the left-hand navigation, click on **CDR**. These are your call dial records. You should see a log of this call.

That's it! Your Synway UC-200 is now configured to make and receive calls with Telnyx.

[Back to Top](#h_7459c11e35)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally, check out:

* [Synway user documentation](https://wiki.synway.net/index.php/User_Manual)
* [Synway hardware documentation](https://wiki.synway.net/index.php/Hardware_Manual)
* [Synway developer documentation](https://wiki.synway.net/index.php/Programmer_Manual)
* [Download drivers](https://wiki.synway.net/index.php/Drivers_Download)
* [Demo and other tools](https://wiki.synway.net/index.php/Demos_&_Tools)
* [Synway contact/support](https://www.synway.net/messagea/Product_Inquiry.html)

---

Related Articles

[Configuring an Elastix 4 PBX IP Trunk](https://support.telnyx.com/en/articles/1130622-configuring-an-elastix-4-pbx-ip-trunk)[How to configure a Thirdlane PBX](https://support.telnyx.com/en/articles/1130631-how-to-configure-a-thirdlane-pbx)[Configuring an Elastix 4 PBX Trunk](https://support.telnyx.com/en/articles/1130654-configuring-an-elastix-4-pbx-trunk)[Yeastar S-Series: Telnyx SIP](https://support.telnyx.com/en/articles/5748952-yeastar-s-series-telnyx-sip)[How to configure Yeastar P-series](https://support.telnyx.com/en/articles/13375115-how-to-configure-yeastar-p-series)

Did this answer your question?

😞😐😃

Table of contents
