---
source_url: https://support.telnyx.com/en/articles/6169513-grandstream-grp260x-sip-trunk
scraped: 2026-06-11
---

Grandstream GRP260x: SIP Trunk | Telnyx Help Center

[Skip to main content](#main-content)

# Grandstream GRP260x: SIP Trunk

Learn how to configure a Telnyx SIP trunk on the Grandstream GRP260x Series IP phones

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_31bc93499e)

Part of the GRP series of Carrier-Grade IP Phones, the [Grandstream GRP260x](https://content.grandstream.com/grp260x-introduction-webinar) is an essential 2-line model designed with zero-touch provisioning for mass deployment and easy management. It boasts some pretty cool features, including 5-way voice conferencing and dual band Wi-Fi support (GRP2602W only), EHS support for Plantronics, Jabra & Sennheiser headsets, as well as multi-language support. The GRP series includes carrier-grade security features that include secure boot, dual firmware images and encrypted data storage. For cloud provisioning and centralized management, the GRP260X is supported by [Grandstream’s Device Management System (GDMS)](https://www.grandstream.com/products/device-management/gdms/product/gdms), which provides a centralized interface to manage and monitor deployments of Grandstream endpoints.

|  |
| --- |
| ***Note:*** *This guide covers the GRP260x series of IP phones. For information about the* GRP261x, GRP262x & GRP263x series of phone, see this document. |

**Additional resources:**

* [GRP260x Series – Administration Guide](https://documentation.grandstream.com/knowledge-base/grp260x-series-administration-guide/)
* [GRP26xx – Firmware Upgrade Guide](https://documentation.grandstream.com/knowledge-base/grp26xx-firmware-upgrade-guide/)
* [GRP Series – Display Language Guide](https://documentation.grandstream.com/knowledge-base/grp-series-display-language-guide/)[GRP2601/P – Quick Installation Guide](https://documentation.grandstream.com/knowledge-base/grp2601-p-quick-installation-guide/)
* [GRP2602/P/W – Quick Installation Guide](https://documentation.grandstream.com/knowledge-base/grp2602-p-w-quick-installation-guide/)
* [GRP2603/P – Quick Installation Guide](https://documentation.grandstream.com/knowledge-base/grp2603-p-quick-installation-guide/)
* [GRP2604/P – Quick Installation Guide](https://documentation.grandstream.com/knowledge-base/grp2604-p-quick-installation-guide/)
* [Grandstream FAQ](https://blog.grandstream.com/faq)
* [Grandstream user forum](https://forums.grandstream.com/)
* [Helpdesk](https://helpdesk.grandstream.com/)

---

# Instructions for creating a SIP trunk on your Grandstream GRP 260x device

In this activity, you will:

1. [Configure a Telnyx SIP trunk on your device](#h_abd603805f)

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
* Use your phone's base or handset to find the device IP address. This IP address will link you to the web portal, where you will complete your configuration. See the [Grandstream GRP 260x Series admin guide](https://documentation.grandstream.com/knowledge-base/grp260x-series-administration-guide/#configuration-via-web-browser) to find your phone's IP address and obtain the default portal login credentials.

  + Note that you can also [establish a SIP trunk directly from your phone's keypad](https://documentation.grandstream.com/knowledge-base/grp260x-series-administration-guide/#configuration-via-keypad). You can find field values you'll need below.

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Grandstream GRP 260x IP phone /Telnyx configuration coming soon. Check back as we update our docs.* |

The Grandstream GRP 260x web portal has 9 configuration sections. While you may wish to change values across all of these sections, the ones that concern your Telnyx [SIP trunk](https://telnyx.com/products/sip-trunks) integration are:

* Status
* Account

|  |
| --- |
| ***Note:*** *The following settings are required to establish a SIP trunk with your Telnyx service. A full list of settings is available [here](https://documentation.grandstream.com/knowledge-base/grp260x-series-administration-guide/#configuration-guide).* |

## 1. Configure a Telnyx SIP trunk on your device

In this step, you'll create and register a SIP trunk that will connect your device to your Telnyx account or sub-account.

1. [Log into the Grandstream web portal](https://documentation.grandstream.com/knowledge-base/grp260x-series-administration-guide/#configuration-via-web-browser).
2. Navigate to the **Account** settings screen and use the following settings to configure your SIP trunk:  
   ​  
   In the **General Settings >** **Account Register** section:

   1. **Account Active:** Set as *Yes* if you plan to activate your new trunk as soon as it's set up.
   2. **Account Name:** Choose a name for your account. It will display in the phone's LCD screen.
   3. **SIP Server:** *sip.telnyx.com* (For US users. International users see [this table](https://sip.telnyx.com/#signaling-addresses).)
   4. **Secondary SIP Server:**  *64.16.250.10* (For US users. International users see [this table](https://sip.telnyx.com/#signaling-addresses).)
   5. **SIP User ID:** The SIP connection username. Learn more [here](https://support.telnyx.com/en/articles/4245868-sip-connection-types) in the Credentials Connection Setup section.
   6. **SIP Auth ID:** The SIP connection username. Learn more [here](https://support.telnyx.com/en/articles/4245868-sip-connection-types) in the Credentials Connection Setup section.
   7. **SIP Auth Password:** The SIP connection password. Learn more [here](https://support.telnyx.com/en/articles/4245868-sip-connection-types) in the Credentials Connection Setup section.
   8. **Name:** This is your caller ID. You can choose whatever you like, but keep in mind the following naming conventions:

      1. Caller ID Name should be in capital letters. This will appears more clearly/visible on some devices.
      2. You must NOT use any special characters, as they will not be displayed. Spaces are allowed.
      3. Some of regular Canadian providers will not show more than 15 characters. We suggest shrinking or adapt your caller ID.
   9. **Fallback Expiration:** Specifies the duration (in minutes) since failover to the current SIP server or Outbound Proxy before making failback attempts to the primary SIP server or Outbound Proxy.  
      ​

   In the **General Settings >** **Network Settings** section:

   1. **Outbound Proxy:** *sip.telnyx.com*
   2. **Max number of SIP request replies:** Sets the maximum number of retries for the device to send requests to the server. In DNS SRV configuration, if the destination address does not respond, all request messages are resent to the same address according to the configured retry times. Valid range: 1-10.  
      ​

   In the **SIP Settings > Basic Settings** section:

   1. **SIP registration:** Leave this setting enabled if you want your phone to send SIP Register messages to the proxy/server.
   2. **SIP transport:** The network protocol used for SIP transport. The default is *UDP*. If you plan to encrypt traffic, you can choose *TLS/TCP*, provided you've [configured your Telnyx portal to encrypt data](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication).
   3. **SIP listening mode:** Do you want your phone to listen to multiple SIP protocols? You have the option of choosing:

      1. *Dual:* If you've selected UDP, phone will also listen for TCP
      2. *Dual (Secured):* If you're transporting over UDP, phone will also listen for TLS/TCP. If TLS/TCP is selected, phone will also listen for UDP.
      3. *Dual (BLF Enforced)*
      4. *Transport* Only (Default)
   4. **Local SIP port:** UDP will use *5060*, TLS/TCP will use *5061*
3. Navigate to the Status page where you can check all your account details.

That's it, you've now completed the configuration of your Grandstream GRP260x device.  
​

[Back to Top](#h_31bc93499e)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally you can check out:

* [GRP260x Series – Administration Guide](https://documentation.grandstream.com/knowledge-base/grp260x-series-administration-guide/)
* [GRP26xx – Firmware Upgrade Guide](https://documentation.grandstream.com/knowledge-base/grp26xx-firmware-upgrade-guide/)
* [GRP Series – Display Language Guide](https://documentation.grandstream.com/knowledge-base/grp-series-display-language-guide/)[GRP2601/P – Quick Installation Guide](https://documentation.grandstream.com/knowledge-base/grp2601-p-quick-installation-guide/)
* [GRP2602/P/W – Quick Installation Guide](https://documentation.grandstream.com/knowledge-base/grp2602-p-w-quick-installation-guide/)
* [GRP2603/P – Quick Installation Guide](https://documentation.grandstream.com/knowledge-base/grp2603-p-quick-installation-guide/)
* [GRP2604/P – Quick Installation Guide](https://documentation.grandstream.com/knowledge-base/grp2604-p-quick-installation-guide/)
* [Grandstream FAQ](https://blog.grandstream.com/faq)
* [Grandstream user forum](https://forums.grandstream.com/)
* [Helpdesk](https://helpdesk.grandstream.com/)

---

Related Articles

[Grandstream UCM6xxx: SIP Trunks](https://support.telnyx.com/en/articles/5748258-grandstream-ucm6xxx-sip-trunks)[Grandstream GXP21XX](https://support.telnyx.com/en/articles/5819218-grandstream-gxp21xx)[Grandstream GRP2612: SIP Trunk](https://support.telnyx.com/en/articles/6184147-grandstream-grp2612-sip-trunk)[Grandstream GXP1700: SIP Trunk](https://support.telnyx.com/en/articles/6184520-grandstream-gxp1700-sip-trunk)[Grandstream GXV3370](https://support.telnyx.com/en/articles/6187576-grandstream-gxv3370)

Did this answer your question?

😞😐😃

Table of contents
