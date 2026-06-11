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

*Part 3 of 3 — see also: [Part 1](sip-phone-and-device-configuration-with-telnyx--part-1.md), [Part 2](sip-phone-and-device-configuration-with-telnyx--part-2.md)*

A consolidated guide for configuring SIP endpoints from multiple manufacturers—including Algo, Panasonic, FortiFone, Flyingvoice, Fanvil, Positron, Gigaset, Snom, AudioCodes, Konftel, Vtech, Mitel, Alcatel, and BuddyTalk—to register with Telnyx's SIP infrastructure. Covers common prerequisites, the shared SIP parameter set, device-specific web portal navigation, TLS/SRTP encryption, codec selection, and troubleshooting.

## Enabling TLS/SRTP Encryption

TLS encrypts SIP signaling; SRTP encrypts the media (audio) stream. Both are recommended for secure communication.

**On the Telnyx side:** Enable SIP-TLS on your SIP account in the Mission Control Portal before configuring the device.

**On the device side:**

1. Set the **Transport Protocol** to `TLS` (instead of UDP or TCP).
2. Change the SIP server/proxy **Port** to `5061`.
3. Enable **SRTP** / **RTP Encryption** / **Secure RTP** (naming varies by device) and set it to mandatory or compulsory mode.
4. Some devices (e.g., AudioCodes 400HD, Snom D7xx, Mitel 6800/6900) require you to upload TLS certificates.

> **Algo 8301 users:** You must manually install a client certificate named `sipclient.pem` (containing the device certificate and private key) in the `certs` folder via **Advanced Settings → File Manager**. Future firmware releases may support `.crt`, `.cer`, and `.der` extensions.

## Configuring Audio Codecs

After SIP registration is configured, set your preferred codecs. Not all devices expose codec settings in the same place, but the principle is the same: enable the codecs Telnyx supports (G.711 u-law, G.711 A-law, G.722, G.729) and disable all others.

On devices like the Panasonic KX-HDV, Snom C520/D7xx, AudioCodes 400HD, and Vtech VCS754, codecs are configured in an explicit **Audio** or **Media Streaming** section. On others (Algo 8xxx), the G.722 codec is toggled separately in the **Features** tab.

## Verifying SIP Registration

After configuration, confirm your device is successfully registered:

- **Algo 8xxx:** **Status → Device Status** — each extension should show *Successful*.
- **Panasonic KX-HDV:** **Status → VoIP Status**.
- **Snom M100 KLE:** **Status** tab — account should show *Registered*.
- **Konftel 300IPx:** **Status → SIP**.
- **Fanvil X4G:** Refresh the web portal page; the account should show as registered.
- **BuddyTalk:** The phone icon in the upper-left turns green; the device LED transitions from red to green to off.
- **Most devices:** If you can make and receive a test call, registration is successful.

## Troubleshooting

### SIP Registration Status: "Rejected by Server"

The server received the request but did not authorize it.

1. **Credentials:** Double-check your SIP account username, authentication ID, and password (including case). Ensure your browser is not auto-filling incorrect values.
2. **Transport mismatch:** Verify the transport protocol on the device matches what is configured on your Telnyx SIP account (e.g., TLS on one side but not the other will cause rejection).
3. **Address/port:** Check the system log for `500 Internal Server error`, which may indicate an incorrect server address or port.

### SIP Registration Status: "No Reply from Server"

The device cannot communicate with the SIP server.

1. **Internet connection:** Ensure your network is up and stable.
2. **SIP Domain:** Verify that **SIP Domain (Proxy Server)** is entered correctly as `sip.telnyx.com`.
3. **Firewall:** Your firewall may be blocking incoming SIP packets from the server. Open the appropriate port (5060/5061).

### No IP Address Displayed on Phone

- Ensure the phone is connected to the network and a DHCP server is available.
- Try re-registering the handset (e.g., Panasonic KX-TGP 550) or rebooting the device.

### Browser Auto-Fill Overwriting Passwords

When entering SIP credentials in a device's web portal, disable browser auto-fill to prevent it from overwriting the password field with saved credentials.
