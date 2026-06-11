---
source_url: https://support.telnyx.com/en/articles/5464056-setting-up-freepbx-v15-with-telnyx-api
scraped: 2026-06-11
---

Setting Up FreePBX V15 with Telnyx API | Telnyx Help Center

[Skip to main content](#main-content)

# Setting Up FreePBX V15 with Telnyx API

Master the setup of FreePBX V15 Credentials Trunk using Telnyx. Begin your streamlined experience now!

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_e22b63eb98)

[FreePBX](https://www.freepbx.org/) is a web-based open source GUI (graphical user interface) that controls and manages Asterisk (PBX), an open source communication server. FreePBX is licensed under the GNU General Public License (GPL), an open source license. FreePBX can be installed manually or as part of the pre-configured FreePBX Distro that includes the system OS, Asterisk, FreePBX GUI and assorted dependencies.

|  |
| --- |
| ***Note:*** *We suggest using PJSIP as an upgrade from Chan\_SIP, as Chan\_SIP is outdated, and the majority of users are moving to PJSIP which provides a number of more future proof options, and is still actively being improved by the community. You can find out more about PJSIP [here](https://www.pjsip.org/about.htm).* |

Additional documentation and resoruces:

* [FreePBX support](https://www.freepbx.org/support/)
* [FreePBX documentation](https://wiki.freepbx.org/#all-updates)

---

# Instructions for Configuring a FreePBX V15 IP Trunk

In this activity you will:

1. [Install your FreePBX V15](#h_faae438a80)
2. [Configure basic settings for your FreePBX](#h_16bf32ee44)
3. [Configure SIP settings for your FreePBX](#h_ce1b3f439a)
4. [Configure extensions for your FreePBX](#h_3eae387c0a)
5. [Configure a trunk for your FreePBX](#h_6d7bce3690)
6. [Configure outbound and inbound settings for your FreePBX](#h_83e27c430a)
7. [Configure outbound routing](#h_13df0bbb51)
8. [Configure inbound routing](#h_cd044d51db)

**Pre-requisites**

* [Download](https://www.freepbx.org/downloads/) and [install](https://sangomakb.atlassian.net/wiki/spaces/PP/pages/10682958) FreePBX V15
* [Configure your Telnyx Mission Control Portal](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* [Set up a credentials-based connection on your Telnyx Mission Control Portal](https://portal.telnyx.com/#/app/connections)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for FreePBX/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Install your FreePBX V15

In this section, you'll go through the steps you need to follow to install FreePBX.

1. ### **Once you load the ISO onto your server or virtual machine, you'll have a few options to select for installation. We'll be doing a full install via asterisk 16.**

   [![Sangoma Virtual Machine interface. ](https://downloads.intercomcdn.com/i/o/371234430/f3e6e9f02a3b075254e2c15f/image.png?expires=1781168400&signature=f53009d6b6319b3254b0afc55aa8b6a035dd43a0babebc53700f9d580846a78c&req=dycmFMp6mYJfFb4f3HP0gFuv0SS6y4Kye2wXVfOT%2BG4qKplLC5mLanWnImrY%0AHOY%3D%0A)](https://downloads.intercomcdn.com/i/o/371234430/f3e6e9f02a3b075254e2c15f/image.png?expires=1781168400&signature=f53009d6b6319b3254b0afc55aa8b6a035dd43a0babebc53700f9d580846a78c&req=dycmFMp6mYJfFb4f3HP0gFuv0SS6y4Kye2wXVfOT%2BG4qKplLC5mLanWnImrY%0AHOY%3D%0A)
2. ### **You'll be prompted for your preferred video method you want to install.**

   [![Preferred video installation method options on the Virtual machine. ](https://downloads.intercomcdn.com/i/o/371750617/f3e85ba2df6cef3ef3c26aa3/image.png?expires=1781168400&signature=1e33d0e58cb5860c15beb800886fb581b1aab9414908aa3e08ec144568049aec&req=dycmEcx%2Bm4BYFb4f3HP0gE4mffVk4LV3LXl20bY9qzWj%2FCAv17kPH9THhgtm%0AmhI%3D%0A)](https://downloads.intercomcdn.com/i/o/371750617/f3e85ba2df6cef3ef3c26aa3/image.png?expires=1781168400&signature=1e33d0e58cb5860c15beb800886fb581b1aab9414908aa3e08ec144568049aec&req=dycmEcx%2Bm4BYFb4f3HP0gE4mffVk4LV3LXl20bY9qzWj%2FCAv17kPH9THhgtm%0AmhI%3D%0A)
3. ### **The installer will now start.**

   [![The installer interface. ](https://downloads.intercomcdn.com/i/o/371237494/f768024c66e5720d3ebb5295/image.png?expires=1781168400&signature=fe5b090941d20759b3eb722be3909d9b9c35abc49a1bc1a90664d4779e372cd5&req=dycmFMp5mYhbFb4f3HP0gAzIDy6qpL%2BQDewNsmXgJmzdApoor4m9xioFeBML%0A5Q0%3D%0A)](https://downloads.intercomcdn.com/i/o/371237494/f768024c66e5720d3ebb5295/image.png?expires=1781168400&signature=fe5b090941d20759b3eb722be3909d9b9c35abc49a1bc1a90664d4779e372cd5&req=dycmFMp5mYhbFb4f3HP0gAzIDy6qpL%2BQDewNsmXgJmzdApoor4m9xioFeBML%0A5Q0%3D%0A)
4. ### **The installer will start but you will see it shows the root password is not set. You will need to click on the root password box to set your root password. The installation process can not complete until this is done.**

   [![Configuration User Settings. ](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600450/6a1dfe8e806d827c5e130fa6/Screen-20Shot-202017-07-20-20at-2010.39.35-20AM.png?expires=1781168400&signature=74a1b67621d185c586f65d0edc749999b80006ca4e0097dc933f01ea602d197f&req=dSQkEMl%2BmYRfFb4f3HP0gF4h0payer9G1OiGQWpPaz9G%2FIAhhHwGrXxwQMN7%0Afzw%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600450/6a1dfe8e806d827c5e130fa6/Screen-20Shot-202017-07-20-20at-2010.39.35-20AM.png?expires=1781168400&signature=74a1b67621d185c586f65d0edc749999b80006ca4e0097dc933f01ea602d197f&req=dSQkEMl%2BmYRfFb4f3HP0gF4h0payer9G1OiGQWpPaz9G%2FIAhhHwGrXxwQMN7%0Afzw%3D%0A)
5. ### **Type in your root password and confirm it a second time and click on the Done option in the top left screen.**

   [![Root Password settings. ](https://downloads.intercomcdn.com/i/o/371239957/cb48106a43b8b94afb54f88e/image.png?expires=1781168400&signature=09dac023e5f08fe38fa9f8693e9250c30c5e90f186e4adf83d6e2b13e24da94b&req=dycmFMp3lIRYFb4f3HP0gAQZOGiZjcXtsAa2IV%2B56OJ6asT1FbxuCLJIgb4S%0AaF8%3D%0A)](https://downloads.intercomcdn.com/i/o/371239957/cb48106a43b8b94afb54f88e/image.png?expires=1781168400&signature=09dac023e5f08fe38fa9f8693e9250c30c5e90f186e4adf83d6e2b13e24da94b&req=dycmFMp3lIRYFb4f3HP0gAQZOGiZjcXtsAa2IV%2B56OJ6asT1FbxuCLJIgb4S%0AaF8%3D%0A)
6. ### **At this time the FreePBX package itself can take 15 or more minutes to install and does requires access to the internet so depending on your internet speeds it can take awhile to install so be patient.**

   [![Freepbx installation initialization. ](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600456/7efa758314eb270ff69ef76f/Screen-20Shot-202017-07-20-20at-2010.58.19-20AM.png?expires=1781168400&signature=3f177fd1081900512b39434e8cc3ab804ebf7af2afad7e15374f39503baea1ad&req=dSQkEMl%2BmYRZFb4f3HP0gLUmzG%2F1QjjZIzWcoZilEcoK1zPO8jmUS0FvU7lq%0AxLQ%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600456/7efa758314eb270ff69ef76f/Screen-20Shot-202017-07-20-20at-2010.58.19-20AM.png?expires=1781168400&signature=3f177fd1081900512b39434e8cc3ab804ebf7af2afad7e15374f39503baea1ad&req=dSQkEMl%2BmYRZFb4f3HP0gLUmzG%2F1QjjZIzWcoZilEcoK1zPO8jmUS0FvU7lq%0AxLQ%3D%0A)
7. ### **Once the install has 100% completed it will give you a reboot option as shown below. Click on reboot your your system is now installed.**

   [![Complete Configuration interface. ](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600457/09b3e6f7404341e147d98a5e/Screen-20Shot-202017-07-20-20at-2011.19.53-20AM.png?expires=1781168400&signature=325c38228a91898a0a9e94563e94369598c180fc4f5a6d878f78ea501bf7691a&req=dSQkEMl%2BmYRYFb4f3HP0gGd9IMO2SDY6a48CZ7H0mHC3NhBi9K9St0IMQ0nt%0AZuE%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600457/09b3e6f7404341e147d98a5e/Screen-20Shot-202017-07-20-20at-2011.19.53-20AM.png?expires=1781168400&signature=325c38228a91898a0a9e94563e94369598c180fc4f5a6d878f78ea501bf7691a&req=dSQkEMl%2BmYRYFb4f3HP0gGd9IMO2SDY6a48CZ7H0mHC3NhBi9K9St0IMQ0nt%0AZuE%3D%0A)
8. ### **Once the process is complete, you'll reach the Linux console/command prompt login. You can log in here using the username "root" without quotes, and the Root password you selected earlier.**

   [![Linux console prompt login section. ](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600459/9eaf327f9aed4991ba67981e/Screen-20Shot-202017-07-20-20at-2011.58.00-20AM.png?expires=1781168400&signature=b206bacc5fc395bfc087fe3d7e6e8fae29026057a38bedb76b9c66d4432d6f4c&req=dSQkEMl%2BmYRWFb4f3HP0gLPD%2B8q3CmZZAMmnOnXcmK1Y%2FfduS6R4iAA%2BOTXD%0AB9A%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600459/9eaf327f9aed4991ba67981e/Screen-20Shot-202017-07-20-20at-2011.58.00-20AM.png?expires=1781168400&signature=b206bacc5fc395bfc087fe3d7e6e8fae29026057a38bedb76b9c66d4432d6f4c&req=dSQkEMl%2BmYRWFb4f3HP0gLPD%2B8q3CmZZAMmnOnXcmK1Y%2FfduS6R4iAA%2BOTXD%0AB9A%3D%0A)
9. ### **After you log in, you should see the IP address of your PBX as shown below. Take note of this IP address as you will need it in the next step.**

   [![IP address page. ](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600460/cb485197bf2d00f58b6be3f2/Screen-20Shot-202017-07-20-20at-2011.57.27-20AM.png?expires=1781168400&signature=a1a0ac902f778c3d75a59751409a86bf6d1a5078e9ef0feb6dcaa1a4ad5c5c40&req=dSQkEMl%2BmYdfFb4f3HP0gJCNT4395ngW3GRHmTEZbC7w38%2BXBkLSDaosxZI9%0Ao%2FM%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600460/cb485197bf2d00f58b6be3f2/Screen-20Shot-202017-07-20-20at-2011.57.27-20AM.png?expires=1781168400&signature=a1a0ac902f778c3d75a59751409a86bf6d1a5078e9ef0feb6dcaa1a4ad5c5c40&req=dSQkEMl%2BmYdfFb4f3HP0gJCNT4395ngW3GRHmTEZbC7w38%2BXBkLSDaosxZI9%0Ao%2FM%3D%0A)
10. #### **Enter the IP address of the new PBX into your web browser. The first time you do so, you'll be asked to create the admin username and the admin password. That username and password will be used in the future to access the FreePBX configuration screen.** Note: These passwords do not change the Root password! They are only used for access to the FreePBX web interface.

    [![Initial Setup for FreePBX. ](https://downloads.intercomcdn.com/i/o/371682345/b542cbfa5a33996e3c37677b/image.png?expires=1781168400&signature=882a192ce4ef441af5b58a0430f0676fcd002a90fa0e053db9bb67fcaa73c280&req=dycmEMF8noVaFb4f3HP0gO8F%2BRtVpNphvE8fKz5%2BpYJEZvAM4uC0BFO6h0n7%0A1Bg%3D%0A)](https://downloads.intercomcdn.com/i/o/371682345/b542cbfa5a33996e3c37677b/image.png?expires=1781168400&signature=882a192ce4ef441af5b58a0430f0676fcd002a90fa0e053db9bb67fcaa73c280&req=dycmEMF8noVaFb4f3HP0gO8F%2BRtVpNphvE8fKz5%2BpYJEZvAM4uC0BFO6h0n7%0A1Bg%3D%0A)
11. ### **Once submitted you can log in to the admin panel with the username and password set up on the step above.**

[Back to Top](#h_e22b63eb98)

## 2. Configuring basic settings for your FreePBX

In this step, you'll configure your FreePBX V15 and connect it to Telnyx. To begin, notice that the main FreePBX screen will offer you four options:

[![Basic settings configuration. ](https://downloads.intercomcdn.com/i/o/371686829/2e2dc2f528c30feb84c8f24c/image.png?expires=1781168400&signature=01710212a4d1efc6c11a36d48cf70f94632b14c8d397c9ddd079acee81f3ba3a&req=dycmEMF4lYNWFb4f3HP0gFX7ylpFUZTTghLR7lHwmQEEL0CwGZIPjswRG7bg%0AsB1Kd4WlvLYMKYysBQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/371686829/2e2dc2f528c30feb84c8f24c/image.png?expires=1781168400&signature=01710212a4d1efc6c11a36d48cf70f94632b14c8d397c9ddd079acee81f3ba3a&req=dycmEMF4lYNWFb4f3HP0gFX7ylpFUZTTghLR7lHwmQEEL0CwGZIPjswRG7bg%0AsB1Kd4WlvLYMKYysBQ%3D%3D%0A)

* **FreePBX Administration** will allow you to configure your PBX. Use the admin username and admin password you configured in the step above to login. This section is what most people refer to as "FreePBX."

* **User Control Panel** is where a user can log in to make web calls, set up their phone buttons, view voicemails, send and receive faxes, use SMS & XMPP messaging, view conferences, and more, depending on what you have enabled for the user, see [User Control Panel (UCP) 14+](https://wiki.freepbx.org/pages/viewpage.action?pageId=74318855) for more information.

* **Operator Panel** is a screen that allows an operator to control calls (needs additional licensing)

* **Get Support** takes you to a web page about various official support options for FreePBX.

1. Enter in the username, password and admin email address in order to create your account.

   [![Initial setup configuration. ](https://downloads.intercomcdn.com/i/o/371682345/b542cbfa5a33996e3c37677b/image.png?expires=1781168400&signature=882a192ce4ef441af5b58a0430f0676fcd002a90fa0e053db9bb67fcaa73c280&req=dycmEMF8noVaFb4f3HP0gO8F%2BRtVpNphvE8fKz5%2BpYJEZvAM4uC0BFO6h0n7%0A1Bg%3D%0A)](https://downloads.intercomcdn.com/i/o/371682345/b542cbfa5a33996e3c37677b/image.png?expires=1781168400&signature=882a192ce4ef441af5b58a0430f0676fcd002a90fa0e053db9bb67fcaa73c280&req=dycmEMF8noVaFb4f3HP0gO8F%2BRtVpNphvE8fKz5%2BpYJEZvAM4uC0BFO6h0n7%0A1Bg%3D%0A)
2. Once you've created your account, you'll be brought to the dashboard. Select **FreePBX Administration** and enter your username and password.
3. Follow the process to activate your FreePBX V15.

   [![FreePBX server welcome page. ](https://downloads.intercomcdn.com/i/o/371690168/5184de3771cc9ed8849b612e/image.png?expires=1781168400&signature=bfa6fb9b95cd41e40ee98aa17ced8bdd8d6b8b9c007a899eee3261306d75ed9c&req=dycmEMB%2BnIdXFb4f3HP0gFNF0Btjc7BZVSiqH5buLz8yssKx71QQwYHCbqQ2%0ABD8%3D%0A)](https://downloads.intercomcdn.com/i/o/371690168/5184de3771cc9ed8849b612e/image.png?expires=1781168400&signature=bfa6fb9b95cd41e40ee98aa17ced8bdd8d6b8b9c007a899eee3261306d75ed9c&req=dycmEMB%2BnIdXFb4f3HP0gFNF0Btjc7BZVSiqH5buLz8yssKx71QQwYHCbqQ2%0ABD8%3D%0A)
4. Select your default locales.

   [![Default locales selection. ](https://downloads.intercomcdn.com/i/o/371692642/306870ad1740ec770a45f39d/image.png?expires=1781168400&signature=470bae47dc0cc65164dd526b635d30e36eba898f596ade0765cec51029ec2327&req=dycmEMB8m4VdFb4f3HP0gOtFlqfIw%2F3vwlsLA2Y91717crVjNOGFwHlqZMs%2B%0ADcE%3D%0A)](https://downloads.intercomcdn.com/i/o/371692642/306870ad1740ec770a45f39d/image.png?expires=1781168400&signature=470bae47dc0cc65164dd526b635d30e36eba898f596ade0765cec51029ec2327&req=dycmEMB8m4VdFb4f3HP0gOtFlqfIw%2F3vwlsLA2Y91717crVjNOGFwHlqZMs%2B%0ADcE%3D%0A)
5. You'll be presented with some firewall details and other suggestions. You are welcome to set this up based on your requirements.
6. Once you're back at the dashboard, you'll see more detail.

   [![FreePBX dashboard. ](https://downloads.intercomcdn.com/i/o/371694374/30dfd033ce49665b12e68e36/image.png?expires=1781168400&signature=35196af0f31fa1b0de2e9eaf368b635b376c866d7da7cc8435ba1fcab7162b98&req=dycmEMB6noZbFb4f3HP0gGUdBjMUW%2F%2BO560BfuEgobUw9gkYyMz5cdNhWSqs%0AESU%3D%0A)](https://downloads.intercomcdn.com/i/o/371694374/30dfd033ce49665b12e68e36/image.png?expires=1781168400&signature=35196af0f31fa1b0de2e9eaf368b635b376c866d7da7cc8435ba1fcab7162b98&req=dycmEMB6noZbFb4f3HP0gGUdBjMUW%2F%2BO560BfuEgobUw9gkYyMz5cdNhWSqs%0AESU%3D%0A)

[Back to Top](#h_e22b63eb98)

## 3. Configuring SIP settings for your FreePBX

At this point you can now work on confirming network settings and configuring your [SIP trunks](https://telnyx.com/products/sip-trunks) and extensions.

1. Make your way to **Settings -> Asterisk SIP Settings** in order to confirm your **network settings**.
2. You'll want to ensure you populate the **external** and **local** network addresses under **General SIP Settings** and **Chan SIP Settings**.
3. Click **Submit** and then **Apply Config.**

   [![SIP settings page. ](https://downloads.intercomcdn.com/i/o/371697572/e476b66d413bf486b78b9ad9/image.png?expires=1781168400&signature=f0b1cbe67b777b8b874ae27901065b9987a5b8b405e262e56951b44641f04028&req=dycmEMB5mIZdFb4f3HP0gK%2BzENCyhQSm3sDQWwrh6%2FwbCW%2BAIA9%2FxldI9SMk%0AwQw%3D%0A)](https://downloads.intercomcdn.com/i/o/371697572/e476b66d413bf486b78b9ad9/image.png?expires=1781168400&signature=f0b1cbe67b777b8b874ae27901065b9987a5b8b405e262e56951b44641f04028&req=dycmEMB5mIZdFb4f3HP0gK%2BzENCyhQSm3sDQWwrh6%2FwbCW%2BAIA9%2FxldI9SMk%0AwQw%3D%0A)

[Back to Top](#h_e22b63eb98)

## 4. Configure Extensions for your Free PBX

In this section, you'll configure all your PJSIP extensions.

1. Make your way to **Applications -> Extensions -> Add Extension -> Add New Chan SIP Extension.** The **Outbound CID** is the [number you purchased](https://portal.telnyx.com/#/app/numbers/my-numbers) from your Telnyx Mission Control Portal. The extensions secret may need to be populated under the **Other** tab.

   [![SIP extensions credentials page. ](https://downloads.intercomcdn.com/i/o/371705263/1b06c4567a19e09ac142ab42/image.png?expires=1781168400&signature=46cfa4e22ecb55d68c5356f64feb58a896062800a5896485f215b48f34698eda&req=dycmEcl7n4dcFb4f3HP0gOEVajEjKHSjDB7HSCrmtxC0JAhOuwlN8gYkJwHj%0A%2B9U%3D%0A)](https://downloads.intercomcdn.com/i/o/371705263/1b06c4567a19e09ac142ab42/image.png?expires=1781168400&signature=46cfa4e22ecb55d68c5356f64feb58a896062800a5896485f215b48f34698eda&req=dycmEcl7n4dcFb4f3HP0gOEVajEjKHSjDB7HSCrmtxC0JAhOuwlN8gYkJwHj%0A%2B9U%3D%0A)

   ***Note*** *that if you do not set an Outbound CID for your extension, you will need to enable this on your trunk.*  
   ​  
   ​***Note*** *that this device uses CHAN\_SIP technology listening on Port 5160 (UDP - this is a NON STANDARD port).*  
   ​
2. Click **Submit** and **Apply Config.**

For testing purposes, you can now use your SIP client to register with FreePBX using the username, password/secret and local IP address of your FreePBX.

[Back to Top](#h_e22b63eb98)

## 5. Configure a Trunk for your FreePBX

1. Make your way to **Connectivity -> Trunks -> Add Trunk -> Add New Chan SIP Trunk.** You'll now be located in the **General** tab.
2. Enter a Trunk name, your Outbound CID and the maximum channels you'd like for this trunk.

   [![General Connectivity settings tab. ](https://downloads.intercomcdn.com/i/o/399026883/62cccb32daa8bb361769eb61/Screenshot+from+2021-10-05+13-56-14.png?expires=1781168400&signature=4f24de459947d0776eb8402cb6e74c19d14a24a64cbb2cfec01e8b3f28588a9a&req=dykuFst4lYlcFb4f3HP0gJh8CESR54m3NN5loLvz7bJAUVsfje0FoQtF%2BSBS%0ANlk%3D%0A)](https://downloads.intercomcdn.com/i/o/399026883/62cccb32daa8bb361769eb61/Screenshot+from+2021-10-05+13-56-14.png?expires=1781168400&signature=4f24de459947d0776eb8402cb6e74c19d14a24a64cbb2cfec01e8b3f28588a9a&req=dykuFst4lYlcFb4f3HP0gJh8CESR54m3NN5loLvz7bJAUVsfje0FoQtF%2BSBS%0ANlk%3D%0A)

   ***Note****: If you choose not to set an Outbound CID on your trunk, then you must set an Outbound CID on each relevant extension. If you do not set a caller ID on either the trunk or each extension, then your calls will reach our SIP proxy without a valid caller ID. You may instead choose to enable a Caller ID Override in your SIP Connection’s Outbound Options from within the Telnyx Portal. Please review our [caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy) for accepted formats.*  
   ​
3. Proceed to the **Dialed Number Manipulation Rules** tab. Depending on your use case, we've provided a simple dial pattern US numbers below.

   [![Trunk Addition page. ](https://downloads.intercomcdn.com/i/o/398953812/06ecfbc64f66c6b2b86a1dcc/Screenshot+from+2021-10-05+11-49-41.png?expires=1781168400&signature=a0e2d2d3d59c8cd437fa5a936a10e2425e7affd4aa7411a903c3a249beaf0b62&req=dykvH8x9lYBdFb4f3HP0gN0a1fQaz%2FHTJlLvi8AS2GCYxYG8I3c0Trbg8L%2FA%0AkOg%3D%0A)](https://downloads.intercomcdn.com/i/o/398953812/06ecfbc64f66c6b2b86a1dcc/Screenshot+from+2021-10-05+11-49-41.png?expires=1781168400&signature=a0e2d2d3d59c8cd437fa5a936a10e2425e7affd4aa7411a903c3a249beaf0b62&req=dykvH8x9lYBdFb4f3HP0gN0a1fQaz%2FHTJlLvi8AS2GCYxYG8I3c0Trbg8L%2FA%0AkOg%3D%0A)

   **For US numbers:**

   1. prepend:*1*; match pattern: *NXXNXXXXXX*
   2. prepend: blank; match pattern: *1NXXNXXXXXX*

   **International:**

   1. prepend: Country Dialing prefix; match pattern: *NXXNXXXXXX*
   2. prepend:blank; match pattern: (Country Dialing prefix)*NXXNXXXXXX*

[Back to Top](#h_e22b63eb98)

## 6. Configure Outbound and Inbound Settings for your FreePBX

1. Still in the **Add Trunk** configuration tool, Click on the **SIP Settings** tab and click on the **Outgoing** sub-tab. Make sure to specify:

   1. **username:**your\_sip\_connection\_credentials\_based\_telnyx\_username
   2. **secret:**your\_sip\_connection\_credentials\_based\_telnyx\_password
   3. **type:** *friend*
   4. **qualify:** yes
   5. **insecure:** *port,invite*
   6. **host:** *sip.telnyx.com*
   7. **fromdomain:** *sip.telnyx.com*
   8. **disallow:** *all*
   9. **allow:** *ulaw*

      [![SIP settings tab. ](https://downloads.intercomcdn.com/i/o/371718541/5775bb835fbf005aec343119/image.png?expires=1781168400&signature=d37f16170b970593f324e2eca5d79f2acd0ddf7b4cb4534d947b149c88ecedfe&req=dycmEch2mIVeFb4f3HP0gGFXmDOuGl2g%2FV%2FjdRw%2BJ3YY6nTQqQp6iRNmc2G1%0A6Cc%3D%0A)](https://downloads.intercomcdn.com/i/o/371718541/5775bb835fbf005aec343119/image.png?expires=1781168400&signature=d37f16170b970593f324e2eca5d79f2acd0ddf7b4cb4534d947b149c88ecedfe&req=dycmEch2mIVeFb4f3HP0gGFXmDOuGl2g%2FV%2FjdRw%2BJ3YY6nTQqQp6iRNmc2G1%0A6Cc%3D%0A)
2. Now click on the Incoming sub-tab. Make sure to specify:

   1. **username:**your\_sip\_connection\_credentials\_based\_telnyx\_username
   2. **secret:**your\_sip\_connection\_credentials\_based\_telnyx\_password
   3. **type:** *friend*
   4. **insecure:** *port,invite*
   5. **host:** *sip.telnyx.com*
   6. **dtmfmode:** *rfc2833*
   7. **disallow:** *all*
   8. **allow:** *ulaw*
   9. **Register String:**  
      your\_sip\_connection\_credentials\_based\_telnyx\_username:your\_sip\_connection\_credentials\_based\_telnyx\_password*@sip.telnyx.com*/your\_sip\_connection\_credentials\_based\_telnyx\_username   
      ​

      Example: *Eliza1234:[mypassword123@sip.telnyx.com](mailto:mypassword123@sip.telnyx.com)/Eliza1234*

      [![Incoming sub tab. ](https://downloads.intercomcdn.com/i/o/371720304/e8621017054f676a8864f84a/image.png?expires=1781168400&signature=ebc1e81e27ee7308a5dde0990d1e19a7d5b5c6b85658f196cd221398ddd1cf1a&req=dycmEct%2BnoFbFb4f3HP0gIQMbQ6OrtsxkHOuL7IPskaMdKLpRF%2BITGMj0Zid%0AgXI%3D%0A)](https://downloads.intercomcdn.com/i/o/371720304/e8621017054f676a8864f84a/image.png?expires=1781168400&signature=ebc1e81e27ee7308a5dde0990d1e19a7d5b5c6b85658f196cd221398ddd1cf1a&req=dycmEct%2BnoFbFb4f3HP0gIQMbQ6OrtsxkHOuL7IPskaMdKLpRF%2BITGMj0Zid%0AgXI%3D%0A)

[Back to Top](#h_e22b63eb98)

## 7. Configure outbound routing

1. Make your way to **Connectivity > Outbound Routes > Add Outbound Route.**
2. Enter the route name, route CID and specify the Telnyx\_IP trunk for this outbound route.

   [![Outbound routes settings. ](https://downloads.intercomcdn.com/i/o/371722743/0b6e9bd339b5dc3d62ee9bc0/image.png?expires=1781168400&signature=f8e7a713a686607e37d7e4404ea141d77ea15d35f8d792caca863011d46056bd&req=dycmEct8moVcFb4f3HP0gCSnPXItHCe6eAd88yMRPKNsNc7dLiIx0STuihjy%0AKgo%3D%0A)](https://downloads.intercomcdn.com/i/o/371722743/0b6e9bd339b5dc3d62ee9bc0/image.png?expires=1781168400&signature=f8e7a713a686607e37d7e4404ea141d77ea15d35f8d792caca863011d46056bd&req=dycmEct8moVcFb4f3HP0gCSnPXItHCe6eAd88yMRPKNsNc7dLiIx0STuihjy%0AKgo%3D%0A)
3. Click **Submit** and **Apply Config**.

[Back to Top](#h_e22b63eb98)

## 8. Configure inbound routing

1. Make your way to **Connectivity -> Inbound Routes -> Add Inbound Route.**
2. Enter the route name description, DID associated with this route and specify the extension that should be associated when calls are received to the DID.
3. Click **Submit** and **Apply Config**.

|  |
| --- |
| ***NOTE:*** *By default, when creating a SIP Connection in the Telnyx Mission Control Portal, the number formats for the ANI and DNIS will be set to E.164. This means Telnyx will send the dialled number in the SIP INVITE to your FreePBX system with 11 digits. As the [DID number](https://telnyx.com/resources/sip-did) above is in 11 digit format, the call will be accepted and routed to the extension. However, you can control the number formats as you desire and can read more about it* [here](https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats). |

That's it, you've now completed the configuration of FreePBX V15 IP Trunk and can now make and receive calls by using Telnyx as your SIP provider!

[Back to Top](#h_e22b63eb98)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* FreePBX's [help section](https://www.freepbx.org/support/) for community or paid support
* [FreePBX support](https://www.freepbx.org/support/)
* [FreePBX documentation](https://wiki.freepbx.org/#all-updates)

---

---

Related Articles

[Configuring a FreePBX V13 Credentials Trunk](https://support.telnyx.com/en/articles/1130648-configuring-a-freepbx-v13-credentials-trunk)[FreePBX V14: IP Trunk - ChanSIP](https://support.telnyx.com/en/articles/3284736-freepbx-v14-ip-trunk-chansip)[FreePBX V14: Credentials - ChanSIP](https://support.telnyx.com/en/articles/3284752-freepbx-v14-credentials-chansip)[FreePBX V15: IP Trunk - PJSIP](https://support.telnyx.com/en/articles/5619595-freepbx-v15-ip-trunk-pjsip)[FreePBX V15: Credentials - PJSIP](https://support.telnyx.com/en/articles/5619597-freepbx-v15-credentials-pjsip)

Did this answer your question?

😞😐😃

Table of contents
