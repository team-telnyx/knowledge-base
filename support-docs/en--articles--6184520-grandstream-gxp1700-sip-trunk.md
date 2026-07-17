---
source_url: https://support.telnyx.com/en/articles/6184520-grandstream-gxp1700-sip-trunk
title: "Grandstream GXP1700: SIP Trunk"
description: "Learn how to configure a Telnyx SIP trunk on your Grandstream GXP1700 Series IP phone. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: e2e6e884b2018d0849a4c4bbdbdb5a6a5f06183786c408d51208f565fa4605af
---







# Grandstream GXP1700: SIP Trunk

Learn how to configure a Telnyx SIP trunk on your Grandstream GXP1700 Series IP phone. See Telnyx guidance and requirements.

C




[Jump to Instructions](#h_34e62e341d)

|  |  |
| --- | --- |
| The [Grandstream GXP1760W](https://www.grandstream.com/products/ip-voice-telephony-gxp-series-ip-phones/gxp-series-mid-range-ip-phones/product/gxp1760w) is a mid-range IP phone with integrated dual-band Wi-Fi (GXP1760W only), a sleek design and moderate call-volume features. It comes equipped with 6 lines, 3 SIP accounts, 6 dual-color line keys and 4 XML programmable context sensitive soft keys on a 200 x 80 pixel (3.3”) back-lit LCD display screen. For added personalization the GXP1760W features personalized ring tone/ring back tone music and integration with advanced web and enterprise applications. The GXP1760W features dual auto-sensing 10/100Mbps network ports and offers automated provisioning features with media access control. This mid-range IP phone delivers outstanding performance and design to users worldwide at a budget-friendly price point. | The [Grandstream GXP1780/1782](https://www.grandstream.com/products/ip-voice-telephony-gxp-series-ip-phones/gxp-series-mid-range-ip-phones/product/gxp1780) is a powerful mid-range IP phone with advanced telephony features. This mid-range IP phone comes equipped with 8 lines, 4 SIP accounts, 8 dual-color line keys and 4 XML programmable context sensitive soft keys on a 200 x 80 pixel (3.3”) back-lit LCD display screen. For added personalization the GXP1780/1782 features personalized ring tone/ring back tone music and integration with advanced web and enterprise applications. It is also one of the first Grandstream phones to come equipped with a Kensington Security Slot— one of the most popular anti-theft solutions on the market. The GXP1780/1782 supports the fastest possible connection speeds with dual auto-sensing Gigabit network ports (on GXP1782 only) as well as automated provisioning features with media access control. The GXP1780/1782 is the perfect fit for users looking for a featured-pack IP phone that delivers high performance and design at an affordable price point. |

**Additional resources:**

* [GXP1700 series user Guide](https://documentation.grandstream.com/knowledge-base/gxp17xx-series-user-guide/)
* [GS Affinity user guide](https://documentation.grandstream.com/knowledge-base/gs-affinity-user-guide/)
* [Administration Guide](https://documentation.grandstream.com/knowledge-base/gxp17xx-series-administration-guide/)
* [Firmware Upgrade Guide](https://documentation.grandstream.com/knowledge-base/firmware-upgrade-guide/)
* [Display Language Guide](https://documentation.grandstream.com/knowledge-base/grp-series-display-language-guide/)
* [GXP1760W – Quick Installation Guide](https://documentation.grandstream.com/knowledge-base/gxp1760w-quick-installation-guide/)
* [GXP1780/1782 – Quick Installation Guide](https://documentation.grandstream.com/knowledge-base/gxp1780-1782-quick-installation-guide/)
* [Additional GXP1700 series documentation](https://documentation.grandstream.com/article-categories/gxp17xx/)
* [Grandstream FAQ](https://blog.grandstream.com/faq)
* [Grandstream user forum](https://forums.grandstream.com/)
* [Helpdesk](https://helpdesk.grandstream.com/)

---

## Instructions for creating a SIP trunk on your Grandstream GXP1700 device

In this activity, you will:

1. [Configure a Telnyx SIP trunk on your device](#h_515407d6b2)
2. [Configure audio settings](#h_4e860c55c8)

**Pre-Requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* [Purchase a DID](https://portal.telnyx.com/#/app/numbers/search-numbers)
* [Set up your Telnyx SIP connection](https://portal.telnyx.com/#/app/connections)
* [Provision your number](https://portal.telnyx.com/#/app/numbers/my-numbers) (Assign it to a SIP connection)
* [Create an outbound voice profile](https://portal.telnyx.com/#/app/outbound)
* Create a [credentials-based connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
* Ensure your phone is on the [most current firmware](https://documentation.grandstream.com/knowledge-base/grp26xx-firmware-upgrade-guide/)
* Connect your device to an ethernet port to establish an internet connection
* Use your phone's base or handset to find the device IP address. This IP address will link you to the web portal, where you will complete your configuration. See the [Grandstream GXP1700 Series admin guide](https://documentation.grandstream.com/knowledge-base/gxp17xx-series-administration-guide/#configuration-via-web-browser) to find your phone's IP address and obtain the default portal login credentials.

  + Note that you can also [establish a SIP trunk directly from your phone's keypad](https://documentation.grandstream.com/knowledge-base/gxp17xx-series-administration-guide/#configuration-via-keypad). You can find field values you'll need below.

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Grandstream* GXP1700 *IP phone /Telnyx configuration coming soon. Check back as we update our docs.* |

The Grandstream GXP1700 web portal has 9 configuration sections. While you may wish to change values across all of these sections, the ones that concern your Telnyx [SIP trunk](https://telnyx.com/products/sip-trunks) integration are:

* Status
* Account
* Settings

|  |
| --- |
| ***Note:*** *The following settings are required to establish a SIP trunk with your Telnyx service. A full list of settings is available [here](https://documentation.grandstream.com/knowledge-base/gxp17xx-series-administration-guide/#configuration-guide).* |

## 1. Configure a Telnyx SIP trunk on your device

In this step, you'll create and register a SIP trunk that will connect your device to your Telnyx account or sub-account.

1. ### **Log into the [Grandstream](https://documentation.grandstream.com/knowledge-base/gxp17xx-series-administration-guide/#configuration-via-web-browser) web portal.**
2. ### **Navigate to the "Account" screen.**
3. ### **In the "Account > General Settings" section:**

   1. **Account Active:** Set as *Yes* if you plan to activate your new trunk as soon as it's set up.
   2. **Account Name:** Choose a name for your account. It will display in the phone's LCD screen.
   3. **SIP Server:** *sip.telnyx.com* (For US users. International users see [this table](https://sip.telnyx.com/#signaling-addresses).)
   4. **Secondary SIP Server:** *64.16.250.10* (For US users. International users see [this table](https://sip.telnyx.com/#signaling-addresses).)
   5. **Outbound Proxy:** *sip.telnyx.com*
   6. **SIP User ID:** The SIP connection username. Learn more [here](https://support.telnyx.com/en/articles/4245868-sip-connection-types) in the Credentials Connection Setup section.
   7. **Authenticate ID:** The SIP connection username. Learn more [here](https://support.telnyx.com/en/articles/4245868-sip-connection-types) in the Credentials Connection Setup section.
   8. **Authenticate Password:** The SIP connection password. Learn more [here](https://support.telnyx.com/en/articles/4245868-sip-connection-types) in the Credentials Connection Setup section.
   9. **Name:** This is your caller ID. You can choose whatever you like, but keep in mind the following naming conventions:

      1. Caller ID Name should be in capital letters. This will appears more clearly/visible on some devices.
      2. You must NOT use any special characters, as they will not be displayed. Spaces are allowed.
      3. Some of regular Canadian providers will not show more than 15 characters. We suggest shrinking or adapt your caller ID.

   1. Rule: This will be your rule settings (number, pattern, prefix to add etc.)
   2. Type: Choose the type of the rule (*pattern*, *block*, *dial now,* *prefix* or *second tone*).
   3. Fallback Expiration: Specifies the duration (in minutes) since failover to the current SIP server or Outbound Proxy before making failback attempts to the primary SIP server or Outbound Proxy.
4. ### **In the "Account > Network Settings" section:**

   1. **DNS Mode:** This parameter controls how the Search Appliance looks up IP addresses for hostnames.
      There are four modes: *A Record* (default)*, SRV, NATPTR/SRV, Use Configured IP*.

      1. If you want to locate the server by DNS SRV, select *SRV* or *NATPTR/SRV*
      2. If *Use Configured IP* is selected, fill in the three fields below:

         * **Primary IP**
         * **Backup IP 1**
         * **Backup IP 2**
      3. If SIP server is configured as domain name, phone will not send DNS query, but select *Primary IP* or *Backup IP x* to send SIP message if at least one of them are not empty.
      4. Phone will try to use Primary IP first. After 3 tries without any response, it will switch to Backup IP x, and then it will switch back to Primary IP after 3 re-tries.
      5. If SIP server is already an IP address, phone will use it directly even *User Configured IP* is selected.
5. ### **In the "Account > SIP Settings > Basic Settings" section:**

   1. **SIP registration:** Leave this setting enabled if you want your phone to send SIP Register messages to the proxy/server.
   2. **Local SIP port:** UDP will use *5060*, TLS/TCP will use *5061*
   3. **SIP transport:** The network protocol used for SIP transport. The default is *UDP*. If you plan to encrypt traffic, you can choose *TLS/TCP*, provided you've [configured your Telnyx portal to encrypt data](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication).
   4. **SIP listening mode:** Do you want your phone to listen to multiple SIP protocols? You have the option of choosing:

      1. *Dual:* If you've selected UDP, phone will also listen for TCP
      2. *Dual (Secured):* If you're transporting over UDP, phone will also listen for TLS/TCP. If TLS/TCP is selected, phone will also listen for UDP.
      3. *Dual (BLF Enforced)*
      4. *Transport* Only (Default)

[Back to Top](#h_34e62e341d)

## 2. Configure audio settings

1. In the **Account** **> Audio Settings** section:

   1. **Preferred Vocoder:** The following is a list of codecs (both audio and video) that Telnyx supports:

      * *ulaw(g711u)*
      * *alaw(g711a)*
      * *g722*
      * *g729*
        ​**Note:** Using firmware version 1.0.0.43 or higher, users are now able to perform concurrent calls using G.729 codec as well.
2. Navigate to the **Settings** screen.
3. In the **Settings > General Settings** section:

   1. **STUN Server:** *stun.telnyx.com:3478*
4. Navigate to the Status page where you can check all your account details.

That's it, you've now completed the configuration of your Grandstream GXP1700 device.
​

[Back to Top](#h_34e62e341d)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally you can check out:

* [GXP1700 series user Guide](https://documentation.grandstream.com/knowledge-base/gxp17xx-series-user-guide/)
* [GS Affinity user guide](https://documentation.grandstream.com/knowledge-base/gs-affinity-user-guide/)
* [Administration Guide](https://documentation.grandstream.com/knowledge-base/gxp17xx-series-administration-guide/)
* [Firmware Upgrade Guide](https://documentation.grandstream.com/knowledge-base/firmware-upgrade-guide/)
* [Display Language Guide](https://documentation.grandstream.com/knowledge-base/grp-series-display-language-guide/)
* [GXP1760W – Quick Installation Guide](https://documentation.grandstream.com/knowledge-base/gxp1760w-quick-installation-guide/)
* [GXP1780/1782 – Quick Installation Guide](https://documentation.grandstream.com/knowledge-base/gxp1780-1782-quick-installation-guide/)
* [Additional GXP1700 series documentation](https://documentation.grandstream.com/article-categories/gxp17xx/)
* [Grandstream FAQ](https://blog.grandstream.com/faq)
* [Grandstream user forum](https://forums.grandstream.com/)
* [Helpdesk](https://helpdesk.grandstream.com/)

---

Related Articles

[Grandstream UCM6xxx: SIP Trunks](https://support.telnyx.com/en/articles/5748258-grandstream-ucm6xxx-sip-trunks)[Grandstream GXP21XX](https://support.telnyx.com/en/articles/5819218-grandstream-gxp21xx)[Grandstream GRP260x: SIP Trunk](https://support.telnyx.com/en/articles/6169513-grandstream-grp260x-sip-trunk)[Grandstream GRP2612: SIP Trunk](https://support.telnyx.com/en/articles/6184147-grandstream-grp2612-sip-trunk)[Grandstream GXV3370](https://support.telnyx.com/en/articles/6187576-grandstream-gxv3370)

Did this answer your question?

😞😐😃
