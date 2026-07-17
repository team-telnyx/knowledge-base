---
source_url: https://support.telnyx.com/en/articles/6209971-fanvil-x-series-ip-phone
title: "Fanvil X-Series: IP Phone"
description: "Learn how to configure a Telnyx SIP trunk on the Fanvil X-Series IP… See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: ef51d4d7b305a08d1ea7fd9bf8da858705d59e6dfc37db9cf94e6f5991b3837d
---







# Fanvil X-Series: IP Phone

Learn how to configure a Telnyx SIP trunk on the Fanvil X-Series IP… See Telnyx guidance and requirements.

C




[Jump to Instructions](#h_194e85ab33)

The [Fanvil X-series](https://fanvil.com/products/p1/x/index.html) of SIP desk phones includes a wide range of IP phones with something for everyone and covers everything from entry level to high-end models.

|  |
| --- |
| ***Note:*** *This document covers all X-series IP phones with the exception of the [X4/X4G](https://app.intercom.com/a/apps/ltcafuzd/articles/articles/5811487/show) and the [X2C/X2CP](https://app.intercom.com/a/apps/ltcafuzd/articles/articles/6206756/show) phones, which are linked here.* |

**Additional Resources:**

* [X-series firmware and user manuals](https://fanvil.com/service/doc/file/p1/x1/x7agaoduanchupinghuaji/index.html)
* [Fanvil FAQ](https://www.fanvil.com/Support/index.html)
* [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html)
* [Fanvil support](https://www.fanvil.com/Support/ticket.html)

---

## Instructions for setting up and configuring a SIP trunk on the Fanvil X-series IP phones

**In this activity you will:**

1. [Configure a line with a Telnyx SIP trunk](#h_70e206af13)
2. [Configure voice and video settings](#h_f9c88af28f)
3. [(Optional) Upload a TLS certificate (For encrypted connections)](#h_bce8a291b6)

**Pre-requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
* Make sure your phone is running the [latest firmware](https://www.fanvil.com/Support/download/id/91.html)
* Make sure you can log into the web GUI. Refer to the Web Management section of your phone's user manual for instructions.

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

SIP account registration tutorial for Fanvil IP phones:

## 1. **Configure a line with a Telnyx SIP trunk**

In this step you'll configure your first Telnyx [SIP trunk](https://telnyx.com/products/sip-trunks) via the phone's web interface or device screen. This guide focuses on the web interface. If you are using the phone screen, follow the instructions in the [pre-requisite section](#h_9af24f5345) and use the parameters in this section.

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

   ![ Register Settings section of the Web GUI. ](_images/4824a0b4d660ea0c.png)
5. You can now configure the **SIP Server 2** section if you want.

[Back to Top](#h_194e85ab33)

## 2. Configure voice and video settings

In this section, you'll add codecs to your phone configuration that will support optimal audio and video.

1. From the line you configured in [step 1](#h_70e206af13), expand the **Codecs Settings** section.
2. From here, you can set the priority and availability of audio and video codecs by adding or removing them from the list. The following is a list of codecs (both audio and video) that Telnyx supports:

   **Audio:**

   * *ulaw(g711u)*
   * *alaw(g711a)*
   * *g722*
   * *g729*

   **Video:**

   * *H264*

[Back to Top](#h_194e85ab33)

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

That's it, you've now completed the configuration of your Fanvil X-series IP phone with your Telnyx account.

[Back to Top](#h_194e85ab33)

---

## Additional Resources

## Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally you can check out:

* [X-series firmware and user manuals](https://fanvil.com/service/doc/file/p1/x1/x7agaoduanchupinghuaji/index.html)
* [Fanvil FAQ](https://www.fanvil.com/Support/index.html)
* [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html)
* [Fanvil support](https://www.fanvil.com/Support/ticket.html)

---

---

Related Articles

[Fanvil H2U: Compact IP](https://support.telnyx.com/en/articles/6202755-fanvil-h2u-compact-ip)[Fanvil H3: Hotel IP](https://support.telnyx.com/en/articles/6202965-fanvil-h3-hotel-ip)[Fanvil X2CP/X2C/X2P: Call Center IP](https://support.telnyx.com/en/articles/6206756-fanvil-x2cp-x2c-x2p-call-center-ip)[Fanvil X7 Series: IP Phones](https://support.telnyx.com/en/articles/6209215-fanvil-x7-series-ip-phones)[Fanvil XU Series: IP Phone](https://support.telnyx.com/en/articles/6210147-fanvil-xu-series-ip-phone)

Did this answer your question?

😞😐😃
