---
source_url: https://support.telnyx.com/en/articles/2602782-ip-authentication-with-tech-prefix
scraped: 2026-06-11
---

IP Authentication with Tech Prefix | Telnyx Help Center

[Skip to main content](#main-content)

# IP Authentication with Tech Prefix

In this article we will explain IP authentication with tech prefixes and when to use them.

Written by Dillin

May 25, 2024

Table of contents

The tech prefix setting can be found under the settings tab of your [SIP Connections](https://portal.telnyx.com/#/app/connections) Authentication & Routing Configuration section.

[![Authentication &amp; Routing Configuration section](https://downloads.intercomcdn.com/i/o/980156439/ffdcecc21f52efc92d8d7f13/Screenshot+from+2024-03-03+10-08-21.png?expires=1781167500&signature=c4bc021269cd7655b8aad6e6d5e9fbee326c3d1760c286e0c1cc1c2a03cac314&req=fSgnF8x4mYJWFb4f3HP0gPO%2FaCwwqRCm3mDrpFbm5OZCgFrDiao4QSFgqqq2%0AB0yEWLeUbHnIj76OUA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/980156439/ffdcecc21f52efc92d8d7f13/Screenshot+from+2024-03-03+10-08-21.png?expires=1781167500&signature=c4bc021269cd7655b8aad6e6d5e9fbee326c3d1760c286e0c1cc1c2a03cac314&req=fSgnF8x4mYJWFb4f3HP0gPO%2FaCwwqRCm3mDrpFbm5OZCgFrDiao4QSFgqqq2%0AB0yEWLeUbHnIj76OUA%3D%3D%0A)

# Why are tech prefixes beneficial?

In environments where a single IP address is used for multiple outbound voice profiles, it is vital to distinguish each client's traffic uniquely. Telnyx supports this requirement by allowing multiple IP connections to share the same IP.

To differentiate each client, simply apply a unique 4-digit tech prefix to each connection. It's important to remember that for your outbound calls sent to Telnyx, this tech prefix must be included; otherwise, the call will not be recognized, leading to a SIP 407 Proxy Authentication response and call rejection.

## **What exactly is a tech prefix?**

A tech prefix is a simple yet powerful 4-digit number prefixed to the number you are dialing. For example, if you have a tech prefix of "1234" and wish to dial "18005678912", you would dial "123418005678912". This prefix does not need to be manually entered each time; your phone system's outbound settings can be configured to automatically prepend the tech prefix to all calls.

## Do you support tech prefixes at the number level settings?

Yes, Telnyx supports the application of tech prefixes at the [number level](https://support.telnyx.com/en/articles/4349113-my-numbers-page#h_d4c4ba170f). For guidance on setting this up, please refer to the comprehensive article on enabling tech prefix settings for your numbers. This functionality allows for a more granular control of call routing and identification, ensuring that each client's traffic is properly managed and authenticated.

## "Termination Endpoint" Error and Its Implications:

It is important to note that while connections can share the same IP address, they must be uniquely identified to avoid the "[Termination Endpoint](https://support.telnyx.com/en/articles/4320411-more-about-outbound-voice-profiles#h_8af1e9166d)" error. This error occurs when another connection with the same IP address is already assigned to an outbound voice profile. To prevent this, ensure each connection has a unique combination, achieved through a tech prefix, token or p charge info.

​  
​

---

Related Articles

[Configuring an Elastix 4 PBX IP Trunk](https://support.telnyx.com/en/articles/1130622-configuring-an-elastix-4-pbx-ip-trunk)[Configuring an AVAYA IP trunk with Telnyx](https://support.telnyx.com/en/articles/1130627-configuring-an-avaya-ip-trunk-with-telnyx)[Ip Authentication with X-Telnyx-Token](https://support.telnyx.com/en/articles/4860170-ip-authentication-with-x-telnyx-token)[FreePBX V15 IP Trunk - ChanSIP Tutorial](https://support.telnyx.com/en/articles/5467232-freepbx-v15-ip-trunk-chansip-tutorial)[FreePBX V15: IP Trunk - PJSIP](https://support.telnyx.com/en/articles/5619595-freepbx-v15-ip-trunk-pjsip)

Did this answer your question?

😞😐😃

Table of contents
