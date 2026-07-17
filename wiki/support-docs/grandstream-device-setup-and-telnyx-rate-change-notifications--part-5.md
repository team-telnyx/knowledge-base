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

*Part 5 of 6 — see also: [Part 1](grandstream-device-setup-and-telnyx-rate-change-notifications--part-1.md), [Part 2](grandstream-device-setup-and-telnyx-rate-change-notifications--part-2.md), [Part 3](grandstream-device-setup-and-telnyx-rate-change-notifications--part-3.md), [Part 4](grandstream-device-setup-and-telnyx-rate-change-notifications--part-4.md), [Part 6](grandstream-device-setup-and-telnyx-rate-change-notifications--part-6.md)*

This page consolidates Telnyx setup guides for several Grandstream devices (DP752, GRP260x, GRP2612, GXP1700, and GXV3370) along with information about how Telnyx notifies customers of rate changes and upcoming updates to the Global Conversational rate deck. Each device section walks through prerequisites, SIP trunk configuration, codec settings, and account setup, while the rate change sections explain notification timelines, origination type classifications, and pricing update frequency.

## Grandstream GXV3370

The [GXV3370 IP Video Phone](https://www.grandstream.com/products/ip-video-telephony/ip-video-phones-android/product/gxv3370) for Android combines a 16-line IP video phone with a multi-platform video conferencing solution, all with the functionality of an Android tablet, to offer an all-in-one communications solution.

The GXV3370, which runs on the Android platform, features a 7" 1024×600 capacitive touch screen TFT LCD, camera, dual gigabit ports with PoE/PoE+, HD audio and video, integrated Wi-Fi (802.11a/b/g/n) and Bluetooth, and rich peripheral interfaces. It combines a state-of-the-art IP video phone, an advanced video conferencing solution, and the functionality of a tablet.

Additional resources:

- [User manual](https://documentation.grandstream.com/knowledge-base/gxv3370-user-guide/)
- [GS Affinity user manual](https://documentation.grandstream.com/knowledge-base/gs-affinity-user-guide/)
- [Admin manual](https://documentation.grandstream.com/knowledge-base/gxv3370-administration-guide/)
- [Firmware upgrade guide](https://documentation.grandstream.com/knowledge-base/firmware-upgrade-guide/)
- [All other GXV3370 reference material](https://documentation.grandstream.com/article-categories/gxv3370/)
- [Grandstream FAQ](https://blog.grandstream.com/faq)
- [Grandstream user forum](https://forums.grandstream.com/)
- [Helpdesk](https://helpdesk.grandstream.com/)

### Configuring a Telnyx SIP trunk on the GXV3370

In this activity you will:

1. Configure a Telnyx SIP trunk on your device
2. Configure codecs

**Pre-Requisites**

- Ensure that your [Telnyx Mission Command Portal](get-started-with-a-mission-control-account.md) is configured properly
- [Purchase a DID](https://portal.telnyx.com/#/app/numbers/search-numbers)
- [Set up your Telnyx SIP connection](https://portal.telnyx.com/#/app/connections)
- [Provision your number](https://portal.telnyx.com/#/app/numbers/my-numbers) (Assign it to a SIP connection)
- [Create an outbound voice profile](https://portal.telnyx.com/#/app/outbound)
- Create a [credentials-based connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal
- RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
- [Ensure your device is on the latest firmware](https://documentation.grandstream.com/knowledge-base/firmware-upgrade-guide/)
- Use your phone's base or handset to find the device IP address. See the [Provisioning section of the Admin Guide](https://documentation.grandstream.com/knowledge-base/gxv3370-administration-guide/#upgrade-and-provisioning-configuration) to find your phone's IP address and obtain the default portal login credentials.

*Note:* The following settings are required to establish a SIP trunk with your Telnyx service. A full list of settings is available [here](https://documentation.grandstream.com/knowledge-base/gxv3370-administration-guide/).

#### Configure the SIP trunk

1. [Log into the Web GUI](https://documentation.grandstream.com/knowledge-base/gxv3370-administration-guide/#upgrade-and-provisioning-configuration).
2. Navigate to the **Account** screen and go to **General Settings**. In the **On Register** section, provide the following:
   - **Account Active:** This switch determines if the account will become active once created. The default value for the first account is *Yes*.
   - **Account Name:** Give your account a name that makes sense for your connection (e.g., `TelnyxTrunk`).
   - **SIP Server:** `sip.telnyx.com` (for USA. For all other countries, see [this table](https://sip.telnyx.com/#signaling-addresses))
   - **SIP User ID:** Your SIP account/sub-account ID
   - **SIP Authentication ID:** The SIP connection username. See the Credentials Connection Setup section in [SIP Connection Types](https://support.telnyx.com/en/articles/4245868-sip-connection-types).
   - **SIP Password:** The SIP connection password.
   - **Display Name:** Your caller ID. Keep in mind:
     - Caller ID Name should be in capital letters for clearer display on some devices.
     - Do not use special characters; spaces are allowed.
     - Some Canadian providers will not show more than 15 characters.
   - **VoiceMail Access Number:** Configure the voicemail user ID to retrieve voicemail by pressing Listen on the message screen. This user ID is usually the VM portal access number (e.g., `*97`).
   - **Outbound Proxy:** `sip.telnyx.com`
3. Still on the **Account** screen, go to **SIP Settings**. In the **SIP Basic Settings** section, provide the following:
   - **SIP registration:** Leave enabled if you want your phone to send SIP Register messages to the proxy/server.
   - **SIP transport:** The network protocol used for SIP transport. Default is *UDP*. If you plan to encrypt traffic, choose *TLS/TCP*, provided you've [configured your Telnyx portal to encrypt data](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication).
   - **Local SIP port:** UDP will use `5060`, TLS/TCP will use `5061`.

#### Configure codecs

1. Still on the **Account** screen, go to **Codec Settings**. In the **Preferred Vocoder** section, provide the following:
   - **Preferred Vocoder:** Select the codecs to be used on WiFi, 2, 3, and 4G. Telnyx supports the following audio codecs:
     - `ulaw(g711u)`
     - `alaw(g711a)`
     - `g722`
     - `g729`
   - **DTMF:** `RFC2833`
2. In the **Preferred Video Codec** section, provide the following:
   - **Preferred Video Codec:** `H264`

## Rate Change Notifications

Whenever a rate has changed with Telnyx, a brief rate update email is sent to all customers. There is no need to worry about missing changes—Telnyx keeps customers updated automatically.

### How rate change notifications work

Telnyx sends an email to all customers any time its rates change. Customers on either the Global Conversational rate deck or default pricing will be notified of future changes via an email to the address associated with their Mission Control Portal account. Each notification is sent **3 days before** the change is live in the rate decks.

*Note:* If your Telnyx account has no outbound usage in the 30 days prior to the change, you will not be notified about updates to the rate deck.
