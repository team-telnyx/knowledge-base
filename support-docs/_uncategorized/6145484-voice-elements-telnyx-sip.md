---
source_url: https://support.telnyx.com/en/articles/6145484-voice-elements-telnyx-sip
scraped: 2026-06-11
---

Voice Elements: Telnyx SIP | Telnyx Help Center

[Skip to main content](#main-content)

# Voice Elements: Telnyx SIP

Voice Elements, a Microsoft .NET development environment released by Inventive Labs Corporation in 2008.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to instructions](#h_dc214f2b78)

Voice Elements is a Microsoft .NET development environment for building automated telephone systems. Voice Elements was released by Inventive Labs Corporation in 2008, based on their original CTI32 toolkit. Software developers who use C#, VB.NET or Delphi use Voice Elements to write telephony-based applications, such as Interactive Voice Response systems, voice dialers, auto attendants, call centers and more.

The Voice Elements Dashboard has several SIP and PBX connection options to choose from. In this article, we cover how to connect to Telnyx and leverage it as a SIP provider.

**Additional resources:**

* [Voice Elements documentation](https://www.voiceelements.com/docs/)
* [Contact Voice Elements support](https://www.voiceelements.com/contact/)
* [Try Voice Elements for free](https://www.voiceelements.com/demo/)
* [Getting started with Telnyx](https://sip.telnyx.com/#signaling-addresses)

---

# Instructions for configuring Voice Elements to use Telnyx as a SIP provider

In this activity you will:

1. [Create a Telnyx SIP trunk in Voice Elements](#h_f2bdaff90f)
2. [Test your firewall](#h_d08e0a65e7)

**Pre-requisites**

* Your Telnyx Portal must be correctly [set up and configured for use](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* [Download and install](https://www.voiceelements.com/docs/premise-guide/installing-voice-elements-premise-software/) Voice Elements
* **(Optional)** If you're planning to use TLS encryption, you'll need to enable TLS encryption in your Telnyx portal. To learn more about TLS and other VoIP security topics, see [this article](https://support.telnyx.com/en/articles/4404575-tls-and-srtp).  
  ​

**Video walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

## 1. Create a Telnyx SIP trunk in Voice Elements

In this section, you will connect Voice Elements to Telnyx so you can use Telnyx as your SIP provider.

1. Open the Voice Elements wizard and select the **Connectivity** tab.
2. In the **Carrier/Gateway/Devices** section, select the *Other* option.
3. In the **Location** section, select the *External IP Authentication (SIP Carrier - Preferred)* option.

   [![Connectivity tab on the Voice Elements wizard. ](https://downloads.intercomcdn.com/i/o/498714105/5d9e90c4ee66901be2d7c802/VE-Premise-Wizard-Connectivity-Other-External-IP-Registrar.png?expires=1781168400&signature=e73877a69958dec821a2449a2b23417004f9c12d6080297f84c53c761586886b&req=cCkvEch6nIFaFb4f3HP0gIH8NXjf1nhXT0aX6mPJwxCr8wsjPv5M8VA85TDz%0Aj0M%3D%0A)](https://downloads.intercomcdn.com/i/o/498714105/5d9e90c4ee66901be2d7c802/VE-Premise-Wizard-Connectivity-Other-External-IP-Registrar.png?expires=1781168400&signature=e73877a69958dec821a2449a2b23417004f9c12d6080297f84c53c761586886b&req=cCkvEch6nIFaFb4f3HP0gIH8NXjf1nhXT0aX6mPJwxCr8wsjPv5M8VA85TDz%0Aj0M%3D%0A)
4. You'll need to enter Telnyx's connection information in the text boxes below. Enter the following information:

   1. **Destination IP/URL:** *sip.telnyx.com* (In the USA, for other countries, use your top-level domain extension. If you're uncertain, you can find them [here](https://sip.telnyx.com/#signaling-addresses).)
   2. Public and local IPs will be populated already. You can leave these alone.
5. Once you enter Telnyx's IP or URL, you'll be asked to provide additional information:

   1. **Registrar IP/URL:** *sip:sip.telnyx.com*
   2. **AuthURI:** your\_telnyx\_username*@sip.telnyx.com*
   3. **Username:** The SIP connection username. Learn more [here](https://support.telnyx.com/en/articles/4245868-sip-connection-types) in the Credentials Connection Setup section.
   4. **Pwd:** The SIP connection password. Learn more [here](https://support.telnyx.com/en/articles/4245868-sip-connection-types) in the Credentials Connection Setup section.
   5. *A note about ports:* Port 5060 should be typically used for UDP or TCP transportation. If you're using TLS to encrypt your traffic, use port 5061 and ensure that you have configured your portal properly as outlined in your [pre-requisite activities](#h_74840ee2df).

[Back to Top](#h_dc214f2b78)

## 2 Test your Firewall

In this section, you will perform a firewall configuration and test it. Using a firewall with any external service is a critical step. Because this isn't a Telnyx-side configuration activity, we recommend you consult [Voice Elements' firewall configuration documentation](https://www.voiceelements.com/docs/programmable-voice/configuration/firewall/). But in case you don't need this documentation:

|  |
| --- |
| ***A WARNING ABOUT SIP SNIFFERS:*** *SIP sniffers are bots seek out SIP servers on the internet and try to break in hoping to find weaknesses that would allow them to place free calls over your system.*    *To combat this, we HIGHLY recommend that you only permit [Telnyx IP addresses](https://support.telnyx.com/en/articles/1130687-whitelisting-telnyx-ip-addresses) to have access to this port.* |

That's it! You've successfully connected Voice Elements to your Telnyx account and can now use it

[Back to Top](#h_dc214f2b78)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally check out:

* [Voice Elements documentation](https://www.voiceelements.com/docs/)
* [Contact Voice Elements support](https://www.voiceelements.com/contact/)
* [Try Voice Elements for free](https://www.voiceelements.com/demo/)
* [Getting started with Telnyx](https://sip.telnyx.com/#signaling-addresses)

---

Related Articles

[Configuring Grandstream GXP16XX with Telnyx](https://support.telnyx.com/en/articles/1130660-configuring-grandstream-gxp16xx-with-telnyx)[Fanvil X4G: Telnyx Setup](https://support.telnyx.com/en/articles/5811487-fanvil-x4g-telnyx-setup)[Panasonic KX-HDV: Telnyx setup](https://support.telnyx.com/en/articles/5814406-panasonic-kx-hdv-telnyx-setup)[Gigaset A510: Telnyx Setup](https://support.telnyx.com/en/articles/5815209-gigaset-a510-telnyx-setup)[Konftel 300IPx: Telnyx Setup](https://support.telnyx.com/en/articles/5822579-konftel-300ipx-telnyx-setup)

Did this answer your question?

😞😐😃

Table of contents
