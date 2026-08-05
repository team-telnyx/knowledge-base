---
title: Telnyx Voice, Fax, and STIR/SHAKEN Configuration Reference
summary: A consolidated reference covering Cisco SPA112/122 ATA setup with Telnyx,
  fax service configuration via T.38 or G711, Fax API error codes, STUN/TURN server
  usage, STIR/SHAKEN attestation and verstat parameters, the Robocall Mitigation Database,
  and Noise Suppression configuration for SIP trunks.
sources:
- url: https://support.telnyx.com/en/articles/1130665-configuring-your-cisco-spa112-122-ata
- url: https://support.telnyx.com/en/articles/1130672-fax-service-with-telnyx-via-t-38-or-g711
- url: https://support.telnyx.com/en/articles/1130682-telnyx-stun-and-turn-server
- url: https://support.telnyx.com/en/articles/4967498-fax-api-error-list
- url: https://support.telnyx.com/en/articles/5402969-stir-shaken-with-telnyx
- url: https://support.telnyx.com/en/articles/5544430-robocall-mitigation-database
- url: https://support.telnyx.com/en/articles/5761463-canadian-stir-shaken-implementation-faqs
- url: https://support.telnyx.com/en/articles/7421223-shaken-stir-parameters
- url: https://support.telnyx.com/en/articles/9260287-key-configuration-notes-for-noise-suppression
- url: https://support.telnyx.com/en/collections/3968239-telnyx-fax-configuration-errors
updated_at: 2026-08-05T13:30:57Z
---

# Telnyx Voice, Fax, and STIR/SHAKEN Configuration Reference

*Part 1 of 3 — see also: [Part 2](telnyx-voice-fax-and-stir-shaken-configuration-reference--part-2.md), [Part 3](telnyx-voice-fax-and-stir-shaken-configuration-reference--part-3.md)*

A consolidated reference covering Cisco SPA112/122 ATA setup with Telnyx, fax service configuration via T.38 or G711, Fax API error codes, STUN/TURN server usage, STIR/SHAKEN attestation and verstat parameters, the Robocall Mitigation Database, and Noise Suppression configuration for SIP trunks.

## Cisco SPA112/122 ATA Configuration

The Cisco SPA112 and SPA122 are compact broadband ATAs compatible with international voice and data standards, historically popular for small-business VoIP. Note that Cisco announced end-of-life for these products in 2019; basic customer support continues until 2025, with the last service contract renewal scheduled for 2024. See [Cisco's SPA end-of-life documentation](https://www.cisco.com/c/en/us/products/collateral/unified-communications/small-business-voice-gateways-ata/eos-eol-notice-c51-743206.html) for details. Firefox has known issues with the device configuration UI; use Chrome or IE instead.

### Prerequisites

- Apply the latest firmware: [SPA112](https://software.cisco.com/download/home/283998771/type) and [SPA122](https://software.cisco.com/download/home/283998793/type).
- Have a number in your Telnyx account.
- Have configured a connection and assigned the number to it.
- Have configured an outbound profile and assigned the connection to it.

### Accessing the Configuration Utility

1. Connect the device to your network through your router.
2. Open a browser and enter `192.168.0.1` (or `192.168.1.1`) to access the router.
3. Log in with your router credentials (change defaults if still in use).
4. Find the connected devices list and locate the entry containing "SPA112" or "SPA122".
5. Click the device's IP address to open the Cisco Phone Adapter Configuration Utility. For the SPA122, if one address does not load the utility correctly, try the other.
6. Log in with the default credentials (`admin` / `admin`) and change them immediately.

### Telnyx Mission Control Portal Settings

On the connection's **Inbound** tab, set **Number Format (DNIS)** to **SIP Username**. Because Telnyx does not support phone numbers as connection usernames, configure inbound calls to be sent to the alphanumeric username of the connection so they reach the ATA through the trunk username.

### Cisco SPA SIP and Quick Setup Settings

On the **Voice → SIP** sub-tab:

- STUN enable: Yes
- STUN server: `stun.telnyx.com`
- STUN test enable: Yes

On the **Quick Setup** tab:

- Proxy: `sip.telnyx.com`
- Display Name: your DID (e.g., `12245181471`). Some firmware versions send the Display Name as the registration username; if registration fails, clear the Display Name and configure a caller ID override on the connection's outbound settings.
- User ID: the connection username from the portal
- Password: the connection password from the portal
- Dial Plan: see the [Dial Plan for Linksys ATAs](dial-plan-for-linksys-atas.md) reference

### Voice Line Configuration

On **Voice → Line 1**:

- Line Enable: yes
- NAT Mapping Enable: yes (if NAT is in use)
- NAT Keep Alive Enable: yes (if NAT is in use)
- SIP Port: 5060
- For T.38 fax, set Fax Enable T38: yes
- Proxy: `sip.telnyx.com`
- Register Expires: 300
- Proxy Fallback Intvl: 300
- Register: yes
- Use DNS SRV: no
- DNS SRV Auto Prefix: no

### Subscriber Information and Codecs

Verify the **User ID** and **Password** match your SIP credentials. The preferred codecs are `g711u` or `g729`. Confirm the dial plan matches the one set in Quick Setup.

### Optional Audio Optimization

Cisco defaults (SIP T1 = 0.5 sec, RTP packet size 0.030) can cause retransmissions on high-latency links. To improve audio:

- SIP T1: 1
- RTP Packet Size: 0.02
- RTP Port Min: 10000
- RTP Port Max: 20000

### Optional TLS Encryption

1. Confirm the device is on the latest firmware via the **Status** tab.
2. On **Voice → Line 1**, set Secure Call Setting: yes.
3. Set SIP Transport: TLS and SIP Port: 5061.
4. Import a CA certificate: on the left menu, click **Provisions**, then set Custom CA URL to `https://crt.sh/?id=1199354`.
5. Submit; the device will reboot to enable TLS.

During secure calls, periodic beeps are heard. To disable the notification, clear the **Secure Call Indication Tone** field under **Voice → Regional → Call Progress Tones**. To re-enable, repopulate with `397@-19,507@-19;15(0/2/0,.2/.1/1,.1/2.1/2)`.

## Telnyx STUN and TURN Servers

Telnyx provides STUN and TURN servers to help VoIP devices traverse NAT and establish reliable media paths.

- **STUN server:** `stun.telnyx.com:3478` — enables devices behind NAT to discover their public IP and port for direct connections, reducing latency and improving call quality.
- **TURN server:** `turn.telnyx.com:3478` — relays media when a direct connection is not possible. Username and password are available from Telnyx support.

For background on NAT and VoIP, see Telnyx's resource on the [dangers of NAT and VoIP](https://telnyx.com/resources/dangers-network-address-translation-nat-voip).

## Fax Service with Telnyx (T.38 or G711)

### Outbound Fax Setup

1. Create a SIP Connection: **SIP Connections → Add SIP Connection**, choose User/Pass or IP authentication, and submit.
2. Create an Outbound Profile: **Outbound → +ADD OUTBOUND PROFILE**, name it, select the connection, and add.

By default, Telnyx sends a T.38 re-INVITE when fax tone is detected. To change this, edit the connection's outbound settings and adjust **T.38 Re-invite Initiated By** to Telnyx (default), Customer, or Disabled (which enables G711 fax calls).

### Inbound Fax Setup

1. Create a SIP Connection under **Connections → ADD CONNECTION**.
2. Purchase a number under **Numbers → Search Numbers** and check out.
3. Assign the connection to the number under **Numbers → My Numbers** using the Connection drop-down.

By default, Telnyx expects the customer to send a T.38 re-INVITE; if none is received, the fax continues with G711. To force T.38, open **Advanced Options** (gear icon) next to the number, expand **Expert Configuration**, and enable **Enable T.38 Fax Gateway**.

### Fax Machine Settings

Optimize a physical fax machine connected via an ATA with these settings:

- Set baud rate to 9600 or below (sometimes labeled "transmission speed", "compatibility mode", or "VoIP mode").
- Disable Error Correction Mode (ECM) to avoid retransmits caused by normal packet loss, jitter, and latency.
- Set fax resolution to "normal" rather than high/fine/ultra-fine.
- Disable dial tone detection if the machine fails to dial outbound.

Note: SRTP encryption is not supported when T.38 is enabled.
