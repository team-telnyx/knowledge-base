---
source_url: https://support.telnyx.com/en/articles/6281943-alcatel-sd601-sd602-sip-door
scraped: 2026-06-11
---

Alcatel: SD601/SD602 SIP Door | Telnyx Help Center

[Skip to main content](#main-content)

# Alcatel: SD601/SD602 SIP Door

Learn how to configure a Telnyx SIP trunk with the Alcatel SD601 and SD 602 SIP door phones.

C

Written by Customer Success

June 6, 2024

Table of contents

[Jump to Instructions](#h_e5d1b913a9)

The [Alcatel SD601 SIP door phone](https://www.alcatel-home.com/en2/product/alcatel-sd601), and [SD602 SIP door phone](https://www.alcatel-home.com/en2/product/alcatel-sd602) are robust, heavy-duty access-control video solutions. Offering a CMOS camera *(602 only)*, an RFID reader, and relay access control, the SD602 supports up to 2 SIP accounts so you can know for sure that your business is secure. This door phone unit is compatible with the [Alcatel SP2505G IP phone](https://www.alcatel-home.com/en2/product/alcatel-sp2505g).

**Main features:**

* 1280x760 CMOS camera *(602 only)*
* 1 Programmable key with backlight
* Door opening with [DTMF](https://support.telnyx.com/en/articles/1130710-what-is-dtmf), PIN code, RFID card or indoor switch
* 1 embedded door switch relay
* 1 embedded indoor switch interface
* 2 SIP accounts
* Power over Ethernet
* Integrated noise reduction with 2 mics *(602 only)*
* Indoor usage
* Full duplex handsfree
* Dust and water protected as per IP65

**Additional resources:**

* [User manual](https://www.alcatel-home.com/sites/default/files/product/1507/files/alcatel-sd601-qg.pdf) (SD601)
* [Connection guide](https://www.alcatel-home.com/sites/default/files/product/1507/files/alcatel-sd601-mountingdimensions.pdf) (SD601)
* [User manual](https://www.alcatel-home.com/sites/default/files/product/1508/files/alcatel-sd602qg.pdf) (SD602)
* [Datasheet](https://www.alcatel-home.com/sites/default/files/product/1441/files/alcatelsd601en2021.pdf) (SD601)
* [Datasheet](https://www.alcatel-home.com/sites/default/files/product/1447/files/alcatelsd602en2021.pdf) (SD602)
* [Product support](https://www.alcatel-home.com/en2/customer-service-after-sales-support)
* [Customer service](https://www.alcatel-home.com/en2/customer-service-after-sales-support)

---

# Instructions for configuring a Telnyx SIP trunk with the Alcatel SD60x SIP door phone

**In this activity you will:**

1. [Connect your door phone with the web interface](#h_f6c29429e9)
2. [Configure a SIP trunk](#h_f2b3baf8c6)

**Pre-requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* [Purchase a DID from Telnyx](https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers)

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for the Alcatel SD60x door phone/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Connect your door phone with the web interface

In this section, you will get the IP address of your door phone and use it to log into the web interface.

1. Power on your door phone and press and hold the # key on the phone's keypad for 3 seconds. You will hear an audio announcement that will read out your device's IP address. Take note of this.
2. Open a web browser on your computer (ensure the computer is on the same network). and enter *http://*<THE IP ADDRESS YOU OBTAINED IN STEP 1>
3. You'll need to log into the web interface. The default login credentials are:

   1. **Username:** *admin*
   2. **Password:** *admin*

|  |
| --- |
| ***Note:*** *Your system uses DHCP by default to obtain an IP address. If you want to use a fixed IP address (the default is 192.168.1.128), press and hold the DSS key for 10 seconds until you hear a beep. Then press the DSS key 3 times. After 10 seconds, the IP address acquisition mode will be changed.* |

[Back to Top](#h_e5d1b913a9)

## 2. Configure a SIP trunk

In this section, you will add a Telnyx [SIP trunk](https://telnyx.com/products/sip-trunks) to your door phone.

1. From the web interface, navigate to **SYSTEM > SIP Accounts**.
2. Provide the following configuration information:

   1. **Phone number:** One of the DIDs you have purchased from Telnyx as part of your [pre-requisite activities](#h_398c0cf58d).
   2. **Display name:** The name you want to see displayed when the door phone calls your phone. (Your door phone's caller ID.)
   3. **Authentication Name:** Your Telnyx portal username
   4. **Authentication Password:** Your Telnyx portal password
   5. **Activate:** Checking this box will activate the SIP trunk
   6. **SIP Proxy Server Address:** *sip.telnyx.com* (US. For international, see [this document](https://sip.telnyx.com/#signaling-addresses).)
   7. **SIP Proxy Server Port:** *5060*

That's it, you've now completed the configuration of your SIP door phone with your Telnyx account.

[Back to Top](#h_e5d1b913a9)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally you can check out (the same links as you find in the Additional resources section:

* [User manual](https://www.alcatel-home.com/sites/default/files/product/1507/files/alcatel-sd601-qg.pdf) (SD601)
* [Connection guide](https://www.alcatel-home.com/sites/default/files/product/1507/files/alcatel-sd601-mountingdimensions.pdf) (SD601)
* [User manual](https://www.alcatel-home.com/sites/default/files/product/1508/files/alcatel-sd602qg.pdf) (SD602)
* [Datasheet](https://www.alcatel-home.com/sites/default/files/product/1441/files/alcatelsd601en2021.pdf) (SD601)
* [Datasheet](https://www.alcatel-home.com/sites/default/files/product/1447/files/alcatelsd602en2021.pdf) (SD602)
* [Product support](https://www.alcatel-home.com/en2/customer-service-after-sales-support)
* [Customer service](https://www.alcatel-home.com/en2/customer-service-after-sales-support)

---

Related Articles

[Fanvil A32i: Telnyx Setup](https://support.telnyx.com/en/articles/6056428-fanvil-a32i-telnyx-setup)[Grandstream GRP260x: SIP Trunk](https://support.telnyx.com/en/articles/6169513-grandstream-grp260x-sip-trunk)[Grandstream GRP2612: SIP Trunk](https://support.telnyx.com/en/articles/6184147-grandstream-grp2612-sip-trunk)[Grandstream GXP1700: SIP Trunk](https://support.telnyx.com/en/articles/6184520-grandstream-gxp1700-sip-trunk)[Fanvil H3W/H5W: WiFi IP](https://support.telnyx.com/en/articles/6203347-fanvil-h3w-h5w-wifi-ip)

Did this answer your question?

😞😐😃

Table of contents
