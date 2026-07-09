---
source_url: https://support.telnyx.com/en/articles/6203401-fanvil-h5-hotel-ip
scraped: 2026-07-08
content_hash: 614e5fff31d793cd71927030734644d5eb16d790bca7d8d59ef1d5a6d60e336b
---

Fanvil H5: Hotel IP | Telnyx Help Center

[Skip to main content](#main-content)

# Fanvil H5: Hotel IP

Learn how to configure a Telnyx SIP trunk on the Fanvil H5 Hotel IP phone

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_e5274d3b35)

With two available colors (White & Black), [Fanvil H5](https://www.fanvil.com/Product/info/id/79.html) is a great and affordable choice for hotel IP phone. Possessing a 3.5-inch color screen, it is also an user-friendly hotel IP phone. Hotel could customize the information (such as hotel’s address, logo, related phone numbers and etc) on the screen, and bring a better living experience to the hotel guests.

**Product features:**

* 3.5-inch color screen
* HD audio
* 1 USB charging port
* 6 programmable keys
* Call transfer
* PoE

**Additional resources:**

* [Fanvil H5 user manual](https://www.fanvil.com/Uploads/Temp/download/20201110/5faa5e5b85b05.pdf)
* [Fanvil FAQ](https://www.fanvil.com/Support/index.html)
* [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html)
* [Fanvil support](https://www.fanvil.com/Support/ticket.html)
* [Fanvil H5 firmware](https://www.fanvil.com/Support/download/id/79.html)

---

# Instructions for setting up and configuring your Fanvil H5 Hotel IP phone

In this activity you will:

1. [Configure a line with a Telnyx SIP trunk](#h_c8e19c59ae)
2. [Configure voice and video](#h_b68b90ac2b)

**Pre-requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
* Make sure your phone is running the latest [firmware](https://www.fanvil.com/Support/download/id/79.html)
* Make sure you can log into the web GUI. This is where you'll configure your [SIP trunk](https://telnyx.com/products/sip-trunks). You can find the default credentials and other information on page 13 of the [phone's user manual](https://www.fanvil.com/Uploads/Temp/download/20201110/5faa5e5b85b05.pdf) (5: Phone Settings - sections 5.1 -.53)

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

SIP account registration tutorial for Fanvil IP phones:

## 1. **Configure a line with a Telnyx SIP trunk**

In this step you'll configure your first Telnyx SIP trunk via the phone's web interface or device screen. This guide focuses on the web interface. If you are using the phone screen, follow the instructions in the [pre-requisite section](#h_2aeb783943) and use the parameters in this section.

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

   1. **SIP Proxy Address:** *sip.telnyx.com* (For international, see [this document](https://sip.telnyx.com/#signaling-addresses).)
   2. **SIP Proxy Port:** If you are using TCP or UDP transport, use port *5060*. If you are using TLS transport, use port *5061.*
   3. **Outbound Proxy Address**: *sip.telnyx.com* (For international, see [this document](https://sip.telnyx.com/#signaling-addresses).)
   4. **Outbound Proxy Port:** If you are using TCP or UDP transport, use port *5060*. If you are using TLS transport, use port *5061.*
   5. **Realm:** Enter the name of the realm to which the SIP interface is connected.
4. In the **Advanced Settings** sub-section:

   1. **DTMF Type:** *RFC 2833*
   2. **Transport Protocol:** Choose *TCP* or *UDP* unless you are encrypting traffic and have set up encryption on your Telnyx portal. In this case, choose *TLS*.  
      ​  
      ​*Note that if you are encrypting traffic, you'll need to go into **Lines > Dial Peer** and make sure the **Port** setting is changed to* 5061.
   3. **SIP Encryption**: Enable this if you're using TLS
   4. **SIP Encryption Key:** Obtain a key [here](https://crt.sh/?id=1199354).

[Back to Top](#h_e5274d3b35)

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

That's it, you've now completed the configuration of the Fanvil H5 Hotel IP phone with your Telnyx account.  
​  
​

[Back to Top](#h_e5274d3b35)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally you can check out:

* [Fanvil H5 user manual](https://www.fanvil.com/Uploads/Temp/download/20201110/5faa5e5b85b05.pdf)
* [Fanvil FAQ](https://www.fanvil.com/Support/index.html)
* [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html)
* [Fanvil support](https://www.fanvil.com/Support/ticket.html)
* [Fanvil H5 firmware](https://www.fanvil.com/Support/download/id/79.html)

---

Related Articles

[Fanvil H2U: Compact IP](https://support.telnyx.com/en/articles/6202755-fanvil-h2u-compact-ip)[Fanvil H3: Hotel IP](https://support.telnyx.com/en/articles/6202965-fanvil-h3-hotel-ip)[Fanvil H3W/H5W: WiFi IP](https://support.telnyx.com/en/articles/6203347-fanvil-h3w-h5w-wifi-ip)[Fanvil X2CP/X2C/X2P: Call Center IP](https://support.telnyx.com/en/articles/6206756-fanvil-x2cp-x2c-x2p-call-center-ip)[Fanvil X-Series: IP Phone](https://support.telnyx.com/en/articles/6209971-fanvil-x-series-ip-phone)

Did this answer your question?

😞😐😃

Table of contents
