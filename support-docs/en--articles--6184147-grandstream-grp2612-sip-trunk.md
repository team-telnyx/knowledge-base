---
source_url: https://support.telnyx.com/en/articles/6184147-grandstream-grp2612-sip-trunk
title: "Grandstream GRP2612: SIP Trunk"
description: "Learn how to configure a Telnyx SIP trunk on your Grandstream GRP2612/GRP2612P/GRP2612W Series IP phone. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 9b9f42c71ba239b0f983b8e8725f32a9f2a07b616cf53fc7fddae9953448fba1
---







# Grandstream GRP2612: SIP Trunk

Learn how to configure a Telnyx SIP trunk on your Grandstream GRP2612/GRP2612P/GRP2612W Series IP phone. See Telnyx guidance and requirements.

C




[Jump to Instructions](#h_ccc918609d)

The Grandstream [GRP2612](https://www.grandstream.com/products/ip-voice-telephony/carrier-grade-ip-phones/grp-series-professional-ip-phones/product/grp2612-p-w-g)/[GRP2612P](https://www.grandstream.com/products/ip-voice-telephony/carrier-grade-ip-phones/grp-series-professional-ip-phones/product/grp2612-p-w-g)/[GRP2612W](https://www.grandstream.com/products/ip-voice-telephony/carrier-grade-ip-phones/grp-series-professional-ip-phones/product/grp2612-p-w-g) series of IP phones features 4 dual-color line keys which can be digitally programmed as up to 16 provisionable BLF/fast-dial keys. This series also boasts a 2.4” (320x240) TFT color LCD screen, 4 programmable context-sensitive soft keys, 100M network ports, integrated PoE (GRP2612P & GRP2612W only), integrated dual-band Wi-Fi (GRP2612W only), 3-way conference, and Electronic Hook Switch (EHS).

|  |
| --- |
| ***Note:*** *This guide covers the* GRP261x, GRP262x & GRP263x *series of IP phones. For information about the GRP260x*  series, see this document. |

**Additional resources:**

* [User Guide](https://documentation.grandstream.com/knowledge-base/grp260x-series-administration-guide/)
* [Administration Guide](https://documentation.grandstream.com/knowledge-base/grp261x-grp262x-grp263x-series-administration-guide/)
* [Firmware Upgrade Guide](https://documentation.grandstream.com/knowledge-base/grp26xx-firmware-upgrade-guide/)
* [Display Language Guide](https://documentation.grandstream.com/knowledge-base/grp-series-display-language-guide/)
* [GRP2670 – Quick Installation Guide](https://documentation.grandstream.com/knowledge-base/grp2670-quick-installation-guide/)
* [GRP2634 – Quick Installation Guide](https://documentation.grandstream.com/knowledge-base/grp2634-quick-installation-guide/)
* [GRP2624 – Quick Installation Guide](https://documentation.grandstream.com/knowledge-base/grp2624-quick-installation-guide/)
* [GRP2616 – Quick Installation Guide](https://documentation.grandstream.com/knowledge-base/grp2616-quick-installation-guide/)
* [Grandstream FAQ](https://blog.grandstream.com/faq)
* [Grandstream user forum](https://forums.grandstream.com/)
* [Helpdesk](https://helpdesk.grandstream.com/)

---

## Instructions for creating a SIP trunk on your Grandstream GRP2612/GRP2612P/GRP2612W device

In this activity, you will:

1. [Configure a Telnyx SIP trunk on your device](#h_2b54125331)

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
* Use your phone's base or handset to find the device IP address. This IP address will link you to the web portal, where you will complete your configuration. See the [Grandstream GRP2612/GRP2612P/GRP2612W Series admin guide](https://documentation.grandstream.com/knowledge-base/grp261x-grp262x-grp263x-series-administration-guide/#configuration-via-web-browser) to find your phone's IP address and obtain the default portal login credentials.

  + Note that you can also [establish a SIP trunk directly from your phone's keypad](https://documentation.grandstream.com/knowledge-base/grp261x-grp262x-grp263x-series-administration-guide/#configuration-via-keypad). You can find field values you'll need below.

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Grandstream* GRP2612/GRP2612P/GRP2612W *IP phone /Telnyx configuration coming soon. Check back as we update our docs.* |

The Grandstream GRP2612/GRP2612P/GRP2612W web portal has 9 configuration sections. While you may wish to change values across all of these sections, the ones that concern your Telnyx SIP trunk integration are:

* Status
* Account

|  |
| --- |
| ***Note:*** *The following settings are required to establish a SIP trunk with your Telnyx service. A full list of settings is available [here](https://documentation.grandstream.com/knowledge-base/grp261x-grp262x-grp263x-series-administration-guide/#configuration-guide).* |

## 1. Configure a Telnyx SIP trunk on your device

In this step, you'll create and register a SIP trunk that will connect your device to your Telnyx account or sub-account.

1. [Log into the Grandstream web portal](https://documentation.grandstream.com/knowledge-base/grp261x-grp262x-grp263x-series-administration-guide/#configuration-via-web-browser).
2. Navigate to the **Account** settings screen and use the following settings to configure your SIP trunk:

   ### **In the Account General Settings > Account Register section:**

   1. **Account Active:** Set as *Yes* if you plan to activate your new trunk as soon as it's set up.
   2. **Account Name:** Choose a name for your account. It will display in the phone's LCD screen.
   3. **SIP Server:** *sip.telnyx.com* (For US users. International users see [this table](https://sip.telnyx.com/#signaling-addresses).)
   4. **Secondary SIP Server:** *64.16.250.10* (For US users. International users see [this table](https://sip.telnyx.com/#signaling-addresses).)
   5. **Outbound Proxy:** *sip.telnyx.com*
   6. **SIP User ID:** The SIP connection username. Learn more [here](https://support.telnyx.com/en/articles/4245868-sip-connection-types) in the Credentials Connection Setup section.
   7. **SIP Authentication ID:** The SIP connection username. Learn more [here](https://support.telnyx.com/en/articles/4245868-sip-connection-types) in the Credentials Connection Setup section.
   8. **SIP Authentication Password:** The SIP connection password. Learn more [here](https://support.telnyx.com/en/articles/4245868-sip-connection-types) in the Credentials Connection Setup section.

   ### **In the Account General Settings > Account Dial Plan section:**

   1. **Name:** This is your caller ID. You can choose whatever you like, but keep in mind the following naming conventions:

      1. Caller ID Name should be in capital letters. This will appears more clearly/visible on some devices.
      2. You must NOT use any special characters, as they will not be displayed. Spaces are allowed.
      3. Some of regular Canadian providers will not show more than 15 characters. We suggest shrinking or adapt your caller ID.
   2. **Rule:** This will be your rule settings (number, pattern, prefix to add etc.)\
   3. **Type:** Choose the type of the rule (*pattern*, *block*, *dial now,* *prefix* or *second tone*).
      ​

   ### **In the Account General Settings > Network Settings section:**

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
         ​

   ### **In the Account General Settings > SIP Settings > Basic Settings section:**

   1. **SIP registration:** Leave this setting enabled if you want your phone to send SIP Register messages to the proxy/server.
   2. **Local SIP port:** UDP will use *5060*, TLS/TCP will use *5061*
   3. **SIP transport:** The network protocol used for SIP transport. The default is *UDP*. If you plan to encrypt traffic, you can choose *TLS/TCP*, provided you've [configured your Telnyx portal to encrypt data](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication).
   4. **SIP listening mode:** Do you want your phone to listen to multiple SIP protocols? You have the option of choosing:

      1. *Dual:* If you've selected UDP, phone will also listen for TCP
      2. *Dual (Secured):* If you're transporting over UDP, phone will also listen for TLS/TCP. If TLS/TCP is selected, phone will also listen for UDP.
      3. *Dual (BLF Enforced)*
      4. *Transport* Only (Default)
3. Navigate to the Status page where you can check all your account details.

That's it, you've now completed the configuration of your Grandstream GRP260x device.
​

[Back to Top](#h_ccc918609d)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally you can check out:

* [User Guide](https://documentation.grandstream.com/knowledge-base/grp260x-series-administration-guide/)
* [Administration Guide](https://documentation.grandstream.com/knowledge-base/grp261x-grp262x-grp263x-series-administration-guide/)
* [Firmware Upgrade Guide](https://documentation.grandstream.com/knowledge-base/grp26xx-firmware-upgrade-guide/)
* [Display Language Guide](https://documentation.grandstream.com/knowledge-base/grp-series-display-language-guide/)
* [GRP2670 – Quick Installation Guide](https://documentation.grandstream.com/knowledge-base/grp2670-quick-installation-guide/)
* [GRP2634 – Quick Installation Guide](https://documentation.grandstream.com/knowledge-base/grp2634-quick-installation-guide/)
* [GRP2624 – Quick Installation Guide](https://documentation.grandstream.com/knowledge-base/grp2624-quick-installation-guide/)
* [GRP2616 – Quick Installation Guide](https://documentation.grandstream.com/knowledge-base/grp2616-quick-installation-guide/)
* [Grandstream FAQ](https://blog.grandstream.com/faq)
* [Grandstream user forum](https://forums.grandstream.com/)
* [Helpdesk](https://helpdesk.grandstream.com/)

---

Related Articles

[Grandstream UCM6xxx: SIP Trunks](https://support.telnyx.com/en/articles/5748258-grandstream-ucm6xxx-sip-trunks)[Grandstream GXP21XX](https://support.telnyx.com/en/articles/5819218-grandstream-gxp21xx)[Grandstream GRP260x: SIP Trunk](https://support.telnyx.com/en/articles/6169513-grandstream-grp260x-sip-trunk)[Grandstream GXP1700: SIP Trunk](https://support.telnyx.com/en/articles/6184520-grandstream-gxp1700-sip-trunk)[Grandstream GXV3370](https://support.telnyx.com/en/articles/6187576-grandstream-gxv3370)

Did this answer your question?

😞😐😃
