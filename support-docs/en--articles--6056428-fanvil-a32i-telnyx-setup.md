---
source_url: https://support.telnyx.com/en/articles/6056428-fanvil-a32i-telnyx-setup
scraped: 2026-07-08
content_hash: 47a579bd64db9c985994600d304247da03150233f2a5e476fcc71b37d15c0d44
---

Fanvil A32i: Telnyx Setup | Telnyx Help Center

[Skip to main content](#main-content)

# Fanvil A32i: Telnyx Setup

Learn how to configure a Telnyx SIP trunk on the Fanvil A32i Android Console IP phone

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_9b42e0da7f)

Featuring a Goose-neck speaker and a large touch screen, [Fanvil A32i](https://www.fanvil.com/Product/info/id/139.html) is an Android console IP phone with stylish outlook and powerful functions. As a mini management device, Fanvil A32i caters to the management requirements in small and medium control centers and helps to level-up the daily management efficiency and the ability to handle any emergency. Featuring the business elegant outlook with smooth lines, a

big color touch screen, user-friendly interface, A32i can be the most helpful management phone in the control center.

**Product Features**

* 20 SIP Lines
* Gooseneck Microphone
* 10.1-inch Touch Screen with 112 DSS Keys
* 1080P Fanvil CM60 HD USB Camera（Optional）
* Support Three-way Video Conference
* Support H.264 Video Codec
* Built-in Harman Speaker
* Fanvil PTM Phone Handle（Optional）
* Built-in 2.4G/5G WiFi and Bluetooth
* Support EHS Wireless Earphone

**Additional resources:**

* [Fanvil A32i user manual](https://fanvil.com.hk/wp-content/uploads/2021/09/A32i-Android-Console-IP-Phone-A32i-User-Manual.pdf)
* [Fanvil FAQ](https://www.fanvil.com/Support/index.html)
* [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html)
* [Fanvil support](https://www.fanvil.com/Support/ticket.html)
* [Fanvil A32i firmware](https://www.fanvil.com/Support/download/id/139.html)

---

# Instructions for setting up and configuring your Fanvil X4G IP phone

In this activity you will:

1. [Configure a line with a Telnyx SIP trunk](#h_014039ea68)
2. [Configure voice and video settings](#h_a8b733832f)

**Pre-requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
* Make sure your phone is running the [latest firmware](https://www.fanvil.com/Support/download/id/139.html)
* Make sure you can log into the web GUI. This is where you'll configure your [SIP trunk](https://telnyx.com/products/sip-trunks). You can find the address and default credentials on page 32 of the phone's [user manual](https://fanvil.com.hk/wp-content/uploads/2021/09/A32i-Android-Console-IP-Phone-A32i-User-Manual.pdf). (section 7.7: Web Management)

  + You can also configure your SIP trunk directly through the interface on the phone's screen. Press the line key for a long time, or press the button in the function menu **Phone Settings > Account > Line** configuration and use the parameters found in this document to configure your trunk. Then click **OK** to save the configuration. If you're asked for a PIN, the default PIN is *123*.

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

SIP account registration tutorial for Fanvil IP phones:

## 1. **Configure a line with a Telnyx SIP trunk**

In this step you'll configure your first Telnyx SIP trunk via the phone's web interface or device screen. This guide focuses on the web interface. If you are using the phone screen, follow the instructions in the [pre-requisite section](#h_463b8b7b31) and use the parameters in this section.

1. Log into your web GUI and navigate to **Line > SIP**.
2. Use the **Line** dropdown to select a SIP line to configure, and provide the following:
3. In the **Register Settings** section:

   1. **Username:** This is your Telnyx portal main or sub-account username.
   2. **Display Name:** This is your caller ID. You can choose whatever you like, but keep in mind the following naming conventions:

      1. Caller ID Name should be in capital letters. This will appears more clearly/visible on some devices.
      2. You must NOT use any special characters, as they will not be displayed. Spaces are allowed.
      3. Some of regular Canadian providers will not show more than 15 characters. We suggest shrinking or adapt your caller ID.
   3. **Realm:** Enter the name of the realm to which the SIP interface is connected.
   4. **Authentication User:** This is your Telnyx portal main or sub-account username.
   5. **Authentication Password:** This is your Telnyx portal main or sub-account password.
   6. **Server Name**: *sip.telnyx.com* (For international, see [this document](https://sip.telnyx.com/#signaling-addresses).)
4. In the **SIP Server 1** sub-section:

   1. **Server Address:** *sip.telnyx.com* (For international, see [this document](https://sip.telnyx.com/#signaling-addresses).)
   2. **Server Port:** If you are using TCP or UDP transport, use port *5060*. If you are using TLS transport, use port *5061.*
   3. **Transport Protocol:** Choose *TCP* or *UDP* unless you are encrypting traffic and have set up encryption on your Telnyx portal. In this case, choose *TLS*.
   4. **Proxy Server Address:** *sip.telnyx.com* (For international, see [this document](https://sip.telnyx.com/#signaling-addresses).)

   ![SIP Server 1 sub-section.](_images/4824a0b4d660ea0c.png)
5. You can now configure the **SIP Server 2** section if you want.

[Back to Top](#h_9b42e0da7f)

## 2. Configure voice and video settings

In this section, you'll add codecs to your phone configuration that will support optimal audio and video.

1. From the line you configured in [step 1](#h_014039ea68), expand the **Codecs Settings** section.
2. From here, you can set the priority and availability of audio and video codecs by adding or removing them from the list. The following is a list of codecs (both audio and video) that Telnyx supports:

   **Audio:**

   * *ulaw(g711u)*
   * *alaw(g711a)*
   * *g722*
   * *g729*

   **Video:**

   * *H264*

That's it, you've now completed the configuration of the Fanvil A32i IP phone with your Telnyx account.  
​

[Back to Top](#h_9b42e0da7f)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally you can check out:

* [Fanvil A32i user manual](https://fanvil.com.hk/wp-content/uploads/2021/09/A32i-Android-Console-IP-Phone-A32i-User-Manual.pdf)
* [Fanvil FAQ](https://www.fanvil.com/Support/index.html)
* [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html)
* [Fanvil support](https://www.fanvil.com/Support/ticket.html)
* [Fanvil A32i firmware](https://www.fanvil.com/Support/download/id/139.html)

---

Related Articles

[Fanvil H2U: Compact IP](https://support.telnyx.com/en/articles/6202755-fanvil-h2u-compact-ip)[Fanvil H3: Hotel IP](https://support.telnyx.com/en/articles/6202965-fanvil-h3-hotel-ip)[Fanvil H3W/H5W: WiFi IP](https://support.telnyx.com/en/articles/6203347-fanvil-h3w-h5w-wifi-ip)[Fanvil X2CP/X2C/X2P: Call Center IP](https://support.telnyx.com/en/articles/6206756-fanvil-x2cp-x2c-x2p-call-center-ip)[Fanvil X-Series: IP Phone](https://support.telnyx.com/en/articles/6209971-fanvil-x-series-ip-phone)

Did this answer your question?

😞😐😃

Table of contents
