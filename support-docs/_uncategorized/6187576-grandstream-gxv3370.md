---
source_url: https://support.telnyx.com/en/articles/6187576-grandstream-gxv3370
scraped: 2026-06-11
---

Grandstream GXV3370 | Telnyx Help Center

[Skip to main content](#main-content)

# Grandstream GXV3370

Learn how to configure a Telnyx SIP trunk on the Grandstream GVX3370 (Android OS)

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_4aa8a80ba4)

The [GXV3370 IP Video Phone](https://www.grandstream.com/products/ip-video-telephony/ip-video-phones-android/product/gxv3370) for Android combines a 16-line IP video phone with a multi-platform video conferencing solution, all with the functionality of an Android tablet, to offer an all-in-one communications solution.

The GXV3370, which runs on the Android platform, features a 7” 1024×600 capacitive touch screen TFT LCD, camera, dual gigabit ports with PoE/PoE+, HD audio and video, integrated Wi-Fi (802.11a/b/g/n) and Bluetooth, and rich peripheral interfaces. It combines a state-of-the-art IP video phone, an advanced video conferencing solution, and the functionality of a tablet.

**Additional resources:**

* [User manual](https://documentation.grandstream.com/knowledge-base/gxv3370-user-guide/)
* [GS Affinity user manual](https://documentation.grandstream.com/knowledge-base/gs-affinity-user-guide/)
* [Admin manual](https://documentation.grandstream.com/knowledge-base/gxv3370-administration-guide/)
* [Firmware upgrade guide](https://documentation.grandstream.com/knowledge-base/firmware-upgrade-guide/)
* [All other GXV3370 reference material](https://documentation.grandstream.com/article-categories/gxv3370/)
* [Grandstream FAQ](https://blog.grandstream.com/faq)
* [Grandstream user forum](https://forums.grandstream.com/)
* [Helpdesk](https://helpdesk.grandstream.com/)

---

# Instructions for creating a SIP trunk on the Grandstream GXV3370 Video Phone

In this activity, you will:

1. [Configure a Telnyx SIP trunk on your device](#h_3aee2b2370)
2. [Configure codecs](#h_06b04eaf2f)

**Pre-Requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* [Purchase a DID](https://portal.telnyx.com/#/app/numbers/search-numbers)
* [Set up your Telnyx SIP connection](https://portal.telnyx.com/#/app/connections)
* [Provision your number](https://portal.telnyx.com/#/app/numbers/my-numbers) (Assign it to a SIP connection)
* [Create an outbound voice profile](https://portal.telnyx.com/#/app/outbound)
* Create a [credentials-based connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
* [Ensure your device is on the latest firmware](https://documentation.grandstream.com/knowledge-base/firmware-upgrade-guide/)
* Use your phone's base or handset to find the device IP address. This IP address will link you to the web portal, where you will complete your configuration. See the [Provisioning section of the Admin Guide](https://documentation.grandstream.com/knowledge-base/gxv3370-administration-guide/#upgrade-and-provisioning-configuration) to find your phone's IP address and obtain the default portal login credentials.  
  ​

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Grandstream GXV3370 Video Phone /Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Configure a Telnyx SIP trunk on your device

In this step, you'll create and register a [SIP trunk](https://telnyx.com/products/sip-trunks) that will connect your device to your Telnyx account or sub-account.

|  |
| --- |
| ***Note:*** *The following settings are required to establish a SIP trunk with your Telnyx service. A full list of settings is available [here](https://documentation.grandstream.com/knowledge-base/gxv3370-administration-guide/).* |

1. [Log into the Web GUI](https://documentation.grandstream.com/knowledge-base/gxv3370-administration-guide/#upgrade-and-provisioning-configuration).
2. Navigate to the **Account** screen and go to **General Settings**. In the **On Register** section, provide the following:

   1. **Account Active:** This switch determines if the account will become active once created. The default value for the first account is *Yes*.
   2. **Account Name:** Give your account a name that makes sense for your connection. In the example, we used *TelnyxTrunk*.
   3. **SIP Server:** *sip.telnyx.com* (for USA. For all other countries, see [this table](https://sip.telnyx.com/#signaling-addresses))
   4. **SIP User ID:** Your SIP account/sub-account ID
   5. **SIP Authentication ID:** The SIP connection username. Learn more [here](https://support.telnyx.com/en/articles/4245868-sip-connection-types) in the Credentials Connection Setup section.
   6. **SIP Password:** The SIP connection password. Learn more [here](https://support.telnyx.com/en/articles/4245868-sip-connection-types) in the Credentials Connection Setup section.
   7. **Display Name:** This is your caller ID. You can choose whatever you like, but keep in mind the following naming conventions:

      1. Caller ID Name should be in capital letters. This will appears more clearly/visible on some devices.
      2. You must NOT use any special characters, as they will not be displayed. Spaces are allowed.
      3. Some of regular Canadian providers will not show more than 15 characters. We suggest shrinking or adapt your caller ID.
   8. **VoiceMail Access Number:** Configure the voicemail user ID to retrieve voicemail by pressing Listen on the message screen. This user ID is usually the VM portal access number (ie: *\*97*)
   9. **Outbound Proxy:** *sip.telnyx.com*
3. Still on the **Account** screen, go to **SIP Settings** In the **SIP Basic Settings** section, provide the following:

   1. **SIP registration:** Leave this setting enabled if you want your phone to send SIP Register messages to the proxy/server.
   2. **SIP transport:** The network protocol used for SIP transport. The default is *UDP*. If you plan to encrypt traffic, you can choose *TLS/TCP*, provided you've [configured your Telnyx portal to encrypt data](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication).
   3. **Local SIP port:** UDP will use *5060*, TLS/TCP will use *5061*

[Back to Top](#h_4aa8a80ba4)

## 2. Configure codecs

In this section, you'll configure your codecs for audio calling.

1. Still on the **Account** screen, go to **Codec Settings** In the **Preferred Vocoder** section, provide the following:

   1. **Preferred Vocoder:** Select the codecs to be used on WiFi, 2, 3, and 4G. The following is a list of codecs (both audio and video) that Telnyx supports:

      **Audio:**

      * *ulaw(g711u)*
      * *alaw(g711a)*
      * *g722*
      * *g729*
   2. **DTMF:** *RFC2833*
2. In the **Preferred Video Codec** section, provide the following:

   1. **Preferred Video Codec:** *H264*

That's it, you've now completed the configuration of your Grandstream GXV3370 Video Phone with your Telnyx account.  
​

[Back to Top](#h_4aa8a80ba4)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally you can check out:

* [User manual](https://documentation.grandstream.com/knowledge-base/gxv3370-user-guide/)
* [GS Affinity user manual](https://documentation.grandstream.com/knowledge-base/gs-affinity-user-guide/)
* [Admin manual](https://documentation.grandstream.com/knowledge-base/gxv3370-administration-guide/)
* [Firmware upgrade guide](https://documentation.grandstream.com/knowledge-base/firmware-upgrade-guide/)
* [All other GXV3370 reference material](https://documentation.grandstream.com/article-categories/gxv3370/)
* [Grandstream FAQ](https://blog.grandstream.com/faq)
* [Grandstream user forum](https://forums.grandstream.com/)
* [Helpdesk](https://helpdesk.grandstream.com/)

---

Related Articles

[Grandstream UCM6xxx: SIP Trunks](https://support.telnyx.com/en/articles/5748258-grandstream-ucm6xxx-sip-trunks)[Grandstream GXP21XX](https://support.telnyx.com/en/articles/5819218-grandstream-gxp21xx)[Grandstream GRP260x: SIP Trunk](https://support.telnyx.com/en/articles/6169513-grandstream-grp260x-sip-trunk)[Grandstream GXP1700: SIP Trunk](https://support.telnyx.com/en/articles/6184520-grandstream-gxp1700-sip-trunk)[Grandstream Wave Lite (iPhone)](https://support.telnyx.com/en/articles/6184748-grandstream-wave-lite-iphone)

Did this answer your question?

😞😐😃

Table of contents
