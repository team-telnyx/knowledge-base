---
source_url: https://support.telnyx.com/en/articles/1130620-freepbx-trunk-settings-with-telnyx
scraped: 2026-06-11
---

FreePBX Trunk Settings With Telnyx | Telnyx Help Center

[Skip to main content](#main-content)

# FreePBX Trunk Settings With Telnyx

Learn how to configure a FreePBX V13 IP trunk with Telnyx. Get started today. HINT: It's easy.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_afe197f7e2)

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

1. [Install your FreePBX V13](#h_e14789d304)
2. [Configure basic settings for your FreePBX](#h_266095bb88)
3. [Configure SIP settings for your FreePBX](#h_5d9c04ead4)
4. [Configure extensions for your FreePBX](#h_df489774b0)
5. [Configure a trunk for your FreePBX](#h_120e6edea6)
6. [Configure outbound and inbound settings for your FreePBX](#h_9cf11cdc8e)
7. [Configure outbound routing](#h_586e2c623d)
8. [Configure inbound routing](#h_d2035fef38)

**Pre-requisites**

* [Download](https://www.freepbx.org/downloads/) and [install](https://www.freepbx.org/get-started/) FreePBX V13
* [Configure your Telnyx Mission Control Portal](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* [Set up an IP connection on your Telnyx Mission Control Portal](https://portal.telnyx.com/#/app/connections)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for FreePBX/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Install your FreePBX V13

In this section, you'll go through the steps you need to follow to install FreePBX.

1. ### **Once you load the ISO onto your server or virtual machine, you'll have a few options to select for installation. We'll be doing a full install via asterisk 13.**

   [![A page showing ISO installation using asterisk 13](https://downloads.intercomcdn.com/i/o/143563822/42a6c08fac1469d0cca195e4/fpbx1.png?expires=1781167500&signature=69b587f7faebdaf81e7c876760a96f1dddeeca9d538cbac5e71b481423a2f3fe&req=dSQkE899lYNdFb4f3HP0gCnqDbRuBPHLeZPTPg%2FbOSRCGXLb%2BlMi5HfHzC%2FV%0AtrM%3D%0A)](https://downloads.intercomcdn.com/i/o/143563822/42a6c08fac1469d0cca195e4/fpbx1.png?expires=1781167500&signature=69b587f7faebdaf81e7c876760a96f1dddeeca9d538cbac5e71b481423a2f3fe&req=dSQkE899lYNdFb4f3HP0gCnqDbRuBPHLeZPTPg%2FbOSRCGXLb%2BlMi5HfHzC%2FV%0AtrM%3D%0A)
2. ### **Confirm your network settings.**

   [![Network setting confirmations page. ](https://downloads.intercomcdn.com/i/o/143564023/2f6042fae441489e77aed253/fpbx2.png?expires=1781167500&signature=76a5ef121b43e67c33797cba96750e50a7e347fb8768b4d5067e63df90dae687&req=dSQkE896nYNcFb4f3HP0gNqS6of%2BktSzKcsaSZcVtnTqTsLWd5OqRR%2FMzt8r%0A3wQ%3D%0A)](https://downloads.intercomcdn.com/i/o/143564023/2f6042fae441489e77aed253/fpbx2.png?expires=1781167500&signature=76a5ef121b43e67c33797cba96750e50a7e347fb8768b4d5067e63df90dae687&req=dSQkE896nYNcFb4f3HP0gNqS6of%2BktSzKcsaSZcVtnTqTsLWd5OqRR%2FMzt8r%0A3wQ%3D%0A)
3. ### **Choose and confirm your root password.**

   [![Root password confirmation page. ](https://downloads.intercomcdn.com/i/o/143564187/32a46bb06a195135130fb14d/pbx4.png?expires=1781167500&signature=8469d1f726dca137649da726002f172a1a77e1908361e53d4c3d428b5dde1053&req=dSQkE896nIlYFb4f3HP0gKnjhU7VuZ%2BWFHaWc4lAZKjyhYlGuBCyz%2BLe3xyx%0Ayk0%3D%0A)](https://downloads.intercomcdn.com/i/o/143564187/32a46bb06a195135130fb14d/pbx4.png?expires=1781167500&signature=8469d1f726dca137649da726002f172a1a77e1908361e53d4c3d428b5dde1053&req=dSQkE896nIlYFb4f3HP0gKnjhU7VuZ%2BWFHaWc4lAZKjyhYlGuBCyz%2BLe3xyx%0Ayk0%3D%0A)
4. ### **Wait while your packages are installed.**

   [![Package installation waiting page. ](https://downloads.intercomcdn.com/i/o/143564263/c17f8516b74410bf29b05cb2/fpbx5.png?expires=1781167500&signature=7857071255bca485f228fa736194d70b2939ce12ccd3576aeb6e9fffc8000cf9&req=dSQkE896n4dcFb4f3HP0gNWpXCasmWVtjX77qnJY0XQgY%2FaHj13BPTFMmUEP%0A43o%3D%0A)](https://downloads.intercomcdn.com/i/o/143564263/c17f8516b74410bf29b05cb2/fpbx5.png?expires=1781167500&signature=7857071255bca485f228fa736194d70b2939ce12ccd3576aeb6e9fffc8000cf9&req=dSQkE896n4dcFb4f3HP0gNWpXCasmWVtjX77qnJY0XQgY%2FaHj13BPTFMmUEP%0A43o%3D%0A)
5. ### **Enter your root username and password.**

   [![Localhost credentials input point. ](https://downloads.intercomcdn.com/i/o/143565289/a91f27db12806e28739123af/fpbx7.png?expires=1781167500&signature=3edaa92b8cda1734fc903232cfad235cb2de411c9fa6221c3622f4838e923c5f&req=dSQkE897n4lWFb4f3HP0gPoY1Yb3e2PruZS0YgJ56S2mKG96vsq2tDfOoROt%0AyRg%3D%0A)](https://downloads.intercomcdn.com/i/o/143565289/a91f27db12806e28739123af/fpbx7.png?expires=1781167500&signature=3edaa92b8cda1734fc903232cfad235cb2de411c9fa6221c3622f4838e923c5f&req=dSQkE897n4lWFb4f3HP0gPoY1Yb3e2PruZS0YgJ56S2mKG96vsq2tDfOoROt%0AyRg%3D%0A)
6. ### **You'll now be provided with the URL you need to use in order to access the FreePBX web interface.**

   [![The FreePBX Web Interface. ](https://downloads.intercomcdn.com/i/o/143565361/964fa7c84ed97147519f2a9b/fpbx8.png?expires=1781167500&signature=e9f0f0ac7568cf9ae33883147552035027a28e87fa4afac95e77eb674900e186&req=dSQkE897nodeFb4f3HP0gAmdOGa7S%2BzOayVxqgRFb04%2BakV1dDhMSAapRSIs%0An6g%3D%0A)](https://downloads.intercomcdn.com/i/o/143565361/964fa7c84ed97147519f2a9b/fpbx8.png?expires=1781167500&signature=e9f0f0ac7568cf9ae33883147552035027a28e87fa4afac95e77eb674900e186&req=dSQkE897nodeFb4f3HP0gAmdOGa7S%2BzOayVxqgRFb04%2BakV1dDhMSAapRSIs%0An6g%3D%0A)

   ##
7. #### **Enter the IP address of the new PBX into your web browser. The first time you do so, you'll be asked to create the admin username and the admin password. That username and password will be used in the future to access the FreePBX configuration screen.** **Note:** These passwords do not change the Root password! They are only used for access to the FreePBX web interface.

   [![Admin user credential creation interface. ](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600462/6bb7ec3442d8b721dd202f39/Screen-20Shot-202017-07-20-20at-2011.58.40-20AM.png?expires=1781167500&signature=e510639bf99ef4e3ebcbd2edd639038f8bac6354484307eff26104e17c145add&req=dSQkEMl%2BmYddFb4f3HP0gFpYnnjFfWSGoZBDK%2BVUPyaMEFHRLQQZ9a8QNDgg%0A2is%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600462/6bb7ec3442d8b721dd202f39/Screen-20Shot-202017-07-20-20at-2011.58.40-20AM.png?expires=1781167500&signature=e510639bf99ef4e3ebcbd2edd639038f8bac6354484307eff26104e17c145add&req=dSQkEMl%2BmYddFb4f3HP0gFpYnnjFfWSGoZBDK%2BVUPyaMEFHRLQQZ9a8QNDgg%0A2is%3D%0A)
8. ### **Once submitted you can log in to the admin panel with the username and password set up on the step above.**

[Back to Top](#h_afe197f7e2)

## 2. Configuring basic settings for your FreePBX

In this step, you'll configure your FreePBX V15 and connect it to Telnyx. To begin, notice that the main FreePBX screen will offer you four options:

[![The main FreePBX screen, with four options offering. ](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600466/37729d78058a1170722533ce/Screen-20Shot-202014-05-29-20at-2010.20.24-20AM.png?expires=1781167500&signature=3ce147def828772b946bf69ffaf7be1edf5b1b078c32b413a0bc4bd20de715ea&req=dSQkEMl%2BmYdZFb4f3HP0gNOmOJJf3%2BqaQ%2BuHgxfDduxYE%2BjbTkhaq8EG5VXL%0AGWBdVic3YKVc5sf8Rw%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/143600466/37729d78058a1170722533ce/Screen-20Shot-202014-05-29-20at-2010.20.24-20AM.png?expires=1781167500&signature=3ce147def828772b946bf69ffaf7be1edf5b1b078c32b413a0bc4bd20de715ea&req=dSQkEMl%2BmYdZFb4f3HP0gNOmOJJf3%2BqaQ%2BuHgxfDduxYE%2BjbTkhaq8EG5VXL%0AGWBdVic3YKVc5sf8Rw%3D%3D%0A)

* **FreePBX Administration** will allow you to configure your PBX. Use the admin username and admin password you configured in the step above to login. This section is what most people refer to as "FreePBX."
* **User Control Panel** is where a user can log in to make web calls, set up their phone buttons, view voicemails, send and receive faxes, use SMS & XMPP messaging, view conferences, and more, depending on what you have enabled for the user.
* **Operator Panel** is a screen that allows an operator to control calls
* **Get Support** takes you to a web page about various official support options for FreePBX.

1. ### **Once you've created your account, you'll be brought to the dashboard. Select "FreePBX Administration" and enter your username and password.**
2. ### **Follow the process to activate your FreePBX V15.**

   [![FreePBX Administration dashboard. ](https://downloads.intercomcdn.com/i/o/143566230/27f5a23c63080cda42159a3c/fpbx14.png?expires=1781167500&signature=7cfec3089084a51c62cae05e5c2ce77c8bde21650681a18cf0621a86ae35e0a6&req=dSQkE894n4JfFb4f3HP0gFofgQmX%2Bpt4PhLnP%2FK8s5WVd1Dtkdee8wmcRIh3%0AowI%3D%0A)](https://downloads.intercomcdn.com/i/o/143566230/27f5a23c63080cda42159a3c/fpbx14.png?expires=1781167500&signature=7cfec3089084a51c62cae05e5c2ce77c8bde21650681a18cf0621a86ae35e0a6&req=dSQkE894n4JfFb4f3HP0gFofgQmX%2Bpt4PhLnP%2FK8s5WVd1Dtkdee8wmcRIh3%0AowI%3D%0A)
3. ### **Select your default locales.**

   [![Page to select default locales. ](https://downloads.intercomcdn.com/i/o/143566311/c173089b1b769d89e5b3e221/fpbx15.png?expires=1781167500&signature=3f6421798c8c508304360bc87b1638f7d0150bf31b0c4c347c27c8d2a06a98b9&req=dSQkE894noBeFb4f3HP0gFh2ewHBYtha12KheQnC17PwUafS%2Bo%2FB7kUkWgeG%0AVCI%3D%0A)](https://downloads.intercomcdn.com/i/o/143566311/c173089b1b769d89e5b3e221/fpbx15.png?expires=1781167500&signature=3f6421798c8c508304360bc87b1638f7d0150bf31b0c4c347c27c8d2a06a98b9&req=dSQkE894noBeFb4f3HP0gFh2ewHBYtha12KheQnC17PwUafS%2Bo%2FB7kUkWgeG%0AVCI%3D%0A)
4. ### **You'll be presented with some firewall details and other suggestions. You are welcome to set this up based on your requirements.**
5. ### **Once you're back at the dashboard, you'll see more detail.**

   [![Admin dashboard with more administration details. ](https://downloads.intercomcdn.com/i/o/143566551/19e5790665c7adf2a01350dd/fpbx16.png?expires=1781167500&signature=76d2c88461a33139737df696bd26f75340ba665bc2156221f39af5f3de914928&req=dSQkE894mIReFb4f3HP0gOhd2GA0F1Pfw6E33M6kSV6LgqsVADr809Ct5EgD%0AfHc%3D%0A)](https://downloads.intercomcdn.com/i/o/143566551/19e5790665c7adf2a01350dd/fpbx16.png?expires=1781167500&signature=76d2c88461a33139737df696bd26f75340ba665bc2156221f39af5f3de914928&req=dSQkE894mIReFb4f3HP0gOhd2GA0F1Pfw6E33M6kSV6LgqsVADr809Ct5EgD%0AfHc%3D%0A)

[Back to Top](#h_afe197f7e2)

## 3. Configuring SIP settings for your FreePBX

At this point you can now work on confirming network settings and configuring your [SIP trunks](https://telnyx.com/products/sip-trunks) and extensions.

1. Make your way to **Settings -> Asterisk SIP Settings** in order to confirm your **network settings**.
2. You'll want to ensure you populate the **external** and **local** network addresses under **General SIP Settings** and **Chan SIP Settings**.
3. Click **Submit** and then **Apply Config.**

   [![Asterisk SIP Settings for network settings confirmation. ](https://downloads.intercomcdn.com/i/o/143566942/46b99f394b17b98806e2f3b9/fpbx17.png?expires=1781167500&signature=85572541e4d6ecebddbc7c4c62139e75bb3cf5ef2dfd762e5f776f6af7fee3a9&req=dSQkE894lIVdFb4f3HP0gCExM47wXcv4TFHUJdVzCxlRDY4NkBKWF2SfmfsK%0AgqQ%3D%0A)](https://downloads.intercomcdn.com/i/o/143566942/46b99f394b17b98806e2f3b9/fpbx17.png?expires=1781167500&signature=85572541e4d6ecebddbc7c4c62139e75bb3cf5ef2dfd762e5f776f6af7fee3a9&req=dSQkE894lIVdFb4f3HP0gCExM47wXcv4TFHUJdVzCxlRDY4NkBKWF2SfmfsK%0AgqQ%3D%0A)

[Back to Top](#h_afe197f7e2)

## 4. Configure Extensions for your Free PBX

In this section, you'll configure all your PJSIP extensions.

1. Make your way to **Applications -> Extensions -> Add Extension -> Add New Chan SIP Extension.** The **Outbound CID** is the [number you purchased](https://portal.telnyx.com/#/app/numbers/my-numbers) from your Telnyx Mission Control Portal. The extensions secret may need to be populated under the **Other** tab.  
   ​  
   ​***Note*** *that if you do not set an Outbound CID for your extension, you will need to enable this on your trunk.*  
   ​  
   ​***Note*** *that this device uses CHAN\_SIP technology listening on Port 5160 (UDP - this is a NON STANDARD port).*

   [![New Chan SIP Extension Interface. ](https://downloads.intercomcdn.com/i/o/143567417/1a092920f8309cc81aea2edd/fpbx18.png?expires=1781167500&signature=70d31e343c5753b44090c50d62a325effffc5f7fe504a88726d4e2b0293a5f6d&req=dSQkE895mYBYFb4f3HP0gJGbjHtFPI7u515Do0WdQoQmkItuoXsY95QR2NHh%0ASMA%3D%0A)](https://downloads.intercomcdn.com/i/o/143567417/1a092920f8309cc81aea2edd/fpbx18.png?expires=1781167500&signature=70d31e343c5753b44090c50d62a325effffc5f7fe504a88726d4e2b0293a5f6d&req=dSQkE895mYBYFb4f3HP0gJGbjHtFPI7u515Do0WdQoQmkItuoXsY95QR2NHh%0ASMA%3D%0A)
2. Click **Submit** and **Apply Config.**

For testing purposes, you can now use your SIP client to register with FreePBX using the username, password/secret and local IP address of your FreePBX.

[Back to Top](#h_afe197f7e2)

## 5. Configure a Trunk for your FreePBX

1. Make your way to **Connectivity -> Trunks -> Add Trunk -> Add New Chan SIP Trunk.** You'll now be located in the **General** tab.
2. Enter a Trunk name, your Outbound CID and the maximum channels you'd like for this trunk.

   [![General tab interface for FreePBX configuration. ](https://downloads.intercomcdn.com/i/o/143568243/14edd224552aa89a58e02a25/fpbx19.png?expires=1781167500&signature=6974df3fb15c155e6189dc6119353a66a1563caad94d5d83fe5c589f35f76159&req=dSQkE892n4VcFb4f3HP0gB1p87YFvTrJIngpTDlsy7uuB57TKfv9R%2BnyFb5F%0A%2B7w%3D%0A)](https://downloads.intercomcdn.com/i/o/143568243/14edd224552aa89a58e02a25/fpbx19.png?expires=1781167500&signature=6974df3fb15c155e6189dc6119353a66a1563caad94d5d83fe5c589f35f76159&req=dSQkE892n4VcFb4f3HP0gB1p87YFvTrJIngpTDlsy7uuB57TKfv9R%2BnyFb5F%0A%2B7w%3D%0A)

   ***Note****: If you choose not to set an Outbound CID on your trunk, then you must set an Outbound CID on each relevant extension. If you do not set a caller ID on either the trunk or each extension, then your calls will reach our SIP proxy without a valid caller ID. You may instead choose to enable a Caller ID Override in your SIP Connection’s Outbound Options from within the Telnyx Portal. Please review our [caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy) for accepted formats.*  
   ​
3. Proceed to the **Dialed Number Manipulation Rules** tab. Depending on your use case, we've provided a simple dial pattern US numbers below.

   [![Dialed Number Manipulation Rules tab. ](https://downloads.intercomcdn.com/i/o/143568366/2abd5eb969096e1ee3fd139e/fpbx20.png?expires=1781167500&signature=e784f7d912a0e06f2509e35f8f4a3cf65d9bde6ffcbcc9f4d861c21f4078be64&req=dSQkE892nodZFb4f3HP0gErjDm6CvmXfUX%2BTtQ7rUFyNb%2Fon1OdlP8LN7dpO%0A690%3D%0A)](https://downloads.intercomcdn.com/i/o/143568366/2abd5eb969096e1ee3fd139e/fpbx20.png?expires=1781167500&signature=e784f7d912a0e06f2509e35f8f4a3cf65d9bde6ffcbcc9f4d861c21f4078be64&req=dSQkE892nodZFb4f3HP0gErjDm6CvmXfUX%2BTtQ7rUFyNb%2Fon1OdlP8LN7dpO%0A690%3D%0A)

   **For US numbers:**

   1. prepend:*1*; match pattern: *NXXNXXXXXX*
   2. prepend: blank; match pattern: *1NXXNXXXXXX*

   **International:**

   1. prepend: Country Dialing prefix; match pattern: *NXXNXXXXXX*
   2. prepend:blank; match pattern: (Country Dialing prefix)*NXXNXXXXXX*

[Back to Top](#h_afe197f7e2)

## 6. Configure Outbound and Inbound Settings for your FreePBX

1. Still in the **Add Trunk** configuration tool, Click on the **SIP Settings** tab and click on the **Outgoing** sub-tab. Make sure to specify:

   1. **type:** *friend*
   2. **qualify:** *yes*
   3. **insecure:** *port,invite*
   4. **host:** *sip.telnyx.com*
   5. **fromdomain:** *sip.telnyx.com*
   6. **disallow:** *all*
   7. **allow:** *ulaw*

      [![Add Trunk configuration interface.](https://downloads.intercomcdn.com/i/o/143568570/17ad8d0ded0e6a6b00caf683/fpbx21.png?expires=1781167500&signature=a430f008dec6e1175614ae8c65221b81bfc7ff0a36de755ea75b06cf5feec7e0&req=dSQkE892mIZfFb4f3HP0gMCyT%2BfstOLF3%2F1YP8RJpgZPdQDKNQBhzx2Ol4er%0AzTI%3D%0A)](https://downloads.intercomcdn.com/i/o/143568570/17ad8d0ded0e6a6b00caf683/fpbx21.png?expires=1781167500&signature=a430f008dec6e1175614ae8c65221b81bfc7ff0a36de755ea75b06cf5feec7e0&req=dSQkE892mIZfFb4f3HP0gMCyT%2BfstOLF3%2F1YP8RJpgZPdQDKNQBhzx2Ol4er%0AzTI%3D%0A)
2. Now click on the **Incoming** sub-tab. Make sure to specify:

   1. **type:** *friend*
   2. **insecure:** *port,invite*
   3. **host:** *sip.telnyx.com*
   4. **dtmfmode:** *rfc2833*
   5. **disallow:** *all*
   6. **allow:** *ulaw*

      [![Incoming sub-tab interface. ](https://downloads.intercomcdn.com/i/o/143568584/cddf6ec3ea4bf1456666908d/fpbx22.png?expires=1781167500&signature=98b66155dbe7602eec5de67d00c49f84b8c577f6f93a61fae992cf575d2a3498&req=dSQkE892mIlbFb4f3HP0gEhqSg01rmQTOka14tZfR7iWq0aRhMukT5Aizfqh%0AR0M%3D%0A)](https://downloads.intercomcdn.com/i/o/143568584/cddf6ec3ea4bf1456666908d/fpbx22.png?expires=1781167500&signature=98b66155dbe7602eec5de67d00c49f84b8c577f6f93a61fae992cf575d2a3498&req=dSQkE892mIlbFb4f3HP0gEhqSg01rmQTOka14tZfR7iWq0aRhMukT5Aizfqh%0AR0M%3D%0A)

[Back to Top](#h_afe197f7e2)

## 7. Configure outbound routing

1. Make your way to **Connectivity > Outbound Routes > Add Outbound Route.**
2. Enter the route name, route CID and specify the Telnyx\_IP trunk for this outbound route.

   [![Outbound Route configuration interface. ](https://downloads.intercomcdn.com/i/o/143568878/eb9f7159757921d692c5cf3c/fpbx23.png?expires=1781167500&signature=63260fdf48a764f1894a1976d5d3b939bd5625197daaa0622d709bfb92676894&req=dSQkE892lYZXFb4f3HP0gJAS1%2BDpElQd%2FrLnUnpSv2H6t8exMGCwmarQf1Ov%0ANlQ%3D%0A)](https://downloads.intercomcdn.com/i/o/143568878/eb9f7159757921d692c5cf3c/fpbx23.png?expires=1781167500&signature=63260fdf48a764f1894a1976d5d3b939bd5625197daaa0622d709bfb92676894&req=dSQkE892lYZXFb4f3HP0gJAS1%2BDpElQd%2FrLnUnpSv2H6t8exMGCwmarQf1Ov%0ANlQ%3D%0A)
3. Click **Submit** and **Apply Config**.

[Back to Top](#h_afe197f7e2)

## 8. Configure inbound routing

1. Make your way to **Connectivity -> Inbound Routes -> Add Inbound Route.**
2. Enter the route name description, DID associated with this route and specify the extension that should be associated when calls are received to the DID.
3. Click **Submit** and **Apply Config**.

|  |
| --- |
| ***Note:*** *By default, when creating a SIP Connection in the Telnyx Mission Control Portal, the number formats for the ANI and DNIS will be set to E.164. This means Telnyx will send the dialled number in the SIP INVITE to your FreePBX system with 11 digits. As the [DID number](https://telnyx.com/resources/sip-did) above is in 11 digit format, the call will be accepted and routed to the extension. However, you can control the number formats as you desire and can read more about it* [here](https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats). |

That's it, you've now completed the configuration of FreePBX V13 IP Trunk and can now make and receive calls by using Telnyx as your SIP provider!

[Back to Top](#h_afe197f7e2)

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

[Configuring a FreePBX V13 Credentials Trunk](https://support.telnyx.com/en/articles/1130648-configuring-a-freepbx-v13-credentials-trunk)[FreePBX V14: IP Trunk - ChanSIP](https://support.telnyx.com/en/articles/3284736-freepbx-v14-ip-trunk-chansip)[FreePBX V14: Credentials - ChanSIP](https://support.telnyx.com/en/articles/3284752-freepbx-v14-credentials-chansip)[FreePBX V15 IP Trunk - ChanSIP Tutorial](https://support.telnyx.com/en/articles/5467232-freepbx-v15-ip-trunk-chansip-tutorial)[FreePBX V15: IP Trunk - PJSIP](https://support.telnyx.com/en/articles/5619595-freepbx-v15-ip-trunk-pjsip)

Did this answer your question?

😞😐😃

Table of contents
