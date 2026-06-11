---
source_url: https://support.telnyx.com/en/articles/5819218-grandstream-gxp21xx
scraped: 2026-06-11
---

Grandstream GXP21XX | Telnyx Help Center

[Skip to main content](#main-content)

# Grandstream GXP21XX

Learn how to set up and configure a Grandstream GXP21XX (2135, 2170) IP Phone and connect it to your Telnyx account.

C

Written by Customer Success

January 10, 2024

Table of contents

---

[Jump to Instructions](#h_840e813c4e)

The [Grandstream GXP21XX](https://www.grandstream.com/products/ip-voice-telephony-gxp-series-ip-phones/gxp-series-high-end-ip-phones/product/gxp2170) is a powerful, high-end suite of IP phones ideal for busy users who handle high call volumes. Receptionists, administrators, sales staff and other call-intensive rolls can enjoy efficiency by utilizing the GXP21XX’s 12 line keys, 4.3 inch color display LCD and 48 digital, on-screen speed dial/BLF keys. Provide users with the fastest possible connection speeds thanks to the device’s dual Gigabit, PoE network ports. Maximized call control, expandable speed dial/BLF capabilities and a sleek design makes this phone the ultimate high-volume experience.

As all Grandstream IP phones do, the GXP21XX features state-of-the-art security encryption technology (SRTP and TLS). The GXP21XX supports a variety of automated provisioning options, including zero-configuration with Grandstream’s UCM series IP PBXs, encrypted XML files and TR-069, to make mass deployment extremely easy.

Additional documentation:

* [GXP21XX documentation](https://www.grandstream.com/hubfs/Product_Documentation/gxp21xx_administration_guide.pdf)

---

# Instructions for configuring the Grandstream GXP21XX IP Phone to work with Telnyx

|  |
| --- |
| **Note:** *The setup and configuration of the GXP21XX is almost identical to that of* [the GXP1630 and GXP2135](https://support.telnyx.com/en/articles/5815720-grandstream-gxp-telnyx-setup). |

In this activity you will:

1. [Get your device's IP address and log into the Grandstream phone's web portal](#h_0cd474bda6)
2. [Configure your GXP21XX](#h_5b32509cb8)

**Pre-requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Grandstream GXP 21XX/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Get your device's IP address and log into your phone's web portal

In this step, you'll obtain the IP address from your GXP, which you'll need to log into the web portal in the next step.

1. From your phone, navigate to **Menu >> Status >­> Network Status >> IPv4 Address** and take note of the IP address on this screen. You'll need it next.
2. On a computer connected to the same network as your phone, open a web browser and type *http://* followed by the phone's IP address into the address bar of your browser.
3. Log into the portal. Out of the box, the default credentials are:

   1. **Username:** *admin*
   2. **Password:** *admin*

   [![Grandstream portal entry. ](https://downloads.intercomcdn.com/i/o/435418196/02c366f53df95203841c95e3/Screen+Shot+2021-12-16+at+10.08.50.png?expires=1781168400&signature=8a941d7189884cd4ca9c287c7aed3c0e4f4b6a2ffbf1c960d48b7662066751ce&req=cCMiEsh2nIhZFb4f3HP0gLaecVmmRK8UukorrvdJ%2F%2Be%2FuNK10p%2BuhmTyotDM%0Ap1M%3D%0A)](https://downloads.intercomcdn.com/i/o/435418196/02c366f53df95203841c95e3/Screen+Shot+2021-12-16+at+10.08.50.png?expires=1781168400&signature=8a941d7189884cd4ca9c287c7aed3c0e4f4b6a2ffbf1c960d48b7662066751ce&req=cCMiEsh2nIhZFb4f3HP0gLaecVmmRK8UukorrvdJ%2F%2Be%2FuNK10p%2BuhmTyotDM%0Ap1M%3D%0A)

[Back to Top](#h_840e813c4e)

## 2. Configure your Grandstream GXP

In this step, you'll create a [SIP trunk](https://telnyx.com/products/sip-trunks) and connect your phone to Telnyx.

1. Click on **Accounts** in the top menu.
2. Expand the account you're looking to configure and click **General Settings**.

   [![Accounts button. ](https://downloads.intercomcdn.com/i/o/435413302/72675efc348bbedd82f0f830/Screen+Shot+2021-12-16+at+10.11.27.png?expires=1781168400&signature=ba3c2f152aff5ea1128991d79d579de351a294111a4c0e7aacb3127ce6e34bb5&req=cCMiEsh9noFdFb4f3HP0gGQCkPHH4%2FdGsJK8kAFlJrP13zNFTxl2nsLjFdMd%0ASNQ%3D%0A)](https://downloads.intercomcdn.com/i/o/435413302/72675efc348bbedd82f0f830/Screen+Shot+2021-12-16+at+10.11.27.png?expires=1781168400&signature=ba3c2f152aff5ea1128991d79d579de351a294111a4c0e7aacb3127ce6e34bb5&req=cCMiEsh9noFdFb4f3HP0gGQCkPHH4%2FdGsJK8kAFlJrP13zNFTxl2nsLjFdMd%0ASNQ%3D%0A)

   You can also use the top navigation to get here if you want.

   [![General settings button.](https://downloads.intercomcdn.com/i/o/435414420/36868141641ca73005f21a40/Screen+Shot+2021-12-16+at+10.12.43.png?expires=1781168400&signature=0a5e62e528d2f2d8e7057316b3e8c42c00cf1d0eedae7e7de6ad1cc63a7a0ad9&req=cCMiEsh6mYNfFb4f3HP0gLXexb2BULgLw7a%2FfeVuE3pD7K2MIdfqSRg4g6PF%0A0mo%3D%0A)](https://downloads.intercomcdn.com/i/o/435414420/36868141641ca73005f21a40/Screen+Shot+2021-12-16+at+10.12.43.png?expires=1781168400&signature=0a5e62e528d2f2d8e7057316b3e8c42c00cf1d0eedae7e7de6ad1cc63a7a0ad9&req=cCMiEsh6mYNfFb4f3HP0gLXexb2BULgLw7a%2FfeVuE3pD7K2MIdfqSRg4g6PF%0A0mo%3D%0A)
3. On this page, enter the following information:

   1. **Account Name:** Give it a name that makes sense for you
   2. **SIP Server:** *sip.telnyx.com*
   3. **SIP User ID:** Your Telnyx SIP account username
   4. **Authentication ID:** Your Telnyx SIP account username
   5. **Authenticate Password:** Your Telnyx SIP account password
   6. **Name:** This is your caller ID. You can choose whatever you like, but keep in mind the following naming conventions:

      1. Caller ID Name should be in capital letters. This will appears more clearly/visible on some devices.
      2. You must NOT use any special characters, as they will not be displayed. Spaces are allowed.
      3. Some of regular Canadian providers will not show more than 15 characters. We suggest shrinking or adapt your caller ID.
   7. **Voice Mail Access Number:** *\*97*

   [![General settings section. ](https://downloads.intercomcdn.com/i/o/435388621/6c92ce9aad27d05f92aa0aab/1.png?expires=1781168400&signature=b359e477afe17a21b06acaf56306c931256c8a64cde3c2899f8e8259d1cb1576&req=cCMiFcF2m4NeFb4f3HP0gC84j3auftlg7OjergSROmxa%2B1Fa77ztr49j1Rk9%0Ae0Q%3D%0A)](https://downloads.intercomcdn.com/i/o/435388621/6c92ce9aad27d05f92aa0aab/1.png?expires=1781168400&signature=b359e477afe17a21b06acaf56306c931256c8a64cde3c2899f8e8259d1cb1576&req=cCMiFcF2m4NeFb4f3HP0gC84j3auftlg7OjergSROmxa%2B1Fa77ztr49j1Rk9%0Ae0Q%3D%0A)
4. Now, while still in **Accounts > Account 1** *(or the account you want to configure)* click on **SIP Settings > Basic Settings** and provide the following information:

   1. **SIP Registration:** *Yes*
   2. **Register Expiration:** *5* (this is in minutes)
   3. **Enable OPTIONS Keep Alive:** *Yes*
   4. **Local SIP Port:** *5060* if you have not enabled TLS encryption. If you have, choose *5061*.
   5. **SIP Transport:** *UDP* or *TCP* if you have not enabled TLS encryption. If you have, choose *TLS/TCP*.

   [![Account 1 section. ](https://downloads.intercomcdn.com/i/o/435393594/7e8bba33df0f0fd6860a99c4/Screen+Shot+2021-12-16+at+09.44.39.png?expires=1781168400&signature=c49fe2b909b327f80ed6dc10f5e03970683de792d19ffb743a533145041b59f8&req=cCMiFcB9mIhbFb4f3HP0gFetkPtT2JLOTPcaGBGZUwqJaXoCmaYTE4JbfLpu%0A0w4%3D%0A)](https://downloads.intercomcdn.com/i/o/435393594/7e8bba33df0f0fd6860a99c4/Screen+Shot+2021-12-16+at+09.44.39.png?expires=1781168400&signature=c49fe2b909b327f80ed6dc10f5e03970683de792d19ffb743a533145041b59f8&req=cCMiFcB9mIhbFb4f3HP0gFetkPtT2JLOTPcaGBGZUwqJaXoCmaYTE4JbfLpu%0A0w4%3D%0A)

   \*This screenshot demonstrates a connection that uses UDP transport.
5. **Accounts > Account X > SIP > Custom SIP Header** and *disable*:

   * **Use Privacy Header:** *Yes*
   * **Use P-Preferred-Identity Header:** *Yes*
   * **Use X-Grandstream-PBX Header:** *No*
   * **Use P-Access-Network-Info Header**: *No*

   **Use P-Emergency-Info Header:** *No*
6. Go to **Accounts > Account X > SIP > Audio Settings,** and choose codec *G729A/B* or *G722* as preferred Vocoder.
7. Click **Save and Apply.**

That's it! You've finished configuring your Grandstream GXP 21XX profile, and can now start testing calls!

[Back to Top](#h_840e813c4e)

## Troubleshooting

## 1. Outgoing call issues

Are you able to receive incoming calls but outgoing calls are failing with a *No response* error? Try this:

1. Login into your device's settings and head to **Accounts > Account X > SIP > Custom SIP Header** and disable the following:

   * **Use X-Grandstream-PBX Header**
   * **Use P-Access-Network-Info Header**
   * **Use P-Emergency-Info Header**
2. Go to **Accounts > Account X > SIP > Audio Settings**, and choose codec *G729A/B* as preferred Vocoder and the rest with *PCMU*.

[Back to Top](#h_840e813c4e)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [GXP21XX documentation](https://www.grandstream.com/hubfs/Product_Documentation/gxp21xx_administration_guide.pdf)

---

Related Articles

[Configuring Grandstream GXP16XX with Telnyx](https://support.telnyx.com/en/articles/1130660-configuring-grandstream-gxp16xx-with-telnyx)[Grandstream GXP: Telnyx Setup](https://support.telnyx.com/en/articles/5815720-grandstream-gxp-telnyx-setup)[Grandstream GRP260x: SIP Trunk](https://support.telnyx.com/en/articles/6169513-grandstream-grp260x-sip-trunk)[Grandstream GXP1700: SIP Trunk](https://support.telnyx.com/en/articles/6184520-grandstream-gxp1700-sip-trunk)[Grandstream GXV3370](https://support.telnyx.com/en/articles/6187576-grandstream-gxv3370)

Did this answer your question?

😞😐😃

Table of contents
