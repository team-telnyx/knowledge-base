---
title: Telnyx SIP Trunking Configuration
summary: A comprehensive guide to configuring and managing SIP trunking with Telnyx,
  covering connection types, authentication methods, inbound/outbound settings, failover
  and retry logic, SRV record handling, number formats, SIP protocols, STUN/TURN servers,
  SIP URI calling, response codes, and advanced features such as SHAKEN/STIR, PRACK,
  and Record-Route headers.
sources:
- url: https://support.telnyx.com/en/articles/10666839-how-telnyx-handles-srv-records-for-sip-calls
  content_hash: 5336b5985fa0913e7af2de79105b8bbbc1f3cbb846981d704a7ff0224d8a61aa
- url: https://support.telnyx.com/en/articles/1130682-telnyx-stun-and-turn-server
  content_hash: ba7ff5ec0ec7e77fd1c8912a6804912e1470dbc9bc937fd3b8d6558c2d8fb90b
- url: https://support.telnyx.com/en/articles/1130705-sip-protocols-that-telnyx-uses
  content_hash: 46cc3f3d1bcbc1eca17597a21e7696d3b43edc8dee1e78f5b051c30ee339c516
- url: https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats
  content_hash: ef78abc67f49329534f7f4ada45772b5ab64bd91ac90625c16b047ab548f9fa6
- url: https://support.telnyx.com/en/articles/1130715-register-multiple-devices-on-one-connection
  content_hash: 6e5e7522f82c82f4e181a1d36ef99eb765ba03f0b6911e5b6bff44e80f4a84a0
- url: https://support.telnyx.com/en/articles/1130717-limits-on-concurrent-outbound-calls
  content_hash: 5922c4b3028b0d7fd9850e5cfd442f62ebe0e2557b35bde4290290f7759aeb90
- url: https://support.telnyx.com/en/articles/11358700-what-is-the-u-s-reassigned-numbers-database
  content_hash: 330252b32ac1fb45a47251b787e1bc0544cb49b895132f43194e7468710374bb
- url: https://support.telnyx.com/en/articles/1176364-sip-connection-failover-guide-ip-fqdn-based
  content_hash: b6ad5a6fbf819ec53aa61ad285c4320f020e9b60e9841c08c1a7583284fd3994
- url: https://support.telnyx.com/en/articles/2602782-ip-authentication-with-tech-prefix
  content_hash: 64dda14685cddc1fcb163aaa34f9f7d32e88737d67bd655691779e914542affb
- url: https://support.telnyx.com/en/articles/2925713-sip-uri-calling
  content_hash: 3cb9214746855254d83c27a4e329fbecf530bb91d79cda3d10bf43ba6f011ff7
- url: https://support.telnyx.com/en/articles/4245868-sip-connection-types
  content_hash: 121f24b961c0971bf305ae76944014f708745fe2ac15f08670909000bc4908eb
- url: https://support.telnyx.com/en/articles/4304898-sip-trunking-methods-requests-responses
  content_hash: e16cf3db090ad672d0669dc9c568db73a6dddc9d007b64b29a7b70d9edb922d4
- url: https://support.telnyx.com/en/articles/4320364-sip-connection-fail-over-and-retries
  content_hash: 36988aa18169e77583bc8d547d59584dddf444027ca86e1ffcb71ff4829349f4
- url: https://support.telnyx.com/en/articles/4351104-sip-connection-settings
  content_hash: 0b31f4e550f422c6fc2ea735848b1e17bb39b55248fd5718a784c214a0a03071
- url: https://support.telnyx.com/en/articles/4363904-sip-registration
  content_hash: 405244c50457a2e39cfe8e60b1db43961179f4bbc3028609415ef8c5eb0b498e
- url: https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings
  content_hash: 13555768a2d461956c3844d32092859b8fef4a0134829a70ca40ceffb478513e
- url: https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes
  content_hash: 51d1300c62f3c37573b8043d8169495ff6dec4168a2fa26a1fa421b37b517e20
- url: https://support.telnyx.com/en/articles/4860170-ip-authentication-with-x-telnyx-token
  content_hash: e5e100fcae875b6de79eb0856aa249445b813d50d3ccfdc70811011ad0f4a8da
- url: https://support.telnyx.com/en/articles/6169513-grandstream-grp260x-sip-trunk
  content_hash: ee2ab10a3b5059edd8c19cb6ca4c4e81c8cb94a40cf9a220b9a0ca41028ccb2f
- url: https://support.telnyx.com/en/articles/6902981-understanding-sip-prack-protocol
  content_hash: bb7aacbe5432b5ccb06087b93b7a52de14bdf49dc306bfecad67330620bd917f
- url: https://support.telnyx.com/en/articles/7029684-telephony-credentials-types
  content_hash: c3560f0e76972b8af4a3004d3ac523645b3b6e3798b3165ae14e029445c33b9d
- url: https://support.telnyx.com/en/articles/7421223-shaken-stir-parameters
  content_hash: c046bb41d844fe4c70629bd7afd01ab5819661455fb182a876a212d5a2607585
- url: https://support.telnyx.com/en/articles/8096455-how-to-configure-a-sip-trunk
  content_hash: 4440cdca8094dd344bcd02ba9cb8d2ded23ed9100c2aca3e64653cde9cfa27cc
- url: https://support.telnyx.com/en/articles/9133298-sip-record-route-headers
  content_hash: 81dfd46b008a8cd6c4683c97567afe552e35a2af269cd81a96901b3f0e0607f6
updated_at: 2026-06-11T11:25:41Z
---

# Telnyx SIP Trunking Configuration

*Part 1 of 4 — see also: [Part 2](telnyx-sip-trunking-configuration--part-2.md), [Part 3](telnyx-sip-trunking-configuration--part-3.md), [Part 4](telnyx-sip-trunking-configuration--part-4.md)*

A comprehensive guide to configuring and managing SIP trunking with Telnyx, covering connection types, authentication methods, inbound/outbound settings, failover and retry logic, SRV record handling, number formats, SIP protocols, STUN/TURN servers, SIP URI calling, response codes, and advanced features such as SHAKEN/STIR, PRACK, and Record-Route headers.

## SIP Connection Types

Telnyx offers three primary SIP Connection types, each suited to different network environments:

- **Credentials-based** — Use when your system has a dynamic public IP address. A username and password are generated automatically (editable in the Authentication & Routing section). It is highly recommended to choose a strong password of 12–16+ characters with mixed complexity.
- **IP Address-based** — Use when you have a static public IP address. Enter the IP and port in the connection settings. Multiple IPs can be added with Sequential or Round Robin routing. If your IP changes, calls will fail.
- **FQDN-based** — Uses a Fully Qualified Domain Name for inbound routing. Choose an FQDN type (typically A record) and enter the domain. For outbound, select either Credentials or IP Address authentication. Multiple FQDNs and IPs can be assigned with configurable routing priority.

Each SIP Connection receives a universally unique identifier (connection ID), visible below the settings sub-tab, used for API interactions. Connections can be deactivated via the status toggle on the SIP Connections page, which stops all inbound and outbound call processing.

## Authentication Methods

Beyond the three connection types, Telnyx supports advanced authentication methods for IP-based connections that share a single IP address across multiple connections:

### Tech Prefix

A 4-digit number prefixed to the dialed number (e.g., tech prefix `1234` + number `18005678912` → dial `123418005678912`). Your PBX can auto-prepend this. Without the tech prefix, calls receive a **SIP 407 Proxy Authentication** response. Tech prefixes can also be applied at the number level for granular routing control.

### X-Telnyx-Token

A custom string sent in the `X-Telnyx-Token` SIP header. The token must:
- Contain only alphanumeric characters and dashes (`-`)
- Be 12–48 characters long
- Be globally unique

The portal suggests a randomly generated token based on the connection name, but you can use a custom string. The SIP INVITE must originate from an IP associated with the connection.

### P-Charge-Info

A telephone number associated with the connection must be sent in the `P-Charge-Info` SIP header on the INVITE message.

These methods prevent the "Termination Endpoint" error that occurs when multiple connections share the same IP but lack unique identification.

## SIP Connection Settings

SIP Connection settings are organized into five categories: Authentication & Routing Configuration, Webhooks, AnchorSite®, Advanced Settings, and RTCP Settings.

### Webhooks

Webhook settings send connection events (Call Initiated, Call Answered, Call Bridged, Call Hangup, Call Voicemail Completed) to a specified URL, with a Failover URL as backup. Three API versions are available:

- **API V1** — No longer recommended.
- **API V2** — Recommended; JSON payloads over HTTP.
- **TeXML** — Fetches XML instructions from the webhook URL; form-data over HTTP.

**Important:** Setting a webhook URL treats the call as programmable voice rather than SIP trunking. This may anchor media in a region that doesn't support programmable voice (e.g., Australia). For notification-only use cases, consider removing the webhook URL. A Voice API application must be associated with numbers to issue call control commands.

#### Park Outbound Calls

When enabled, outbound calls are parked (generating SIP 180 Ringing to the caller) while awaiting Voice API commands (answer, play audio, bridge, transfer). The typical use case involves WebRTC clients registering with credential-based connections, where a backend application issues dial and bridge commands after the caller is parked.

### AnchorSite®

Controls which media server anchors your calls. The default, **Latency**, proactively monitors latency from your endpoints to Telnyx PoPs. To ensure proper latency detection, whitelist Telnyx's [media IP addresses](https://sip.telnyx.com/#media). For credential-based connections, include the SIP Connection **username** in the contact header of your first INVITE so the SIP Proxy can identify your connection and apply the correct AnchorSite.

### Advanced Settings

- **Encode Contact Header** — Encodes the SIP contact header to avoid NAT/ALG issues.
- **DTMF Types** — RFC 2833 (recommended), Inband (most prone to issues), or SIP Info (out-of-band).
- **Enable On-Net T.38 Passthrough** — Allows sender and receiver to negotiate T.38 directly.
- **Enable Comfort Noise for Call on Hold** — Generates comfort noise on hold; if unchecked, you must generate your own noise or music to avoid RTP timeouts.

### RTCP Settings

- **RTCP+1** (default) — Uses the next port after RTP.
- **RTCP mux** — Multiplexes RTP and RTCP through a single UDP port, simplifying NAT traversal.
- **Report Frequency** — Interval in seconds between RTCP packets.
- **RTCP Capture and Storage** — Enables RTCP reporting when checked.

## Inbound SIP Settings

| Setting | Description |
|---|---|
| Number Format (DNIS/ANI) | Controls the number format in FROM/TO and INVITE URI. See [Telnyx SIP Trunking Configuration#Number Formats](telnyx-sip-trunking-configuration-number-formats.md) below. |
| SIP Transport Protocol | Set signalling transport (IP/FQDN/MS Teams auth only). |
| SIP Region | Set the Telnyx region for signalling (IP/FQDN/MS Teams auth only). |
| No Ringback Timeout | How long Telnyx waits for a 180/183 response (default 5s; min 1s, max 2 min). |
| No Answer Timeout | How long Telnyx waits for a 200 OK (default 5s; min 1s, max 10 min). |
| SIP Subdomain | Allows calls to a defined subdomain (e.g., `client123.sip.telnyx.com`). |
| Receive SIP Subdomain Calls | Allow from anyone (public) or only from your connections. |
| Channel Limit | Max concurrent inbound calls (default: unlimited). |
| Receive SIP URI Calls | Credential connections only — allow from anyone, only your connections, or disabled. |
| Encrypted Media | Enables SRTP media encryption on inbound. |
| Default Ringback Setting | Relays messages/early media from called party to PSTN carrier. |
| Generate Ringback Tone (183) | Sends instant 183 with SDP and US ringback tone; stops if called party sends early media. |
| Enable Instant Ringback (180) | Sends instant 180 Ringing; carrier generates ringback. |
| Offered Audio/Video Codecs | Select and order preferred codecs. |
| Enable SIP Compact Headers | Reduces bandwidth by compacting SIP headers. |
| Enable Prack | Enables acknowledgment of provisional 1xx responses. |
| Receive ISUP Headers into SIP Headers | Converts SS7 ISUP body content into SIP headers. |
| Enable Shaken/Stir Header | Includes attestation information in webhooks. |
| Enable 3rd Party Call Control | For Cisco UCM; handles late media negotiation (INVITE without SDP). |
| Enable Simultaneous Ringing | Multiple SIP devices under the same credentials ring simultaneously. |

## Outbound SIP Settings

| Setting | Description |
|---|---|
| Outbound Voice Profile | Associate an outbound voice profile with the connection. |
| Localization Country | Dial with local exit codes and local number formats without +country code. Without a country, numbers are validated as US. |
| Channel Limit for Outbound Calls | Max concurrent outbound calls; excess receives 403. |
| Caller ID Override | Override caller ID always, for normal calls, or for emergency calls only. |
| T.38 Re-invite Initiated By | Set to Telnyx (default), Customer, or Disabled for fax. |
| Encrypted Media | Expects SRTP crypto attributes on outbound INVITEs. |
| Default Ringback Settings | Passes 18x/early media from PSTN carrier to caller. |
| Enable Instant Ringback (180) | Sends instant 180; caller generates ringback. |
| Generate Ringback Tone (183) | Sends 183 with SDP and US ringback tone. |
