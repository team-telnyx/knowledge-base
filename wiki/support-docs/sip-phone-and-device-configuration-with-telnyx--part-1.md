---
title: SIP Phone and Device Configuration with Telnyx
summary: A consolidated guide for configuring SIP endpoints from multiple manufacturers—including
  Algo, Panasonic, FortiFone, Flyingvoice, Fanvil, Positron, Gigaset, Snom, AudioCodes,
  Konftel, Vtech, Mitel, Alcatel, and BuddyTalk—to register with Telnyx's SIP infrastructure.
  Covers common prerequisites, the shared SIP parameter set, device-specific web portal
  navigation, TLS/SRTP encryption, codec selection, and troubleshooting.
sources:
- url: https://support.telnyx.com/en/articles/5790092-algo-8xxx-telnyx-endpoints
- url: https://support.telnyx.com/en/articles/5807663-panasonic-kx-tgp-550
- url: https://support.telnyx.com/en/articles/5808185-buddytalk-bt110-bt120
- url: https://support.telnyx.com/en/articles/5810226-fortifone-fon-570
- url: https://support.telnyx.com/en/articles/5810663-flyingvoice-telnyx-setup
- url: https://support.telnyx.com/en/articles/5811487-fanvil-x4g-telnyx-setup
- url: https://support.telnyx.com/en/articles/5811545-fortifone-setup-fon-375-175-h25
- url: https://support.telnyx.com/en/articles/5811761-positron-ip-phone
- url: https://support.telnyx.com/en/articles/5814406-panasonic-kx-hdv-telnyx-setup
- url: https://support.telnyx.com/en/articles/5815209-gigaset-a510-telnyx-setup
- url: https://support.telnyx.com/en/articles/5815678-snom-c520-telnyx-setup
- url: https://support.telnyx.com/en/articles/5819923-audiocodes-400hd
- url: https://support.telnyx.com/en/articles/5822579-konftel-300ipx-telnyx-setup
- url: https://support.telnyx.com/en/articles/5822706-snom-d7xx-telnyx-setup
- url: https://support.telnyx.com/en/articles/5822823-snom-m100-kle-telnyx-setup
- url: https://support.telnyx.com/en/articles/5822901-vtech-vcs754-telnyx-setup
- url: https://support.telnyx.com/en/articles/6060646-gigaset-a690-as690
- url: https://support.telnyx.com/en/articles/6244551-mitel-5320e-5330e-5340e-sip
- url: https://support.telnyx.com/en/articles/6249691-mitel-6800-6900-sip
- url: https://support.telnyx.com/en/articles/6281943-alcatel-sd601-sd602-sip-door
updated_at: 2026-06-11T11:33:51Z
---

# SIP Phone and Device Configuration with Telnyx

*Part 1 of 3 — see also: [Part 2](sip-phone-and-device-configuration-with-telnyx--part-2.md), [Part 3](sip-phone-and-device-configuration-with-telnyx--part-3.md)*

A consolidated guide for configuring SIP endpoints from multiple manufacturers—including Algo, Panasonic, FortiFone, Flyingvoice, Fanvil, Positron, Gigaset, Snom, AudioCodes, Konftel, Vtech, Mitel, Alcatel, and BuddyTalk—to register with Telnyx's SIP infrastructure. Covers common prerequisites, the shared SIP parameter set, device-specific web portal navigation, TLS/SRTP encryption, codec selection, and troubleshooting.

## Prerequisites

Before configuring any SIP endpoint with Telnyx, ensure the following:

- Your [Telnyx Mission Control Portal](telnyx-mission-control-portal.md) account is properly set up.
- You have at least one Telnyx SIP account or sub-account with valid credentials (username and password).
- A valid Caller ID is configured on your SIP account if the device will make outgoing calls (anonymous outbound calls are not possible).
- A DID (phone number) is provisioned from Telnyx if the device requires one.
- **Recommended:** Enable TLS on your Telnyx portal if you want to encrypt SIP traffic (see [Does Telnyx Encrypt Communication?](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)).
- Your device is running the latest firmware from the manufacturer.
- Your firewall allows SIP communication on the appropriate port (5060 for UDP/TCP, 5061 for TLS).

## Common SIP Configuration Parameters

Nearly every device shares the same core set of SIP parameters when registering with Telnyx. Use the table below as a quick reference regardless of your device model.

| Parameter | Value |
|---|---|
| SIP Server / Proxy / Registrar | `sip.telnyx.com` |
| SIP Port (UDP / TCP) | `5060` |
| SIP Port (TLS) | `5061` |
| Authentication ID / Username | Your Telnyx SIP account (or sub-account) username |
| Authentication Password | Your Telnyx SIP account password |
| Display Name / Caller ID | See Caller ID naming conventions below |
| Transport Protocol | `UDP` (default); `TLS` if encrypting |
| Registration Expiry | `300` seconds (commonly recommended) |
| Outbound Proxy | `sip.telnyx.com` (with appropriate port) |
| Service Domain | `sip.telnyx.com` |

For a list of international signaling addresses, see [Telnyx SIP Signaling Addresses](https://sip.telnyx.com/#signaling-addresses).

### Caller ID Naming Conventions

- Use **capital letters** for maximum visibility on receiving devices.
- **No special characters** — they will not be displayed. Spaces are allowed.
- Some Canadian providers truncate the name to **15 characters**; keep your Caller ID concise.

## Supported Audio Codecs

Telnyx supports the following codecs. Enable those you need and disable any others on your device:

- **G.711 u-law** (g711u)
- **G.711 A-law** (g711a)
- **G.722** (wideband)
- **G.729**

## Getting Your Device IP Address

All devices are configured through a web portal. You need the device's IP address to access it. The method varies by manufacturer:

| Device | How to Find the IP Address |
|---|---|
| Algo 8xxx | Displayed on the device's landing page after boot |
| Panasonic KX-TGP 550 | Handset: **Menu → IP Service → Network Setting → IP Setting** |
| Panasonic KX-HDV | Phone: **Basic Settings → Other Options → Embedded Web → On**, then **System Settings → Status → IPv4 Settings → IP Address** |
| BuddyTalk BT110/BT120 | Via the BuddyTalk Setup App |
| FortiFone FON-570 | Phone: **OK/Menu → Status** |
| FortiFone FON-375/175/H25 | Phone: **Menu → Status** |
| Flyingvoice | Displayed on the LCD after initialization |
| Fanvil X4G | Phone: **OK → Status → IP Address** |
| Positron IP304 | Phone: **Menu → Status → Information** |
| Gigaset A510 / A690 | Press the paging button on the base station |
| Snom C520 | Phone: **Menu → Status → Network** |
| Snom D7xx | Phone: **Settings → Information → System Information** |
| Snom M100 KLE | Phone: **Menu → Status → Network** |
| AudioCodes 400HD | Phone: **Menu → Device Status → Network Settings → IP Address** |
| Konftel 300IPx | Phone: **Menu → Status → Network** |
| Vtech VCS754 | Phone: **Menu → Status → Network** |
| Mitel 5320E/5330E/5340E | Hold volume up+down, release up, press 234, release down, then navigate to **Phone IP Address** |
| Mitel 6800/6900 | Phone UI: **Phone Status → IP&MAC Addresses** or **Network → IP Address** (varies by model) |
| Alcatel SD601/SD602 | Hold `#` for 3 seconds; IP is read aloud |

## Web Portal Default Credentials

Open a browser on a computer on the same network and navigate to `http://<DEVICE_IP>`. Default credentials for first-time login:

| Device | Username | Password |
|---|---|---|
| Algo 8xxx | (none) | (none) |
| Panasonic KX-TGP 550 | admin | adminpass |
| Panasonic KX-HDV | admin | adminpass |
| BuddyTalk BT110/BT120 | (via Setup App) | (via Setup App) |
| FortiFone FON-570 | admin | 23646 |
| FortiFone FON-375/175/H25 | admin | 23656 |
| Flyingvoice | admin | admin |
| Fanvil X4G | admin | admin |
| Positron IP304 | admin | admin |
| Gigaset A510 / A690 | (System PIN) | 0000 |
| Snom C520 | admin | admin |
| Snom D7xx | admin | 0000 |
| Snom M100 KLE | admin | admin |
| AudioCodes 400HD | admin | 1234 |
| Konftel 300IPx | ADMIN | 1234 |
| Vtech VCS754 | admin | admin |
| Mitel 5320E/5330E/5340E | admin | Model number (e.g. `5320e`) |
| Mitel 6800/6900 (admin) | admin | 22222 |
| Mitel 6800/6900 (user) | user | *(blank)* |
| Alcatel SD601/SD602 | admin | admin |

**Always change default credentials after first login.**
