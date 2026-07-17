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

*Part 4 of 6 — see also: [Part 1](grandstream-device-setup-and-telnyx-rate-change-notifications--part-1.md), [Part 2](grandstream-device-setup-and-telnyx-rate-change-notifications--part-2.md), [Part 3](grandstream-device-setup-and-telnyx-rate-change-notifications--part-3.md), [Part 5](grandstream-device-setup-and-telnyx-rate-change-notifications--part-5.md), [Part 6](grandstream-device-setup-and-telnyx-rate-change-notifications--part-6.md)*

This page consolidates Telnyx setup guides for several Grandstream devices (DP752, GRP260x, GRP2612, GXP1700, and GXV3370) along with information about how Telnyx notifies customers of rate changes and upcoming updates to the Global Conversational rate deck. Each device section walks through prerequisites, SIP trunk configuration, codec settings, and account setup, while the rate change sections explain notification timelines, origination type classifications, and pricing update frequency.

## Grandstream GXP1700

The [Grandstream GXP1760W](https://www.grandstream.com/products/ip-voice-telephony-gxp-series-ip-phones/gxp-series-mid-range-ip-phones/product/gxp1760w) is a mid-range IP phone with integrated dual-band Wi-Fi (GXP1760W only), a sleek design and moderate call-volume features. It comes equipped with 6 lines, 3 SIP accounts, 6 dual-color line keys and 4 XML programmable context sensitive soft keys on a 200 x 80 pixel (3.3") back-lit LCD display screen. The GXP1760W features personalized ring tone/ring back tone music and integration with advanced web and enterprise applications, dual auto-sensing 10/100Mbps network ports, and automated provisioning features with media access control.

The [Grandstream GXP1780/1782](https://www.grandstream.com/products/ip-voice-telephony-gxp-series-ip-phones/gxp-series-mid-range-ip-phones/product/gxp1780) is a powerful mid-range IP phone with advanced telephony features. It comes equipped with 8 lines, 4 SIP accounts, 8 dual-color line keys and 4 XML programmable context sensitive soft keys on a 200 x 80 pixel (3.3") back-lit LCD display screen. The GXP1780/1782 features personalized ring tone/ring back tone music, integration with advanced web and enterprise applications, and a Kensington Security Slot. The GXP1780/1782 supports dual auto-sensing Gigabit network ports (on GXP1782 only) and automated provisioning features with media access control.

Additional resources:

- [GXP1700 series user Guide](https://documentation.grandstream.com/knowledge-base/gxp17xx-series-user-guide/)
- [GS Affinity user guide](https://documentation.grandstream.com/knowledge-base/gs-affinity-user-guide/)
- [Administration Guide](https://documentation.grandstream.com/knowledge-base/gxp17xx-series-administration-guide/)
- [Firmware Upgrade Guide](https://documentation.grandstream.com/knowledge-base/firmware-upgrade-guide/)
- [Display Language Guide](https://documentation.grandstream.com/knowledge-base/grp-series-display-language-guide/)
- [GXP1760W – Quick Installation Guide](https://documentation.grandstream.com/knowledge-base/gxp1760w-quick-installation-guide/)
- [GXP1780/1782 – Quick Installation Guide](https://documentation.grandstream.com/knowledge-base/gxp1780-1782-quick-installation-guide/)
- [Additional GXP1700 series documentation](https://documentation.grandstream.com/article-categories/gxp17xx/)
- [Grandstream FAQ](https://blog.grandstream.com/faq)
- [Grandstream user forum](https://forums.grandstream.com/)
- [Helpdesk](https://helpdesk.grandstream.com/)

### Configuring a Telnyx SIP trunk on the GXP1700

In this activity you will:

1. Configure a Telnyx SIP trunk on your device
2. Configure audio settings

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
- Use your phone's base or handset to find the device IP address. See the [Grandstream GXP1700 Series admin guide](https://documentation.grandstream.com/knowledge-base/gxp17xx-series-administration-guide/#configuration-via-web-browser) to find your phone's IP address and obtain the default portal login credentials. You can also [establish a SIP trunk directly from your phone's keypad](https://documentation.grandstream.com/knowledge-base/gxp17xx-series-administration-guide/#configuration-via-keypad).

The Grandstream GXP1700 web portal has 9 configuration sections. The ones that concern your Telnyx SIP trunk integration are **Status**, **Account**, and **Settings**.

*Note:* The following settings are required to establish a SIP trunk with your Telnyx service. A full list of settings is available [here](https://documentation.grandstream.com/knowledge-base/gxp17xx-series-administration-guide/#configuration-guide).

#### Configure the SIP trunk

1. [Log into the Grandstream web portal](https://documentation.grandstream.com/knowledge-base/gxp17xx-series-administration-guide/#configuration-via-web-browser).
2. Navigate to the **Account** screen.
3. In **Account > General Settings**:
   - **Account Active:** Set as *Yes* if you plan to activate your new trunk as soon as it's set up.
   - **Account Name:** Choose a name for your account. It will display in the phone's LCD screen.
   - **SIP Server:** `sip.telnyx.com` (For US users. International users see [this table](https://sip.telnyx.com/#signaling-addresses).)
   - **Secondary SIP Server:** `64.16.250.10` (For US users. International users see [this table](https://sip.telnyx.com/#signaling-addresses).)
   - **Outbound Proxy:** `sip.telnyx.com`
   - **SIP User ID:** The SIP connection username. See the Credentials Connection Setup section in [SIP Connection Types](https://support.telnyx.com/en/articles/4245868-sip-connection-types).
   - **Authenticate ID:** The SIP connection username.
   - **Authenticate Password:** The SIP connection password.
   - **Name:** Your caller ID. Keep in mind:
     - Caller ID Name should be in capital letters for clearer display on some devices.
     - Do not use special characters; spaces are allowed.
     - Some Canadian providers will not show more than 15 characters.
   - **Rule:** Your rule settings (number, pattern, prefix to add, etc.).
   - **Type:** Choose the type of the rule (*pattern*, *block*, *dial now*, *prefix* or *second tone*).
   - **Fallback Expiration:** Specifies the duration (in minutes) since failover to the current SIP server or Outbound Proxy before making failback attempts to the primary SIP server or Outbound Proxy.
4. In **Account > Network Settings**:
   - **DNS Mode:** Controls how the device looks up IP addresses for hostnames. Four modes: *A Record* (default), *SRV*, *NATPTR/SRV*, *Use Configured IP*.
     - To locate the server by DNS SRV, select *SRV* or *NATPTR/SRV*.
     - If *Use Configured IP* is selected, fill in **Primary IP**, **Backup IP 1**, and **Backup IP 2**.
     - If SIP server is configured as a domain name, the phone will not send DNS query, but will select *Primary IP* or *Backup IP x* to send SIP message if at least one is not empty.
     - The phone will try to use Primary IP first. After 3 tries without any response, it will switch to Backup IP x, and then switch back to Primary IP after 3 re-tries.
     - If SIP server is already an IP address, the phone will use it directly even if *User Configured IP* is selected.
5. In **Account > SIP Settings > Basic Settings**:
   - **SIP registration:** Leave enabled if you want your phone to send SIP Register messages to the proxy/server.
   - **Local SIP port:** UDP will use `5060`, TLS/TCP will use `5061`.
   - **SIP transport:** The network protocol used for SIP transport. Default is *UDP*. If you plan to encrypt traffic, choose *TLS/TCP*, provided you've [configured your Telnyx portal to encrypt data](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication).
   - **SIP listening mode:** Options include:
     - *Dual:* If you've selected UDP, phone will also listen for TCP.
     - *Dual (Secured):* If you're transporting over UDP, phone will also listen for TLS/TCP. If TLS/TCP is selected, phone will also listen for UDP.
     - *Dual (BLF Enforced)*
     - *Transport* Only (Default)

#### Configure audio settings

1. In **Account > Audio Settings**:
   - **Preferred Vocoder:** Telnyx supports the following codecs:
     - `ulaw(g711u)`
     - `alaw(g711a)`
     - `g722`
     - `g729`

     *Note:* Using firmware version 1.0.0.43 or higher, users are now able to perform concurrent calls using G.729 codec as well.
2. Navigate to the **Settings** screen.
3. In **Settings > General Settings**:
   - **STUN Server:** `stun.telnyx.com:3478`
4. Navigate to the Status page where you can check all your account details.
