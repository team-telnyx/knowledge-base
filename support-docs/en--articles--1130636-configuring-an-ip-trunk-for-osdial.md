---
source_url: https://support.telnyx.com/en/articles/1130636-configuring-an-ip-trunk-for-osdial
scraped: 2026-06-11
---

Configuring an IP Trunk for OSDial | Telnyx Help Center

[Skip to main content](#main-content)

# Configuring an IP Trunk for OSDial

Learn how to set up a connection between you OS dial server and the Telnyx Mission Control Portal.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_b5c49b03de)

[OSDial](https://osdial.com/) is a popular full-featured predictive dialer, that uses Open Source licenses to greatly reduce the cost without sacrificing quality or functionality. Able to dial in every imaginable way, this is the most flexible and cost-effective dialer available today.

Additional documentation:

* [OSDial support](https://osdial.com/support/)
* [OSDial community](https://osdial.com/sitemap/)
* [Build an OSDial server - easy instructions!](https://osdial.com/sitemap/)
* [OSDial training sessions](https://osdial.com/support/)

---

# Instructions for configuring an IP trunk between OSDial and Telnyx

In this activity you will:

1. [Create a SIP trunk](#h_70ce827498)

**Pre-requisites:**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for OSDial/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Create a SIP trunk

In this section, we will create a [SIP trunk](https://telnyx.com/products/sip-trunks) between OSDial and your Telnyx account.

1. Log into the OS dial web portal and going to **Admin > Carriers > Add new carrier** and provide the following information:

   1. **Carrier ID:** *Telnyx*
   2. **Carrier Name:***Telnyx*
   3. **Registration String:** leave blank
   4. **Template ID:** None
   5. **Account Entry:** *Telnyx*
   6. **Disallow:** *all*
   7. **Allow:** *ulaw*
   8. **Allow:** *G 729*
   9. **Type:** *Peer*
   10. **Insecure:** *port,invite*
   11. **Host:** *sip.telnyx.com*
   12. **DTMFMode:** *RFC 2833*
   13. **Context:** *default*
   14. **Protocol:** *SIP*
   15. **Global String:** *Telnyx=SIP/telnyx*
   16. **Dial Plan:** *exten => \_9NXXXXXXXXXX,1,AGI(agi://127.0.0.1:4577/call\_log)  
       exten => \_9NXXXXXXXXXX,2,Dial(${Telnyx}/${EXTEN:1},60,tTor)  
       exten => \_9NXXXXXXXXXX,3,Hangup*  
       ​  
       In this case, 9 is the prefix that will be dialed to send calls to Telnyx's trunk.

That's it! You're now ready to start making calls with OSDial using Telnyx as your service provider.  
​

[Back to Top](#h_977c764a75)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [OSDial support](https://osdial.com/support/)
* [OSDial community](https://osdial.com/sitemap/)
* [Build an OSDial server - easy instructions!](https://osdial.com/sitemap/)
* [OSDial training sessions](https://osdial.com/support/)

---

Related Articles

[Asterisk: Configure an Asterisk IP trunk](https://support.telnyx.com/en/articles/1130628-asterisk-configure-an-asterisk-ip-trunk)[Configuring a Vicidial IP trunk with Telnyx](https://support.telnyx.com/en/articles/1130632-configuring-a-vicidial-ip-trunk-with-telnyx)[Configuring a GOautodial PBX IP Trunk](https://support.telnyx.com/en/articles/1130649-configuring-a-goautodial-pbx-ip-trunk)[Configuring an Asterisk Credentials Trunk](https://support.telnyx.com/en/articles/1130676-configuring-an-asterisk-credentials-trunk)[Configuring a GoAutoDial PBX SIP Trunk](https://support.telnyx.com/en/articles/1130694-configuring-a-goautodial-pbx-sip-trunk)

Did this answer your question?

😞😐😃

Table of contents
