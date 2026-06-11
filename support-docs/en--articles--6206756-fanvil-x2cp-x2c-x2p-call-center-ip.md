---
source_url: https://support.telnyx.com/en/articles/6206756-fanvil-x2cp-x2c-x2p-call-center-ip
scraped: 2026-06-11
---

Fanvil X2CP/X2C/X2P: Call Center IP | Telnyx Help Center

[Skip to main content](#main-content)

# Fanvil X2CP/X2C/X2P: Call Center IP

Learn how to configure a Telnyx SIP trunk on the Fanvil X2C/X2P/X2CP call center IP phone

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_d64aa0e564)

|  |  |
| --- | --- |
| The [Fanvil X2CP call center IP phone](https://www.fanvil.com/Product/info/id/96.html#) offers an intuitive, clean design and rich features at a cost-effective price. The backlit high resolution display allow users to get access to key information at a glance. Effective call monitor, LED function keys for mute/hold/auto answering/headset and the foot pedal switch could greatly improve productivity of call center staff. PoE integrated and rich extension functions of call center headset support, EHS wireless headset support provides more convenience.    **Product features:**  * 2 lines * HD voice * EHS * Supervision * LED button * Pedal switch | The [Fanvil X2P/X2C call center IP phone](https://www.fanvil.com/Product/info/id/64.html) offers high C/P ratio and provides a unique foot pedal answer option. It has a 2.8 inch 320x240 color LCD, dual 10/100 mbps network ports with integrated PoE, ideal for extended network use. The X2P supports 2 lines and plus SRTP/HTTPS/TLS, VLAN and QoS. It includes RJ9 and 3.5mm port and EHS headset use and supervision, has been designed very specifically for improving the efficiency of call center service.      **Product Features:**  * Color screen * HD voice * EHS * Supervision * LED button * Pedal switch |

**Additional resources:**

* Firmware:

  + [X2CP](https://www.fanvil.com/Support/download/id/96.html)
  + [X2C/X2P](https://www.fanvil.com/Support/download/id/64.html)
* User Manuals:

  + [X2CP](https://www.fanvil.com/Uploads/Temp/download/20200109/5e16c3554c22d.pdf)
  + [X2C/X2P](https://www.fanvil.com/Uploads/Temp/download/20200109/5e16c31bac331.pdf)
* [Fanvil FAQ](https://www.fanvil.com/Support/index.html)
* [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html)
* [Fanvil support](https://www.fanvil.com/Support/ticket.html)

---

# Instructions for setting up and configuring your Fanvil X2C/X2P series call center IP phone

In this activity you will:

1. [Configure a line with a Telnyx SIP trunk](#h_7521dbc64e)
2. [Configure voice and video](#h_f1dfe71455)
3. [(Optional) Upload a TLS certificate](#h_c478278130)

**Pre-requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
* Make sure your phone is running the latest firmware (see the **Additional resources** section above.)
* Make sure you can log into the web GUI. Refer to the Web Portal section of your phone's user manual for instructions.

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

SIP account registration tutorial for Fanvil IP phones:

## 1. **Configure a line with a Telnyx SIP trunk**

In this step you'll configure your first Telnyx [SIP trunk](https://telnyx.com/products/sip-trunks) via the phone's web interface or device screen. This guide focuses on the web interface. If you are using the phone screen, follow the instructions in the [pre-requisite section](#h_60b100ea56) and use the parameters in this section.

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
   6. **SIP Proxy Server Port:** If you are using TCP or UDP transport, use port *5060*. If you are using TLS transport, use port *5061.*
   7. **Outbound Proxy Address**: *sip.telnyx.com* (For international, see [this document](https://sip.telnyx.com/#signaling-addresses).)
   8. **Outbound Proxy Port:** If you are using TCP or UDP transport, use port *5060*. If you are using TLS transport, use port *5061.*
   9. **Realm:** Enter the name of the realm to which the SIP interface is connected.

[Back to Top](#h_d64aa0e564)

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

[Back to Top](#h_d64aa0e564)

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

   1. **TLS Certification File:** Obtain a certificate [here](https://crt.sh/?id=1199354)

That's it, you've now completed the configuration of the Fanvil X2C/X2P series phone with your Telnyx account.  
​  
​

[Back to Top](#h_d64aa0e564)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally you can check out:

* Firmware:

  + [X2CP](https://www.fanvil.com/Support/download/id/96.html)
  + [X2C/X2P](https://www.fanvil.com/Support/download/id/64.html)
* User Manuals:

  + [X2CP](https://www.fanvil.com/Uploads/Temp/download/20200109/5e16c3554c22d.pdf)
  + [X2C/X2P](https://www.fanvil.com/Uploads/Temp/download/20200109/5e16c31bac331.pdf)
* [Fanvil FAQ](https://www.fanvil.com/Support/index.html)
* [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html)
* [Fanvil support](https://www.fanvil.com/Support/ticket.html)

---

Related Articles

[Fanvil H2U: Compact IP](https://support.telnyx.com/en/articles/6202755-fanvil-h2u-compact-ip)[Fanvil H3: Hotel IP](https://support.telnyx.com/en/articles/6202965-fanvil-h3-hotel-ip)[Fanvil H5: Hotel IP](https://support.telnyx.com/en/articles/6203401-fanvil-h5-hotel-ip)[Fanvil X1/X1P: IP Phone](https://support.telnyx.com/en/articles/6206533-fanvil-x1-x1p-ip-phone)[Fanvil X-Series: IP Phone](https://support.telnyx.com/en/articles/6209971-fanvil-x-series-ip-phone)

Did this answer your question?

😞😐😃

Table of contents
