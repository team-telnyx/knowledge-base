---
source_url: https://support.telnyx.com/en/articles/5807979-konftel-300wx-telnyx-setup
scraped: 2026-07-08
content_hash: ee9ad29b8d22624f13d9b9f8f41b4844ed0e1939a28a580f423d301e8a491a19
---

Konftel 300Wx: Telnyx Setup | Telnyx Help Center

[Skip to main content](#main-content)

# Konftel 300Wx: Telnyx Setup

Effortlessly set up and configure Konftel 300 Series conference phones with Telnyx for enhanced communication solutions.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_cab6579182)

[Konftel](https://www.konftel.com/) has become one of the large names in conference calling since its inception in 1988. Konftel is Client-Neutral certified.

The [Konftel 300Wx](https://www.konftel.com/en/products/konftel-300wx) is a wireless conference phone that allows you to hold meetings wherever is convenient for you without being confined by networks or. outlets. The wireless DECT technology is reliable and secure. The rechargeable battery ensures more than 60 call hours, so you can talk for a full work week without worrying about power. Hybrid design combines the Konftel meeting app with phone calls and the microphone capability can be expanded to allow for additional mics.

Additional documentation:

* [Konftel 300Wx product data sheet](https://www.konftel.com/-/media/konftel/files/product-documentation/konftel-300wx/konftel300wx_datasheet_eng-low.pdf?la=en)
* [Konftel 300Wx installation guide](https://www.konftel.com/-/media/konftel/files/user-guide/konftel-ip-dect-10---installation-guide/ip-dect-10-system-guide_eng.pdf?la=en)
* [Konftel 300Wx quickstart guide](https://www.konftel.com/-/media/konftel/files/quick-guide/konftel-300wx/konftel300wx-qg_eng.pdf?la=en)
* [Konftel 300Wx user guide](https://www.konftel.com/-/media/konftel/files/user-guide/konftel-300wx/user-guide-konftel-300wx_rev5-c_eng.pdf?la=en)
* [Konftel support](https://www.konftel.com/en/support)

---

# Instructions for configuring the Konftel 300Wx conference phone

In this activity you will

1. [Obtain your device's IP address](#h_b70cb77f87)
2. [Add a SIP server in the Konftel web portal](#h_0cb2710e56)
3. [Add an extension](#h_63b1fc7734)
4. [Verify that your server is registered](#h_65f8d771eb)

**Pre-requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* [Provision a DID from Telnyx](https://portal.telnyx.com/#/app/numbers/search-numbers) ([How do I do this?](https://support.telnyx.com/en/articles/3562148-requesting-numbers))

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Panasonic KX-TGP 550 phone/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Obtain your device's IP address

In this step, you'll log into the Konftel web portal in order to obtain the device's IP address, which you'll need to complete future steps.

1. From your 300Wx device, go into the phone menu.
2. Click on **Status**, then select **Network**.
3. You'll find the IP address here. Take note of it, as you'll need it in a future step.
4. From your computer, open a web browser and enter your phone's IP address into the address bar. Prepend this with *<http://>.*
5. For your first login, use the default credentials:

   1. **Username:** admin
   2. **Password:** admin

[Back to Top](#h_cab6579182)

## 2. Add a SIP server in the Konftel web portal

In this step, you'll create and configure a SIP server in Konftel and connect it to Telnyx.

1. From the left-hand menu of the Konftel web portal, click **Server**.
2. From the **Server** page, click **Add Server** and provide the following information:

   1. **Server Alias:** Choose a name for your server.
   2. **NAT Adaption:** *Enabled*
   3. **Registrar:** *sip.telnyx.com*
   4. **Outbound Proxy:** *sip.telnyx.com*
   5. **Reregistration Time (s):** *300*
   6. **SIP Transport:** *TCP*
   7. **Keep Alive:** *Enabled*
   8. **Codec Priority:** Your chosen Telnyx-supported codecs:

      1. ulaw(g711u)
      2. alaw(g711a)
      3. g722
      4. g729
   9. (If you have enabled TLS and wish to encrypt calls over your device) **Secure RTP:** *Enabled*
   10. (If you have enabled TLS and wish to encrypt calls over your device) **Secure RTP Auth**: *Enabled*
3. Click **Save**.

[Back to Top](#h_cab6579182)

## 3. Add an extension

In this step, you'll add an extension for your 300Wx

1. From the left-hand menu of the Konftel web portal, click **Extensions**.
2. On the Extensions window, click **Add Extension** and provide the following information:

   1. **Extension:** Your Telnyx DID
   2. **Authentication Username:** Your Telnyx SIP username
   3. **Authentication Password:** Your Telnyx SIP password
   4. **Server:** The server you created in [step 2](#h_0cb2710e56). Make sure if you have multiple servers configured, you select the right one.
3. On the right, select the device you want to use for this extension.
4. Click **Save**.

[Back to Top](#h_cab6579182)

## 4 Verify that your server is running

In this step, you'll confirm your device was registered.

1. From the left-hand menu of the Konftel web portal, click **Extensions** and check your new server's **State** field in the table. It shoud say *SIP Registered*.

That's it! You have now set up and configured your Konftel 300Wx to work with Telnyx.

[Back to Top](#h_cab6579182)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [Konftel 300Wx product data sheet](https://www.konftel.com/-/media/konftel/files/product-documentation/konftel-300wx/konftel300wx_datasheet_eng-low.pdf?la=en)
* [Konftel 300Wx installation guide](https://www.konftel.com/-/media/konftel/files/user-guide/konftel-ip-dect-10---installation-guide/ip-dect-10-system-guide_eng.pdf?la=en)
* [Konftel 300Wx quickstart guide](https://www.konftel.com/-/media/konftel/files/quick-guide/konftel-300wx/konftel300wx-qg_eng.pdf?la=en)
* [Konftel 300Wx user guide](https://www.konftel.com/-/media/konftel/files/user-guide/konftel-300wx/user-guide-konftel-300wx_rev5-c_eng.pdf?la=en)
* [Konftel support](https://www.konftel.com/en/support)

---

---

Related Articles

[Polycom: Setup with Telnyx](https://support.telnyx.com/en/articles/5619617-polycom-setup-with-telnyx)[Flyingvoice: Telnyx Setup](https://support.telnyx.com/en/articles/5810663-flyingvoice-telnyx-setup)[Gigaset A510: Telnyx Setup](https://support.telnyx.com/en/articles/5815209-gigaset-a510-telnyx-setup)[Snom C520: Telnyx Setup](https://support.telnyx.com/en/articles/5815678-snom-c520-telnyx-setup)[Konftel 300IPx: Telnyx Setup](https://support.telnyx.com/en/articles/5822579-konftel-300ipx-telnyx-setup)

Did this answer your question?

😞😐😃

Table of contents
