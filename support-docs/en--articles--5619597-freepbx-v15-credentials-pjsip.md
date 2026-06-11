---
source_url: https://support.telnyx.com/en/articles/5619597-freepbx-v15-credentials-pjsip
scraped: 2026-06-11
---

FreePBX V15: Credentials - PJSIP | Telnyx Help Center

[Skip to main content](#main-content)

# FreePBX V15: Credentials - PJSIP

Learn how to configure a FreePBX V15 Credentials trunk with Telnyx using PJSIP

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_ee68fbb156)

[FreePBX](https://www.freepbx.org/) is a web-based open source GUI (graphical user interface) that controls and manages Asterisk (PBX), an open source communication server. FreePBX is licensed under the GNU General Public License (GPL), an open source license. FreePBX can be installed manually or as part of the pre-configured FreePBX Distro that includes the system OS, Asterisk, FreePBX GUI and assorted dependencies.

PJSIP is an Open Source and separate extension of the Asterisk, and Asterisk derived systems. It provides a resource for assigning multiple trunks via SRV addresses, and more options. PJSIP also provides three main components of real-time multimedia application, i.e. signaling, media features, and NAT traversal, among other things that have been taken care of by PJSIP.  
​  
We suggest using PJSIP as an upgrade from Chan\_SIP, as Chan\_SIP is outdated, and the majority of users are moving to PJSIP which provides a number of more future proof options, and is still actively being improved by the community. You can find out more about PJSIP [here](https://www.pjsip.org/about.htm).

Additional documentation and resoruces:

* [FreePBX support](https://www.freepbx.org/support/)
* [FreePBX documentation](https://wiki.freepbx.org/#all-updates)

---

# Instructions for Configuring a FreePBX V15 IP Trunk

In this activity you will:

1. [Install your FreePBX V15](#h_dd13d72ed9)
2. [Configure basic settings for your FreePBX](#h_41d7ce2c98)
3. [Configure SIP settings for your FreePBX](#h_f876525ce3)
4. [Configure extensions for your FreePBX](#h_07f98572d9)
5. [Configure a trunk for your FreePBX](#h_1c0d414098)
6. [Configure PJSIP outbound settings for your FreePBX](#h_c6fc4bb6f1)
7. [Set up call routing on your FreePBX](#h_f472c381df)

## Pre-requisites

* [Download](https://www.freepbx.org/downloads/) and [install](https://sangomakb.atlassian.net/wiki/spaces/PP/pages/10682958/PBX+Platforms+Home) FreePBX V15
* [Configure your Telnyx Mission Control Portal](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* [Purchase a DID](https://portal.telnyx.com/#/app/numbers/search-numbers)
* [Set up your Telnyx SIP connection](https://portal.telnyx.com/#/app/connections)
* [Provision your number](https://portal.telnyx.com/#/app/numbers/my-numbers) (Assign it to a SIP connection)
* [Create an outbound voice profile](https://portal.telnyx.com/#/app/outbound)
* Create a [credentials-based connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)

## Video Walkthrough

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for FreePBX/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Install your FreePBX V15

In this section, you'll go through the steps you need to follow to install FreePBX.

1. ### **Once you load the ISO onto your server or virtual machine, you'll have a few options to select for installation. We'll be doing a full install via asterisk 16.**

   [![A loaded virtual machine/server. ](https://downloads.intercomcdn.com/i/o/371234430/f3e6e9f02a3b075254e2c15f/image.png?expires=1781168400&signature=f53009d6b6319b3254b0afc55aa8b6a035dd43a0babebc53700f9d580846a78c&req=dycmFMp6mYJfFb4f3HP0gFuv0SS6y4Kye2wXVfOT%2BG4qKplLC5mLanWnImrY%0AHOY%3D%0A)](https://downloads.intercomcdn.com/i/o/371234430/f3e6e9f02a3b075254e2c15f/image.png?expires=1781168400&signature=f53009d6b6319b3254b0afc55aa8b6a035dd43a0babebc53700f9d580846a78c&req=dycmFMp6mYJfFb4f3HP0gFuv0SS6y4Kye2wXVfOT%2BG4qKplLC5mLanWnImrY%0AHOY%3D%0A)
2. ### **You'll be prompted for your preferred video method you want to install.**

   [![Video method selection tab. ](https://downloads.intercomcdn.com/i/o/371750617/f3e85ba2df6cef3ef3c26aa3/image.png?expires=1781168400&signature=1e33d0e58cb5860c15beb800886fb581b1aab9414908aa3e08ec144568049aec&req=dycmEcx%2Bm4BYFb4f3HP0gE4mffVk4LV3LXl20bY9qzWj%2FCAv17kPH9THhgtm%0AmhI%3D%0A)](https://downloads.intercomcdn.com/i/o/371750617/f3e85ba2df6cef3ef3c26aa3/image.png?expires=1781168400&signature=1e33d0e58cb5860c15beb800886fb581b1aab9414908aa3e08ec144568049aec&req=dycmEcx%2Bm4BYFb4f3HP0gE4mffVk4LV3LXl20bY9qzWj%2FCAv17kPH9THhgtm%0AmhI%3D%0A)
3. ### **The installer will now start.**

   [![Active installer. ](https://downloads.intercomcdn.com/i/o/371237494/f768024c66e5720d3ebb5295/image.png?expires=1781168400&signature=fe5b090941d20759b3eb722be3909d9b9c35abc49a1bc1a90664d4779e372cd5&req=dycmFMp5mYhbFb4f3HP0gAzIDy6qpL%2BQDewNsmXgJmzdApoor4m9xioFeBML%0A5Q0%3D%0A)](https://downloads.intercomcdn.com/i/o/371237494/f768024c66e5720d3ebb5295/image.png?expires=1781168400&signature=fe5b090941d20759b3eb722be3909d9b9c35abc49a1bc1a90664d4779e372cd5&req=dycmFMp5mYhbFb4f3HP0gAzIDy6qpL%2BQDewNsmXgJmzdApoor4m9xioFeBML%0A5Q0%3D%0A)
4. ### **You'll notice that the root password is not set. You will need to click on the root password box to set your root password. The installation process can not complete until this is done.**

   [![Installer root password settings. ](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600450/6a1dfe8e806d827c5e130fa6/Screen-20Shot-202017-07-20-20at-2010.39.35-20AM.png?expires=1781168400&signature=74a1b67621d185c586f65d0edc749999b80006ca4e0097dc933f01ea602d197f&req=dSQkEMl%2BmYRfFb4f3HP0gF4h0payer9G1OiGQWpPaz9G%2FIAhhHwGrXxwQMN7%0Afzw%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600450/6a1dfe8e806d827c5e130fa6/Screen-20Shot-202017-07-20-20at-2010.39.35-20AM.png?expires=1781168400&signature=74a1b67621d185c586f65d0edc749999b80006ca4e0097dc933f01ea602d197f&req=dSQkEMl%2BmYRfFb4f3HP0gF4h0payer9G1OiGQWpPaz9G%2FIAhhHwGrXxwQMN7%0Afzw%3D%0A)
5. ### **Type in your root password and confirm it a second time and click on the Done option in the top left screen.**

   [![Root password confirmation. ](https://downloads.intercomcdn.com/i/o/371239957/cb48106a43b8b94afb54f88e/image.png?expires=1781168400&signature=09dac023e5f08fe38fa9f8693e9250c30c5e90f186e4adf83d6e2b13e24da94b&req=dycmFMp3lIRYFb4f3HP0gAQZOGiZjcXtsAa2IV%2B56OJ6asT1FbxuCLJIgb4S%0AaF8%3D%0A)](https://downloads.intercomcdn.com/i/o/371239957/cb48106a43b8b94afb54f88e/image.png?expires=1781168400&signature=09dac023e5f08fe38fa9f8693e9250c30c5e90f186e4adf83d6e2b13e24da94b&req=dycmFMp3lIRYFb4f3HP0gAQZOGiZjcXtsAa2IV%2B56OJ6asT1FbxuCLJIgb4S%0AaF8%3D%0A)
6. ### **At this time the FreePBX package itself can take 15 or more minutes to install and does requires access to the internet so depending on your internet speeds it can take awhile to install so be patient.**

   [![A page showing an ongoing FreePBX installation. ](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600456/7efa758314eb270ff69ef76f/Screen-20Shot-202017-07-20-20at-2010.58.19-20AM.png?expires=1781168400&signature=3f177fd1081900512b39434e8cc3ab804ebf7af2afad7e15374f39503baea1ad&req=dSQkEMl%2BmYRZFb4f3HP0gLUmzG%2F1QjjZIzWcoZilEcoK1zPO8jmUS0FvU7lq%0AxLQ%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600456/7efa758314eb270ff69ef76f/Screen-20Shot-202017-07-20-20at-2010.58.19-20AM.png?expires=1781168400&signature=3f177fd1081900512b39434e8cc3ab804ebf7af2afad7e15374f39503baea1ad&req=dSQkEMl%2BmYRZFb4f3HP0gLUmzG%2F1QjjZIzWcoZilEcoK1zPO8jmUS0FvU7lq%0AxLQ%3D%0A)
7. ### **Once the install has 100% completed it will give you a reboot option as shown below. Click on reboot your your system is now installed.**

   [![A page showing a complete configuration. ](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600457/09b3e6f7404341e147d98a5e/Screen-20Shot-202017-07-20-20at-2011.19.53-20AM.png?expires=1781168400&signature=325c38228a91898a0a9e94563e94369598c180fc4f5a6d878f78ea501bf7691a&req=dSQkEMl%2BmYRYFb4f3HP0gGd9IMO2SDY6a48CZ7H0mHC3NhBi9K9St0IMQ0nt%0AZuE%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600457/09b3e6f7404341e147d98a5e/Screen-20Shot-202017-07-20-20at-2011.19.53-20AM.png?expires=1781168400&signature=325c38228a91898a0a9e94563e94369598c180fc4f5a6d878f78ea501bf7691a&req=dSQkEMl%2BmYRYFb4f3HP0gGd9IMO2SDY6a48CZ7H0mHC3NhBi9K9St0IMQ0nt%0AZuE%3D%0A)
8. ### **Once the process is complete, you'll reach the Linux console/command prompt login. You can log in here using the username "root" without quotes, and the Root password you selected earlier.**

   [![IP Address tab. ](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600459/9eaf327f9aed4991ba67981e/Screen-20Shot-202017-07-20-20at-2011.58.00-20AM.png?expires=1781168400&signature=b206bacc5fc395bfc087fe3d7e6e8fae29026057a38bedb76b9c66d4432d6f4c&req=dSQkEMl%2BmYRWFb4f3HP0gLPD%2B8q3CmZZAMmnOnXcmK1Y%2FfduS6R4iAA%2BOTXD%0AB9A%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600459/9eaf327f9aed4991ba67981e/Screen-20Shot-202017-07-20-20at-2011.58.00-20AM.png?expires=1781168400&signature=b206bacc5fc395bfc087fe3d7e6e8fae29026057a38bedb76b9c66d4432d6f4c&req=dSQkEMl%2BmYRWFb4f3HP0gLPD%2B8q3CmZZAMmnOnXcmK1Y%2FfduS6R4iAA%2BOTXD%0AB9A%3D%0A)

   ###
9. ### **After you log in, you should see the IP address of your PBX as shown below. Take note of this IP address as you will need it in the next step.**

   [![IP address tab. ](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600460/cb485197bf2d00f58b6be3f2/Screen-20Shot-202017-07-20-20at-2011.57.27-20AM.png?expires=1781168400&signature=a1a0ac902f778c3d75a59751409a86bf6d1a5078e9ef0feb6dcaa1a4ad5c5c40&req=dSQkEMl%2BmYdfFb4f3HP0gJCNT4395ngW3GRHmTEZbC7w38%2BXBkLSDaosxZI9%0Ao%2FM%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600460/cb485197bf2d00f58b6be3f2/Screen-20Shot-202017-07-20-20at-2011.57.27-20AM.png?expires=1781168400&signature=a1a0ac902f778c3d75a59751409a86bf6d1a5078e9ef0feb6dcaa1a4ad5c5c40&req=dSQkEMl%2BmYdfFb4f3HP0gJCNT4395ngW3GRHmTEZbC7w38%2BXBkLSDaosxZI9%0Ao%2FM%3D%0A)
10. #### **Enter the IP address of the new PBX into your web browser. The first time you do so, you'll be asked to create the admin username and the admin password. That username and password will be used in the future to access the FreePBX configuration screen.** **Note:** These passwords do not change the Root password! They are only used for access to the FreePBX web interface.

    [![FreePBX support initial setup interface. ](https://downloads.intercomcdn.com/i/o/371682345/b542cbfa5a33996e3c37677b/image.png?expires=1781168400&signature=882a192ce4ef441af5b58a0430f0676fcd002a90fa0e053db9bb67fcaa73c280&req=dycmEMF8noVaFb4f3HP0gO8F%2BRtVpNphvE8fKz5%2BpYJEZvAM4uC0BFO6h0n7%0A1Bg%3D%0A)](https://downloads.intercomcdn.com/i/o/371682345/b542cbfa5a33996e3c37677b/image.png?expires=1781168400&signature=882a192ce4ef441af5b58a0430f0676fcd002a90fa0e053db9bb67fcaa73c280&req=dycmEMF8noVaFb4f3HP0gO8F%2BRtVpNphvE8fKz5%2BpYJEZvAM4uC0BFO6h0n7%0A1Bg%3D%0A)

[Back to Top](#h_ee68fbb156)

## 2. Configuring basic settings for your FreePBX

In this step, you'll configure your FreePBX V15 and connect it to Telnyx. To begin, notice that the main FreePBX screen will offer you four options:

[![FreePBX basic settings. ](https://downloads.intercomcdn.com/i/o/371686829/2e2dc2f528c30feb84c8f24c/image.png?expires=1781168400&signature=01710212a4d1efc6c11a36d48cf70f94632b14c8d397c9ddd079acee81f3ba3a&req=dycmEMF4lYNWFb4f3HP0gFX7ylpFUZTTghLR7lHwmQEEL0CwGZIPjswRG7bg%0AsB1Kd4WlvLYMKYysBQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/371686829/2e2dc2f528c30feb84c8f24c/image.png?expires=1781168400&signature=01710212a4d1efc6c11a36d48cf70f94632b14c8d397c9ddd079acee81f3ba3a&req=dycmEMF4lYNWFb4f3HP0gFX7ylpFUZTTghLR7lHwmQEEL0CwGZIPjswRG7bg%0AsB1Kd4WlvLYMKYysBQ%3D%3D%0A)

* **FreePBX Administration** will allow you to configure your PBX. Use the admin username and admin password you configured in the step above to login. This section is what most people refer to as "FreePBX."

* **User Control Panel** is where a user can log in to make web calls, set up their phone buttons, view voicemails, send and receive faxes, use SMS & XMPP messaging, view conferences, and more, depending on what you have enabled for the user, see [User Control Panel (UCP) 14+](https://wiki.freepbx.org/pages/viewpage.action?pageId=74318855) for more information.

* **Operator Panel** is a screen that allows an operator to control calls (needs additional licensing)

* **Get Support** takes you to a web page about various official support options for FreePBX.

1. Enter the username, password, and admin email address in order to create your account.

   [![Initial setup settings interface.](https://downloads.intercomcdn.com/i/o/371682345/b542cbfa5a33996e3c37677b/image.png?expires=1781168400&signature=882a192ce4ef441af5b58a0430f0676fcd002a90fa0e053db9bb67fcaa73c280&req=dycmEMF8noVaFb4f3HP0gO8F%2BRtVpNphvE8fKz5%2BpYJEZvAM4uC0BFO6h0n7%0A1Bg%3D%0A)](https://downloads.intercomcdn.com/i/o/371682345/b542cbfa5a33996e3c37677b/image.png?expires=1781168400&signature=882a192ce4ef441af5b58a0430f0676fcd002a90fa0e053db9bb67fcaa73c280&req=dycmEMF8noVaFb4f3HP0gO8F%2BRtVpNphvE8fKz5%2BpYJEZvAM4uC0BFO6h0n7%0A1Bg%3D%0A)
2. Once you've created your account, you'll be brought to the dashboard. Select **FreePBX Administration** and enter your username and password.
3. Follow the process to activate your FreePBX V15.

   [![FreePBX server welcome page.](https://downloads.intercomcdn.com/i/o/371690168/5184de3771cc9ed8849b612e/image.png?expires=1781168400&signature=bfa6fb9b95cd41e40ee98aa17ced8bdd8d6b8b9c007a899eee3261306d75ed9c&req=dycmEMB%2BnIdXFb4f3HP0gFNF0Btjc7BZVSiqH5buLz8yssKx71QQwYHCbqQ2%0ABD8%3D%0A)](https://downloads.intercomcdn.com/i/o/371690168/5184de3771cc9ed8849b612e/image.png?expires=1781168400&signature=bfa6fb9b95cd41e40ee98aa17ced8bdd8d6b8b9c007a899eee3261306d75ed9c&req=dycmEMB%2BnIdXFb4f3HP0gFNF0Btjc7BZVSiqH5buLz8yssKx71QQwYHCbqQ2%0ABD8%3D%0A)

   1. Select your default locales.

      [![Default locales settings. ](https://downloads.intercomcdn.com/i/o/371692642/306870ad1740ec770a45f39d/image.png?expires=1781168400&signature=470bae47dc0cc65164dd526b635d30e36eba898f596ade0765cec51029ec2327&req=dycmEMB8m4VdFb4f3HP0gOtFlqfIw%2F3vwlsLA2Y91717crVjNOGFwHlqZMs%2B%0ADcE%3D%0A)](https://downloads.intercomcdn.com/i/o/371692642/306870ad1740ec770a45f39d/image.png?expires=1781168400&signature=470bae47dc0cc65164dd526b635d30e36eba898f596ade0765cec51029ec2327&req=dycmEMB8m4VdFb4f3HP0gOtFlqfIw%2F3vwlsLA2Y91717crVjNOGFwHlqZMs%2B%0ADcE%3D%0A)
   2. You'll be presented with some firewall details and other suggestions. You are welcome to set this up based on your requirements.
   3. Once you're back at the dashboard, you'll see more detail.

      [![FreePBX dashboard. ](https://downloads.intercomcdn.com/i/o/371694374/30dfd033ce49665b12e68e36/image.png?expires=1781168400&signature=35196af0f31fa1b0de2e9eaf368b635b376c866d7da7cc8435ba1fcab7162b98&req=dycmEMB6noZbFb4f3HP0gGUdBjMUW%2F%2BO560BfuEgobUw9gkYyMz5cdNhWSqs%0AESU%3D%0A)](https://downloads.intercomcdn.com/i/o/371694374/30dfd033ce49665b12e68e36/image.png?expires=1781168400&signature=35196af0f31fa1b0de2e9eaf368b635b376c866d7da7cc8435ba1fcab7162b98&req=dycmEMB6noZbFb4f3HP0gGUdBjMUW%2F%2BO560BfuEgobUw9gkYyMz5cdNhWSqs%0AESU%3D%0A)

   ​

[Back to Top](#h_ee68fbb156)

## 3. Configuring SIP settings for your FreePBX

At this point you can now work on confirming network settings and configuring your [SIP trunks](https://telnyx.com/products/sip-trunks) and extensions.

1. Make your way to **Settings -> Asterisk SIP Settings** in order to confirm your **network settings**.
2. You'll want to ensure you populate the **external** and **local** network addresses under **General SIP Settings** and **PJSIP Settings**.
3. Click **Submit** and then **Apply Config.**

   [![Asterisk SIP settings. ](https://downloads.intercomcdn.com/i/o/371697572/e476b66d413bf486b78b9ad9/image.png?expires=1781168400&signature=f0b1cbe67b777b8b874ae27901065b9987a5b8b405e262e56951b44641f04028&req=dycmEMB5mIZdFb4f3HP0gK%2BzENCyhQSm3sDQWwrh6%2FwbCW%2BAIA9%2FxldI9SMk%0AwQw%3D%0A)](https://downloads.intercomcdn.com/i/o/371697572/e476b66d413bf486b78b9ad9/image.png?expires=1781168400&signature=f0b1cbe67b777b8b874ae27901065b9987a5b8b405e262e56951b44641f04028&req=dycmEMB5mIZdFb4f3HP0gK%2BzENCyhQSm3sDQWwrh6%2FwbCW%2BAIA9%2FxldI9SMk%0AwQw%3D%0A)

[Back to Top](#h_ee68fbb156)

## 4. Configure Extensions for your Free PBX

In this section, you'll configure all your PJSIP extensions.

1. Make your way to **Applications -> Extensions -> Add Extension -> Add New Chan PJSIP Extension.** The **Outbound CID** is the [number you purchased](https://portal.telnyx.com/#/app/numbers/my-numbers) from your Telnyx Mission Control Portal. The extensions secret may need to be populated under the **Other** tab.

   [![Applications settings. ](https://downloads.intercomcdn.com/i/o/398948735/4a1641fdf8da99bbe4446ae7/Screenshot+from+2021-10-05+11-40-03.png?expires=1781168400&signature=37e1bcafb9acbac4dc445ef92103806394e97afe0d5a02645a1369d1e864aa90&req=dykvH812moJaFb4f3HP0gBC9bSoHhV7D3A4bzAxYMe5SpHWmKWJnLUOPmAuw%0Aab0%3D%0A)](https://downloads.intercomcdn.com/i/o/398948735/4a1641fdf8da99bbe4446ae7/Screenshot+from+2021-10-05+11-40-03.png?expires=1781168400&signature=37e1bcafb9acbac4dc445ef92103806394e97afe0d5a02645a1369d1e864aa90&req=dykvH812moJaFb4f3HP0gBC9bSoHhV7D3A4bzAxYMe5SpHWmKWJnLUOPmAuw%0Aab0%3D%0A)

   ***Note that*** *if you do not set an Outbound CID for your extension, you will need to enable this on your trunk.*  
   ​  
   This device uses **PJSIP** technology listening on Port 5060 (UDP)  
   ​
2. Click **Submit** and **Apply Config.**

   [![PJSIP addition extension. ](https://downloads.intercomcdn.com/i/o/398950563/9361fbf8595850c5cabfa9e2/Screenshot+from+2021-10-05+11-43-32.png?expires=1781168400&signature=1861342c1d6af1bce206675a0c6f71aa06319fb1edc8dd2eb8a386313bfffc67&req=dykvH8x%2BmIdcFb4f3HP0gJbyn%2BeIuYX1AyUOPvAot1lXEkRRj7zc58fUxVwm%0A210%3D%0A)](https://downloads.intercomcdn.com/i/o/398950563/9361fbf8595850c5cabfa9e2/Screenshot+from+2021-10-05+11-43-32.png?expires=1781168400&signature=1861342c1d6af1bce206675a0c6f71aa06319fb1edc8dd2eb8a386313bfffc67&req=dykvH8x%2BmIdcFb4f3HP0gJbyn%2BeIuYX1AyUOPvAot1lXEkRRj7zc58fUxVwm%0A210%3D%0A)

For testing purposes, you can now use your SIP client to register with FreePBX using the username, password/secret and local IP address of your FreePBX.

##

[Back to Top](#h_ee68fbb156)

## 5. Configure a Trunk for your FreePBX

1. Make your way to **Connectivity -> Trunks -> Add Trunk -> Add New PJSIP Trunk.** You'll now be located in the **General** tab.
2. Enter a Trunk name, your Outbound CID and the maximum channels you'd like for this trunk.

   [![Trunk editing page. ](https://downloads.intercomcdn.com/i/o/399026883/62cccb32daa8bb361769eb61/Screenshot+from+2021-10-05+13-56-14.png?expires=1781168400&signature=4f24de459947d0776eb8402cb6e74c19d14a24a64cbb2cfec01e8b3f28588a9a&req=dykuFst4lYlcFb4f3HP0gJh8CESR54m3NN5loLvz7bJAUVsfje0FoQtF%2BSBS%0ANlk%3D%0A)](https://downloads.intercomcdn.com/i/o/399026883/62cccb32daa8bb361769eb61/Screenshot+from+2021-10-05+13-56-14.png?expires=1781168400&signature=4f24de459947d0776eb8402cb6e74c19d14a24a64cbb2cfec01e8b3f28588a9a&req=dykuFst4lYlcFb4f3HP0gJh8CESR54m3NN5loLvz7bJAUVsfje0FoQtF%2BSBS%0ANlk%3D%0A)

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

[Back to Top](#h_ee68fbb156)

## 6. Configure PJSIP Outbound Settings for your FreePBX

[![PJSIP settings in the trunk editing section. ](https://downloads.intercomcdn.com/i/o/399024964/a4d09d59f938bac5cb24c81b/Screenshot+from+2021-10-05+13-52-11.png?expires=1781168400&signature=9a6642e4585e25efbe1a2cf4159e93b364ace450c746b521e85d9c0ed0c14639&req=dykuFst6lIdbFb4f3HP0gIC2b5qzv46K9vv0MY0qmjmfnjx7iCX21R0zz4Bv%0AiNOeIhn58O6GMbqFbg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/399024964/a4d09d59f938bac5cb24c81b/Screenshot+from+2021-10-05+13-52-11.png?expires=1781168400&signature=9a6642e4585e25efbe1a2cf4159e93b364ace450c746b521e85d9c0ed0c14639&req=dykuFst6lIdbFb4f3HP0gIC2b5qzv46K9vv0MY0qmjmfnjx7iCX21R0zz4Bv%0AiNOeIhn58O6GMbqFbg%3D%3D%0A)

1. Make sure to specify:

   1. **Username**: as the credential based SIP Connections username from your Telnyx account.
   2. **Auth Username**: as the credential based SIP Connections username from your Telnyx account.
   3. **Secret:** as the credential based SIP Connections password from your Telnyx account.
   4. **SIP Server**: as your preferred Telnyx SIP Proxy (*sip.telnyx.com* in this instance for USA).
   5. **SIP Server Port:** *5060* if you are using UDP or TCP transport. *5061* if you are using TLS transport.

      [![PJSP settings configuration. ](https://downloads.intercomcdn.com/i/o/398967375/97bc7bf927b6bb6cf011558f/Screenshot+from+2021-10-05+12-11-21.png?expires=1781168400&signature=c70957a238f669f056f14e370dbeed8eabc5be70747360f475a61f3209800e52&req=dykvH895noZaFb4f3HP0gFYYuRWh%2Fu8LN3ZslXGN2GskusehyD%2Bo8csAKTbg%0AgOA%3D%0A)](https://downloads.intercomcdn.com/i/o/398967375/97bc7bf927b6bb6cf011558f/Screenshot+from+2021-10-05+12-11-21.png?expires=1781168400&signature=c70957a238f669f056f14e370dbeed8eabc5be70747360f475a61f3209800e52&req=dykvH895noZaFb4f3HP0gFYYuRWh%2Fu8LN3ZslXGN2GskusehyD%2Bo8csAKTbg%0AgOA%3D%0A)
2. Click **Submit** and **Apply Config.**
3. You might see something like "**WARNING**: This trunk is not used by any routes! This trunk will not be able to be used for outbound calls until a route is setup that uses it."

[Back to Top](#h_ee68fbb156)

## 7. Set up call routing on your FreePBX

1. Make your way to **Connectivity -> Outbound Routes -> Add Outbound Route**

   [![Outbound routes section. ](https://downloads.intercomcdn.com/i/o/398972024/0c264b149def8ec7f2e361cc/Screenshot+from+2021-10-05+12-21-18.png?expires=1781168400&signature=3ead311731a005b2fbff69d98a12728c01c52f865cb2e6aae2380c430253e6aa&req=dykvH858nYNbFb4f3HP0gDdrE%2B1yQCdgT85MwWijHfsGuwzpLxVYOtaEoRYB%0Azuk%3D%0A)](https://downloads.intercomcdn.com/i/o/398972024/0c264b149def8ec7f2e361cc/Screenshot+from+2021-10-05+12-21-18.png?expires=1781168400&signature=3ead311731a005b2fbff69d98a12728c01c52f865cb2e6aae2380c430253e6aa&req=dykvH858nYNbFb4f3HP0gDdrE%2B1yQCdgT85MwWijHfsGuwzpLxVYOtaEoRYB%0Azuk%3D%0A)
2. In **Route Settings:**

   1. Set the route name
   2. Ensure *Telnyx Trunk* is selected for the trunk sequence

      [![Outbound routes for Telnyx trunk. ](https://downloads.intercomcdn.com/i/o/399028847/a5724363793b3c4692aef0f9/Screenshot+from+2021-10-05+13-58-20.png?expires=1781168400&signature=46e834715396b4f9471768a326fd82b2b7906e57c13973138ccd475ab9a56103&req=dykuFst2lYVYFb4f3HP0gKjlpRtEl1iQIuTSKza%2F9ZQ5rHt6abiMpBdazkr3%0ActY%3D%0A)](https://downloads.intercomcdn.com/i/o/399028847/a5724363793b3c4692aef0f9/Screenshot+from+2021-10-05+13-58-20.png?expires=1781168400&signature=46e834715396b4f9471768a326fd82b2b7906e57c13973138ccd475ab9a56103&req=dykuFst2lYVYFb4f3HP0gKjlpRtEl1iQIuTSKza%2F9ZQ5rHt6abiMpBdazkr3%0ActY%3D%0A)
3. In **Dial Patterns:**

   1. Use the dial pattern wizards to make all the dial patterns that apply to you.

      [![Dial patterns for Telnyx. ](https://downloads.intercomcdn.com/i/o/398974582/36270634490f0ecc3f110da6/Screenshot+from+2021-10-05+12-28-53.png?expires=1781168400&signature=1af305b84e2c2d025ee7baa71625e95796c09bd172828b42439d75c41867a1ba&req=dykvH856mIldFb4f3HP0gFRdUsy%2B54VKtqy671OIAeZ2sP4t%2F6xZNwOLWwmM%0AwDc%3D%0A)](https://downloads.intercomcdn.com/i/o/398974582/36270634490f0ecc3f110da6/Screenshot+from+2021-10-05+12-28-53.png?expires=1781168400&signature=1af305b84e2c2d025ee7baa71625e95796c09bd172828b42439d75c41867a1ba&req=dykvH856mIldFb4f3HP0gFRdUsy%2B54VKtqy671OIAeZ2sP4t%2F6xZNwOLWwmM%0AwDc%3D%0A)
4. Click **Generate Routes, Submit** and **Apply Config.**
5. Now make your way to **Connectivity -> Inbound Routes -> Add Inbound Route.**
6. Enter the route name description, DID associated with this route and specify the **extension** that should be associated when calls are received to the DID.

   [![Inbound routes for incoming routes. ](https://downloads.intercomcdn.com/i/o/398986299/425b10dde71f5024e7eb1a6e/Screenshot+from+2021-10-05+12-36-35.png?expires=1781168400&signature=2fcd9ce34d48cb3e6aad8cfac4a91c809cccae34affef568154ba5de5a23b524&req=dykvH8F4n4hWFb4f3HP0gI7Iw0Zg0j5dFQtIIBmROeX147ZG2Oz98QGg32%2FN%0AWN4%3D%0A)](https://downloads.intercomcdn.com/i/o/398986299/425b10dde71f5024e7eb1a6e/Screenshot+from+2021-10-05+12-36-35.png?expires=1781168400&signature=2fcd9ce34d48cb3e6aad8cfac4a91c809cccae34affef568154ba5de5a23b524&req=dykvH8F4n4hWFb4f3HP0gI7Iw0Zg0j5dFQtIIBmROeX147ZG2Oz98QGg32%2FN%0AWN4%3D%0A)
7. Click **Submit** and **Apply Config**.

|  |
| --- |
| ***Note:*** *By default, when creating a SIP Connection in the Telnyx Mission Control Portal, the number formats for the ANI and DNIS will be set to E.164. This means Telnyx will send the dialled number in the SIP INVITE to your FreePBX system with 11 digits. As the [DID number](https://telnyx.com/resources/sip-did) above is in 11 digit format, the call will be accepted and routed to the extension. However, you can control the number formats as you desire and can read more about it [here](https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats).* |

That's it, you've now completed the configuration of FreePBX V15 Credentials PJSIP Trunk and can now make and receive calls by using Telnyx as your SIP provider.  
​

[Back to Top](#h_ee68fbb156)

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

[Configuring a FreePBX V13 Credentials Trunk](https://support.telnyx.com/en/articles/1130648-configuring-a-freepbx-v13-credentials-trunk)[FreePBX V14: IP Trunk - ChanSIP](https://support.telnyx.com/en/articles/3284736-freepbx-v14-ip-trunk-chansip)[FreePBX V14: Credentials - ChanSIP](https://support.telnyx.com/en/articles/3284752-freepbx-v14-credentials-chansip)[Setting Up FreePBX V15 with Telnyx API](https://support.telnyx.com/en/articles/5464056-setting-up-freepbx-v15-with-telnyx-api)[FreePBX V15: IP Trunk - PJSIP](https://support.telnyx.com/en/articles/5619595-freepbx-v15-ip-trunk-pjsip)

Did this answer your question?

😞😐😃

Table of contents
