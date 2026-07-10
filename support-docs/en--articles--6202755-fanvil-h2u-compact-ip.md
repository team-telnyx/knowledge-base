---
source_url: https://support.telnyx.com/en/articles/6202755-fanvil-h2u-compact-ip
scraped: 2026-07-08
content_hash: 4aa4bbd3b66218fc9e7a7f9063586c2bfd57a4cbcf01c7b3f5cd1473994cd1e2
---

Fanvil H2U: Compact IP | Telnyx Help Center

[Skip to main content](#main-content)

# Fanvil H2U: Compact IP

Learn how to configure a Telnyx SIP trunk on the Fanvil H2U Compact IP phone

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_74c1412ea0)

Tiny and stylish, [Fanvil H2U Compact IP phone](https://www.fanvil.com/Product/info/id/122.html) possesses brand new features including 2 SIP lines, 10 speed dial keys, 1 programmable DSS key and a HD speaker on handset. Supporting desktop and wall-mounted mode, PoE and power supply charging mode, Fanvil H2U is more than a hotel phone and also can be applied in multiple scenarios, such as school, hospital, supermarket and residence.

**Product Features**

* HD audio
* Opus
* 2 SIP lines
* 10 speed dial keys
* 1 DSS key
* Supports PoE

**Additional resources:**

* [Fanvil H2U user manual](https://www.fanvil.com/Uploads/Temp/download/20210421/607fcc2424c72.pdf)
* [Fanvil FAQ](https://www.fanvil.com/Support/index.html)
* [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html)
* [Fanvil support](https://www.fanvil.com/Support/ticket.html)
* [Fanvil H2U firmware](https://www.fanvil.com/Support/download/id/122.html)

---

# Instructions for setting up and configuring your Fanvil H2U IP phone

In this activity you will:

1. [Configure a line with a Telnyx SIP trunk](#h_7de14f1e6f)
2. [Configure voice and video settings](#h_e01a992dd5)

**Pre-requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
* Make sure your phone is running the [latest firmware](https://www.fanvil.com/Support/download/id/122.html)
* Make sure you can log into the web GUI. This is where you'll configure your [SIP trunk](https://telnyx.com/products/sip-trunks). Each phone is shipped with its own administrator account. The first time you log into the web GUI, use the default credentials:

  + **Username:** *admin*
  + **Password:** *admin*

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

SIP account registration tutorial for Fanvil IP phones:

## 1. **Configure a line with a Telnyx SIP trunk**

In this step you'll configure your first Telnyx SIP trunk via the phone's web interface or device screen. This guide focuses on the web interface. If you are using the phone screen, follow the instructions in the [pre-requisite section](#h_a99bb9c4ca) and use the parameters in this section.

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

   ![Register Settings section in the web GUI. ](_images/4824a0b4d660ea0c.png)
5. You can now configure the **SIP Server 2** section if you want.

[Back to Top](#h_74c1412ea0)

## 2. Configure voice and video settings

In this section, you'll add codecs to your phone configuration that will support optimal audio and video.

1. From the line you configured in [step 1](#h_7de14f1e6f), expand the **Codecs Settings** section.
2. From here, you can set the priority and availability of audio and video codecs by adding or removing them from the list. The following is a list of codecs (both audio and video) that Telnyx supports:

   **Audio:**

   * *ulaw(g711u)*
   * *alaw(g711a)*
   * *g722*
   * *g729*

   **Video:**

   * *H264*

That's it, you've now completed the configuration of the Fanvil H2U IP phone with your Telnyx account.  
​

[Back to Top](#h_74c1412ea0)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally you can check out:

* [Fanvil H2U user manual](https://www.fanvil.com/Uploads/Temp/download/20210421/607fcc2424c72.pdf)
* [Fanvil FAQ](https://www.fanvil.com/Support/index.html)
* [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html)
* [Fanvil support](https://www.fanvil.com/Support/ticket.html)
* [Fanvil H2U firmware](https://www.fanvil.com/Support/download/id/122.html)

---

Related Articles

[Fanvil H3: Hotel IP](https://support.telnyx.com/en/articles/6202965-fanvil-h3-hotel-ip)[Fanvil H3W/H5W: WiFi IP](https://support.telnyx.com/en/articles/6203347-fanvil-h3w-h5w-wifi-ip)[Fanvil X2CP/X2C/X2P: Call Center IP](https://support.telnyx.com/en/articles/6206756-fanvil-x2cp-x2c-x2p-call-center-ip)[Fanvil V-Series: IP Phones](https://support.telnyx.com/en/articles/6209862-fanvil-v-series-ip-phones)[Fanvil X-Series: IP Phone](https://support.telnyx.com/en/articles/6209971-fanvil-x-series-ip-phone)

Did this answer your question?

😞😐😃

Table of contents
