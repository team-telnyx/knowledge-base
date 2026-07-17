---
source_url: https://support.telnyx.com/en/articles/6209215-fanvil-x7-series-ip-phones
title: "Fanvil X7 Series: IP Phones"
description: "Learn how to configure a Telnyx SIP trunk on the Fanvil X7A models/X7/X7C… See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: af6b31993be03fb2a546c27e5c677d05dfb6f007b0536d834c5eebf8634f1cc7
---







# Fanvil X7 Series: IP Phones

Learn how to configure a Telnyx SIP trunk on the Fanvil X7A models/X7/X7C… See Telnyx guidance and requirements.

C




[Jump to Instructions](#h_987b5f88b6)

|  |  |
| --- | --- |
| **FANVIL X7 IP PHONE**    The [Fanvil X7 IP phone](https://www.fanvil.com/Product/info/id/93.html) is a high-end enterprise phone for business users who need immediate access to all of their important information. In addition to a 7-inch capacitive touch screen for up to 127 DSS key entries, the telephone also features 20 SIP lines, HD audio with Opus support, Built-in Bluetooth, Wi-Fi connectivity and more!    **Product Features:**  * 20 lines * HD audio * 7" color display * Built-in Bluetooth * 127 DSS keys * WiFi connectivity | **FANVIL X7C IP PHONE**    The [Fanvil X7C IP phone](https://www.fanvil.com/Product/info/id/94.html) is a high-end enterprise IP phone for business users who need immediate access to all of their important information. In addition to a 5-inch high-resolution color screen, the telephone also features 20 SIP lines, HD audio with Opus support, up to 60 DSS keys (12 physical), Built-in Bluetooth, Wi-Fi connectivity and more!    **Product Features:**  * 20 lines * HD audio * 5" color display * Built-in Bluetooth * 60 DSS keys * WiFi connectivity |
| **FANVIL X7A ANDROID TOUCHSCREEN IP PHONE (with/without camera)**    With Android 9.0 OS, the [Fanvil X7A IP phone](https://www.fanvil.com/Product/info/id/124.html) provides a more intelligent and smoother touch operation experience for the users. 112 DSS keys on the 7-inch color touch screen, built-in WiFi, built-in Bluetooth make daily communication smarter and simpler. Matching an optional USB camera Fanvil CM60, Fanvil X7A can deliver a superb audio and video for the group conference.    **Product Features:**  * Android 9.0 OS * 20 SIP lines * HD audio * 7" color touchscreen * Built-in Bluetooth * 112 DSS keys * Built-in 2.4G/5G WiFi | **Additional resources:**  * Firmware:  + [X7](http://fanvil.com/Support/download/id/93.html)   + [X7C](https://www.fanvil.com/Support/download/id/94.html)   + [X7A](https://www.fanvil.com/Support/download/id/124.html)   + [X7A (with camera)](https://www.fanvil.com/Support/download/id/125.html) * User manuals  + [X7](https://www.fanvil.com/Uploads/Temp/download/20210106/5ff5946b8b78e.pdf)   + [X7C](https://www.fanvil.com/Uploads/Temp/download/20210106/5ff594a2412cf.pdf)   + [X7A](https://www.fanvil.com/Uploads/Temp/download/20210112/5ffd956d5a486.pdf)   + [X7A (with camera)](https://www.fanvil.com/Uploads/Temp/download/20210112/5ffd95117fb3f.pdf) * [Fanvil FAQ](https://www.fanvil.com/Support/index.html) * [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html) * [Fanvil support](https://www.fanvil.com/Support/ticket.html) |

---

## Instructions for setting up and configuring a SIP trunk on the Fanvil X7 series IP phones

**In this activity you will:**

1. [Configure a line with a Telnyx SIP trunk](#h_8f3fa7686b)
2. [Configure voice and video settings](#h_a8d458de58)
3. [(Optional) Upload a TLS certificate (For encrypted connections)](#h_033384e48f)

**Pre-requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
* Make sure your phone is running the [latest firmware](https://www.fanvil.com/Support/download/id/122.html)
* Make sure you can log into the web GUI. Refer to the Web Management section of your phone's user manual for instructions.

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

SIP account registration tutorial for Fanvil IP phones:

## 1. **Configure a line with a Telnyx SIP trunk**

In this step you'll configure your first Telnyx [SIP trunk](https://telnyx.com/products/sip-trunks) via the phone's web interface or device screen. This guide focuses on the web interface. If you are using the phone screen, follow the instructions in the [pre-requisite section](#h_bda0970c90) and use the parameters in this section.

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

   ![Register Settings section of the web GUI. ](_images/4824a0b4d660ea0c.png)
5. You can now configure the **SIP Server 2** section if you want.

[Back to Top](#h_987b5f88b6)

## 2. Configure voice and video settings

In this section, you'll add codecs to your phone configuration that will support optimal audio and video.

1. From the line you configured in [step 1](#h_8f3fa7686b), expand the **Codecs Settings** section.
2. From here, you can set the priority and availability of audio and video codecs by adding or removing them from the list. The following is a list of codecs (both audio and video) that Telnyx supports:

   **Audio:**

   * *ulaw(g711u)*
   * *alaw(g711a)*
   * *g722*
   * *g729*

   **Video:**

   * *H264*

[Back to Top](#h_987b5f88b6)

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

That's it, you've now completed the configuration of your Fanvil X7 series IP phone with your Telnyx account.

[Back to Top](#h_987b5f88b6)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally you can check out:

* Firmware:

  + [X7](http://fanvil.com/Support/download/id/93.html)
  + [X7C](https://www.fanvil.com/Support/download/id/94.html)
  + [X7A](https://www.fanvil.com/Support/download/id/124.html)
  + [X7A (with camera)](https://www.fanvil.com/Support/download/id/125.html)
* User manuals

  + [X7](https://www.fanvil.com/Uploads/Temp/download/20210106/5ff5946b8b78e.pdf)
  + [X7C](https://www.fanvil.com/Uploads/Temp/download/20210106/5ff594a2412cf.pdf)
  + [X7A](https://www.fanvil.com/Uploads/Temp/download/20210112/5ffd956d5a486.pdf)
  + [X7A (with camera)](https://www.fanvil.com/Uploads/Temp/download/20210112/5ffd95117fb3f.pdf)
* [Fanvil FAQ](https://www.fanvil.com/Support/index.html)
* [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html)
* [Fanvil support](https://www.fanvil.com/Support/ticket.html)

---

Related Articles

[Fanvil H2U: Compact IP](https://support.telnyx.com/en/articles/6202755-fanvil-h2u-compact-ip)[Fanvil H3: Hotel IP](https://support.telnyx.com/en/articles/6202965-fanvil-h3-hotel-ip)[Fanvil X2CP/X2C/X2P: Call Center IP](https://support.telnyx.com/en/articles/6206756-fanvil-x2cp-x2c-x2p-call-center-ip)[Fanvil X-Series: IP Phone](https://support.telnyx.com/en/articles/6209971-fanvil-x-series-ip-phone)[Fanvil XU Series: IP Phone](https://support.telnyx.com/en/articles/6210147-fanvil-xu-series-ip-phone)

Did this answer your question?

😞😐😃
