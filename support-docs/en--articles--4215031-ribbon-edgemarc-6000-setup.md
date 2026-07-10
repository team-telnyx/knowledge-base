---
source_url: https://support.telnyx.com/en/articles/4215031-ribbon-edgemarc-6000-setup
scraped: 2026-07-08
content_hash: fa885e15ed84df8d8ea129722211aa2424781218abdc297a3ee4c90c0b8e477d
---

Ribbon: EdgeMarc 6000 Setup | Telnyx Help Center

[Skip to main content](#main-content)

# Ribbon: EdgeMarc 6000 Setup

Learn how to configure the Ribbon:EdgeMarc SBC with Telnyx - Master your config with this guide.

C

Written by Customer Success

February 1, 2024

Table of contents

[Jump to Instructions](#h_d15e0bfea3)

The [Ribbon EdgeMarc 6000](https://ribboncommunications.com/solutions/enterprise-solutions/secure-cloud-communications-solutions/microsoft-solutions-teams-direct-routing) is the newest addition to the Intelligent Edge family. It acts as a flexible demarcation/control point and service insertion device with physical telephony ports and power to run multiple virtual network functions (VNFs). Specifically designed for unified communications offerings, this network device can connect to a variety of digital and analog legacy systems. Its ARM®-based architecture provides dramatic value, performance and scale, while automated “zero touch” provisioning, remote monitoring and management reduce operating expense. The EdgeMarc 6000 has plenty of room to run VNFs to meet customer-specific needs.

|  |
| --- |
| ***Note:*** *This configuration guide is also compatible with the EdgeMarc VOS 15.7.* |

Additional resources:

* [EdgeMarc 6000 documentation](https://rbbn.my.site.com/Support/login)
* [EdgeMarc/Ribbon support](https://ribboncommunications.com/services/ribbon-support-portal)
* [EdgeMarc VoIP settings overview](https://rbbn.my.site.com/Partners/login)

---

# Instructions for Configuring an Edge SBC with Telnyx

In this activity you will:

1. [Configure your SIP settings](#configuring-your-telnyx-mission-control-portal)
2. [Define your SIP trunk registration](#h_5934a8ec3e)
3. [Configure inbound rules](#h_c2989153ce)
4. [Configure outbound rules](#h_2e1d2700e2)

**Pre-requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* [Purchase a DID](https://portal.telnyx.com/#/app/numbers/search-numbers)
* [Set up your Telnyx SIP connection](https://portal.telnyx.com/#/app/connections)
* [Provision your number](https://portal.telnyx.com/#/app/numbers/my-numbers) (Assign it to a SIP connection)
* [Create an outbound voice profile](https://portal.telnyx.com/#/app/outbound)
* Create an [IP authentication connection](https://support.telnyx.com/en/articles/2602782-ip-authentication-with-tech-prefix) on your Telnyx Mission Control Portal
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
* Have the SBC set up with your IP-PBX, with one or more clients configured and running calls between them

**Video Walk-through**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for EdgeMarc/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. **Configure your SIP settings**

In this section, you'll learn how to configure your SIP settings through the Ribbon EdgeMarc portal.

1. [Log into EdgeMarc](https://rbbn.my.site.com/Support/login).
2. From the left-hand navigation, choose **VoIP > SIP**. You'll be taken to the **SIP Settings** page.
3. Find the **SIP protocol settings section** and provide the following information:

   1. **SIP Server Address**: *sip.telnyx.com*
   2. **SIP Server Port:** *5060*
   3. **SIP Server Transport**: *UDP*
   4. **Use Custom Domain:** Check the box
   5. **SIP Server Domain:** *sip.telnyx.com*
   6. **Limit Inbound to listed Proxies:** Check the box
   7. **Limit Outbound to listed Proxies:** Check the box

      ![SIP settings page on the EdgeMarc. ](_images/2671e9f8dd38e047.png)

[Back to Top](#h_d15e0bfea3)

## 2. Define your SIP Trunk Registration

In this section, you'll configure your [SIP trunk](https://telnyx.com/products/sip-trunks) registration mode. You can then configure trunk registrations with the WAN side of the soft switch as-well as the registration mode for the PBX on the LAN side. This will allow for sending SIP messages from the WAN side inbound and for sending SIP messages to the WAN side outbound.

1. From the left-hand navigation, choose **VoIP > SIP > B2BUA**.
2. Find the **Trunking Devices** section.
3. Click the **New Row** button and provide the following information:

   1. **Name:** Identifies the name of your trunking device
   2. **Model:** Select your PBX from the drop-down list.
   3. **IP:** Check the IP radio button. In the field beside it, enter the IP address of your PBX.
   4. **Transport:** Choose a transport. Use *TLS* if you are using TLS encryption. Otherwise, choose *UDP* or *TCP*.
   5. **Port:** *5060* (Unless you are using TLS, in which case, enter *5061*)  
      ​

      ![SIP trunk configuration page. ](_images/6b86478ce7440b41.png)
4. Click **Update** to create the trunking device for PBX.
5. Then click **Submit** at the bottom of the page. This pushes the configuration to the EdgeMarc.

[Back to Top](#h_d15e0bfea3)

## 3. Configure inbound rules

In this section, you'll configure inbound rules and routing, which will allow for sending SIP messages from the EdgeMarc to the PBX.

1. From the left-hand navigation, choose **VoIP > SIP > B2BUA** and click on the **Match** tab.
2. Click **New Row** to create a new entry and provide the following information:

   1. **Direction:** *Inbound*
   2. **Mode:** *BothModes*
   3. **Default:** Select radio button
   4. **Action:** *Inbound*

[Back to Top](#h_d15e0bfea3)

## 4. Configure outbound rules

1. From the left-hand navigation, choose **VoIP > SIP > B2BUA** and click on the **Match** tab.
2. Click **New Row** to create a new entry and provide the following information:

   1. **Direction:** *Outbound*
   2. **Mode:** *BothModes*
   3. **Pattern:** Select radio button and then select *Calling* from the drop-down menu.
   4. **Called/Calling Party:** Depending on your preference, you can allow all callers by entering "." and alternately, ou can pattern-match on partial caller numbers such as *1312270X*
   5. **Source:** *Any*
   6. **Action:** *Outbound*
3. Click **Update**.
4. Click **Submit** to send the configuration to EdgeMarc.

That's it! You've successfully configured your EdgeMarc SBC with Telnyx!  
​

[Back to Top](#h_d15e0bfea3)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [EdgeMarc 6000 documentation](https://rbbn.my.site.com/Support/login)
* [EdgeMarc/Ribbon support](https://ribboncommunications.com/services/ribbon-support-portal)
* [EdgeMarc VoIP settings overview](https://rbbn.my.site.com/Partners/login)

---

---

Related Articles

[Grandstream UMC6202: Auth Setup](https://support.telnyx.com/en/articles/1295514-grandstream-umc6202-auth-setup)[Sansay: SBC VSXi Setup](https://support.telnyx.com/en/articles/4301888-sansay-sbc-vsxi-setup)[Yeastar S-Series: Telnyx SIP](https://support.telnyx.com/en/articles/5748952-yeastar-s-series-telnyx-sip)[Xorcom PBX: SIP Trunk](https://support.telnyx.com/en/articles/5754127-xorcom-pbx-sip-trunk)[How to configure Yeastar P-series](https://support.telnyx.com/en/articles/13375115-how-to-configure-yeastar-p-series)

Did this answer your question?

😞😐😃

Table of contents
