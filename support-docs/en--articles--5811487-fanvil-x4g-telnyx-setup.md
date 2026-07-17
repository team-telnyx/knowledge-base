---
source_url: https://support.telnyx.com/en/articles/5811487-fanvil-x4g-telnyx-setup
title: "Fanvil X4G: Telnyx Setup"
description: "Take control of your business communication with our step-by-step setup guide for Fanvil X4/X4G. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: e8d951e72f27dba5059f2df0426667dbd1b3d0d142af3ea268a88be354b7a7ba
---







# Fanvil X4G: Telnyx Setup

Take control of your business communication with our step-by-step setup guide for Fanvil X4/X4G. See Telnyx guidance and requirements.

C




[Jump to Instructions](#h_7fb71be8d0)

The [Fanvil X4/X4G](https://www.fanvil.com/Product/info/id/72.html) is a feature-rich sip phone for business. The 4-Line IP Phone has been designed by pursuing ease of use in even the tiniest details. Dual 10/100 Mbps(X4G: 10/100/1000 Mbps) network ports with integrated PoE are ideal for extended network use. Delivering a superb sound quality as well as rich visual experience. With second DSS color screen, the IP Phone supports up to 30 DSS keys which improve work efficiency. Using standard encryption protocols to perform highly secure remote provisioning and software upgrades.

Additional documentation:

* [Fanvil FAQ](https://www.fanvil.com/Support/index.html)
* [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html)
* [Fanvil support](https://www.fanvil.com/Support/ticket.html)
* [Fanvil X4 series firmware](https://www.fanvil.com/Support/download/id/72.html)

---

## Instructions for setting up and configuring your Fanvil X4G IP phone

In this activity you will:

1. [Get your phone's IP address](#h_e6c7d8a3ce)
2. [Create a SIP account in the Fanvil web portal](#h_4ff19ea74b)

**Pre-requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

SIP account registration tutorial for Fanvil IP phones:

## 1. Get your phone's IP address

In this step, you'll obtain the IP address from your Fanvil, which you'll need to log into the web portal in the next step.

1. From your IP phone go to **OK > Status ­> IP Address** to obtain its IP address.
2. From a computer on the same physical network, open a web browser and enter this IP address. Prepend it with *http://*
3. Log in for the first time with the following default credentials (Don't forget to change them after!)

   1. **Username:** *admin*
   2. **Password:** *admin*

[Back to Top](#h_7fb71be8d0)

## 2. Create a SIP account in the Fanvil web portal

In this section, you will create a SIP connection in Fanvil and link it to your Telnyx account.

1. Click on **Lines** in the left-hand menu.
2. Click on the **SIP** tab and provide the following:

   1. **Username:** Your or Telnyx account username
   2. **Display name:** This is your caller ID. You can choose whatever you like, but keep in mind the following naming conventions:

      1. Caller ID Name should be in capital letters. This will appears more clearly/visible on some devices.
      2. You must NOT use any special characters, as they will not be displayed. Spaces are allowed.
      3. Some of regular Canadian providers will not show more than 15 characters. We suggest shrinking or adapt your caller ID.
   3. **Authentication name:** Your Telnyx account username
   4. **Authentication Password:** Your Telnyx account password
   5. **Server Name:** *sip.telnyx.com*
   6. **Register Address:** *sip.telnyx.com*
   7. **Register Port:** If you are using UDP transport, use port *5060*. If you are using TLS transport, use port *5061.*
   8. **Proxy Server Address:** *sip.telnyx.com*
   9. **Backup Proxy Server Address:** *sip.telnyx.com*
   10. **Backup Proxy Server Port:** If you are using UDP transport, use port *5060*. If you are using TLS transport, use port *5061.*
   11. **Activate:** Check this box to activate
3. Click **Apply**.
4. Refresh the page to ensure that your new SIP account shows as registered.

That's it! You've finished configuring your Fanvil X4G profile, and can now start testing calls!

[Back to Top](#h_7fb71be8d0)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [Fanvil FAQ](https://www.fanvil.com/Support/index.html)
* [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html)
* [Fanvil support](https://www.fanvil.com/Support/ticket.html)
* [Fanvil X4 series firmware](https://www.fanvil.com/Support/download/id/72.html)

---

Related Articles

[Fanvil A32i: Telnyx Setup](https://support.telnyx.com/en/articles/6056428-fanvil-a32i-telnyx-setup)[Fanvil H3: Hotel IP](https://support.telnyx.com/en/articles/6202965-fanvil-h3-hotel-ip)[Fanvil X1/X1P: IP Phone](https://support.telnyx.com/en/articles/6206533-fanvil-x1-x1p-ip-phone)[Fanvil X2CP/X2C/X2P: Call Center IP](https://support.telnyx.com/en/articles/6206756-fanvil-x2cp-x2c-x2p-call-center-ip)[Fanvil X-Series: IP Phone](https://support.telnyx.com/en/articles/6209971-fanvil-x-series-ip-phone)

Did this answer your question?

😞😐😃
