---
title: 'Fanvil IP Phones: Telnyx Setup'
summary: Configure a Telnyx SIP trunk on Fanvil IP phones across the H-series (H2U,
  H3, H3W, H5W, H5), A32i, X-series (X1/X1P, X2CP/X2C/X2P, X7, general X-series),
  XU-series (X3U/X4U/X5U/X6U), and V-series (V62/V64/V65/V67). All models share the
  same core SIP settings, codec preferences, and optional TLS configuration, though
  the web GUI layout and field names vary slightly between firmware generations.
sources:
- url: https://support.telnyx.com/en/articles/6056428-fanvil-a32i-telnyx-setup
  content_hash: b266cd43acfb5779e25efab0594e1eb08f949139781b235260bb08bfb318f057
- url: https://support.telnyx.com/en/articles/6202755-fanvil-h2u-compact-ip
  content_hash: 07d2ec29a8dd0d2e63b1d7f16382f063e8c528776fd7fb91bb4920c995382bf2
- url: https://support.telnyx.com/en/articles/6202965-fanvil-h3-hotel-ip
  content_hash: df53100fcb255d5491a5b5796b093dcc026d30136bf96134afc27db2b5a033e1
- url: https://support.telnyx.com/en/articles/6203347-fanvil-h3w-h5w-wifi-ip
  content_hash: 2b5d57391bb96e78fcd8d615dbc15f709e24d99bc9d6d21ef7615825cb9141c4
- url: https://support.telnyx.com/en/articles/6203401-fanvil-h5-hotel-ip
  content_hash: f9428ca288c9a9048b2c312801f718701a19568c6eb93d47729d123512bcc7eb
- url: https://support.telnyx.com/en/articles/6206533-fanvil-x1-x1p-ip-phone
  content_hash: 4528c82a0b2952a178b295d713de70572ffd246c75bdd66f095bdc9b5a4daec0
- url: https://support.telnyx.com/en/articles/6206756-fanvil-x2cp-x2c-x2p-call-center-ip
  content_hash: 039d146574411cd40dd4fc41cfcb30b160aca4766e751e91bc67aed8fde09d19
- url: https://support.telnyx.com/en/articles/6209215-fanvil-x7-series-ip-phones
  content_hash: e96c0c9fd809fd6752ae5534707ed3d8775afeb4de9c39af5608fc65e0cbd421
- url: https://support.telnyx.com/en/articles/6209862-fanvil-v-series-ip-phones
  content_hash: f3f12a4367beb8c282d19942ec53b4831f7b58ca92940ae431a92f7cc29c3da1
- url: https://support.telnyx.com/en/articles/6209971-fanvil-x-series-ip-phone
  content_hash: c47714052fa3f174a314be35f8ae8737d151c1570d14816914e2092dbd07284c
- url: https://support.telnyx.com/en/articles/6210147-fanvil-xu-series-ip-phone
  content_hash: 9eee924d3bce4bce7fa3e6a5560b1be9fa1d5c38a15dce9188a55ceecd36048d
updated_at: 2026-06-11T11:29:47Z
---

# Fanvil IP Phones: Telnyx Setup

*Part 1 of 2 — see also: [Part 2](fanvil-ip-phones-telnyx-setup--part-2.md)*

Configure a Telnyx SIP trunk on Fanvil IP phones across the H-series (H2U, H3, H3W, H5W, H5), A32i, X-series (X1/X1P, X2CP/X2C/X2P, X7, general X-series), XU-series (X3U/X4U/X5U/X6U), and V-series (V62/V64/V65/V67). All models share the same core SIP settings, codec preferences, and optional TLS configuration, though the web GUI layout and field names vary slightly between firmware generations.

## Supported Phone Models

The following Fanvil IP phone models can be configured with a Telnyx SIP trunk using the instructions on this page.

| Series | Models | Key Features |
|---|---|---|
| A-Series | A32i | Android console, 10.1″ touch screen, 20 SIP lines, gooseneck mic, optional CM60 camera |
| H-Series | H2U | Compact, 2 SIP lines, 10 speed dial keys, PoE |
| H-Series | H3 | Hotel, 6 programmable keys, PoE, USB charging |
| H-Series | H3W | WiFi hotel, 2 SIP lines, built-in 2.4G WiFi, PoE |
| H-Series | H5W | WiFi hotel, 3.5″ color screen, H.264 video decoding, PoE |
| H-Series | H5 | Hotel, 3.5″ color screen, 6 programmable keys, PoE |
| X-Series | X1/X1P | Entry-level, 2 lines, backlight lattice display, PoE |
| X-Series | X2CP/X2C/X2P | Call center, HD voice, EHS, pedal switch, supervision |
| X-Series | X7/X7C/X7A | High-end enterprise, 20 SIP lines, touch screen, WiFi, Bluetooth |
| X-Series | General X-series | Covers remaining X-models (excl. X4/X4G and X2C/X2CP) |
| XU-Series | X3U/X3U Pro/X4U/X5U/X6U | Enterprise/high-end, HD audio, Opus, color displays, PoE |
| V-Series | V62/V64/V65/V67 | Business/flagship, HD audio/video, Opus, WiFi, Bluetooth |

## Prerequisites

Before configuring your Fanvil phone, ensure the following:

- Your [Telnyx Mission Control Portal](telnyx-mission-control-portal.md) account is properly set up.
- **Recommended:** Enable TLS to encrypt your SIP traffic.
- Your phone is running the latest firmware from [Fanvil's support site](https://www.fanvil.com/Support/index.html).
- You can log into the phone's web GUI. Default credentials vary by model:
  - **H2U, H3, H3W, H5W:** Username `admin`, Password `admin`
  - **A32i:** Refer to section 7.7 (Web Management) of the [user manual](https://fanvil.com.hk/wp-content/uploads/2021/09/A32i-Android-Console-IP-Phone-A32i-User-Manual.pdf)
  - **H5:** Refer to page 13 of the [user manual](https://www.fanvil.com/Uploads/Temp/download/20201110/5faa5e5b85b05.pdf)
  - **X1/X1P:** Refer to page 15 (Section 4.4) of the [user manual](https://www.fanvil.com/Uploads/Temp/download/20201109/5fa90afc7ca32.pdf)
  - **Other models:** Refer to the Web Management or Web Portal section of the respective user manual

You can also configure the SIP trunk directly on the phone screen (e.g., **Phone Settings > Account > Line** on the A32i; long-press a line key to access line config). The default PIN is `123` when prompted on-device.

## Configure a SIP Trunk

All Fanvil models use the same core SIP parameters. The web GUI organises them differently depending on firmware generation. Identify which layout your phone uses and follow the corresponding steps below.

### Layout A — Register Settings + SIP Server 1

Applies to: **A32i, H2U, H3, H3W, H5W, X7/X7C/X7A, V-series, general X-series, XU-series**

1. Log into the web GUI and navigate to **Line > SIP**.
2. Use the **Line** dropdown to select a SIP line to configure.
3. In the **Register Settings** section, fill in:
   - **Username:** Your SIP connection username (see [SIP Connection Types](sip-connection-types.md) Credentials Connection Setup)
   - **Display Name:** Your caller ID. Use capital letters; no special characters (spaces are allowed). Some Canadian providers truncate to 15 characters.
   - **Realm:** The realm to which the SIP interface is connected.
   - **Authentication Name / Authentication User:** Your SIP connection username.
   - **Authentication Password:** Your SIP connection password.
   - **Server Name:** `sip.telnyx.com` (for international addresses, see [Telnyx signaling addresses](https://sip.telnyx.com/#signaling-addresses))
4. In the **SIP Server 1** sub-section:
   - **Server Address:** `sip.telnyx.com` (for international, see [signaling addresses](https://sip.telnyx.com/#signaling-addresses))
   - **Server Port:** `5060` for TCP/UDP; `5061` for TLS
   - **Transport Protocol:** `TCP` or `UDP` (use `TLS` only if encryption is enabled in your Telnyx portal)
   - **Proxy Server Address** (A32i only): `sip.telnyx.com`
5. Optionally configure **SIP Server 2** for redundancy.

### Layout B — Basic Settings + Advanced Settings

Applies to: **H5, X1/X1P, X2CP/X2C/X2P**

1. Log into the web GUI and navigate to **Line > SIP**.
2. Use the **Line** dropdown to select a SIP line to configure.
3. In the **Basic Settings** section, fill in:
   - **Username:** Your SIP connection username
   - **Display Name:** Your caller ID (same conventions as above)
   - **Authentication Name:** Your SIP connection username
   - **Authentication Password:** Your SIP connection password
   - **SIP Proxy Server Address / SIP Proxy Address:** `sip.telnyx.com` (this also serves as the outbound and backup proxy address where applicable)
   - **SIP Proxy Port:** `5060` for TCP/UDP; `5061` for TLS
   - **Outbound Proxy Address:** `sip.telnyx.com`
   - **Outbound Proxy Port:** `5060` for TCP/UDP; `5061` for TLS
   - **Realm:** The realm to which the SIP interface is connected
4. In the **Advanced Settings** sub-section:
   - **DTMF Type:** `RFC 2833`
   - **Transport Protocol / Transportation Protocol:** `TCP` or `UDP` (use `TLS` only if encryption is enabled in your Telnyx portal)
     - If using TLS, go to **Lines > Dial Peer** and change the **Port** setting to `5061`.
   - **SIP Encryption** (H5): Enable if using TLS; obtain a key from [crt.sh](https://crt.sh/?id=1199354)
   - **RTP Encryption** (X1/X1P, X2CP/X2C/X2P): Optionally enable if using TLS; obtain a key from [crt.sh](https://crt.sh/?id=1199354)

## Configure Voice and Video Codecs

After configuring the SIP line, set the codec priorities:

1. Expand the **Codecs Settings** section for the line you just configured.
2. Add or remove codecs to match Telnyx's supported list and set priority order:

   **Audio codecs:**
   - `ulaw (g711u)`
   - `alaw (g711a)`
   - `g722`
   - `g729`

   **Video codec:**
   - `H264`

## Upload a TLS Certificate (Optional)

If you are encrypting traffic with TLS, upload a certificate. This applies to **X1/X1P, X2CP/X2C/X2P, X7 series, V-series, general X-series, and XU-series**.

1. In **Lines > SIP**, find the **Advanced Settings** sub-section and confirm:
   - **DTMF Type:** `RFC 2833`
   - **Transportation Protocol:** `TLS`
   - If encrypting traffic, go to **Lines > Dial Peer** and change the **Port** to `5061`.
   - **RTP Encryption:** Optionally enable; obtain a key from [crt.sh](https://crt.sh/?id=1199354)
2. Navigate to **Line > Basic Settings**, find the **STUN Settings** section, and set:
   - **TLS Certification File:** Obtain a certificate from [crt.sh](https://crt.sh/?id=1199354)
