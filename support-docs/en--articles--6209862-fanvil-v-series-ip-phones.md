---
source_url: https://support.telnyx.com/en/articles/6209862-fanvil-v-series-ip-phones
scraped: 2026-07-08
content_hash: d34d15827bcbe63d0f372719ef1d30c3f6abfa6eb3e7b81752194e098d670bbb
---

Fanvil V-Series: IP Phones | Telnyx Help Center

[Skip to main content](#main-content)

# Fanvil V-Series: IP Phones

Learn how to configure a Telnyx SIP trunk on the Fanvil V67/V65/V64/V62 phones

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_6e32dcf3ae)

|  |  |
| --- | --- |
| **FANVIL V67 FLAGSHIP SMART VIDEO PHONE**    The [V67 Smart Video phone](https://www.fanvil.com/Product/info/id/157.html) is more than an efficient telephone but also a delicate work of art, which provides a more intelligent and elegant office operation experience for executives, managers and teleworkers. With brand new design, V67 features an adjustable touch screen and a keypad with colorful light effect that improve the beauty and comfort of office desktop.    **Product Features:**  * Antibacterial surface protection * Adjustable 7" color touchscreen * Colorful light-up keypad * HD audio * Opus support * HD video * 10-party audio conferencing * Built-in 2.4G/5G WiFi * Built-in Bluetooth * Miracast | **FANVIL V65 PRIME BUSINESS PHONE**    [The V65 Prime Business phone](https://www.fanvil.com/Product/info/id/158.html) is more than an efficient telephone but a delicate work of art, providing a smart and smooth business communication experience for executives and managers. As the prime business phone featuring an adjustable screen and built-in Bluetooth 4.2 and 2.4G/5G Wi-Fi, V65 is a perfect combination of elegant outside and powerful inside.    **Product Features:**  * Antibacterial surface protection * Adjustable 4.3" color touchscreen * HD audio * Opus support * HD video * 6-party audio conferencing * Built-in 2.4G/5G WiFi * Built-in Bluetooth * USB * Link with security products |
| **FANVIL V64 PRIME BUSINESS PHONE**    The [V64 Prime Business phone](https://www.fanvil.com/Product/info/id/159.html) is more than an efficient telephone but a delicate work of art, providing a smart and smooth business communication experience for enterprises. As the prime business phone featuring a color LCD screen and built-in Bluetooth 4.2 and 2.4G/5G Wi-Fi, V64 is a perfect combination of elegant outside and powerful inside.    **Product Features:**  * 3.5" color LCD screen * HD audio * Opus support * 6-party audio conferencing * Built-in 2.4G/5G WiFi * Built-in Bluetooth * USB * Link with security products * Dual gigabit ports, integrate PoE | **FANVIL V62 ESSENTIAL BUSINESS PHONE**    [The V62 Essential Business phone](https://www.fanvil.com/Product/info/id/160.html) is more than an efficient telephone but a delicate work of art, providing a smart and smooth business communication experience for enterprises. As the essential business phone featuring a graphical Dot-matrix screen with backlight and necessary VoIP features and other extended features, V62 is a great combination of elegant outside and powerful inside.    **Product Features:**  * HD audio * Opus support * 6-party audio conferencing * WiFi dongle * Support EHS/Bluetooth wireless headset * USB * Link with security products * Dual gigabit ports, integrate PoE |

**Additional resources:**

* Firmware:

  + V67 (see section 10.7.5, page 90 of the [user manual](https://www.fanvil.com/Uploads/Temp/download/20220310/6229a2f42d58f.pdf))
  + V65 (see section 10.7.5, page 104 of the [user manual](https://www.fanvil.com/Uploads/Temp/download/20220412/62555c3e41d94.pdf))
  + [V64](https://www.fanvil.com/Support/download/id/159.html)
  + [V62](https://www.fanvil.com/Support/download/id/160.html)
* User manuals

  + [V67](https://www.fanvil.com/Uploads/Temp/download/20220310/6229ab6b347e3.pdf)
  + [V64/V65](https://www.fanvil.com/Uploads/Temp/download/20220412/62555c3e41d94.pdf)
  + [V62](https://www.fanvil.com/Uploads/Temp/download/20220310/6229ab6b347e3.pdf)
* [Fanvil FAQ](https://www.fanvil.com/Support/index.html)
* [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html)
* [Fanvil support](https://www.fanvil.com/Support/ticket.html)

---

# Instructions for setting up and configuring a SIP trunk on your Fanvil V-series IP device

**In this activity you will:**

1. [Configure a line with a Telnyx SIP trunk](#h_009160ed7e)
2. [Configure voice and video settings](#h_7aa5188f01)
3. [(Optional) Upload a TLS certificate (For encrypted connections)](#h_641a9d5328)

**Pre-requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
* Make sure your phone is running the latest firmware (See the **Additional resources** section above)
* Make sure you can log into the web GUI. Refer to the Web Management section of your phone's user manual for instructions. (User manuals: [V67](https://www.fanvil.com/Uploads/Temp/download/20220310/6229ab6b347e3.pdf), [V64/V65](https://www.fanvil.com/Uploads/Temp/download/20220412/62555c3e41d94.pdf), [V62](https://www.fanvil.com/Uploads/Temp/download/20220310/6229ab6b347e3.pdf))

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

SIP account registration tutorial for Fanvil IP phones:

## 1. **Configure a line with a Telnyx SIP trunk**

In this step you'll configure your first Telnyx [SIP trunk](https://telnyx.com/products/sip-trunks) via the phone's web interface or device screen. This guide focuses on the web interface. If you are using the phone screen, follow the instructions in the [pre-requisite section](#h_00b63e9e92) and use the parameters in this section.

1. Log into your web GUI and navigate to **Line > SIP**.
2. Use the **Line** dropdown to select a SIP line to configure, and provide the following:
3. In the **Register Settings** section:

   1. **Username:** The SIP connection username. Learn more [here](https://support.telnyx.com/en/articles/4245868-sip-connection-types) in the Credentials Connection Setup section.
   2. **Display Name:** This is your caller ID. You can choose whatever you like, but keep in mind the following naming conventions:

      1. Caller ID Name should be in capital letters. This will appears more clearly/visible on some devices.
      2. You must NOT use any special characters, as they will not be displayed. Spaces are allowed.
      3. Some of regular Canadian providers will not show more than 15 characters. We suggest shrinking or adapt your caller ID.
   3. **Realm:** Enter the name of the realm to which the SIP interface is connected.
   4. **Authentication Name:** The SIP connection username. Learn more [here](https://support.telnyx.com/en/articles/4245868-sip-connection-types) in the Credentials Connection Setup section.
   5. **Authentication Password:** The SIP connection password. Learn more [here](https://support.telnyx.com/en/articles/4245868-sip-connection-types) in the Credentials Connection Setup section.

   1. **Server Name**: *sip.telnyx.com* (For international, see [this document](https://sip.telnyx.com/#signaling-addresses).)
4. In the **SIP Server 1** sub-section:

   1. **Server Address:** *sip.telnyx.com* (For international, see [this document](https://sip.telnyx.com/#signaling-addresses).)
   2. **Server Port:** If you are using TCP or UDP transport, use port *5060*. If you are using TLS transport, use port *5061.*
   3. **Transport Protocol:** Choose *TCP* or *UDP* unless you are encrypting traffic and have set up encryption on your Telnyx portal. In this case, choose *TLS*.

   ![Register Settings section of the Web GUI. ](_images/4824a0b4d660ea0c.png)
5. You can now configure the **SIP Server 2** section if you want.

[Back to Top](#h_6e32dcf3ae)

## 2. Configure voice and video settings

In this section, you'll add codecs to your phone configuration that will support optimal audio and video.

1. From the line you configured in [step 1](#h_009160ed7e), expand the **Codecs Settings** section.
2. From here, you can set the priority and availability of audio and video codecs by adding or removing them from the list. The following is a list of codecs (both audio and video) that Telnyx supports:

   **Audio:**

   * *ulaw(g711u)*
   * *alaw(g711a)*
   * *g722*
   * *g729*

   **Video:**

   * *H264*

[Back to Top](#h_6e32dcf3ae)

## 3. (Optional) Upload a TLS certificate (For encrypted connections)

If you are encrypting traffic with TLS, you'll need to upload a TLS certificate, which you'll do in this section.

1. In the **Lines > SIP section,** find the **Advanced Settings** sub-section:

   1. **DTMF Type:** *RFC 2833*
   2. **Transportation Protocol:** Choose *TCP* or *UDP* unless you are encrypting traffic and have set up encryption on your Telnyx portal. In this case, choose *TLS*.  
      ​  
      ​*Note that if you are encrypting traffic, you'll need to go into **Lines > Dial Peer** and make sure the **Port** setting is changed to* 5061.
   3. **RTP Encryption**: (Optional) Enable this if you're using TLS
   4. **RTP Encryption Key:** (Optional) Obtain a key [here](https://crt.sh/?id=1199354)
2. Navigate to **Line > Basic Settings** and find the **STUN Settings** section and set:

   1. **TLS Certification File:** Obtain a certificate [here](https://crt.sh/?id=1199354).

That's it, you've now completed the configuration of your Fanvil V-series IP phone with your Telnyx account.

[Back to Top](#h_6e32dcf3ae)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally you can check out:

* Firmware:

  + V67 (see section 10.7.5, page 90 of the [user manual](https://www.fanvil.com/Uploads/Temp/download/20220310/6229a2f42d58f.pdf))
  + V65 (see section 10.7.5, page 104 of the [user manual](https://www.fanvil.com/Uploads/Temp/download/20220412/62555c3e41d94.pdf))
  + [V64](https://www.fanvil.com/Support/download/id/159.html)
  + [V62](https://www.fanvil.com/Support/download/id/160.html)
* User manuals

  + [V67](https://www.fanvil.com/Uploads/Temp/download/20220310/6229ab6b347e3.pdf)
  + [V64/V65](https://www.fanvil.com/Uploads/Temp/download/20220412/62555c3e41d94.pdf)
  + [V62](https://www.fanvil.com/Uploads/Temp/download/20220310/6229ab6b347e3.pdf)
* [Fanvil FAQ](https://www.fanvil.com/Support/index.html)
* [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html)
* [Fanvil support](https://www.fanvil.com/Support/ticket.html)

---

---

Related Articles

[Fanvil H2U: Compact IP](https://support.telnyx.com/en/articles/6202755-fanvil-h2u-compact-ip)[Fanvil H3: Hotel IP](https://support.telnyx.com/en/articles/6202965-fanvil-h3-hotel-ip)[Fanvil H3W/H5W: WiFi IP](https://support.telnyx.com/en/articles/6203347-fanvil-h3w-h5w-wifi-ip)[Fanvil X7 Series: IP Phones](https://support.telnyx.com/en/articles/6209215-fanvil-x7-series-ip-phones)[Fanvil X-Series: IP Phone](https://support.telnyx.com/en/articles/6209971-fanvil-x-series-ip-phone)

Did this answer your question?

😞😐😃

Table of contents
