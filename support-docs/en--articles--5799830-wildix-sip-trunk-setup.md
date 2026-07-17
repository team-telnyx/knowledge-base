---
source_url: https://support.telnyx.com/en/articles/5799830-wildix-sip-trunk-setup
title: "Wildix: SIP Trunk Setup"
description: "Learn how to set up and configure a SIP trunk between Wildix and… See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: ad7004f7a8714b3d4f105724588b45c256da6e72c6a17a84e779314233b577df
---







# Wildix: SIP Trunk Setup

Learn how to set up and configure a SIP trunk between Wildix and… See Telnyx guidance and requirements.

C




[Jump to Instructions](#h_d9c3c4e6b9)

[Wildix](https://www.wildix.com/) created their VoIP PBX system in 2005. Intuitive and easy to use, Wildix provides a browser-based WebRTC that is fully cross-OS compatible and doesn't require you to install any software to use. Wildix creates and develops software based IP-telephony applications for business communications that bring together presence information, audio and video calls, Instant Messaging, conferences, online chat, fax and SMS sending, and desktop sharing.

Additional documentation:

* [Wildix licensing](https://www.wildix.com/product/licensing/)
* [Book a Wildix demo](https://www.wildix.com/try/)
* [Wildix technical documentation](https://wildix.atlassian.net/wiki/spaces)
* [Wildix custom config parameters](https://wildix.atlassian.net/wiki/spaces/DOC/pages/30285078/Custom+config+parameters+List)

---

## Instructions for establishing a [SIP trunk](https://telnyx.com/products/sip-trunks) between Wildix and Telnyx

In this activity you will:

1. [Configure your basic SIP trunk settings](#h_f1bcdc1ae8)
2. [Configure your advanced SIP trunk settings](#h_6ef52cb060)

**Pre-requisites:**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* [Provision a DID from Telnyx](https://portal.telnyx.com/#/app/numbers/search-numbers) ([How do I do this?](https://support.telnyx.com/en/articles/3562148-requesting-numbers))

**Video walkthrough**

Setting up your Telnyx Mission Control Panel so you can make/receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Wildix/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Configure your basic SIP trunk settings

In this activity, you will log into your Wildix portal and configure a SIP trunk to work with Telnyx.

1. Log into your Wildix UI and select **WMS > Trunks > Trunks**.
2. Click on the **+** button located under the SIP table to open a new trunk settings window and enter the following in the Basic Settings tab:

   1. **Pricelist:**
   2. **Title:** *Telnyx SIP trunk* (or something similar - describes your trunk)
   3. **Trunk name:** Give your trunk a name that makes sense for you
   4. **Auth login:** YourTelnyx SIP username
   5. **From user:** Your Telnyx SIP username
   6. **From domain:** Forced from domain header and used in register and invite SIP messages
   7. **Address or host name:** *sip.telnyx.com*
   8. **Password:** Your Telnyx SIP password
   9. **Dialplan:** Dialplan procedure for routing calls coming from this trunk (typically *main*)
   10. **Tone Zone:** Your country/region
   11. **Country Code:** Used for number normalization, enter the country in which the trunk is being used.
   12. **Keep-Alive:** If checked, this enables periodic sending of keep alive messages to the trunk.
   13. **Enable Registration:** Enable outgoing registration (in case of PBXs SIP interconnection, it is enabled on the Client PBX SIP trunk and disabled on Server)
   14. **Registration Proxy:** This field, and the subsequent fields that follow, appear only after checking off **Enable registration**. The Registration Proxy field is optional, but if you check this box, make sure that:

       1. **Address or Host Name:** *sip.telnyx.com*
       2. **Auth Login:** Your Telnyx SIP username
       3. **Password:** Your Telnyx SIP password
       4. **From user:** Your Telnyx SIP username

   ![Wildix portal section. ](_images/5bc41697aa60be62.png)

[Back to Top](#h_d9c3c4e6b9)

## 2. Configure your advanced SIP trunk settings

In this step, you'll go on to configure your advanced SIP trunk settings before saving your new SIP trunk. Even though your trunk is ready for registration, there are some settings that we suggest modifying to make everything run a bit more smoothly.

1. From the new SIP trunk window, expand the **Advanced** section and provide the following:

   1. **Audio codecs:** Choose from Telnyx-supported [audio codecs](https://telnyx.com/resources/codecs-affect-voip-sound-quality), namely:

      1. ulaw(g711u)
      2. alaw(g711a)
      3. g722
      4. g729
   2. **Video codecs:** Telnyx supports H264, so you can select this option if you plan to use video.
   3. **T38:** *Yes (*special parameters for T38 support and the maxdatagram)
   4. **Session timer:** Check this box and set a range, for example *min: 90, max: 600*
   5. **Registration expiry (sec):** *180*
   6. **UDP/TCP/TLS:** *UDP*
   7. **[DTMF](https://support.telnyx.com/en/articles/1130710-what-is-dtmf) mode:** *RFC2833*

That's it! You're now ready to start communicating using Wildix.

[Back to Top](#h_d9c3c4e6b9)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally, check out:

* [Wildix licensing](https://www.wildix.com/product/licensing/)
* [Book a Wildix demo](https://www.wildix.com/try/)
* [Wildix technical documentation](https://wildix.atlassian.net/wiki/spaces)
* [Wildix custom config parameters](https://wildix.atlassian.net/wiki/spaces/DOC/pages/30285078/Custom+config+parameters+List)

---

Related Articles

[Configuring a Cisco CUBE/CUCM SIP Trunk](https://support.telnyx.com/en/articles/1130673-configuring-a-cisco-cube-cucm-sip-trunk)[Grandstream UCM6xxx: SIP Trunks](https://support.telnyx.com/en/articles/5748258-grandstream-ucm6xxx-sip-trunks)[Xorcom PBX: SIP Trunk](https://support.telnyx.com/en/articles/5754127-xorcom-pbx-sip-trunk)[PhoneSuite Voiceware](https://support.telnyx.com/en/articles/5800936-phonesuite-voiceware)[Fanvil A32i: Telnyx Setup](https://support.telnyx.com/en/articles/6056428-fanvil-a32i-telnyx-setup)

Did this answer your question?

😞😐😃
