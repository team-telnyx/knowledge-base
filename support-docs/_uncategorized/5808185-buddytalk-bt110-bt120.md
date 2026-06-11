---
source_url: https://support.telnyx.com/en/articles/5808185-buddytalk-bt110-bt120
scraped: 2026-06-11
---

BuddyTalk BT110/BT120 | Telnyx Help Center

[Skip to main content](#main-content)

# BuddyTalk BT110/BT120

Learn how to configure BuddyTalk BT110 to work with Telnyx to make and receive calls.

C

Written by Customer Success

July 2, 2024

Table of contents

[Jump to Instructions](#h_bffe0bad15)

[BuddyTalk](https://www.innomedia.com/buddytalk-product-family/), powered by the Amazon Alexa Voice Service (AVS) and Alexa Communication (ACM), is an intelligent speakerphone and smartspeaker which can be configured to allow a VoIP subscription to deliver incoming and outgoing calls. BuddyTalk is equipped with advanced audio processing and has VoIP capability, all while delivering fantastic calling flexibility, superior voice quality, and strong security.

|  |
| --- |
| ***Note:*** *For an even more rich experience with your BuddyTalk BT product, consider the BuddyTalk Mobile App after you have completed this setup.* |

Additional documentation:

* [BT110 user documentation](https://www.innomedia.com/buddytalk-product-family/)
* [BT120 user documentation](https://www.innomedia.com/buddytalk-product-family/)
* [BT200 user documentation](https://www.innomedia.com/buddytalk-product-family/)
* BT110 features
* [BT120 features](https://www.innomedia.com/buddytalk-product-family/)
* BT110 specifications
* [BT120 specifications](https://www.innomedia.com/buddytalk-product-family/)
* BuddyTalk FAQs
* [BuddyTalk setup page](https://www.innomedia.com/buddytalk-product-family/)

---

# Instructions for configuring BuddyTalk BT110/120 to work with Telnyx

In this activity you will:

1. [Set up your BuddyTalk profile](#h_d1d59c4d95)
2. (OPTIONAL) [Encrypt traffic by enabling TLS](#h_166c2b7a3b)
3. [Have some fun with Alexa!](#h_6d2bc31771)

**Pre-requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* [Provision a DID from Telnyx](https://portal.telnyx.com/#/app/numbers/search-numbers) ([How do I do this?](https://support.telnyx.com/en/articles/3562148-requesting-numbers))
* RECOMMENDED: [Enable TLS if you want to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
* An Amazon account with Comm. enabled
* The Alexa app enabled
* The BuddyTalk Setup App

  + **Android App:** Google Play Store  
    \**The App is supported on phones and tablets running Android 4.4.4 and above.*
  + **iOS App:** [Apple App Store](https://apps.apple.com/us/app/buddytalk-setup/id1434349567)   
    ​*\*The Setup App is supported on phones and tablets running iOS version 12 and above.*
* Appropriate network setup

  + Ensure that your firewall is open for SIP communication on port 5060
* Make sure you can access the [BuddyTalk web console](https://www.innomedia.com/buddytalk-product-family/)
* See details about BuddyTalk deployment pre-requisites [here](https://www.innomedia.com/buddytalk-product-family/).

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

Setting up BuddyTalk through the BuddyTalk Setup App:

|  |
| --- |
| ***Note:*** *Video walkthrough for BuddyTalk/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Set up your BuddyTalk profile

In this step, you will set up your Telnyx account in BuddyTalk.

1. Open your BuddyTalk Setup App and work through the first two setup steps. [The BuddyTalk video](#h_38d4406f4f) can also help with this.
2. On the third step, you will be taken the **Setup Telephony** screen. Provide the following information:

   1. **Name:** Enter your outbound Caller ID name. Use the following naming conventions to choose this:

      1. Caller ID Name should be in **capital letters**. This will appears more clearly/visible on some devices.
      2. You **must NOT use any special characters**, as they will not be displayed. Spaces are allowed.
      3. Some of regular **Canadian providers will not show more than 15 characters**. We suggest shrinking or adapt your caller ID.
   2. **Account ID:** Your Telnyx SIP account ID
   3. **Auth ID:** Your Telnyx SIP account ID
   4. **Password:** Your Telnyx SIP account password
   5. **Domain:** *sip.telnyx.com*
   6. **Outbound proxy (optional):** Toggle this switch to enable outbound proxy
   7. **Proxy (optional):** *sip.telnyx.com*
   8. **Local SIP Port:** *5060*
   9. **Preferred Transport:** *UDP* (default).   
      ​  
      ​**Note that** if you are planning to encrypt calls and have [set up call encryption on your Telnyx portal](#h_e14c90ac20), you should choose *TLS*.

   [![Telnyx account in BuddyTalk](https://downloads.intercomcdn.com/i/o/433696776/3a8a876349de29a4702a1c4f/1.png?expires=1781168400&signature=d4a7fe971867ef14290a621e0b6ef14db607d197bb2d0b8d97042902cd740302&req=cCMkEMB4moZZFb4f3HP0gEjZc2sDqqApXbPHPiuYqZOll5T4oNva7%2BoG2jEN%0ALJc%3D%0A)](https://downloads.intercomcdn.com/i/o/433696776/3a8a876349de29a4702a1c4f/1.png?expires=1781168400&signature=d4a7fe971867ef14290a621e0b6ef14db607d197bb2d0b8d97042902cd740302&req=cCMkEMB4moZZFb4f3HP0gEjZc2sDqqApXbPHPiuYqZOll5T4oNva7%2BoG2jEN%0ALJc%3D%0A)
3. After your SIP registration is complete, you should see the phone icon in the upper left corner turn green. Additionally, the phone LED on top of your device will change from red, to green, before turning off.

[Return to Top](#h_bffe0bad15)

## 2. (OPTIONAL) Encrypt traffic by enabling TLS

In this step, we will configure SIP TLS-SRTP traffic encryption on BuddyTalk, as this is recommended.

1. Log into the [BuddyTalk Web Console](https://www.innomedia.com/buddytalk-product-family/)
2. Click on **Telephony** in the top navigation.
3. In the left-hand menu, click **Profile Config**.
4. Find the profile you just created and click the edit link (This is the PENCIL icon)

   [![Telephony section of the BuddyTalk Web Console. ](https://downloads.intercomcdn.com/i/o/433697130/e1a6c4198464fe5e17a9e9f5/2.png?expires=1781168400&signature=660827fb31950d3370001497e93660da4e54df9f4ca9ab4376b1da361287440b&req=cCMkEMB5nIJfFb4f3HP0gFkhLCBn8PPQ1Zv4PMtDLsznBf2AjwixhoqE4eP9%0AM1s%3D%0A)](https://downloads.intercomcdn.com/i/o/433697130/e1a6c4198464fe5e17a9e9f5/2.png?expires=1781168400&signature=660827fb31950d3370001497e93660da4e54df9f4ca9ab4376b1da361287440b&req=cCMkEMB5nIJfFb4f3HP0gFkhLCBn8PPQ1Zv4PMtDLsznBf2AjwixhoqE4eP9%0AM1s%3D%0A)
5. On the **Edit** screen, find the **SIP Proxy Server** section.
6. Find the **Preferred Transport Protocol** field and select *TLS*.

   [![SIP Server Setting Section. ](https://downloads.intercomcdn.com/i/o/433697309/cbe011108602a659d49e712c/3.png?expires=1781168400&signature=ca9482c97751236d25a40f9c6ea2a14d52d7401f644e92db2f8b0f0366f99e6f&req=cCMkEMB5noFWFb4f3HP0gA6qNI4MgjBaG1qCKbSEzvgdDya2SYzuD4YbJFjt%0ADS4%3D%0A)](https://downloads.intercomcdn.com/i/o/433697309/cbe011108602a659d49e712c/3.png?expires=1781168400&signature=ca9482c97751236d25a40f9c6ea2a14d52d7401f644e92db2f8b0f0366f99e6f&req=cCMkEMB5noFWFb4f3HP0gA6qNI4MgjBaG1qCKbSEzvgdDya2SYzuD4YbJFjt%0ADS4%3D%0A)
7. In the left-hand menu, click on **Port Config**.
8. Find the profile you just created and click the edit link (This is the PENCIL icon)
9. On the **Edit** screen, find the **Line Setting > Line Options** section.
10. Find the **Secure RTP** field and select *SDES*.

    [![Port configuration settings. ](https://downloads.intercomcdn.com/i/o/433697466/3fd8e63e55d29dc2ea5af10e/5.jpeg?expires=1781168400&signature=72bd74fc637724664395dae19be02723b88ffae0ce52b73f92757d65d2d238da&req=cCMkEMB5mYdZFb4f3HP0gF1C9KJwc1LYJ3U9o6k9NtfLoxllH0%2B8w7%2BEC7YR%0Aqrw%3D%0A)](https://downloads.intercomcdn.com/i/o/433697466/3fd8e63e55d29dc2ea5af10e/5.jpeg?expires=1781168400&signature=72bd74fc637724664395dae19be02723b88ffae0ce52b73f92757d65d2d238da&req=cCMkEMB5mYdZFb4f3HP0gF1C9KJwc1LYJ3U9o6k9NtfLoxllH0%2B8w7%2BEC7YR%0Aqrw%3D%0A)

[Back to Top](#h_bffe0bad15)

## 3. Have some fun with Alexa!

Now that you're set up and ready to go, let's learn some useful Alexa voice commands. Start by trying some of these:

* Calling (dialing a number): *"Alexa call (some number)"*
* Calling (by contact): *"Alexa, call (name)"*
* Answer a call: "*Alexa, answer call."*
* Disconnect a call: *"Alexa, hang up."*

You can also use all your other [Alexa skills and commands](https://www.amazon.com/alexa-skills/b?ie=UTF8&node=13727921011), even if they're not related to making or managing calls.

That's it! You're all set up to start using BuddyTalk BT with Telnyx.

[Back to Top](#h_bffe0bad15)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [BT110 user documentation](https://www.innomedia.com/buddytalk-product-family/)
* [BT120 user documentation](https://www.innomedia.com/buddytalk-product-family/)
* [BT200 user documentation](https://www.innomedia.com/buddytalk-product-family/)
* BT110 features
* [BT120 features](https://www.innomedia.com/buddytalk-product-family/)
* BT110 specifications
* [BT120 specifications](https://www.innomedia.com/buddytalk-product-family/)
* [BuddyTalk FAQs](https://www.innomedia.com/buddytalk-product-family/)
* [BuddyTalk setup page](https://www.innomedia.com/buddytalk-product-family/)

---

Related Articles

[Gigaset A510: Telnyx Setup](https://support.telnyx.com/en/articles/5815209-gigaset-a510-telnyx-setup)[Audiocodes 400HD](https://support.telnyx.com/en/articles/5819923-audiocodes-400hd)[Cisco: 68xx/88xx Setup](https://support.telnyx.com/en/articles/5820309-cisco-68xx-88xx-setup)[Fanvil H5: Hotel IP](https://support.telnyx.com/en/articles/6203401-fanvil-h5-hotel-ip)[Fanvil X2CP/X2C/X2P: Call Center IP](https://support.telnyx.com/en/articles/6206756-fanvil-x2cp-x2c-x2p-call-center-ip)

Did this answer your question?

😞😐😃

Table of contents
