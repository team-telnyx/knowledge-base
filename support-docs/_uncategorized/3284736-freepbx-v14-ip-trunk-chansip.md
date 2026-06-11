---
source_url: https://support.telnyx.com/en/articles/3284736-freepbx-v14-ip-trunk-chansip
scraped: 2026-06-11
---

FreePBX V14: IP Trunk - ChanSIP | Telnyx Help Center

[Skip to main content](#main-content)

# FreePBX V14: IP Trunk - ChanSIP

Learn how to configure a FreePBX V14 IP trunk with Telnyx. Get started now.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_e1fc150ffb)

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

1. [Install your FreePBX V14](#h_496eea7cb1)
2. [Configure basic settings for your FreePBX](#h_038150c937)
3. [Configure SIP settings for your FreePBX](#h_0d1f8821d6)
4. [Configure extensions for your FreePBX](#h_70fac506bb)
5. [Configure a trunk for your FreePBX](#h_c6f1eb51f3)
6. [Configure outbound and inbound settings for your FreePBX](#h_e397d5e777)
7. [Configure outbound routing](#h_ebaba3c3ee)
8. [Configure inbound routing](#h_f5fb05f398)

**Pre-requisites**

* [Download](https://www.freepbx.org/downloads/) and [install](https://sangomakb.atlassian.net/wiki/spaces/PP/pages/10682958/PBX+Platforms+Home) FreePBX V14
* [Configure your Telnyx Mission Control Portal](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* [Set up an IP connection on your Telnyx Mission Control Portal](https://portal.telnyx.com/#/app/connections)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for FreePBX/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Install your FreePBX V14

In this section, you'll go through the steps you need to follow to install FreePBX.

1. ### **Once you load the ISO onto your server or virtual machine, you'll have a few options to select for installation. We'll be doing a full install via asterisk 16.**

   [![Installation Virtual Machine. ](https://downloads.intercomcdn.com/i/o/143599126/7e20880ad6fd62ab63420ffc/f1.png?expires=1781168400&signature=eea4a831494dc1d1d0772582e2a5c1d411d8771d73eaebaed29ad9b1ad9b4d29&req=dSQkE8B3nINZFb4f3HP0gJf4Ag8y1zUeddzjrtmJskre5D5PhgVKrSrvkQjV%0Ax2k%3D%0A)](https://downloads.intercomcdn.com/i/o/143599126/7e20880ad6fd62ab63420ffc/f1.png?expires=1781168400&signature=eea4a831494dc1d1d0772582e2a5c1d411d8771d73eaebaed29ad9b1ad9b4d29&req=dSQkE8B3nINZFb4f3HP0gJf4Ag8y1zUeddzjrtmJskre5D5PhgVKrSrvkQjV%0Ax2k%3D%0A)
2. ### **You'll be prompted for your preferred video method you want to install.**

   [![Installation Virtual Machine with preferred video options. ](https://downloads.intercomcdn.com/i/o/143599226/fae135d4a81eb80287c0392c/f2.png?expires=1781168400&signature=3fd96bfbaea8339705d7d244fabd2f6e518ae3b5909f9708d1c943dc7bf9304f&req=dSQkE8B3n4NZFb4f3HP0gJgkzhvnD9AP%2F7Wqc94Tp%2FRqy7mG5ftJxJMeWCX3%0A8xg%3D%0A)](https://downloads.intercomcdn.com/i/o/143599226/fae135d4a81eb80287c0392c/f2.png?expires=1781168400&signature=3fd96bfbaea8339705d7d244fabd2f6e518ae3b5909f9708d1c943dc7bf9304f&req=dSQkE8B3n4NZFb4f3HP0gJgkzhvnD9AP%2F7Wqc94Tp%2FRqy7mG5ftJxJMeWCX3%0A8xg%3D%0A)
3. ### **The installer will now start.**

   [![A running FreePBX installer. ](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600445/96ea8737fc3fd90b8fef9c32/Screen-20Shot-202017-07-20-20at-2010.38.13-20AM.png?expires=1781168400&signature=8bebddf24501e1a592e5672bf91c4aafdca5695e1499cbf8edfb3a2b12c48ddf&req=dSQkEMl%2BmYVaFb4f3HP0gMiet5kl1HErYeAJSmvFxuAzbClkRgU8lmvRXNPs%0Avdw%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600445/96ea8737fc3fd90b8fef9c32/Screen-20Shot-202017-07-20-20at-2010.38.13-20AM.png?expires=1781168400&signature=8bebddf24501e1a592e5672bf91c4aafdca5695e1499cbf8edfb3a2b12c48ddf&req=dSQkEMl%2BmYVaFb4f3HP0gMiet5kl1HErYeAJSmvFxuAzbClkRgU8lmvRXNPs%0Avdw%3D%0A)
4. ### **The installer will start but you will see it shows the root password is not set. You will need to click on the root password box to set your root password. The installation process can not complete until this is done.**

   [![Root password settings in the installer. ](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600450/6a1dfe8e806d827c5e130fa6/Screen-20Shot-202017-07-20-20at-2010.39.35-20AM.png?expires=1781168400&signature=74a1b67621d185c586f65d0edc749999b80006ca4e0097dc933f01ea602d197f&req=dSQkEMl%2BmYRfFb4f3HP0gF4h0payer9G1OiGQWpPaz9G%2FIAhhHwGrXxwQMN7%0Afzw%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600450/6a1dfe8e806d827c5e130fa6/Screen-20Shot-202017-07-20-20at-2010.39.35-20AM.png?expires=1781168400&signature=74a1b67621d185c586f65d0edc749999b80006ca4e0097dc933f01ea602d197f&req=dSQkEMl%2BmYRfFb4f3HP0gF4h0payer9G1OiGQWpPaz9G%2FIAhhHwGrXxwQMN7%0Afzw%3D%0A)
5. ### **Type in your root password and confirm it a second time and click on the Done option in the top left screen.**

   [![Root password credentials confirmation page. ](https://downloads.intercomcdn.com/i/o/371239957/cb48106a43b8b94afb54f88e/image.png?expires=1781168400&signature=09dac023e5f08fe38fa9f8693e9250c30c5e90f186e4adf83d6e2b13e24da94b&req=dycmFMp3lIRYFb4f3HP0gAQZOGiZjcXtsAa2IV%2B56OJ6asT1FbxuCLJIgb4S%0AaF8%3D%0A)](https://downloads.intercomcdn.com/i/o/371239957/cb48106a43b8b94afb54f88e/image.png?expires=1781168400&signature=09dac023e5f08fe38fa9f8693e9250c30c5e90f186e4adf83d6e2b13e24da94b&req=dycmFMp3lIRYFb4f3HP0gAQZOGiZjcXtsAa2IV%2B56OJ6asT1FbxuCLJIgb4S%0AaF8%3D%0A)
6. ### **At this time the FreePBX package itself can take 15 or more minutes to install and does requires access to the internet so depending on your internet speeds it can take awhile to install so be patient.**

   [![A running FreePBX package installer. ](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600456/7efa758314eb270ff69ef76f/Screen-20Shot-202017-07-20-20at-2010.58.19-20AM.png?expires=1781168400&signature=3f177fd1081900512b39434e8cc3ab804ebf7af2afad7e15374f39503baea1ad&req=dSQkEMl%2BmYRZFb4f3HP0gLUmzG%2F1QjjZIzWcoZilEcoK1zPO8jmUS0FvU7lq%0AxLQ%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600456/7efa758314eb270ff69ef76f/Screen-20Shot-202017-07-20-20at-2010.58.19-20AM.png?expires=1781168400&signature=3f177fd1081900512b39434e8cc3ab804ebf7af2afad7e15374f39503baea1ad&req=dSQkEMl%2BmYRZFb4f3HP0gLUmzG%2F1QjjZIzWcoZilEcoK1zPO8jmUS0FvU7lq%0AxLQ%3D%0A)
7. ### **Once the install has 100% completed it will give you a reboot option as shown below. Click on reboot your your system is now installed.**

   [![FreePBX package installer about to reboot. ](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600457/09b3e6f7404341e147d98a5e/Screen-20Shot-202017-07-20-20at-2011.19.53-20AM.png?expires=1781168400&signature=325c38228a91898a0a9e94563e94369598c180fc4f5a6d878f78ea501bf7691a&req=dSQkEMl%2BmYRYFb4f3HP0gGd9IMO2SDY6a48CZ7H0mHC3NhBi9K9St0IMQ0nt%0AZuE%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600457/09b3e6f7404341e147d98a5e/Screen-20Shot-202017-07-20-20at-2011.19.53-20AM.png?expires=1781168400&signature=325c38228a91898a0a9e94563e94369598c180fc4f5a6d878f78ea501bf7691a&req=dSQkEMl%2BmYRYFb4f3HP0gGd9IMO2SDY6a48CZ7H0mHC3NhBi9K9St0IMQ0nt%0AZuE%3D%0A)
8. ### **Once the process is complete, you'll reach the Linux console/command prompt login. You can log in here using the username "root" without quotes, and the Root password you selected earlier.**

   [![Linux/command prompt login interface. ](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600459/9eaf327f9aed4991ba67981e/Screen-20Shot-202017-07-20-20at-2011.58.00-20AM.png?expires=1781168400&signature=b206bacc5fc395bfc087fe3d7e6e8fae29026057a38bedb76b9c66d4432d6f4c&req=dSQkEMl%2BmYRWFb4f3HP0gLPD%2B8q3CmZZAMmnOnXcmK1Y%2FfduS6R4iAA%2BOTXD%0AB9A%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600459/9eaf327f9aed4991ba67981e/Screen-20Shot-202017-07-20-20at-2011.58.00-20AM.png?expires=1781168400&signature=b206bacc5fc395bfc087fe3d7e6e8fae29026057a38bedb76b9c66d4432d6f4c&req=dSQkEMl%2BmYRWFb4f3HP0gLPD%2B8q3CmZZAMmnOnXcmK1Y%2FfduS6R4iAA%2BOTXD%0AB9A%3D%0A)
9. ### **After you log in, you should see the IP address of your PBX as shown below. Take note of this IP address as you will need it in the next step.**

   [![Current network configuration settings page. ](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600460/cb485197bf2d00f58b6be3f2/Screen-20Shot-202017-07-20-20at-2011.57.27-20AM.png?expires=1781168400&signature=a1a0ac902f778c3d75a59751409a86bf6d1a5078e9ef0feb6dcaa1a4ad5c5c40&req=dSQkEMl%2BmYdfFb4f3HP0gJCNT4395ngW3GRHmTEZbC7w38%2BXBkLSDaosxZI9%0Ao%2FM%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600460/cb485197bf2d00f58b6be3f2/Screen-20Shot-202017-07-20-20at-2011.57.27-20AM.png?expires=1781168400&signature=a1a0ac902f778c3d75a59751409a86bf6d1a5078e9ef0feb6dcaa1a4ad5c5c40&req=dSQkEMl%2BmYdfFb4f3HP0gJCNT4395ngW3GRHmTEZbC7w38%2BXBkLSDaosxZI9%0Ao%2FM%3D%0A)
10. ### **Enter the IP address of the new PBX into your web browser. The first time you do so, you'll be asked to create the "admin username" and the "admin password". That username and password will be used in the future to access the FreePBX configuration screen.**

    #### Note: These passwords do not change the Root password! They are only used for access to the FreePBX web interface.

    [![FreePBX administration credentials page. ](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600462/6bb7ec3442d8b721dd202f39/Screen-20Shot-202017-07-20-20at-2011.58.40-20AM.png?expires=1781168400&signature=b61d8769eaca34f1fca6a0659ffec7df83565a4b78bbf5345eb6a20c2e385997&req=dSQkEMl%2BmYddFb4f3HP0gFpYnnjFcmWGoZBDK%2BVUPyYaBg3Yb%2FjqfRanMJQq%0AUyI%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600462/6bb7ec3442d8b721dd202f39/Screen-20Shot-202017-07-20-20at-2011.58.40-20AM.png?expires=1781168400&signature=b61d8769eaca34f1fca6a0659ffec7df83565a4b78bbf5345eb6a20c2e385997&req=dSQkEMl%2BmYddFb4f3HP0gFpYnnjFcmWGoZBDK%2BVUPyYaBg3Yb%2FjqfRanMJQq%0AUyI%3D%0A)
11. ### **Once submitted you can log in to the admin panel with the username and password set up on the step above.**

[Back to Top](#h_e1fc150ffb)

## 2. Configuring basic settings for your FreePBX

In this step, you'll configure your FreePBX V15 and connect it to Telnyx. To begin, notice that the main FreePBX screen will offer you four options:

[![FreePBX interface. ](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600466/37729d78058a1170722533ce/Screen-20Shot-202014-05-29-20at-2010.20.24-20AM.png?expires=1781168400&signature=27754c41e4343770798d9b4875882ddc64e328ed0b55e1bddb4a488cdd781224&req=dSQkEMl%2BmYdZFb4f3HP0gNOmOJJf0OuaQ%2BuHgxfDduyFcfz9a2f0zavOChf7%0A4t46ljRchxLzac747Q%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600466/37729d78058a1170722533ce/Screen-20Shot-202014-05-29-20at-2010.20.24-20AM.png?expires=1781168400&signature=27754c41e4343770798d9b4875882ddc64e328ed0b55e1bddb4a488cdd781224&req=dSQkEMl%2BmYdZFb4f3HP0gNOmOJJf0OuaQ%2BuHgxfDduyFcfz9a2f0zavOChf7%0A4t46ljRchxLzac747Q%3D%3D%0A)

* **FreePBX Administration** will allow you to configure your PBX. Use the admin username and admin password you configured in the step above to login. This section is what most people refer to as "FreePBX."
* **User Control Panel** is where a user can log in to make web calls, set up their phone buttons, view voicemails, send and receive faxes, use SMS & XMPP messaging, view conferences, and more, depending on what you have enabled for the user.
* **Operator Panel** is a screen that allows an operator to control calls
* **Get Support** takes you to a web page about various official support options for FreePBX.

1. ### **Once you've created your account, you'll be brought to the dashboard. Select "FreePBX Administration" and enter your username and password.**
2. ### **Follow the process to activate your FreePBX V15.**

   [![FreePBX welcome message page. ](https://downloads.intercomcdn.com/i/o/143566230/27f5a23c63080cda42159a3c/fpbx14.png?expires=1781168400&signature=630c406bca4bc38f3cca8015cd70e9469186f921bbe26db13a17e049a0b89192&req=dSQkE894n4JfFb4f3HP0gFofgQmX9Zp4PhLnP%2FK8s5XAi24%2FRT1K1uJQMmZm%0A2Ro%3D%0A)](https://downloads.intercomcdn.com/i/o/143566230/27f5a23c63080cda42159a3c/fpbx14.png?expires=1781168400&signature=630c406bca4bc38f3cca8015cd70e9469186f921bbe26db13a17e049a0b89192&req=dSQkE894n4JfFb4f3HP0gFofgQmX9Zp4PhLnP%2FK8s5XAi24%2FRT1K1uJQMmZm%0A2Ro%3D%0A)
3. ### **Select your default locales.**

   [![default locales settings page. ](https://downloads.intercomcdn.com/i/o/143566311/c173089b1b769d89e5b3e221/fpbx15.png?expires=1781168400&signature=8310fcc80933141afb92bd1367b50685a648220c077c1092a1ff394ad80d4e1e&req=dSQkE894noBeFb4f3HP0gFh2ewHBbdla12KheQnC17MbRfTN%2FQiPNhTzVw1a%0APEs%3D%0A)](https://downloads.intercomcdn.com/i/o/143566311/c173089b1b769d89e5b3e221/fpbx15.png?expires=1781168400&signature=8310fcc80933141afb92bd1367b50685a648220c077c1092a1ff394ad80d4e1e&req=dSQkE894noBeFb4f3HP0gFh2ewHBbdla12KheQnC17MbRfTN%2FQiPNhTzVw1a%0APEs%3D%0A)
4. ### **You'll be presented with some firewall details and other suggestions. You are welcome to set this up based on your requirements.**
5. ### **Once you're back at the dashboard, you'll see more detail.**

   [![FreePBX system overview portal. ](https://downloads.intercomcdn.com/i/o/143566551/19e5790665c7adf2a01350dd/fpbx16.png?expires=1781168400&signature=c7680aea4bfc4333b66d4ebeb7607e6ca15de5e22d2b843f7913e0f16c6cacbb&req=dSQkE894mIReFb4f3HP0gOhd2GA0GFLfw6E33M6kSV6vfmcOVBkmmJcH9yLz%0A%2FU4%3D%0A)](https://downloads.intercomcdn.com/i/o/143566551/19e5790665c7adf2a01350dd/fpbx16.png?expires=1781168400&signature=c7680aea4bfc4333b66d4ebeb7607e6ca15de5e22d2b843f7913e0f16c6cacbb&req=dSQkE894mIReFb4f3HP0gOhd2GA0GFLfw6E33M6kSV6vfmcOVBkmmJcH9yLz%0A%2FU4%3D%0A)

[Back to Top](#h_e1fc150ffb)

## 3. Configuring SIP settings for your FreePBX

At this point you can now work on confirming network settings and configuring your [SIP trunks](https://telnyx.com/products/sip-trunks) and extensions.

1. Make your way to **Settings -> Asterisk SIP Settings** in order to confirm your **network settings**.
2. You'll want to ensure you populate the **external** and **local** network addresses under **General SIP Settings** and **Chan SIP Settings**.
3. Click **Submit** and then **Apply Config.**

   [![FreePBX SIP settings configuration. ](https://downloads.intercomcdn.com/i/o/143566942/46b99f394b17b98806e2f3b9/fpbx17.png?expires=1781168400&signature=49e32dba96b517dfd92a6cd95229b9784c39c65a028f93de75eed8f0d5404084&req=dSQkE894lIVdFb4f3HP0gCExM47wUsr4TFHUJdVzCxlOUYZZ%2BxRkFZxa58eY%0ANMo%3D%0A)](https://downloads.intercomcdn.com/i/o/143566942/46b99f394b17b98806e2f3b9/fpbx17.png?expires=1781168400&signature=49e32dba96b517dfd92a6cd95229b9784c39c65a028f93de75eed8f0d5404084&req=dSQkE894lIVdFb4f3HP0gCExM47wUsr4TFHUJdVzCxlOUYZZ%2BxRkFZxa58eY%0ANMo%3D%0A)

[Back to Top](#h_e1fc150ffb)

## 4. Configure Extensions for your Free PBX

In this section, you'll configure all your PJSIP extensions.

1. Make your way to **Applications -> Extensions -> Add Extension -> Add New Chan SIP Extension.** The **Outbound CID** is the [number you purchased](https://portal.telnyx.com/#/app/numbers/my-numbers) from your Telnyx Mission Control Portal. The extensions secret may need to be populated under the **Other** tab.  
   ​  
   ​***Note*** *that if you do not set an Outbound CID for your extension, you will need to enable this on your trunk.*  
   ​  
   ​***Note*** *that this device uses CHAN\_SIP technology listening on Port 5160 (UDP - this is a NON STANDARD port).*

   [![FreePBX SIP extension configuration. ](https://downloads.intercomcdn.com/i/o/143567417/1a092920f8309cc81aea2edd/fpbx18.png?expires=1781168400&signature=410a07ee7f47138c890c21db594970f05b7cc5dc4326eb3ddce892ac02deb38f&req=dSQkE895mYBYFb4f3HP0gJGbjHtFM4%2Fu515Do0WdQoS2jdiTi1k4%2FHokyYUj%0AUbc%3D%0A)](https://downloads.intercomcdn.com/i/o/143567417/1a092920f8309cc81aea2edd/fpbx18.png?expires=1781168400&signature=410a07ee7f47138c890c21db594970f05b7cc5dc4326eb3ddce892ac02deb38f&req=dSQkE895mYBYFb4f3HP0gJGbjHtFM4%2Fu515Do0WdQoS2jdiTi1k4%2FHokyYUj%0AUbc%3D%0A)
2. Click **Submit** and **Apply Config.**

For testing purposes, you can now use your SIP client to register with FreePBX using the username, password/secret and local IP address of your FreePBX.

[Back to Top](#h_e1fc150ffb)

## 5. Configure a Trunk for your FreePBX

1. Make your way to **Connectivity -> Trunks -> Add Trunk -> Add New Chan SIP Trunk.** You'll now be located in the **General** tab.
2. Enter a Trunk name, your Outbound CID and the maximum channels you'd like for this trunk.

   [![configuration. ](https://downloads.intercomcdn.com/i/o/143568243/14edd224552aa89a58e02a25/fpbx19.png?expires=1781168400&signature=773b300709de15925dc204c9771806a7ecb5fde6b4173fde144ce2f87c60615d&req=dSQkE892n4VcFb4f3HP0gB1p87YFsjvJIngpTDlsy7sY%2B8t6PLFRZUlnUYYQ%0AOK0%3D%0A)](https://downloads.intercomcdn.com/i/o/143568243/14edd224552aa89a58e02a25/fpbx19.png?expires=1781168400&signature=773b300709de15925dc204c9771806a7ecb5fde6b4173fde144ce2f87c60615d&req=dSQkE892n4VcFb4f3HP0gB1p87YFsjvJIngpTDlsy7sY%2B8t6PLFRZUlnUYYQ%0AOK0%3D%0A)

   ***Note****: If you choose not to set an Outbound CID on your trunk, then you must set an Outbound CID on each relevant extension. If you do not set a caller ID on either the trunk or each extension, then your calls will reach our SIP proxy without a valid caller ID. You may instead choose to enable a Caller ID Override in your SIP Connection’s Outbound Options from within the Telnyx Portal. Please review our [caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy) for accepted formats.*  
   ​
3. Proceed to the **Dialed Number Manipulation Rules** tab. Depending on your use case, we've provided a simple dial pattern US numbers below.

   [![Dialed Number Manipulation Rules settings page. ](https://downloads.intercomcdn.com/i/o/143568366/2abd5eb969096e1ee3fd139e/fpbx20.png?expires=1781168400&signature=65ab27818bd80496690b22588aa722825c9a773b4e2c7c50641bc448bf91afb9&req=dSQkE892nodZFb4f3HP0gErjDm6CsWTfUX%2BTtQ7rUFzq%2FKIQigJ%2F00GKyv9X%0AHjg%3D%0A)](https://downloads.intercomcdn.com/i/o/143568366/2abd5eb969096e1ee3fd139e/fpbx20.png?expires=1781168400&signature=65ab27818bd80496690b22588aa722825c9a773b4e2c7c50641bc448bf91afb9&req=dSQkE892nodZFb4f3HP0gErjDm6CsWTfUX%2BTtQ7rUFzq%2FKIQigJ%2F00GKyv9X%0AHjg%3D%0A)

   **For US numbers:**

   1. prepend:*1*; match pattern: *NXXNXXXXXX*
   2. prepend: blank; match pattern: *1NXXNXXXXXX*

   **International:**

   1. prepend: Country Dialing prefix; match pattern: *NXXNXXXXXX*
   2. prepend:blank; match pattern: (Country Dialing prefix)*NXXNXXXXXX*

[Back to Top](#h_e1fc150ffb)

## 6. Configure Outbound and Inbound Settings for your FreePBX

1. Still in the **Add Trunk** configuration tool, Click on the **SIP Settings** tab and click on the **Outgoing** sub-tab. Make sure to specify:

   1. **type:** *friend*
   2. **qualify:** *yes*
   3. **insecure:** *port,invite*
   4. **host:** *sip.telnyx.com*
   5. **fromdomain:** *sip.telnyx.com*
   6. **disallow:** *all*
   7. **allow:** *ulaw*

      [![Outbound settings page for FreePBX. ](https://downloads.intercomcdn.com/i/o/143568570/17ad8d0ded0e6a6b00caf683/fpbx21.png?expires=1781168400&signature=0f0b0d75d9546231922ab3722ff8ed34f517246a2bb4f2fdc25d491a719e5bda&req=dSQkE892mIZfFb4f3HP0gMCyT%2Bfsu%2BPF3%2F1YP8RJpgbpp3Bpa%2BDC0P%2BOO%2Bff%0APrw%3D%0A)](https://downloads.intercomcdn.com/i/o/143568570/17ad8d0ded0e6a6b00caf683/fpbx21.png?expires=1781168400&signature=0f0b0d75d9546231922ab3722ff8ed34f517246a2bb4f2fdc25d491a719e5bda&req=dSQkE892mIZfFb4f3HP0gMCyT%2Bfsu%2BPF3%2F1YP8RJpgbpp3Bpa%2BDC0P%2BOO%2Bff%0APrw%3D%0A)
2. Now click on the **Incoming** sub-tab. Make sure to specify:

   1. **type:** *friend*
   2. **insecure:** *port,invite*
   3. **host:** *sip.telnyx.com*
   4. **dtmfmode:** *rfc2833*
   5. **disallow:** *all*
   6. **allow:** *ulaw*

      [![FreePBX Incoming sub-tab. ](https://downloads.intercomcdn.com/i/o/143568584/cddf6ec3ea4bf1456666908d/fpbx22.png?expires=1781168400&signature=5d70b96cf1fa6cf0207d69f5dc4691234af33d0f9a37b95c2f1e4cb4363e9f62&req=dSQkE892mIlbFb4f3HP0gEhqSg01oWUTOka14tZfR7iD0JXKY%2Bl2%2BnCgNGJ9%0APPc%3D%0A)](https://downloads.intercomcdn.com/i/o/143568584/cddf6ec3ea4bf1456666908d/fpbx22.png?expires=1781168400&signature=5d70b96cf1fa6cf0207d69f5dc4691234af33d0f9a37b95c2f1e4cb4363e9f62&req=dSQkE892mIlbFb4f3HP0gEhqSg01oWUTOka14tZfR7iD0JXKY%2Bl2%2BnCgNGJ9%0APPc%3D%0A)

[Back to Top](#h_e1fc150ffb)

## 7. Configure outbound routing

1. Make your way to **Connectivity > Outbound Routes > Add Outbound Route.**
2. Enter the route name, route CID and specify the Telnyx\_IP trunk for this outbound route.

   [![Add Outbound Route section. ](https://downloads.intercomcdn.com/i/o/143568878/eb9f7159757921d692c5cf3c/fpbx23.png?expires=1781168400&signature=f9f41e246176c3939d0d4859f00c353ed6aa54a244e8767665da238d96fcc1ee&req=dSQkE892lYZXFb4f3HP0gJAS1%2BDpHVUd%2FrLnUnpSv2ENclMug0za3RfbMMJu%0AKHk%3D%0A)](https://downloads.intercomcdn.com/i/o/143568878/eb9f7159757921d692c5cf3c/fpbx23.png?expires=1781168400&signature=f9f41e246176c3939d0d4859f00c353ed6aa54a244e8767665da238d96fcc1ee&req=dSQkE892lYZXFb4f3HP0gJAS1%2BDpHVUd%2FrLnUnpSv2ENclMug0za3RfbMMJu%0AKHk%3D%0A)
3. Click **Submit** and **Apply Config**.

[Back to Top](#h_e1fc150ffb)

## 8. Configure inbound routing

1. Make your way to **Connectivity -> Inbound Routes -> Add Inbound Route.**
2. Enter the route name description, DID associated with this route and specify the extension that should be associated when calls are received to the DID.
3. Click **Submit** and **Apply Config**.

|  |
| --- |
| ***Note:*** *By default, when creating a SIP Connection in the Telnyx Mission Control Portal, the number formats for the ANI and DNIS will be set to E.164. This means Telnyx will send the dialled number in the SIP INVITE to your FreePBX system with 11 digits. As the [DID number](https://telnyx.com/resources/sip-did) above is in 11 digit format, the call will be accepted and routed to the extension. However, you can control the number formats as you desire and can read more about it* [here](https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats). |

That's it, you've now completed the configuration of FreePBX V14 IP Trunk and can now make and receive calls by using Telnyx as your SIP provider!

[Back to Top](#h_e1fc150ffb)

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

[FreePBX Trunk Settings With Telnyx](https://support.telnyx.com/en/articles/1130620-freepbx-trunk-settings-with-telnyx)[Configuring a FreePBX V13 Credentials Trunk](https://support.telnyx.com/en/articles/1130648-configuring-a-freepbx-v13-credentials-trunk)[FreePBX V14: Credentials - ChanSIP](https://support.telnyx.com/en/articles/3284752-freepbx-v14-credentials-chansip)[FreePBX V15 IP Trunk - ChanSIP Tutorial](https://support.telnyx.com/en/articles/5467232-freepbx-v15-ip-trunk-chansip-tutorial)[FreePBX V15: IP Trunk - PJSIP](https://support.telnyx.com/en/articles/5619595-freepbx-v15-ip-trunk-pjsip)

Did this answer your question?

😞😐😃

Table of contents
