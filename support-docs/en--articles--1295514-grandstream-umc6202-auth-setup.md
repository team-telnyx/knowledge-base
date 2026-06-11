---
source_url: https://support.telnyx.com/en/articles/1295514-grandstream-umc6202-auth-setup
scraped: 2026-06-11
---

Grandstream UMC6202: Auth Setup | Telnyx Help Center

[Skip to main content](#main-content)

# Grandstream UMC6202: Auth Setup

This article will provide you steps for configuring your Grandstream UMC6202 with Telnyx phone service using Registration (user/pass).

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_ffb5e1a080)

[Grandstream](https://www.grandstream.com/) has been connecting the world since 2002 with SIP Unified Communications solutions that serve the small and medium business and enterprises markets and have been recognized throughout the world for their quality, reliability and innovation. Their open standard SIP-based products offer broad interoperability throughout the industry.

This article guides you on how to configure the [Granstream UMC 6202](https://www.grandstream.com/products/ip-pbxs/ucm-series-ip-pbxs/product/ucm6200-series) to make and receive calls over the internet through a next generation carrier like Telnyx!

Additional documentation and resources:

* [Product datasheet](https://www.grandstream.com/hubfs/Product_Documentation/datasheet_ucm6200_series_english.pdf?hsLang=en) (English)
* [Grandstream FAQ](https://blog.grandstream.com/faq)
* [Grandstream user forum](https://forums.grandstream.com/)
* [Grandstream Learning Center](https://www.grandstream.com/learning-center)
* [Grandstream firmware updates](https://www.grandstream.com/support/firmware)
* How-to guides for [UCM6200 series](https://www.grandstream.com/support/resources?title=UCM6200%20series) and [UCM6510 series](https://www.grandstream.com/support/resources?title=UCM6510)
* [Administrator's user manual](https://www.grandstream.com/hubfs/Product_Documentation/ucm62xx_usermanual.pdf)

---

# Configuring the Grandstream UMC 6202

In this activity you will:

1. [Log into your Grandstream web UI](#h_fd82e20d9b)
2. [Configure a SIP trunk](#h_37db4596e8)
3. [Create an inbound route](#h_b50bbadbbd)
4. [Create an outbound route](#h_822361b2c2)
5. [Configure an outbound caller ID](#h_9b1c8d58ae)

**Pre-requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* [Purchase a DID](https://portal.telnyx.com/#/app/numbers/search-numbers)
* [Set up your Telnyx SIP connection](https://portal.telnyx.com/#/app/connections)
* [Provision your number](https://portal.telnyx.com/#/app/numbers/my-numbers) (Assign it to a SIP connection)
* [Create an outbound voice profile](https://portal.telnyx.com/#/app/outbound)
* Create a [credentials connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal
* Ensure your Grandstream device is running [the latest firmware](https://www.grandstream.com/support/firmware)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Grandstream GXP/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Log into your Grandstream web UI

All the configuration you'll need to do will take place on the web UI, which acts as an interface between you and your Grandstream device. You can access the web UI via the device's IP address. We'll find that, then use it to log in.

1. The IP address used to access the web UI depends on where the user’s computer is connected.

   1. If the computer is connected to *the same switch/router that the UCM6200 series WAN port is connected*, then browse to the IP address that is displayed on the UCM6200 series LCD. This address is the *WAN IP*.
   2. If the computer is connected *to the LAN side of the UCM6200 series*, then users would browse to the default IP of the UCM6200 series which is *192.168.2.1*.
2. If connected successfully, the UCM6200 series login page. Out of the box, your device will have the following default credentials:

   1. **Username**: *admin*
   2. **Password**: *admin*  
      ​*HOWEVER: Units manufactured starting January 2017 have a unique random password printed on the sticker located on the back of the unit. It is highly recommended to change the default password after logging in for the first time. Older units have default password* admin*.*

[Back to Top](#h_ffb5e1a080)

## 2. Configure SIP trunk

1. In the left-hand navigation, expand **Extension/Trunk** and click **VoIP Trunks** in the sub-menu.

   [![SIP trunk configuration portal. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150747857/b01f1f35bccc0bbc692d5c95/d-_sZrHctvps7Iq4Nc33X5Rv7jg0V7Mngqv6PmQ-tKE5L0aTevRXuLQ9FK229Vk1mQA_3cTwEUmje558hPhzkk1d1KMPBosJU3e-C7D8RXyyo5lc_ph1sgmaHrw4ow6dZcH0P5zg?expires=1781167500&signature=86a7b2bd1dcd85a915354a0117c8549e06012caec91bc42c49c813cff6bd0365&req=dSUnEc15lYRYFb4f3HP0gMZshNciLjmL9%2BrrwOLD9GXUvfDH2sMlbCbCNQ%2FM%0Aqzw%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150747857/b01f1f35bccc0bbc692d5c95/d-_sZrHctvps7Iq4Nc33X5Rv7jg0V7Mngqv6PmQ-tKE5L0aTevRXuLQ9FK229Vk1mQA_3cTwEUmje558hPhzkk1d1KMPBosJU3e-C7D8RXyyo5lc_ph1sgmaHrw4ow6dZcH0P5zg?expires=1781167500&signature=86a7b2bd1dcd85a915354a0117c8549e06012caec91bc42c49c813cff6bd0365&req=dSUnEc15lYRYFb4f3HP0gMZshNciLjmL9%2BrrwOLD9GXUvfDH2sMlbCbCNQ%2FM%0Aqzw%3D%0A)
2. Click **Add SIP trunk** and fill in the required information:

   ### Required Fields:

   1. **Type:** *Register [SIP Trunk](https://telnyx.com/products/sip-trunks)*
   2. **Provider Name:** *Telnyx*
   3. **Select host Name:** *sip.telnyx.com*
   4. **Username:** Your Telnyx SIP username
   5. **Password:** Your Telnyx SIP password

      [![SIP trunk credential information input. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150747859/617ffbfe21f03549040509d7/e50UboHYHkCnS1ivTFFQaQtEYaFVabd7BrNVLy2K6xhpyDu6JtR60wO2eqUI_biLmsRhqQCpoYOn5vKmKl7ZSuKhwvjwzKADWAj3qttHaKmo1I-aonCqq-VoIaEyorpwlZk2zTx9?expires=1781167500&signature=2853be4eb1eddfab39baa75552ffd425ddda40d0e137548347a52db05d6ff2e6&req=dSUnEc15lYRWFb4f3HP0gFkvB6rQtx%2FupP1Fz1OyZE9dKjZsDX%2Bp68e8WWSF%0AiDs%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150747859/617ffbfe21f03549040509d7/e50UboHYHkCnS1ivTFFQaQtEYaFVabd7BrNVLy2K6xhpyDu6JtR60wO2eqUI_biLmsRhqQCpoYOn5vKmKl7ZSuKhwvjwzKADWAj3qttHaKmo1I-aonCqq-VoIaEyorpwlZk2zTx9?expires=1781167500&signature=2853be4eb1eddfab39baa75552ffd425ddda40d0e137548347a52db05d6ff2e6&req=dSUnEc15lYRWFb4f3HP0gFkvB6rQtx%2FupP1Fz1OyZE9dKjZsDX%2Bp68e8WWSF%0AiDs%3D%0A)

      [![SIP trunk credential information input interface. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150747861/7eee6f4b5b6ad26e9be48ea9/TqOKhNjWmHfKblqRQcJovn-gLcaKqfU5aeR-VAyXYvK2SmMnZRZ0lKaWHrLkDazJxPFw0PS7xp7FHTxcg9fwSO3Qr5HgYeyJsyAAfL4h6PpCneSak4coacJS1tBtSQlQ2OQZuRGZ?expires=1781167500&signature=1dc16ff2c665d7013026ab7306dbd9abd043678980f65cfbb5f7c56dfd8d9021&req=dSUnEc15lYdeFb4f3HP0gIpunlfwuoYiArsLL0ED1T4Raei39a%2FnQc2NMzMA%0AsXk%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150747861/7eee6f4b5b6ad26e9be48ea9/TqOKhNjWmHfKblqRQcJovn-gLcaKqfU5aeR-VAyXYvK2SmMnZRZ0lKaWHrLkDazJxPFw0PS7xp7FHTxcg9fwSO3Qr5HgYeyJsyAAfL4h6PpCneSak4coacJS1tBtSQlQ2OQZuRGZ?expires=1781167500&signature=1dc16ff2c665d7013026ab7306dbd9abd043678980f65cfbb5f7c56dfd8d9021&req=dSUnEc15lYdeFb4f3HP0gIpunlfwuoYiArsLL0ED1T4Raei39a%2FnQc2NMzMA%0AsXk%3D%0A)
3. Click **Save**.

|  |
| --- |
| ***Note:*** *If you have issues setting this up with a hostname you can always use our primary ip address 192.76.120.10.* |

[Back to Top](#h_ffb5e1a080)

## 3. Create an inbound route

When a call comes in from the outside, it'll need to be directed from sip.telnyx.com to the phone extension you ultimately want it to go, such as a user extension or an IVR extension.   
​

In this section, we'll configure our own inbound routes.  
​

### Steps:

1. #### In the left-hand navigation, expand "**Extension/Trunk"** and click "**Inbound Routes"** in the sub-menu.

   [![Inbound routes icon in Extension/Trunk tab. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150747862/9f06b66340ed40ba9a8d75ca/H8ZOr0ttDRZVO2fNg6qxDBop8LMMG3RMzKDVCBCcljUSlKn9v5mFEvleuBvYkIGt4Vtq-nl7jGQgy6ZpwKP9Pc6C-JxyiUfuUb-xJ7mnpktrpVSgLuTzdahZWkgtp47VgO1vGW5R?expires=1781167500&signature=1cc58d6f5f31c3ec9e2f83ab4988f61774e95ecc3478b25f8772c6fba733e820&req=dSUnEc15lYddFb4f3HP0gJz4Q3E4rC3v9xA5DFtWNRE9APZiqiJiUcWva8Fn%0A9ao%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150747862/9f06b66340ed40ba9a8d75ca/H8ZOr0ttDRZVO2fNg6qxDBop8LMMG3RMzKDVCBCcljUSlKn9v5mFEvleuBvYkIGt4Vtq-nl7jGQgy6ZpwKP9Pc6C-JxyiUfuUb-xJ7mnpktrpVSgLuTzdahZWkgtp47VgO1vGW5R?expires=1781167500&signature=1cc58d6f5f31c3ec9e2f83ab4988f61774e95ecc3478b25f8772c6fba733e820&req=dSUnEc15lYddFb4f3HP0gJz4Q3E4rC3v9xA5DFtWNRE9APZiqiJiUcWva8Fn%0A9ao%3D%0A)
2. #### Select the trunk and then click add on the left hand side of the screen underneath "**Inbound Routes"**.

   [![Inbound routes "Add" icon. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150747864/1a6bcfc2cadbbdcfbc2ec9d3/jPMbNBVKex8YhE4o0C33NUyaYJlxvrWlzVJmwsuabh-yS9w42WUNUgEEJ8IE3zUiYq24YA1SXTVw8-e5BUYPujL-3i7KaXzFLqsMzqMUDmwefSTCWHz_QL55U9Sz-tf6QsfCEb0K?expires=1781167500&signature=95f759f1f40647a0e5dce081aba56649ce770569797c713794325d8a467bc555&req=dSUnEc15lYdbFb4f3HP0gNsCiIesZMpVdMmusmN9ttGxdUBHP4P90jYvO9OG%0AUMA%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150747864/1a6bcfc2cadbbdcfbc2ec9d3/jPMbNBVKex8YhE4o0C33NUyaYJlxvrWlzVJmwsuabh-yS9w42WUNUgEEJ8IE3zUiYq24YA1SXTVw8-e5BUYPujL-3i7KaXzFLqsMzqMUDmwefSTCWHz_QL55U9Sz-tf6QsfCEb0K?expires=1781167500&signature=95f759f1f40647a0e5dce081aba56649ce770569797c713794325d8a467bc555&req=dSUnEc15lYdbFb4f3HP0gNsCiIesZMpVdMmusmN9ttGxdUBHP4P90jYvO9OG%0AUMA%3D%0A)
3. #### Enter in the patterns which apply to this inbound rule. [This is a good article](https://www.voip-info.org/asterisk-dialplan-patterns/) to understand how to correctly format the pattern.

   [![Inbound rule pattern input. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150747865/8d6ba775a332067d842da4e3/Bvn33nx0cuum_da-PqxRXvxR0BNqVg9z9wBLo4OJFeXpyh1bPHq2GrIH9DlJst8n11l8Wun7MM6sKqOp6ECvinoymHAuLRY5eaIiPHbnERKywauQnzviVuypYjrKwtqvIQRzikaa?expires=1781167500&signature=3ae5b8c786a89be695fdda94a3252fac8ca2faa898b2c6bb02498f866c39e419&req=dSUnEc15lYdaFb4f3HP0gL5A13q4Xy%2FcQAiNwCGC4LKdUpG33BxDy%2BuVEXqV%0Ag5s%3D%0A)](https://www.voip-info.org/asterisk-dialplan-patterns/)
4. #### In default mode select your default destination as *Extension*.

   [![Default destination selection interface. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150747871/8333eb567d355b5c6b192fe4/yNTA3yzYknV5YK41wNeQ6x6iLx7HhSJOB6exx4dwBtfseeYMEna0LWL7CKXOEU4iIeZB6quGC3sLkqgDTTm39MxOJY_AFLu3V_wD8d3yTTVicAjm-6vv_81mL_-iQsh_IyIY3QxP?expires=1781167500&signature=592dbe8566df43c167fbc0dbf02a05680808b84101ce2cf85d1acb4fa130ca6e&req=dSUnEc15lYZeFb4f3HP0gFBqTj5vdv6KXhkEVvuT%2FFCasKahvur23XCsyz0L%0AjLc%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150747871/8333eb567d355b5c6b192fe4/yNTA3yzYknV5YK41wNeQ6x6iLx7HhSJOB6exx4dwBtfseeYMEna0LWL7CKXOEU4iIeZB6quGC3sLkqgDTTm39MxOJY_AFLu3V_wD8d3yTTVicAjm-6vv_81mL_-iQsh_IyIY3QxP?expires=1781167500&signature=592dbe8566df43c167fbc0dbf02a05680808b84101ce2cf85d1acb4fa130ca6e&req=dSUnEc15lYZeFb4f3HP0gFBqTj5vdv6KXhkEVvuT%2FFCasKahvur23XCsyz0L%0AjLc%3D%0A)
5. #### Click "**Save"** in the top right-hand corner of the screen.

[Back to Top](#h_ffb5e1a080)

## 4. Create outbound route

Outbound routing is a set of rules that tells FreePBX which Telnyx trunk to use for any given outbound call. Having multiple trunks allows you to control cost by routing calls over the least costly trunk for a particular call. Outbound routes are used to specify what numbers are allowed to go out a particular route.

You will want to make sure you define routes for all types of calls. Not defining a route can leave your users frustrated when they need to make an important call.

### Steps:

1. #### In the left-hand navigation, expand "**Extension/Trunk"** and click "**Outbound Routes"** in the sub-menu.

   [![Outbound routes page in the Extension/Trunk tab. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150747875/1c0c5244130ff3ca59de4759/fyB3Lal9qR1mZ9ymcT3Pc77zqOhB_j896sp0NK8dcqlsDMEO9PKbhzNYMcCmFKQI8z983bHD7mPnXFg2tQ8V8zUkzunV03OMKgjJNrHv1UPgKxM9eIsFjn0omnwrSnqtzvJ0VF46?expires=1781167500&signature=c386a7c630a81ad43ab601fe5e436a426b0805d717ce96e2121793e2274b21f9&req=dSUnEc15lYZaFb4f3HP0gM2xmh6%2B%2F1VZ6ukaTNX67o7FdBAqhr6xk7w8R97k%0Acpw%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150747875/1c0c5244130ff3ca59de4759/fyB3Lal9qR1mZ9ymcT3Pc77zqOhB_j896sp0NK8dcqlsDMEO9PKbhzNYMcCmFKQI8z983bHD7mPnXFg2tQ8V8zUkzunV03OMKgjJNrHv1UPgKxM9eIsFjn0omnwrSnqtzvJ0VF46?expires=1781167500&signature=c386a7c630a81ad43ab601fe5e436a426b0805d717ce96e2121793e2274b21f9&req=dSUnEc15lYZaFb4f3HP0gM2xmh6%2B%2F1VZ6ukaTNX67o7FdBAqhr6xk7w8R97k%0Acpw%3D%0A)

   ####
2. #### Name the calling rule name to something of your choice and add the number pattern.

   [![Outbound routes page in the Extension/Trunk tab. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150747881/e9ab3af274e44edd675cbb2e/5GeU9dSprLq7ap7SZrEuzZT1CoLTCjpRPlfJ2D-SEB5xHJodaAxH8JSPzVwA_578Q0uJTeMteAsarXCkDfnkZx8L32Xy3qXNnL-6wAc79FBKOZHx_SpC_IPRyFE-JiJkUoTTgWz5?expires=1781167500&signature=c5d38d4d85ab34ca50c1890b21627d7f4912ebe351d5bf92b18abe6d54bd6f91&req=dSUnEc15lYleFb4f3HP0gDuxhXouNNdlDB7h5zjUXQ%2FLgAQp3iBZUJlRSf%2Bp%0APqM%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150747881/e9ab3af274e44edd675cbb2e/5GeU9dSprLq7ap7SZrEuzZT1CoLTCjpRPlfJ2D-SEB5xHJodaAxH8JSPzVwA_578Q0uJTeMteAsarXCkDfnkZx8L32Xy3qXNnL-6wAc79FBKOZHx_SpC_IPRyFE-JiJkUoTTgWz5?expires=1781167500&signature=c5d38d4d85ab34ca50c1890b21627d7f4912ebe351d5bf92b18abe6d54bd6f91&req=dSUnEc15lYleFb4f3HP0gDuxhXouNNdlDB7h5zjUXQ%2FLgAQp3iBZUJlRSf%2Bp%0APqM%3D%0A)
3. #### Set your privilege level to match the service plan in the outbound settings on your Telnyx portal.

   [![Privilege level settings in the Outbound routes section. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150747882/2c01f87cce1753ac6030ef0a/CwFWCC3b4V-0ueNz7rXLkSoRagWkM0G0EtL4QwSMPIaXgr6KxbMDlinXKAJcKE1h18km6t5sZBodth0a1OL6XqrPazPt38WSMBJZIBPu6UNDVfXmqyjsG4uKSd3vM0NBsjjILm_3?expires=1781167500&signature=1074d65d6dec5194debcdb2d2d3ec32a01ff902f97246ba25cbcbf6a0ffabc6e&req=dSUnEc15lYldFb4f3HP0gLn63Bt0PUpqX5hJFk79uab7FKZTAKp5aOwGGSZV%0AAQI%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150747882/2c01f87cce1753ac6030ef0a/CwFWCC3b4V-0ueNz7rXLkSoRagWkM0G0EtL4QwSMPIaXgr6KxbMDlinXKAJcKE1h18km6t5sZBodth0a1OL6XqrPazPt38WSMBJZIBPu6UNDVfXmqyjsG4uKSd3vM0NBsjjILm_3?expires=1781167500&signature=1074d65d6dec5194debcdb2d2d3ec32a01ff902f97246ba25cbcbf6a0ffabc6e&req=dSUnEc15lYldFb4f3HP0gLn63Bt0PUpqX5hJFk79uab7FKZTAKp5aOwGGSZV%0AAQI%3D%0A)
4. #### Select your trunk in the use trunk section

   [![Trunk selection portal. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150747886/df4d660900b255a16fd5a1c0/Mum0irVGA-04lk_Al-LJRJ2Xcc6d6J-QLlErWWsqfQHmUHlDacNgY_xPEZl9Vge_fiK0pjEF6Dg2qvVR5FIJKvhBZaMpRKo5kWTI-l9hN23WJxImdjbAFfqgLJLub8jjpi6ryFhh?expires=1781167500&signature=c04f9a8b0ef423f0cfc54c1f18fbd388d2ca49d9ce35928c603075374560b4f5&req=dSUnEc15lYlZFb4f3HP0gDSWg9kufsiYIC%2BqkAPtkEZ1m%2Fm5offWMihkr15J%0A4ko%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150747886/df4d660900b255a16fd5a1c0/Mum0irVGA-04lk_Al-LJRJ2Xcc6d6J-QLlErWWsqfQHmUHlDacNgY_xPEZl9Vge_fiK0pjEF6Dg2qvVR5FIJKvhBZaMpRKo5kWTI-l9hN23WJxImdjbAFfqgLJLub8jjpi6ryFhh?expires=1781167500&signature=c04f9a8b0ef423f0cfc54c1f18fbd388d2ca49d9ce35928c603075374560b4f5&req=dSUnEc15lYlZFb4f3HP0gDSWg9kufsiYIC%2BqkAPtkEZ1m%2Fm5offWMihkr15J%0A4ko%3D%0A)

[Back to Top](#h_ffb5e1a080)

## 5. Configure an outbound caller ID

Now let's configure your outbound caller ID. Grandstream offers many ways to configure a caller ID on your SIP trunk. This section will demonstrate 3 ways of doing this:

* Setting a single global outbound caller ID which will apply to every number on your trunk.
* Setting a unique caller ID for every extension on your trunk.
* Setting a unique caller ID for every outbound route you create (every extension associated with that route will have the same caller ID)

|  |
| --- |
| ***Note:*** *Before configuring an outbound caller ID, you should be aware of some of the naming conventions standard for caller ID creation:*  * *Your outbound Caller ID Name should be in **capital letters**. This will appears more clearly/visible on some devices.* * *You **must NOT use any special characters**, as they will not be displayed.* * *Some of regular **Canadian providers will not show more than 15 characters**. We suggest shrinking or adapt your caller ID.* * ***Spaces are allowed*** *in a caller id name.* * *Be familiar with [Telnyx's caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy)* |

1. To enable a global outbound CID:   
   From the left-hand navigation, expand **PBX Settings** and click **General Settings** in the sub-menu.

   [![General settings sub-tab in the PBX settings section. ](https://downloads.intercomcdn.com/i/o/335830117/c13d1a15d6709858837068d3/image.png?expires=1781167500&signature=89319cabcb620794bd41085120ae9da5d256d1f9c5e6a394708727fac4e8ba89&req=dyMiHsp%2BnIBYFb4f3HP0gFhBH6nk4w18%2Fi4tQlMTssqy2FSynG9%2BCCuSJOWy%0AfW4%3D%0A)](https://downloads.intercomcdn.com/i/o/335830117/c13d1a15d6709858837068d3/image.png?expires=1781167500&signature=89319cabcb620794bd41085120ae9da5d256d1f9c5e6a394708727fac4e8ba89&req=dyMiHsp%2BnIBYFb4f3HP0gFhBH6nk4w18%2Fi4tQlMTssqy2FSynG9%2BCCuSJOWy%0AfW4%3D%0A)
2. To enable caller IDs for each extension:  
   From the left-hand navigation, expand **Extension/Trunk** and click **Extensions** in the sub-menu.
3. Click on the extension you want to assign a caller ID and provide your caller ID in the **CallerID Number** field.

   [![Extension/Trunk sub-menu. ](https://downloads.intercomcdn.com/i/o/335830666/ec0d2f32f7ce7f49ff3a1742/image.png?expires=1781167500&signature=c2ddb2104abe5ca0dd106ab64203598a13890d1ad84b457f6b5866e1a9a4f998&req=dyMiHsp%2Bm4dZFb4f3HP0gBu3Rmghm4PmJTcdbiTgtbMUGvsYcZqYUN00N0rh%0A3cA%3D%0A)](https://downloads.intercomcdn.com/i/o/335830666/ec0d2f32f7ce7f49ff3a1742/image.png?expires=1781167500&signature=c2ddb2104abe5ca0dd106ab64203598a13890d1ad84b457f6b5866e1a9a4f998&req=dyMiHsp%2Bm4dZFb4f3HP0gBu3Rmghm4PmJTcdbiTgtbMUGvsYcZqYUN00N0rh%0A3cA%3D%0A)
4. To enable a caller ID on the outbound route:  
   From the left-hand navigation, expand **Extension/Trunk** and click **Outbound Routes** in the sub-menu.
5. From here, you can set your caller ID for the entire route in the **Outbound Route CID** field.

   [![Outbound route CID field. ](https://downloads.intercomcdn.com/i/o/335831103/250b42f48aa90471dc909127/image.png?expires=1781167500&signature=e9efcf9c2272e0101ad310179d987708809207dfe3d5edd402a297b56f071ebf&req=dyMiHsp%2FnIFcFb4f3HP0gF8AJVFq9m3Y7glCQ4HLf6tBb5tH0xuWa8CbIv1W%0AvP4%3D%0A)](https://downloads.intercomcdn.com/i/o/335831103/250b42f48aa90471dc909127/image.png?expires=1781167500&signature=e9efcf9c2272e0101ad310179d987708809207dfe3d5edd402a297b56f071ebf&req=dyMiHsp%2FnIFcFb4f3HP0gF8AJVFq9m3Y7glCQ4HLf6tBb5tH0xuWa8CbIv1W%0AvP4%3D%0A)

That's it, you've now completed the configuration of Grandstream and can now make and receive calls by using Telnyx as your SIP provider!

[Back to Top](#h_ffb5e1a080)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally, you can check out:

* [Product datasheet](https://www.grandstream.com/hubfs/Product_Documentation/datasheet_ucm6200_series_english.pdf?hsLang=en) (English)
* [Grandstream FAQ](https://blog.grandstream.com/faq)
* [Grandstream user forum](https://forums.grandstream.com/)
* [Grandstream Learning Center](https://www.grandstream.com/learning-center)
* [Grandstream firmware updates](https://www.grandstream.com/support/firmware)
* How-to guides for [UCM6200 series](https://www.grandstream.com/support/resources?title=UCM6200%20series) and [UCM6510 series](https://www.grandstream.com/support/resources?title=UCM6510)
* [Administrator's user manual](https://www.grandstream.com/hubfs/Product_Documentation/ucm62xx_usermanual.pdf)

---

Related Articles

[Grandstream: IP Auth Setup](https://support.telnyx.com/en/articles/2950523-grandstream-ip-auth-setup)[Grandstream UCM6xxx: SIP Trunks](https://support.telnyx.com/en/articles/5748258-grandstream-ucm6xxx-sip-trunks)[Grandstream GRP260x: SIP Trunk](https://support.telnyx.com/en/articles/6169513-grandstream-grp260x-sip-trunk)[Grandstream GXP1700: SIP Trunk](https://support.telnyx.com/en/articles/6184520-grandstream-gxp1700-sip-trunk)[Grandstream GXV3370](https://support.telnyx.com/en/articles/6187576-grandstream-gxv3370)

Did this answer your question?

😞😐😃

Table of contents
