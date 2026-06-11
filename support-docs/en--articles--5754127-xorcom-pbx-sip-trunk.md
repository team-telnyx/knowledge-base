---
source_url: https://support.telnyx.com/en/articles/5754127-xorcom-pbx-sip-trunk
scraped: 2026-06-11
---

Xorcom PBX: SIP Trunk | Telnyx Help Center

[Skip to main content](#main-content)

# Xorcom PBX: SIP Trunk

Learn to set up Xorcom CompletePBX and configure SIP trunks with Telnyx's Mission Control Panel.

C

Written by Customer Success

December 14, 2023

Table of contents

[Jump to Instructions](#h_7831da969f)

Xorcom, designs and manufactures integrated business telephony solutions that support both traditional PSTN and VoIP, including IP PBX (Private Branch Exchange), Hotel Phone Systems – award-winning IP PBX (Private Branch Exchange) for Hospitality, Virtual PBX Systems, and Multi-tenant PBX.

Further documentation:

* CompletePBX 4.6 technical documentation: <https://files.xorcom.com/techdocs/pm0618-completepbx-reference-guide.pdf>   
  ​  
  Note that version 5.x is currently available, however, Xorcom is updating its product documentation and the version 5 docs are not currently available.

---

# Instructions For Configuring a Xorcom CompletePBX SIP Trunk

## In this guide, you will:

1. [Create a CompletePBX SIP trunk](#h_b030b313ef)
2. [Configure an outbound route](#h_bb7fb81679)
3. [Configure an inbound route](#h_3e8a28256d)

**Pre-Requisites**

* [Download](https://www.xorcom.com/pbx-download/) and [install](https://youtu.be/exQmoIqnYTw) CompletePBX

## 1. Create a CompletePBX SIP trunk

In this step, you'll configure your first [SIP trunk](https://telnyx.com/products/sip-trunks) in CompletePBX so you can get ready to make and receive calls.

1. From the left navigation bar, click on **PBX** > **External** then click on **Trunks** and configure the following settings:  
   ​  
   In the **Technology** section, enter the following:

   1. **Technology**: *SIP*
   2. **Description**: Enter a description for this trunk.
   3. **Trunk CID:** If you enter a CallerID Name, it must be in CAPITAL LETTERS, without any special characters (Spaces are allowed) and NOT longer than 15 characters. The Outbound CallerID Name will only work when you call a Canadian number. For the US, you will need to update your record associated with your CallerID Number, in the CNAM database, by requesting an update to our support.  
      ​  
      ​**Note:** If you would like to set your outbound Caller ID Name in the **Trunk CID** fields, it will override everything that your extension/Outbound Routes will try to pass. Enter the Trunk CID and set **Overwrite CID:** *Always*.

   In the **Device for Outgoing Calls (Peer)** section, enter the following:

   1. **Outbound Username:** Your Telnyx username
   2. **Host**: sip.telnyx.com (or, depending on your country, .ca, .au, .eu)
   3. **Port**: 5060
   4. **Remote Username**: Your Telnyx account username
   5. **Remote Secret**: Your Telnyx account password
   6. **From User**: Your Telnyx account username
   7. **From Domain**: sip.telnyx.com
   8. **Insecure**: Choose *Port, Invite* from the dropdown menu
   9. **Allow Inbound Calls**: *Yes*
   10. **Qualify**: *Yes*

   Find the **Register String** section and enter the following:

   1. **Use Default:** *Yes* The whole string will automatically be generated.

   [![CompletePBX configuration for SIP Trunk. ](https://downloads.intercomcdn.com/i/o/422822047/f79b998247f2813d0959b948/xorcom1.png?expires=1781168400&signature=f1b18ecf77ed83023a129a09d4ecbab53e3fccd5bcb0b030020f2d92ff208a44&req=cCIlHst8nYVYFb4f3HP0gIz07Q1AzfMm%2FNuv9sOaMLWmmI%2BgoCkuVh5v4mKi%0AjMs%3D%0A)](https://downloads.intercomcdn.com/i/o/422822047/f79b998247f2813d0959b948/xorcom1.png?expires=1781168400&signature=f1b18ecf77ed83023a129a09d4ecbab53e3fccd5bcb0b030020f2d92ff208a44&req=cCIlHst8nYVYFb4f3HP0gIz07Q1AzfMm%2FNuv9sOaMLWmmI%2BgoCkuVh5v4mKi%0AjMs%3D%0A)
2. Click on the **Advanced** tab and enter the following:

   1. **Type**: *Peer*
   2. **Parameter**: *sendrpid*
   3. **Value**: *PAI*
   4. **Enabled**: *On*

   [![XorCom advanced settings page. ](https://downloads.intercomcdn.com/i/o/422842934/240d7a9c5429478582ced77c/xorcom2.png?expires=1781168400&signature=1bd3c35975506bb12aad1876cd69aaebec58358001ee461a58d7dda9b7e016ae&req=cCIlHs18lIJbFb4f3HP0gDGVypnDiuSCl%2FB7ffKRrJiu%2Bj1v8q73nal8DZwn%0AaJU%3D%0A)](https://downloads.intercomcdn.com/i/o/422842934/240d7a9c5429478582ced77c/xorcom2.png?expires=1781168400&signature=1bd3c35975506bb12aad1876cd69aaebec58358001ee461a58d7dda9b7e016ae&req=cCIlHs18lIJbFb4f3HP0gDGVypnDiuSCl%2FB7ffKRrJiu%2Bj1v8q73nal8DZwn%0AaJU%3D%0A)

[Back to Top](#h_7831da969f)

## 2. Configure an outbound route

In this step, you will configure an outbound calling route pattern that CompletePBX will use as a template, or set of rules, to follow for outbound calls associated with the route.

1. From the lefthand navigation, click **PBX > External.**
2. Click on **Outbound Routes** and set the following:

   In the **General** section, enter the following:

   * **Description**: A description that will help you identify the route, such as *"TLS Calling Rule".*
   * **Trunks**: Select the Telnyx trunk you just created in step 1.
   * **CID**: (Caller ID) If this is not set already in your Telnyx trunk, you can enter your company name here.  
     ​  
     If you enter a CallerID Name, it must be in CAPITAL LETTERS, without any special characters (Spaces are allowed) and NOT longer than 15 characters. The Outbound CallerID Name will only work when you call a Canadian number. For the US, you will need to update your record associated with your CallerID Number, in the CNAM database, by requesting an update to our support.
   * **Overwrite CID**: *Always* if you would like to use this CID associated with this Outbound Route. (Your trunk Overrite CID settings must be set to [NEVER] to use it)

   In the **Dial Patterns** section, enter the following:

   * **Prefix**: You may enter a prefix if needed, such as 9, if you want your extensions to dial 9 before the outgoing number. Note that the number [9] will not be sent to Telnyx.
   * **Pattern**: You can indicate multiple patterns matching for an outbound call. *E.g. for a North American number, you can use NXXNXXXXXX/1NXXNXXXXXX (N = digits between 0-9 and X = digits between 2-9).*

   [![Dial Patterns page. ](https://downloads.intercomcdn.com/i/o/422842847/5c9cee8d4e6d9b4948b00039/xorcom3.png?expires=1781168400&signature=4ef6ddcf6e52676dd6e69ce5d925c3a04b0ef98f1fc32ff2960740faef5ab678&req=cCIlHs18lYVYFb4f3HP0gLLvr69FGuAojtJ1Ce06%2FP3228%2BZyJHWMJvp4pon%0AERM%3D%0A)](https://downloads.intercomcdn.com/i/o/422842847/5c9cee8d4e6d9b4948b00039/xorcom3.png?expires=1781168400&signature=4ef6ddcf6e52676dd6e69ce5d925c3a04b0ef98f1fc32ff2960740faef5ab678&req=cCIlHs18lYVYFb4f3HP0gLLvr69FGuAojtJ1Ce06%2FP3228%2BZyJHWMJvp4pon%0AERM%3D%0A)

   [![Dial pattern settings to set multiple matching patterns. ](https://downloads.intercomcdn.com/i/o/422846180/e2bc40f4092503033b5f2527/xorcom4.png?expires=1781168400&signature=d278c84a8b53c1ff7a930d266ac0cd849680235719960fbc41cc23e455bba665&req=cCIlHs14nIlfFb4f3HP0gP2qec4iqnp4UMfSbznn%2FDOiq%2FPMiAIhCDdHf97p%0At6g%3D%0A)](https://downloads.intercomcdn.com/i/o/422846180/e2bc40f4092503033b5f2527/xorcom4.png?expires=1781168400&signature=d278c84a8b53c1ff7a930d266ac0cd849680235719960fbc41cc23e455bba665&req=cCIlHs14nIlfFb4f3HP0gP2qec4iqnp4UMfSbznn%2FDOiq%2FPMiAIhCDdHf97p%0At6g%3D%0A)

[Back to Top](#h_7831da969f)

## 3. Configure an inbound route

In this step, you will configure an inbound calling route pattern that CompletePBX will require in order for you to receive inbound calls from your DID. Each DID will need to be associated with an inbound route. Multiple DIDs can be associated with the same route, but any single DID can only be associated with a single route.

1. From the lefthand navigation, click **PBX > External.**

Click on **Inbound Routes** and set the following:

In the General section, enter the following:

1. **Routing Method**: *Default*
2. **Description**: Enter a description that will help you identify your inbound route
3. **DID Pattern**: Enter your [DID number](https://telnyx.com/resources/sip-did) as it excluding any dots, parentheses, etc.
4. **Inbound Destination**: Destination to route this inbound call when it is first answered.

[![A screenshot of a configured Xorcom CompletePBX to work with Telnyx.](https://downloads.intercomcdn.com/i/o/422845618/8aac70c29a712958e85aaf9c/xorcom5.png?expires=1781168400&signature=d0797766299102914e451f893ac6a3571d40b684207189f7443b8fc15cccb96b&req=cCIlHs17m4BXFb4f3HP0gNOJv6R1V1klYXkJAw4K7kyp3URiKkTDw1kLzXIl%0ABLPCFRM03CvEh5nZPA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/422845618/8aac70c29a712958e85aaf9c/xorcom5.png?expires=1781168400&signature=d0797766299102914e451f893ac6a3571d40b684207189f7443b8fc15cccb96b&req=cCIlHs17m4BXFb4f3HP0gNOJv6R1V1klYXkJAw4K7kyp3URiKkTDw1kLzXIl%0ABLPCFRM03CvEh5nZPA%3D%3D%0A)

That's it, you've now configured Xorcom CompletePBX to work with Telnyx.

[Back to Top](#h_7831da969f)

---

**Additional Resources**

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

* [Complete PBX technical specifications and documentation](https://files.xorcom.com/techdocs/pm0618-completepbx-reference-guide.pdf)

---

Related Articles

[Configuring an Elastix 4 PBX IP Trunk](https://support.telnyx.com/en/articles/1130622-configuring-an-elastix-4-pbx-ip-trunk)[Configuring an Elastix 4 PBX Trunk](https://support.telnyx.com/en/articles/1130654-configuring-an-elastix-4-pbx-trunk)[Grandstream UCM6xxx: SIP Trunks](https://support.telnyx.com/en/articles/5748258-grandstream-ucm6xxx-sip-trunks)[Yeastar S-Series: Telnyx SIP](https://support.telnyx.com/en/articles/5748952-yeastar-s-series-telnyx-sip)[How to configure Yeastar P-series](https://support.telnyx.com/en/articles/13375115-how-to-configure-yeastar-p-series)

Did this answer your question?

😞😐😃

Table of contents
