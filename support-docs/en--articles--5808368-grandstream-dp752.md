---
source_url: https://support.telnyx.com/en/articles/5808368-grandstream-dp752
scraped: 2026-07-08
content_hash: 0211dcd48b8d7546a5929f9a0be33861a558f311094c3d62e112bae2d3379a0d
---

Grandstream DP752 | Telnyx Help Center

[Skip to main content](#main-content)

# Grandstream DP752

Learn how to make the most of your Grandstream DP752's capabilities by integrating it with Telnyx.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_f189d931af)

The [Grandstream DP752](https://www.grandstream.com/products/ip-voice-telephony/dect-cordless/product/dp720) is a mobilized VoIP solution that doesn't tie a user to their desk. This mobile DECT handset offers all the essential call control features on the go. A single DP752 base station can pair with up to 5 DP722 handsets, and each base station supports up to 10 SIP accounts, full HD audio, a 3.5mm headset jack, multi-language support, a speakerphone and more. And thanks to DECT authentication and encryption, your calls and account are protected.

|  |
| --- |
| ***Note:*** *This guide also supports configuration of a Grandstream DP750* |

Additional documentation:

* [User manual](https://www.grandstream.com/hubfs/Product_Documentation/DP750_DP720_User_Guide.pdf)
* [Admin manual](https://www.grandstream.com/hubfs/Product_Documentation/DP750_DP720_Administration_Guide.pdf)
* [DP750 FAQ](https://blog.grandstream.com/faq)
* [Firmware updates](https://www.grandstream.com/support/firmware)
* [Grandstream Helpdesk](https://helpdesk.grandstream.com/)
* [Grandstream community forum](https://forums.grandstream.com/)

---

# Instructions for configuring a Grandstream DP752 to work with Telnyx

In this activity you will:

1. [Get your DP752's IP address](#h_6df72972d6)
2. [Set up your DP752 for traffic flow](#h_b882234ebb)
3. [Configure codecs](#h_d93918c7c5)
4. [Configure user accounts](#h_29cde5b488)

**Pre-requisites:**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* [Provision a DID from Telnyx](https://portal.telnyx.com/#/app/numbers/search-numbers) ([How do I do this?](https://support.telnyx.com/en/articles/3562148-requesting-numbers))
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
* Ensure your Grandstream DP752 is on the [latest firmware](https://www.grandstream.com/support/firmware)

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Grandstream DP752/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Get your DP752's IP address

In this activity, you will get the IP address from your device so you can use it to set up your SIP account.

1. On DP72x/DP730 handset, press **Menu**.
2. Use arrow keys to reach **Status > Base Status**.
3. Press the **Select** softkey to display Info page, which will contain the IP address of your device. Hang onto this, because you'll need it in the next step.

[Back to Top](#h_f189d931af)

## 2. Set up your DP752 for traffic flow

In this activity, you will set up your device and link it to your Telnyx Mission Control Portal.

1. From your computer, open a browser and paste your device's IP address that you obtained in [step 1](#h_6df72972d6) into the address bar. You may need to prepend the address with *http://* which will take you to your DP750 Base Station.
2. You'll need to log in. For the initial login, you can use the default credentials:

   1. **Username:** *admin*
   2. **Password:** *admin*
3. From the left-hand navigation, expand **Profiles > Profile 1** and click **General Settings** to enter the following information:

   1. **Profile Active:** Select *Yes* unless you want the profile to remain inactive for the time being.
   2. **Profile Name:** Choose a name that makes sense for your purpose.
   3. **SIP Server:** *sip.telnyx.com*
   4. **Failover SIP Server:** *sip.telnyx.com* (Each SIP region has two SIP proxies. In the event of a failover, Telnyx will attempt to connect through the secondary IB SIP proxy.
   5. **Prefer Primary SIP Server:** Select *Yes*.
   6. **Outbound Proxy:** *sip.telnyx.com*
   7. **Voice Mail Access Number:** *\*97*

   ![Telnyx Mission Control Portal.](_images/9d58c4f3d5e6faca.png)
4. Click **Save**, then **Apply**.
5. From the left-hand navigation, expand **SIP Settings > Basic Settings** and change or confirm the following:

   1. **SIP Transport:** By default, *UDP* is selected. If you enabled TLS and your account is configured to use SRTP encryption as part of your [pre-requisite activities](#h_ee00c18dc4) then you should choose *TLS.*
   2. **Local SIP Port:** If you are using UDP transport, use port *5060*. If you are using TLS transport, use port *5061.*

   ![Telnyx Mission Control Portal Basic Settings. ](_images/286d43f6d0fa3239.png)
6. Click **Save**, then **Apply**.

[Back to Top](#h_f189d931af)

## 3. Configure codecs

In this step, you'll configure your [audio codecs](https://telnyx.com/resources/codecs-affect-voip-sound-quality).

1. From the left-hand navigation, expand **Profiles > Profile 1** and change or confirm the following:

   1. **Send DTMF:** Select *In-Audio* and *via RTP*.
   2. **SRTP Mode:** If you are using TLS encryption, select *Enabled and Forced*. Otherwise, leave as default.

   ![Telnyx Mission Control Portal Audio Settings. ](_images/38a2cc06849312a1.png)
2. Click **Save**, then **Apply**.

[Back to Top](#h_f189d931af)

## 4. Configure user accounts

In this step, you'll set up and configure up to 10 SIP accounts on your profile.

1. From the left-hand navigation, expand **DECT > SIP Account Settings** and configure the following for each account:

   1. **SIP User ID:** The Telnyx account ID
   2. **Authenticate ID:** The Telnyx account ID
   3. **Password:** The Telnyx account password
   4. **Name:** This is your caller ID. You can choose whatever you like, but keep in mind the following naming conventions:

      1. Caller ID Name should be in capital letters. This will appears more clearly/visible on some devices.
      2. You must NOT use any special characters, as they will not be displayed. Spaces are allowed.
      3. Some of regular Canadian providers will not show more than 15 characters. We suggest shrinking or adapt your caller ID.
   5. **Profile:** Choose the profile you created in [Step 2](#h_b882234ebb) (We named it Profile 1).
   6. **HS Mode:** The options here are

      1. *Circular mode*: all phones ring sequentially, starting with the phone after the one which rang last.
      2. *Linear mode:* all phones ring sequentially in the predetermined order, starting with the first phone each time.
      3. *Parallel mode:* all phones ring concurrently; after one phone answers, the remaining available phones can make new calls
      4. *Shared mode:* all phones ring concurrently and always share the same line (similar to analog phones).
      5. *Non-Hunting Group:* an account will be assigned to a single specific handset.
   7. **Active:** Whether or not the account is active. Typically will be *Yes*.

   ![Telnyx Mission Control Portal SIP Account Settings. ](_images/ab81b9d75d1f5883.png)
2. Click **Save**, then **Apply.**
3. From the left-hand navigation, expand **DECT > Handset Line Settings.**
4. Make sure the SIP account you just created in [Step 2](#h_b882234ebb) is selected in the Line 1 column for every handset.

   ![Handset Line Settings section. ](_images/1bd6eaa6eceb1da7.png)
5. Click **Save**, then **Apply**.

That's it! You've finished configuring your Grandstream DP752 IP Phone profile, and can now start testing calls!

[Back to Top](#h_f189d931af)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [User manual](https://www.grandstream.com/hubfs/Product_Documentation/DP750_DP720_User_Guide.pdf)
* [Admin manual](https://www.grandstream.com/hubfs/Product_Documentation/DP750_DP720_Administration_Guide.pdf)
* [DP750 FAQ](https://blog.grandstream.com/faq)
* [Firmware updates](https://www.grandstream.com/support/firmware)
* [Grandstream Helpdesk](https://helpdesk.grandstream.com/)
* [Grandstream community forum](https://forums.grandstream.com/)

---

Related Articles

[Grandstream GXP: Telnyx Setup](https://support.telnyx.com/en/articles/5815720-grandstream-gxp-telnyx-setup)[Grandstream GXP21XX](https://support.telnyx.com/en/articles/5819218-grandstream-gxp21xx)[Grandstream GXP1700: SIP Trunk](https://support.telnyx.com/en/articles/6184520-grandstream-gxp1700-sip-trunk)[Grandstream Wave Lite (Android)](https://support.telnyx.com/en/articles/6184897-grandstream-wave-lite-android)[Grandstream GXV3370](https://support.telnyx.com/en/articles/6187576-grandstream-gxv3370)

Did this answer your question?

😞😐😃

Table of contents
