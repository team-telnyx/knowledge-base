---
source_url: https://support.telnyx.com/en/articles/5819923-audiocodes-400hd
scraped: 2026-06-11
---

Audiocodes 400HD | Telnyx Help Center

[Skip to main content](#main-content)

# Audiocodes 400HD

Learn how to set up and configure an Audiocodes 400HD IP phone and connect it to your Telnyx account.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_4720699022)

The [AudioCodes 400HD](https://www.audiocodes.com/media/3063/audiocodes-400hd-ip-phones.pdf) series of IP phones includes a range of easy-to-use, feature-rich products for the service provider, hosted services, unified communications, enterprise IP telephony and contact center markets. Based on the same advanced, field-proven underlying technology as our other VoIP products, AudioCodes high quality IP phones enable service providers, systems integrators and end-customers to build end-to-end VoIP solutions.

Additional documentation:

* [User manual](https://www.audiocodes.com/media/9627/ltrt-11939-430hd-and-440hd-ip-phone-for-microsoft-skype-for-business-users-manual-ver-301.pdf)
* [Admin manual](https://www.audiocodes.com/media/13525/400hd-series-ip-phone-for-microsoft-skype-for-business-administrators-manual-ver-312.pdf)

---

# Instructions for configuring the Audiocodes 400HD IP phone to work with Telnyx

|  |
| --- |
| **Note:** *The setup and configuration of the Audiocodes 400HD is almost identical to that of* [the GXP1630 and GXP2135](https://support.telnyx.com/en/articles/5815720-grandstream-gxp-telnyx-setup). |

In this activity you will:

1. [Get your device's IP address and log into the 400HD phone's web portal](#h_abbcf227d9)
2. [Configure your 400HD](#h_cd1c87d27e)
3. (IF YOU ARE USING TLS ENCRYPTION) [Network settings](#h_d8c7961a88)
4. [Configure registration time and NAT keep alive settings](#h_4d1b28b78e)
5. [Configure audio codecs](#h_7fa4d40461)

**Pre-requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Audiocodes 400HD/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Get your device's IP address and log into your phone's web portal

In this step, you'll obtain the IP address from your 400HD, which you'll need to log into the web portal in the next step.

1. From your phone, navigate to **Menu > Device Status >­ Network Settings > IP Address** and take note of the IP address on this screen. You'll need it next.
2. On a computer connected to the same network as your phone, open a web browser and type *http://* followed by the phone's IP address into the address bar of your browser.
3. Log into the portal. Out of the box, the default credentials are:

   1. **Username:** *admin*
   2. **Password:** *1234*

   [![Credential entry boxes. ](https://downloads.intercomcdn.com/i/o/435514889/0a1f98c0a9568d8659cd7a46/login.png?expires=1781168400&signature=29980a3c28345b37d3670050a445da2f76008e0a7f8f0f144250e6e9ce290df9&req=cCMiE8h6lYlWFb4f3HP0gIpfd3VFSp8ZPzCVz%2Br3hFeuCSiLm1ASpkNmtCV8%0AqcA%3D%0A)](https://downloads.intercomcdn.com/i/o/435514889/0a1f98c0a9568d8659cd7a46/login.png?expires=1781168400&signature=29980a3c28345b37d3670050a445da2f76008e0a7f8f0f144250e6e9ce290df9&req=cCMiE8h6lYlWFb4f3HP0gIpfd3VFSp8ZPzCVz%2Br3hFeuCSiLm1ASpkNmtCV8%0AqcA%3D%0A)
4. Here's the landing page:

   [![Audio Codec landing page. ](https://downloads.intercomcdn.com/i/o/435515234/bb7fe8d67d5d2eb1a615facc/landing.png?expires=1781168400&signature=7e7b5a629c6e49c7945b8bbd85f759035ce92202192e2c81f298a561ca6816b1&req=cCMiE8h7n4JbFb4f3HP0gGSNI2nZcQ%2BL9wb4AopRV2%2B1W7zxDszvbtDpL3oZ%0AJdQ%3D%0A)](https://downloads.intercomcdn.com/i/o/435515234/bb7fe8d67d5d2eb1a615facc/landing.png?expires=1781168400&signature=7e7b5a629c6e49c7945b8bbd85f759035ce92202192e2c81f298a561ca6816b1&req=cCMiE8h7n4JbFb4f3HP0gGSNI2nZcQ%2BL9wb4AopRV2%2B1W7zxDszvbtDpL3oZ%0AJdQ%3D%0A)

[Back to Top](#h_4720699022)

## 2. Configure your 400HD

In this step, you'll create a [SIP trunk](https://telnyx.com/products/sip-trunks) and connect your phone to Telnyx.

1. From the left-hand navigation, make sure you're on the **Configuration** tab and click the + **Quick Setup** folder to expand it.
2. Find the **SIP Proxy and Registrar** section and provide the following information:

   1. **Use SIP Proxy:** *Enable*
   2. **Proxy IP Address or Host Name:** *sip.telnyx.com*
   3. **Proxy Port:** *5060* if you have not enabled TLS encryption. If you have, choose *5061*.
   4. **Use SIP Proxy IP and Port for Registration:** *Enable*
   5. **Use SIP Registrar:** *Disable*

   [![Signaling protocol. ](https://downloads.intercomcdn.com/i/o/435522339/764575e5292333f5f155b252/registrar.png?expires=1781168400&signature=6ee8518d29b28eafffcf04dd87cab429af0be60b53a57c9e4957a373b722dd51&req=cCMiE8t8noJWFb4f3HP0gAayZVZllEOoMfA%2BUnZ2NHNaqIMsCz99dC7SkBxV%0AA3Q%3D%0A)](https://downloads.intercomcdn.com/i/o/435522339/764575e5292333f5f155b252/registrar.png?expires=1781168400&signature=6ee8518d29b28eafffcf04dd87cab429af0be60b53a57c9e4957a373b722dd51&req=cCMiE8t8noJWFb4f3HP0gAayZVZllEOoMfA%2BUnZ2NHNaqIMsCz99dC7SkBxV%0AA3Q%3D%0A)

   *\*This screenshot shows a UDP setup.*
3. Find the **Line Settings** section and provide the following information:

   1. **Line Number:** *1*
   2. **Line 1 Activate:** *Enable*
   3. **Line 1 Display Name:** This is your caller ID. You can choose whatever you like, but keep in mind the following naming conventions:

      1. Caller ID Name should be in capital letters. This will appears more clearly/visible on some devices.
      2. You must NOT use any special characters, as they will not be displayed. Spaces are allowed.
      3. Some of regular Canadian providers will not show more than 15 characters. We suggest shrinking or adapt your caller ID.
   4. **Line 1 User ID:** Your Telnyx account ID
   5. **Line 1 Authentication User Name:** Your Telnyx account ID
   6. **Line 1 Authentication Password:** Your Telnyx account password

   [![Quick Setup section. ](https://downloads.intercomcdn.com/i/o/435529401/2c7698f90b5d7aedb7840115/SIPcreds.png?expires=1781168400&signature=71bd9d38b962421d3b6c97a49c38e151839a1bccc820d81a18bb438a76da7058&req=cCMiE8t3mYFeFb4f3HP0gDlNqprMoCXjdtdnu4E6gUHRvlFWjCvIp9%2FZp7%2FN%0AGFk%3D%0A)](https://downloads.intercomcdn.com/i/o/435529401/2c7698f90b5d7aedb7840115/SIPcreds.png?expires=1781168400&signature=71bd9d38b962421d3b6c97a49c38e151839a1bccc820d81a18bb438a76da7058&req=cCMiE8t3mYFeFb4f3HP0gDlNqprMoCXjdtdnu4E6gUHRvlFWjCvIp9%2FZp7%2FN%0AGFk%3D%0A)

[Back to Top](#h_4720699022)

## 3. (IF YOU ARE USING TLS ENCRYPTION) Network settings

You only need to follow this section if you are using TLS encryption on your account. Ensure that you have [enabled TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication) on your Telnyx portal. If you are not using TLS, you can go on to [section 4](#h_4d1b28b78e).

1. Navigate to **Voice Over IP > Signaling Protocols** and enter the following information:

   1. **SIP Transport Protocol:** *TLS*
   2. **TLS Port:** *5061*
   3. **SIP Local Port:** *5081*
   4. **Proxy IP Address or Host Name:** *sip.telnyx.com:5061*
   5. **Proxy Port:** *5061*
   6. **Use SIP Proxy IP and Port for Registration:** *Disable*
   7. **Use SIP Outbound Proxy:** *Disable*

   [![SIP general. ](https://downloads.intercomcdn.com/i/o/435532949/b933762d47fe5b9259e53f25/enableTLS.png?expires=1781168400&signature=cf727ce9003042bc0fbad749a70d1f6c2e437afde3eb7810b5a7464d63f7b1b4&req=cCMiE8p8lIVWFb4f3HP0gFC638rMnrfolED%2FkvZz1ZuamztX1sqz20au32yO%0Alvg%3D%0A)](https://downloads.intercomcdn.com/i/o/435532949/b933762d47fe5b9259e53f25/enableTLS.png?expires=1781168400&signature=cf727ce9003042bc0fbad749a70d1f6c2e437afde3eb7810b5a7464d63f7b1b4&req=cCMiE8p8lIVWFb4f3HP0gFC638rMnrfolED%2FkvZz1ZuamztX1sqz20au32yO%0Alvg%3D%0A)
2. Now enable SRTP. Navigate to **Voice Over IP > Media Streaming** and enter the following information:

   1. **SRTP Encryption and Authentication:** *REQUIRE ENCRYPTION*
   2. **Method:** *AES\_CM\_128\_ALL\_METHODS*
   3. **Negotiation mode:** *Basic*
   4. **ARIA:** *Disable*

   [![Media streaming section. ](https://downloads.intercomcdn.com/i/o/435534570/8e59b8a4462a0e6f4b003166/srtp.png?expires=1781168400&signature=a3f678763a11e38ea057ad6c6c7946e8006f088993f16e8b1bf2922392c18d78&req=cCMiE8p6mIZfFb4f3HP0gKARby8BKUkJtSSw6MwRPW8A7zYIutubd%2F7F8298%0AGB4%3D%0A)](https://downloads.intercomcdn.com/i/o/435534570/8e59b8a4462a0e6f4b003166/srtp.png?expires=1781168400&signature=a3f678763a11e38ea057ad6c6c7946e8006f088993f16e8b1bf2922392c18d78&req=cCMiE8p6mIZfFb4f3HP0gKARby8BKUkJtSSw6MwRPW8A7zYIutubd%2F7F8298%0AGB4%3D%0A)

## 4. Configure registration time and NAT keep alive settings

In this section, we're going to set up your device to stay awake and ready to receive incoming calls 24/7.

1. From the left-hand panel, go to Voice Over IP > Signaling Protocols and enter the following information:

   1. **Enable Registrar Keep Alive:** *Enable*
   2. **Registrar Keep Alive Period:** *50 Seconds*
   3. **Registration Expires:** *300 Seconds*

   [![Signaling protocol section. ](https://downloads.intercomcdn.com/i/o/435539159/90d01a75849a5bda846d7df2/NATkeepalive.png?expires=1781168400&signature=1672672cc683fb58bd5b73cbbc49b86aa83c4f6cfff57cfc4846d32dc24414ce&req=cCMiE8p3nIRWFb4f3HP0gIj8eGcplBjrQM%2BF1WZHXc7z6cgaafRwmN1yQUVj%0Au5g%3D%0A)](https://downloads.intercomcdn.com/i/o/435539159/90d01a75849a5bda846d7df2/NATkeepalive.png?expires=1781168400&signature=1672672cc683fb58bd5b73cbbc49b86aa83c4f6cfff57cfc4846d32dc24414ce&req=cCMiE8p3nIRWFb4f3HP0gIj8eGcplBjrQM%2BF1WZHXc7z6cgaafRwmN1yQUVj%0Au5g%3D%0A)

## 5. Configure Audio Codecs

Go to **Voice Over IP > Media Streaming** and set your codecs in priority sequence that meets your needs.   
​  
Telnyx supports the following codecs:

1. ulaw(g711u)
2. alaw(g711a)
3. g722
4. g729

That's it! You've finished configuring your Audiocodes 400HD profile, and can now start testing calls!

[Back to Top](#h_4720699022)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [User manual](https://www.audiocodes.com/media/9627/ltrt-11939-430hd-and-440hd-ip-phone-for-microsoft-skype-for-business-users-manual-ver-301.pdf)
* [Admin manual](https://www.audiocodes.com/media/13525/400hd-series-ip-phone-for-microsoft-skype-for-business-administrators-manual-ver-312.pdf)

---

Related Articles

[Panasonic KX-HDV: Telnyx setup](https://support.telnyx.com/en/articles/5814406-panasonic-kx-hdv-telnyx-setup)[Gigaset A510: Telnyx Setup](https://support.telnyx.com/en/articles/5815209-gigaset-a510-telnyx-setup)[Snom C520: Telnyx Setup](https://support.telnyx.com/en/articles/5815678-snom-c520-telnyx-setup)[Fanvil H5: Hotel IP](https://support.telnyx.com/en/articles/6203401-fanvil-h5-hotel-ip)[Fanvil X2CP/X2C/X2P: Call Center IP](https://support.telnyx.com/en/articles/6206756-fanvil-x2cp-x2c-x2p-call-center-ip)

Did this answer your question?

😞😐😃

Table of contents
