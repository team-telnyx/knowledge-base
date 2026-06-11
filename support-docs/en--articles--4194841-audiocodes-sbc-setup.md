---
source_url: https://support.telnyx.com/en/articles/4194841-audiocodes-sbc-setup
scraped: 2026-06-11
---

Audiocodes SBC: Setup | Telnyx Help Center

[Skip to main content](#main-content)

# Audiocodes SBC: Setup

Learn AudioCodes SBC configuration with Telnyx - Click to dive in today.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_6abc1dab54)

[Audiocodes Session Border Control (SBC) devices](https://www.audiocodes.com/solutions-products/products/session-border-controllers-sbcs) deliver seamless connectivity, enhanced security and quality assurance for your VoIP network. This family of SBCs can support both an enterprise environment or a service provider core.

* In the enterprise environment, SBCs form an effective demarcation point between the business’s VoIP network and the service provider’s [SIP trunk](https://telnyx.com/products/sip-trunks), performing SIP protocol mediation and media handling (interoperability), and securing the enterprise VoIP network.
* In the service provider core, AudioCodes SBCs can function as peering SBCs between operator networks or as access SBCs delivering security and protocol normalization.

This SBC lineup includes a range of platforms that offer cost-friendly session border control and hybrid functionality (SIP to TDM, SIP to SIP).

Additional resources:

* [Audiocodes SBC documentation](https://www.audiocodes.com/library/technical-documents?productFamilyGroup=1637)
* [Audiocodes SBC interoperability list](https://www.audiocodes.com/partners/interoperability-list)
* [Audiocodes support](https://www.audiocodes.com/services-support)

---

# Instructions for Configuring Audiocodes SBC with Telnyx

In this activity you will:

1. [Configure your Audiocodes SBC using INI](#h_fa7e9503c6)

**Pre-requisites:**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
* Have your SBC already set up with your IP-PBX, with one or more clients configured and running calls between them

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Audiocodes SBC/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Configure your AudioCodes SBC using INI

**Define your IP Group:**

```
[ IPGroup ]  
IPGroup_Description:  Telnyx   
IPGroup_SIPGroupName: sip.telnyx.com   
[ \IPGroup ]
```

**Define your SIP Proxy:**

```
[ ProxyIp ]   
FORMAT ProxyIp_Index = ProxyIp_IpAddress, ProxyIp_TransportType, ProxyIp_ProxySetId;   
ProxyIp 1 = "192.76.120.10/32:5060", 0, 1;  
ProxyIp 2 = "64.16.250.10/32:5060", 0, 1;    
[ \ProxyIp ]
```

**Define Coders:**

```
[ CodersGroup0 ]  
CodersGroup0_Name:        g711ulaw64k   
CodersGroup0_pTime:       20   
CodersGroup0_PayloadType: 0  
[ \CodersGroup0 ]
```

|  |
| --- |
| ***Note:*** *Depending on your requirements, you may need to set more configurations such as IP profiles and Routing.* |

That's it! You have successfully configured your Audiocodes SBC with Telnyx.

[Back to Top](#h_6abc1dab54)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [Audiocodes SBC documentation](https://www.audiocodes.com/library/technical-documents?productFamilyGroup=1637)
* [Audiocodes SBC interoperability list](https://www.audiocodes.com/partners/interoperability-list)
* [Audiocodes support](https://www.audiocodes.com/services-support)

---

Related Articles

[Oracle: Acme Packet SBC Setup](https://support.telnyx.com/en/articles/4194697-oracle-acme-packet-sbc-setup)[Ribbon: EdgeMarc 6000 Setup](https://support.telnyx.com/en/articles/4215031-ribbon-edgemarc-6000-setup)[Sansay: SBC VSXi Setup](https://support.telnyx.com/en/articles/4301888-sansay-sbc-vsxi-setup)[Gigaset A510: Telnyx Setup](https://support.telnyx.com/en/articles/5815209-gigaset-a510-telnyx-setup)[Audiocodes 400HD](https://support.telnyx.com/en/articles/5819923-audiocodes-400hd)

Did this answer your question?

😞😐😃

Table of contents
