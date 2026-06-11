---
source_url: https://support.telnyx.com/en/articles/5811545-fortifone-setup-fon-375-175-h25
scraped: 2026-06-11
---

FortiFone Setup: FON-375/175/H25 | Telnyx Help Center

[Skip to main content](#main-content)

# FortiFone Setup: FON-375/175/H25

Learn how to set up and configure a FortiFone FON-375, FON-175 or FON-H25 IP phone with Telnyx

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_aff9fe9001)

[FortiFone](https://www.fortinet.com/products/business-phone-systems/fortivoice-fortifone/phones-softclients) is equipped with high-definition audio and reliable performance, enabling efficient and clear conversations. It offers a range of selection from entry-level phones to executive-level phones that offer a variety of features, with programmable line and extension appearances. The FortiFone FON-570 is one of the top-line models and boasts a large 7" color screen for easy configuration and use. Additionally, enjoy 7 dedicated feature keys, 109 programmable phone keys, full-duplex speakerphone, 2 10/100/1000 ethernet ports, and integrated PoE (Power over Ethernet) support.

|  |
| --- |
| ***Note:*** *This document also supports configuration of the FortiFone FON-175 and FortiFone FON-H25. If either of these is the device you're using, you can follow this document.* |

Additional documentation:

* [FortiFONE documentation](https://www.fortinet.com/search?q=fortifone)
* [Fortinet support](https://www.fortinet.com/support/contact)

---

# Instructions for setting up and configuring the FortiFone FON 570

In this activity you will:

1. [Get your device's IP address](#h_40df07ca02)
2. [Set up your FortiFone for traffic flow](#h_a62ac1b7a8)

**Pre-requisites:**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for FortiFone FON-570/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Get your device's IP address

In this step, you'll obtain the IP address from your FortiFone, which you'll need to log into the web portal in the next step.

1. From your phone, tap the **Menu** button on your LCD screen and select **Status** to see your IP address. Take note of this.  
   ​  
   The menu button:

   [![FortiFone meny button.](https://downloads.intercomcdn.com/i/o/434261482/503a47e23db560a7d0b0500e/00.png?expires=1781168400&signature=ab830b5ee49e509b8a3ee8688096c6ddd2fb0e6c7d2bc122b30477a674d6e0ac&req=cCMjFM9%2FmYldFb4f3HP0gGUYgtFBrdmSQ9mJwrUQtfdkfxhbLJO0N02QXc0f%0A%2Blw%3D%0A)](https://downloads.intercomcdn.com/i/o/434261482/503a47e23db560a7d0b0500e/00.png?expires=1781168400&signature=ab830b5ee49e509b8a3ee8688096c6ddd2fb0e6c7d2bc122b30477a674d6e0ac&req=cCMjFM9%2FmYldFb4f3HP0gGUYgtFBrdmSQ9mJwrUQtfdkfxhbLJO0N02QXc0f%0A%2Blw%3D%0A)

   Status:

   [![FortiFone status button. ](https://downloads.intercomcdn.com/i/o/434261814/56bbc574a7056d428b4893fa/1.jpeg?expires=1781168400&signature=0a59ba1ed0d6c294af831e6bf6888e740ad10fec82efd15929dee990deb0fcbc&req=cCMjFM9%2FlYBbFb4f3HP0gNTn9C7OAf6vGixpPr6lvhNLePq76xZCA8tfm%2FUv%0Ah7U%3D%0A)](https://downloads.intercomcdn.com/i/o/434261814/56bbc574a7056d428b4893fa/1.jpeg?expires=1781168400&signature=0a59ba1ed0d6c294af831e6bf6888e740ad10fec82efd15929dee990deb0fcbc&req=cCMjFM9%2FlYBbFb4f3HP0gNTn9C7OAf6vGixpPr6lvhNLePq76xZCA8tfm%2FUv%0Ah7U%3D%0A)

   IP address:

   [![FortiFone mode button. ](https://downloads.intercomcdn.com/i/o/434261974/4c702de0af827314f5664759/0.jpeg?expires=1781168400&signature=370d51a662bbc07e3316298fe60c3de7128878e7832c4f3973a2932b5b51122c&req=cCMjFM9%2FlIZbFb4f3HP0gNf3XLGNeewyUiaQHaYFvLS92ukY5wajq5CBofJX%0AJ3o%3D%0A)](https://downloads.intercomcdn.com/i/o/434261974/4c702de0af827314f5664759/0.jpeg?expires=1781168400&signature=370d51a662bbc07e3316298fe60c3de7128878e7832c4f3973a2932b5b51122c&req=cCMjFM9%2FlIZbFb4f3HP0gNf3XLGNeewyUiaQHaYFvLS92ukY5wajq5CBofJX%0AJ3o%3D%0A)

[Back to Top](#h_aff9fe9001)

## 2. Set up your FortiFone for traffic flow

In this step, you will set up your device and register it with Telnyx.

1. From your computer, open a web browser and enter the IP address of your device that you obtained in [Step 1](https://support.telnyx.com/en/articles/5810226-fortifone-fon-570#h_2a7d29498d) into your address bar. Prepend with *http://*
2. Log into your device. The first time logging in, you'll use the default credentials (Don't forget to change them after!)

   1. **Username:** *admin*
   2. **Password:** *23656*

      [![Fortinet credentials settings section. ](https://downloads.intercomcdn.com/i/o/434262591/6b0485298f89d22ca2670876/2.jpeg?expires=1781168400&signature=90503589b4ede5ad79aafdddf8a8285a54353ed5be2f923cc214497ae51562dd&req=cCMjFM98mIheFb4f3HP0gEuT8XzaBNis3ezLG5zYJIDPeA2CLxutxlgXfuDO%0APqQ%3D%0A)](https://downloads.intercomcdn.com/i/o/434262591/6b0485298f89d22ca2670876/2.jpeg?expires=1781168400&signature=90503589b4ede5ad79aafdddf8a8285a54353ed5be2f923cc214497ae51562dd&req=cCMjFM98mIheFb4f3HP0gEuT8XzaBNis3ezLG5zYJIDPeA2CLxutxlgXfuDO%0APqQ%3D%0A)
3. To register your device with Telnyx, click on **Line** in the left-hand menu and select the **SIP** tab at the top of the page. Find the **Line** section and enter the following:

   1. **Username:** This is your SIP main or sub account username.
   2. **Display Name:** This is your caller ID. You can choose whatever you like, but keep in mind the following naming conventions:

      1. Caller ID Name should be in capital letters. This will appears more clearly/visible on some devices.
      2. You must NOT use any special characters, as they will not be displayed. Spaces are allowed.
      3. Some of regular Canadian providers will not show more than 15 characters. We suggest shrinking or adapt your caller ID.
   3. **Authentication Name:** This is your SIP main or sub account username.
   4. **Authentication Password:** This is your SIP main or sub account password.
   5. **Server Name:** *sip.telnyx.com*
   6. **Register Address:** *sip.telnyx.com*
   7. **Register Port:** If you are using UDP transport, use port *5060*. If you are using TLS transport, use port *5061.*
   8. **Activate:** Check this to activate

   [![Line button. ](https://downloads.intercomcdn.com/i/o/434266026/f9c8e8222f0ef3cee3854a0a/3.png?expires=1781168400&signature=c3692e9de133e7541ec5d56507fb47c2f69383927f9651923c63741b7e03bc37&req=cCMjFM94nYNZFb4f3HP0gKbktFtuxmoXsGeWM6jzCZGQuMJT2KHXgPyVnQIl%0AUXU%3D%0A)](https://downloads.intercomcdn.com/i/o/434266026/f9c8e8222f0ef3cee3854a0a/3.png?expires=1781168400&signature=c3692e9de133e7541ec5d56507fb47c2f69383927f9651923c63741b7e03bc37&req=cCMjFM94nYNZFb4f3HP0gKbktFtuxmoXsGeWM6jzCZGQuMJT2KHXgPyVnQIl%0AUXU%3D%0A)
4. Scroll to the **Advanced** section on this tab and enter the following information:

   1. **Transportation Protocol:** By default, *UDP* is selected. If you enabled TLS and your account is configured to use SRTP encryption as part of your [pre-requisite activities](https://support.telnyx.com/en/articles/5810226-fortifone-fon-570#h_6edc08d8c8) then you should choose *TLS.*
5. This step is OPTIONAL, but is required if you've [planned to encrypt traffic](https://support.telnyx.com/en/articles/5810226-fortifone-fon-570#h_6edc08d8c8). If you are using UDP transport and not encrypting traffic, continue to the next step.   
   ​  
   Still in the **Advanced** section:

   1. **Transportation Protocol:** *TCP*
   2. **RTP Encryption:** Check this box

   [![SIP section of the Line section. ](https://downloads.intercomcdn.com/i/o/434269959/e8dc8c2bee33eeb8428bd2d1/8.jpeg?expires=1781168400&signature=ee037d7cc6af932152093291f6b91be5f0efd1cc42ac86cdeffeeee058dee445&req=cCMjFM93lIRWFb4f3HP0gBtNCa2GS2x0cm9ddmk%2Farg%2BfSx2n1N%2BmuOqNxzx%0Av6g%3D%0A)](https://downloads.intercomcdn.com/i/o/434269959/e8dc8c2bee33eeb8428bd2d1/8.jpeg?expires=1781168400&signature=ee037d7cc6af932152093291f6b91be5f0efd1cc42ac86cdeffeeee058dee445&req=cCMjFM93lIRWFb4f3HP0gBtNCa2GS2x0cm9ddmk%2Farg%2BfSx2n1N%2BmuOqNxzx%0Av6g%3D%0A)

That's it! You've finished configuring your FortiFone FON-375 profile, and can now start testing calls!

[Back to Top](#h_aff9fe9001)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [FortiFONE documentation](https://www.fortinet.com/search?q=fortifone)
* [Fortinet support](https://www.fortinet.com/support/contact)

---

Related Articles

[FortiFone FON-570](https://support.telnyx.com/en/articles/5810226-fortifone-fon-570)[Flyingvoice: Telnyx Setup](https://support.telnyx.com/en/articles/5810663-flyingvoice-telnyx-setup)[Panasonic KX-HDV: Telnyx setup](https://support.telnyx.com/en/articles/5814406-panasonic-kx-hdv-telnyx-setup)[Gigaset A510: Telnyx Setup](https://support.telnyx.com/en/articles/5815209-gigaset-a510-telnyx-setup)[Snom C520: Telnyx Setup](https://support.telnyx.com/en/articles/5815678-snom-c520-telnyx-setup)

Did this answer your question?

😞😐😃

Table of contents
