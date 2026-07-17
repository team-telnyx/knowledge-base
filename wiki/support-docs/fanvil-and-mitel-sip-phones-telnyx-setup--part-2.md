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

*Part 2 of 3 — see also: [Part 1](fanvil-and-mitel-sip-phones-telnyx-setup--part-1.md), [Part 3](fanvil-and-mitel-sip-phones-telnyx-setup--part-3.md)*

Consolidated Telnyx setup guides for the Fanvil A32i, H2U, H3, H3W/H5W, H5, and X1/X1P IP phones, plus the Mitel 5320E/5330E/5340E SIP phones. Each section covers device features, web GUI access, line registration against the Telnyx SIP trunk at sip.telnyx.com, and supported audio/video codecs.

## Fanvil H3W / H5W — WiFi IP Phones

The [Fanvil H3W](https://www.fanvil.com/Product/info/id/138.html) and [Fanvil H5W](https://www.fanvil.com/Product/info/id/137.html) are WiFi IP phones with HD audio, built-in 2.4G WiFi, 2 SIP lines, and PoE. The H3W adds a USB charging port and 6 programmable keys; the H5W adds a 3.5-inch color screen and H.264 video decoding (useful for viewing video at a door before answering).

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

![Settings section.](_images/4824a0b4d660ea0c.png)

5. Optionally configure **SIP Server 2**.

### Configure voice and video codecs

Expand **Codecs Settings** on the configured line. Telnyx supports:

- **Audio:** `ulaw(g711u)`, `alaw(g711a)`, `g722`, `g729`
- **Video:** `H264`

**Additional resources:** [H3W/H5W user manual](https://www.fanvil.com/Uploads/Temp/download/20210608/60bf0ca559890.pdf) · [Fanvil FAQ](https://www.fanvil.com/Support/index.html) · [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html) · [Fanvil support](https://www.fanvil.com/Support/ticket.html) · [H3W firmware](https://www.fanvil.com/Support/download/id/138.html) · [H5W firmware](https://www.fanvil.com/Support/download/id/137.html)

## Fanvil H5 — Hotel IP Phone

The [Fanvil H5](https://www.fanvil.com/Product/info/id/79.html) is a hotel IP phone available in white or black, with a 3.5-inch color screen that hotels can customize with their address, logo, and related phone numbers. It supports HD audio, a USB charging port, 6 programmable keys, call transfer, and PoE.

**Web GUI access:** Default credentials and other information are documented on page 13 of the [H5 user manual](https://www.fanvil.com/Uploads/Temp/download/20201110/5faa5e5b85b05.pdf) (section 5: Phone Settings, 5.1–5.3).

### Configure a line with a Telnyx SIP trunk

1. Log into the web GUI and navigate to **Line > SIP**.
2. Use the **Line** dropdown to select a SIP line.
3. In **Basic Settings**:
   - **Username:** SIP connection username.
   - **Display Name:** Your caller ID.
   - **Authentication Name:** SIP connection username.
   - **Authentication Password:** SIP connection password.
   - **SIP Proxy Address:** `sip.telnyx.com`.
   - **SIP Proxy Port:** `5060` for TCP/UDP, `5061` for TLS.
   - **Outbound Proxy Address:** `sip.telnyx.com`.
   - **Outbound Proxy Port:** `5060` for TCP/UDP, `5061` for TLS.
   - **Realm:** Name of the realm the SIP interface is connected to.
4. In **Advanced Settings**:
   - **DTMF Type:** `RFC 2833`.
   - **Transport Protocol:** `TCP` or `UDP`; choose `TLS` only if encryption is configured. If you use TLS, also go to **Lines > Dial Peer** and change the **Port** to `5061`.
   - **SIP Encryption:** Enable if using TLS.
   - **SIP Encryption Key:** Obtain a key from [crt.sh](https://crt.sh/?id=1199354).

### Configure voice and video codecs

In **Codecs Settings**, set the priority and availability of audio and video codecs. Telnyx supports:

- **Audio:** `ulaw(g711u)`, `alaw(g711a)`, `g722`, `g729`
- **Video:** `H264`

**Additional resources:** [H5 user manual](https://www.fanvil.com/Uploads/Temp/download/20201110/5faa5e5b85b05.pdf) · [Fanvil FAQ](https://www.fanvil.com/Support/index.html) · [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html) · [Fanvil support](https://www.fanvil.com/Support/ticket.html) · [H5 firmware](https://www.fanvil.com/Support/download/id/79.html)

## Fanvil X1 / X1P — IP Phone

The [Fanvil X1 / X1P](https://www.fanvil.com/Product/info/id/89.html) is an entry-level, cost-effective professional desktop IP phone with 2 lines, a 128 x 48 backlit lattice display, 3-way conference calling, RJ9, and PoE.

**Web GUI access:** Default credentials and other information are documented on page 15 of the [X1/X1P user manual](https://www.fanvil.com/Uploads/Temp/download/20201109/5fa90afc7ca32.pdf) (section 4.4: Web Portal).

### Configure a line with a Telnyx SIP trunk

1. Log into the web GUI and navigate to **Line > SIP**.
2. Use the **Line** dropdown to select a SIP line.
3. In **Basic Settings**:
   - **Username:** SIP connection username.
   - **Display Name:** Your caller ID.
   - **Authentication Name:** SIP connection username.
   - **Authentication Password:** SIP connection password.
   - **SIP Proxy Server Address:** `sip.telnyx.com` (also used as the outbound proxy and backup proxy server address).
   - **SIP Proxy Port:** `5060` for TCP/UDP, `5061` for TLS.
   - **Outbound Proxy Address:** `sip.telnyx.com`.
   - **Outbound Proxy Port:** `5060` for TCP/UDP, `5061` for TLS.
   - **Realm:** Name of the realm the SIP interface is connected to.
4. In **Advanced Settings**:
   - **DTMF Type:** `RFC 2833`.
   - **Transportation Protocol:** `TCP` or `UDP`; choose `TLS` only if encryption is configured. If you use TLS, also go to **Lines > Dial Peer** and change the **Port** to `5061`.
   - **RTP Encryption:** (Optional) Enable if using TLS.
   - **RTP Encryption Key:** (Optional) Obtain a key from [crt.sh](https://crt.sh/?id=1199354).

### Configure voice and video codecs

In **Codecs Settings**, set the priority and availability of audio and video codecs. Telnyx supports:

- **Audio:** `ulaw(g711u)`, `alaw(g711a)`, `g722`, `g729`
- **Video:** `H264`

### (Optional) Upload a TLS certificate

If you are encrypting traffic with TLS, upload a TLS certificate:

1. Navigate to **Line > Basic Settings** and find the **STUN Settings** section.
2. Set **TLS Certification File** to a certificate obtained from [crt.sh](https://crt.sh/?id=1199354).

**Additional resources:** [X1/X1P user manual](https://www.fanvil.com/Uploads/Temp/download/20201109/5fa90afc7ca32.pdf) · [Fanvil FAQ](https://www.fanvil.com/Support/index.html) · [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html) · [Fanvil support](https://www.fanvil.com/Support/ticket.html) · [X1/X1P firmware](https://www.fanvil.com/Support/download/id/89.html)
