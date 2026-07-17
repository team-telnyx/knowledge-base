---
title: Telnyx Platform Overview and Grandstream Device Setup
summary: Telnyx is a global Communications Platform as a Service (CPaaS) provider
  offering voice, messaging, WebRTC, Elastic SIP Trunking, AI Inference, Storage,
  and Flow workflow automation over a privately owned IP network. This page consolidates
  Telnyx's product suite, network and partner details, hardware compatibility, encryption
  and STUN/TURN configuration, reseller program, and step-by-step setup guides for
  Grandstream GXP16XX, GXP, GXP21XX, and HT802 devices.
sources:
- url: https://support.telnyx.com/en/articles/1130599-telnyx-tech-specs
- url: https://support.telnyx.com/en/articles/1130637-what-is-telnyx
- url: https://support.telnyx.com/en/articles/1130638-does-telnyx-provide-any-hardware
- url: https://support.telnyx.com/en/articles/1130641-telnyx-recommended-hardware-configurations
- url: https://support.telnyx.com/en/articles/1130646-where-is-telnyx-located
- url: https://support.telnyx.com/en/articles/1130655-can-i-resell-your-services
- url: https://support.telnyx.com/en/articles/1130660-configuring-grandstream-gxp16xx-with-telnyx
- url: https://support.telnyx.com/en/articles/1130682-telnyx-stun-and-turn-server
- url: https://support.telnyx.com/en/articles/1130692-does-telnyx-have-a-blog
- url: https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication
- url: https://support.telnyx.com/en/articles/5725071-grandstream-ht802-telnyx-setup
- url: https://support.telnyx.com/en/articles/5815720-grandstream-gxp-telnyx-setup
- url: https://support.telnyx.com/en/articles/5819218-grandstream-gxp21xx
updated_at: 2026-07-17T09:01:55Z
---

# Telnyx Platform Overview and Grandstream Device Setup

*Part 2 of 3 — see also: [Part 1](telnyx-platform-overview-and-grandstream-device-setup--part-1.md), [Part 3](telnyx-platform-overview-and-grandstream-device-setup--part-3.md)*

Telnyx is a global Communications Platform as a Service (CPaaS) provider offering voice, messaging, WebRTC, Elastic SIP Trunking, AI Inference, Storage, and Flow workflow automation over a privately owned IP network. This page consolidates Telnyx's product suite, network and partner details, hardware compatibility, encryption and STUN/TURN configuration, reseller program, and step-by-step setup guides for Grandstream GXP16XX, GXP, GXP21XX, and HT802 devices.

## Grandstream Device Configuration

The following sections describe how to configure common Grandstream devices with Telnyx. In all cases, ensure your Telnyx Mission Control Portal is configured properly, your device is running the latest firmware, and TLS encryption is enabled where supported.

### Grandstream GXP16XX (GXP1620/GXP1625/GXP1630)

The GXP1620/GXP1625 is geared toward small to mid-sized businesses with light to medium call volume. The GXP1630 is the most powerful entry-level Basic IP phone, supporting 3 SIP accounts, 3 line keys, 4-way conferencing, HD audio, dual-switched Gigabit ports with PoE, 8 BLF/speed dial keys, EHS support for Plantronics headsets, and up to 1000 contacts.

**Configuration steps:**

1. **Log into the Grandstream web UI** by browsing to the device's IP address. Default credentials are `admin` / `admin` (units manufactured after January 2017 have a unique random password on the back sticker).
2. **Create a SIP trunk** under Accounts → Account 1 → General Settings:
   - **SIP Server:** `sip.telnyx.com`
   - **Outbound Proxy:** `sip.telnyx.com`
   - **SIP User ID:** Your Telnyx SIP account username
   - **Authenticate ID:** Your Telnyx SIP account password
3. **Configure Network Settings** under Accounts → Account 1 → Network Settings:
   - **DNS Mode:** A Record
   - **NAT Traversal:** Keep-Alive
4. **Configure SIP Settings** under Accounts → Account 1 → SIP Settings → Basic Settings:
   - **Local SIP Port:** 5060 (or 5061 if TLS is enabled)
   - **SIP Transport:** UDP or TCP (or TLS/TCP if TLS is enabled)
5. **Configure codec preferences** under Accounts → Account 1 → Audio Settings. Supported codecs include ulaw (g711u), alaw (g711a), g722, and g729.

**Troubleshooting outgoing call failures ("No response"):**

1. Under Accounts → Account X → SIP → Custom SIP Header, disable **Use X-Grandstream-PBX Header**, **Use P-Access-Network-Info Header**, and **Use P-Emergency-Info Header**.
2. Under Accounts → Account X → SIP → Audio Settings, set the preferred Vocoder to G729A/B and the rest to PCMU.

### Grandstream GXP (GXP1630/GXP2135)

The GXP2135 is designed for busy users managing medium to heavy call volumes, with 8 lines, 4 SIP accounts, a 2.8-inch color LCD, 32 digital speed dial/BLF keys, dual Gigabit PoE ports, built-in Bluetooth, HD audio, EHS support for Plantronics headsets, and 4-way audio conferencing. Both phones support SRTP and TLS encryption.

**Configuration steps:**

1. **Get the device IP address** from Menu → Status → Network Status → IPv4 Address, then browse to `http://<IP>` and log in with default credentials `admin` / `admin`.
2. **Configure the account** under Accounts → Account 1 → General Settings:
   - **Account Name:** A descriptive name
   - **SIP Server:** `sip.telnyx.com`
   - **SIP User ID:** Your Telnyx SIP account username
   - **Authenticate Password:** Your Telnyx SIP account password
   - **Name:** Outbound Caller ID (use capital letters, no special characters, ≤15 characters)
   - **Voice Mail Access Number:** `*97`
3. **Configure SIP Settings** under Accounts → Account 1 → SIP Settings → Basic Settings:
   - **SIP Registration:** Yes
   - **Register Expiration:** 5 (minutes)
   - **Enable OPTIONS Keep Alive:** Yes
   - **Local SIP Port:** 5060 (or 5061 if TLS is enabled)
   - **SIP Transport:** UDP or TCP (or TLS/TCP if TLS is enabled)
4. Click **Save and Apply**.

**Troubleshooting outgoing call failures ("No response"):**

1. Under Accounts → Account X → SIP → Custom SIP Header, disable **Use X-Grandstream-PBX Header**, **Use P-Access-Network-Info Header**, and **Use P-Emergency-Info Header**.
2. Under Accounts → Account X → SIP → Audio Settings, set the preferred Vocoder to G729A/B.

### Grandstream GXP21XX (GXP2135/GXP2170)

The GXP21XX is a high-end IP phone suited for high call volumes, with 12 line keys, a 4.3-inch color LCD, 48 digital on-screen speed dial/BLF keys, dual Gigabit PoE ports, SRTP and TLS encryption, and automated provisioning options including zero-configuration with Grandstream UCM series IP PBXs, encrypted XML files, and TR-069.

**Configuration steps:**

1. **Get the device IP address** from Menu → Status → Network Status → IPv4 Address, then browse to `http://<IP>` and log in with default credentials `admin` / `admin`.
2. **Configure the account** under Accounts → Account 1 → General Settings:
   - **Account Name:** A descriptive name
   - **SIP Server:** `sip.telnyx.com`
   - **SIP User ID:** Your Telnyx SIP account username
   - **Authentication ID:** Your Telnyx SIP account username
   - **Authenticate Password:** Your Telnyx SIP account password
   - **Name:** Outbound Caller ID (capital letters, no special characters, ≤15 characters)
   - **Voice Mail Access Number:** `*97`
3. **Configure SIP Settings** under Accounts → Account 1 → SIP Settings → Basic Settings:
   - **SIP Registration:** Yes
   - **Register Expiration:** 5 (minutes)
   - **Enable OPTIONS Keep Alive:** Yes
   - **Local SIP Port:** 5060 (or 5061 if TLS is enabled)
   - **SIP Transport:** UDP or TCP (or TLS/TCP if TLS is enabled)
4. **Configure Custom SIP Header** under Accounts → Account X → SIP → Custom SIP Header:
   - **Use Privacy Header:** Yes
   - **Use P-Preferred-Identity Header:** Yes
   - **Use X-Grandstream-PBX Header:** No
   - **Use P-Access-Network-Info Header:** No
   - **Use P-Emergency-Info Header:** No
5. **Configure Audio Settings** under Accounts → Account X → SIP → Audio Settings, choosing G729A/B or G722 as the preferred Vocoder.
6. Click **Save and Apply**.

**Troubleshooting outgoing call failures ("No response"):**

1. Under Accounts → Account X → SIP → Custom SIP Header, disable **Use X-Grandstream-PBX Header**, **Use P-Access-Network-Info Header**, and **Use P-Emergency-Info Header**.
2. Under Accounts → Account X → SIP → Audio Settings, set the preferred Vocoder to G729A/B and the rest to PCMU.

### Grandstream HT802 (Analog Telephone Adapter)

The HT802 is a 2-port analog telephone adapter (ATA) that enables IP telephony on analog phones for residential and office environments. It supports T.38 fax mode and is commonly used to send and receive faxes through Telnyx.

**Pre-requisites:**

- Ensure the device is running the most current firmware (1.0.33.4 or later).
- In the Telnyx Portal under Connection Settings → Inbound, set **DNIS** to *SIP Username* (Telnyx does not support phone numbers as connection usernames).

**Configuration steps:**

1. **Set up the device:**
   - Connect the HT802 to your router via Ethernet.
   - Connect a phone to the configured FXS port.
   - Plug in the power cord and wait 60 seconds.
   - Pick up the connected phone and dial `***`, then `02` to hear the device's IP address.
   - Open a browser to that IP address (remove leading zeros) and log in with the default password `admin`.
2. **Configure FXS PORT1** with the following settings:
   - **Primary SIP server:** `sip.telnyx.com`
   - **Failover SIP server:** Leave blank
   - **Outbound Proxy:** Leave blank (or `sip.telnyx.com` on firmware 1.0.15.4 or lower)
   - **NAT Traversal:** Keep-Alive
   - **SIP User ID:** Your Telnyx SIP ID
   - **Authenticate ID:** Your Telnyx SIP ID
   - **Authenticate Password:** Your Telnyx SIP account password
   - **Name:** Outbound Caller ID (no special characters, ≤15 characters, capital letters recommended)
   - **DNS Mode:** A Record
   - **SIP Registration:** Yes
   - **Unregister on Reboot:** No
   - **Outgoing Call Without Registration:** Yes
   - **Register Expiration:** 5
   - **Allow Incoming SIP Messages from SIP Proxy Only:** Yes
   - **Preferred DTMF method:** In-audio, RFC2833
   - **Use P-Access-Network-Info Header:** No
   - **Use P-Emergency-info Header:** No
   - **Enable Call Features:** No
   - **Dial Plan:** `{[x*]+}`
   - **Preferred Vocoder:** PCMU, PCMA, G72
   - **Fax Mode:** T38
   - **Re-INVITE After Fax Tone Detected:** Disabled
3. **Optional — Prevent direct IP calls:**
   - **Check SIP User ID for Incoming INVITE:** Yes
   - **Allow Incoming SIP Messages from SIP Proxy Only:** Yes
4. **Configure the Telnyx Command Portal** by setting up a Number, Connection, and Outbound Profile, then send a test fax.

**Optional fax reliability settings** (if large faxes have a low success rate):

- **Jitter Buffer Type:** Fixed
- **Jitter Buffer Length:** High
- **Disable Line Echo Canceller (LEC):** Yes
- **Disable Network Echo Suppressor:** Yes
