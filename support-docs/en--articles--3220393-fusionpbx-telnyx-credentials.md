---
source_url: https://support.telnyx.com/en/articles/3220393-fusionpbx-telnyx-credentials
scraped: 2026-06-11
---

FusionPBX: Telnyx Credentials | Telnyx Help Center

[Skip to main content](#main-content)

# FusionPBX: Telnyx Credentials

Configure FusionPBX 4.4 Trunk credentials with Telnyx - It's fast and easy.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_cf4a5ee2e4)

[FusionPBX](https://www.fusionpbx.com/) can be used as a highly available single or domain based multi-tenant PBX, carrier grade switch, call center server, fax server, voip server, voicemail server, conference server, voice application server, appliance framework and more. FreeSWITCH™ is a highly scalable, multi-threaded, multi-platform communication platform. This article guides you on how to configure this PBX for making and receiving calls over the internet through a next generation carrier like Telnyx!

Additional resources:

* [FusionPBX documentation](https://docs.fusionpbx.com/en/latest/)
* [Quick install guide](https://docs.fusionpbx.com/en/latest/getting_started/quick_install.html)
* [Install scripts](https://www.fusionpbx.com/download.php)
* [FusionPBX support](https://www.fusionpbx.com/support)

---

# Instructions for configuring a credentials trunk between FusionPBX and Telnyx

In this activity you will:

1. (OPTIONAL BUT RECOMMENDED) [Install a virtual machine](#h_aa5ccbd9b1)
2. [Install FusionPBX](#install-fusionpbx)
3. [Configure a FusionPBX trunk](#h_9f440cf44c)
4. [Create your extensions](#h_183746c581)
5. [Configure inbound routing](#h_ab0b9ab2d7)
6. [Configure outbound routing](#h_9cefe9bc2a)
7. [Register your extension with a device](#h_eaf6abb3b5)

**Pre-requisites:**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)

  + This includes creating a [credentials-based connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal account, assigned this connection to a DID and outbound profile in order to make and receive calls
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
* [Download](https://www.fusionpbx.com/download) and [install](https://docs.fusionpbx.com/en/latest/getting_started/quick_install.html) FusionPBX
* (RECOMMENDED) We recommend using Debian as the operating system version that should be running FusionPBX. The current Debian version that we tested FusionPBX on was Debian-9.9.  
  ​   
  There are many applications that can be used to set up a Debian Operating System on your computer. In this article we use a program called [VirtualBOX VM](https://www.virtualbox.org/) to set up a Debian Virtual Machine. You can follow [these steps](#h_aa5ccbd9b1) to do so. If you don't want to use a Virtual Machine you can skip these steps and [go straight installation of the FusionPBX.](#install-fusionpbx)

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

Install FusionPBX (From FusionPBX)  
​

|  |
| --- |
| ***Note:*** *Video walkthrough for FusionPBX/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. (OPTIONAL BUT RECOMMENDED) Install a virtual machine

You only need to complete this section if you plan to run your FusionPBX on a virtual machine. If you don't, you can skip to [section 2](#install-fusionpbx).

1. ### **Download and install the [Debian network installer disk image](https://www.debian.org/) and run it.**
2. ### **Click on the New icon in the VirtualBox menu bar.**
3. ### **This will start the New Virtual Machine Wizard. The first screen is just a welcome screen so click Continue to proceed.**
4. ### **On the Name and operating system screen, provide the following:**

   1. **Name:** You can give this any name you like
   2. **Operating System:** *Linux*
   3. **Version:** *Debian (64 bit)*

      [![Running Debian network installer disk image. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141609955/c6e3a68edc9b22ae9cb8bc50/s-n5anVQeLf0SjOvMJjD5eEOPKwDM4zr_8JSZELoxZZk0q1SqQ88fvteLlkHrxGz2wWEolgibQEVefde9c5n9vPAKjl1faHdivPlGGujX9sQHlFT4OWojS8gV3X6moWbjPxPnGvF?expires=1781168400&signature=45ccc844658bd39878156392ecb126a1295d5b6a74eba66a96391f089db0db3a&req=dSQmEMl3lIRaFb4f3HP0gNdTtTSopNgItL6Ld849FPfVK%2BFVuLL0m2R9smvA%0AflY%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141609955/c6e3a68edc9b22ae9cb8bc50/s-n5anVQeLf0SjOvMJjD5eEOPKwDM4zr_8JSZELoxZZk0q1SqQ88fvteLlkHrxGz2wWEolgibQEVefde9c5n9vPAKjl1faHdivPlGGujX9sQHlFT4OWojS8gV3X6moWbjPxPnGvF?expires=1781168400&signature=45ccc844658bd39878156392ecb126a1295d5b6a74eba66a96391f089db0db3a&req=dSQmEMl3lIRaFb4f3HP0gNdTtTSopNgItL6Ld849FPfVK%2BFVuLL0m2R9smvA%0AflY%3D%0A)
5. ### **Click Continue.**
6. ### **On the Memory size screen, you can just use the default setting for the amount of base memory.**

   [![Memory size tab on the Debian network installer. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141609959/053a24e6569fafb2046a2afc/CY5kNsWZifnAt5F4bU9FTwW7V-FEaXO0lWQ_4f0_shpIOTdBElBpNbcKP09HjqdcS9LpsQXTFBXNf1UoaidblFB2KXLCDYq85FHdCctiqrYr7C-oR9h7SS67LV_4p-_1bLycU8q4?expires=1781168400&signature=ca46b46e206c2c4f4846551168dafb3e17972e43a3ab2a1d6f15a56e4a19fe36&req=dSQmEMl3lIRWFb4f3HP0gKMbDLWOZmvCJISEKOuEANsAomVrpwOZOrs9upuy%0AhyQ%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141609959/053a24e6569fafb2046a2afc/CY5kNsWZifnAt5F4bU9FTwW7V-FEaXO0lWQ_4f0_shpIOTdBElBpNbcKP09HjqdcS9LpsQXTFBXNf1UoaidblFB2KXLCDYq85FHdCctiqrYr7C-oR9h7SS67LV_4p-_1bLycU8q4?expires=1781168400&signature=ca46b46e206c2c4f4846551168dafb3e17972e43a3ab2a1d6f15a56e4a19fe36&req=dSQmEMl3lIRWFb4f3HP0gKMbDLWOZmvCJISEKOuEANsAomVrpwOZOrs9upuy%0AhyQ%3D%0A)
7. ### **Click Continue.**
8. ### **On the Hard disk screen, you'll create a new virtual hard disk to use as your VM file system. Select Create a virtual hard disk now.**

   [![Hard disk screen on the Debian network installer. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141609964/6c259f67d4f8c427403cc711/zJmgKRgU9yz-OERA6bPXZlSeRzv5UXPkLJPAZ5aHsaJOteMMUhorbqYW_EMpfhZS7ZPThfYH81AFdRq9dlgeUz7HaCGW7_D3Vf-TfKx45ueWxHGSqeIictmWYLMpOo-iYI_JsFWm?expires=1781168400&signature=b0f376d9b6a6b7e522990e10648e24c4a1a0afbde27a2bbced11ca24afd2507c&req=dSQmEMl3lIdbFb4f3HP0gBHzwgmrqWSSh%2FS9SQ5lIj3%2FupkI3vE0WzAZd%2FH7%0AlHA%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141609964/6c259f67d4f8c427403cc711/zJmgKRgU9yz-OERA6bPXZlSeRzv5UXPkLJPAZ5aHsaJOteMMUhorbqYW_EMpfhZS7ZPThfYH81AFdRq9dlgeUz7HaCGW7_D3Vf-TfKx45ueWxHGSqeIictmWYLMpOo-iYI_JsFWm?expires=1781168400&signature=b0f376d9b6a6b7e522990e10648e24c4a1a0afbde27a2bbced11ca24afd2507c&req=dSQmEMl3lIdbFb4f3HP0gBHzwgmrqWSSh%2FS9SQ5lIj3%2FupkI3vE0WzAZd%2FH7%0AlHA%3D%0A)
9. ### **Click "Create".**
10. ### **In the next screen, you'll specify the format for the virtual hard disk. Just use the default settings here: the native VirtualBox disk image (VDI) format.**
11. ### **Click "Continue".**
12. ### **On the "Storage on physical hard disk" screen, you'll choose how your virtual hard disk is sized. The default option is is "dynamically allocated", and this is the option we recommend.**

    [![Storage on physical hard disk screen. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141609967/f5d24034be6fd990a10fde15/ei_6tDNxK4r8yMqJDbTxLosx8kcc_dT40XL0R41cWgSr_Dxbl3Y0opppATwkWCQAg70NQK5pBUAEBxfWf2puMBEb0CrGb464Kpzc7Mo1NKoJVYibjubGga2UOMMeBnAmNReL9Xaw?expires=1781168400&signature=1c7c748e096f07342fcd32e940946ad4c8e1f44a92f7b2fe86227f60de5976ef&req=dSQmEMl3lIdYFb4f3HP0gK3QigZDG4LBFDbBl7vLClc57r0aVno6SDizXIiY%0AZo8%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141609967/f5d24034be6fd990a10fde15/ei_6tDNxK4r8yMqJDbTxLosx8kcc_dT40XL0R41cWgSr_Dxbl3Y0opppATwkWCQAg70NQK5pBUAEBxfWf2puMBEb0CrGb464Kpzc7Mo1NKoJVYibjubGga2UOMMeBnAmNReL9Xaw?expires=1781168400&signature=1c7c748e096f07342fcd32e940946ad4c8e1f44a92f7b2fe86227f60de5976ef&req=dSQmEMl3lIdYFb4f3HP0gK3QigZDG4LBFDbBl7vLClc57r0aVno6SDizXIiY%0AZo8%3D%0A)
13. ### **Finally, on the "File location and size" screen, choose the location and maximum size of your virtual machine disk. You can just use the defaults here, unless you require anything specific.**

    [![File location and size screen. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141609971/032e906f4511ba61d227e9b0/XMwIgFx3NF4XqAbFVSqnNksz-_grLQiQhnmxmxsZYo6sKB7tTorICH4ZGcH9TJ3CUsG9yH39Y4ZveQiWmTLu5B4oDjBjaJyOpUaTO5Zt8VTaH7b4Cv86x3RaRGAs1NoiVKWFdwGV?expires=1781168400&signature=8470012fadb8302493d0f16aaf8ee674fb30665a96b5f6f908564831c7ac26b9&req=dSQmEMl3lIZeFb4f3HP0gMvTkqZh1s8VzEWWucXETt%2FUlpvU61IpL%2Bpp1zJL%0AZ4U%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141609971/032e906f4511ba61d227e9b0/XMwIgFx3NF4XqAbFVSqnNksz-_grLQiQhnmxmxsZYo6sKB7tTorICH4ZGcH9TJ3CUsG9yH39Y4ZveQiWmTLu5B4oDjBjaJyOpUaTO5Zt8VTaH7b4Cv86x3RaRGAs1NoiVKWFdwGV?expires=1781168400&signature=8470012fadb8302493d0f16aaf8ee674fb30665a96b5f6f908564831c7ac26b9&req=dSQmEMl3lIZeFb4f3HP0gMvTkqZh1s8VzEWWucXETt%2FUlpvU61IpL%2Bpp1zJL%0AZ4U%3D%0A)
14. ### **Click "Create". Welcome to your virtual machine!**

    [![Virtual machine interface. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141609973/2f777145e5b6f949ad97d84f/hFYwDuZftO816XqrnicdSPQPNqTWJ5JvW67M_CMiyVF52MIedvkN44ohK2W7Uf_qSnWxpbFKCKpa3StGg-EsgvKpKB7gC3aswidIY1BO-R4y1yczu7Jupv2g5_quvLlXgKogYbwX?expires=1781168400&signature=2f01ee625ca2d026eea8e8757178312c2790716692e71d533d9a44ed19cfebfd&req=dSQmEMl3lIZcFb4f3HP0gFMW4xl0F8k53%2FFT6z9G3RXBvfICWAXIaNGjNDcw%0AriY%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141609973/2f777145e5b6f949ad97d84f/hFYwDuZftO816XqrnicdSPQPNqTWJ5JvW67M_CMiyVF52MIedvkN44ohK2W7Uf_qSnWxpbFKCKpa3StGg-EsgvKpKB7gC3aswidIY1BO-R4y1yczu7Jupv2g5_quvLlXgKogYbwX?expires=1781168400&signature=2f01ee625ca2d026eea8e8757178312c2790716692e71d533d9a44ed19cfebfd&req=dSQmEMl3lIZcFb4f3HP0gFMW4xl0F8k53%2FFT6z9G3RXBvfICWAXIaNGjNDcw%0AriY%3D%0A)
15. ### **Click on the "Settings" gear at the top left of your new VM and find the "Storage" option in the left-hand navigation.**
16. ### **Select the Debian file under the "Controller: IDE".**

    [![Settings gear on the newly launched Virtual Machine. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141609975/674bf8bafe061765995d9559/woWC9pI5yxqnqXqerkXvQRu15SjC4SgY6w0_VkD2-VGugrK5-Dy9LrzFzrK4JKkuqItZ7IeT9k98-19GeLbAIw-qLR4r_XJWiQ3PllFWjAp33GKgZWHXbHPJZcuQe1iBy3-2bJuq?expires=1781168400&signature=9cde945d141717f837337f216387aed66c7b1ac0b94f09cc940e4936ad5980e9&req=dSQmEMl3lIZaFb4f3HP0gLO9exd0OAMWdHGdbkMHUWfyHJ8DqO9RpMyUATfY%0ARIs%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141609975/674bf8bafe061765995d9559/woWC9pI5yxqnqXqerkXvQRu15SjC4SgY6w0_VkD2-VGugrK5-Dy9LrzFzrK4JKkuqItZ7IeT9k98-19GeLbAIw-qLR4r_XJWiQ3PllFWjAp33GKgZWHXbHPJZcuQe1iBy3-2bJuq?expires=1781168400&signature=9cde945d141717f837337f216387aed66c7b1ac0b94f09cc940e4936ad5980e9&req=dSQmEMl3lIZaFb4f3HP0gLO9exd0OAMWdHGdbkMHUWfyHJ8DqO9RpMyUATfY%0ARIs%3D%0A)
17. ### **You'll see that the network ISO image is configured for your virtual machine and you can now start it. It will boot, and begin the Debian Linux installation process on the VM.**
18. ### **After this completes, you can go to your VirtualBox homepage and hit the power "button" on the page. This will power it on and allow you to specify your desired configurations, such as preferred language etc. and once complete, you can install your FusionPBX.**

[Back to Top](#h_cf4a5ee2e4)

## 2. Install FusionPBX

FusionPBX can be installed on several different operating systems however we recommend using Debian. If you are installing Debian from scratch it will have prompted you during the installation phase to have created a root password. This will be the password you will enter when you run the command *su root* in the terminal.

1. ### **Visit this website that FusionPBX recommends for following the [install script](http://docs.fusionpbx.com/en/latest/getting_started/quick_install.html) as it is much simpler and faster than previous ways.**
2. ### **Run the following commands as root. This will run a scrip that installs FusionPBX, FreeSWITCH release package and its dependencies, iptables, Fail2ban, NGINX, PHP-FPM, and PostgreSQL.**

   ```
   #upgrade the packages  
   apt-get update && apt-get upgrade -y  
     
   #install packages  
   apt-get install -y git lsb-release  
     
   #get the install script  
   cd /usr/src && git clone https://github.com/fusionpbx/fusionpbx-install.sh.git  
     
   #change the working directory  
   cd /usr/src/fusionpbx-install.sh/debian
   ```
3. ### **At the end of the install script you will be instructed to go to the IP address of the server in your web browser to finish the install in the FusionPBX GUI.**

   [![Script running interface. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141609978/171b31c358431d1226abfe31/0BdTMmvyRbccEzqyLETXksFNWJg4Svc_iRI12U78KLbXJvOdaV-OPVtTZ3-Twv5V38x0wEt34hq0GYX6X-ftuZvx3uArk774YcZXRWCJE2kbdV6ypEGD6TtSicrw-9Oamvwc9wDK?expires=1781168400&signature=23518b7e858dde586774661eabff283544c81381fbf646cae38f05f79039d00b&req=dSQmEMl3lIZXFb4f3HP0gM0wLGnEIa0nViOuARj%2FbUhYLkEljWS5%2BKn1fCHE%0AYj8%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141609978/171b31c358431d1226abfe31/0BdTMmvyRbccEzqyLETXksFNWJg4Svc_iRI12U78KLbXJvOdaV-OPVtTZ3-Twv5V38x0wEt34hq0GYX6X-ftuZvx3uArk774YcZXRWCJE2kbdV6ypEGD6TtSicrw-9Oamvwc9wDK?expires=1781168400&signature=23518b7e858dde586774661eabff283544c81381fbf646cae38f05f79039d00b&req=dSQmEMl3lIZXFb4f3HP0gM0wLGnEIa0nViOuARj%2FbUhYLkEljWS5%2BKn1fCHE%0AYj8%3D%0A)
4. ### **Once you have opened a browser with the URL the terminal gave you, you should see a GUI where you will go on to configure FusionPBX.**
5. ### **Choose your language and click "Next".**

   [![GUI to configure FusionPBX. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141609987/d27d2096decaee53ce6afcaf/OAdcQaObcH4qLNuuwYgT_0UxwZ-6hsIIuOrLGmX0c4dV2H4IimvC4PSEPipnbAlWnzZxiW4MKkgen96N0xPbLSgXUV9mdDtCf0PipNMbsyJhMDlt2kcY1IkShXNbgu9RexsgwRyh?expires=1781168400&signature=1aba6542b39d3048cd13591424a6a99a032089861dac540a7c7c87bd498486c3&req=dSQmEMl3lIlYFb4f3HP0gFJJCCNpCfLwS8YVESjq2oIHrrcbln2xoHX%2Bm9kc%0Ae7I%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141609987/d27d2096decaee53ce6afcaf/OAdcQaObcH4qLNuuwYgT_0UxwZ-6hsIIuOrLGmX0c4dV2H4IimvC4PSEPipnbAlWnzZxiW4MKkgen96N0xPbLSgXUV9mdDtCf0PipNMbsyJhMDlt2kcY1IkShXNbgu9RexsgwRyh?expires=1781168400&signature=1aba6542b39d3048cd13591424a6a99a032089861dac540a7c7c87bd498486c3&req=dSQmEMl3lIlYFb4f3HP0gFJJCCNpCfLwS8YVESjq2oIHrrcbln2xoHX%2Bm9kc%0Ae7I%3D%0A)
6. ### **Your event socket settings will be automatically detected. Click "Next".**

   [![Event Socket settings interface. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141609993/8783b33a68597903aa30655a/vjXcKN-qjVahPx2q0vGCa0RW5TS7mXz31ITBFw9DBZJs9Zt9SsM9SiAfbLG75wFeb_RnWXVIk175uO4yJTv2vn7xwcR4IcbIgyZLIde43ihKpk5gHVm1AuP2Sejh-W4fIMndKknC?expires=1781168400&signature=d4bb1e606885b4fcd8755b1d203b8ddb89afe72ddba3763866e36f953184924d&req=dSQmEMl3lIhcFb4f3HP0gJE%2Fq%2FLDoGGDADccyP1jRSzx3JMYXsQQNz0QG%2BOk%0AeDA%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141609993/8783b33a68597903aa30655a/vjXcKN-qjVahPx2q0vGCa0RW5TS7mXz31ITBFw9DBZJs9Zt9SsM9SiAfbLG75wFeb_RnWXVIk175uO4yJTv2vn7xwcR4IcbIgyZLIde43ihKpk5gHVm1AuP2Sejh-W4fIMndKknC?expires=1781168400&signature=d4bb1e606885b4fcd8755b1d203b8ddb89afe72ddba3763866e36f953184924d&req=dSQmEMl3lIhcFb4f3HP0gJE%2Fq%2FLDoGGDADccyP1jRSzx3JMYXsQQNz0QG%2BOk%0AeDA%3D%0A)
7. ### **Here you will need to enter a username and password as your login credentials for FusionPBX.**

   [![Admin configuration tab. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141609996/9dcb0016e0e6d07116ef8997/bfE7WWFpBk_ANdMD_GS7oei1lk5EvRpHOWhxcInEi8CIXl1meW2EhdAb69zMZehYoNe_PvNb62TsIgi_AKRt4xY5ZmNRb9nPZeGHKt6xBMODud-t8TB51VP1DRZvqDWis0cUTx93?expires=1781168400&signature=56ad86d761eb3d59560c9fab8f1aa89e522a35350250299c9629ecc6d9127dcb&req=dSQmEMl3lIhZFb4f3HP0gHwo8e75HNCDpoTmNkr3Zzpc2FQ53GQrt8mtFX0D%0AXk0%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141609996/9dcb0016e0e6d07116ef8997/bfE7WWFpBk_ANdMD_GS7oei1lk5EvRpHOWhxcInEi8CIXl1meW2EhdAb69zMZehYoNe_PvNb62TsIgi_AKRt4xY5ZmNRb9nPZeGHKt6xBMODud-t8TB51VP1DRZvqDWis0cUTx93?expires=1781168400&signature=56ad86d761eb3d59560c9fab8f1aa89e522a35350250299c9629ecc6d9127dcb&req=dSQmEMl3lIhZFb4f3HP0gHwo8e75HNCDpoTmNkr3Zzpc2FQ53GQrt8mtFX0D%0AXk0%3D%0A)
8. ### **Any writing in bold indicates that you *must* fill it in. At this point you will need to go back to the terminal and grab the details you would have seen, just above the server IP, that relate to the database username and password.**

   [![Database configuration tab. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141609998/8d9e1cbe9010a7c97ba8b1f7/A33PdMSWj-wWT9B2lKezxYG5Iq0g4Syf0Eyg7iw7qfZt2psNGckkInrDz3iw9f6-YiT1u5AGaYO4TWTsd5MrLt81xUDbdBHsJVkPHYUAdh-lTdurujDtTzv9LruvnevFBgOmtKCc?expires=1781168400&signature=8b16a84a4e5c3a3671f689facc656f33bd7b06ade2cd5bf0afbc7871682137d2&req=dSQmEMl3lIhXFb4f3HP0gPxh%2FRFT5Y%2BmsDwEKHvxWsis2vtFA67sx9kKKOvC%0A8Gw%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141609998/8d9e1cbe9010a7c97ba8b1f7/A33PdMSWj-wWT9B2lKezxYG5Iq0g4Syf0Eyg7iw7qfZt2psNGckkInrDz3iw9f6-YiT1u5AGaYO4TWTsd5MrLt81xUDbdBHsJVkPHYUAdh-lTdurujDtTzv9LruvnevFBgOmtKCc?expires=1781168400&signature=8b16a84a4e5c3a3671f689facc656f33bd7b06ade2cd5bf0afbc7871682137d2&req=dSQmEMl3lIhXFb4f3HP0gPxh%2FRFT5Y%2BmsDwEKHvxWsis2vtFA67sx9kKKOvC%0A8Gw%3D%0A)
9. ### **Click "Next".**
10. ### **You'll be brought back to the login page where you will sign in with the username and password from step 7.**

    [![FusionPBX admin interface. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141609999/eddee88e0e0670742549ac7b/qXILBPFQR209aJdbWUskbElWVB8fb61jrqWQargPPJ8RtQPDc511pEnd9hw-nSxcZaEU82X_87kITcxyOhsJ8-U4t4pQGVUEjTjdcn0MJeXgWGDk3Ev0g6tAU4VQFmcEzF9mmb--?expires=1781168400&signature=fb943cea6535adfa2274d1b50ca7a39e5228ffc051fdac6e298fbb9702e31b39&req=dSQmEMl3lIhWFb4f3HP0gEEMTB52%2F2MIQAh9q%2BWEBez%2F4l71gkB4%2FKvv4UFb%0A3xI%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141609999/eddee88e0e0670742549ac7b/qXILBPFQR209aJdbWUskbElWVB8fb61jrqWQargPPJ8RtQPDc511pEnd9hw-nSxcZaEU82X_87kITcxyOhsJ8-U4t4pQGVUEjTjdcn0MJeXgWGDk3Ev0g6tAU4VQFmcEzF9mmb--?expires=1781168400&signature=fb943cea6535adfa2274d1b50ca7a39e5228ffc051fdac6e298fbb9702e31b39&req=dSQmEMl3lIhWFb4f3HP0gEEMTB52%2F2MIQAh9q%2BWEBez%2F4l71gkB4%2FKvv4UFb%0A3xI%3D%0A)

[Back to Top](#h_cf4a5ee2e4)

## 3. Configure a FusionPBX trunk

Once you have the installation of your FusionPBX set up, It is now time to configure your PBX so that you can make and receive calls through Telnyx!

1. ### **Go to the "Advanced" header and to "Upgrade" in the drop down list.**
2. ### **Tick "App Defaults" and press the "Execute" button on the bottom-right.**

   [![Upgrade section on the FusionPBX portal. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141610004/57095bdf71932ebdbc9aedda/crM16sCeju3HqavF2vw_UPzGPQpLTOUznNhdfRYqrgd5VI_SwH9wU12oSZ0xFzYQQnFsCv5N72qgmkhKh8PjPj70OmXVXHGmU9yHM009vTzDjXV2DxN3FautdJ80OBi5n8_gdFVE?expires=1781168400&signature=68519a45387dde89572a328a8ac4b656657b85abb8c78df6120d759d26b8e021&req=dSQmEMh%2BnYFbFb4f3HP0gLa214UOM5CypYW9S0YlcMgiA0svDNzwFK%2F8NGtx%0A5x8%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141610004/57095bdf71932ebdbc9aedda/crM16sCeju3HqavF2vw_UPzGPQpLTOUznNhdfRYqrgd5VI_SwH9wU12oSZ0xFzYQQnFsCv5N72qgmkhKh8PjPj70OmXVXHGmU9yHM009vTzDjXV2DxN3FautdJ80OBi5n8_gdFVE?expires=1781168400&signature=68519a45387dde89572a328a8ac4b656657b85abb8c78df6120d759d26b8e021&req=dSQmEMh%2BnYFbFb4f3HP0gLa214UOM5CypYW9S0YlcMgiA0svDNzwFK%2F8NGtx%0A5x8%3D%0A)
3. ### **Go to the "Accounts" header, select "Gateway", and provide the following details**

   1. **Gateway**: *Telnyx*
   2. **Username**: The username from your Telnyx credentials based connection.
   3. **Password**: The password from your Telnyx credentials based connection.
   4. **From User**: The username from your Telnyx credentials based connection.
   5. **From Domain**: *sip.telnyx.com*
   6. **Proxy**: *sip.telnyx.com*

      [![Accounts section on the FusionPBX portal. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141610007/4f6796a0115b19fe816e8543/JIOlzjYTyf4aUeAckJWoWGLmVkqcaK99nlkRl4hebTzPf-LXA-AQMrpbepRW1LD1k1SpU0l5Qcx6rVvH-fHR1OUEq5-RKZxUonQVfcJ5pGVpS_0gPqI76M6NcSLKG4kLpRYKDLo-?expires=1781168400&signature=10e89112ca7cbd370b60072d012868daf5e67396d5914869e09d984170b26f54&req=dSQmEMh%2BnYFYFb4f3HP0gJ%2Fl3RiBxiF6zdQLa%2FvRNoTsm%2FftB7joycmfc7s4%0AW2Q%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141610007/4f6796a0115b19fe816e8543/JIOlzjYTyf4aUeAckJWoWGLmVkqcaK99nlkRl4hebTzPf-LXA-AQMrpbepRW1LD1k1SpU0l5Qcx6rVvH-fHR1OUEq5-RKZxUonQVfcJ5pGVpS_0gPqI76M6NcSLKG4kLpRYKDLo-?expires=1781168400&signature=10e89112ca7cbd370b60072d012868daf5e67396d5914869e09d984170b26f54&req=dSQmEMh%2BnYFYFb4f3HP0gJ%2Fl3RiBxiF6zdQLa%2FvRNoTsm%2FftB7joycmfc7s4%0AW2Q%3D%0A)
4. ### **Click "Save". You'll be taken to a screen where you'll see that FusionPBX is now registered with Telnyx.**

   [![FusionPBX portal. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141610009/49d9930363bab83ea09f6cd6/9zv9oWXNvMM1rHkUCou8uXMIyHJXdWze7AV8oospxH0xEgDXZ4jXChPIPTKIb0HNrrFIph4y5W7AhWOY-t7ZJYzKPE1rX8rAdFPjyv9bGe0Rt7Lmxgs0AiEMdi24xigF-6D7cguA?expires=1781168400&signature=cce06ea9d1f1ed62bbbd43451915fcde074e163a5f57d384a25e23560ec18937&req=dSQmEMh%2BnYFWFb4f3HP0gLgnfsI2i0rOeFSzsOl4IVfpEl1LcjiurLp69AD1%0Ab24%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141610009/49d9930363bab83ea09f6cd6/9zv9oWXNvMM1rHkUCou8uXMIyHJXdWze7AV8oospxH0xEgDXZ4jXChPIPTKIb0HNrrFIph4y5W7AhWOY-t7ZJYzKPE1rX8rAdFPjyv9bGe0Rt7Lmxgs0AiEMdi24xigF-6D7cguA?expires=1781168400&signature=cce06ea9d1f1ed62bbbd43451915fcde074e163a5f57d384a25e23560ec18937&req=dSQmEMh%2BnYFWFb4f3HP0gLgnfsI2i0rOeFSzsOl4IVfpEl1LcjiurLp69AD1%0Ab24%3D%0A)

[Back to Top](#h_cf4a5ee2e4)

## 4. Create your extensions

1. ### **Now go to the "Accounts" header and select "Extensions".**
2. ### **Click the "Add" button to add an extension. The following image shows an example of what they should look like.**

   Note: The Telnyx support portal automatically shrinks images, so if you have trouble seeing it, right-click on the image and select Open Image in New Tab to view it in full size.   
   ​

   [![Extensions section of the FusionPBX portal. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141610011/9d5b666341d4258b7beca84f/HmD2P0jxlJy3o32s5ED_M7oKWzhhhyHPcqXy0u2lXYzqlEq98n9__sSnjSX5doZrRJ06sN2LlAYxB1-zOOuGlr-kyAyYY2MPIFEgsoCB5BLksDRsA3iKkfxl-XWk-diGHhW5qEQG?expires=1781168400&signature=5bc723d2c3e988f1e08e6425d949b2075605cf254c4245b28aea70fa13ad3e4b&req=dSQmEMh%2BnYBeFb4f3HP0gPzCul60FySLsOrCE0LOPeyWBAI7%2BJOQNdhBriLO%0AsHA%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141610011/9d5b666341d4258b7beca84f/HmD2P0jxlJy3o32s5ED_M7oKWzhhhyHPcqXy0u2lXYzqlEq98n9__sSnjSX5doZrRJ06sN2LlAYxB1-zOOuGlr-kyAyYY2MPIFEgsoCB5BLksDRsA3iKkfxl-XWk-diGHhW5qEQG?expires=1781168400&signature=5bc723d2c3e988f1e08e6425d949b2075605cf254c4245b28aea70fa13ad3e4b&req=dSQmEMh%2BnYBeFb4f3HP0gPzCul60FySLsOrCE0LOPeyWBAI7%2BJOQNdhBriLO%0AsHA%3D%0A)
3. ### **Once you've created an extension, you can click into it and change the password that was given to you if you'd like to.**

   Note: Depending on your phone configuration, you may also wish to configure an outbound caller ID. You can apply this via the "Outbound Caller ID Number" field. For more information on the fields below, please visit [FusionPBX's extensions documentation](https://docs.fusionpbx.com/en/latest/accounts/extensions.html).  
   ​  
   ​*Before configuring an outbound caller ID, you should be aware of some of the naming conventions standard for caller ID creation:*

   * #### **Your outbound Caller ID Name should be in "capital letters". This will appears more clearly/visible on some devices.**
   * #### **You "must NOT use any special characters", as they will not be displayed.**
   * #### **Some of regular "Canadian providers will not show more than 15 characters". We suggest shrinking or adapt your caller ID.**
   * #### **"Spaces are allowed" in a caller id name.**
   * #### **Be familiar with [Telnyx's caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy).**

     [![Outbound Caller ID Number field. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141610014/be43bd50671eed94b6219daa/_u3sAZoyhUxgIhsf9u17ZMgHjiisQk9iRfT2Pk19fYYGiabGxzX-28xWJV-EwZo5V8BaIsJNvr0_zHlweFoBw8_IuaONzKWLSHEnIGn5HaEVz26SpiTRm-SPnhLw-pA-toqeafBf?expires=1781168400&signature=37a5432088ce0f6eb5c96c7b23f839a1405c006fb660b24bd84d32e81bcef9ca&req=dSQmEMh%2BnYBbFb4f3HP0gEmDNQbb6nz84D5bxKNMlJWA6ZFTRnbuj2470lQz%0A7NU%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141610014/be43bd50671eed94b6219daa/_u3sAZoyhUxgIhsf9u17ZMgHjiisQk9iRfT2Pk19fYYGiabGxzX-28xWJV-EwZo5V8BaIsJNvr0_zHlweFoBw8_IuaONzKWLSHEnIGn5HaEVz26SpiTRm-SPnhLw-pA-toqeafBf?expires=1781168400&signature=37a5432088ce0f6eb5c96c7b23f839a1405c006fb660b24bd84d32e81bcef9ca&req=dSQmEMh%2BnYBbFb4f3HP0gEmDNQbb6nz84D5bxKNMlJWA6ZFTRnbuj2470lQz%0A7NU%3D%0A)
4. #### Click "**Save"**.
5. #### Go to the "**Dialplan"** header and select "**Destinations"**.
6. #### Click the "**Add"** button to add your destinations.

   [![Destinations section of the Dial Plan field. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141610015/92da404d3c1aa3fd632058de/aaJisA5xqgkDIGPzNiLcCCrSW3fHB0GOEH_aViboakWGtEhxVDhsUGe_vaBDFUvTpFuuuYik6HuhmN4XLI6v8Oqqqos4UZTCTnrJd5lqy4fP6Z-Tiom70n0JtxAEya53zjL_2eNB?expires=1781168400&signature=e53d3e83db079c9d944e5e1a37959688b80ebea5c83120776bc0ef30253e8d24&req=dSQmEMh%2BnYBaFb4f3HP0gAOA5sbyyC9znvheigUZscAAqBPocobzBHNTjlVa%0AxWM%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141610015/92da404d3c1aa3fd632058de/aaJisA5xqgkDIGPzNiLcCCrSW3fHB0GOEH_aViboakWGtEhxVDhsUGe_vaBDFUvTpFuuuYik6HuhmN4XLI6v8Oqqqos4UZTCTnrJd5lqy4fP6Z-Tiom70n0JtxAEya53zjL_2eNB?expires=1781168400&signature=e53d3e83db079c9d944e5e1a37959688b80ebea5c83120776bc0ef30253e8d24&req=dSQmEMh%2BnYBaFb4f3HP0gAOA5sbyyC9znvheigUZscAAqBPocobzBHNTjlVa%0AxWM%3D%0A)

   1. You'll want to add in a number that you purchased on your Portal account to "**Destination"** - Make sure to add a *+1* in front of the number.
   2. Then for "**Actions"**, select an extension you created from the drop-down list.

      [![Destination section. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141610020/a3ff7db4cdfc847de4556ab5/jWrb-YTj5GcrCSHb97vbyR6znSh6Zn77ZXYNsTzHqMeBkOchNYOrtYsvQBV-Lv8H88rb3oTRf4p2_3ZCLVTYxo9PNzaHBE5ZVuQuOexpoTG6YmdvI0L0jrzQssFLaDzyCWk1-7Nh?expires=1781168400&signature=307f98e2800a8b3fddb88e1fa27a373e6b575be433743a4e3cacc571129a6e86&req=dSQmEMh%2BnYNfFb4f3HP0gOQpimRg9EKUz6G9FAN7MQL5gwM6O%2Fe3mNMI2oMQ%0A%2B2I%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141610020/a3ff7db4cdfc847de4556ab5/jWrb-YTj5GcrCSHb97vbyR6znSh6Zn77ZXYNsTzHqMeBkOchNYOrtYsvQBV-Lv8H88rb3oTRf4p2_3ZCLVTYxo9PNzaHBE5ZVuQuOexpoTG6YmdvI0L0jrzQssFLaDzyCWk1-7Nh?expires=1781168400&signature=307f98e2800a8b3fddb88e1fa27a373e6b575be433743a4e3cacc571129a6e86&req=dSQmEMh%2BnYNfFb4f3HP0gOQpimRg9EKUz6G9FAN7MQL5gwM6O%2Fe3mNMI2oMQ%0A%2B2I%3D%0A)
7. #### Click "**Save"**.

[Back to Top](#h_cf4a5ee2e4)

## 5. Configure inbound routing

In this step, you will configure an inbound calling route pattern that CompletePBX will require in order for you to receive inbound calls from your DID. Each DID will need to be associated with an inbound route. Multiple DIDs can be associated with the same route, but any single DID can only be associated with a single route.

1. Go to the **Dialplan** header and select **Inbound routes**. Your inbound routes should be added automatically that relate to your destinations you created.

   [![Inbound routes in the Dial Plan section. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141610022/d0915bc7f02caa391b057a43/7HseU4uZ_bz6su-X2znvfczQkmZPyDYnpvYc55kfnOy4bhdVi-uVjYN2GHm6RARgSuJbwdR3QbaQOxwDt18eL2Dwcnt9iS2OBTA-QHfvNN_sCvcBs8OhRWGtuUzViyUXcvca2XdC?expires=1781168400&signature=f5de1cc0bf622a18fbf8267f0c370e34539b4d5a26768508fa48c7bdce24e322&req=dSQmEMh%2BnYNdFb4f3HP0gHMe4ayviPlE6lwFpmYSfK69I1luvo4GJdbJ7ay0%0ALvI%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141610022/d0915bc7f02caa391b057a43/7HseU4uZ_bz6su-X2znvfczQkmZPyDYnpvYc55kfnOy4bhdVi-uVjYN2GHm6RARgSuJbwdR3QbaQOxwDt18eL2Dwcnt9iS2OBTA-QHfvNN_sCvcBs8OhRWGtuUzViyUXcvca2XdC?expires=1781168400&signature=f5de1cc0bf622a18fbf8267f0c370e34539b4d5a26768508fa48c7bdce24e322&req=dSQmEMh%2BnYNdFb4f3HP0gHMe4ayviPlE6lwFpmYSfK69I1luvo4GJdbJ7ay0%0ALvI%3D%0A)
2. When you click on any of the numbers you created as inbound routes you will see a dialplan like the picture that follows. (You will need to make sure that your number format is set to E164 on your connection you created in your Mission Control Portal.)

   [![Inbound routes in the Dial Plan section. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141610024/119e81ac3bef16ae42244427/JHO_Yzh0lvXipftJwBQztg_koa8d_o9DR99Vaa7MrgqswNO3i4nw1yt1Ke-OmUD9uiFLxop4Il7hKvIp1yOrcYGOne6WRkbGGIRMxj7o65CUFkwewTVCq74y70rd8Wo8FOd7ChHC?expires=1781168400&signature=2f35530597fc4a553eeb5911455678bba6c57427fdf1b98711d53f9853086e53&req=dSQmEMh%2BnYNbFb4f3HP0gI6at4gD2%2F7pLWth5LwZzUWZOC91AJvXsA2Q1teV%0AAIA%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141610024/119e81ac3bef16ae42244427/JHO_Yzh0lvXipftJwBQztg_koa8d_o9DR99Vaa7MrgqswNO3i4nw1yt1Ke-OmUD9uiFLxop4Il7hKvIp1yOrcYGOne6WRkbGGIRMxj7o65CUFkwewTVCq74y70rd8Wo8FOd7ChHC?expires=1781168400&signature=2f35530597fc4a553eeb5911455678bba6c57427fdf1b98711d53f9853086e53&req=dSQmEMh%2BnYNbFb4f3HP0gI6at4gD2%2F7pLWth5LwZzUWZOC91AJvXsA2Q1teV%0AAIA%3D%0A)

[Back to Top](#h_cf4a5ee2e4)

## 6. Configure outbound routing

In this step, you will configure an outbound calling route pattern that CompletePBX will use as a template, or set of rules, to follow for outbound calls associated with the route.

1. Go to the **Dialplan** header and select **Outbound routes**.
2. Click the **Add** button to create your different outbound routes.

   [![Outbound routes in the Dial Plan header. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141610028/23b1fe172b791825cf359988/p8QZ_1MIlnlX56va9ouWGKRcgHqF4sgejXlodI3l4xEASYGkwm4btK7tCSJukTIsjBxq1LzJXIYWLIyBqsZvddC_SEVBrNVm0KtYragAfrcl9hyLycDLDLveu0cJbICC4X1pdGp8?expires=1781168400&signature=2865e97216042a51700bb6a61f84be878f16c35d65f80748af7a1c4605885e0c&req=dSQmEMh%2BnYNXFb4f3HP0gJuT42JuHEMZQxLYF4ILK8BlnCx89DYKUmR%2BO%2FNJ%0ADv8%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141610028/23b1fe172b791825cf359988/p8QZ_1MIlnlX56va9ouWGKRcgHqF4sgejXlodI3l4xEASYGkwm4btK7tCSJukTIsjBxq1LzJXIYWLIyBqsZvddC_SEVBrNVm0KtYragAfrcl9hyLycDLDLveu0cJbICC4X1pdGp8?expires=1781168400&signature=2865e97216042a51700bb6a61f84be878f16c35d65f80748af7a1c4605885e0c&req=dSQmEMh%2BnYNXFb4f3HP0gJuT42JuHEMZQxLYF4ILK8BlnCx89DYKUmR%2BO%2FNJ%0ADv8%3D%0A)
3. Create your outbound route using the following parameters:

   1. **Gateway**: Select *Telnyx*
   2. **Dialplan Expression**: Select the region you want to configure the dialplan expression for. i.e.: *North America*

      [![Outbound routes credentials field. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141610033/90ab872c26271e62a0a4d5a6/Ce4ouP0EndVR-GLk_44RRUXSTMXJu_-zUK4TZ26S1aBqvzHVwiWhDjNmInEqzMsAaf9t3lURUygSd8WCDfNQW_Hk8te19ZhAcRsaClFyFOIIS8zeZJ82DhTme2jRzj39TaYJE7Yt?expires=1781168400&signature=d40eef82eb13daac47732251f804e1b3b511a50d722f9014d79d538649b7ee94&req=dSQmEMh%2BnYJcFb4f3HP0gIuLOzPZ%2Bi4Mpw8V2tohhKkS%2Bm0GGihOb7Mo%2BYe%2B%0Axvs%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141610033/90ab872c26271e62a0a4d5a6/Ce4ouP0EndVR-GLk_44RRUXSTMXJu_-zUK4TZ26S1aBqvzHVwiWhDjNmInEqzMsAaf9t3lURUygSd8WCDfNQW_Hk8te19ZhAcRsaClFyFOIIS8zeZJ82DhTme2jRzj39TaYJE7Yt?expires=1781168400&signature=d40eef82eb13daac47732251f804e1b3b511a50d722f9014d79d538649b7ee94&req=dSQmEMh%2BnYJcFb4f3HP0gIuLOzPZ%2Bi4Mpw8V2tohhKkS%2Bm0GGihOb7Mo%2BYe%2B%0Axvs%3D%0A)
4. Click **Save**.

[Back to Top](#h_cf4a5ee2e4)

## 7. Register your extensions with a device

1. Go to the **Status** header and select **Registrations**. At this point you will need to register the extensions you created with whatever device you choose.   
   ​  
   In this example, we used [Zoiper](https://support.telnyx.com/en/articles/6133517-zoiper-communicator) and Xlite softphone to register these extensions.
2. All your registered devices will show up on the registration’s page.

   [![Extension registration in the status field. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141610043/d5c28feef48188f1fa359278/IDe8o7oTX-RI0gGMsV6_gCGwMTUuA9eTAT9LDhENqgsWkhcwAkrfiddS9CJ8AF40ckDxbO7pCbBbSQGnqqKp_E2HAGCnDfaYmevJtxF7UsuQVII-NC6HaZFEv_KWEBVNlSRlQbZP?expires=1781168400&signature=c5015291060d340fca90bf2f4c5df6b585c607293668f7c3af6031ba64853e13&req=dSQmEMh%2BnYVcFb4f3HP0gG2dz2QVHRV%2BkT0lccs5W%2BovfezMRYQdYSy0qGRc%0AS88%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/141610043/d5c28feef48188f1fa359278/IDe8o7oTX-RI0gGMsV6_gCGwMTUuA9eTAT9LDhENqgsWkhcwAkrfiddS9CJ8AF40ckDxbO7pCbBbSQGnqqKp_E2HAGCnDfaYmevJtxF7UsuQVII-NC6HaZFEv_KWEBVNlSRlQbZP?expires=1781168400&signature=c5015291060d340fca90bf2f4c5df6b585c607293668f7c3af6031ba64853e13&req=dSQmEMh%2BnYVcFb4f3HP0gG2dz2QVHRV%2BkT0lccs5W%2BovfezMRYQdYSy0qGRc%0AS88%3D%0A)

Both extensions are registered with the servers IP address so they can now make and receive calls internally via calling 1000 or 1001. Your inbound and outbound routes are set and you will be able to make and receive calls externally also.

That's it, you've now completed the configuration of FusionPBX and can now make and receive calls by using Telnyx as the SIP provider.

[Back to Top](#h_cf4a5ee2e4)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [FusionPBX documentation](https://docs.fusionpbx.com/en/latest/)
* [Quick install guide](https://docs.fusionpbx.com/en/latest/getting_started/quick_install.html)
* [Install scripts](https://www.fusionpbx.com/download.php)
* [FusionPBX support](https://www.fusionpbx.com/support)

---

---

Related Articles

[FreePBX Trunk Settings With Telnyx](https://support.telnyx.com/en/articles/1130620-freepbx-trunk-settings-with-telnyx)[Configuring a FreePBX V13 Credentials Trunk](https://support.telnyx.com/en/articles/1130648-configuring-a-freepbx-v13-credentials-trunk)[FreePBX V13: PJSIP Credentials](https://support.telnyx.com/en/articles/1277754-freepbx-v13-pjsip-credentials)[FreePBX V14: Credentials - ChanSIP](https://support.telnyx.com/en/articles/3284752-freepbx-v14-credentials-chansip)[FreePBX V15: Credentials - PJSIP](https://support.telnyx.com/en/articles/5619597-freepbx-v15-credentials-pjsip)

Did this answer your question?

😞😐😃

Table of contents
