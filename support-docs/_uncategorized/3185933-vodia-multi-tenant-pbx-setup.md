---
source_url: https://support.telnyx.com/en/articles/3185933-vodia-multi-tenant-pbx-setup
scraped: 2026-06-11
---

Vodia: Multi-Tenant PBX Setup | Telnyx Help Center

[Skip to main content](#main-content)

# Vodia: Multi-Tenant PBX Setup

Configure Vodia Multi-Tenant PBX with Credentials - It's easy and fast, get started today.

C

Written by Customer Success

June 6, 2024

Table of contents

[Jump to Instructions](#h_4ff0450d5f)

Vodia PBX is designed with flexibility and convenience in mind. It offers both CPE as well as hosted deployments. This flexibility and convenience can be seen in the platform as well as in the phones and the [SIP trunks](https://telnyx.com/products/sip-trunks). This **IP-PBX** can run on any major platform **Windows, Linux or MAC OS**. Vodia support **all SIP phones** out there with automatic provisioning for the mainstream phones like [Polycom](https://www.poly.com/us/en), [Snom](https://www.snomamericas.com/), [Cisco](https://www.cisco.com/), [Grandstream](https://www.grandstream.com/), Yealink and [more](https://web.vodia.com/supported-phones).

Additional resources:

* [Vodia documentation](https://doc.vodia.com/)
* [Supported phones](https://web.vodia.com/supported-phones)
* [Vodia forums](https://forum.vodia.com/)
* [Vodia support](https://vodia.zammad.com/#login) (Requires login)
* [Vodia portal login](https://portal.vodia.com/)

---

# Instructions for configuring the Vodia Multi-Tenant PBX

In this activity you will:

1. [Create a SIP trunk](#h_3d1db149ad)
2. [Configure inbound routing](#h_a091f19d46)

**Pre-requisites:**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* [Create a credentials-based connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
* [Download](https://web.vodia.com/) and [install](https://doc.vodia.com/docs/software) Vodia

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Vodia PBX/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Create a SIP trunk

In this section, you'll configure a SIP trunk between your Vodia IP phone and your Telnyx account.

1. Log into Vodia PBX, navigate to your Domain, and, from the left-hand navigation choose **TRUNKS > VoIP Providers.**
2. Click on **Add.**
3. From the **Provider** dropdown, select *Telnyx*.

   [![The personal domain on the Vodia PBX. ](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/137498121/257e716de44b3424356eb6ab/choose.png?expires=1781168400&signature=c2775eadd337fd520512ba70852f66262c20909f506274f978a10e562f857b1f&req=dSMgEsB2nINeFb4f3HP0gHXX65lYkXUpy6bsAR%2BJQccZsBEBAbNiCddTgePF%0AyHo%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/137498121/257e716de44b3424356eb6ab/choose.png?expires=1781168400&signature=c2775eadd337fd520512ba70852f66262c20909f506274f978a10e562f857b1f&req=dSMgEsB2nINeFb4f3HP0gHXX65lYkXUpy6bsAR%2BJQccZsBEBAbNiCddTgePF%0AyHo%3D%0A)
4. When asked, enter your Telnyx username and password.

   [![Administration credentials on the Vodia interface. ](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/137498122/d1839c34d81e1680b349e136/userpass.png?expires=1781168400&signature=8d3585608e95cf2b1b56697edd3187afda0424ff7869e80a9199162d58547124&req=dSMgEsB2nINdFb4f3HP0gMqFBqyJhz9HBl7nGiGX5J34C%2B9kFaQQUYp%2F0x%2F%2B%0A8fA%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/137498122/d1839c34d81e1680b349e136/userpass.png?expires=1781168400&signature=8d3585608e95cf2b1b56697edd3187afda0424ff7869e80a9199162d58547124&req=dSMgEsB2nINdFb4f3HP0gMqFBqyJhz9HBl7nGiGX5J34C%2B9kFaQQUYp%2F0x%2F%2B%0A8fA%3D%0A)
5. Click **Create**.

|  |
| --- |
| ***Note:*** *Because Vodia PBX has a built-in Telnyx template, you won't need to enter certain details such as the SIP outbound proxy or trunk headers configuration. Vodia also automatically creates a dial plan for the domain, so there is no need for you to create a dial plan unless you plan to edit it.*  [Current Trunks edit portal.](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/137498124/586f94eb8b37105ae16a52e1/trunk200ok_1.png?expires=1781168400&signature=3968c7b45cd3b0477d1f7cd7007bb46bd71eaa1346a34bb09440b4b876afdab1&req=dSMgEsB2nINbFb4f3HP0gBviIoBVdx%2FJF9st5r6NOxnb127MNTNieTj%2F1YnW%0AjsM%3D%0A) |

[Back to Top](#h_4ff0450d5f)

## 2. Configure inbound routing

In this section, you will route your Telnyx phone number(s) into the Vodia PBX.

1. Navigate to your registered Telynx trunk, and scroll down to **Routing/Redirection.**
2. Vodia supports the following inbound methods:

   1. Send all to the destination request URL
   2. Send all calls to a specific account
   3. Send to a 10 Digit DID
   4. Match extension after a prefix
   5. Use a list of expression  
      ​

   For this exercise, we are going choose "Send all calls to a specific account" When you call into the system all calls will go the specified extension.

   [![Routing/Redirection for inbound. ](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/137498126/750057cc96485a7d6b7b9d53/incoming-20extension.png?expires=1781168400&signature=29caf72ddd741b7cf8aeec8cef8da0746cb67e38b37067eba448645f16a4d7b4&req=dSMgEsB2nINZFb4f3HP0gJJiR9rQQQ%2B6D8%2FY35hDeoXpQEHkHfDJmdxifwNe%0AlZs%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/137498126/750057cc96485a7d6b7b9d53/incoming-20extension.png?expires=1781168400&signature=29caf72ddd741b7cf8aeec8cef8da0746cb67e38b37067eba448645f16a4d7b4&req=dSMgEsB2nINZFb4f3HP0gJJiR9rQQQ%2B6D8%2FY35hDeoXpQEHkHfDJmdxifwNe%0AlZs%3D%0A)
3. If you have multiple Telnyx phone numbers you would like to route into the Vodia PBX, make sure you're in Admin mode in your Vodia PBX and navigate to DID management.

   [![Admin on the Vodia PBX. ](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/137498127/bb4ac79382254242883c72dd/DIDmana.png?expires=1781168400&signature=f520d1ef014b9d89858f18f9e5497df52baf5c829321a7e79aac375eda316044&req=dSMgEsB2nINYFb4f3HP0gAchFYNQ6lNo%2FW1H3qbs2BNExUbtVdBjQpoF%2B6x5%0A%2FSQ%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/137498127/bb4ac79382254242883c72dd/DIDmana.png?expires=1781168400&signature=f520d1ef014b9d89858f18f9e5497df52baf5c829321a7e79aac375eda316044&req=dSMgEsB2nINYFb4f3HP0gAchFYNQ6lNo%2FW1H3qbs2BNExUbtVdBjQpoF%2B6x5%0A%2FSQ%3D%0A)
4. The DID management will help you configure multiple DIDs by assigning them to specific extensions the system.

   [![DID Management portal on the Vodia PBX. ](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/137498128/fddbe424780180482071245f/addDID.png?expires=1781168400&signature=b17c8cafa708775b264e8190ddc6e5ea4d43392deb302918761488cc5d30dadf&req=dSMgEsB2nINXFb4f3HP0gL7pqMCqyNhJNWuohDWzByTsmnpR5UUDpZYWgP%2FV%0A3hk%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/137498128/fddbe424780180482071245f/addDID.png?expires=1781168400&signature=b17c8cafa708775b264e8190ddc6e5ea4d43392deb302918761488cc5d30dadf&req=dSMgEsB2nINXFb4f3HP0gL7pqMCqyNhJNWuohDWzByTsmnpR5UUDpZYWgP%2FV%0A3hk%3D%0A)
5. Navigate to your Telnyx trunk from your Vodia PBX system, scroll down to **Routing/Redirection** and choose *Send all to the destination request URL*.

That's it, you've now completed the configuration of Zoiper 5 and can now make and receive calls by using Telnyx as the SIP provider.  
​

[Back to Top](#h_4ff0450d5f)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [Vodia documentation](https://doc.vodia.com/)
* [Supported phones](https://web.vodia.com/supported-phones)
* [Vodia forums](https://forum.vodia.com/)
* [Vodia support](https://vodia.zammad.com/#login) (Requires login)
* [Vodia portal login](https://portal.vodia.com/)

---

Related Articles

[Configuring an Elastix 4 PBX IP Trunk](https://support.telnyx.com/en/articles/1130622-configuring-an-elastix-4-pbx-ip-trunk)[How to configure a Thirdlane PBX](https://support.telnyx.com/en/articles/1130631-how-to-configure-a-thirdlane-pbx)[Configuring an Elastix 4 PBX Trunk](https://support.telnyx.com/en/articles/1130654-configuring-an-elastix-4-pbx-trunk)[Positron IP PBX](https://support.telnyx.com/en/articles/5790910-positron-ip-pbx)[ScopTEL IP PBX](https://support.telnyx.com/en/articles/5803103-scoptel-ip-pbx)

Did this answer your question?

😞😐😃

Table of contents
