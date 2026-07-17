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

*Part 1 of 3 — see also: [Part 2](fanvil-and-mitel-sip-phones-telnyx-setup--part-2.md), [Part 3](fanvil-and-mitel-sip-phones-telnyx-setup--part-3.md)*

Consolidated Telnyx setup guides for the Fanvil A32i, H2U, H3, H3W/H5W, H5, and X1/X1P IP phones, plus the Mitel 5320E/5330E/5340E SIP phones. Each section covers device features, web GUI access, line registration against the Telnyx SIP trunk at sip.telnyx.com, and supported audio/video codecs.

## Overview

This page consolidates Telnyx setup guides for several Fanvil and Mitel SIP desk phones. Each device follows the same general workflow — log into the phone's web GUI, register a line against the Telnyx SIP trunk at `sip.telnyx.com`, and configure the supported audio/video codecs — but the exact field names and menu paths differ between models.

## Pre-requisites (all devices)

Before configuring any device on this page, make sure that:

- Your [Telnyx Mission Control Portal](telnyx-mission-control-portal.md) account is configured correctly.
- TLS encryption is enabled on the Telnyx portal if you intend to use it (recommended).
- The phone is running the latest firmware from Fanvil or Mitel.
- You can log into the phone's web GUI using the default credentials listed in each device section below.

For international deployments, replace `sip.telnyx.com` with the appropriate regional signaling address from the [Telnyx signaling addresses reference](https://sip.telnyx.com/#signaling-addresses).

## Caller ID naming conventions

All devices on this page share the same caller ID guidance. The **Display Name** (or **User Display Name** on Mitel) is your outbound caller ID. Follow these conventions:

- Use capital letters so the name renders clearly on receiving devices.
- Do not use special characters — they will not be displayed. Spaces are allowed.
- Some Canadian carriers truncate caller ID names to 15 characters; keep the name short if you call Canada frequently.

## Fanvil A32i — Android Console IP Phone

The [Fanvil A32i](https://www.fanvil.com/Product/info/id/139.html) is an Android console IP phone designed for small and medium control centers. It features a gooseneck microphone, a 10.1-inch touch screen with 112 DSS keys, optional 1080P USB camera, three-way video conferencing, H.264 video codec, a built-in Harman speaker, optional PTM handset, and built-in 2.4G/5G WiFi and Bluetooth. It supports up to 20 SIP lines.

**Web GUI access:** Default credentials are documented on page 32 of the [A32i user manual](https://fanvil.com.hk/wp-content/uploads/2021/09/A32i-Android-Console-IP-Phone-A32i-User-Manual.pdf) (section 7.7: Web Management). You can also configure the SIP trunk directly on the phone by long-pressing the line key, or via **Phone Settings > Account > Line**. The default device PIN is `123`.

### Configure a line with a Telnyx SIP trunk

1. Log into the web GUI and navigate to **Line > SIP**.
2. Use the **Line** dropdown to select a SIP line.
3. In **Register Settings**:
   - **Username:** Telnyx portal main or sub-account username.
   - **Display Name:** Your caller ID (see conventions above).
   - **Realm:** Name of the realm the SIP interface is connected to.
   - **Authentication User:** Telnyx portal main or sub-account username.
   - **Authentication Password:** Telnyx portal main or sub-account password.
   - **Server Name:** `sip.telnyx.com`.
4. In **SIP Server 1**:
   - **Server Address:** `sip.telnyx.com`.
   - **Server Port:** `5060` for TCP/UDP, `5061` for TLS.
   - **Transport Protocol:** `TCP` or `UDP`; choose `TLS` only if encryption is configured on the Telnyx portal.
   - **Proxy Server Address:** `sip.telnyx.com`.

![SIP Server 1 sub-section.](_images/4824a0b4d660ea0c.png)

5. Optionally configure **SIP Server 2**.

### Configure voice and video codecs

Expand **Codecs Settings** on the configured line and add or remove codecs. Telnyx supports:

- **Audio:** `ulaw(g711u)`, `alaw(g711a)`, `g722`, `g729`
- **Video:** `H264`

**Additional resources:** [A32i user manual](https://fanvil.com.hk/wp-content/uploads/2021/09/A32i-Android-Console-IP-Phone-A32i-User-Manual.pdf) · [Fanvil FAQ](https://www.fanvil.com/Support/index.html) · [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html) · [Fanvil support](https://www.fanvil.com/Support/ticket.html) · [A32i firmware](https://www.fanvil.com/Support/download/id/139.html)

## Fanvil H2U — Compact IP Phone

The [Fanvil H2U](https://www.fanvil.com/Product/info/id/122.html) is a compact IP phone with HD audio, Opus support, 2 SIP lines, 10 speed dial keys, 1 DSS key, and PoE. It supports desktop and wall-mounted modes and is suitable for hotels, schools, hospitals, supermarkets, and residences.

**Web GUI access:** Default credentials are `admin` / `admin`.

### Configure a line with a Telnyx SIP trunk

1. Log into the web GUI and navigate to **Line > SIP**.
2. Use the **Line** dropdown to select a SIP line.
3. In **Register Settings**:
   - **Username:** SIP connection username (see [SIP connection types](https://support.telnyx.com/en/articles/4245868-sip-connection-types)).
   - **Display Name:** Your caller ID.
   - **Realm:** Name of the realm the SIP interface is connected to.
   - **Authentication Name:** SIP connection username.
   - **Authentication Password:** SIP connection password.
   - **Server Name:** `sip.telnyx.com`.
4. In **SIP Server 1**:
   - **Server Address:** `sip.telnyx.com`.
   - **Server Port:** `5060` for TCP/UDP, `5061` for TLS.
   - **Transport Protocol:** `TCP` or `UDP`; choose `TLS` only if encryption is configured.

![Register Settings section in the web GUI.](_images/4824a0b4d660ea0c.png)

5. Optionally configure **SIP Server 2**.

### Configure voice and video codecs

Expand **Codecs Settings** on the configured line. Telnyx supports:

- **Audio:** `ulaw(g711u)`, `alaw(g711a)`, `g722`, `g729`
- **Video:** `H264`

**Additional resources:** [H2U user manual](https://www.fanvil.com/Uploads/Temp/download/20210421/607fcc2424c72.pdf) · [Fanvil FAQ](https://www.fanvil.com/Support/index.html) · [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html) · [Fanvil support](https://www.fanvil.com/Support/ticket.html) · [H2U firmware](https://www.fanvil.com/Support/download/id/122.html)

## Fanvil H3 — Hotel IP Phone

The [Fanvil H3](https://www.fanvil.com/Product/info/id/78.html) is an affordable hotel IP phone with HD audio, PoE, a USB charging port, 6 programmable keys, and call transfer.

**Web GUI access:** Default credentials are `admin` / `admin`.

### Configure a line with a Telnyx SIP trunk

1. Log into the web GUI and navigate to **Line > SIP**.
2. Use the **Line** dropdown to select a SIP line.
3. In **Register Settings**:
   - **Username:** SIP connection username.
   - **Display Name:** Your caller ID.
   - **Realm:** Name of the realm the SIP interface is connected to.
   - **Authentication Name:** SIP connection username.
   - **Authentication Password:** SIP connection password.
   - **Server Name:** `sip.telnyx.com`.
4. In **SIP Server 1**:
   - **Server Address:** `sip.telnyx.com`.
   - **Server Port:** `5060` for TCP/UDP, `5061` for TLS.
   - **Transport Protocol:** `TCP` or `UDP`; choose `TLS` only if encryption is configured.

![Register Settings section of the web GUI.](_images/4824a0b4d660ea0c.png)

5. Optionally configure **SIP Server 2**.

### Configure voice and video codecs

Expand **Codecs Settings** on the configured line. Telnyx supports:

- **Audio:** `ulaw(g711u)`, `alaw(g711a)`, `g722`, `g729`
- **Video:** `H264`

**Additional resources:** [H3 user manual](https://www.fanvil.com/Uploads/Temp/download/20210421/607fcc2424c72.pdf) · [Fanvil FAQ](https://www.fanvil.com/Support/index.html) · [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html) · [Fanvil support](https://www.fanvil.com/Support/ticket.html) · [H3 firmware](https://www.fanvil.com/Support/download/id/78.html)
