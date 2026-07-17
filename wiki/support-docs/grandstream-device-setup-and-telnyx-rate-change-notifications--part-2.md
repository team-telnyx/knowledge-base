---
title: Grandstream Device Setup and Telnyx Rate Change Notifications
summary: This page consolidates Telnyx setup guides for several Grandstream devices
  (DP752, GRP260x, GRP2612, GXP1700, and GXV3370) along with information about how
  Telnyx notifies customers of rate changes and upcoming updates to the Global Conversational
  rate deck. Each device section walks through prerequisites, SIP trunk configuration,
  codec settings, and account setup, while the rate change sections explain notification
  timelines, origination type classifications, and pricing update frequency.
sources:
- url: https://support.telnyx.com/en/articles/1130658-how-do-i-know-if-a-rate-has-changed
- url: https://support.telnyx.com/en/articles/5808368-grandstream-dp752
- url: https://support.telnyx.com/en/articles/6169513-grandstream-grp260x-sip-trunk
- url: https://support.telnyx.com/en/articles/6184147-grandstream-grp2612-sip-trunk
- url: https://support.telnyx.com/en/articles/6184520-grandstream-gxp1700-sip-trunk
- url: https://support.telnyx.com/en/articles/6187576-grandstream-gxv3370
- url: https://support.telnyx.com/en/articles/6974437-updates-to-global-conversational-rate-deck
updated_at: 2026-07-17T09:05:40Z
---

# Grandstream Device Setup and Telnyx Rate Change Notifications

*Part 2 of 6 — see also: [Part 1](grandstream-device-setup-and-telnyx-rate-change-notifications--part-1.md), [Part 3](grandstream-device-setup-and-telnyx-rate-change-notifications--part-3.md), [Part 4](grandstream-device-setup-and-telnyx-rate-change-notifications--part-4.md), [Part 5](grandstream-device-setup-and-telnyx-rate-change-notifications--part-5.md), [Part 6](grandstream-device-setup-and-telnyx-rate-change-notifications--part-6.md)*

This page consolidates Telnyx setup guides for several Grandstream devices (DP752, GRP260x, GRP2612, GXP1700, and GXV3370) along with information about how Telnyx notifies customers of rate changes and upcoming updates to the Global Conversational rate deck. Each device section walks through prerequisites, SIP trunk configuration, codec settings, and account setup, while the rate change sections explain notification timelines, origination type classifications, and pricing update frequency.

## Grandstream GRP260x

Part of the GRP series of Carrier-Grade IP Phones, the [Grandstream GRP260x](https://content.grandstream.com/grp260x-introduction-webinar) is an essential 2-line model designed with zero-touch provisioning for mass deployment and easy management. It features 5-way voice conferencing, dual band Wi-Fi support (GRP2602W only), EHS support for Plantronics, Jabra & Sennheiser headsets, and multi-language support. The GRP series includes carrier-grade security features such as secure boot, dual firmware images, and encrypted data storage. For cloud provisioning and centralized management, the GRP260x is supported by [Grandstream's Device Management System (GDMS)](https://www.grandstream.com/products/device-management/gdms/product/gdms).

*Note:* This guide covers the GRP260x series. For information about the GRP261x, GRP262x & GRP263x series, see the [Grandstream GRP2612](grandstream-grp2612.md) guide.

Additional resources:

- [GRP260x Series – Administration Guide](https://documentation.grandstream.com/knowledge-base/grp260x-series-administration-guide/)
- [GRP26xx – Firmware Upgrade Guide](https://documentation.grandstream.com/knowledge-base/grp26xx-firmware-upgrade-guide/)
- [GRP Series – Display Language Guide](https://documentation.grandstream.com/knowledge-base/grp-series-display-language-guide/)
- [GRP2601/P – Quick Installation Guide](https://documentation.grandstream.com/knowledge-base/grp2601-p-quick-installation-guide/)
- [GRP2602/P/W – Quick Installation Guide](https://documentation.grandstream.com/knowledge-base/grp2602-p-w-quick-installation-guide/)
- [GRP2603/P – Quick Installation Guide](https://documentation.grandstream.com/knowledge-base/grp2603-p-quick-installation-guide/)
- [GRP2604/P – Quick Installation Guide](https://documentation.grandstream.com/knowledge-base/grp2604-p-quick-installation-guide/)
- [Grandstream FAQ](https://blog.grandstream.com/faq)
- [Grandstream user forum](https://forums.grandstream.com/)
- [Helpdesk](https://helpdesk.grandstream.com/)

### Configuring a Telnyx SIP trunk on the GRP260x

**Pre-Requisites**

- Ensure that your [Telnyx Mission Command Portal](get-started-with-a-mission-control-account.md) is configured properly
- [Purchase a DID](https://portal.telnyx.com/#/app/numbers/search-numbers)
- [Set up your Telnyx SIP connection](https://portal.telnyx.com/#/app/connections)
- [Provision your number](https://portal.telnyx.com/#/app/numbers/my-numbers) (Assign it to a SIP connection)
- [Create an outbound voice profile](https://portal.telnyx.com/#/app/outbound)
- Create a [credentials-based connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal
- RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
- Ensure your phone is on the [most current firmware](https://documentation.grandstream.com/knowledge-base/grp26xx-firmware-upgrade-guide/)
- Connect your device to an ethernet port to establish an internet connection
- Use your phone's base or handset to find the device IP address. See the [Grandstream GRP 260x Series admin guide](https://documentation.grandstream.com/knowledge-base/grp260x-series-administration-guide/#configuration-via-web-browser) to find your phone's IP address and obtain the default portal login credentials. You can also [establish a SIP trunk directly from your phone's keypad](https://documentation.grandstream.com/knowledge-base/grp260x-series-administration-guide/#configuration-via-keypad).

The Grandstream GRP 260x web portal has 9 configuration sections. The ones that concern your Telnyx SIP trunk integration are **Status** and **Account**.

*Note:* The following settings are required to establish a SIP trunk with your Telnyx service. A full list of settings is available [here](https://documentation.grandstream.com/knowledge-base/grp260x-series-administration-guide/#configuration-guide).

1. [Log into the Grandstream web portal](https://documentation.grandstream.com/knowledge-base/grp260x-series-administration-guide/#configuration-via-web-browser).
2. Navigate to the **Account** settings screen and configure the following:

   **General Settings > Account Register:**
   - **Account Active:** Set as *Yes* if you plan to activate your new trunk as soon as it's set up.
   - **Account Name:** Choose a name for your account. It will display in the phone's LCD screen.
   - **SIP Server:** `sip.telnyx.com` (For US users. International users see [this table](https://sip.telnyx.com/#signaling-addresses).)
   - **Secondary SIP Server:** `64.16.250.10` (For US users. International users see [this table](https://sip.telnyx.com/#signaling-addresses).)
   - **SIP User ID:** The SIP connection username. See the Credentials Connection Setup section in [SIP Connection Types](https://support.telnyx.com/en/articles/4245868-sip-connection-types).
   - **SIP Auth ID:** The SIP connection username.
   - **SIP Auth Password:** The SIP connection password.
   - **Name:** Your caller ID. Keep in mind:
     - Caller ID Name should be in capital letters for clearer display on some devices.
     - Do not use special characters; spaces are allowed.
     - Some Canadian providers will not show more than 15 characters.
   - **Fallback Expiration:** Specifies the duration (in minutes) since failover to the current SIP server or Outbound Proxy before making failback attempts to the primary SIP server or Outbound Proxy.

   **General Settings > Network Settings:**
   - **Outbound Proxy:** `sip.telnyx.com`
   - **Max number of SIP request replies:** Sets the maximum number of retries for the device to send requests to the server. Valid range: 1-10.

   **SIP Settings > Basic Settings:**
   - **SIP registration:** Leave enabled if you want your phone to send SIP Register messages to the proxy/server.
   - **SIP transport:** The network protocol used for SIP transport. Default is *UDP*. If you plan to encrypt traffic, choose *TLS/TCP*, provided you've [configured your Telnyx portal to encrypt data](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication).
   - **SIP listening mode:** Options include:
     - *Dual:* If you've selected UDP, phone will also listen for TCP.
     - *Dual (Secured):* If you're transporting over UDP, phone will also listen for TLS/TCP. If TLS/TCP is selected, phone will also listen for UDP.
     - *Dual (BLF Enforced)*
     - *Transport* Only (Default)
   - **Local SIP port:** UDP will use `5060`, TLS/TCP will use `5061`.
3. Navigate to the Status page where you can check all your account details.
