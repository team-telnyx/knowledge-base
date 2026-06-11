---
source_url: https://support.telnyx.com/en/articles/3284164-elastix-5-credentials-trunk
scraped: 2026-06-11
---

Elastix 5: Credentials Trunk | Telnyx Help Center

[Skip to main content](#main-content)

# Elastix 5: Credentials Trunk

In this article we will explain how to configure an Elastix 5 Credentials Trunk.

C

Written by Customer Success

October 23, 2023

Table of contents

[Jump to Instructions](#h_ddd07169a1)

[Elastix 5](https://www.3cx.com/) is a **high-performance turnkey PBX** that’s easy to install and manage. Powered by 3CX you get a complete unified communications solution with softphones included for Android, iOS, Windows and Mac as well as a web-client. Supported IP Phones, Trunks and gateways are all automatically configured with inbuilt templates. You also get integrated WebRTC video conferencing for free. Available on-premise on Windows, Linux, Raspberry Pi or in the Cloud.

Additional documentation:

* [Elastix admin guide](https://www.3cx.com/docs/manual/)
* [Elastix user guide](https://www.3cx.com/user-manual/)
* [Elastix support](https://www.3cx.com/support/)

---

# Instructions for Configuring Elastix

In this activity you will:

1. [Complete first-time setup of Elastix](#h_bb21d4fcff)
2. [Create a Telnyx SIP trunk](#h_7ee5612075)
3. [Create inbound rules](#h_165e1f85b4)
4. [Create outbound rules](#h_35f616006a)

**Pre-requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* [Purchase a DID](https://portal.telnyx.com/#/app/numbers/search-numbers)
* [Set up your Telnyx SIP connection](https://portal.telnyx.com/#/app/connections)
* [Provision your number](https://portal.telnyx.com/#/app/numbers/my-numbers) (Assign it to a SIP connection)
* [Create an outbound voice profile](https://portal.telnyx.com/#/app/outbound)
* Create a [credentials-based connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
* [Download](https://www.3cx.com/community/threads/elastix-2-0-0-57-iso-download.112659/) and [install](https://www.3cx.com/community/threads/elastix-2-0-0-57-iso-download.112659/) Elastix

  + You'll need an [Elastix license key](https://www.3cx.com/phone-system/download-phone-system/)
  + Take note of any username/password combination you set during this activity. You'll need them at a later stage.

**Video walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Elastix/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Complete first-time setup of Elastix

In this section, we will complete installation and initial setup of your Elastix 5 service.

1. ### **Once the installation has finished, you'll be prompted to choose either running the tool from the "web browser" or from the "command line". We recommend the web browser. There is a "URL" provided which you will need to use to access the graphical user interface in order to configure Elastix 5.**

   [![3CX Configuration Tool. ](https://downloads.intercomcdn.com/i/o/143556737/402befb9c7a4beb18b59b817/elastix1.png?expires=1781168400&signature=f60a7bf48cdce30fde0a42f710da842f432e5a1f5e6132db9dbcca3a1e6ea760&req=dSQkE8x4moJYFb4f3HP0gB2AmQPQu%2B4XJlI22JFrFf6HQ314oItMBtZsA4%2F%2B%0Af1A%3D%0A)](https://downloads.intercomcdn.com/i/o/143556737/402befb9c7a4beb18b59b817/elastix1.png?expires=1781168400&signature=f60a7bf48cdce30fde0a42f710da842f432e5a1f5e6132db9dbcca3a1e6ea760&req=dSQkE8x4moJYFb4f3HP0gB2AmQPQu%2B4XJlI22JFrFf6HQ314oItMBtZsA4%2F%2B%0Af1A%3D%0A)
2. ### **Once you've acquired the key, proceed to creating a new install and click "Next".**

   [![3CX Phone system installation page. ](https://downloads.intercomcdn.com/i/o/143557927/793d5628eec24a0d1987c89b/elastix2.png?expires=1781168400&signature=88edc482f219b03cd8967b5fdbae27b31cf0ceb615486722ca12632692e5968c&req=dSQkE8x5lINYFb4f3HP0gAvnM8Fa5wIsFX0KVkud188KE%2Bpry4e3bxAkynF8%0ApHs%3D%0A)](https://downloads.intercomcdn.com/i/o/143557927/793d5628eec24a0d1987c89b/elastix2.png?expires=1781168400&signature=88edc482f219b03cd8967b5fdbae27b31cf0ceb615486722ca12632692e5968c&req=dSQkE8x5lINYFb4f3HP0gAvnM8Fa5wIsFX0KVkud188KE%2Bpry4e3bxAkynF8%0ApHs%3D%0A)
3. ### **Your public IP address will automatically be detected next and you can choose to either go with the one that was detected or enter an IP address in manually. Once you've done this, click "Next".**
4. ### **Choose whether your IP address is "static" or "dynamic" and click "next".**

   [![Public IP installation page. ](https://downloads.intercomcdn.com/i/o/143558250/4ceef3e2b66fe4718954e223/elastix4.png?expires=1781168400&signature=8167f577b5c522f793665665b14729fcd0da6141bbd2fbeffabf619ae3229f4b&req=dSQkE8x2n4RfFb4f3HP0gKCkPWU1Vjis%2FolPam6gMlJ50KlkgJ0ho6UE7DcB%0AFjY%3D%0A)](https://downloads.intercomcdn.com/i/o/143558250/4ceef3e2b66fe4718954e223/elastix4.png?expires=1781168400&signature=8167f577b5c522f793665665b14729fcd0da6141bbd2fbeffabf619ae3229f4b&req=dSQkE8x2n4RfFb4f3HP0gKCkPWU1Vjis%2FolPam6gMlJ50KlkgJ0ho6UE7DcB%0AFjY%3D%0A)
5. ### **Select the ports required for 3CX Management console. They automatically populate default values for you but you can choose your own.**

   [![Port selection for web services installation page. ](https://downloads.intercomcdn.com/i/o/143558339/9ec488d8343fe30a328d8c99/elastix5.png?expires=1781168400&signature=9c028a37fa3d507d430535a3b768d50cba9a163409b2a2101e7e88f5bdbdd504&req=dSQkE8x2noJWFb4f3HP0gOdVeBAe9%2BDNPKoxU5ZFYuM9J3JmuYj%2B7eC869oD%0AeA8%3D%0A)](https://downloads.intercomcdn.com/i/o/143558339/9ec488d8343fe30a328d8c99/elastix5.png?expires=1781168400&signature=9c028a37fa3d507d430535a3b768d50cba9a163409b2a2101e7e88f5bdbdd504&req=dSQkE8x2noJWFb4f3HP0gOdVeBAe9%2BDNPKoxU5ZFYuM9J3JmuYj%2B7eC869oD%0AeA8%3D%0A)
6. ### **Proceed to select the default network adapter.**

   [![Default Network Adapter. ](https://downloads.intercomcdn.com/i/o/143558380/903331428623352df0b7cc7a/elastix6.png?expires=1781168400&signature=c67464dc93709cd747e567dd4aacc34c696ffc966b126c6688f2331fb942d73d&req=dSQkE8x2nolfFb4f3HP0gJFuOBYWmY8sg6BHI92J8tV59hxsdP7U7dLozg7N%0ANhs%3D%0A)](https://downloads.intercomcdn.com/i/o/143558380/903331428623352df0b7cc7a/elastix6.png?expires=1781168400&signature=c67464dc93709cd747e567dd4aacc34c696ffc966b126c6688f2331fb942d73d&req=dSQkE8x2nolfFb4f3HP0gJFuOBYWmY8sg6BHI92J8tV59hxsdP7U7dLozg7N%0ANhs%3D%0A)
7. ### **Your FQDN and certificates will now be generated.**

   [![FQDN and certificates installation page. ](https://downloads.intercomcdn.com/i/o/143558545/b762af62282fe9620a99a6ae/elastix7.png?expires=1781168400&signature=4f8c85a6f64a184732891a2b02c162baf6283c660ddbb5d0ef51c1a9524bcd81&req=dSQkE8x2mIVaFb4f3HP0gF01uthin923bmLd3WURvvubiWtAnAJ%2BoLZw1pm3%0Al1I%3D%0A)](https://downloads.intercomcdn.com/i/o/143558545/b762af62282fe9620a99a6ae/elastix7.png?expires=1781168400&signature=4f8c85a6f64a184732891a2b02c162baf6283c660ddbb5d0ef51c1a9524bcd81&req=dSQkE8x2mIVaFb4f3HP0gF01uthin923bmLd3WURvvubiWtAnAJ%2BoLZw1pm3%0Al1I%3D%0A)
8. ### **Select how many digits your extensions should have.**

   [![3CX extension length. ](https://downloads.intercomcdn.com/i/o/143558586/a952d9268957d6186f3a6a72/elastix8.png?expires=1781168400&signature=18e1a5e68fd6cbfd2518449fd57d6405eb17aeda4bc71684d586da1dfdf222e2&req=dSQkE8x2mIlZFb4f3HP0gFzbkTK2IJ6bNdIlud6537C5BWw%2FmKu0ym35xN30%0A%2Bv4%3D%0A)](https://downloads.intercomcdn.com/i/o/143558586/a952d9268957d6186f3a6a72/elastix8.png?expires=1781168400&signature=18e1a5e68fd6cbfd2518449fd57d6405eb17aeda4bc71684d586da1dfdf222e2&req=dSQkE8x2mIlZFb4f3HP0gFzbkTK2IJ6bNdIlud6537C5BWw%2FmKu0ym35xN30%0A%2Bv4%3D%0A)
9. ### **Enter an Email for important system notifications.**

   [![Admin Email for important system notifications. ](https://downloads.intercomcdn.com/i/o/143558637/8c944ed27964815e3aafd8c5/elastix9.png?expires=1781168400&signature=95078589861cd0c53635f612edf6b50e79b7453f9cc705d8f096dd22c9d1b78c&req=dSQkE8x2m4JYFb4f3HP0gMdYzNGk01a%2BfVrpj%2F4ylMJyjTGA7Osqz73gCzkI%0AP4M%3D%0A)](https://downloads.intercomcdn.com/i/o/143558637/8c944ed27964815e3aafd8c5/elastix9.png?expires=1781168400&signature=95078589861cd0c53635f612edf6b50e79b7453f9cc705d8f096dd22c9d1b78c&req=dSQkE8x2m4JYFb4f3HP0gMdYzNGk01a%2BfVrpj%2F4ylMJyjTGA7Osqz73gCzkI%0AP4M%3D%0A)
10. ### **Select Country and Time Zone.**

    [![country and time zone installation page. ](https://downloads.intercomcdn.com/i/o/143558666/7474883b9675fbfaba5668fd/elastix10.png?expires=1781168400&signature=8f9e35457f8f46b98b8ffe9688cbded488329a33499340037ea945aae9e02155&req=dSQkE8x2m4dZFb4f3HP0gDpncgoVjip%2F7aUfkmXeaDERhvWnUFqZuaTiv%2BwQ%0Aav0%3D%0A)](https://downloads.intercomcdn.com/i/o/143558666/7474883b9675fbfaba5668fd/elastix10.png?expires=1781168400&signature=8f9e35457f8f46b98b8ffe9688cbded488329a33499340037ea945aae9e02155&req=dSQkE8x2m4dZFb4f3HP0gDpncgoVjip%2F7aUfkmXeaDERhvWnUFqZuaTiv%2BwQ%0Aav0%3D%0A)
11. ### **Create an Operator Extension.**

    [![Operator extension installation page. ](https://downloads.intercomcdn.com/i/o/143558747/57310910f8da7ed023112d67/elastix11.png?expires=1781168400&signature=132941b3c9f23c5de427b7720e1e2937efd252507cf4a7be0e9e7b88487442f0&req=dSQkE8x2moVYFb4f3HP0gCJvWBvJgYTDa4osG0JUMEiymzRYqNfvBL7d2eS6%0A4FE%3D%0A)](https://downloads.intercomcdn.com/i/o/143558747/57310910f8da7ed023112d67/elastix11.png?expires=1781168400&signature=132941b3c9f23c5de427b7720e1e2937efd252507cf4a7be0e9e7b88487442f0&req=dSQkE8x2moVYFb4f3HP0gCJvWBvJgYTDa4osG0JUMEiymzRYqNfvBL7d2eS6%0A4FE%3D%0A)
12. ### **As an additional security measure, you can specify to which countries calls can be made.**

    [![Preferred language installation page. ](https://downloads.intercomcdn.com/i/o/143558811/6d24fc5ac9bf66406c6cadac/elastix12.png?expires=1781168400&signature=c11b67d4b10d001d636bc5981b086b731163da2c4595e01fbd7917d309964026&req=dSQkE8x2lYBeFb4f3HP0gJW9VkN69%2FaDtUa9Ba4IpWwbbXYalusqNVYOqY7w%0AIBA%3D%0A)](https://downloads.intercomcdn.com/i/o/143558811/6d24fc5ac9bf66406c6cadac/elastix12.png?expires=1781168400&signature=c11b67d4b10d001d636bc5981b086b731163da2c4595e01fbd7917d309964026&req=dSQkE8x2lYBeFb4f3HP0gJW9VkN69%2FaDtUa9Ba4IpWwbbXYalusqNVYOqY7w%0AIBA%3D%0A)
13. ### **Select your preferred language.**

    [![Preferred language installation page. ](https://downloads.intercomcdn.com/i/o/143558822/8c4636d6da2cef7a5a147910/elastix13.png?expires=1781168400&signature=4916e241028955406497ddbff79175ee98bf8b17846e170aff75cda013f0a84e&req=dSQkE8x2lYNdFb4f3HP0gNwjo66OX0fd2qiWE7HLHWKqdCB%2BiZOga03mgKRu%0AQDg%3D%0A)](https://downloads.intercomcdn.com/i/o/143558822/8c4636d6da2cef7a5a147910/elastix13.png?expires=1781168400&signature=4916e241028955406497ddbff79175ee98bf8b17846e170aff75cda013f0a84e&req=dSQkE8x2lYNdFb4f3HP0gNwjo66OX0fd2qiWE7HLHWKqdCB%2BiZOga03mgKRu%0AQDg%3D%0A)
14. ### **At this point the PBX basic settings are now fully configured and you'll be shown a congratulations page upon successfully completing the steps. Make sure you note the details that are provided but a copy of the details are also sent to the admin email you specified on a previous step.**
15. ### **Use the FQDN or your public IP address URL in order to access the PBX interface. If the PBX is on your local LAN, and your router has a firewall, ensure to apply port forwarding to the ports you specified in step 3 - otherwise the interface may not resolve for you.**
16. ### **Log in with the "username" and "password" you created.**

    [![3CX management console. ](https://downloads.intercomcdn.com/i/o/143559374/c8f484b1256d9d5866226256/elastix15.png?expires=1781168400&signature=763fa2e4504e417de82207e1ccbc2c11aa3d3d3191f223cb5a7895c9a9ede623&req=dSQkE8x3noZbFb4f3HP0gGWy091edrCjARlOFZA5q8O3CybLQNK%2BKChkmBWA%0Ad6o%3D%0A)](https://downloads.intercomcdn.com/i/o/143559374/c8f484b1256d9d5866226256/elastix15.png?expires=1781168400&signature=763fa2e4504e417de82207e1ccbc2c11aa3d3d3191f223cb5a7895c9a9ede623&req=dSQkE8x3noZbFb4f3HP0gGWy091edrCjARlOFZA5q8O3CybLQNK%2BKChkmBWA%0Ad6o%3D%0A)
17. ### **You'll be brought the the dashboard now.**

    [![3CX management dashboard console. ](https://downloads.intercomcdn.com/i/o/143560121/3bcb5b2dd331319d3f4627f7/elsatix16.png?expires=1781168400&signature=6ac9ee85bef0faaf4d07d491125f4ed062006dfc3351cb10d18311cac843d1a1&req=dSQkE89%2BnINeFb4f3HP0gO6NagGak5eSomi8k7r%2Bk%2BiUkjrmie4GQPESJZ8F%0A3d0%3D%0A)](https://downloads.intercomcdn.com/i/o/143560121/3bcb5b2dd331319d3f4627f7/elsatix16.png?expires=1781168400&signature=6ac9ee85bef0faaf4d07d491125f4ed062006dfc3351cb10d18311cac843d1a1&req=dSQkE89%2BnINeFb4f3HP0gO6NagGak5eSomi8k7r%2Bk%2BiUkjrmie4GQPESJZ8F%0A3d0%3D%0A)
18. ### **Go to "Settings > Network to confirm your network settings":**
19. ### **On the "Ports" Tab set:**

    1. #### **"SIP Port":** *5060*
20. ### **On the "Public IP" Tab: Find the "External IP Configuration" section and double check your Public IP is correct and that you have selected the proper Network card Interface.**

    ***Note*** *: Please make sure that connection IP on the Telnyx Mission Control Portal and Static Public IP are the same. You can also use the FQDN for inbound calls and the IP for outbound calls.*

[Back to Top](#h_ddd07169a1)

## 2. Create a Telnyx SIP trunk

In this section, you will create a [SIP trunk](https://telnyx.com/products/sip-trunks) between Elastix and Telnyx.

1. ### **From the left-hand navigation, click on "SIP Trunks".**
2. ### **Click "+ Add SIP Trunk" near the top of the screen.**
3. ### **A new pop up will be opened. You need to enter/select all the required details :**

   1. #### **"Select Country": Worldwide**
   2. #### **"Select Provider in your Country": Telnyx LLC**
   3. ### **"Main Trunk No": <Enter the number which you have purchased on your Telnyx Mission Control Portal>**

      [![SIP Trunk/VoIP Provider interface. ](https://downloads.intercomcdn.com/i/o/135579193/a8b2e2765d9bda80062168c4/image.png?expires=1781168400&signature=1a82b8522d6a991afc8c8b72d3b5a7e2ccc95bbf5b6a1bb6c39ee957cc78f033&req=dSMiE853nIhcFb4f3HP0gPeFdJTyZX%2Fn6J66xtuDvAfrcegl5tOowqN7iPq%2F%0ADAQ%3D%0A)](https://downloads.intercomcdn.com/i/o/135579193/a8b2e2765d9bda80062168c4/image.png)
4. ### **After entering the details, Click on "OK".**
5. ### **This will open the trunk configuration window.**
6. ### **Click on the "General" tab and start at the "Trunk Details" section. Provide the following information:**

   1. #### **"Enter name of Trunk":** *Telnyx LLC*
   2. #### **"Registrar/Server/Gateway Hostname or IP":** *sip-anycast1.telnyx.com:5060* or *sip.telnyx.com:5060*
   3. #### **"Outbound Proxy":** *sip.telnyx.com*
   4. #### **"Number of SIM Calls":** <set your preferred amount of simultaneous calls>

      [![3CX Dashboard. ](https://downloads.intercomcdn.com/i/o/116804887/1ccdf298a762d01836e22412/change.jpg?expires=1781168400&signature=3ce8b583161f594a138feccabdb06b5ca2fa7c4cfa5c3d5ca521f23d9946c95e&req=dSEhHsl6lYlYFb4f3HP0gHxewZ8RBkSdyW4Mi2CT%2BVA0%2BTkxZNzeDS8XV6Kn%0A0os%3D%0A)](https://downloads.intercomcdn.com/i/o/116804887/1ccdf298a762d01836e22412/change.jpg)
7. ### **Find the "Authentication" section and provide the following information:**

   1. #### **"Type of Authentication":** *Register/Account based*
   2. #### **"Authentication ID (aka SIP user ID)":** Your Telnyx account username
   3. #### **"Authentication Password":** Your Telnyx account password

      [![Authentication dashboard on 3CX. ](https://downloads.intercomcdn.com/i/o/37739545/266e21680c7755f64d1f0a59/File1509107718169?expires=1781168400&signature=d67be9450a72f43927662bf172ed32a522159786c4ff0022a9521fd014b1261a&req=dycgFcB7mYQTWLcX3D%2B5hgJVsXrbJGf9bT5jLQ%2FZALf42osH31gkzjrLLWke%0Agw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/37739545/266e21680c7755f64d1f0a59/File1509107718169)
8. ### **Now find the "Route calls to" section and provide the following information:**

   1. #### **"Main Trunk number":** By default number will be shown. You need cross-verify with the number which you have purchased on telnyx portal
   2. #### **"Destination for calls during the office hours":** Based on your requirement
   3. #### **"Destination for calls outside the office hours":** Based on your requirement

      [!["Route calls to" section on 3CX. ](https://downloads.intercomcdn.com/i/o/37739546/c3223abe1f08d0257ad372cb/File1509107718207?expires=1781168400&signature=4b1c5a7a3a28530c7150a700197c9574387d6ad3b7a6595e956227ec91ab2fa8&req=dycgFcB7mYcTWLcX3D%2B5hjGV3F3SDMaAWEaesZJfZ3sKbd8bBopCuUB%2Bu2xS%0AQg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/37739546/c3223abe1f08d0257ad372cb/File1509107718207)
9. ### **Click on the "Options" tab and provide the following information:**

   1. #### **"Require registration for":** *Do not require*
   2. #### Remove the *GSM-FR* from "**Assigned Codecs"**
10. ### **Click "Apply".**
11. ### **Click on the "Outbound Parameters" tab.**
12. ### **Find the "SIP Field" section and provide the following information:**

    1. #### **"Contact User Part":** *Custom Field* (Leave the custom value blank)

       [![Outbound procedures field. ](https://downloads.intercomcdn.com/i/o/335778657/21461eaf7fb427178897f87a/image.png?expires=1781168400&signature=1a00a26379e9bafe68c7f240bd1fb08610bb1d7fd2d9582e06c4765171b90260&req=dyMiEc52m4RYFb4f3HP0gHmp41ZsBb4RrKnkcy7Y8ZLbTvUlf8JGNvDKVgL9%0AhOk%3D%0A)](https://downloads.intercomcdn.com/i/o/335778657/21461eaf7fb427178897f87a/image.png?expires=1781168400&signature=1a00a26379e9bafe68c7f240bd1fb08610bb1d7fd2d9582e06c4765171b90260&req=dyMiEc52m4RYFb4f3HP0gHmp41ZsBb4RrKnkcy7Y8ZLbTvUlf8JGNvDKVgL9%0AhOk%3D%0A)
13. ### **Click "Apply".**
14. ### **Click "OK" at the top of the page.**
15. ### **If all the fields are entered correctly the IP trunk will now be live. We can now proceed to our inbound and outbound rules.**

    [![SIP Trunks section. ](https://downloads.intercomcdn.com/i/o/37739547/f13058c7b96adaacca2b1e57/File1509107718250?expires=1781168400&signature=0d9c2e82d86e4e7ab245ec1e87da1243e2d2b0bd31a0156156e5a405ff1fd498&req=dycgFcB7mYYTWLcX3D%2B5hlCEe%2BEgwgFq8OGQOuCHzBMwg%2Ftyr0p0%2Bw4wsjoa%0ATQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/37739547/f13058c7b96adaacca2b1e57/File1509107718250)

[Back to Top](#h_ddd07169a1)

## 3. Create inbound rules

In this section, we'll create inbound rules to manage your incoming calls.

1. #### From the left-hand navigation, click "**Inbound Rules"**.
2. #### Click on "**+Add DID Rule**" near the top of the screen.
3. #### In the "**General"** section, provide the following information:

   1. #### **"Name":** give your outbound rule a name that makes sense for your inbound rule.
   2. #### **"DID/DDI":** One of the DIDs you provisioned from Telnyx as part of your [pre-requisite activities](#h_566f57a59c)

      [![Inbound rules section. ](https://downloads.intercomcdn.com/i/o/37739548/7381896e4939a87623dd3dd8/File1509107718295?expires=1781168400&signature=575c2b333b8d078ed2f32c351012602ab73e4ffcb6fff6a6ee103c5cba18ba67&req=dycgFcB7mYkTWLcX3D%2B5hqoynk0%2BwMXXFkFaSROsIDjT%2F%2FLnskHXU6yyLZrH%0APg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/37739548/7381896e4939a87623dd3dd8/File1509107718295)
4. #### In the "**Route calls to"** section, provide the following information:

   1. #### **"Main Trunk number":** By default number will be shown. You need cross-verify with the number which you have purchased on telnyx portal
   2. #### **"Destination for calls during the office hours":** Based on your requirement
   3. #### **"Destination for calls outside the office hours":** Based on your requirement

      [!["Route calls to" section. ](https://downloads.intercomcdn.com/i/o/37739549/5de00fbdcfb9009e4dbec6c8/File1509107718333?expires=1781168400&signature=4af262b3e957b5b03444a2f64717867d38e4549f4c5469e91acf0a96eace1184&req=dycgFcB7mYgTWLcX3D%2B5hsERwMaJ%2BBxpm12ne8YwYIgH%2Fud6qkS55S2YYDyq%0Aiw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/37739549/5de00fbdcfb9009e4dbec6c8/File1509107718333)

[Back to Top](#h_ddd07169a1)

## 4. Create outbound rules

In this section, we'll create outbound rules to manage your outgoing calls.

1. ### **From the left-hand navigation, click Outbound Rules.**
2. ### **Click on +Add near the top of the screen.**
3. ### **In the General section, provide the following information:**

   1. #### **Rule Name:** Enter anything that makes sense for your rule

      [!["Add outbound rule" section. ](https://downloads.intercomcdn.com/i/o/37739550/140544231b9f3347b9215c22/File1509107718366?expires=1781168400&signature=b2e85c6780bbcdc729e7263a63026fd697182c9ea9b969280d7c133ab528ed61&req=dycgFcB7mIETWLcX3D%2B5htRwoGhEFPzhz0qExrpW6QapkFM2PVY4zhyAAgle%0ADQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/37739550/140544231b9f3347b9215c22/File1509107718366)
4. ### **In the "Apply this rule to these calls" section, provide the following information:**

   1. #### **"Calls to numbers starting with prefix":** Leave empty
   2. #### **"Calls from extension(s)":** Provide your extension numbers. We used *000* as an example here.
   3. #### **"Calls to numbers with a length of":** Leave empty

      [!["Apply this rule to these calls" section. ](https://downloads.intercomcdn.com/i/o/37739551/2db181344b002a5942bee926/File1509107718409?expires=1781168400&signature=e5ad0e9205c96dc61ff8d45e742be44a1a5fbdca7f2ea3f017532f8abe94e1e1&req=dycgFcB7mIATWLcX3D%2B5homCSpS5YqRdVizzxfQ3Ugb6r0zhODZExWHb2wr5%0AZg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/37739551/2db181344b002a5942bee926/File1509107718409)
5. ### **In the "Make outbound calls on" section, we will be configuring routes for your calls. We can configure up to 3. The first will be your primary call route and the second and third will be used as backup.For each route, digits can be stripped or added. Strip Digits 0 on Route 1 and Strip Digits 1 digit for remaining 2 routes. This is also one of the many ways an "outbound caller ID" can be applied within 3CX. If you choose to apply an outbound caller ID on your Outbound Route, it will be applied to all calls that proceed through this route.**

   [!["Make outbound calls on" section. ](https://downloads.intercomcdn.com/i/o/335778966/3cbd27c0be807929dc1c3801/image.png?expires=1781168400&signature=6ac78442a4cda28566fe19731fdec21c1c82a4ca5d523a9935d5dfaf31a3e0ee&req=dyMiEc52lIdZFb4f3HP0gEE2KEmkEqW90YSnKnjrdyx5oXEqRsNoU%2Fpz8%2FKH%0ABuU%3D%0A)](https://downloads.intercomcdn.com/i/o/335778966/3cbd27c0be807929dc1c3801/image.png?expires=1781168400&signature=6ac78442a4cda28566fe19731fdec21c1c82a4ca5d523a9935d5dfaf31a3e0ee&req=dyMiEc52lIdZFb4f3HP0gEE2KEmkEqW90YSnKnjrdyx5oXEqRsNoU%2Fpz8%2FKH%0ABuU%3D%0A)

[!["User information" section. ](https://downloads.intercomcdn.com/i/o/335779057/aae96d05cacab1ef742e242c/image.png?expires=1781168400&signature=75d80206dcc5f9c55fcdfcc573a518ac7fcb81c8b4b1ffd0f9cb8130d5b28c29&req=dyMiEc53nYRYFb4f3HP0gNFNO5aKN9YN15ZHxrxQxljo0O9AIF81llCewcje%0A7WV9hwKOn4eY%2Br%2FYOg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/335779057/aae96d05cacab1ef742e242c/image.png?expires=1781168400&signature=75d80206dcc5f9c55fcdfcc573a518ac7fcb81c8b4b1ffd0f9cb8130d5b28c29&req=dyMiEc53nYRYFb4f3HP0gNFNO5aKN9YN15ZHxrxQxljo0O9AIF81llCewcje%0A7WV9hwKOn4eY%2Br%2FYOg%3D%3D%0A)

|  |
| --- |
| ***Note:*** *Before configuring an outbound caller ID, you should be aware of some of the naming conventions standard for caller ID creation:*  * *Your outbound Caller ID Name should be in **capital letters**. This will appears more clearly/visible on some devices.* * *You **must NOT use any special characters**, as they will not be displayed.* * *Some of regular **Canadian providers will not show more than 15 characters**. We suggest shrinking or adapt your caller ID.* * ***Spaces are allowed*** *in a caller id name.* * *Be familiar with [Telnyx's caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy)*  *If you choose not to add an outbound caller ID on your outbound route, you can instead apply it for each user or extension.* |

### **After completing the configuration, click OK.**

That's it, you've now completed the configuration of Elastix 5 Credentials Trunk and can now make and receive calls by using Telnyx as your SIP provider!

[Back to Top](#h_ddd07169a1)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally, you can check out:

* [Elastix admin guide](https://www.3cx.com/docs/manual/)
* [Elastix user guide](https://www.3cx.com/user-manual/)
* [Elastix support](https://www.3cx.com/support/)

---

Related Articles

[Configuring a FreePBX V13 Credentials Trunk](https://support.telnyx.com/en/articles/1130648-configuring-a-freepbx-v13-credentials-trunk)[Configuring a Cisco CME Credentials Trunk](https://support.telnyx.com/en/articles/1130668-configuring-a-cisco-cme-credentials-trunk)[Elastix 5: FQDN Trunk Setup](https://support.telnyx.com/en/articles/3284033-elastix-5-fqdn-trunk-setup)[FreePBX V14: Credentials - ChanSIP](https://support.telnyx.com/en/articles/3284752-freepbx-v14-credentials-chansip)[FreePBX V15: IP Trunk - PJSIP](https://support.telnyx.com/en/articles/5619595-freepbx-v15-ip-trunk-pjsip)

Did this answer your question?

😞😐😃

Table of contents
