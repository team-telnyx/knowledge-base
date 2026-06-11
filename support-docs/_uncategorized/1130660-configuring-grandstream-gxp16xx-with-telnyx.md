---
source_url: https://support.telnyx.com/en/articles/1130660-configuring-grandstream-gxp16xx-with-telnyx
scraped: 2026-06-11
---

Configuring Grandstream GXP16XX with Telnyx | Telnyx Help Center

[Skip to main content](#main-content)

# Configuring Grandstream GXP16XX with Telnyx

In this article we will explain how to configure Grandstream GXP1620/GXP1625 and GXP1630 with the Telnyx Mission Control portal.

C

Written by Customer Success

October 18, 2023

Table of contents

[Jump to Instructions](#h_b1174ea24e)

The [Grandstream GXP1620/GXP1625 IP phones](https://www.grandstream.com/products/ip-voice-telephony-gxp-series-ip-phones/gxp-series-basic-ip-phones/product/gxp1620/gxp1625) are geared specifically for small to mid-sized businesses and feature effective and essential functionalities to create an easy-to-use experience for a user with light to medium call volume. Its focus on essential features and standard call support makes the GXP1620/25 a versatile and dependable phone.

Additional documentation:

* [Product datasheet (English)](https://www.grandstream.com/hubfs/Product_Documentation/datasheet_gxp1620_1625_english.pdf?hsLang=en)
* [Grandstream firmware updates](https://www.grandstream.com/support/firmware)
* [GXP16XX product documentation](https://www.grandstream.com/hubfs/Product_Documentation/gxp16xx_administration_guide.pdf)
* [Grandstream FAQ](https://blog.grandstream.com/faq)
* [Grandstream user forum](https://forums.grandstream.com/)
* [Grandstream Learning Center](https://www.grandstream.com/learning-center)

---

# Instructions for configuring your Grandstream GXP 1625

In this activity you will:

1. [Log into your Grandstream UI](#h_79bca1329c)
2. [Create a SIP trunk](#h_eceaea9c8f)
3. [Configure codec preferences](#h_a10b5e6922)

**Pre-requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* [Purchase a DID](https://portal.telnyx.com/#/app/numbers/search-numbers)
* [Set up your Telnyx SIP connection](https://portal.telnyx.com/#/app/connections)
* [Provision your number](https://portal.telnyx.com/#/app/numbers/my-numbers) (Assign it to a SIP connection)
* [Create an outbound voice profile](https://portal.telnyx.com/#/app/outbound)
* Create an [IP connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal
* Ensure your Grandstream device is running [the latest firmware](https://www.grandstream.com/support/firmware)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Grandstream GXP/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Log into your Grandstream web UI

All the configuration you'll need to do will take place on the web UI, which acts as an interface between you and your Grandstream device. You can access the web UI via the device's IP address. We'll find that, then use it to log in.

1. The IP address used to access the web UI depends on where the user’s computer is connected.

   1. If the computer is connected to *the same switch/router that the UCM6200 series WAN port is connected*, then browse to the IP address that is displayed on the UCM6200 series LCD. This address is the *WAN IP*.
   2. If the computer is connected *to the LAN side of the UCM6200 series*, then users would browse to the default IP of the UCM6200 series which is *192.168.2.1*.
2. If connected successfully, the UCM6200 series login page. Out of the box, your device will have the following default credentials:

   1. **Username**: *admin*
   2. **Password**: *admin*  
      ​*HOWEVER: Units manufactured starting January 2017 have a unique random password printed on the sticker located on the back of the unit.*

      [![Grandstream web UI interface. ](https://downloads.intercomcdn.com/i/o/33534240/0928255a4382f29af9892961/gxp1625_01.png?expires=1781167500&signature=38e8d96508a6d41eff6306950514ee7b8ee1e53735fe31d396b990d9ad3fa9ac&req=dyMiFc18mYETWLcX3D%2B5huU9mTWhXs0x917LItIeWDf1YgQxZIjRxgirS1KY%0A6Q%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/33534240/0928255a4382f29af9892961/gxp1625_01.png?expires=1781167500&signature=38e8d96508a6d41eff6306950514ee7b8ee1e53735fe31d396b990d9ad3fa9ac&req=dyMiFc18mYETWLcX3D%2B5huU9mTWhXs0x917LItIeWDf1YgQxZIjRxgirS1KY%0A6Q%3D%3D%0A)

[Back to Top](#h_b1174ea24e)

## 2. Create a SIP trunk

In this section, we're going to create a new [SIP trunk](https://telnyx.com/products/sip-trunks) that will connect your Grandstream device with your Telnyx account.

1. From the top navigation, select **Accounts**.
2. From here, select **Accounts 1**, then **General Settings** in left-hand navigation.

   [![Accounts section of the Grandstream web portal. ](https://downloads.intercomcdn.com/i/o/440969328/287cd351ac5ec9f495efb462/accounts.png?expires=1781167500&signature=dc6c5ef540c8b333c2866a18107d8d4db623f3bc4d644d12d4be78982c63eaae&req=cCQnH893noNXFb4f3HP0gAiHhYU4Y5ad0dOyUy0peDPH8mfj%2BXtZsX%2FZO5pi%0AgVY%3D%0A)](https://downloads.intercomcdn.com/i/o/440969328/287cd351ac5ec9f495efb462/accounts.png?expires=1781167500&signature=dc6c5ef540c8b333c2866a18107d8d4db623f3bc4d644d12d4be78982c63eaae&req=cCQnH893noNXFb4f3HP0gAiHhYU4Y5ad0dOyUy0peDPH8mfj%2BXtZsX%2FZO5pi%0AgVY%3D%0A)
3. Provide the following information to configure this account.

   1. **SIP Server:** *sip.telnyx.com*
   2. **Outbound Proxy:** *sip.telnyx.com*
   3. **SIP User ID:** Your Telnyx SIP account username
   4. **Authenticate ID:** Your Telnyx SIP account password

      [![Account configuration in General Settings. ](https://downloads.intercomcdn.com/i/o/440970187/6043ef4a02b8e41c23db76f8/1.png?expires=1781167500&signature=96224ebc7302274703633b7cbf92cf8f5cc8068398316d2b4c18e16b64ab3d91&req=cCQnH85%2BnIlYFb4f3HP0gGQnYwUNJW2ooxYtTdDlBbKzzyNGN1ROsBTnNzqb%0AHIY%3D%0A)](https://downloads.intercomcdn.com/i/o/440970187/6043ef4a02b8e41c23db76f8/1.png?expires=1781167500&signature=96224ebc7302274703633b7cbf92cf8f5cc8068398316d2b4c18e16b64ab3d91&req=cCQnH85%2BnIlYFb4f3HP0gGQnYwUNJW2ooxYtTdDlBbKzzyNGN1ROsBTnNzqb%0AHIY%3D%0A)
4. Now select **Network Settings** from **Accounts 1** in left-hand navigation and provide the following:

   1. **DNS Mode:** *A Record*
   2. **NAT Traversal:** *Keep-Alive*
5. Next, select **SIP Settings > Basic Settings** from **Accounts 1** in left-hand navigation and make sure the following are set according to your encryption/transport settings in your Telnyx Mission Control Portal:

   1. **Local SIP Port:** *5060* if you have not enabled TLS encryption. If you have, choose *5061*
   2. **SIP Transport:** *UDP* or *TCP* if you have not enabled TLS encryption. If you have, choose *TLS/TCP*.

      [![Network settings in the Grandstream web UI. ](https://downloads.intercomcdn.com/i/o/440971419/885c25702a06876f0b54cd9d/3.png?expires=1781167500&signature=ebb46e2047f5087e20fcac5a9580b98ca03d4579d5d9e6d5ddd34b752da50723&req=cCQnH85%2FmYBWFb4f3HP0gOUVlKYpDKtS7GnAB4%2F40QEKz5MqNrWEf%2BVf4HiA%0Aqmo%3D%0A)](https://downloads.intercomcdn.com/i/o/440971419/885c25702a06876f0b54cd9d/3.png?expires=1781167500&signature=ebb46e2047f5087e20fcac5a9580b98ca03d4579d5d9e6d5ddd34b752da50723&req=cCQnH85%2FmYBWFb4f3HP0gOUVlKYpDKtS7GnAB4%2F40QEKz5MqNrWEf%2BVf4HiA%0Aqmo%3D%0A)

## 3. Configure codec preferences

In this section, you'll select the codecs you'll use for audio calling.

1. Select **Audio Settings** from **Accounts 1** in left-hand navigation to set your codec preferences. You can choose any Telnyx-supported [audio codecs](https://telnyx.com/resources/codecs-affect-voip-sound-quality):

   1. ulaw(g711u)
   2. alaw(g711a)
   3. g722
   4. g729

That's it, you've now completed the configuration of your Grandstream and can now make and receive calls by using Telnyx as your SIP provider!

[Back to Top](#h_b1174ea24e)

## Troubleshooting

## 1. Outgoing call issues

Are you able to receive incoming calls but outgoing calls are failing with a *No response* error? Try this:

1. Login into your device's settings and head to **Accounts > Account X > SIP > Custom SIP Header** and disable the following:

   * **Use X-Grandstream-PBX Header**
   * **Use P-Access-Network-Info Header**
   * **Use P-Emergency-Info Header**
2. Go to **Accounts > Account X > SIP > Audio Settings**, and choose codec *G729A/B* as preferred Vocoder and the rest with *PCMU*.

[Back to Top](#h_b1174ea24e)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally, you can check out:

* [Product datasheet (English)](https://www.grandstream.com/hubfs/Product_Documentation/datasheet_gxp1620_1625_english.pdf?hsLang=en)
* [Grandstream firmware updates](https://www.grandstream.com/support/firmware)
* [GXP16XX product documentation](https://www.grandstream.com/hubfs/Product_Documentation/gxp16xx_administration_guide.pdf)
* [Grandstream FAQ](https://blog.grandstream.com/faq)
* [Grandstream user forum](https://forums.grandstream.com/)
* [Grandstream Learning Center](https://www.grandstream.com/learning-center)

---

## Can't find what you're looking for? Click the chat bubble at your lower right hand corner and start a chat!

---

Related Articles

[Grandstream HT802: Telnyx Setup](https://support.telnyx.com/en/articles/5725071-grandstream-ht802-telnyx-setup)[Grandstream GXP: Telnyx Setup](https://support.telnyx.com/en/articles/5815720-grandstream-gxp-telnyx-setup)[Grandstream GXP21XX](https://support.telnyx.com/en/articles/5819218-grandstream-gxp21xx)[Grandstream Wave Lite (iPhone)](https://support.telnyx.com/en/articles/6184748-grandstream-wave-lite-iphone)[Grandstream GXV3370](https://support.telnyx.com/en/articles/6187576-grandstream-gxv3370)

Did this answer your question?

😞😐😃

Table of contents
