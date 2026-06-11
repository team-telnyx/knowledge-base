---
source_url: https://support.telnyx.com/en/articles/6161111-3cx-configuring-a-3cx-v18-pbx
scraped: 2026-06-11
---

3CX: Configuring a 3CX V18 PBX | Telnyx Help Center

[Skip to main content](#main-content)

# 3CX: Configuring a 3CX V18 PBX

Learn how to configure a 3CX V18 PBX SIP Trunk (Calls & Messaging) with Telnyx through their import provider option using XML

Written by Dillin

Updated over 3 weeks ago

Table of contents

[Jump to Instructions](#:~:text=Instructions%20for%20Configuring%20a%203CX%20V18%20PBX%20Trunk)

[3CX](https://www.3cx.com/) is an open standards IP PBX that offers complete Unified Communications, out of the box. Suitable for any business size or industry 3CX can accommodate to your every need; from mobility and status to advanced contact center features and more, at a fraction of the cost.  
​  
3CX makes installation, management and maintenance of your PBX so easy that you can effortlessly manage it yourself, whether on an appliance or server at your premise or in the cloud. This article guides you on how to configure this PBX for making and receiving calls over the internet through a next generation carrier like Telnyx!

|  |
| --- |
| ***NOTE****: you'll need to acquire a license when installing this version of 3CX. You'll be prompted to fill out a [form](https://www.3cx.com/phone-system/download-phone-system/) and include your email address so they can verify your email and send you the license key.*  ***NOTE:*** Telnyx is no longer a supported vendor on 3CX and 3CX has decided to shut down support for third party vendors altogether in some of their versions and to only offer their customers the option to connect with their supported vendors. Please check your 3CX version and make sure third party vendors (non-supported providers from 3CX's perspective) are available in your version. |

---

# Instructions for Configuring a 3CX V18 PBX Trunk

In this guide you will:

1. [Perform a basic setup](#h_9535a5e87f)
2. [Configure your PBX](#h_a477259f1f)

   1. [Confirm your network settings](#h_8036cfb560)
   2. [Create a Telnyx SIP trunk](#:~:text=2.2.%20Create%20a%20Telnyx%20SIP%20Trunk)
   3. [Configure inbound rule](#h_4c36c30479)
   4. [Configure outbound rule](#h_af8b85c3d2)
   5. [See an important example of an outbound rule](#h_15d20e720d)
   6. [Configure an extension for inbound / outbound messaging](#h_c1201e552a)
   7. [Test the 3CX webclient](#h_dd546b7f5a)

## Pre-requisites

* [Set up and configure your Telnyx Mission Control Portal](https://support.telnyx.com/en/articles/5717957-zoiper-5-pro-telnyx-setup#h_dc5df9cfdf)
* Have created a credentials-based or IP based [SIP connection](https://portal.telnyx.com/#/voice/connections) on your Telnyx Mission Control Portal account, assigned this connection to a DID and outbound profile in order to make and receive calls.
* Have created a [messaging profile](https://portal.telnyx.com/#/programmable-messaging/profiles) on your Telnyx Mission Control Portal account, assigned this connection to a DID in order to send and receive messages.
* [Download](https://www.3cx.com/phone-system/download-links/) and [install](https://www.3cx.com/docs/manual/) 3CX

  + Note that during installation, 3CX will provide you with a username and password. You will need these to log into the web interface.

|  |
| --- |
| ***Note:***  *3CX will detect your pubic IP address and you can specify if this is a static or dynamic IP.*    *You can configure your 3CX with an FQDN; 3CX will provide you with one - they do this to ensure your FQDN is set to resolve to your Public IP and for generating certificates.*    *You'll then choose your default network adapter and decide whether you want the extensions to use the local IP of your PBX or the FQDn you created.*    *At the end, you'll choose your preferred http/https port numbers which will be used to allow you to access the 3CX web interface via your FQDN or Public IP.* |

## 1. Perform the basic setup

In this step, you'll do a basic configuration before creating your Telnyx [SIP trunk](https://telnyx.com/products/sip-trunks).

1. Log into 3CX with the username and password provided to you during the installation process.

   [![3CX Sign in screen](https://downloads.intercomcdn.com/i/o/378429732/f483a3f372a7a69e36056f02/image.png?expires=1781168400&signature=82af8d1293daea410723bc86a1ed394aaed40139011938905da22d52d56cf30a&req=dycvEst3moJdFb4f3HP0gEzN7cPka2K%2BLZYs3j9CWJ43KVbVSFOMNRXTExz4%0AUL8%3D%0A)](https://downloads.intercomcdn.com/i/o/378429732/f483a3f372a7a69e36056f02/image.png?expires=1781168400&signature=82af8d1293daea410723bc86a1ed394aaed40139011938905da22d52d56cf30a&req=dycvEst3moJdFb4f3HP0gEzN7cPka2K%2BLZYs3j9CWJ43KVbVSFOMNRXTExz4%0AUL8%3D%0A)
2. On the "**Extension Length"** tab, specify your extension length by choosing how many digits your extension should have (default is 3). Note that this CANNOT be changed later.  
   ​

   ### Extension Length Tab:

   [![Extension length tab](https://downloads.intercomcdn.com/i/o/141990708/49752d67a65b3045470583e5/3cx2.png?expires=1781168400&signature=426238184c54d6270380fa963c3d0a0f1b7379a30bc2e2170938ed75cb4d612a&req=dSQmH8B%2BmoFXFb4f3HP0gNE0iJn4%2Bkd4VtbKAv11lasJHGe6P4tB5y0Im7K4%0A2vY%3D%0A)](https://downloads.intercomcdn.com/i/o/141990708/49752d67a65b3045470583e5/3cx2.png?expires=1781168400&signature=426238184c54d6270380fa963c3d0a0f1b7379a30bc2e2170938ed75cb4d612a&req=dSQmH8B%2BmoFXFb4f3HP0gNE0iJn4%2Bkd4VtbKAv11lasJHGe6P4tB5y0Im7K4%0A2vY%3D%0A)
3. Click "**Next"**.
4. On the "**Admin Email"** tab and enter an email you want to use to receive system notifications and other important information.  
   ​

   ### Admin Email Tab:

   [![admin email tab](https://downloads.intercomcdn.com/i/o/141990778/4a4dd0a4962f9c121760d795/3cx3.png?expires=1781168400&signature=7297a62927f5bf5f3878567ee970aa79d576bb7c14b3953436b05c0ad7b0225b&req=dSQmH8B%2BmoZXFb4f3HP0gLKmSKg9PU7B42TkD1yv2cXhYOg7prKJCvj4%2BIjH%0Ag4M%3D%0A)](https://downloads.intercomcdn.com/i/o/141990778/4a4dd0a4962f9c121760d795/3cx3.png?expires=1781168400&signature=7297a62927f5bf5f3878567ee970aa79d576bb7c14b3953436b05c0ad7b0225b&req=dSQmH8B%2BmoZXFb4f3HP0gLKmSKg9PU7B42TkD1yv2cXhYOg7prKJCvj4%2BIjH%0Ag4M%3D%0A)
5. Click "**Next"**.
6. On the "**Timezone"** tab, set your timezone.

   ### Timezone Tab:

   [![timezone tab](https://downloads.intercomcdn.com/i/o/141990935/25028a7816ec7a243df6834a/3cx4.png?expires=1781168400&signature=3a93b242345ac9b009150a49143158b6ddcca1f474ee5a09b9724f49d80b60d2&req=dSQmH8B%2BlIJaFb4f3HP0gMWu6k59%2FxFrRByzK78aTkd06C5D3NuNHr%2FsZxfc%0AEnw%3D%0A)](https://downloads.intercomcdn.com/i/o/141990935/25028a7816ec7a243df6834a/3cx4.png?expires=1781168400&signature=3a93b242345ac9b009150a49143158b6ddcca1f474ee5a09b9724f49d80b60d2&req=dSQmH8B%2BlIJaFb4f3HP0gMWu6k59%2FxFrRByzK78aTkd06C5D3NuNHr%2FsZxfc%0AEnw%3D%0A)
7. Click "**Next"**.
8. On the Operator tab, you can specify a default operator extension. This will be the default destination for all inbound calls, as well as a voicemail extension.

   ### Operator Tab:

   [![operator tab](https://downloads.intercomcdn.com/i/o/141991003/30514193ed5a05710fd53d62/3cx5.png?expires=1781168400&signature=dd45fcf2a3d81a4da6063d4c506238d1b9c76c17ed3eb6467a67638716abd26c&req=dSQmH8B%2FnYFcFb4f3HP0gJJDDipF2Fjqea1%2Bay8C5xZVVYXqlvI75zq%2FNBLY%0Azvc%3D%0A)](https://downloads.intercomcdn.com/i/o/141991003/30514193ed5a05710fd53d62/3cx5.png?expires=1781168400&signature=dd45fcf2a3d81a4da6063d4c506238d1b9c76c17ed3eb6467a67638716abd26c&req=dSQmH8B%2FnYFcFb4f3HP0gJJDDipF2Fjqea1%2Bay8C5xZVVYXqlvI75zq%2FNBLY%0Azvc%3D%0A)
9. Click "**Next"**.
10. On the "**Allowed Countries"** tab, you can select all regions permitted for outgoing call.

    [![Allowed countries setup](https://downloads.intercomcdn.com/i/o/141991087/cd58e4713a31edcf6508a538/3cx6.png?expires=1781168400&signature=773c3f70234281e22d6c3e6177b31f15c38ec7d06d5863a24c9129c9f2e7c70c&req=dSQmH8B%2FnYlYFb4f3HP0gPtol67TsuWtpb1Ia4IqntTLWIB6AE6AcwrWnVZ0%0AdKE%3D%0A)](https://downloads.intercomcdn.com/i/o/141991087/cd58e4713a31edcf6508a538/3cx6.png?expires=1781168400&signature=773c3f70234281e22d6c3e6177b31f15c38ec7d06d5863a24c9129c9f2e7c70c&req=dSQmH8B%2FnYlYFb4f3HP0gPtol67TsuWtpb1Ia4IqntTLWIB6AE6AcwrWnVZ0%0AdKE%3D%0A)
11. Click "**Next"**.
12. On the "**Prompt set"** tab, you can select the language spoken by your automated prompts.

    [![Prompt set selection](https://downloads.intercomcdn.com/i/o/141991184/e0db5acf4976225432cf38c3/3cx7.png?expires=1781168400&signature=7ba763388b09de9ef406e1031fc2d5a82ea48e4669794cdf3884ef7533c0cbf5&req=dSQmH8B%2FnIlbFb4f3HP0gDG35rQQZzgseiNHOCdmQMtb%2F6TvCN7jBioJxYvX%0AIZ0%3D%0A)](https://downloads.intercomcdn.com/i/o/141991184/e0db5acf4976225432cf38c3/3cx7.png?expires=1781168400&signature=7ba763388b09de9ef406e1031fc2d5a82ea48e4669794cdf3884ef7533c0cbf5&req=dSQmH8B%2FnIlbFb4f3HP0gDG35rQQZzgseiNHOCdmQMtb%2F6TvCN7jBioJxYvX%0AIZ0%3D%0A)
13. Click "**Next"**.
14. On the "**Registration"** tab, enter your personal detail to register your setup.

[Back to Top](#h_87213f8535)

## 2. Configure your PBX

In this step, you'll configure everything needed to start making and receiving calls with 3CX through Telnyx, including network settings, SIP trunks, inbound/outbound routes etc.

## 2.1. Confirm your network settings

1. Click on the **Ports** tab and ensure your SIP port is set to 5060.
2. Click on the **Public IP** tab and ensure that your Public IP is correct and that you have selected the proper Network card Interface.
3. Click on the **Settings** tab and click on **Network Settings** and then on the Public IP tab. Find the **External IP Configuration** section and ensure that the connection IP on the portal matches the Static Public IP.

## 2.2. Create a Telnyx SIP Trunk

1. Click on "**SIP Trunks"** in the left-hand navigation menu.
2. Click "**Import Provider"** near the top of the screen.
3. A new pop up will open. Enter/select the following:

   1. Upload the **telnyx.pv.xml** file attachment at the end of this article.

      1. Try your browser in incognito mode or clear cache/cookies if you can't access the file otherwise, please try another browser.
      2. Our support team can also help provide the file if you can't access it.
      3. This will pre-populate the trunk settings.
   2. Enter the main trunk number.

      [![Creating the SIP trunk](https://downloads.intercomcdn.com/i/o/501212759/aa790f5a95b145adaa184490/Screenshot+from+2022-04-22+10-05-33.png?expires=1781168400&signature=327b40b63fe31cfef7083a15415d5c400a0b4b79de563eb6156e804b8d509ade&req=cSAmFMh8moRWFb4f3HP0gFs36383Y%2B873IwAPeyPmRAF0PMQKxU%2FgoTlSvlj%0AOak%3D%0A)](https://downloads.intercomcdn.com/i/o/501212759/aa790f5a95b145adaa184490/Screenshot+from+2022-04-22+10-05-33.png?expires=1781168400&signature=327b40b63fe31cfef7083a15415d5c400a0b4b79de563eb6156e804b8d509ade&req=cSAmFMh8moRWFb4f3HP0gFs36383Y%2B873IwAPeyPmRAF0PMQKxU%2FgoTlSvlj%0AOak%3D%0A)
4. Click "**OK"**. This will open the trunk configuration window.
5. Click on the the "**General"** tab and find "**Trunk Details":**

   1. **Enter name of Trunk:** *Telnyx LLC*
   2. **Registrar/Server/Gateway Hostname or IP:** *sip-anycast1.telnyx.com:5060 or sip.telnyx.com:5060*
   3. **Outbound Proxy:** *<leave blank unless you are using a proxy to send calls to first>*
   4. **Number of SIM Calls:** <set your preferred amount of simultaneous calls>
   5. [![Number of SIM calls](https://downloads.intercomcdn.com/i/o/698656911/cbe047caab7d593b05543759/Screenshot+from+2023-03-25+10-45-52.png?expires=1781168400&signature=133578250494a6abb7f9cf610df2ed1353c49b4f21c0ba2fadde31483023ab95&req=cikvEMx4lIBeFb4f3HP0gETwbjvAxecQQbCS75yXg0zjtHHxf0U0lxhrV6CK%0AcU8%3D%0A)](https://downloads.intercomcdn.com/i/o/698656911/cbe047caab7d593b05543759/Screenshot+from+2023-03-25+10-45-52.png?expires=1781168400&signature=133578250494a6abb7f9cf610df2ed1353c49b4f21c0ba2fadde31483023ab95&req=cikvEMx4lIBeFb4f3HP0gETwbjvAxecQQbCS75yXg0zjtHHxf0U0lxhrV6CK%0AcU8%3D%0A)
6. ### **Authentication** section:

   1. **Type of Authentication:** Register/Account based

      1. **Authentication ID:** <You need to use the username from the connection which you have created in the Telnyx portal>
      2. **Authentication Password:** <You need to use password from the connection which you have created in the Telnyx portal>
      3. **3 Way Authentication:** Do not enable

         [![Authentication section](https://downloads.intercomcdn.com/i/o/37739545/266e21680c7755f64d1f0a59/File1509107718169?expires=1781168400&signature=d67be9450a72f43927662bf172ed32a522159786c4ff0022a9521fd014b1261a&req=dycgFcB7mYQTWLcX3D%2B5hgJVsXrbJGf9bT5jLQ%2FZALf42osH31gkzjrLLWke%0Agw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/37739545/266e21680c7755f64d1f0a59/File1509107718169?expires=1781168400&signature=d67be9450a72f43927662bf172ed32a522159786c4ff0022a9521fd014b1261a&req=dycgFcB7mYQTWLcX3D%2B5hgJVsXrbJGf9bT5jLQ%2FZALf42osH31gkzjrLLWke%0Agw%3D%3D%0A)
   2. **Type of Authentication:** Do not require - IP based

      1. Select this option if you would prefer to send and receive calls from the public IP address of your 3CX instance.
      2. **Authentication ID:** Leave empty
      3. **Authentication Password:** Leave empty
      4. **3 Way Authentication:** Do no enable  
         ​
7. Find the "**Route calls to"** section.

   1. **Main Trunk number :**<By default number will be shown. You need cross verify with the number which you have purchased on telnyx portal>
   2. **Destination for calls during the office hours :** <Based on your requirement>
   3. **Destination for calls outside the office hours :** <Based on your requirement>

      [![Routing calls example](https://downloads.intercomcdn.com/i/o/37739546/c3223abe1f08d0257ad372cb/File1509107718207?expires=1781168400&signature=4b1c5a7a3a28530c7150a700197c9574387d6ad3b7a6595e956227ec91ab2fa8&req=dycgFcB7mYcTWLcX3D%2B5hjGV3F3SDMaAWEaesZJfZ3sKbd8bBopCuUB%2Bu2xS%0AQg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/37739546/c3223abe1f08d0257ad372cb/File1509107718207?expires=1781168400&signature=4b1c5a7a3a28530c7150a700197c9574387d6ad3b7a6595e956227ec91ab2fa8&req=dycgFcB7mYcTWLcX3D%2B5hjGV3F3SDMaAWEaesZJfZ3sKbd8bBopCuUB%2Bu2xS%0AQg%3D%3D%0A)
8. For the other "**sub tabs"** available, these will have been pre-populated with general settings that Telnyx recommends from the xml file uploaded.

   1. Click **OK** when you are happy with the trunk settings.
9. Lastly, this provider trunk pre-populates information in the "**SMS sub tab"**.

   1. **API Key**: Visit <https://portal.telnyx.com/#/api-keys> to generate a key and paste into the field.
   2. **Provider URL**: <https://api.telnyx.com/v2/messages>
   3. **Copy webhook URL**: Visit <https://portal.telnyx.com/#/programmable-messaging/profiles> and make sure to copy and paste this URL into your messaging profile that you've created to allow for inbound and outbound messaging.
   4. [![Copying webhook URL](https://downloads.intercomcdn.com/i/o/698660949/224f137d1a948d51adc34409/Screenshot+from+2023-03-25+10-53-49.png?expires=1781168400&signature=7314f56c5492a71f3fee30c35fd0caf26b4e139d76684883d063d77b18837714&req=cikvEM9%2BlIVWFb4f3HP0gBd34RXsHOc1dns4iBjSbGBu7LO9Ho%2F4kqG6kiWu%0AQ3c%3D%0A)](https://downloads.intercomcdn.com/i/o/698660949/224f137d1a948d51adc34409/Screenshot+from+2023-03-25+10-53-49.png?expires=1781168400&signature=7314f56c5492a71f3fee30c35fd0caf26b4e139d76684883d063d77b18837714&req=cikvEM9%2BlIVWFb4f3HP0gBd34RXsHOc1dns4iBjSbGBu7LO9Ho%2F4kqG6kiWu%0AQ3c%3D%0A)
   5. Click **OK** when you are happy with the trunk settings.  
      ​
10. Your Telnyx trunk is now live!

[![Confirmation SIP trunk is live](https://downloads.intercomcdn.com/i/o/37739547/f13058c7b96adaacca2b1e57/File1509107718250?expires=1781168400&signature=0d9c2e82d86e4e7ab245ec1e87da1243e2d2b0bd31a0156156e5a405ff1fd498&req=dycgFcB7mYYTWLcX3D%2B5hlCEe%2BEgwgFq8PuUPOm95hCwyREbQONsiC435eN%2B%0AXDoRmkHj8SE84d3Z%0A)](https://downloads.intercomcdn.com/i/o/37739547/f13058c7b96adaacca2b1e57/File1509107718250?expires=1781168400&signature=0d9c2e82d86e4e7ab245ec1e87da1243e2d2b0bd31a0156156e5a405ff1fd498&req=dycgFcB7mYYTWLcX3D%2B5hlCEe%2BEgwgFq8PuUPOm95hCwyREbQONsiC435eN%2B%0AXDoRmkHj8SE84d3Z%0A)

## 2.3. Configure inbound rule

1. Click on "**Inbound Rules**" from the navigation menu on the left.
2. Click on "**+Add DID Rule**" near the top of the screen.
3. Find the **General** section and ensure the following:

   1. **Name:** *IB\_Telnyx* (or any name that can identify your inbound rule)

      [![Configuring inbound rule](https://downloads.intercomcdn.com/i/o/378446756/1546aec92d08e8e92c076bab/image.png?expires=1781168400&signature=a709de67950a4f2adeb42020773fa2afce56bc6e2d1a9f6d306e5d9563fcbede&req=dycvEs14moRZFb4f3HP0gCv%2B2pmLnz6%2F4qWNWn670UKpTsQHk4ixMynnHlxE%0AhIw%3D%0A)](https://downloads.intercomcdn.com/i/o/378446756/1546aec92d08e8e92c076bab/image.png?expires=1781168400&signature=a709de67950a4f2adeb42020773fa2afce56bc6e2d1a9f6d306e5d9563fcbede&req=dycvEs14moRZFb4f3HP0gCv%2B2pmLnz6%2F4qWNWn670UKpTsQHk4ixMynnHlxE%0AhIw%3D%0A)
4. Find the **Route calls to** section and ensure that:

   1. **Destination for calls during office hours:** *Extension* and ensure that your desired extension is selected (is usually *000*).

      [![Routing calls view](https://downloads.intercomcdn.com/i/o/378447263/1f0af0a485209ed733228246/image.png?expires=1781168400&signature=e3cc60a4a1b229c64d7f2a9b7727ae20522e1c0a87d44008935c569ad83b26f0&req=dycvEs15n4dcFb4f3HP0gF593ocgV6GwiKdpjOUvQyiiZawKoUwl4cMThLeM%0AsWA%3D%0A)](https://downloads.intercomcdn.com/i/o/378447263/1f0af0a485209ed733228246/image.png?expires=1781168400&signature=e3cc60a4a1b229c64d7f2a9b7727ae20522e1c0a87d44008935c569ad83b26f0&req=dycvEs15n4dcFb4f3HP0gF593ocgV6GwiKdpjOUvQyiiZawKoUwl4cMThLeM%0AsWA%3D%0A)

## 2.4. Configure outbound rule

1. Click on **Outbound Rules** from the navigation menu on the left.
2. Click on **+Add** near the top of the screen.
3. Find the **General** section and ensure the following:

   1. **Name:** *OB\_Telnyx* (or any name that can identify your outbound rule)

      [![Configure outbound rule](https://downloads.intercomcdn.com/i/o/37739550/140544231b9f3347b9215c22/File1509107718366?expires=1781168400&signature=b2e85c6780bbcdc729e7263a63026fd697182c9ea9b969280d7c133ab528ed61&req=dycgFcB7mIETWLcX3D%2B5htRwoGhEFPzhz0qExrpW6QapkFM2PVY4zhyAAgle%0ADQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/37739550/140544231b9f3347b9215c22/File1509107718366?expires=1781168400&signature=b2e85c6780bbcdc729e7263a63026fd697182c9ea9b969280d7c133ab528ed61&req=dycgFcB7mIETWLcX3D%2B5htRwoGhEFPzhz0qExrpW6QapkFM2PVY4zhyAAgle%0ADQ%3D%3D%0A)
4. Find the **Apply this rule to these calls** section and fill in the following:

   1. **Calls to numbers starting with prefix :** <leave empty>
   2. **Calls from extension(s) :** <You need to give the extension numbers>

      1. **NOTE**: ‘000’ is the extension I have used as an example.
   3. **Calls to Numbers with a length of :** <leave empty>

      [![Applying rules to calls](https://downloads.intercomcdn.com/i/o/37739551/2db181344b002a5942bee926/File1509107718409?expires=1781168400&signature=e5ad0e9205c96dc61ff8d45e742be44a1a5fbdca7f2ea3f017532f8abe94e1e1&req=dycgFcB7mIATWLcX3D%2B5homCSpS5YqRdVizzxfQ3Ugb6r0zhODZExWHb2wr5%0AZg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/37739551/2db181344b002a5942bee926/File1509107718409?expires=1781168400&signature=e5ad0e9205c96dc61ff8d45e742be44a1a5fbdca7f2ea3f017532f8abe94e1e1&req=dycgFcB7mIATWLcX3D%2B5homCSpS5YqRdVizzxfQ3Ugb6r0zhODZExWHb2wr5%0AZg%3D%3D%0A)
5. Find the **Make outbound calls on** section. This is where you will configure your routes. You can configure up to 3 routes for calls. The second and third route will be used as backup. For each route, digits can be stripped or added. Strip Digits 0 on Route 1 and Strip Digits 1 digit for remaining 2 routes.  
   ​  
   This is also one of the many ways an **outbound caller ID** can be applied within 3CX. If you choose to apply an outbound caller ID on your Outbound Route, it will be applied to all calls that proceed through this route.

   [![Outbound call routing](https://downloads.intercomcdn.com/i/o/378450256/345f7179936f71054d8feedd/image.png?expires=1781168400&signature=18da0df599fe8544536fc588154f44062ed921308517882844a719cace2e8b0a&req=dycvEsx%2Bn4RZFb4f3HP0gGskhu63MD3ua5PaiLfdwKbZLx476slv8y%2FMd715%0At4I%3D%0A)](https://downloads.intercomcdn.com/i/o/378450256/345f7179936f71054d8feedd/image.png?expires=1781168400&signature=18da0df599fe8544536fc588154f44062ed921308517882844a719cace2e8b0a&req=dycvEsx%2Bn4RZFb4f3HP0gGskhu63MD3ua5PaiLfdwKbZLx476slv8y%2FMd715%0At4I%3D%0A)

|  |
| --- |
| ***Note:*** *If you choose not to add an outbound caller ID on your outbound route, you can instead apply it for each user or extension.*    *If a caller ID is not set through 3CX, it is likely that the calls will reach us without a caller ID. If this is the case, you may choose to apply a Caller ID Override from your SIP Connection’s outbound options in the Telnyx Portal. Otherwise, your calls will be rejected. Please review our [caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy) for accepted formats.* |

[![User information section](https://downloads.intercomcdn.com/i/o/378451501/790e457be88f2fb58542cd64/image.png?expires=1781168400&signature=0601f26ca17d21858ec0c1b33fc90840620904cd3cccc9b1993d01e475d3bc45&req=dycvEsx%2FmIFeFb4f3HP0gEmDDqW8NfOG5f%2FQPu037VqtIzmJS6yFkJnTK5I3%0AXSPHQclmQJbXe1wjXQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/378451501/790e457be88f2fb58542cd64/image.png?expires=1781168400&signature=0601f26ca17d21858ec0c1b33fc90840620904cd3cccc9b1993d01e475d3bc45&req=dycvEsx%2FmIFeFb4f3HP0gEmDDqW8NfOG5f%2FQPu037VqtIzmJS6yFkJnTK5I3%0AXSPHQclmQJbXe1wjXQ%3D%3D%0A)

Depending on your use case, you may have specific dialling format rules and 3CX provides a great overview [here](https://www.3cx.com/blog/voip-howto/outbound-rules-a-complete-example/).

After completing this configuration, click "**OK**".

## **An important example of an outbound rule**

The outbound rule feature in 3cx is a powerful tool for configuring your 3CX phone system that extra mile allowing you to create much more complex rules – allowing you to not only select backup routes which come into effect when other routes fail, but also to select a different set of routes, depending on the type of number being dialed. Below you will find an example outbound rule for handling 911 Emergency Calls:

[![General outbound rule example](https://downloads.intercomcdn.com/i/o/378533625/d09fbf5d66fefc022e2a7419/image.png?expires=1781168400&signature=bffe002d7d5cf68c1a05a8cc809959bee37d51dd9e21467b9bebc8a574e3209d&req=dycvE8p9m4NaFb4f3HP0gKZQMgqbZYZ3W66uqEjXOb%2FSBKtVO2pJwfOGsouT%0ACsZzV2x%2FiaEVWm2h3A%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/378533625/d09fbf5d66fefc022e2a7419/image.png?expires=1781168400&signature=bffe002d7d5cf68c1a05a8cc809959bee37d51dd9e21467b9bebc8a574e3209d&req=dycvE8p9m4NaFb4f3HP0gKZQMgqbZYZ3W66uqEjXOb%2FSBKtVO2pJwfOGsouT%0ACsZzV2x%2FiaEVWm2h3A%3D%3D%0A)

[![Applying rules to calls](https://downloads.intercomcdn.com/i/o/378533851/0319af0f26658946d1e3b422/image.png?expires=1781168400&signature=a1cd1ec8f5b93c9df6edb31a8f7b79cb810990e0807fc6c7061a7485afb609d0&req=dycvE8p9lYReFb4f3HP0gM8iS%2F5A88ZJFgwOv%2BR%2Be%2BCxzN5lFkt62sjxKslT%0AH955QOMLL%2FpHhxIe1g%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/378533851/0319af0f26658946d1e3b422/image.png?expires=1781168400&signature=a1cd1ec8f5b93c9df6edb31a8f7b79cb810990e0807fc6c7061a7485afb609d0&req=dycvE8p9lYReFb4f3HP0gM8iS%2F5A88ZJFgwOv%2BR%2Be%2BCxzN5lFkt62sjxKslT%0AH955QOMLL%2FpHhxIe1g%3D%3D%0A)

[![Making outbound calls on specific routes](https://downloads.intercomcdn.com/i/o/378534062/8594b1b8388727092bf58a52/image.png?expires=1781168400&signature=9c256659766c2d69ea86048e5adb68f393f5df32572ad7840a1b66ee87f1c5d4&req=dycvE8p6nYddFb4f3HP0gOPdu1JyM9p9aCIFngp5KPGOT3JQGBrAZmdCbm2C%0A4LHFaQDVn2zxJDz5dQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/378534062/8594b1b8388727092bf58a52/image.png?expires=1781168400&signature=9c256659766c2d69ea86048e5adb68f393f5df32572ad7840a1b66ee87f1c5d4&req=dycvE8p6nYddFb4f3HP0gOPdu1JyM9p9aCIFngp5KPGOT3JQGBrAZmdCbm2C%0A4LHFaQDVn2zxJDz5dQ%3D%3D%0A)

For additional outbound rule examples which you may find useful please see the following [support article](https://www.3cx.com/blog/voip-howto/outbound-rules-a-complete-example/) from 3CX.

That's it, you've now completed the configuration of 3CX V18 PBX Credential Trunk and can now make and receive calls by using Telnyx as your SIP provider!

## 2.5. Configure extension for inbound and outbound messaging.

1. An existing extension/user will have been created during the initial setup.

   1. Visit the "users" section where you can add more extensions or edit existing extensions.
   2. In our example below, we're going to click into extension 101 so we can enable messaging on the extension which is associated with one of the numbers we configured in our inbound routes.
   3. [![Configuring extensions](https://downloads.intercomcdn.com/i/o/585692576/c8790e467d21886707d22103/Screenshot+from+2022-09-23+17-53-12.png?expires=1781168400&signature=9e3549a73c6dbfe1805115d519e9bfc9df6dded7fce7238502d2a5fd8c0c51b2&req=cSgiEMB8mIZZFb4f3HP0gPhuOZ1ekIZf%2FSZttdyM1FPJ6vQ7f%2FHffReXqCvn%0Acsk%3D%0A)](https://downloads.intercomcdn.com/i/o/585692576/c8790e467d21886707d22103/Screenshot+from+2022-09-23+17-53-12.png?expires=1781168400&signature=9e3549a73c6dbfe1805115d519e9bfc9df6dded7fce7238502d2a5fd8c0c51b2&req=cSgiEMB8mIZZFb4f3HP0gPhuOZ1ekIZf%2FSZttdyM1FPJ6vQ7f%2FHffReXqCvn%0Acsk%3D%0A)
   4. You will be brought to the "**General**" tab.

      1. Visit the end of the page and make sure to assign the DID to the extension. **Previously in V18 Update 5 you would have to enable SMS on the associated DID but this is no longer a requirement.**

         [![Web authentication and DIDs](https://downloads.intercomcdn.com/i/o/667509597/ce6276240a8ac47d058d0088/Screenshot+from+2022-09-23+17-54-24.png?expires=1781168400&signature=f254473eedc0862a288b3de74ae8031ce0d1d78f65ab209adf929d878d298f4b&req=ciYgE8l3mIhYFb4f3HP0gP3vE8VLOnUA6BGJGIqz8yl1mSWceC8BvSz1TpTi%0A%2BYM%3D%0A)](https://downloads.intercomcdn.com/i/o/667509597/ce6276240a8ac47d058d0088/Screenshot+from+2022-09-23+17-54-24.png?expires=1781168400&signature=f254473eedc0862a288b3de74ae8031ce0d1d78f65ab209adf929d878d298f4b&req=ciYgE8l3mIhYFb4f3HP0gP3vE8VLOnUA6BGJGIqz8yl1mSWceC8BvSz1TpTi%0A%2BYM%3D%0A)
      2. Click **OK** at the top of the page which will make inbound and messaging live for the extension.

## 2.6. Access 3CX Native WebClient to send and receive messages.

1. During the extension creation process at the initial setup, you would have received an email from 3CX "**Your User Account on your New 3CX System"** with a link to their webclient along with the extensions username and password.
2. Visit the link and login.

   1. This is an app you can use on the web for making and receiving calls/sms for each given extension that is created.
3. Once logged in visit the contacts section.

   1. Click “+” icon to add a contact.
   2. Enter in the name and mobile number of the contact.
   3. Click the “save” icon on the top right.
   4. [![Native 3CX client](https://downloads.intercomcdn.com/i/o/585697006/350bea57e797c2dec1434393/74044290-bb62-4ca7-b8ee-04da707b9a38.png?expires=1781168400&signature=a4f39fd451eb6f5783cd5b287934291da2af9a6d8f0782b3144eff134ba45320&req=cSgiEMB5nYFZFb4f3HP0gHh1dZ11ndIuF0G9PP%2FRrjzToz6L2guAh8si%2BUIO%0AogQ%3D%0A)](https://downloads.intercomcdn.com/i/o/585697006/350bea57e797c2dec1434393/74044290-bb62-4ca7-b8ee-04da707b9a38.png?expires=1781168400&signature=a4f39fd451eb6f5783cd5b287934291da2af9a6d8f0782b3144eff134ba45320&req=cSgiEMB5nYFZFb4f3HP0gHh1dZ11ndIuF0G9PP%2FRrjzToz6L2guAh8si%2BUIO%0AogQ%3D%0A)
   5. Once the contacts are saved, you can now use them in the chat section.
4. Visit the chat section

   1. Click “+” symbol
   2. and then “Send SMS”
   3. [![Sending SMS](https://downloads.intercomcdn.com/i/o/585698164/a8167c92c81dd310c6dccd93/075d2f79-e99a-4dce-8775-10f3f27a7827.png?expires=1781168400&signature=d875502cdc990a33015f434b8ee89bceecdef1cac8e4df864bfbaac4c571829a&req=cSgiEMB2nIdbFb4f3HP0gPp0qZ8PfEQt7GZzysLbdcrv6e%2FAtXqUOzuVTM3H%0AQr4%3D%0A)](https://downloads.intercomcdn.com/i/o/585698164/a8167c92c81dd310c6dccd93/075d2f79-e99a-4dce-8775-10f3f27a7827.png?expires=1781168400&signature=d875502cdc990a33015f434b8ee89bceecdef1cac8e4df864bfbaac4c571829a&req=cSgiEMB2nIdbFb4f3HP0gPp0qZ8PfEQt7GZzysLbdcrv6e%2FAtXqUOzuVTM3H%0AQr4%3D%0A)
   4. choose the contact you want to send an SMS to.
   5. [![Choosing a contact](https://downloads.intercomcdn.com/i/o/585698391/580c98fb03a6edf0b7376bbf/6824ebb7-1382-4a8e-a93a-3fc1f79ee2c8.png?expires=1781168400&signature=e47dedb1e3ef1af9fbb3ed9c9ea5c1891afb0846062c86c281b3f9df45a01695&req=cSgiEMB2noheFb4f3HP0gLMGsoYTggqJ7CnrM579VPd70nGkdSL%2F2JNIFeHp%0AXVs%3D%0A)](https://downloads.intercomcdn.com/i/o/585698391/580c98fb03a6edf0b7376bbf/6824ebb7-1382-4a8e-a93a-3fc1f79ee2c8.png?expires=1781168400&signature=e47dedb1e3ef1af9fbb3ed9c9ea5c1891afb0846062c86c281b3f9df45a01695&req=cSgiEMB2noheFb4f3HP0gLMGsoYTggqJ7CnrM579VPd70nGkdSL%2F2JNIFeHp%0AXVs%3D%0A)
   6. type your message and hit enter to send.
   7. The message will send to the destination.
   8. Once the destination responds, you’ll see it in the chat.
   9. [![Receiving a response](https://downloads.intercomcdn.com/i/o/585699343/df0e249265f8268ea3168f7f/a9dec25c-d6e2-4b81-aaba-565e96060e6e.png?expires=1781168400&signature=d94a3342c022361f9da9ba61da797c5080c1575d0095144dc538d49c7c7d9e1e&req=cSgiEMB3noVcFb4f3HP0gFiDKJwp50ZgML3ZCSPUNh8K8%2BMyv1RBt38dY4UC%0A6d4%3D%0A)](https://downloads.intercomcdn.com/i/o/585699343/df0e249265f8268ea3168f7f/a9dec25c-d6e2-4b81-aaba-565e96060e6e.png?expires=1781168400&signature=d94a3342c022361f9da9ba61da797c5080c1575d0095144dc538d49c7c7d9e1e&req=cSgiEMB3noVcFb4f3HP0gFiDKJwp50ZgML3ZCSPUNh8K8%2BMyv1RBt38dY4UC%0A6d4%3D%0A)

That's it, you've now completed the configuration of 3CX V18 PBX and can now make and receive calls & messages by using Telnyx as your SIP provider!

[Back to Top](#h_87213f8535)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, you can check out:

* 3CX's [help section](https://www.3cx.com/support/) for extra support!
* Latest information on [3CX V18 Updates](https://www.3cx.com/blog/releases/).

[telnyx.pv.xml](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/997239819/230a8f6b1b503d635675fed1/telnyx_pv.xml?expires=1781168400&signature=72f1ed028d5b8aa91fb14c849f822027dbe30841752f3ea216316b743ff20eb3&req=fSkgFMp3lYBWFb4f3HP0gJNSzR3AxXSEHaYGLCbAoF4Rzgj3Tt%2FvrCmQ%2Bhpb%0A%2F%2B9KXZLulA%3D%3D%0A)

---

Related Articles

[Configuring an Elastix 4 PBX IP Trunk](https://support.telnyx.com/en/articles/1130622-configuring-an-elastix-4-pbx-ip-trunk)[How to configure a Thirdlane PBX](https://support.telnyx.com/en/articles/1130631-how-to-configure-a-thirdlane-pbx)[Configuring an Elastix 4 PBX Trunk](https://support.telnyx.com/en/articles/1130654-configuring-an-elastix-4-pbx-trunk)[Xorcom PBX: SIP Trunk](https://support.telnyx.com/en/articles/5754127-xorcom-pbx-sip-trunk)[3CX: Configuring a 3CX V20 PBX 20.0 Update 5 (Build 20.0.5.551) (March 2025 Update)](https://support.telnyx.com/en/articles/8683996-3cx-configuring-a-3cx-v20-pbx-20-0-update-5-build-20-0-5-551-march-2025-update)

Did this answer your question?

😞😐😃

Table of contents
