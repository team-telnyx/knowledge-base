---
title: SIP Connections
summary: A consolidated reference for configuring Telnyx SIP Connections in the Mission
  Control Portal, covering connection types (Credentials, IP, FQDN, UAC), authentication
  and routing, inbound and outbound settings, number formats, SIP URI calling, AnchorSite®
  media anchoring, webhooks, advanced options, and DID assignment.
sources:
- url: https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats
- url: https://support.telnyx.com/en/articles/1130713-what-is-my-sip-account-connection-password
- url: https://support.telnyx.com/en/articles/1177115-how-to-setup-a-did-to-sip-connection
- url: https://support.telnyx.com/en/articles/14805261-how-to-configure-sip-attach-using-a-uac-connection
- url: https://support.telnyx.com/en/articles/2925713-sip-uri-calling
- url: https://support.telnyx.com/en/articles/4245868-sip-connection-types
- url: https://support.telnyx.com/en/articles/4351104-sip-connection-settings
- url: https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings
- url: https://support.telnyx.com/en/articles/5271423-guide-to-sip-anchorsite-settings
updated_at: 2026-08-05T13:31:54Z
---

# SIP Connections

*Part 3 of 5 — see also: [Part 1](sip-connections--part-1.md), [Part 2](sip-connections--part-2.md), [Part 4](sip-connections--part-4.md), [Part 5](sip-connections--part-5.md)*

A consolidated reference for configuring Telnyx SIP Connections in the Mission Control Portal, covering connection types (Credentials, IP, FQDN, UAC), authentication and routing, inbound and outbound settings, number formats, SIP URI calling, AnchorSite® media anchoring, webhooks, advanced options, and DID assignment.

## Authentication & Routing

The Authentication & Routing Configuration section lets you choose between the connection types described above. For IP-authenticated SIP Connections, Telnyx offers three advanced authentication methods to further secure traffic:

- **Tech Prefix** — a 4-digit prefix that must be appended to the destination number.
- **Token** — a string sent in a custom SIP header `X-Telnyx-Token` on the SIP INVITE.
- **P Charge Info** — a telephone number associated with the connection sent in the `P-Charge-Info` SIP header on the SIP INVITE.

### SIP Account Connection Password

When creating a SIP connection with **credentials** authentication, a random username and password are generated but can be changed. A random password generator is recommended for additional security.

To find your SIP credentials:

1. Log in to the [Telnyx Portal](https://portal.telnyx.com).
2. Navigate to **Voice → SIP Trunking**.
3. Find the SIP connection and click the **pencil (edit) icon**.
4. Open the **Authentication and routing** tab.
5. Your username and password are displayed here; you can view, copy, or update them at any time.

## Inbound Settings

Inbound settings control how Telnyx delivers calls to your SIP Connection.

### Number Format (DNIS / ANI)

This setting controls the number format in the FROM/TO and INVITE URI. It is useful when your system only supports a particular number format on inbound rules.

- **DNIS (Dialed Number Information Service)** — allows the recipient of a call to know the phone number originally dialed.
- **ANI (Automatic Number Identification)** — determines the origination telephone number on toll calls for billing purposes.

By default, **E.164** is selected. Available formats include:

- **+E.164** — number with the `+` in front of the country code.
- **E.164** — number without the `+` in front of the country code.
- **National (10 digits)** — local 10-digit format of the country.
- **SIP Username** — the username of the SIP Connection. Only available for credential-authenticated connections and only for DNIS.
- **+E.164 / National (10 digits)** — ANI only. If the dialed number and origin are both US-based, the SIP INVITE contains a 10-digit ANI; if the origin is international, Telnyx sends the ANI as +E.164.
- **E.164 / National (10 digits)** — ANI only. Same logic as above, but Telnyx sends E.164 (without `+`) for international origins.

For WebRTC applications using a credential-authenticated connection, set the DNIS number format to **SIP Username** so inbound calls deliver the SIP Connection's username in the SIP INVITE. Also select the **VP8/9** codecs in the advanced inbound settings to support video.

### Other Inbound Settings

- **SIP Transport Protocol** — available on IP Auth, FQDN Auth, or MS Teams Auth connections.
- **SIP Region** — available on IP Auth, FQDN Auth, or MS Teams Auth connections; sets the Telnyx region from which SIP signaling is sent.
- **No Ringback Timeout** — how long Telnyx waits for your SIP 180/183 response before terminating the call. Default: 5 seconds (range: 1 second to 2 minutes).
- **No Answer Timeout** — how long Telnyx waits for your SIP 200 OK response before terminating the call. Default: 5 seconds (range: 1 second to 10 minutes).
- **SIP Subdomain** — available on IP Auth, FQDN Auth, or MS Teams Auth connections; sets a SIP subdomain that can receive calls. Leaving this empty disables SIP subdomain calls.
- **Receive SIP Subdomain Calls** — available on IP Auth, FQDN Auth, or MS Teams Auth connections; controls whether Telnyx processes calls with a defined subdomain. Can be set to allow from anyone (public internet) or only from your other account connections.
- **Channel Limit** — controls how many concurrent calls are allowed. Default: no limit.
- **Receive SIP URI Calls** — available on credential-type connections; controls whether Telnyx processes calls where `sip:username@sip.telnyx.com` is dialed. Can be disabled, allowed from anyone, or only from your connections.
- **Encrypted Media** — encrypts inbound media with SRTP; Telnyx sends the SIP INVITE with crypto media attributes.
- **Default Ringback Setting** — Telnyx does not send anything but relays any messages and/or early media from the called party to the PSTN inbound carrier.
- **Generate Ringback Tone (183)** — Telnyx replies with an instant 183 message with SDP and sends early media carrying a US ringback tone to the PSTN inbound carrier.
- **Enable Instant Ringback (180)** — Telnyx replies with an instant 180 Ringing message; the PSTN inbound carrier is expected to generate a ringback tone.
- **Offered Audio / Video Codecs** — enable and order your preferred codecs.
- **Enable SIP Compact Headers** — sends SIP headers compacted to reduce bandwidth consumption.
- **Enable PRACK** — allows acknowledgment of provisional 1XX responses. Disabled by default.
- **Receive ISUP Headers into SIP Headers** — converts SS7 PSTN ISUP information from the SIP INVITE body into SIP headers.
- **Enable Shaken/Stir Header** — receive attestation information in webhooks for incoming calls.
- **Enable 3rd Party Call Control** — for Cisco UCM devices and cases where the SIP INVITE doesn't include SDP (late media negotiation).
- **Enable Simultaneous Ringing** — allows multiple SIP devices registered under the same credentials-authenticated SIP connection to ring at the same time.

## Outbound Settings

Outbound settings control how calls are sent from your SIP Connection.

- **Outbound Voice Profile** — choose which outbound profile the SIP Connection is associated with.
- **Localization Country** — when enabled, allows dialing out with the associated exit code of that country and dialing local numbers without the exit + country code. When unspecified, Telnyx validates dialed numbers as US; if validation fails, a 404 invalid destination response is returned.
- **Channel Limit for Outbound Calls** — Telnyx honors the channel limit and returns a 403 channel limit reached response when exceeded.
- **Caller ID Override** — always override the caller ID, override for normal calls only, or override for emergency calls only.
- **(FAX Settings) T.38 Re-invite Initiated By** — Telnyx (default), Customer, or Disabled.
- **Encrypted Media** — encrypts outbound media with SRTP; Telnyx expects the SIP INVITE to include crypto media attributes.
- **Default Ringback Settings** — any 18x messages and/or early media from the PSTN Term Carrier are passed to the calling party agent.
- **Enable Instant Ringback (180)** — Telnyx replies with an instant 180 message; the calling party agent is expected to generate a ringback tone.
- **Generate Ringback Tone (183)** — Telnyx replies with an instant 183 message with SDP and sends early media carrying a US ringback tone to the calling party agent.
