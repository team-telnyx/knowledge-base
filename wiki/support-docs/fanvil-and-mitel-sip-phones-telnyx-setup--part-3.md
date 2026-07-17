---
title: 'Fanvil and Mitel SIP Phones: Telnyx Setup'
summary: Consolidated Telnyx setup guides for the Fanvil A32i, H2U, H3, H3W/H5W, H5,
  and X1/X1P IP phones, plus the Mitel 5320E/5330E/5340E SIP phones. Each section
  covers device features, web GUI access, line registration against the Telnyx SIP
  trunk at sip.telnyx.com, and supported audio/video codecs.
sources:
- url: https://support.telnyx.com/en/articles/6056428-fanvil-a32i-telnyx-setup
- url: https://support.telnyx.com/en/articles/6202755-fanvil-h2u-compact-ip
- url: https://support.telnyx.com/en/articles/6202965-fanvil-h3-hotel-ip
- url: https://support.telnyx.com/en/articles/6203347-fanvil-h3w-h5w-wifi-ip
- url: https://support.telnyx.com/en/articles/6203401-fanvil-h5-hotel-ip
- url: https://support.telnyx.com/en/articles/6206533-fanvil-x1-x1p-ip-phone
- url: https://support.telnyx.com/en/articles/6244551-mitel-5320e-5330e-5340e-sip
updated_at: 2026-07-17T09:10:55Z
---

# Fanvil and Mitel SIP Phones: Telnyx Setup

*Part 3 of 3 — see also: [Part 1](fanvil-and-mitel-sip-phones-telnyx-setup--part-1.md), [Part 2](fanvil-and-mitel-sip-phones-telnyx-setup--part-2.md)*

Consolidated Telnyx setup guides for the Fanvil A32i, H2U, H3, H3W/H5W, H5, and X1/X1P IP phones, plus the Mitel 5320E/5330E/5340E SIP phones. Each section covers device features, web GUI access, line registration against the Telnyx SIP trunk at sip.telnyx.com, and supported audio/video codecs.

## Mitel 5320E / 5330E / 5340E — SIP Phones

The Mitel MiVoice 5300 series are full-feature enterprise IP phones with embedded gigabit support and self-labeling keys. They differ primarily in display size and the number of programmable keys:

- **MiVoice 5320e** — backlit 160 x 320 LCD, 8 self-labeling keys, 12 fixed function keys, 3 context-sensitive softkeys, wideband audio (G.722), secure voice via encryption. See the [5320e product page](https://www.mitel.com/products/devices-accessories/ip-phones-peripherals/mivoice-5320e-ip-phone).
- **MiVoice 5330e** — large backlit 160 x 320 graphics display with auto dimming, 24 self-labeling keys (3 pages of 8), dual gigabit Ethernet, wideband audio, 12 fixed function keys, 3 context-sensitive softkeys. See the [5330e product page](https://www.mitel.com/products/devices-accessories/ip-phones-peripherals/mivoice-5330e-ip-phone).
- **MiVoice 5340e** — large backlit 160 x 320 graphics display with auto dimming, 48 self-labeling keys (3 pages of 16), dual gigabit Ethernet, wideband audio, 13 fixed function keys, 6 context-sensitive softkeys, optional modules for conferencing, additional buttons, DECT/Bluetooth, or local emergency access. See the [5340e product page](https://www.mitel.com/products/devices-accessories/ip-phones-peripherals/mivoice-5340e-ip-phone).

### Log into the Mitel Web Configuration Tool

Mitel phone configuration is done through the Mitel Web Configuration Tool. To find the phone's IP address:

1. Simultaneously press and hold the up and down volume keys on the phone.
2. While continuing to hold the down arrow key, release the up arrow key.
3. Press `234` on the keypad, then release the down arrow key. The **Network Settings?** option appears.
4. Press `#` (No). The **Network Parameters?** option appears.
5. Press `*` (Yes). The **View Current Values?** option appears.
6. Press `*` (Yes). The **View Current Network?** option appears.
7. Press `*` (Yes). This opens **Current Network Params**.
8. Use the down volume arrow key to scroll to **Phone IP Address** and note the address.
9. From a computer on the same network, open a browser and enter the phone's IP address. First-time login uses:
   - **Username:** `admin`
   - **Password:** The phone's model number — `5320e`, `5330e`, or `5340e`.

### Configure your SIP trunk

1. From the left-hand navigation, go to **Admin Tools > User List Config** and enter:
   - **User ID or Extension:** Your Telnyx account ID.
   - **User Display Name:** Your caller ID (see conventions above).
   - **SIP Authentication User Name:** Your Telnyx account ID.
   - **SIP Authentication Password:** Your Telnyx account password.
   - **Line Type:** `SIP`.
   - **SIP Proxy Server:** `sip.telnyx.com` (US; see [signaling addresses](https://sip.telnyx.com/#signaling-addresses) for international).
   - **Port:** `5060` for TCP/UDP, `5061` for TLS.
   - **Scheme:** `TCP` or `UDP`; choose `TLS` only if encryption is configured.
   - **SIP Registry Server:** `sip.telnyx.com`.
   - **Port:** `5060` for TCP/UDP, `5061` for TLS.
   - **Scheme:** `TCP` or `UDP`; choose `TLS` only if encryption is configured.
   - **SIP Outbound Server:** `sip.telnyx.com`.
   - **Port:** `5060` for TCP/UDP, `5061` for TLS.
   - **Scheme:** `TCP` or `UDP`; choose `TLS` only if encryption is configured.

![User List Configuration section.](_images/4c9b6e2a9fd6602e.png)

2. Click **OK** to submit.

**Additional resources:** [5300 series user manuals](https://www.mitel.com/document-center/devices-and-accessories/ip-phones/5300-series/5300-sip-phones) · [Mitel Learning Center](https://www.mitel.com/support/learning-center) · [Mitel live training webinars](https://www.mitel.com/support/learning-center/live-webinars) · [Mitel user group](https://www.mitel.com/partners/mitel-user-group)

## Related wiki pages

- [Fanvil H2U: Compact IP](fanvil-h2u-compact-ip.md)
- [Fanvil H3: Hotel IP](fanvil-h3-hotel-ip.md)
- [Fanvil H3W/H5W: WiFi IP](fanvil-h3w-h5w-wifi-ip.md)
- [Fanvil H5: Hotel IP](fanvil-h5-hotel-ip.md)
- [Fanvil X1/X1P: IP Phone](fanvil-x1-x1p-ip-phone.md)
- [Fanvil A32i: Telnyx Setup](fanvil-a32i-telnyx-setup.md)
- [Mitel: 5320E/5330E/5340E SIP](mitel-5320e-5330e-5340e-sip.md)
