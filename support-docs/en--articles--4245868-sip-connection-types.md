---
source_url: https://support.telnyx.com/en/articles/4245868-sip-connection-types
scraped: 2026-06-11
---

SIP Connection: Types | Telnyx Help Center

[Skip to main content](#main-content)

# SIP Connection: Types

This article explains the different types of SIP Connections available in the Mission Control Portal.

Written by Dillin

Updated over 3 weeks ago

Table of contents

# What are the Sip Connection Types?

We offer four different authentication types to register your switch to ours. This article will show you how to configure these types within the Mission Control Portal and explain the various settings that SIP Connections have. (Details on setting up MS Teams SBC can be found here: [https://support.telnyx.com/en/articles/5253876-ms-teams-telnyx-pstn](https://support.telnyx.com/en/articles/5253876-configuring-telnyx-with-microsoft-teams-direct-routing))

***Call Control:*** If you are looking to setup a programmable voice connection/application, this can be done in the programmable voice section of the Portal. Click the button below to go there.

[Portal - Programmable Voice](https://portal.telnyx.com/#/voice/connections)

[Call Control Documentation](https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-fundamentals)

## SIP Connection Registration Types Explained

Deciding on what registration type to use depends on your use case. As a rule of thumb, a **credential-based** **connection** is used if you have a **dynamic public IP address**. If you have a **static IP address**, then you can use an **IP-based connection** instead.

Below are guides on how to setup the following connection types:

* Credential-based Authentication
* IP-based Authentication
* FDQN-based Authentication

## Credentials Connection Setup

### 1. Click Create SIP Connection at the SIP Connection Tab in the Portal.

### 2. Enter the name you wish to have for your connection.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333431242/13b199b53c0ac00557a4569ef8d5/image.png?expires=1781167500&signature=d7d1f7a7ffc11663ad491d817756986b3e3ce34918303f3fab718a42697d8682&req=diMkFc19nINbW%2FMW1HO4zX12AHjsumC%2FgnQvLkv%2FFyGa1%2Bi5EYKrVXf1ig8F%0AhKrSoK5ejqn8ZuMDQ3U%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333431242/13b199b53c0ac00557a4569ef8d5/image.png?expires=1781167500&signature=d7d1f7a7ffc11663ad491d817756986b3e3ce34918303f3fab718a42697d8682&req=diMkFc19nINbW%2FMW1HO4zX12AHjsumC%2FgnQvLkv%2FFyGa1%2Bi5EYKrVXf1ig8F%0AhKrSoK5ejqn8ZuMDQ3U%3D%0A)

### 3. Select Credentials as the Connection Type

A username and password will automatically be generated but you can change the credentials via the Authentication & Routing Configuration section within the SIP connection's settings. It is **highly recommended** that you choose a **strong password**.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333434026/f83f0c1320c800057f1029ca4e38/image.png?expires=1781167500&signature=4217d4cde0617e47be84b80cd4c3f8ffa67ada1be36ac0ffbfd305087a5d99ac&req=diMkFc19mYFdX%2FMW1HO4zVc%2FquzgbrmrWN%2B3tzRvNhLHCGP%2BxJJiVkkw4qHo%0AeyP0cQmQDuUdKXrfEx8%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333434026/f83f0c1320c800057f1029ca4e38/image.png?expires=1781167500&signature=4217d4cde0617e47be84b80cd4c3f8ffa67ada1be36ac0ffbfd305087a5d99ac&req=diMkFc19mYFdX%2FMW1HO4zVc%2FquzgbrmrWN%2B3tzRvNhLHCGP%2BxJJiVkkw4qHo%0AeyP0cQmQDuUdKXrfEx8%3D%0A)

### 4. Click next or your user details will not be saved

**Note:** *Once your **Credential Connection** is created, you can display the username and password by going into your SIP Connection > Authentication and routing*

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333443178/3376304ca4f5c14351049312d24d/image.png?expires=1781167500&signature=11cef80133acb9df350d5e46e65df9045ad2d523a5af7f273e7c21c37e20f8d8&req=diMkFc16noBYUfMW1HO4zYVO%2Fnymrx5glUU2A3Gl58Yq6sNkfQVADBuX0aGL%0ApM0ssHzFb5sEhjOIdxc%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333443178/3376304ca4f5c14351049312d24d/image.png?expires=1781167500&signature=11cef80133acb9df350d5e46e65df9045ad2d523a5af7f273e7c21c37e20f8d8&req=diMkFc16noBYUfMW1HO4zYVO%2Fnymrx5glUU2A3Gl58Yq6sNkfQVADBuX0aGL%0ApM0ssHzFb5sEhjOIdxc%3D%0A)

## IP Address Connection Setup

### 1. Click Create SIP Connection at the SIP Connection Tab in the Portal.

### **2. Enter the name you wish to have for your connection.**

### 3. Select IP Address as the Connection Type

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333447545/d1ffc8a7821277b38f70975b1184/image.png?expires=1781167500&signature=d281145e71724000511881448cdfca1d9a92c67d3425e9379497020f465512a2&req=diMkFc16moRbXPMW1HO4zbrxN1g4NGyZ2WHTZ7ixI4PoATGddg5fzATnJOZ6%0A3vRsJBGYPAl5lyWwH8Q%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333447545/d1ffc8a7821277b38f70975b1184/image.png?expires=1781167500&signature=d281145e71724000511881448cdfca1d9a92c67d3425e9379497020f465512a2&req=diMkFc16moRbXPMW1HO4zbrxN1g4NGyZ2WHTZ7ixI4PoATGddg5fzATnJOZ6%0A3vRsJBGYPAl5lyWwH8Q%3D%0A)

Enter an IP address and port via the IP addresses section within the SIP connections settings and click **Add** IP address**.**

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333450404/7506e1cea6b4bc8f95fb05ede465/image.png?expires=1781167500&signature=ff08f52f2b7f51ebbbaa0d8e7e1ea5e31a170385e2446c2068e666f905c19a8b&req=diMkFc17nYVfXfMW1HO4zfojdPEaM2ZDtl5kKUixf3TtZTTdhRCoa3l0dSbi%0AFjJ%2Bvmk2Ohke3IhAmrM%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333450404/7506e1cea6b4bc8f95fb05ede465/image.png?expires=1781167500&signature=ff08f52f2b7f51ebbbaa0d8e7e1ea5e31a170385e2446c2068e666f905c19a8b&req=diMkFc17nYVfXfMW1HO4zfojdPEaM2ZDtl5kKUixf3TtZTTdhRCoa3l0dSbi%0AFjJ%2Bvmk2Ohke3IhAmrM%3D%0A)

You can add multiple IP addresses and select the order of preference. There are two routing methods to choose from; **Sequential** and **Round Robin**.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333452515/c5ea1491bd1a5f3efab11eda9b5a/image.png?expires=1781167500&signature=5bbb504027bccbf0b2fa370c4a786692b85e197bf4fb1b476fc7ee7704fa4260&req=diMkFc17n4ReXPMW1HO4zdo%2BnnaA9kC8kRq6RuFds%2F%2BmPlrwEBt1sdUIJumY%0AfWlFHoSESLEPxIgDOEc%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333452515/c5ea1491bd1a5f3efab11eda9b5a/image.png?expires=1781167500&signature=5bbb504027bccbf0b2fa370c4a786692b85e197bf4fb1b476fc7ee7704fa4260&req=diMkFc17n4ReXPMW1HO4zdo%2BnnaA9kC8kRq6RuFds%2F%2BmPlrwEBt1sdUIJumY%0AfWlFHoSESLEPxIgDOEc%3D%0A)

**Note:** If you do not have a static IP address, it will change and you will be unable to receive or make calls.

## FQDN Connection Setup

### 1. Click Create SIP Connection at the SIP Connection Tab in the Portal.

### **2. Enter the name you wish to have for your connection.**

### **3. Select FQDN as the Connection Type**

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333457236/af5aa860d0f416cb04a39cba9faa/image.png?expires=1781167500&signature=c8eb094876837249385e6bff077323941f89cda597a78ab7514976e2b544ec3d&req=diMkFc17moNcX%2FMW1HO4zakqqe8qvxCY%2BcswH7CcGYKUbZN0JQzLWDnKTsbB%0AIb%2F0dMRN%2F5t3SHRiz%2Bo%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333457236/af5aa860d0f416cb04a39cba9faa/image.png?expires=1781167500&signature=c8eb094876837249385e6bff077323941f89cda597a78ab7514976e2b544ec3d&req=diMkFc17moNcX%2FMW1HO4zakqqe8qvxCY%2BcswH7CcGYKUbZN0JQzLWDnKTsbB%0AIb%2F0dMRN%2F5t3SHRiz%2Bo%3D%0A)

This connection type is slightly different as it has an inbound setting and an outbound setting.

In the **Next step**, clic on add FQDN, choose your **FQDN** type (for most users this will be **A**) and enter your **Fully Qualified Domain Name** in the input box. Click **Save** to add the address.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333459844/ee8ea5cc97cf7f6d45d6be4b1758/image.png?expires=1781167500&signature=caf0228ec9a2a075907fe0f2ecc90114d7f1941c1427011178958b010259af3b&req=diMkFc17lIlbXfMW1HO4zevJfx6cxwM0yI9qNJw1j8Iupd4jD%2FVDQc8xDk3w%0AQVwBzPPdjxSpa6iqMLc%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333459844/ee8ea5cc97cf7f6d45d6be4b1758/image.png?expires=1781167500&signature=caf0228ec9a2a075907fe0f2ecc90114d7f1941c1427011178958b010259af3b&req=diMkFc17lIlbXfMW1HO4zevJfx6cxwM0yI9qNJw1j8Iupd4jD%2FVDQc8xDk3w%0AQVwBzPPdjxSpa6iqMLc%3D%0A)

In the **outbound calls authentication**, choose either **Credentials** or **IP Address**, and configure using the guides above.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333470470/347fb14c45389b013baf458ffcc0/image.png?expires=1781167500&signature=b53b3e941fab9507bee662db9bb6beaef244a062c2d8b535646c80e61595347a&req=diMkFc15nYVYWfMW1HO4za46SW2K1H85d8Oh6dD5orsT0gyDW4rbLWspWmM0%0AvHaIKftV21kwWdWRtJQ%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333470470/347fb14c45389b013baf458ffcc0/image.png?expires=1781167500&signature=b53b3e941fab9507bee662db9bb6beaef244a062c2d8b535646c80e61595347a&req=diMkFc15nYVYWfMW1HO4za46SW2K1H85d8Oh6dD5orsT0gyDW4rbLWspWmM0%0AvHaIKftV21kwWdWRtJQ%3D%0A)

**Note:** *You can assign multiple FQDN addresses on the Inbound section and multiple IP addresses on the Outbound section to a single FQDN registered connection. You can change the routing priority and routing method in the connection settings.*

## Where can I find the connection id?

Once a connection is created, you can find the unique connection id just below the settings sub tab of the SIP Connection as seen below:

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333476762/89e5925a2634356b47fb0c2a8073/image.png?expires=1781167500&signature=e63c46d6c71a82c5618d2a3dd25696e8cf99458f12460732d498d7ca9599b37d&req=diMkFc15m4ZZW%2FMW1HO4zZjoNfvhpxmio3bVjjXYDvVgU4lsnxd73%2FBduvte%0AgNkafm%2BR6UQdxLcdV0Y%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333476762/89e5925a2634356b47fb0c2a8073/image.png?expires=1781167500&signature=e63c46d6c71a82c5618d2a3dd25696e8cf99458f12460732d498d7ca9599b37d&req=diMkFc15m4ZZW%2FMW1HO4zZjoNfvhpxmio3bVjjXYDvVgU4lsnxd73%2FBduvte%0AgNkafm%2BR6UQdxLcdV0Y%3D%0A)

Take a look at our [SIP Connections API](https://developers.telnyx.com/docs/voice/sip-trunking/configuration-guides/index#sip-trunking-configuration-guides) if you want to programmatically update the SIP Connection settings.

## How do I deactivate or disable my SIP Connection?

To deactivate or disable your SIP Connection visit the SIP Connections page, select edit on your desired SIP Connection, and click the toggle under the "status" option. This will deactivate the SIP Connection which will mean inbound calls and outbound calls will not be processed. See this image below for reference.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333484437/25d1414a2f6d785cfed18e965da4/image.png?expires=1781167500&signature=4743e5afef2ee7891fc15eb0e5005835c00e705dec31927958f680c92ac98a3b&req=diMkFc12mYVcXvMW1HO4zST7E7Bqjzy4efnu%2BTyw5JVzfs8TtxaTn5Eaw%2F%2Bp%0A85fAH9Ra%2BvSpHl5nDrs%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333484437/25d1414a2f6d785cfed18e965da4/image.png?expires=1781167500&signature=4743e5afef2ee7891fc15eb0e5005835c00e705dec31927958f680c92ac98a3b&req=diMkFc12mYVcXvMW1HO4zST7E7Bqjzy4efnu%2BTyw5JVzfs8TtxaTn5Eaw%2F%2Bp%0A85fAH9Ra%2BvSpHl5nDrs%3D%0A)

---

Related Articles

[SIP Connection Failover Guide (IP/FQDN-Based)](https://support.telnyx.com/en/articles/1176364-sip-connection-failover-guide-ip-fqdn-based)[SIP Connection: Settings](https://support.telnyx.com/en/articles/4351104-sip-connection-settings)[SIP Registration](https://support.telnyx.com/en/articles/4363904-sip-registration)[Guide to SIP AnchorSite® Settings](https://support.telnyx.com/en/articles/5271423-guide-to-sip-anchorsite-settings)[Yeastar S-Series: Telnyx SIP](https://support.telnyx.com/en/articles/5748952-yeastar-s-series-telnyx-sip)

Did this answer your question?

😞😐😃

Table of contents
