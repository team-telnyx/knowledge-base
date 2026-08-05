---
title: Telnyx Hardware Compatibility and Device Setup
summary: Telnyx is a cloud-based communications platform that does not sell hardware
  but is compatible with virtually any SIP-enabled device. This page consolidates
  guidance on recommended hardware configurations and step-by-step setup instructions
  for a range of supported devices, including IP phones, conference phones, ATAs,
  SBCs, and PBX systems.
sources:
- url: https://support.telnyx.com/en/articles/1130638-does-telnyx-provide-any-hardware
- url: https://support.telnyx.com/en/articles/1130641-telnyx-recommended-hardware-configurations
- url: https://support.telnyx.com/en/articles/4194841-audiocodes-sbc-setup
- url: https://support.telnyx.com/en/articles/5619617-polycom-setup-with-telnyx
- url: https://support.telnyx.com/en/articles/5800936-phonesuite-voiceware
- url: https://support.telnyx.com/en/articles/5815678-snom-c520-telnyx-setup
- url: https://support.telnyx.com/en/articles/5819923-audiocodes-400hd
- url: https://support.telnyx.com/en/articles/5820183-plantronics-polycom-obi300-setup
- url: https://support.telnyx.com/en/articles/5820309-cisco-68xx-88xx-setup
- url: https://support.telnyx.com/en/articles/5822706-snom-d7xx-telnyx-setup
updated_at: 2026-08-05T13:29:19Z
---

# Telnyx Hardware Compatibility and Device Setup

*Part 3 of 3 — see also: [Part 1](telnyx-hardware-compatibility-and-device-setup--part-1.md), [Part 2](telnyx-hardware-compatibility-and-device-setup--part-2.md)*

Telnyx is a cloud-based communications platform that does not sell hardware but is compatible with virtually any SIP-enabled device. This page consolidates guidance on recommended hardware configurations and step-by-step setup instructions for a range of supported devices, including IP phones, conference phones, ATAs, SBCs, and PBX systems.

## Snom D7xx Desk Phone Setup

The Snom Professional D7XX series (D120, D717, D735, D785) provides wideband HD audio, Bluetooth compatibility, programmable keys, and preinstalled security certificates. The setup steps apply across the D-series models.

**Get the device IP address and log into the web portal:**

1. Press the **Settings** button, scroll to **Information > System Information** to find the IP address.
2. Enter `http://<IP address>` in a browser.
3. Default credentials: User `admin`, Password `0000`.

![Snom D7xx System Information](_images/5ade2d1c0d8a9b66.png)

Click on **Identity 1** (or the identity to configure).

**Configure the D7xx phone:**

On the **Login** tab:

- Displayname: caller ID (capital letters, no special characters, spaces allowed; Canadian providers may not show more than 15 characters)
- Account: Telnyx account ID
- Password: Telnyx account password
- Registrar: `sip.telnyx.com` (or `sip.telnyx.com:5061` for TLS)
- Outbound Proxy: `sip.telnyx.com` (or `sip.telnyx.com:5061` for TLS)
- Authentication Username: Telnyx account ID
- Mailbox: `*97`

![Snom D7xx Login tab](_images/d832bc8ed16d85f5.png)

Click **Apply**.

On the **SIP** tab:

- Dial-Plan String: `^.$`
- Proposed Expiry: `300`
- Subscription Expiry: `300`
- Failed Subscription Retry Time: `300`

![Snom D7xx SIP tab](_images/789f952afcba872a.png)

Click **Apply**.

**Configure codecs:**

In the RTP Identity Settings field, set codecs in priority sequence. Telnyx supports `ulaw(g711u)`, `alaw(g711a)`, `g722`, and `g729`.

For TLS, also set:

- RTP Encryption: `on`
- RTP/SAVP: `Mandatory`

Click **Apply**, then **Save** at the top of the page.

![Snom D7xx RTP Identity Settings](_images/c9317f7746c13998.png)

## Caller ID Naming Conventions

When configuring a caller ID name across Telnyx-supported devices, observe the following conventions:

- Use capital letters for clearer display on some devices.
- Do not use special characters; spaces are allowed.
- Some Canadian providers will not display more than 15 characters, so consider shortening the caller ID accordingly.

## Related Pages

- [Does Telnyx provide any hardware?](does-telnyx-provide-any-hardware.md)
- [Telnyx Recommended Hardware Configurations](telnyx-recommended-hardware-configurations.md)
- [Audiocodes SBC: Setup](audiocodes-sbc-setup.md)
- [Polycom: Setup with Telnyx](polycom-setup-with-telnyx.md)
- [PhoneSuite Voiceware](phonesuite-voiceware.md)
- [Snom C520: Telnyx Setup](snom-c520-telnyx-setup.md)
- [Audiocodes 400HD](audiocodes-400hd.md)
- [Plantronics/Polycom: OBi300 Setup](plantronics-polycom-obi300-setup.md)
- [Cisco: 68xx/88xx Setup](cisco-68xx-88xx-setup.md)
- [Snom D7xx: Telnyx Setup](snom-d7xx-telnyx-setup.md)
