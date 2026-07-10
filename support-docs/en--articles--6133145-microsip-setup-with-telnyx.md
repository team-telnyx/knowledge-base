---
source_url: https://support.telnyx.com/en/articles/6133145-microsip-setup-with-telnyx
scraped: 2026-07-08
content_hash: 74eaa640d53924397476309c86ea9d65e8d2100d1a8b4295015c283ddeb35b6a
---

MicroSIP: Setup with Telnyx | Telnyx Help Center

[Skip to main content](#main-content)

# MicroSIP: Setup with Telnyx

Learn how to set up and configure a MicroSIP softphone and set Telnyx as your SIP provider.

C

Written by Customer Success

June 6, 2024

Table of contents

[Jump to Instructions](#h_b0615de50d)

[MicroSIP](https://www.microsip.org) is an open source portable SIP softphone based on the PJSIP stack.

|  |
| --- |
| ***Note:*** *MicroSIP is only available for the Windows platform.* |

[MicroSIP](https://support.telnyx.com/en/articles/6133145-microsip-setup-with-telnyx) supports high quality VoIP calls (person-to-person or on regular phones) and offers free person-to-person calls, as well as very affordable international calls.

MicroSIP's standout features include:

* Small footprint (>2.5MB) and RAM usage (>5MB) - written in C and C++ with minimal possible system resources usage
* User-friendly, ideal for daily use
* Functionality - voice; video H.264 and H.263+, VP8; SIMPLE messaging (RFC 3428) and presence (RFC 3903, 6665); [DTMF](https://support.telnyx.com/en/articles/1130710-what-is-dtmf) In-band, RCF2833, SIP-INFO.
* Compatibility - conform to SIP standards
* Voice quality and vast codec support
* WebRTC echo cancellation algorithm and voice activity detection
* Allows for transport privacy: supports TLS / SRTP for control and media
* Portability - has no additional dependencies and stores setting in ini file
* [Multi-language and RTL support/localization](https://www.microsip.org/translation)
* Designed with accessibility in mind, allowing for use of screen reader software such as NVDA

**Additional Resources:**

Downloads and source code:

* [Download MicroSIP](https://www.microsip.org/downloads/current)
* [MicroSIP custom build: Personalize your MicroSIP!](https://www.microsip.org/custom)
* [MicroSIP source code](https://www.microsip.org/source)

FAQ and help

* [MicroSIP FAQ](https://www.microsip.org/faq)
* [MicroSIP troubleshooting](https://www.microsip.org/issues)
* [MicroSIP help documentation](https://www.microsip.org/help)
* [Feature/change requests](https://www.microsip.org/wishes)
* [Supported languages/localization](https://www.microsip.org/translation)
* [Contact MicroSIP](https://www.microsip.org/contact)

---

# Instructions for setting up and configuring the MicroSIP softphone with Telnyx as provider

In this activity you will:

1. [Add Telnyx as your SIP provider and create a trunk](#h_696f55ea48)
2. [(Optional) encrypt your calls](#h_195e5042da)
3. [Configure audio settings](#h_a1e1f71848)

**Pre-requisites**

* Your Telnyx Portal must be correctly [set up and configured for use](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* Have your SIP Credentials (The username/password for your main SIP account or SIP sub-account)
* Have [DID(s) available](https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers) to assign
* A PC running a Windows OS
* [Download](https://www.microsip.org/downloads/current) and install MicroSIP

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

## 1 Add Telnyx as your SIP provider and create a trunk

In this section, you'll configure your first [SIP trunk](https://telnyx.com/products/sip-trunks) on your MicroSIP softphone.

1. Run the MicroSIP application. On the home screen, click on the arrow at the top-right of the screen.
2. Click **Edit Account** to open the account screen.
3. Provide the following information:

   1. **Account Name:** This value is your choice
   2. **SIP Server:** *sip.telnyx.com*
   3. **SIP Proxy:** *sip.telnyx.com*
   4. **Username:** Your main Telnyx account or sub-account
   5. **Domain:** *sip.telnyx.com*
   6. **Login:** Your main Telnyx account or sub-account username
   7. **Password:** Your main Telnyx account or sub-account password
   8. **Display Name:** This will become your caller ID. Note the following caller ID naming conventions:

      1. Caller ID Name should be in capital letters. This will appears more clearly/visible on some devices.
      2. You must NOT use any special characters, as they will not be displayed. Spaces are allowed.
      3. Some of regular Canadian providers will not show more than 15 characters. We suggest shrinking or adapt your caller ID.
   9. **Media Encryption:** If you are using UDP or TCP transport, leave as *Disabled*. If you are using TLS encryption, select *Mandatory SRTP (RTP/SAVP)*
   10. **Transport:** Select the mode of transport you're using. Either *Auto (UDP/TCP)* or *TLS*.

   ![Homescreen of the MicroSIP application.](_images/65b6b33301e57c85.png)

[Back to Top](#h_b0615de50d)

## 2. (Optional) Encrypt your calls

In this section, you'll finish setting up call encryption. This isn't required unless you chose TLS as your transport protocol.

|  |
| --- |
| ***Note:*** *If you plan to encrypt your calls, make sure your media encryption and transport settings are configured correctly in steps 3i and 3j of [section 1](#h_696f55ea48).* |

1. Navigate to **MicroSIP > Settings** to open the settings configuration.
2. Make the following changes:

   1. **Source Port:** *5061*
   2. **RTP Ports:** Set this range between *10001 - 20000*

      ![MicroSIP Settings section. ](_images/0babb2ac103185af.png)
3. Click **Save**.

[Back to Top](#h_b0615de50d)

## 3. Configure Audio Settings

In this section, you'll configure your codecs and eliminate echo during calls in order to optimize your audio experience.

1. Navigate to **MicroSIP > Settings** to open the settings configuration.
2. Find the available and enabled codecs and choose any Telnyx-supported codecs you want to use. Telnyx supports the following [audio codecs](https://telnyx.com/resources/codecs-affect-voip-sound-quality):

   * ulaw(g711u)
   * alaw(g711a)
   * g722
   * g729
3. Find the **EC** checkbox and check this. This facilitates echo cancellation.

   ![MicroSIP Settings section.](_images/f86ea7f59e711edb.png)

That's it! You've finished configuring your MicroSIP softphone, and can now start testing calls!  
​

[Back to Top](#h_b0615de50d)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* Downloads and source code:

  + [Download MicroSIP](https://www.microsip.org/downloads/current)
  + [MicroSIP custom build: Personalize your MicroSIP!](https://www.microsip.org/custom)
  + [MicroSIP source code](https://www.microsip.org/source)

  FAQ and help

  + [MicroSIP FAQ](https://www.microsip.org/faq)
  + [MicroSIP troubleshooting](https://www.microsip.org/issues)
  + [MicroSIP help documentation](https://www.microsip.org/help)
  + [Feature/change requests](https://www.microsip.org/wishes)
  + [Supported languages/localization](https://www.microsip.org/translation)
  + [Contact MicroSIP](https://www.microsip.org/contact)

---

Related Articles

[Algo 8xxx: Telnyx Endpoints](https://support.telnyx.com/en/articles/5790092-algo-8xxx-telnyx-endpoints)[Gigaset A510: Telnyx Setup](https://support.telnyx.com/en/articles/5815209-gigaset-a510-telnyx-setup)[Snom C520: Telnyx Setup](https://support.telnyx.com/en/articles/5815678-snom-c520-telnyx-setup)[Vtech VCS754: Telnyx Setup](https://support.telnyx.com/en/articles/5822901-vtech-vcs754-telnyx-setup)[Fanvil A32i: Telnyx Setup](https://support.telnyx.com/en/articles/6056428-fanvil-a32i-telnyx-setup)

Did this answer your question?

😞😐😃

Table of contents
