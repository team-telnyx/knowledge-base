---
source_url: https://support.telnyx.com/en/articles/6206533-fanvil-x1-x1p-ip-phone
scraped: 2026-06-11
---

Fanvil X1/X1P: IP Phone | Telnyx Help Center

[Skip to main content](#main-content)

# Fanvil X1/X1P: IP Phone

The Fanvil X1 / X1P IP phone is an economical professional desktop IP Telephone ideal for entry-level users.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_00cf95e4ef)

[The Fanvil X1 / X1P IP phone](https://www.fanvil.com/Product/info/id/89.html) is an entry-level, cost-effective professional desktop IP Telephone. Coupled with basic features including 2-lines, 3-party conference function, easy-to-read backlight Lattice display, it deftly meets the affordability and reliability requirements of any budget.

**Product features:**

* 2 lines
* 128 x 48 clear backlight screen
* 3-way conference calling
* RJ9
* PoE

**Additional resources:**

* [Fanvil X1/XP user manual](https://www.fanvil.com/Uploads/Temp/download/20201109/5fa90afc7ca32.pdf)
* [Fanvil FAQ](https://www.fanvil.com/Support/index.html)
* [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html)
* [Fanvil support](https://www.fanvil.com/Support/ticket.html)
* [Fanvil X1/XP firmware](https://www.fanvil.com/Support/download/id/89.html)

---

# Instructions for setting up and configuring your Fanvil X1/XG IP phone

In this activity you will:

1. [Configure a line with a Telnyx SIP trunk](#h_95438cbd0a)
2. [Configure voice and video](#h_1fc2812cc6)
3. [(Optional) Upload a TLS certificate](#h_5efc0358da)

**Pre-requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
* Make sure your phone is running the latest [firmware](https://www.fanvil.com/Support/download/id/89.html)
* Make sure you can log into the web GUI. This is where you'll configure your [SIP trunk](https://telnyx.com/products/sip-trunks). You can find the default credentials and other information on page 15 of the [phone's user manual](https://www.fanvil.com/Uploads/Temp/download/20201109/5fa90afc7ca32.pdf) (Section 4.4: Web Portal)

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

SIP account registration tutorial for Fanvil IP phones:

## 1. **Configure a line with a Telnyx SIP trunk**

In this step you'll configure your first Telnyx SIP trunk via the phone's web interface or device screen. This guide focuses on the web interface. If you are using the phone screen, follow the instructions in the [pre-requisite section](#h_a9d2a3cf6c) and use the parameters in this section.

1. Log into your web GUI and navigate to **Line > SIP**.
2. Use the **Line** dropdown to select a SIP line to configure, and provide the following:
3. In the **Basic Settings** section:

   1. **Username:** The SIP connection username. Learn more [here](https://support.telnyx.com/en/articles/4245868-sip-connection-types) in the Credentials Connection Setup section.
   2. **Display Name:** This is your caller ID. You can choose whatever you like, but keep in mind the following naming conventions:

      1. Caller ID Name should be in capital letters. This will appears more clearly/visible on some devices.
      2. You must NOT use any special characters, as they will not be displayed. Spaces are allowed.
      3. Some of regular Canadian providers will not show more than 15 characters. We suggest shrinking or adapt your caller ID.
   3. **Authentication Name:** The SIP connection username. Learn more [here](https://support.telnyx.com/en/articles/4245868-sip-connection-types) in the Credentials Connection Setup section.
   4. **Authentication Password:** The SIP connection password. Learn more [here](https://support.telnyx.com/en/articles/4245868-sip-connection-types) in the Credentials Connection Setup section.
   5. **SIP Proxy Server Address:** *sip.telnyx.com* (For international, see [this document](https://sip.telnyx.com/#signaling-addresses).) Note that this will also be the outbound proxy server address, and the backup proxy server address.)
   6. **SIP Proxy Port:** If you are using TCP or UDP transport, use port *5060*. If you are using TLS transport, use port *5061.*
   7. **Outbound Proxy Address**: *sip.telnyx.com* (For international, see [this document](https://sip.telnyx.com/#signaling-addresses).)
   8. **Outbound Proxy Port:** If you are using TCP or UDP transport, use port *5060*. If you are using TLS transport, use port *5061.*
   9. **Realm:** Enter the name of the realm to which the SIP interface is connected.
4. In the **Advanced Settings** sub-section:

   1. **DTMF Type:** *RFC 2833*
   2. **Transportation Protocol:** Choose *TCP* or *UDP* unless you are encrypting traffic and have set up encryption on your Telnyx portal. In this case, choose *TLS*.  
      ​  
      ​*Note that if you are encrypting traffic, you'll need to go into **Lines > Dial Peer** and make sure the **Port** setting is changed to* 5061.
   3. **RTP Encryption**: (Optional) Enable this if you're using TLS
   4. **RTP Encryption Key:** (Optional) Obtain a key [here](https://crt.sh/?id=1199354).

## 2. Configure voice and video

1. In the **Codecs Settings** section:

   1. Set the priority and availability of audio and video codecs by adding or removing them from the list. The following is a list of codecs (both audio and video) that Telnyx supports:

      **Audio:**

      * *ulaw(g711u)*
      * *alaw(g711a)*
      * *g722*
      * *g729*

      **Video:**

      * *H264*

[Back to Top](#h_00cf95e4ef)

## 3. (Optional) Upload a TLS certificate (For encrypted connections)

If you are encrypting traffic with TLS, you'll need to upload a TLS certificate, which you'll do in this section.

1. Navigate to **Line > Basic Settings** and find the **STUN Settings** section and set:

   1. **TLS Certification File:** Obtain a certificate [here](https://crt.sh/?id=1199354)

That's it, you've now completed the configuration of the Fanvil X1/X1P IP Phone with your Telnyx account.  
​

[Back to Top](#h_00cf95e4ef)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally you can check out:

* [Fanvil X1/XP user manual](https://www.fanvil.com/Uploads/Temp/download/20201109/5fa90afc7ca32.pdf)
* [Fanvil FAQ](https://www.fanvil.com/Support/index.html)
* [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html)
* [Fanvil support](https://www.fanvil.com/Support/ticket.html)
* [Fanvil X1/XP firmware](https://www.fanvil.com/Support/download/id/89.html)

---

Related Articles

[Fanvil H2U: Compact IP](https://support.telnyx.com/en/articles/6202755-fanvil-h2u-compact-ip)[Fanvil H3: Hotel IP](https://support.telnyx.com/en/articles/6202965-fanvil-h3-hotel-ip)[Fanvil H5: Hotel IP](https://support.telnyx.com/en/articles/6203401-fanvil-h5-hotel-ip)[Fanvil X7 Series: IP Phones](https://support.telnyx.com/en/articles/6209215-fanvil-x7-series-ip-phones)[Fanvil X-Series: IP Phone](https://support.telnyx.com/en/articles/6209971-fanvil-x-series-ip-phone)

Did this answer your question?

😞😐😃

Table of contents
