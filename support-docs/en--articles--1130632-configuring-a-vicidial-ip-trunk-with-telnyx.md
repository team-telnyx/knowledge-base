---
source_url: https://support.telnyx.com/en/articles/1130632-configuring-a-vicidial-ip-trunk-with-telnyx
title: "Configuring a Vicidial IP trunk with Telnyx"
description: "In this article we will walk you through how configuring a Vicidial IP trunk at Telnyx. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 571e092cc671b0ddd605cc1281e26d891dbd85c0d6033cefa49898d53fad873d
---







# Configuring a Vicidial IP trunk with Telnyx

In this article we will walk you through how configuring a Vicidial IP trunk at Telnyx. See Telnyx guidance and requirements.




[Jump to Instructions](#h_dfe3471e39)

[Vicidial](https://www.vicidial.com/?p=470) is an enterprise class, open source, contact center suite in use by many large call centers around the world. It has over fourteen thousand (14,000) registered installations in over 100 countries around the world. The official releases of Vicidial have been downloaded over twenty five thousand (25,000) times in the last year alone.

This article guides you on how to configure this PBX for making and receiving calls over the internet through a next generation carrier like Telnyx!

Additional documentation:

* [Vicidial support](https://www.vicidial.com/?page_id=151)
* [Vicidial user manual](https://www.vicidial.org/download_survey.php) (free version. Additionally, there is a [paid version](http://www.vicidial.org/store.php#MANAGER) with higher resolution)

---

## Instructions for configuring a Vicidial IP trunk

In this document you will

1. [Configure your Telnyx Mission Control Portal to work with Vicidial](#h_feb6f00743)
2. [Configure Vicidial](#configuring-your-vicidial)

**Pre-requisites**

* You'll need to have created an [IP based connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal account, assigned this connection to a DID and outbound profile in order to make and receive calls
* [Download](https://www.vicidial.com/?page_id=210) and [install](https://www.vicidial.com/?page_id=151) Vicidial
* Make sure your [Telnyx Mission Control Portal is set up properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)

**Video Walkthrough**

Coming soon! Check back frequently as we update our documentation.

## 1. Configure your Telnyx Mission Control Portal to work with Vicidial

**First, you'll need to purchase a number:**

1. Visit the **Numbers** page via the navigation menu on the left-hand side.
2. Select the **Search Numbers** tab.
3. Select your search type: (NPA-NXX, Region, Toll Free or Advanced).
4. Input your search criteria and click **Search**.
5. Results will display below.
6. Click **+ Add to Cart** to select the number(s) you'd like to purchase.
7. Click on the **Shopping Cart** to view your selected numbers and check out.
8. Once purchased, your numbers will be visible on the **My Numbers** tab within the **Numbers** page.

**Next, you'll set up a connection:**

1. Visit the **Connections** page via the navigation menu on the left hand side.
2. Click the **Add Connection** button (located towards the top right corner).
3. Input a name for the connection.
4. Select **IP Address** for your Authentication Method and input the IP Address of your Vicidial instance.
5. Click the **Create** button to finish creating your connection.

**Now, you'll provision your number (assign to a connection):**

1. Go back to the **Numbers** page via the navigation menu on the left hand side.
2. Select the **My Numbers** tab (you may have defaulted to this already).
3. Click the **Select Connection** drop-down next to your number. You should see the connection you just created - select it.
4. Your number is now all set on the portal.

**And finally, you'll create your outbound profile:**

1. Visit the Outbound section via the navigation menu on the left hand side.
2. Click the **+ Add Outbound Profile** button (located towards the top right corner).
3. Select the connection you created via the **Select Connection** drop-down.
4. Choose the **Traffic Type** and **Service Plan** that meets your needs.
5. Click **Add**.
6. You are now setup for outbound calling on the portal.

[Back to Top](#h_dfe3471e39)

## 2. Configure Vicidial

1. Log into the Vicidial web portal and going to **Admin -> Carriers -> Add new carrier.**
2. Enter the following information:

   1. **Carrier ID:** *TelnyxCarrier*
   2. **Name:** *telnyxRegistration*
   3. **String :** leave blank*.*
   4. **Template ID:** *NONE*
   5. **Account Entry:** *[telnyx]*
   6. **Disallow:** All
   7. **Allow:** *ulaw*
   8. **Allow:** *g729*
   9. **Type:** *peer*
   10. **Insecure:** *port,invite*
   11. **Host:** [sip.telnyx.com](https://sip.telnyx.com)
   12. **dtmf mode:** *rfc2833*
   13. **Context:** *default*
   14. **Protocol:** *SIP*
   15. **Global String:** *Telnyx=SIP/telnyx*
   16. **Dial Plan:**
       ​*exten => \_91NXXNXXXXXX,1,AGI(agi://127.0.0.1:4577/call\_log)
       exten => \_91NXXNXXXXXX,2,Dial(${Telnyx}/${EXTEN:1},60,tTor)
       exten => \_91NXXNXXXXXX,3,Hangup*
       ​
       In this case, 9 is the prefix that will be dialed to send calls to Telnyx's trunk.

Depending on your phone configuration, you may also wish to configure an outbound caller ID to be in accordance with our [caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy). You can do this on a per-user or per-campaign basis.

To apply a per-user caller ID:

1. Open the **Users** tab in the Vicidial administration portal.
2. Select **Modify** next to the relevant user.
3. Select Apply the desired outbound caller ID in the **Outbound CallerID** field.
4. Click **Submit**.

To apply a caller ID on a campaign:

1. Select the **Campaigns** tab in the Vicidial administration portal.
2. Select **Modify** next to the campaign you want to have the caller ID.
3. Click the **Detail** tab and apply the desired caller ID in the **Campaign CallerID** field.
4. Click **Submit**.

That's it, you've now completed the configuration of Vicidial and can now make and receive calls by using Telnyx as your SIP provider!

[Back to Top](#h_dfe3471e39)

---

## Additional Resources

## Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally you can check out:

* [Vicidial support](https://www.vicidial.com/?page_id=151)
* [Vicidial user manual](https://www.vicidial.org/download_survey.php) (free version. Additionally, there is a [paid version](http://www.vicidial.org/store.php#MANAGER) with higher resolution)

---

---

Related Articles

[Configuring a Cisco CUBE/CUCM IP Trunk](https://support.telnyx.com/en/articles/1130606-configuring-a-cisco-cube-cucm-ip-trunk)[Configuring an AVAYA IP trunk with Telnyx](https://support.telnyx.com/en/articles/1130627-configuring-an-avaya-ip-trunk-with-telnyx)[Asterisk: Configure an Asterisk IP trunk](https://support.telnyx.com/en/articles/1130628-asterisk-configure-an-asterisk-ip-trunk)[Configuring a GoAutoDial PBX SIP Trunk](https://support.telnyx.com/en/articles/1130694-configuring-a-goautodial-pbx-sip-trunk)[Vicidial: Configure Vicidial Credentials](https://support.telnyx.com/en/articles/1176353-vicidial-configure-vicidial-credentials)

Did this answer your question?

😞😐😃
