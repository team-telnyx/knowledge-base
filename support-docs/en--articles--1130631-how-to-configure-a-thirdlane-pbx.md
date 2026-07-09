---
source_url: https://support.telnyx.com/en/articles/1130631-how-to-configure-a-thirdlane-pbx
scraped: 2026-07-08
content_hash: 1e45d5bfb349bef08924720fc68cbcadb76be27962fea1085f8b3cf2864d521c
---

How to configure a Thirdlane PBX | Telnyx Help Center

[Skip to main content](#main-content)

# How to configure a Thirdlane PBX

In this article we will walk you through how to configure a Thirdlane PBX IP trunk at Telnyx.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_76ca35de8c)

[Thirdlane IP-PBX](https://www.thirdlane.com/products/thirdlane-pbx)  is complete business communications platform with a feature rich Multi Tenant IP PBX at its core. It addresses the needs of Internet Telephony Service Providers and other companies that need to provide multiple virtual PBXs (usually for different companies or departments) and manage them through a single web interface. This article guides you on how to configure this PBX for making and receiving calls over the internet through a next generation carrier like Telnyx!

Additional documentation:

* [Thirdlane user documentation](https://www.thirdlane.com/docs/platform/introduction)
* [Thirdlane support](https://www.thirdlane.com/support)
* [Thirdlane REST API](https://www.thirdlane.com/docs/platform/api)

---

# Instructions for Configuring a Thirdlane PBX

In this activity you will:

1. [Create a SIP trunk](#h_5b8a422969)
2. [Configure dialing on your SIP trunk](#h_e7c844f668)
3. [Configure caller ID to work with your trunk dialing configuration](#h_34e0a1d10a)
4. [Set up phone numbers using provisioned DIDs](#h_455990bbf1)
5. [Configure inbound routes](#h_1483bd8624)
6. [Assign any still-unassigned numbers to the tenant](#h_fc22ded8c7)
7. [Unassign numbers from the tenant](#h_102aad5175)
8. [Create extensions for your assigned numbers](#h_42d0c1ced2)
9. [Configure SMS gateway](#h_1ba92b1717)
10. [Enable SMS for your new phone numbers](#h_2fe14627b3)
11. [Configure additional Thirdlane settings and post-requisites](#h_42d0c1ced2)

## **Pre-requisites**

* [Configure your Telnyx Mission Control Portal](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) which will help you:

  + Set up a connection
  + [Provision a DID from Telnyx](https://portal.telnyx.com/#/app/numbers/search-numbers) ([How do I do this?](https://support.telnyx.com/en/articles/3562148-requesting-numbers))
  + Create an outbound voice profile
* Thirdlane (non Telnyx-specific) setup:

  + [Download](https://www.thirdlane.com/products/multi-tenant-pbx) (this is a trial - contact Thirdland to provision an account) and [install](https://www.dropbox.com/s/w3c5oamhsnp4s26/PBXManagerAdminGuide.pdf?dl=0) Thirdlane PBX
  + Follow the steps in the [Getting Started and Configuration Manager steps provided by Thirdlane](https://www.thirdlane.com/docs/platform/installing)
  + Perform a [default setup on Thirdlane](https://www.thirdlane.com/docs/platform/default-values)
  + [Configure TLS transport](https://www.thirdlane.com/docs/platform/tls-transport)
  + [Configure security settings](https://www.thirdlane.com/docs/platform/trusted-ips)
  + [Create an ICE server](https://www.thirdlane.com/docs/platform/ice-servers) (***Note that*** *as of version 10.0.1, Thirdlane will automatically install and configure a STUN and a TURN server)*
  + [Configure dialplan variables](https://www.thirdlane.com/docs/platform/dialplan-variables)
  + OPTIONAL BUT RECOMMENDED: [Create a dialplan script](https://www.thirdlane.com/docs/platform/dialplan-scripts) if you plan to use them
  + OPTIONAL BUT RECOMMENDED: Configure [default hold music](https://www.thirdlane.com/docs/platform/default-music-on-hold), if you plan to use it
  + Set basic [inbound](https://www.thirdlane.com/docs/platform/inbound-permissions) and [outbound](https://www.thirdlane.com/docs/platform/outbound-dialing-permissions) permissions

## 1. Create a SIP trunk

Before we do anything, we are going to need to set up a [SIP trunk](https://telnyx.com/products/sip-trunks) to connect Thirdlane PBX with Telnyx. This will allow your Telnyx account to communicate with Thirdlane PBX so you can make and receive calls, SMS messages, configure routes, and more.

|  |
| --- |
| ***Note:*** *When you create a new trunk, Thirdlane Configuration Manager will prefill the form with the values you specified in the* [default setup](https://www.thirdlane.com/docs/platform/default-values) *done as part of your* [pre-requisite activities](#h_898816635a). |

1. From your Thirdlane PBX portal, expand **Telephony Settings** in the left-hand menu and click on **Trunks**.
2. Select **Create Trunk** and provide the following:

   1. **Name:** Unique alphanumeric name for the Trunk (no spaces or special characters are allowed). In some cases the name of IP Trunks will be provided to you by your service provider.
   2. **Status:** This setting is referenced in the default Thirdlane supplied scripts used for Outbound Routes. This allows to disable Trunk temporarily if required.
   3. **Description:** Description of the Trunk, optional.
   4. **Available to tenants:** Only available in Thirdlane Muti Tenant systems. Trunks can be created for use by all [Tenants](https://www.thirdlane.com/docs/platform/tenants) or only a particular tenant. If Trunk is set up for a particular [Tenant](https://www.thirdlane.com/docs/platform/tenants) it won't be available for use by other Tenants and will not appear as an option in Outbound Routes for other Tenants.
   5. **Host:** IP address of your VoIP service provider's gateway or proxy. In case of a "friend" Trunk type, you can also enter "dynamic" in this field. Peers handle both inbound and outbound calls and are matched by IP/port. Users handle inbound calls only. See Asterisk documentation for details about authorization rules.
   6. **Outbound proxy:** *sip.telnyx.com*
   7. **Context:** Specifies the context for this Trunk. For external inbound providers it should be set to the default from-outside context.
   8. **User Name:** Your Telnyx SIP trunk/account username
   9. **Password:** Your Telnyx SIP trunk/account password
   10. **Enabled codecs:** Use Telnyx codec preferences. Telnyx supports the following codecs:

       1. *ulaw(g711u)*
       2. *alaw(g711a)*
       3. *g722*
       4. *g729*
   11. **Disabled codecs:** Codecs to be disabled for this trunk. Either any that Telnyx does not support (see prior list) or any supported codecs you don't want to use
   12. Encryption: Call encryption for your trunk. You have the following options:

       1. **Enforce**. Make all the outbound calls via this Trunk encrypted and accept only encrypted inbound calls.
       2. **Reject**. Make all the outbound calls unencrypted and accept only unencrypted inbound calls.
       3. **Negotiate, trying encrypted first**. Try to make encrypted outbound calls first, and if that fails, fall back to unencrypted. Accept both encrypted and unencrypted inbound calls.
       4. **Negotiate, trying unencrypted first**. Try to make unencrypted outbound calls first, and if that fails, fall back to encrypted. Accept both encrypted and unencrypted inbound calls.
   13. **DTMF mode:** *In-audio, RFC2833*
   14. **Quality (ms):** *No* (the amount of time the server waits for keepalive packets from the endpoint.)
   15. **Other Options:** This section allows you to specify additional options that don't have corresponding GUI fields. Specify any additional options in the key=value form. Each pair should be entered on a separate line.
   16. **Registration:** Leave blank

   ![Expanding telephony settings through Thirdlane PBX portal. ](_images/058365c5624be832.png)

|  |
| --- |
| ***Note:*** *You can delete your trunk if you need to, however, deleting a trunk that it used by an outbound route will make the route invalid.* |

[Back to top](#h_76ca35de8c)

## 2. Configure trunk dialing

Before we start adding numbers that will be used to make/receive calls, we're going to want to make sure our trunk understands the way our numbers are dialed (For example, will you need users to dial 9 before calling out?) We will configure this in the following steps.

1. From your Thirdlane PBX portal, expand **System Management** in the left-hand menu and click on **Trunks**.
2. Edit the trunk you want to configure.
3. Select the **Trunk Dialing** tab and provide the following information:

   1. **Number of digits to strip:** How many digits will be stripped from the front of a dialed number (for example, if you require users to press 9 to dial out, you'd strip 1 digit - the 9 - from the number before placing the call)
   2. **String to prepend:** The string that will be prepended from the dialed number. This can also be specified in your outbound routes.
   3. **Dial command options:** Prepends specific options to **dial command options** string.
   4. **SIP Header:** Allows you to add up to 4 custom SIP headers. For example:  
      ​

      ```
      X-Custom-Header:VALUE
      ```

   ![Configuring trunk dialing through Thirdlane PBX portal. ](_images/0a15e314eec8acdb.png)

[Back to top](#h_76ca35de8c)

## 3. Configure caller ID to work with your trunk dialing configuration

This section allows you to specify how to alter Caller ID on outbound calls given the trunk dialing configuration you set up in [section 2](#h_e7c844f668).

1. From your Thirdlane PBX portal, expand **System Management** in the left-hand menu and click on **Trunks**.
2. Edit the trunk you want to configure.
3. Select the **Caller ID** tab and enter the following:

   1. **Number of digits to strip:** How many digits will be stripped from the front of a dialed number (for example, if you require users to press 9 to dial out, you'd strip 1 digit - the 9 - from the number before placing the call)
   2. **String to prepend:** The string that will be prepended from the dialed number. This can also be specified in your outbound routes.

[Back to top](#h_76ca35de8c)

## 4. Set up phone numbers using provisioned DIDs

It's time to create a phone number that can be used to make/receive calls! The phone numbers will be created from the [DIDs you provisioned from Telnyx](https://portal.telnyx.com/#/app/numbers/search-numbers) during your [pre-requisite activities](#h_898816635a).

1. From your Thirdlane PBX portal, expand **System Management > Telephony Settings** in the left-hand menu and click on **Phone Numbers** (Some setups may say **DIDs** instead of **Phone Numbers** - for those who see **DIDs**, click on that) .All your phone numbers, if you have any, will be shown on this page.
2. To filter your number view, use the controls above the phone number list.

   1. **Select from:** Allows you to filter out phone numbers. You can choose from:

      1. *All*
      2. *Assigned to tenants*
      3. *Unassigned numbers*
      4. *Assigned to the currently selected tenant*
      5. *Phone numbers in use* (such as those assigned to user extensions or voice menus)
3. To add a range of new phone numbers:

   1. Enter your range using the **From** and **To** fields below the phone number list. (From bottom of range, to top of range)
   2. **Prepend:** This field prepends a prefix to the numbers in the range you're adding (for example, if a number starts with a 0 or a +)
   3. **Assign:** Check this checkbox if you want the new phone numbers to be assigned to the currently selected tenant.
4. Click the **Add Phone Numbers** button.

   ![An interface to set up phone numbers using provisioned DIDs](_images/6bd505e1092904b2.png)

   ***Note that*** *you can also add phone numbers in bulk by uploading them in .csv format.*

[Back to top](#h_76ca35de8c)

## 5. Configure inbound routes

In this section, you'll specify the inbound route that a caller will take when they dial a number (for example, routed to a certain user's extension or an IVR).

1. From the left-hand navigation, expand the **Selected Tenant Management** dropdown.
2. You'll see another dropdown called **Call Routing.** Click this dropdown and select **Inbound routes.**

   ![An interface for configuring call routes.](_images/d1d0c0de05bdf96b.png)
3. Select **Time Based Routes Group.** Then select **Add Route.** Enter the details similar to the below. Press Save when you are finished.

   ![Selecting time based routes group for inbound routes. ](_images/3d503099f668b00b.png)

At this point, inbound calling to your DID is now ready to go! Simply ensure you register your client to your PBX with the extensions username and password. The domain will be the public IP of your PBX server.  
​

[Back to top](#h_76ca35de8c)

## 6. Assign any unassigned numbers to the tenant

If you have any numbers (DIDs) that you did not assign to your tenant when you added them in [step 3](#h_455990bbf1), you can do that now.

1. From the left-hand navigation, expand **System Management** and select **DIDs**.

   ![An interface to assign any unassigned numbers to the tenant](_images/021d6d871f97c376.png)

   These DIDs will be the ones that you purchased from your [Telnyx Mission Control Portal](https://portal.telnyx.com/#/app/numbers/search-numbers) account.
2. Find the number you want to enable and click the checkbox beside the number.
3. Select **Assign Selected** on the top-right of the screen. This will assign the DID to the current tenant and will make it accessible to be assigned to an extension.

   ![An interface for assigning selected DIDs. ](_images/a031f8cb709f0939.png)

[Back to top](#h_76ca35de8c)

## 7. Unassign numbers from the tenant

There will often be situations where you will also want to unassign a number from the tenant.

1. To **unassign** assigned numbers, simply select the number(s) using the checkbox next to them and click **Unassign Selected** in the top navigation.

   ![Page to unassign numbers from the tenant.](_images/ec8e6b0d4f809c8e.png)

   ​***Note that*** *you cannot unassign any number currently in use without first deleting its corresponding inbound route. We will discuss inbound routes in a later section.*

[Back to top](#h_76ca35de8c)

## 8. Create extensions for your assigned numbers

In this section, you'll configure all of your extensions that you will associate with the DIDs you purchased from Telnyx and loaded in [section 1](#h_5b8a422969).

1. From the left pane, navigate to **Selected Tenant Management** and expand the dropdown. You'll see another dropdown called **Extensions and Contacts.**
2. Click this dropdown and select **User Extensions** toview and create all your extensions and associate these extensions with your DIDs. These DIDs will be the one's you purchased from your [Telnyx Mission Control Portal](https://portal.telnyx.com/#/app/numbers/search-numbers) account

   ![Page for creating extensions for your assigned numbers 1. ](_images/7e005c0c02316805.png)
3. Click **Create Extension** and open the **Basic** tab.
4. Enter the first name, last name and extension number for the user you're assigning to this extension.

   ![Page for creating extensions for your assigned numbers 2.](_images/35d64b0b004bcc59.png)
5. Click **Save**. You'll now see an extension created in your extensions section.

   ![Page for creating extensions for your assigned numbers 3.](_images/05a77932c9586a42.png)
6. Open the new extension for editing (pencil icon) and click on the **Phone** tab.
7. Find the **SIP User name** and **Password** fields. The values in these fields, along with your server IP address, can be used to register other devices to register to the PBX. These devices will need to be registered so they can receive the inbound calls to the DIDs associated to the extensions.

   ![Page for creating extensions for your assigned numbers 4. ](_images/9afe1698f6dc8cd5.png)
8. Return to the DID section from the left-hand menu. Find the DID you just set up. You'll see that the **Used in Inbound Routes** checkbox is enabled and the DID is now associated to extension 101.

   ![Page for creating extensions for your assigned numbers 5. ](_images/5ec2af059a091145.png)

[Back to top](#h_76ca35de8c)

## 9. Configure SMS gateway

In this step, you can configure an SMS gateway and your connections with SMS providers which will allow you to send and receive SMS messages.

1. From your Thirdlane PBX portal, expand **System Management** in the left-hand menu and click on **SMS Gateways**.
2. To create a new SMS gateway, click on the **Create** button and provide the following information:

   1. **Name**. Unique alphanumeric name for the SMS Gateway (no spaces or special characters are allowed).
   2. **Provider**. *Telnyx*
   3. **Description**. Description of the SMS Gateway, optional.
   4. **Domain**. Domain to be used to receive inbound SMS messages and status information sent by your SMS provider
   5. **API Key**. Provision [here](https://support.telnyx.com/en/articles/4305158-api-keys-and-how-to-use-them).

Once the SMS gateway is created, the Configuration Manager will generate a URL for receiving inbound SMS messages and status information sent by Telnyx. You need to specify these URLs on your Telnyx Mission Control Portal.

|  |
| --- |
| ***Note:*** *You can delete your SMS gateway being used by an SMS enabled phone number if you need to, however, deleting a SMS gateway that it used by an inbound route will make the route invalid.* |

[Back to top](#h_76ca35de8c)

## 10. Enable SMS for your new phone number(s)

In this section, we will enable SMS for any phone number(s) you want to use for sending text messages.

1. Expand **System Management** and click on **Phone Numbers**.
2. Select the number(s) you want to SMS-enabled using the checkbox next to them
3. Use the **SMS Gateway** dropdown to select an SMS gateway from a list of configured gateways.
4. Click the **Set SMS Gateway for selected** button.
5. After you've enabled SMS for your numbers, you can assign them to users in **Inbound SMS Routes**.

   ![Interface for SMS enablement for your new numbers. ](_images/172533199179785e.png)

[Back to top](#h_76ca35de8c)

## 11. Configure additional Thirdlane settings and post-requisites

The remainder of your setup doesn't require any further Telnyx-related configuration and you will want to refer to Thirdlane's documentation for the most current source of truth regarding their services. Before you can make calls, you'll need to ensure that the following conditions have been met:

1. You have configured extensions and contacts through the [Bulk Generator](https://www.thirdlane.com/docs/platform/bulk-generator), [User Extensions](https://www.thirdlane.com/docs/platform/user-extensions), and the [Company Directory](https://www.thirdlane.com/docs/platform/company-directory)
2. You have configured call routing: [inbound routes](https://www.thirdlane.com/docs/platform/inbound-routes), [outbound routes](https://www.thirdlane.com/docs/platform/outbound-routes), [dialing permissions](https://www.thirdlane.com/docs/platform/tenant-outbound-dialing-permissions#!), and [day/night mode](https://www.thirdlane.com/docs/platform/daynight-mode)
3. You have configured [inbound SMS routing](https://www.thirdlane.com/docs/platform/inbound-sms-routes)
4. You have configured additional [Thirdlane-side PBX features](https://www.thirdlane.com/docs/platform/pickup-groups#!)

That's it, you've now completed the configuration of your Thirdlane IP-PBX and can now make and receive calls by using Telnyx as the SIP provider.

[Back to top](#h_76ca35de8c)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally, check out:

* [Thirdlane user documentation](https://www.thirdlane.com/docs/platform/introduction)
* [Thirdlane support](https://www.thirdlane.com/support)
* [Thirdlane REST API](https://www.thirdlane.com/docs/platform/api)

---

Related Articles

[Configuring an Elastix 4 PBX IP Trunk](https://support.telnyx.com/en/articles/1130622-configuring-an-elastix-4-pbx-ip-trunk)[Configuring an Elastix 4 PBX Trunk](https://support.telnyx.com/en/articles/1130654-configuring-an-elastix-4-pbx-trunk)[Xorcom PBX: SIP Trunk](https://support.telnyx.com/en/articles/5754127-xorcom-pbx-sip-trunk)[3CX: Configuring a 3CX V18 PBX](https://support.telnyx.com/en/articles/6161111-3cx-configuring-a-3cx-v18-pbx)[How to configure Yeastar P-series](https://support.telnyx.com/en/articles/13375115-how-to-configure-yeastar-p-series)

Did this answer your question?

😞😐😃

Table of contents
