---
source_url: https://support.telnyx.com/en/articles/1130627-configuring-an-avaya-ip-trunk-with-telnyx
scraped: 2026-06-11
---

Configuring an AVAYA IP trunk with Telnyx | Telnyx Help Center

[Skip to main content](#main-content)

# Configuring an AVAYA IP trunk with Telnyx

In this article we will walk you through configuring an AVAYA IP trunk with Telnyx so you can get started right away!

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_94d8640d89)

Learn how to establish connection between your [AVAYA](https://www.avaya.com/en/) server, and your Telnyx Mission Control Portal. We will describe a sample configuration of the IP trunk and the dialplan.

Additional documentation and resources:

* [AVAYA server support](https://support.avaya.com/products/P0956/common-servers)
* AVAYA SIP trunking - overview

---

# Instructions for configuring an Avaya IP trunk

In this activity you will:

1. [Create your SIP line](#h_ef640d5b47%5C)

**Pre-requisites**

* Completed your AVAYA installation and telecommunication-applications deployment.
* [Configure your Telnyx Mission Control Portal](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) which will help you:
* [Provision a DID from Telnyx](https://portal.telnyx.com/#/app/numbers/search-numbers) ([How do I do this](https://support.telnyx.com/en/articles/3562148-requesting-numbers)?)

**Video walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Avaya/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Create your SIP line

1. Under IP Offices/Line add SIP line with the following Configurations:  
   ​  
   ​**SIP Line**

   ```
   Line Number: 100 (whichever number you have available)  
   ITSP Domain Name: sip.telnyx.com  
   URI Type: SIP  
   Location: Cloud  
   Prefix: 1 (whichever prefix you'd like to add)  
   In service: Enable  
   Check OOS: Enable  
   Refresh Method: Auto  
   Timer (seconds): On Demand
   ```

   ​**Transport**

   ```
   ITSP Proxy Address: sip.telnyx.com  
   Layer 4 Protocol: UDP  
   Send Port: 5060  
   Use Network Topology Info: LAN 2 (whichever LAN you have configured for SIP trunking)  
   Explicit DNS Server(s): Add your DNS Server
   ```

   **SIP URI**  
   Add channel with the following configurations:

   ```
   Via: 1.2.3.4 (1.2.3.4 = your public IP)  
   Local URI: *  
   Contact: *  
   Display Name: *  
   PAI: *  
   Registration: 0:    
   Incoming Group: 100 (Number added on SIP Line)  
   Outgoing Group: 100 (Number added on SIP Line)  
   Max Calls per Channel: 10
   ```

   **Dial Plan**  
   Under IP Offices/[Short Code](https://telnyx.com/products/sms-short-code) add a Short Code with the following Configurations:  
   ​

   ```
   Code: 9N; (you can use 9 or whatever number you want to dial to differentiate Telnyx trunk)  
   Feature: Dial  
   Telephone Number: 1N  
   Line Group: 100 (number added on SIP Line)  
   Locale: United States (US English)
   ```

|  |
| --- |
| ***Note:*** *To make outbound calls, Telnyx requires either a valid caller ID from your device or a caller ID override enabled on your SIP connection. Please view our [caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy) for information on enabling a caller ID override from within the Telnyx portal.* |

That's it! You've now configured an AVAYA IP trunk and connected it to Telnyx!

[Back to Top](#h_94d8640d89)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally, check out:

* [AVAYA server support](https://support.avaya.com/products/P0956/common-servers)
* AVAYA SIP trunking - overview

---

---

Related Articles

[Configuring a Cisco CUBE/CUCM IP Trunk](https://support.telnyx.com/en/articles/1130606-configuring-a-cisco-cube-cucm-ip-trunk)[FreePBX Trunk Settings With Telnyx](https://support.telnyx.com/en/articles/1130620-freepbx-trunk-settings-with-telnyx)[Configuring a Vicidial IP trunk with Telnyx](https://support.telnyx.com/en/articles/1130632-configuring-a-vicidial-ip-trunk-with-telnyx)[Configuring a Cisco CUBE/CUCM SIP Trunk](https://support.telnyx.com/en/articles/1130673-configuring-a-cisco-cube-cucm-sip-trunk)[Configuring Telnyx SIP Trunking with Avaya](https://support.telnyx.com/en/articles/1130695-configuring-telnyx-sip-trunking-with-avaya)

Did this answer your question?

😞😐😃

Table of contents
