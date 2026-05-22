---
title: Configure SIP phones with Telnyx (Grandstream, Gigaset, FortiFone, Flyingvoice)
summary: End‑to‑end guide to register popular IP phones to Telnyx using a credentials‑based
  SIP connection. Includes universal settings, codecs and DTMF, TLS/SRTP options,
  voicemail and caller ID tips, plus device‑specific field mappings for Grandstream
  GXV3370, Gigaset A510/A690/DX800a, FortiFone FON‑570/375/175/H25, and Flyingvoice.
sources:
- url: https://support.telnyx.com/en/articles/6187576-grandstream-gxv3370
  content_hash: f75a754a6be7b66b4e892021cab6bf25785af6a4ab92b7982205bb1a2d62ab26
- url: https://support.telnyx.com/en/articles/6167480-gigaset-configuring-the-gigaset-dx800a
  content_hash: 3025cd590ef804154bf22433854e2b11e020dcc1fba90a44f5a4af991e2fc2ee
- url: https://support.telnyx.com/en/articles/5815209-gigaset-a510-telnyx-setup
  content_hash: e42db1a297cc98d6d2e762b3152cfa6cf76b0295b47da9bade99793ad60f8fcd
- url: https://support.telnyx.com/en/articles/6060646-gigaset-a690-as690
  content_hash: 9dfb013df952192c34f098fd63cf01ca3cb8cabd92a64f93f006ed2e195c803c
- url: https://support.telnyx.com/en/articles/5811545-fortifone-setup-fon-375-175-h25
  content_hash: d264a81635e4108ebeb2cce8e195482326b07d6d8aa3cfa3beda8db86d97358c
- url: https://support.telnyx.com/en/articles/5810226-fortifone-fon-570
  content_hash: b055019bb46ae732708a7bede0d679feb2a2d1033208c69f11fd8f7eeb3fc19b
- url: https://support.telnyx.com/en/articles/5810663-flyingvoice-telnyx-setup
  content_hash: 297be44dbfda67bc514ad7193d3bf0d2562809a05fa5f7b76306576dbc74483d
updated_at: 2026-05-20T15:09:08Z
---

# Configure SIP phones with Telnyx (Grandstream, Gigaset, FortiFone, Flyingvoice)

*Part 1 of 2 — see also: [Part 2](configure-sip-phones-with-telnyx-grandstream-gigaset-fortifone-flyingvoice--part-2.md)*

End‑to‑end guide to register popular IP phones to Telnyx using a credentials‑based SIP connection. Includes universal settings, codecs and DTMF, TLS/SRTP options, voicemail and caller ID tips, plus device‑specific field mappings for Grandstream GXV3370, Gigaset A510/A690/DX800a, FortiFone FON‑570/375/175/H25, and Flyingvoice.

## Before you begin
- Create or sign in to your Telnyx Mission Control account and set up the basics:
  - Configure your account: https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account
  - Purchase a DID, provision it to your SIP connection, and create an Outbound Voice Profile:
    - Numbers: https://portal.telnyx.com/#/app/numbers/search-numbers and https://portal.telnyx.com/#/app/numbers/my-numbers
    - Connections: https://portal.telnyx.com/#/app/connections (choose a credentials-based connection)
    - Outbound profiles: https://portal.telnyx.com/#/app/outbound
- Recommended: Enable TLS/SRTP if your device supports it: https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication
- Connect the phone to your LAN and ensure internet access.
- Update device firmware (check the vendor’s guide for your model).
- Find the device IP, then access its web UI from a browser on the same network.

## Universal Telnyx SIP settings
Use these values unless your device or region requires otherwise:
- SIP server / domain / proxy / outbound proxy: sip.telnyx.com
  - For non‑US regions, see the signaling address list: https://sip.telnyx.com/#signaling-addresses
- Transport: UDP by default; use TLS for encrypted signaling (recommended). Some UIs label this as SIP transport or Network Protocol.
- Ports: 5060 for UDP/TCP, 5061 for TLS
- Registration (SIP Register): Enabled
- Registration refresh/expiry: 180–600 seconds (see device notes below)
- Outbound proxy mode: Always (on devices that offer this option)
- STUN: Optional; if needed use stun.telnyx.com:3478

## How to register any IP phone
1) Log into the device web UI
- Browse to http://<device_IP> and sign in with the device’s credentials (see device‑specific notes below for defaults).

2) Add or edit an account/line/connection
- Username / SIP User ID / Register Name / User Name: your Telnyx SIP connection username (main or sub‑account)
- Authentication ID / Authentication Name: same as your Telnyx SIP username (if a separate field is provided)
- Password: your Telnyx SIP connection password
- SIP server / domain / registrar / proxy / outbound proxy: sip.telnyx.com
- Port: 5060 (UDP/TCP) or 5061 (TLS)
- Transport: UDP (default) or TLS if encrypting
- Registration refresh/expiry: set to the model’s recommended value (180–600s)
- Activate/Account Active/Line Active: Enabled
- Save/apply, then verify the registration status shows Registered

3) Assign the account to handsets/lines (if applicable)
- Many multi‑handset/base systems (e.g., Gigaset) require mapping the new SIP account to outgoing/incoming for each handset (see Gigaset tips below).

## Recommended codecs and DTMF
- Audio codecs supported by Telnyx:
  - G.711 µ‑law (ulaw, g711u)
  - G.711 A‑law (alaw, g711a)
  - G.722 (HD)
  - G.729
- DTMF: RFC2833 (often listed as RTP‑event)
- Video (if supported): H.264 (e.g., Grandstream GXV3370)

## TLS/SRTP encryption and ports
- Signaling: set SIP transport to TLS and use port 5061.
- Media: enable SRTP on devices that support it (often labeled RTP Encryption or SRTP; some models allow “Compulsory/Required”).
- Ensure your Telnyx connection is configured for encryption before enabling on the device.

## Caller ID and voicemail conventions
- Display Name (Caller ID Name) recommendations:
  - Use capital letters for better readability on some devices.
  - Avoid special characters; spaces are fine.
  - Some Canadian carriers show ≤15 characters; keep it short.
- Voicemail access number (where configurable): *97

## Device-specific notes and field names
### Grandstream GXV3370 (Android video phone)
- Where to configure: Account > General Settings and SIP Settings.
- Key fields
  - Account Active: Yes
  - SIP Server: sip.telnyx.com
  - SIP User ID / Authentication ID / Password: your Telnyx SIP credentials
  - Outbound Proxy: sip.telnyx.com
  - SIP Transport: UDP (default) or TLS/TCP for encryption
  - Local SIP port: 5060 (UDP), 5061 (TLS/TCP)
  - VoiceMail Access Number: *97
- Codecs: enable ulaw, alaw, G.722, G.729; DTMF RFC2833
- Video: H.264 preferred
- Firmware/login: see the Grandstream administration guide for the latest firmware steps and default web UI credentials.
  - Admin guide: https://documentation.grandstream.com/knowledge-base/gxv3370-administration-guide/

### Gigaset A510 and A690/AS690 (handset + base)
- Find IP: briefly press the paging button on the base; IP shows on the handset display.
- Web UI PIN: default 0000 at first login.
- Telephony > Connections (Edit the target line)
  - Connection name/number: label of your choice
  - Authentication Name / Username: your Telnyx SIP username
  - Authentication Password: your Telnyx SIP password
  - Domain / Proxy server / Registration server: sip.telnyx.com
  - Ports: 5060 (UDP), 5061 (TLS)
  - Registration refresh time: 300s
  - STUN enabled: No (leave empty), unless your network requires it
  - Outbound proxy mode: Always
  - Outbound server: sip.telnyx.com (port 5060/5061 to match transport)
  - Select Network Protocol: UDP by default or TLS if encrypting
- Number Assignment (map the line to handsets)
  - For outgoing calls: select your Telnyx line
  - For incoming calls: enable your Telnyx line

### Gigaset DX800a (legacy hybrid desk phone)
- Web UI PIN: default 0000.
- Telephony > Edit connection > Show Advanced Settings
  - Authentication Name / Username: your Telnyx SIP username
  - Authentication Password: your Telnyx SIP password
  - Domain / Proxy / Registration Address: sip.telnyx.com
  - Ports: 5060 (UDP/TCP), 5061 (TLS)
  - Registration Refresh Time: 600s
  - STUN: optional; if enabled use stun.telnyx.com:3478
  - Outbound proxy mode: Always; Outbound Server: sip.telnyx.com (port per transport)
- Number Assignment: choose your Telnyx account for incoming and outgoing

### FortiFone FON‑570
- Find IP: press OK/Menu > Status on the phone.
- Default web UI login: Username admin, Password 23646 (change after login).
- Account > Register
  - Line Active: Enabled
  - Label / Display Name: as desired (see caller ID tips)
  - Register Name / User Name: your Telnyx SIP username
  - Password: your Telnyx SIP password
  - Server Host: sip.telnyx.com
  - Port: 5060 (UDP), 5061 (TLS)
  - Transport: UDP or TLS (if encrypting)
  - Server Expires: 300s
- Advanced (if encrypting): set RTP Encryption/SRTP to Compulsory
- Date/Time (optional): Time via DHCP: Yes; Primary NTP: pool.ntp.org (optional)

### FortiFone FON‑375 / FON‑175 / FON‑H25
- Find IP: Menu > Status.
- Default web UI login: Username admin, Password 23656 (change after login).
- Line > SIP
  - Username / Authentication Name: your Telnyx SIP username
  - Authentication Password: your Telnyx SIP password
  - Display Name: caller ID text (see tips)
  - Server Name / Register Address: sip.telnyx.com
  - Register Port: 5060 (UDP), 5061 (TLS)
  - Activate: check to enable
  - Transport Protocol: UDP or TLS (if encrypting)
- Advanced (if encrypting): set Transport to TCP if required by model and enable RTP Encryption (SRTP)

### Flyingvoice IP phones (Wi‑Fi and desk)
- Default web UI login: Username admin, Password admin (change after login).
- SIP Account > Line 1
  - Line Enable: Enable
  - Display Name: caller ID text (see tips)
  - Phone Number / Account: your Telnyx SIP username
  - Password: your Telnyx SIP password
  - Proxy Server: sip.telnyx.com
  - Proxy Port: 5060 (UDP), 5061 (TLS)
  - Transport: UDP or TLS (if encrypting)
  - Voice Mailbox Numbers: *97
  - Register Refresh Interval: 180s
  - RTP Port Min/Max: per your network policy (example shown by vendor: 100001–200000)
- Save & Apply
- On‑phone setup alternative: Menu > Advanced (default password admin) > Accounts > Line 1, enable Registration and enter the same values above.
