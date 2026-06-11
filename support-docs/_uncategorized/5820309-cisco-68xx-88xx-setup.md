---
source_url: https://support.telnyx.com/en/articles/5820309-cisco-68xx-88xx-setup
scraped: 2026-06-11
---

Cisco: 68xx/88xx Setup | Telnyx Help Center

[Skip to main content](#main-content)

# Cisco: 68xx/88xx Setup

Learn how to configure a Cisco 68xx/88xx series IP phone to worth with Telnyx.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_0a462c8775)

The Cisco [68xx](https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-6800-series-multiplatform-firmware/series.html) and [88xx](https://www.cisco.com/c/en/us/products/collaboration-endpoints/unified-ip-phone-8800-series/index.html?dtid=osscdc000283) series are a great fit for businesses of all sizes seeking secure, high-quality, full-featured VoIP. Select models provide affordable entry to HD video and support for highly-active, in-campus mobile workers. This advanced series provides flexible deployment options for Cisco pre-approved third-party [UCaaS](https://telnyx.com/resources/ucaas) providers

These multiplatform phones are designed for affordability. They deliver reliable, business-grade audio, with Gigabit Ethernet integration and low power usage. Ideal for customers with moderate to active VoIP needs, the 68xx/88xx series phones are supported on Cisco-approved third-party unified communications as a service (UCaaS) providers.

Additional documentation:

* [Product support](https://www.cisco.com/c/en/us/support/all-products.html)
* [The Cisco Community](https://community.cisco.com/t5/technology-and-support/ct-p/technology-support)
* [Cisco documentation](https://software.cisco.com/portal/pub/download/portal/select.html?&i=!m&mdfid=284729655) Use the filters to find what you need

---

# Instructions for setting up and configuring your Cisco 68xx/88xx

|  |
| --- |
| **Note:** *The setup and configuration of the Cisco 68xx and 88xx series are identical. This guide will satisfy both.* |

In this activity you will:

1. [Get your device's IP address and log into the phone's web portal](#h_72f38f8299)
2. [Configure a SIP extension](#h_3316ae63fb)
3. (FOR TLS EXTENSIONS ONLY) [Configure additional security settings](#h_d40966aa01)

**Pre-requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
* (FOR ACCOUNTS USING TLS) You may need to provide a TLS certificate. You can [obtain it here](https://crt.sh/?id=1199354).

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Cisco 68xx or 88xx/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Get your device's IP address and log into your phone's web portal

In this step, you'll obtain the IP address from your Cisco phone, which you'll need to log into the web portal in the next step.

1. From your phone, click on the **Menu** button on the phone and navigate to **Network Status >­ IPv4 Address** and take note of the IP address on this screen. You'll need it next.
2. On a computer connected to the same network as your phone, open a web browser and type *http://* followed by the phone's IP address into the address bar of your browser.
3. Log into the portal. Out of the box, you can just skip the login credentials the first time by pressing **Skip**.

[Back to Top](#h_0a462c8775)

## 2. Configure a SIP extension

In this section, you'll configure your extension and connect your phone to Telnyx.

1. Click on the **Voice** tab at the top. Then click on the tab showing the extension you want to configure.
2. Find the **General and NAT Settings** section and enter the following information:

   1. **Line Enable:** *Yes*
   2. **NAT Mapping Enable**: *Yes*
   3. **NAT Keep Alive Enable**: *Yes*
3. Find the **SIP Settings** section and enter the following information:

   1. **SIP Transport**: *UDP* or *TCP* if you have not enabled TLS encryption. If you have, choose *TLS*.
   2. **SIP Port**: *5060* if you have not enabled TLS encryption. If you have, choose *5061*.

   [![General and NAT Settings section](https://downloads.intercomcdn.com/i/o/435991238/4cbe3d9acda54fb665f80232/0sip.png?expires=1781168400&signature=7a23245c6b4ee87cfb9367c681aea3efdc27ae4e4b8f83c1f55fa731b75fe743&req=cCMiH8B%2Fn4JXFb4f3HP0gFPRBXlnZxq62OfDCHUw8Mlnfe%2FgT1Wc17Qkb6NU%0AdRY%3D%0A)](https://downloads.intercomcdn.com/i/o/435991238/4cbe3d9acda54fb665f80232/0sip.png?expires=1781168400&signature=7a23245c6b4ee87cfb9367c681aea3efdc27ae4e4b8f83c1f55fa731b75fe743&req=cCMiH8B%2Fn4JXFb4f3HP0gFPRBXlnZxq62OfDCHUw8Mlnfe%2FgT1Wc17Qkb6NU%0AdRY%3D%0A)
4. Find the **Proxy and Registration** section and enter the following information:

   1. **Proxy**: *sip.telnyx.com*
   2. **Outbound Proxy**: *sip.telnyx.com*
   3. **Register**: *Yes*
   4. **Register Expires**: *300*
5. Find the **Subscriber Information** section and enter the following information:

   1. **Display Name**: This is your caller ID. You can choose whatever you like, but keep in mind the following naming conventions:

      1. Caller ID Name should be in capital letters. This will appears more clearly/visible on some devices.
      2. You must NOT use any special characters, as they will not be displayed. Spaces are allowed.
      3. Some of regular Canadian providers will not show more than 15 characters. We suggest shrinking or adapt your caller ID.
   2. **User ID**: Your Telnyx account ID
   3. **Password**: Your Telnyx account password
   4. **Auth ID**: Your Telnyx account ID

   [![Subscriber Information section](https://downloads.intercomcdn.com/i/o/435991490/e319880857fb3bbeb86c78d3/1SIP.png?expires=1781168400&signature=314d79e9851357af66733f78e6d408a542ef2792190b39c0b615381b4e49eb07&req=cCMiH8B%2FmYhfFb4f3HP0gH2p%2FFeK3aT0U3pfKsQ9MxMZ%2Bo3wpGNFH6srrNQK%0AyRw%3D%0A)](https://downloads.intercomcdn.com/i/o/435991490/e319880857fb3bbeb86c78d3/1SIP.png?expires=1781168400&signature=314d79e9851357af66733f78e6d408a542ef2792190b39c0b615381b4e49eb07&req=cCMiH8B%2FmYhfFb4f3HP0gH2p%2FFeK3aT0U3pfKsQ9MxMZ%2Bo3wpGNFH6srrNQK%0AyRw%3D%0A)
6. Find the **Audio Configuration** section and set your codecs in priority sequence that meets your needs.   
   ​  
   Telnyx supports the following [audio codecs](https://telnyx.com/resources/codecs-affect-voip-sound-quality):

   1. ulaw(g711u)
   2. alaw(g711a)
   3. g722
   4. g729

   Additionally, if you are using TLS encryption, verify the following:

   1. **Encryption Method**: *AES128*

   [![Audio configuration section. ](https://downloads.intercomcdn.com/i/o/435991894/5c3e3c294211b240a93eeb76/2sip.png?expires=1781168400&signature=b0a42bf58bb482dc3b7d36e5ecb75fb2c6eb68062b05c73c822ff5a1ebefd2a4&req=cCMiH8B%2FlYhbFb4f3HP0gMCaKkDgVr%2FERdZGtk%2FuObmgp5zZpDF2w8qrSwBJ%0Ahq4%3D%0A)](https://downloads.intercomcdn.com/i/o/435991894/5c3e3c294211b240a93eeb76/2sip.png?expires=1781168400&signature=b0a42bf58bb482dc3b7d36e5ecb75fb2c6eb68062b05c73c822ff5a1ebefd2a4&req=cCMiH8B%2FlYhbFb4f3HP0gMCaKkDgVr%2FERdZGtk%2FuObmgp5zZpDF2w8qrSwBJ%0Ahq4%3D%0A)

   [![Audio Configuration section](https://downloads.intercomcdn.com/i/o/435992337/214ca898895068bcbf400004/4aes.png?expires=1781168400&signature=5c658e35ca5191cde60bb98b3c2c36ea2e5ec46125fe54fb5e8e26a6c3fb8c10&req=cCMiH8B8noJYFb4f3HP0gNTFBcpR0p%2B72vpv%2FS0M3DvA%2BmgG3V6i0%2FShPwqN%0AGFg%3D%0A)](https://downloads.intercomcdn.com/i/o/435992337/214ca898895068bcbf400004/4aes.png?expires=1781168400&signature=5c658e35ca5191cde60bb98b3c2c36ea2e5ec46125fe54fb5e8e26a6c3fb8c10&req=cCMiH8B8noJYFb4f3HP0gNTFBcpR0p%2B72vpv%2FS0M3DvA%2BmgG3V6i0%2FShPwqN%0AGFg%3D%0A)

[Back to Top](#h_0a462c8775)

## 3. (FOR TLS EXTENSIONS ONLY) Additional security settings

If you have configured your profile for TLS call encryption, you'll need to ensure you have secure calling turned on. Additionally, some Cisco devices require you to have uploaded a TLS certificate (such as the 6821).

1. Click on the **Voice** tab at the top. Then click on the **User** sub-tab.
2. Find the **Supplementary Services** section and set the following:

   1. **Secure Call Setting:** *Yes*

   [![Supplementary Services section](https://downloads.intercomcdn.com/i/o/435993185/93d788021b237829ce384ae9/5user.png?expires=1781168400&signature=c075cce22757d05843f63f88a6506ddca969b2061e859d9f60aa5b11b0707085&req=cCMiH8B9nIlaFb4f3HP0gELaY2q5P0cP0pGCFu1r6%2FV3uPgkAjJjox83CIyr%0AiC4%3D%0A)](https://downloads.intercomcdn.com/i/o/435993185/93d788021b237829ce384ae9/5user.png?expires=1781168400&signature=c075cce22757d05843f63f88a6506ddca969b2061e859d9f60aa5b11b0707085&req=cCMiH8B9nIlaFb4f3HP0gELaY2q5P0cP0pGCFu1r6%2FV3uPgkAjJjox83CIyr%0AiC4%3D%0A)
3. You only need to complete this step if your device requires a TLS certificate. Find the certificate [here](https://crt.sh/?id=1199354) if you have not done so already. While still on the **Voice** tab, click on the **Provisioning** sub-tab.
4. Paste the certificate link in the **Custom CA Rule** field.  
   ​

   [![Custom CA Rule field](https://downloads.intercomcdn.com/i/o/435994901/497c41840f3832a8daf56ae6/6provisioning.png?expires=1781168400&signature=62b1cba5ddb1621628d63e36aeff4663d668b0ae55eb437d41ecf787bad4ed69&req=cCMiH8B6lIFeFb4f3HP0gEIQiiWnb0sTRUHYtCIzwFE2PdO%2FW5rTAyGt%2FAd6%0Ac5c%3D%0A)](https://downloads.intercomcdn.com/i/o/435994901/497c41840f3832a8daf56ae6/6provisioning.png?expires=1781168400&signature=62b1cba5ddb1621628d63e36aeff4663d668b0ae55eb437d41ecf787bad4ed69&req=cCMiH8B6lIFeFb4f3HP0gEIQiiWnb0sTRUHYtCIzwFE2PdO%2FW5rTAyGt%2FAd6%0Ac5c%3D%0A)
5. Once you're done, click the **Submit All Changes** button at the bottom of the screen. You'll get a *Phone is updating configuration* message. ***Do not unplug the phone during this state.*** After a few seconds, the device will be ready.

That's it! You've finished configuring your 68xx/88xx series phone profile, and can now start testing calls!

[Back to Top](#h_0a462c8775)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly!

Additionally, check out:

* [Product support](https://www.cisco.com/c/en/us/support/all-products.html)
* [The Cisco Community](https://community.cisco.com/t5/technology-and-support/ct-p/technology-support)
* [Cisco documentation](https://software.cisco.com/portal/pub/download/portal/select.html?&i=!m&mdfid=284729655) Use the filters to find what you need

---

---

Related Articles

[Configuring your Cisco SPA112/122 ATA](https://support.telnyx.com/en/articles/1130665-configuring-your-cisco-spa112-122-ata)[Snom D7xx: Telnyx Setup](https://support.telnyx.com/en/articles/5822706-snom-d7xx-telnyx-setup)[Grandstream GRP260x: SIP Trunk](https://support.telnyx.com/en/articles/6169513-grandstream-grp260x-sip-trunk)[Fanvil X2CP/X2C/X2P: Call Center IP](https://support.telnyx.com/en/articles/6206756-fanvil-x2cp-x2c-x2p-call-center-ip)[Fanvil X-Series: IP Phone](https://support.telnyx.com/en/articles/6209971-fanvil-x-series-ip-phone)

Did this answer your question?

😞😐😃

Table of contents
