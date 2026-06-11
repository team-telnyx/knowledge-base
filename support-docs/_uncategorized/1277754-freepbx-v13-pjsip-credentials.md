---
source_url: https://support.telnyx.com/en/articles/1277754-freepbx-v13-pjsip-credentials
scraped: 2026-06-11
---

FreePBX V13: PJSIP Credentials | Telnyx Help Center

[Skip to main content](#main-content)

# FreePBX V13: PJSIP Credentials

In this article we will explain how to configure a FreePBX PJSIP V13 Credentials Trunk with Telnyx.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#instructions-to-configure-a-freepbx-pjsip-v13)

[FreePBX](https://www.freepbx.org/) is a web-based open source GUI (graphical user interface) that controls and manages Asterisk (PBX), an open source communication server. FreePBX is licensed under the GNU General Public License (GPL), an open source license. FreePBX can be installed manually or as part of the pre-configured FreePBX Distro that includes the system OS, Asterisk, FreePBX GUI and assorted dependencies.

You'll need to have created a [Credentials based connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal account, assigned this connection to a DID and outbound profile in order to make and receive calls.

Additional documentation and resources:

* [FreePBX documentation](https://wiki.freepbx.org/#all-updates) (This is useful for any configuration instructions that don't involve Telnyx and are maintained solely by FreePBX)
* [FreePBX community](https://community.freepbx.org/)
* [FreePBX support](https://www.freepbx.org/support/)
* [FreePBX videos](https://www.freepbx.org/videos/)

---

# Instructions to Configure a FreePBX PJSIP V13

In this activity you will:

1. [Install FreePBX](#h_34dbd49eeb) (You can also follow [instructions provided by FreePBX](https://www.freepbx.org/get-started/))
2. [Configure your SIP trunk](#chanpjsip-trunkconfiguration)
3. [Configure outbound routes](#h_87e6b8ee2f)
4. [Configure inbound routes](#h_979a5348af)

**Pre-requisites**

* [Set up and configure your Telnyx Mission Control Portal](https://support.telnyx.com/en/articles/5717957-zoiper-5-pro-telnyx-setup#h_dc5df9cfdf)
* Have created a [credentials based connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal account, assigned this connection to a DID and outbound profile in order to make and receive calls.
* [Download](https://www.freepbx.org/downloads/) and [install](https://www.freepbx.org/get-started/) FreePBX. You can also see [our installation guide](#h_34dbd49eeb) below.
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)

**Video walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for FreePBX/Telnyx SIP trunking configuration coming soon. Check back as we update our docs.* |

## 1. Install FreePBX

Once you've loaded the FreePBX ISO onto your server or virtual machine, you'll have a few options to select for installation. We'll be doing a full install via asterisk 13. So go ahead and run the installer.

### Steps:

1. #### Select **Full Install**.

   [![FreePBX ISO interface for installation. ](https://downloads.intercomcdn.com/i/o/143563822/42a6c08fac1469d0cca195e4/fpbx1.png?expires=1781167500&signature=69b587f7faebdaf81e7c876760a96f1dddeeca9d538cbac5e71b481423a2f3fe&req=dSQkE899lYNdFb4f3HP0gCnqDbRuBPHLeZPTPg%2FbOSRCGXLb%2BlMi5HfHzC%2FV%0AtrM%3D%0A)](https://downloads.intercomcdn.com/i/o/143563822/42a6c08fac1469d0cca195e4/fpbx1.png?expires=1781167500&signature=69b587f7faebdaf81e7c876760a96f1dddeeca9d538cbac5e71b481423a2f3fe&req=dSQkE899lYNdFb4f3HP0gCnqDbRuBPHLeZPTPg%2FbOSRCGXLb%2BlMi5HfHzC%2FV%0AtrM%3D%0A)
2. #### Confirm your network settings.

   [![FreePBX ISO interface for network settings confirmation. ](https://downloads.intercomcdn.com/i/o/143564023/2f6042fae441489e77aed253/fpbx2.png?expires=1781167500&signature=76a5ef121b43e67c33797cba96750e50a7e347fb8768b4d5067e63df90dae687&req=dSQkE896nYNcFb4f3HP0gNqS6of%2BktSzKcsaSZcVtnTqTsLWd5OqRR%2FMzt8r%0A3wQ%3D%0A)](https://downloads.intercomcdn.com/i/o/143564023/2f6042fae441489e77aed253/fpbx2.png?expires=1781167500&signature=76a5ef121b43e67c33797cba96750e50a7e347fb8768b4d5067e63df90dae687&req=dSQkE896nYNcFb4f3HP0gNqS6of%2BktSzKcsaSZcVtnTqTsLWd5OqRR%2FMzt8r%0A3wQ%3D%0A)
3. #### Confirm your **root** password.

   [![FreePBX ISO interface for root password confirmation. ](https://downloads.intercomcdn.com/i/o/143564187/32a46bb06a195135130fb14d/pbx4.png?expires=1781167500&signature=8469d1f726dca137649da726002f172a1a77e1908361e53d4c3d428b5dde1053&req=dSQkE896nIlYFb4f3HP0gKnjhU7VuZ%2BWFHaWc4lAZKjyhYlGuBCyz%2BLe3xyx%0Ayk0%3D%0A)](https://downloads.intercomcdn.com/i/o/143564187/32a46bb06a195135130fb14d/pbx4.png?expires=1781167500&signature=8469d1f726dca137649da726002f172a1a77e1908361e53d4c3d428b5dde1053&req=dSQkE896nIlYFb4f3HP0gKnjhU7VuZ%2BWFHaWc4lAZKjyhYlGuBCyz%2BLe3xyx%0Ayk0%3D%0A)
4. #### Wait for all the necessary packages to be installed.

   [![FreePBX ISO interface for installation of necessary packages. ](https://downloads.intercomcdn.com/i/o/143564263/c17f8516b74410bf29b05cb2/fpbx5.png?expires=1781167500&signature=7857071255bca485f228fa736194d70b2939ce12ccd3576aeb6e9fffc8000cf9&req=dSQkE896n4dcFb4f3HP0gNWpXCasmWVtjX77qnJY0XQgY%2FaHj13BPTFMmUEP%0A43o%3D%0A)](https://downloads.intercomcdn.com/i/o/143564263/c17f8516b74410bf29b05cb2/fpbx5.png?expires=1781167500&signature=7857071255bca485f228fa736194d70b2939ce12ccd3576aeb6e9fffc8000cf9&req=dSQkE896n4dcFb4f3HP0gNWpXCasmWVtjX77qnJY0XQgY%2FaHj13BPTFMmUEP%0A43o%3D%0A)
5. #### More modules will be updated after successful internet tests.

   [![FreePBX ISO interface for module upload. ](https://downloads.intercomcdn.com/i/o/143564923/20588fda35211533be793648/fpbx6.png?expires=1781167500&signature=d74c32238bb7136f96bbe63411402ec80f272fa8a022fc8af00b26aeed8cb338&req=dSQkE896lINcFb4f3HP0gNjiH1H7ZEiESSw3F53q3Na2%2FzN2%2B3cWTi7i9SMs%0AWTA%3D%0A)](https://downloads.intercomcdn.com/i/o/143564923/20588fda35211533be793648/fpbx6.png?expires=1781167500&signature=d74c32238bb7136f96bbe63411402ec80f272fa8a022fc8af00b26aeed8cb338&req=dSQkE896lINcFb4f3HP0gNjiH1H7ZEiESSw3F53q3Na2%2FzN2%2B3cWTi7i9SMs%0AWTA%3D%0A)
6. #### Enter **root** and the password you created from step 2.

   [![FreePBX ISO interface for password credentials input. ](https://downloads.intercomcdn.com/i/o/143565289/a91f27db12806e28739123af/fpbx7.png?expires=1781167500&signature=3edaa92b8cda1734fc903232cfad235cb2de411c9fa6221c3622f4838e923c5f&req=dSQkE897n4lWFb4f3HP0gPoY1Yb3e2PruZS0YgJ56S2mKG96vsq2tDfOoROt%0AyRg%3D%0A)](https://downloads.intercomcdn.com/i/o/143565289/a91f27db12806e28739123af/fpbx7.png?expires=1781167500&signature=3edaa92b8cda1734fc903232cfad235cb2de411c9fa6221c3622f4838e923c5f&req=dSQkE897n4lWFb4f3HP0gPoY1Yb3e2PruZS0YgJ56S2mKG96vsq2tDfOoROt%0AyRg%3D%0A)
7. #### You'll now be provided with the URL you need to use in order to access the FreePBX web interface.

   [![FreePBX ISO interface for needed login URL. ](https://downloads.intercomcdn.com/i/o/143565361/964fa7c84ed97147519f2a9b/fpbx8.png?expires=1781167500&signature=e9f0f0ac7568cf9ae33883147552035027a28e87fa4afac95e77eb674900e186&req=dSQkE897nodeFb4f3HP0gAmdOGa7S%2BzOayVxqgRFb04%2BakV1dDhMSAapRSIs%0An6g%3D%0A)](https://downloads.intercomcdn.com/i/o/143565361/964fa7c84ed97147519f2a9b/fpbx8.png?expires=1781167500&signature=e9f0f0ac7568cf9ae33883147552035027a28e87fa4afac95e77eb674900e186&req=dSQkE897nodeFb4f3HP0gAmdOGa7S%2BzOayVxqgRFb04%2BakV1dDhMSAapRSIs%0An6g%3D%0A)
8. #### You'll be brought to the initial setup and must enter in the username, password and admin email address in order to create your account.

   [![FreePBX Admin credentials input interface. ](https://downloads.intercomcdn.com/i/o/143565426/ba8fc39099cbedb419b63cc9/fpbx9.png?expires=1781167500&signature=3d1227baaed193dbb1bcbd2f5c4ef15c768eb8945c6a7ae33aff40d020ea1cb8&req=dSQkE897mYNZFb4f3HP0gPNW2NQRTKWoktK2ODYflGqVnJS8X9agWkUMCNpN%0A8r0%3D%0A)](https://downloads.intercomcdn.com/i/o/143565426/ba8fc39099cbedb419b63cc9/fpbx9.png?expires=1781167500&signature=3d1227baaed193dbb1bcbd2f5c4ef15c768eb8945c6a7ae33aff40d020ea1cb8&req=dSQkE897mYNZFb4f3HP0gPNW2NQRTKWoktK2ODYflGqVnJS8X9agWkUMCNpN%0A8r0%3D%0A)
9. #### Once you've created your account, you'll be brought to the dashboard. Select **FreePBX Administration** and enter your username and password.

   [![FreePBX dashboard. ](https://downloads.intercomcdn.com/i/o/143565591/b080b9539b474110e82ba004/fpbx10.png?expires=1781167500&signature=b658b2114faacfdac1adb815dba9e0a39b5cb9e807c0b8af8590f3e2cfb2c024&req=dSQkE897mIheFb4f3HP0gLUdlTKvNeaGz%2FYzcNXJ%2FTSi%2Btd7AeQg6F31lW3J%0Ayl0%3D%0A)](https://downloads.intercomcdn.com/i/o/143565591/b080b9539b474110e82ba004/fpbx10.png?expires=1781167500&signature=b658b2114faacfdac1adb815dba9e0a39b5cb9e807c0b8af8590f3e2cfb2c024&req=dSQkE897mIheFb4f3HP0gLUdlTKvNeaGz%2FYzcNXJ%2FTSi%2Btd7AeQg6F31lW3J%0Ayl0%3D%0A)
10. #### Follow the process to activate your FreePBX V13.

    [![Default locale selection portal. ](https://downloads.intercomcdn.com/i/o/143566230/27f5a23c63080cda42159a3c/fpbx14.png?expires=1781167500&signature=7cfec3089084a51c62cae05e5c2ce77c8bde21650681a18cf0621a86ae35e0a6&req=dSQkE894n4JfFb4f3HP0gFofgQmX%2Bpt4PhLnP%2FK8s5WVd1Dtkdee8wmcRIh3%0AowI%3D%0A)](https://downloads.intercomcdn.com/i/o/143566230/27f5a23c63080cda42159a3c/fpbx14.png?expires=1781167500&signature=7cfec3089084a51c62cae05e5c2ce77c8bde21650681a18cf0621a86ae35e0a6&req=dSQkE894n4JfFb4f3HP0gFofgQmX%2Bpt4PhLnP%2FK8s5WVd1Dtkdee8wmcRIh3%0AowI%3D%0A)
11. #### Select your default locales.

    [![Default locales section. ](https://downloads.intercomcdn.com/i/o/143566311/c173089b1b769d89e5b3e221/fpbx15.png?expires=1781167500&signature=3f6421798c8c508304360bc87b1638f7d0150bf31b0c4c347c27c8d2a06a98b9&req=dSQkE894noBeFb4f3HP0gFh2ewHBYtha12KheQnC17PwUafS%2Bo%2FB7kUkWgeG%0AVCI%3D%0A)](https://downloads.intercomcdn.com/i/o/143566311/c173089b1b769d89e5b3e221/fpbx15.png?expires=1781167500&signature=3f6421798c8c508304360bc87b1638f7d0150bf31b0c4c347c27c8d2a06a98b9&req=dSQkE894noBeFb4f3HP0gFh2ewHBYtha12KheQnC17PwUafS%2Bo%2FB7kUkWgeG%0AVCI%3D%0A)
12. #### You'll be presented with some firewall details and other suggestions. You are welcome to set this up based on your requirements.

[Back to Top](#instructions-to-configure-a-freepbx-pjsip-v13)

## 2. Configure your SIP trunk

The default behavior of FreePBX version 13 is to use chan\_pjsip for endpoints and trunks.

1. Make your way to **Settings > Asterisk SIP Settings** in order to confirm your network settings.
2. You'll want to ensure you populate the **external** and **local** network addresses under **General SIP Settings** and **Chan SIP Settings**.
3. Once you've completed this, click **Submit** and then **Apply Config.**

   [![FreePBX settings section.](https://downloads.intercomcdn.com/i/o/143566942/46b99f394b17b98806e2f3b9/fpbx17.png?expires=1781167500&signature=85572541e4d6ecebddbc7c4c62139e75bb3cf5ef2dfd762e5f776f6af7fee3a9&req=dSQkE894lIVdFb4f3HP0gCExM47wXcv4TFHUJdVzCxlRDY4NkBKWF2SfmfsK%0AgqQ%3D%0A)](https://downloads.intercomcdn.com/i/o/143566942/46b99f394b17b98806e2f3b9/fpbx17.png?expires=1781167500&signature=85572541e4d6ecebddbc7c4c62139e75bb3cf5ef2dfd762e5f776f6af7fee3a9&req=dSQkE894lIVdFb4f3HP0gCExM47wXcv4TFHUJdVzCxlRDY4NkBKWF2SfmfsK%0AgqQ%3D%0A)
4. Now go to **Applications -> Extensions > Add Extension > Add New Chan SIP Extension.** The **Outbound CID** is the [number you purchased](https://portal.telnyx.com/#/app/numbers/my-numbers) from your Telnyx Mission Control Portal. The extensions secret may need to be populated under the **Other** tab.  
   ​  
   ​*Note that if you do not set an Outbound CID for your Extension, you must enable this on your trunk. See the [Pre-requisites](https://support.telnyx.com/en/articles/1130648-configuring-a-freepbx-v13-credentials-trunk#h_b67fe20e22) section.*  
   ​  
   ​*Note: This device uses CHAN\_SIP technology listening on Port 5160 (UDP - this is a NON STANDARD port).*
5. Click **Submit** and **Apply Config.**
6. Navigate to **Settings > Advanced Settings > Dialplan > Operational > SIP Channel Driver**.

   [![FreePBX settings section for advanced settings. ](https://downloads.intercomcdn.com/i/o/37865970/8a09b6bb2f23a4dc60e2a488/File1509332385386?expires=1781167500&signature=f8a14bb8e2afb092eefeebfb38f2fea545dd09d951b8af3a1a8eab3cf53ed24e&req=dycvEMx3moETWLcX3D%2B5hrybLjeFveTuLFTVuk2YuRraB97m47RPFk2VxNCe%0ACA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/37865970/8a09b6bb2f23a4dc60e2a488/File1509332385386?expires=1781167500&signature=f8a14bb8e2afb092eefeebfb38f2fea545dd09d951b8af3a1a8eab3cf53ed24e&req=dycvEMx3moETWLcX3D%2B5hrybLjeFveTuLFTVuk2YuRraB97m47RPFk2VxNCe%0ACA%3D%3D%0A)
7. Navigate to **Connectivity > Trunks** and click on **+Add Trunk** to expand its dropdown.
8. Select **Add SIP (chan\_pjsip)** from this menu.

   [![FreePBX settings section for advanced settings to add SIP. ](https://downloads.intercomcdn.com/i/o/37866087/e3132f22f39caccbac34a24f/image.png?expires=1781167500&signature=20d71da5cc26882759f57cb6afcaf3fa96a9b1b6158e6147df0a0fb1c2af389e&req=dycvEM9%2BlYYTWLcX3D%2B5hnsYZI8WifRUFhSO%2FhfxdPIuBjZ7LoQqkqhKZ16C%0AeQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/37866087/e3132f22f39caccbac34a24f/image.png?expires=1781167500&signature=20d71da5cc26882759f57cb6afcaf3fa96a9b1b6158e6147df0a0fb1c2af389e&req=dycvEM9%2BlYYTWLcX3D%2B5hnsYZI8WifRUFhSO%2FhfxdPIuBjZ7LoQqkqhKZ16C%0AeQ%3D%3D%0A)
9. Click on **General Settings** and provide the following details:

   1. **Trunk Name:** *Telnyx\_userAuth*
   2. **Outbound CallerID:** your\_Telnyx\_number
   3. **CID Options:** *Allow Any CID*

      [![FreePBX settings section for general settings. ](https://downloads.intercomcdn.com/i/o/37866126/0e45f76de72c340d162fe6bf/image.png?expires=1781167500&signature=302bb8c2809de166472d8ad96b0107143ca32c02989d030a23a0e0491992f7b8&req=dycvEM9%2Fn4cTWLcX3D%2B5hnO9WEW9yEUE0SyhET8F3X2YaNNbnqsIOnWxegVx%0Alg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/37866126/0e45f76de72c340d162fe6bf/image.png?expires=1781167500&signature=302bb8c2809de166472d8ad96b0107143ca32c02989d030a23a0e0491992f7b8&req=dycvEM9%2Fn4cTWLcX3D%2B5hnO9WEW9yEUE0SyhET8F3X2YaNNbnqsIOnWxegVx%0Alg%3D%3D%0A)
10. Click on the **Dialed Number Manipulation Rules** tab. You can leave this entire section in its default state, but you can also enter dial patterns here:

    1. **For US numbers:**

       * prepend:*1*; match pattern: *NXXNXXXXXX*
       * prepend: blank; match pattern: *1NXXNXXXXXX*
    2. **For international numbers:**

       * prepend: Country Dialing prefix; match pattern: *NXXNXXXXXX*
       * prepend:blank; match pattern: (Country Dialing prefix)*NXXNXXXXXX*

       [![Dialed manipulation rules tab. ](https://downloads.intercomcdn.com/i/o/37866147/47680e1ab6f82d8f24482d28/image.png?expires=1781167500&signature=07be65d6484e8f74a39941a19b10a7880d92a956a1542d324aad7341722191e5&req=dycvEM9%2FmYYTWLcX3D%2B5hus7SqBkXU1coZii%2Bx9svHRttz1xnFumLVLw%2BdSB%0Amw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/37866147/47680e1ab6f82d8f24482d28/image.png?expires=1781167500&signature=07be65d6484e8f74a39941a19b10a7880d92a956a1542d324aad7341722191e5&req=dycvEM9%2FmYYTWLcX3D%2B5hus7SqBkXU1coZii%2Bx9svHRttz1xnFumLVLw%2BdSB%0Amw%3D%3D%0A)
11. Click on the **PJSIP Settings** tab and on the **General** sub-tab.  
    ​

    ### Provide the Following Properties:

    1. **Username :** Your Telnyx account username
    2. **Secret :** The password for your Telnyx trunk found under the connection → "show password" link in your Telnyx portal
    3. **Authentication :** *Outbound*
    4. **Registration :** *Send*
    5. **Language Code :** *English* (or the language you wish to conduct calls in)
    6. **SIP Server :** *[Sip.telnyx.com](https://sip.telnyx.com/)*
    7. **SIP Server Port :** *5060* if you have not enabled TLS encryption. If you have, choose *5061*.
    8. **Context :** *from-pstn*
    9. **Transport :** *UDP* or *TCP* if you have not enabled TLS encryption. If you have, choose *TLS/TCP*.

       [![General sub-tab of the PJSIP Settings.  ](https://downloads.intercomcdn.com/i/o/37866231/797101285257b35507530b97/image.png?expires=1781167500&signature=5a65aa8f34cb35a7ed214a71fe9d5518344a9917309db49ffb9f29c36ce566ec&req=dycvEM98noATWLcX3D%2B5hmxqZg2mfouBrN86FP8jQ4XehivRU4hcz99FAzJz%0ApQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/37866231/797101285257b35507530b97/image.png?expires=1781167500&signature=5a65aa8f34cb35a7ed214a71fe9d5518344a9917309db49ffb9f29c36ce566ec&req=dycvEM98noATWLcX3D%2B5hmxqZg2mfouBrN86FP8jQ4XehivRU4hcz99FAzJz%0ApQ%3D%3D%0A)
12. Open the **PJSIP Settings > Advanced** sub-tab and adjust the following:

    1. **From Domain:** *sip.telnyx.com*

       [![Advanced settings tab of PJSIP Settings. ](https://downloads.intercomcdn.com/i/o/37866242/52b248dcb74af63e7449eb3e/image.png?expires=1781167500&signature=11076d15c1d122e9254d0d53f3abc266d106ad8d1e46ac8a4986ad292602dae6&req=dycvEM98mYMTWLcX3D%2B5hruNiWhOd%2FmPfyikNYNl%2FPyBupLTUEYcj4fVdDEK%0AMQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/37866242/52b248dcb74af63e7449eb3e/image.png?expires=1781167500&signature=11076d15c1d122e9254d0d53f3abc266d106ad8d1e46ac8a4986ad292602dae6&req=dycvEM98mYMTWLcX3D%2B5hruNiWhOd%2FmPfyikNYNl%2FPyBupLTUEYcj4fVdDEK%0AMQ%3D%3D%0A)
13. Open the **PJSIP Settings > Codecs** sub-tab and adjust the following:

    1. Select *ulaw, alaw, gsm, g722, g729, Opus*. All other boxes should be unchecked, as these are the Telnyx-supported codecs.
    2. If you plan to do any video communication, Telnyx supports the H264 video codec.

       [![Codecs settings section of the PJSIP Settings. ](https://downloads.intercomcdn.com/i/o/37866261/c040f5186b656185e846f7d4/image.png?expires=1781167500&signature=8c742c307d5a77701ae733d85df4db2ffb396e74300586e178430e40d8e943a9&req=dycvEM98m4ATWLcX3D%2B5htpmdZ%2BfHVT4wzVCq9EYCIPqAoWbe2zeNTjSHf6T%0Amg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/37866261/c040f5186b656185e846f7d4/image.png?expires=1781167500&signature=8c742c307d5a77701ae733d85df4db2ffb396e74300586e178430e40d8e943a9&req=dycvEM98m4ATWLcX3D%2B5htpmdZ%2BfHVT4wzVCq9EYCIPqAoWbe2zeNTjSHf6T%0Amg%3D%3D%0A)
14. Click **Submit**, then **Apply Config**.

[Back to Top](#instructions-to-configure-a-freepbx-pjsip-v13)

## 3. Configure outbound routes

Outbound routing is a set of rules that tells FreePBX which Telnyx trunk to use for any given outbound call. Having multiple trunks allows you to control cost by routing calls over the least costly trunk for a particular call. Outbound routes are used to specify what numbers are allowed to go out a particular route.

You will want to make sure you define routes for all types of calls. Not defining a route can leave your users frustrated when they need to make an important call.

1. Navigate to **Connectivity -> Outbound Routes.**
2. Create a new outbound route and provide the following on the **Route Settings** tab:

   1. **Route Name:** Something distinct that makes sense for your route purpose.
   2. **Trunk Sequence for Matched Routes:** Select the trunk you just created in [section 2](#chanpjsip-trunkconfiguration).
   3. **Route Name :** *Outbound\_Telnyx*
   4. **Route CID :**  Number you purchased on the Telnyx portal.
   5. **Trunk Sequence for Matched Routes :** Select the trunk you just created in [section 2](#chanpjsip-trunkconfiguration).

      [![Outbound rates configuration settings. ](https://downloads.intercomcdn.com/i/o/37866289/631df98764609ec42d5163d4/image.png?expires=1781167500&signature=3d873a5c12f6136b53a0acd638201ff3ed492d4958d624e7211d2365fd967c3d&req=dycvEM98lYgTWLcX3D%2B5hgZkQuTIGRE8GsNdwsAvXvjhSjY5w9OkCeqOaIoV%0Aqw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/37866289/631df98764609ec42d5163d4/image.png?expires=1781167500&signature=3d873a5c12f6136b53a0acd638201ff3ed492d4958d624e7211d2365fd967c3d&req=dycvEM98lYgTWLcX3D%2B5hgZkQuTIGRE8GsNdwsAvXvjhSjY5w9OkCeqOaIoV%0Aqw%3D%3D%0A)
3. Now select the **Dial Patterns** tab to the right of the **Route Settings** tab and enter dial patterns exactly as you see in the following image. This pattern allows you to dial 10 Digits (U.S. Calling), 11 Digits (North American Calling).   
   ​  
   ​*If you need dial patterns for a region outside North America, please contact Telnyx support.*

   [![Dial patterns section of outbound rates. ](https://downloads.intercomcdn.com/i/o/37866302/3653d04099f1ae33e9694a84/image.png?expires=1781167500&signature=b88894acc05787e012f1aad882c14d25d00c688a37c77c9e824d5fb458a6b0fe&req=dycvEM99nYMTWLcX3D%2B5hmxvkgBBZbIuxHhIbXgCL%2FB1Mhsgv2eCvqv30VfV%0AzQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/37866302/3653d04099f1ae33e9694a84/image.png?expires=1781167500&signature=b88894acc05787e012f1aad882c14d25d00c688a37c77c9e824d5fb458a6b0fe&req=dycvEM99nYMTWLcX3D%2B5hmxvkgBBZbIuxHhIbXgCL%2FB1Mhsgv2eCvqv30VfV%0AzQ%3D%3D%0A)

   ***Note*** *that our current documentation portal shrinks screenshots, making some detail difficult to see. Right-click on the image above and select "Open image in new tab" from the context menu. This will open the image in a new tab and display it at its full size and resolution.*  
   ​
4. Click **Submit**, then **Apply Config**.

[Back to Top](#instructions-to-configure-a-freepbx-pjsip-v13)

## 4. Configure inbound routes

When a call comes in from the outside, it'll need to be directed from sip.telnyx.com to the phone extension you ultimately want it to go, such as a user extension or an IVR extension.

In this section, we'll configure our own inbound routes.

1. Make your way to **Connectivity -> Inbound Routes** and open the **General** tab.
2. The following image demonstrates an inbound route that will send *ANY* call to a certain extension.   
   ​  
   To direct a specific number to a specific extension you would create a route and set the "[DID Number](https://telnyx.com/resources/sip-did)" field to your 11 digit DID with sip.telnyx.com (for instance : [12172031700](http://#)).

[![Inbound routes configuration section. ](https://downloads.intercomcdn.com/i/o/37866320/8ed4a7441a9a0494c5923aaa/image.png?expires=1781167500&signature=8ba1bc47d411e974eee60ddc6144fb4a172b5bc247c857253b3f966027aa0a27&req=dycvEM99n4ETWLcX3D%2B5huiVEoi54mHNZbHZ0CU2lCPc2TPnyZPQN%2Fqx6%2F5u%0AGh%2FIvSLtLeElEeC2%0A)](https://downloads.intercomcdn.com/i/o/37866320/8ed4a7441a9a0494c5923aaa/image.png?expires=1781167500&signature=8ba1bc47d411e974eee60ddc6144fb4a172b5bc247c857253b3f966027aa0a27&req=dycvEM99n4ETWLcX3D%2B5huiVEoi54mHNZbHZ0CU2lCPc2TPnyZPQN%2Fqx6%2F5u%0AGh%2FIvSLtLeElEeC2%0A)

|  |
| --- |
| ***Note:*** *By default, when creating a SIP Connection in the Telnyx Mission Control Portal, the number formats for the ANI and DNIS will be set to E.164. This means Telnyx will send the dialled number in the SIP INVITE to your FreePBX system with 11 digits. As the DID number above is in 11 digit format, the call will be accepted and routed to the extension. However, you can control the number formats as you desire and can read more about it [here](https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats).* |

That's it, you've now completed the configuration of FreePBX PJSIP V13 Credentials Trunk and can now make and receive calls by using Telnyx as your SIP provider.

[Back to Top](#instructions-to-configure-a-freepbx-pjsip-v13)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally, you can check out:

* [FreePBX documentation](https://wiki.freepbx.org/#all-updates)
* [FreePBX community](https://community.freepbx.org/)
* [FreePBX support](https://www.freepbx.org/support/)
* [FreePBX videos](https://www.freepbx.org/videos/)

---

---

Related Articles

[Configuring a FreePBX V13 Credentials Trunk](https://support.telnyx.com/en/articles/1130648-configuring-a-freepbx-v13-credentials-trunk)[FreePBX V14: Credentials - ChanSIP](https://support.telnyx.com/en/articles/3284752-freepbx-v14-credentials-chansip)[FreePBX V15 IP Trunk - ChanSIP Tutorial](https://support.telnyx.com/en/articles/5467232-freepbx-v15-ip-trunk-chansip-tutorial)[FreePBX V15: IP Trunk - PJSIP](https://support.telnyx.com/en/articles/5619595-freepbx-v15-ip-trunk-pjsip)[FreePBX V15: Credentials - PJSIP](https://support.telnyx.com/en/articles/5619597-freepbx-v15-credentials-pjsip)

Did this answer your question?

😞😐😃

Table of contents
