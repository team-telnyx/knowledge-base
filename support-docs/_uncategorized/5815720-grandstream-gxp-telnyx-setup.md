---
source_url: https://support.telnyx.com/en/articles/5815720-grandstream-gxp-telnyx-setup
scraped: 2026-06-11
---

Grandstream GXP: Telnyx Setup | Telnyx Help Center

[Skip to main content](#main-content)

# Grandstream GXP: Telnyx Setup

Learn how to set up and configure a Grandstream GXP1630/GXP2135 IP Phone and connect it to your Telnyx account.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_5a7ed2c3f5)

|  |  |
| --- | --- |
| Grandstream GXP1630 | Grandstream GXP2135 |
| Our most powerful entry-level Basic IP phone, the [GXP1630](https://www.grandstream.com/products/ip-voice-telephony-gxp-series-ip-phones/gxp-series-basic-ip-phones/product/gxp1630) delivers an effective communications platform for access to quick call control. Delivering a vibrant and clear user-interface, this device is a perfect solution for those who handle low to medium call volume and require access to key call efficiency functionalities. | The [Grandstream GXP2135](https://www.grandstream.com/products/ip-voice-telephony-gxp-series-ip-phones/gxp-series-high-end-ip-phones/product/gxp2135) is the ideal selection for busy users who value call control, productivity and usability, and manage medium to heavy call volumes. Equipped with 8 lines and 4 SIP accounts, a 2.8 inch color LCD display, and 32 digital speed dial/BLF keys, the GXP2135 enables quick and powerful usability.    As all Grandstream IP phones do, the GXP2135 features state-of-the-art security encryption technology (SRTP and TLS). The GXP2135 supports a variety of automated provisioning options, including zero-configuration with Grandstream’s UCM series IP PBXs, encrypted XML files and TR-069, to make mass deployment extremely easy. |
| It boasts such features as:  * 3 SIP accounts, 3 line keys, 4-way conferencing, 3 XML programmable context-sensitive soft keys * HD audio on speakerphone and handset * Dual-switched Gigabit ports, integrated PoE * 8 dual-colored BLF/speed dial keys * EHS support for Plantronics headsets * Up to 1000 contacts, call history up to 200 records  Additional documentation:  * [GXP1630 user guide](https://www.grandstream.com/hubfs/Product_Documentation/gxp16xx_user_guide.pdf) * [GXP1630 Admin manual](https://www.grandstream.com/hubfs/Product_Documentation/gxp16xx_administration_guide.pdf) | It boasts such features as:  * 8 lines, 4 SIP accounts, 4 XML programmable context-sensitive soft keys * Dual switched, auto-sensing Gigabit ports, built-in PoE * 32 digitally programmable and customizable BLF/speed-dial keys * Built-in Bluetooth for syncing headsets and mobile devices for contact books, calendars & call transferring * HD audio on the handset and speakerphone; full duplex speakerphone * Supports EHS compatible Plantronics headsets * 4-way audio conferencing for easy conference calls  Additional documentation:  * [GXP2135 product documentation](https://www.grandstream.com/hubfs/Product_Documentation/gxp21xx_user_guide.pdf) * [GXP2135 user manual](https://www.grandstream.com/hubfs/Product_Documentation/gxp2130_gxp2140_gxp2160_gxp2135_gxp2170_quick_user_guide_english..pdf) * [GXP2135 admin manual](https://www.grandstream.com/hubfs/Product_Documentation/gxp21xx_administration_guide.pdf) |

---

# Instructions for configuring the Grandstream GXP IP Phone to work with Telnyx

|  |
| --- |
| ***Note:*** *The configuration steps for both the Grandstream GXP1630 and the GXP2135 are identical. This guide will satisfy the setup and configuration of either.* |

In this activity you will:

1. [Get your device's IP address and log into the Gigaset phone's web portal](#h_988037d0d8)
2. [Configure your GXP](#h_cf2677162e)

## Pre-requisites

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)

## Video Walkthrough

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Grandstream GXP/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Get your device's IP address and log into your phone's web portal

In this step, you'll obtain the IP address from your GXP, which you'll need to log into the web portal in the next step.

1. From your phone, navigate to **Menu >> Status >­> Network Status >> IPv4 Address** and take note of the IP address on this screen. You'll need it next.
2. On a computer connected to the same network as your phone, open a web browser and type *http://* followed by the phone's IP address into the address bar of your browser.
3. Log into the portal. Out of the box, the default credentials are:

   1. **Username:** *admin*
   2. **Password:** *admin*

   [![Grandstream portal entry. ](https://downloads.intercomcdn.com/i/o/435418196/02c366f53df95203841c95e3/Screen+Shot+2021-12-16+at+10.08.50.png?expires=1781168400&signature=8a941d7189884cd4ca9c287c7aed3c0e4f4b6a2ffbf1c960d48b7662066751ce&req=cCMiEsh2nIhZFb4f3HP0gLaecVmmRK8UukorrvdJ%2F%2Be%2FuNK10p%2BuhmTyotDM%0Ap1M%3D%0A)](https://downloads.intercomcdn.com/i/o/435418196/02c366f53df95203841c95e3/Screen+Shot+2021-12-16+at+10.08.50.png?expires=1781168400&signature=8a941d7189884cd4ca9c287c7aed3c0e4f4b6a2ffbf1c960d48b7662066751ce&req=cCMiEsh2nIhZFb4f3HP0gLaecVmmRK8UukorrvdJ%2F%2Be%2FuNK10p%2BuhmTyotDM%0Ap1M%3D%0A)

[Back to Top](#h_5a7ed2c3f5)

## 2. Configure your Grandstream GXP

In this step, you'll create a [SIP trunk](https://telnyx.com/products/sip-trunks) and connect your phone to Telnyx.

1. Click on **Accounts** in the top menu.
2. Expand the account you're looking to configure and click **General Settings**.

   [![Account general settings. ](https://downloads.intercomcdn.com/i/o/435413302/72675efc348bbedd82f0f830/Screen+Shot+2021-12-16+at+10.11.27.png?expires=1781168400&signature=ba3c2f152aff5ea1128991d79d579de351a294111a4c0e7aacb3127ce6e34bb5&req=cCMiEsh9noFdFb4f3HP0gGQCkPHH4%2FdGsJK8kAFlJrP13zNFTxl2nsLjFdMd%0ASNQ%3D%0A)](https://downloads.intercomcdn.com/i/o/435413302/72675efc348bbedd82f0f830/Screen+Shot+2021-12-16+at+10.11.27.png?expires=1781168400&signature=ba3c2f152aff5ea1128991d79d579de351a294111a4c0e7aacb3127ce6e34bb5&req=cCMiEsh9noFdFb4f3HP0gGQCkPHH4%2FdGsJK8kAFlJrP13zNFTxl2nsLjFdMd%0ASNQ%3D%0A)

   You can also use the top navigation to get here if you want.

   [![General settings button.](https://downloads.intercomcdn.com/i/o/435414420/36868141641ca73005f21a40/Screen+Shot+2021-12-16+at+10.12.43.png?expires=1781168400&signature=0a5e62e528d2f2d8e7057316b3e8c42c00cf1d0eedae7e7de6ad1cc63a7a0ad9&req=cCMiEsh6mYNfFb4f3HP0gLXexb2BULgLw7a%2FfeVuE3pD7K2MIdfqSRg4g6PF%0A0mo%3D%0A)](https://downloads.intercomcdn.com/i/o/435414420/36868141641ca73005f21a40/Screen+Shot+2021-12-16+at+10.12.43.png?expires=1781168400&signature=0a5e62e528d2f2d8e7057316b3e8c42c00cf1d0eedae7e7de6ad1cc63a7a0ad9&req=cCMiEsh6mYNfFb4f3HP0gLXexb2BULgLw7a%2FfeVuE3pD7K2MIdfqSRg4g6PF%0A0mo%3D%0A)
3. On this page, enter the following information:

   1. **Account Name:** Give it a name that makes sense for you

      **SIP Server:** *sip.telnyx.com*

      **SIP User ID:** Your Telnyx SIP account username

      **Authenticate Password:** Your Telnyx SIP account password

      **Name:** This is your caller ID. You can choose whatever you like, but keep in mind the following naming conventions:

      1. Caller ID Name should be in capital letters. This will appears more clearly/visible on some devices.
      2. You must NOT use any special characters, as they will not be displayed. Spaces are allowed.
      3. Some of regular Canadian providers will not show more than 15 characters. We suggest shrinking or adapt your caller ID.
   2. **Voice Mail Access Number:** *\*97*

   [![General settings in the accounts section. ](https://downloads.intercomcdn.com/i/o/435388621/6c92ce9aad27d05f92aa0aab/1.png?expires=1781168400&signature=b359e477afe17a21b06acaf56306c931256c8a64cde3c2899f8e8259d1cb1576&req=cCMiFcF2m4NeFb4f3HP0gC84j3auftlg7OjergSROmxa%2B1Fa77ztr49j1Rk9%0Ae0Q%3D%0A)](https://downloads.intercomcdn.com/i/o/435388621/6c92ce9aad27d05f92aa0aab/1.png?expires=1781168400&signature=b359e477afe17a21b06acaf56306c931256c8a64cde3c2899f8e8259d1cb1576&req=cCMiFcF2m4NeFb4f3HP0gC84j3auftlg7OjergSROmxa%2B1Fa77ztr49j1Rk9%0Ae0Q%3D%0A)
4. Now, while still in **Accounts > Account 1** *(or the account you want to configure)* click on **SIP Settings > Basic Settings** and provide the following information:

   1. **SIP Registration:** *Yes*
   2. **Register Expiration:** *5* (this is in minutes)
   3. **Enable OPTIONS Keep Alive:** *Yes*
   4. **Local SIP Port:** *5060* if you have not enabled TLS encryption. If you have, choose *5061*.
   5. **SIP Transport:** *UDP* or *TCP* if you have not enabled TLS encryption. If you have, choose *TLS/TCP*.

   [![Accounts section.](https://downloads.intercomcdn.com/i/o/435393594/7e8bba33df0f0fd6860a99c4/Screen+Shot+2021-12-16+at+09.44.39.png?expires=1781168400&signature=c49fe2b909b327f80ed6dc10f5e03970683de792d19ffb743a533145041b59f8&req=cCMiFcB9mIhbFb4f3HP0gFetkPtT2JLOTPcaGBGZUwqJaXoCmaYTE4JbfLpu%0A0w4%3D%0A)](https://downloads.intercomcdn.com/i/o/435393594/7e8bba33df0f0fd6860a99c4/Screen+Shot+2021-12-16+at+09.44.39.png?expires=1781168400&signature=c49fe2b909b327f80ed6dc10f5e03970683de792d19ffb743a533145041b59f8&req=cCMiFcB9mIhbFb4f3HP0gFetkPtT2JLOTPcaGBGZUwqJaXoCmaYTE4JbfLpu%0A0w4%3D%0A)

   \*This screenshot demonstrates a connection that uses UDP transport.
5. Click **Save and Apply.**

That's it! You've finished configuring your Grandstream GXP profile, and can now start testing calls!

[Back to Top](#h_5a7ed2c3f5)

---

## Troubleshooting

## "I can receive incoming calls, but outgoing call are failing. The error says 'No response'"

**Answer**

1. Log into the web portal and navigate to **Accounts > Account X > SIP > Custom SIP Header** and *disable*:

   1. **Use X-Grandstream-PBX Header**
   2. **Use P-Access-Network-Info Header**
   3. **Use P-Emergency-Info Header**
2. Go to **Accounts > Account X > SIP > Audio Settings,** and choose codec *G729A/B* as preferred Vocoder.

[Back to Top](#h_5a7ed2c3f5)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [GXP1630 user guide](https://www.grandstream.com/hubfs/Product_Documentation/gxp16xx_user_guide.pdf)
* [GXP1630 Admin manual](https://www.grandstream.com/hubfs/Product_Documentation/gxp16xx_administration_guide.pdf)
* [GXP2135 product documentation](https://www.grandstream.com/hubfs/Product_Documentation/gxp21xx_user_guide.pdf)
* [GXP2135 user manual](https://www.grandstream.com/hubfs/Product_Documentation/gxp2130_gxp2140_gxp2160_gxp2135_gxp2170_quick_user_guide_english..pdf)
* [GXP2135 admin manual](https://www.grandstream.com/hubfs/Product_Documentation/gxp21xx_administration_guide.pdf)

---

Related Articles

[Configuring Grandstream GXP16XX with Telnyx](https://support.telnyx.com/en/articles/1130660-configuring-grandstream-gxp16xx-with-telnyx)[Grandstream: IP Auth Setup](https://support.telnyx.com/en/articles/2950523-grandstream-ip-auth-setup)[Grandstream HT802: Telnyx Setup](https://support.telnyx.com/en/articles/5725071-grandstream-ht802-telnyx-setup)[Grandstream GXP21XX](https://support.telnyx.com/en/articles/5819218-grandstream-gxp21xx)[Grandstream GXP1700: SIP Trunk](https://support.telnyx.com/en/articles/6184520-grandstream-gxp1700-sip-trunk)

Did this answer your question?

😞😐😃

Table of contents
