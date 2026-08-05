---
title: Configuring Grandstream IP Phones with Telnyx
summary: Step-by-step instructions for configuring Grandstream GXP16XX, GXP21XX, GXP1700,
  GRP260x, and GRP2612 series IP phones to register as SIP endpoints against a Telnyx
  Mission Control account, including account, network, SIP, and audio settings plus
  troubleshooting for common one-way audio and failed-call issues.
sources:
- url: https://support.telnyx.com/en/articles/1130660-configuring-grandstream-gxp16xx-with-telnyx
- url: https://support.telnyx.com/en/articles/5815720-grandstream-gxp-telnyx-setup
- url: https://support.telnyx.com/en/articles/5819218-grandstream-gxp21xx
- url: https://support.telnyx.com/en/articles/6169513-grandstream-grp260x-sip-trunk
- url: https://support.telnyx.com/en/articles/6184147-grandstream-grp2612-sip-trunk
- url: https://support.telnyx.com/en/articles/6184520-grandstream-gxp1700-sip-trunk
updated_at: 2026-08-05T13:30:50Z
---

# Configuring Grandstream IP Phones with Telnyx

*Part 2 of 3 — see also: [Part 1](configuring-grandstream-ip-phones-with-telnyx--part-1.md), [Part 3](configuring-grandstream-ip-phones-with-telnyx--part-3.md)*

Step-by-step instructions for configuring Grandstream GXP16XX, GXP21XX, GXP1700, GRP260x, and GRP2612 series IP phones to register as SIP endpoints against a Telnyx Mission Control account, including account, network, SIP, and audio settings plus troubleshooting for common one-way audio and failed-call issues.

## Configuring the GXP1700 Series (GXP1760W, GXP1780/1782)

The [GXP1760W](https://www.grandstream.com/products/ip-voice-telephony-gxp-series-ip-phones/gxp-series-mid-range-ip-phones/product/gxp1760w) is a mid-range IP phone with 6 lines, 3 SIP accounts, integrated dual-band Wi-Fi, and dual 10/100 Mbps network ports. The [GXP1780/1782](https://www.grandstream.com/products/ip-voice-telephony-gxp-series-ip-phones/gxp-series-mid-range-ip-phones/product/gxp1780) adds 8 lines, 4 SIP accounts, Gigabit ports on the GXP1782, and a Kensington Security Slot.

### Account → General Settings

- **Account Active:** `Yes`
- **Account Name:** Descriptive name shown on the LCD
- **SIP Server:** `sip.telnyx.com` (US; international users see the [signaling addresses table](https://sip.telnyx.com/#signaling-addresses))
- **Secondary SIP Server:** `64.16.250.10` (US; international users see the [signaling addresses table](https://sip.telnyx.com/#signaling-addresses))
- **Outbound Proxy:** `sip.telnyx.com`
- **SIP User ID:** SIP connection username (see [SIP connection types](https://support.telnyx.com/en/articles/4245868-sip-connection-types))
- **Authenticate ID:** SIP connection username
- **Authenticate Password:** SIP connection password
- **Name:** Caller ID (capital letters, no special characters, ≤15 characters for some Canadian carriers)
- **Rule / Type:** Dial plan rule and type (`pattern`, `block`, `dial now`, `prefix`, or `second tone`)
- **Fallback Expiration:** Minutes before failback attempts to the primary SIP server

### Account → Network Settings

- **DNS Mode:** `A Record` (default), `SRV`, `NATPTR/SRV`, or `Use Configured IP`. If `Use Configured IP` is selected, populate **Primary IP**, **Backup IP 1**, and **Backup IP 2**. The phone tries Primary IP first, switches to Backup IP after 3 failed attempts, and reverts to Primary IP after 3 more retries.

### Account → SIP Settings → Basic Settings

- **SIP Registration:** Enabled (so the phone sends SIP Register messages)
- **Local SIP Port:** `5060` (UDP) or `5061` (TLS/TCP)
- **SIP Transport:** `UDP` (default) or `TLS/TCP` if encryption is enabled in the Telnyx portal
- **SIP Listening Mode:** `Transport Only` (default), `Dual`, `Dual (Secured)`, or `Dual (BLF Enforced)`

### Audio and STUN settings

In **Account → Audio Settings**, set **Preferred Vocoder** to one of the Telnyx-supported codecs:

- `ulaw (g711u)`
- `alaw (g711a)`
- `g722`
- `g729` (firmware 1.0.0.43+ supports concurrent G.729 calls)

In **Settings → General Settings**, set **STUN Server** to `stun.telnyx.com:3478`.

Verify registration on the **Status** page.

## Configuring the GRP260x Series

The [Grandstream GRP260x](https://content.grandstream.com/grp260x-introduction-webinar) is a carrier-grade 2-line IP phone with zero-touch provisioning, 5-way voice conferencing, dual-band Wi-Fi on the GRP2602W, EHS support for Plantronics/Jabra/Sennheiser, secure boot, dual firmware images, encrypted data storage, and centralized management via [Grandstream Device Management System (GDMS)](https://www.grandstream.com/products/device-management/gdms/product/gdms).

### Account → General Settings → Account Register

- **Account Active:** `Yes`
- **Account Name:** Descriptive name shown on the LCD
- **SIP Server:** `sip.telnyx.com` (US; international users see the [signaling addresses table](https://sip.telnyx.com/#signaling-addresses))
- **Secondary SIP Server:** `64.16.250.10` (US; international users see the [signaling addresses table](https://sip.telnyx.com/#signaling-addresses))
- **SIP User ID:** SIP connection username
- **SIP Auth ID:** SIP connection username
- **SIP Auth Password:** SIP connection password
- **Name:** Caller ID (capital letters, no special characters, ≤15 characters for some Canadian carriers)
- **Fallback Expiration:** Minutes before failback attempts to the primary SIP server

### Account → General Settings → Network Settings

- **Outbound Proxy:** `sip.telnyx.com`
- **Max number of SIP request replies:** `1`–`10` retries before failover

### Account → SIP Settings → Basic Settings

- **SIP Registration:** Enabled
- **SIP Transport:** `UDP` (default) or `TLS/TCP` if encryption is enabled in the Telnyx portal
- **SIP Listening Mode:** `Transport Only` (default), `Dual`, `Dual (Secured)`, or `Dual (BLF Enforced)`
- **Local SIP Port:** `5060` (UDP) or `5061` (TLS/TCP)

Verify registration on the **Status** page.

## Configuring the GRP2612/GRP2612P/GRP2612W

The [GRP2612/GRP2612P/GRP2612W](https://www.grandstream.com/products/ip-voice-telephony/carrier-grade-ip-phones/grp-series-professional-ip-phones/product/grp2612-p-w-g) series features 4 dual-color line keys (provisionable as up to 16 BLF/fast-dial keys), a 2.4" TFT color LCD, 4 programmable soft keys, 100M network ports, integrated PoE (P/W models), integrated dual-band Wi-Fi (W model), 3-way conferencing, and EHS support. The same configuration flow applies to the GRP261x, GRP262x, and GRP263x families.

### Account → General Settings → Account Register

- **Account Active:** `Yes`
- **Account Name:** Descriptive name shown on the LCD
- **SIP Server:** `sip.telnyx.com` (US; international users see the [signaling addresses table](https://sip.telnyx.com/#signaling-addresses))
- **Secondary SIP Server:** `64.16.250.10` (US; international users see the [signaling addresses table](https://sip.telnyx.com/#signaling-addresses))
- **Outbound Proxy:** `sip.telnyx.com`
- **SIP User ID:** SIP connection username
- **SIP Authentication ID:** SIP connection username
- **SIP Authentication Password:** SIP connection password

### Account → General Settings → Account Dial Plan

- **Name:** Caller ID (capital letters, no special characters, ≤15 characters for some Canadian carriers)
- **Rule:** Dial plan rule (number, pattern, prefix to add, etc.)
- **Type:** `pattern`, `block`, `dial now`, `prefix`, or `second tone`

### Account → General Settings → Network Settings

- **DNS Mode:** `A Record` (default), `SRV`, `NATPTR/SRV`, or `Use Configured IP`. If `Use Configured IP` is selected, populate **Primary IP**, **Backup IP 1**, and **Backup IP 2**. The phone tries Primary IP first, switches to Backup IP after 3 failed attempts, and reverts to Primary IP after 3 more retries.

### Account → SIP Settings → Basic Settings

- **SIP Registration:** Enabled
- **Local SIP Port:** `5060` (UDP) or `5061` (TLS/TCP)
- **SIP Transport:** `UDP` (default) or `TLS/TCP` if encryption is enabled in the Telnyx portal
- **SIP Listening Mode:** `Transport Only` (default), `Dual`, `Dual (Secured)`, or `Dual (BLF Enforced)`

Verify registration on the **Status** page.

## Troubleshooting

### Outgoing calls fail with "No response" while incoming calls work

This is the most common issue across the GXP families. Apply the following:

1. In **Accounts → Account X → SIP → Custom SIP Header**, disable:
   - **Use X-Grandstream-PBX Header**
   - **Use P-Access-Network-Info Header**
   - **Use P-Emergency-Info Header**
2. In **Accounts → Account X → SIP → Audio Settings**, set the preferred Vocoder to `G729A/B` and the remaining codecs to `PCMU`.

### Verify registration

After saving and applying, navigate to the **Status** page on the device to confirm the SIP account is registered. If the account shows "Not Registered", double-check the SIP User ID, Authenticate ID/Authentication ID, and Authenticate/Authentication Password against the credentials in the Telnyx Mission Control Portal.
