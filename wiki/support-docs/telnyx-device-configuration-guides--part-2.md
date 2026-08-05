---
title: Telnyx Device Configuration Guides
summary: Step-by-step instructions for configuring Telnyx SIP trunks on a range of
  supported devices, including the Ribbon EdgeMarc 6000 SBC, Snom M100 KLE base station,
  Mitel 5320E/5330E/5340E and 6800/6900 SIP phones, and Alcatel SD601/SD602 SIP door
  phones. Each guide covers prerequisites, device access, SIP server settings, and
  registration parameters required to connect the device to the Telnyx Mission Control
  Portal.
sources:
- url: https://support.telnyx.com/en/articles/4215031-ribbon-edgemarc-6000-setup
- url: https://support.telnyx.com/en/articles/5822823-snom-m100-kle-telnyx-setup
- url: https://support.telnyx.com/en/articles/6244551-mitel-5320e-5330e-5340e-sip
- url: https://support.telnyx.com/en/articles/6249691-mitel-6800-6900-sip
- url: https://support.telnyx.com/en/articles/6281943-alcatel-sd601-sd602-sip-door
updated_at: 2026-08-05T13:36:02Z
---

# Telnyx Device Configuration Guides

*Part 2 of 4 — see also: [Part 1](telnyx-device-configuration-guides--part-1.md), [Part 3](telnyx-device-configuration-guides--part-3.md), [Part 4](telnyx-device-configuration-guides--part-4.md)*

Step-by-step instructions for configuring Telnyx SIP trunks on a range of supported devices, including the Ribbon EdgeMarc 6000 SBC, Snom M100 KLE base station, Mitel 5320E/5330E/5340E and 6800/6900 SIP phones, and Alcatel SD601/SD602 SIP door phones. Each guide covers prerequisites, device access, SIP server settings, and registration parameters required to connect the device to the Telnyx Mission Control Portal.

## Mitel 5320E/5330E/5340E SIP Setup

The Mitel MiVoice 5300e series are full-feature IP phones with backlit graphics displays, embedded gigabit support, and self-labeling keys. The 5320e has 8 programmable keys, the 5330e has 24 keys across three pages, and the 5340e has 48 keys across three pages. All support wideband audio (G.722), HTML Desktop Toolkit, Mitel MiCollab Client, and Mitel Intelligent Directory.

Additional resources: [5300 series user manuals](https://www.mitel.com/document-center/devices-and-accessories/ip-phones/5300-series/5300-sip-phones), [Mitel Learning Center](https://www.mitel.com/support/learning-center), [Mitel live training webinars](https://www.mitel.com/support/learning-center/live-webinars), [Mitel user group](https://www.mitel.com/partners/mitel-user-group).

### Log Into the Mitel Web Configuration Tool

1. Simultaneously press and hold the up and down volume keys on the phone.
2. While holding the down arrow, release the up arrow.
3. Press `234` on the keypad, then release the down arrow. The **Network Settings?** option appears.
4. Press `#` (No). The **Network Parameters?** option appears.
5. Press `*` (Yes). The **View Current Values?** option appears.
6. Press `*` (Yes). The **View Current Network?** option appears.
7. Press `*` (Yes) to open **Current Network Params**.
8. Scroll to **Phone IP Address** and note the IP address.
9. From a computer on the same network, enter the IP address in a browser. Default credentials:
   - **Username:** `admin`
   - **Password:** The phone's model number (`5320e`, `5330e`, or `5340e`)

### Configure the SIP Trunk

1. From the left-hand navigation, go to **Admin Tools > User List Config** and enter:
   - **User ID or Extension:** Telnyx account ID
   - **User Display Name:** Caller ID (use capital letters, no special characters, spaces allowed; some Canadian providers limit to 15 characters)
   - **SIP Authentication User Name:** Telnyx account ID
   - **SIP Authentication Password:** Telnyx account password
   - **Line Type:** `SIP`
   - **SIP Proxy Server:** `sip.telnyx.com` (US; see [international signaling addresses](https://sip.telnyx.com/#signaling-addresses))
   - **Port:** `5060` for TCP/UDP, `5061` for TLS
   - **Scheme:** `TCP` or `UDP` (or `TLS` if encryption is enabled)
   - **SIP Registry Server:** `sip.telnyx.com`
   - **Port:** `5060` for TCP/UDP, `5061` for TLS
   - **Scheme:** `TCP` or `UDP` (or `TLS` if encryption is enabled)
   - **SIP Outbound Server:** `sip.telnyx.com`
   - **Port:** `5060` for TCP/UDP, `5061` for TLS
   - **Scheme:** `TCP` or `UDP` (or `TLS` if encryption is enabled)

![User List Configuration section.](_images/4c9b6e2a9fd6602e.png)

2. Click **OK** to submit.
