---
source_url: https://support.telnyx.com/en/articles/1176353-vicidial-configure-vicidial-credentials
scraped: 2026-07-08
content_hash: 142b9376b059e1523c0c1aafae30b5258a259e178de80247258eb56d134fd8df
---

Vicidial: Configure Vicidial Credentials | Telnyx Help Center

[Skip to main content](#main-content)

# Vicidial: Configure Vicidial Credentials

This article guides you on how to configure a Vicidial PBX for making and receiving calls over the internet through Telnyx!

Written by Dillin

January 10, 2024

Table of contents

[Jump to Instructions](#h_8283fc149c)

[Vicidial](https://www.vicidial.com/?p=470) is an enterprise class, open source, contact center suite in use by many large call centers around the world. It has over fourteen thousand (14,000) registered installations in over 100 countries around the world. The official releases of Vicidial have been downloaded over twenty five thousand (25,000) times in the last year alone.

This article guides you on how to configure this PBX for making and receiving calls over the internet through a next generation carrier like Telnyx!

Additional documentation:

* [Vicidial support](https://www.vicidial.com/?page_id=151)
* [Vicidial user manual](https://www.vicidial.org/download_survey.php) (free version. Additionally, there is a [paid version](http://www.vicidial.org/store.php#MANAGER) with higher resolution)

---

# Instructions for configuring a Vicidial IP trunk

In this document you will

1. [Configure your Telnyx Mission Control Portal to work with Vicidial](#h_cf792dd9f5)
2. [Configure Vicidial](#h_1889bc5863)

**Pre-requisites**

* You'll need to have created an [credentials-based connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal account, assigned this connection to a DID and outbound profile in order to make and receive calls
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
4. Select *Credentials* for your Authentication Method and input the desired user/password combination.
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

[Back to Top](#h_8283fc149c)

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
   9. **Type:** *friend*
   10. **Host:** [sip.telnyx.com](https://sip.telnyx.com/)
   11. **Username:** The username you set up in step 1
   12. **Password:** The password you set up in step 1
   13. **dtmf mode:** *rfc2833*
   14. **Context:** *default*
   15. **Protocol:** *SIP*
   16. **Global String:** *Telnyx=SIP/telnyx*
   17. **Dial Plan:**  
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

[Back to Top](#h_8283fc149c)

---

## Additional Resources

## Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally you can check out:

* [Vicidial support](https://www.vicidial.com/?page_id=151)
* [Vicidial user manual](https://www.vicidial.org/download_survey.php) (free version. Additionally, there is a [paid version](http://www.vicidial.org/store.php#MANAGER) with higher resolution)

---

Related Articles

[Asterisk: Configure an Asterisk IP trunk](https://support.telnyx.com/en/articles/1130628-asterisk-configure-an-asterisk-ip-trunk)[Configuring a Vicidial IP trunk with Telnyx](https://support.telnyx.com/en/articles/1130632-configuring-a-vicidial-ip-trunk-with-telnyx)[Configuring Linphone with Telnyx](https://support.telnyx.com/en/articles/1130674-configuring-linphone-with-telnyx)[Configuring an Asterisk Credentials Trunk](https://support.telnyx.com/en/articles/1130676-configuring-an-asterisk-credentials-trunk)[Configuring a GoAutoDial PBX SIP Trunk](https://support.telnyx.com/en/articles/1130694-configuring-a-goautodial-pbx-sip-trunk)

Did this answer your question?

😞😐😃

Table of contents
