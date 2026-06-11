---
title: SIP Phone and Device Configuration with Telnyx
summary: A consolidated guide for configuring SIP endpoints from multiple manufacturers—including
  Algo, Panasonic, FortiFone, Flyingvoice, Fanvil, Positron, Gigaset, Snom, AudioCodes,
  Konftel, Vtech, Mitel, Alcatel, and BuddyTalk—to register with Telnyx's SIP infrastructure.
  Covers common prerequisites, the shared SIP parameter set, device-specific web portal
  navigation, TLS/SRTP encryption, codec selection, and troubleshooting.
sources:
- url: https://support.telnyx.com/en/articles/5790092-algo-8xxx-telnyx-endpoints
  content_hash: 43ca570acdf8ebf6af50947bff040e28e24183f6673051cef18a2161a4d93c5b
- url: https://support.telnyx.com/en/articles/5807663-panasonic-kx-tgp-550
  content_hash: 1d878fa381b0d731ad7ccc2cdd136a855809ca306a898b9067c3a24e7f93a519
- url: https://support.telnyx.com/en/articles/5808185-buddytalk-bt110-bt120
  content_hash: 866e579aeb36008f61ab49040c70d1429fc218655424cad0ad7fb9f4437c0671
- url: https://support.telnyx.com/en/articles/5810226-fortifone-fon-570
  content_hash: 70651e5612d9ba764c99554d14d8bd5a25af6f06b40176de119869f58e7e6c79
- url: https://support.telnyx.com/en/articles/5810663-flyingvoice-telnyx-setup
  content_hash: 28d39cec6c3e81af149dac9816f242865cf90f411e6f4e8a740aa625d5645f27
- url: https://support.telnyx.com/en/articles/5811487-fanvil-x4g-telnyx-setup
  content_hash: 20dc83f187ac9e5af1b5e71f1714b8c1677cadade2d40fa58903cea1e2541470
- url: https://support.telnyx.com/en/articles/5811545-fortifone-setup-fon-375-175-h25
  content_hash: c89aadd3c2d42bdac8e226df1256e84dba0b9f3f4c75e80c2fbc6b8004736abb
- url: https://support.telnyx.com/en/articles/5811761-positron-ip-phone
  content_hash: 555b1188c4bc60511fb3439fd6d8ead34b36fa82775e1a2cf3080f387f8eb90c
- url: https://support.telnyx.com/en/articles/5814406-panasonic-kx-hdv-telnyx-setup
  content_hash: 7e68027552375addf716c64971fd320a371fb080b3a3242ea44635f5dd2de932
- url: https://support.telnyx.com/en/articles/5815209-gigaset-a510-telnyx-setup
  content_hash: 205804c4ccf4a39a3fdefd347884de57d1fbda2c1c84d57cafec40d05c995b07
- url: https://support.telnyx.com/en/articles/5815678-snom-c520-telnyx-setup
  content_hash: 2e68c5508cdcfdf14e0d1492c675407ddf6f737af0f227593499e829bc6caa97
- url: https://support.telnyx.com/en/articles/5819923-audiocodes-400hd
  content_hash: af10c7110f9cfbe7b52cdc198d2dbb1d576c97dee61451ad82533f7377b32ec2
- url: https://support.telnyx.com/en/articles/5822579-konftel-300ipx-telnyx-setup
  content_hash: d8d1a62aaade1a708c7623a567f6a9e9182bfb68e0e769c1db3a2bd3269c1551
- url: https://support.telnyx.com/en/articles/5822706-snom-d7xx-telnyx-setup
  content_hash: b7337d44aff1aa006de484a7afcab53c5d1ef7f88df83609ed61bedd7fe3c70c
- url: https://support.telnyx.com/en/articles/5822823-snom-m100-kle-telnyx-setup
  content_hash: fc2033a52310b276053c73d5f87dc0ff352440551476cf05e0c6f855b6395e7d
- url: https://support.telnyx.com/en/articles/5822901-vtech-vcs754-telnyx-setup
  content_hash: 9fbbdf4f96e4268f208b007991818036a0640422e9ba8b368e4bc7bda6ef9a99
- url: https://support.telnyx.com/en/articles/6060646-gigaset-a690-as690
  content_hash: 0410b7c3f4457518fca5fab15bc4d8ed88ab43d5ad379e9817d9e8d07250bd21
- url: https://support.telnyx.com/en/articles/6244551-mitel-5320e-5330e-5340e-sip
  content_hash: 30c2edf7512d16a10227ccabf0391943a3e72b2a94b2096d4fd9a192bde7c6f9
- url: https://support.telnyx.com/en/articles/6249691-mitel-6800-6900-sip
  content_hash: dc8bed8636a3a31bb30b16f23eb273a5b64ad82977918eb6a901159f098333ed
- url: https://support.telnyx.com/en/articles/6281943-alcatel-sd601-sd602-sip-door
  content_hash: b8ca5df7332e282dd6fb657ca84dd5e27971a6c762f083d17a823d2007e6aa82
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
