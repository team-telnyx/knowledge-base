---
title: Telnyx SIP Trunking Configuration
summary: A comprehensive guide to configuring and managing SIP trunking with Telnyx,
  covering connection types, authentication methods, inbound/outbound settings, failover
  and retry logic, SRV record handling, number formats, SIP protocols, STUN/TURN servers,
  SIP URI calling, response codes, and advanced features such as SHAKEN/STIR, PRACK,
  and Record-Route headers.
sources:
- url: https://support.telnyx.com/en/articles/10666839-how-telnyx-handles-srv-records-for-sip-calls
- url: https://support.telnyx.com/en/articles/1130682-telnyx-stun-and-turn-server
- url: https://support.telnyx.com/en/articles/1130705-sip-protocols-that-telnyx-uses
- url: https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats
- url: https://support.telnyx.com/en/articles/1130715-register-multiple-devices-on-one-connection
- url: https://support.telnyx.com/en/articles/1130717-limits-on-concurrent-outbound-calls
- url: https://support.telnyx.com/en/articles/11358700-what-is-the-u-s-reassigned-numbers-database
- url: https://support.telnyx.com/en/articles/1176364-sip-connection-failover-guide-ip-fqdn-based
- url: https://support.telnyx.com/en/articles/2602782-ip-authentication-with-tech-prefix
- url: https://support.telnyx.com/en/articles/2925713-sip-uri-calling
- url: https://support.telnyx.com/en/articles/4245868-sip-connection-types
- url: https://support.telnyx.com/en/articles/4304898-sip-trunking-methods-requests-responses
- url: https://support.telnyx.com/en/articles/4320364-sip-connection-fail-over-and-retries
- url: https://support.telnyx.com/en/articles/4351104-sip-connection-settings
- url: https://support.telnyx.com/en/articles/4363904-sip-registration
- url: https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings
- url: https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes
- url: https://support.telnyx.com/en/articles/4860170-ip-authentication-with-x-telnyx-token
- url: https://support.telnyx.com/en/articles/6169513-grandstream-grp260x-sip-trunk
- url: https://support.telnyx.com/en/articles/6902981-understanding-sip-prack-protocol
- url: https://support.telnyx.com/en/articles/7029684-telephony-credentials-types
- url: https://support.telnyx.com/en/articles/7421223-shaken-stir-parameters
- url: https://support.telnyx.com/en/articles/8096455-how-to-configure-a-sip-trunk
- url: https://support.telnyx.com/en/articles/9133298-sip-record-route-headers
updated_at: 2026-06-11T11:25:41Z
---

# Telnyx SIP Trunking Configuration

*Part 2 of 4 — see also: [Part 1](telnyx-sip-trunking-configuration--part-1.md), [Part 3](telnyx-sip-trunking-configuration--part-3.md), [Part 4](telnyx-sip-trunking-configuration--part-4.md)*

A comprehensive guide to configuring and managing SIP trunking with Telnyx, covering connection types, authentication methods, inbound/outbound settings, failover and retry logic, SRV record handling, number formats, SIP protocols, STUN/TURN servers, SIP URI calling, response codes, and advanced features such as SHAKEN/STIR, PRACK, and Record-Route headers.

## SIP Registration

SIP Registration tells Telnyx where to send inbound calls for credential-based connections. The process involves:

1. **User Agent** sends REGISTER to the **SIP Registrar Server**.
2. Registrar responds with 401 Unauthorized (challenge).
3. User Agent resends REGISTER with credentials.
4. On success, Registrar responds 200 OK; the binding table stores the Address of Record (AOR).

**Key points:**
- Registration is only required for **inbound** calls. Outbound calls use SIP authentication (407 challenge/response).
- Use a low expiry refresh (around 180 seconds) so Telnyx maintains a current AOR.
- For TCP/TLS, Telnyx reuses the TCP connection established by the User Agent (port 5060 for TCP). If the contact header port differs from the source port, Telnyx adds an "alias" to the AOR.
- The high-volume short-duration product (`siphv.telnyx.com`) does **not** support SIP registration; use `sip.telnyx.com`, `sip.telnyx.ca`, `sip.telnyx.eu`, or `sip.telnyx.com.au` instead.

### Failed vs. Successful Registration

A failed registration returns repeated **401 Unauthorized** responses (typically due to incorrect username or password). Until registration succeeds, inbound calls cannot be routed because no AOR is on file.

For SIP URI calling to credential connections, ensure the contact header username matches the SIP Connection username.

## Failover and Retries

Telnyx's failover policy ensures calls connect regardless of issues on either side. Key concepts:

- **IP1 / IP2** — Primary and secondary signalling IPs of the SIP Region (US: 192.76.120.10 and 64.16.250.10).
- **Routes** — Each IP (IP auth) or FQDN (FQDN auth) is a route.
- **Route Preferences** — Sequential (Primary/Secondary/Tertiary) or Round Robin (random order). Number-level settings **override** connection-level settings.
- **Call Connected** — A call is considered "connected" (not necessarily answered) if it results in: 486 Busy, 404 Not Found, 603 Declined, rings without answer (180/183), or is answered (200 OK).

To stop retry of inbound INVITEs, return a **603 Declined** response.

### Failover Scenarios

**Single-route connection:** Attempt from IP1 → if not connected, retry from IP2.

**Multi-route connection:** Attempt from IP1 to route 1 → IP1 to route 2 → IP1 to route 3 → IP2 to route 1 → IP2 to route 2 → IP2 to route 3.

**Credential auth connection:** Attempts go through KSS (SIP registrar) instances — primary KSS, then secondary, then tertiary — each through IP1 or IP2 (whichever the device registered to).

**Call Forward on Failure:** After exhausting connection routes, attempts go to the Call Forward PSTN number through up to 10 termination carriers.

**Call Forward Always:** Sends directly to the PSTN number through up to 10 termination carriers.

**SRV records (FQDN connections):** See [Telnyx SIP Trunking Configuration#SRV Record Handling](telnyx-sip-trunking-configuration-srv-record-handling.md) below.

**Outbound to PSTN:** Attempts through up to 10 termination carriers.

### Primary and Secondary Proxies

For redundancy, configure both primary and secondary Telnyx SIP proxies:

- **Inbound:** Ensure firewalls/ACLs allow traffic from both primary and secondary proxy IPs.
- **Outbound (IP addresses):** Primary: `192.76.120.10`, Secondary: `64.16.250.10` (US region).
- **Outbound (FQDN with A record):** Primary: `sip.telnyx.com`, Failover: `sip-anycast2.telnyx.com` (US region).
- **Outbound (FQDN with SRV — recommended):** Use `sip.telnyx.com`; failover is automatic.
- For other regions, adjust the domain accordingly (e.g., `sip.telnyx.eu`, `sip.telnyx.ca`, `sip.telnyx.com.au`). See [sip.telnyx.com](https://sip.telnyx.com/) for all regions.

## SRV Record Handling

SRV (Service) records in DNS specify server locations for specific services, enabling load balancing and failover for SIP traffic. Telnyx honors SRV records in two scenarios: SIP FQDN Connections (inbound routing) and Voice API calls to external domains.

Telnyx selects the appropriate SRV record based on the transport protocol used in the SIP request.

### RURI With a Port Number

If the RURI contains a port (e.g., `sip:+1234567890@sip.example.com:5060`), Telnyx performs an **A-record lookup only**, bypassing SRV.

### RURI Without a Port Number

If the RURI does not contain a port (e.g., `sip:+1234567890@sip.example.com`), Telnyx performs an **SRV lookup** and routes based on priority and weight. If no SRV record exists, Telnyx falls back to an A-record lookup using the default SIP port (5060 for UDP/TCP, 5061 for TLS). If the first SRV target fails with SIP 503, Telnyx attempts the next highest priority target.

### Key Considerations

- **Remove port numbers** from dial commands to leverage SRV. Correct: `"to" => "sip:+1234567890@sip.example.com"`. Incorrect: `"to" => "sip:+1234567890@sip.example.com:5060"`.
- If no SRV or A-record exists, the call fails with **SIP 478 (Unresolvable Destination)**.
- Ensure SRV targets have properly configured, resolvable A records.

## Number Formats

SIP Connections allow you to control the format of both the DNIS (dialed number) and ANI (originating number) in inbound SIP INVITEs.

### DNIS Options

- **+E.164** — Number with `+` and country code.
- **E.164** — Number without `+`.
- **National (10 digits)** — Local 10-digit format.
- **SIP Username** — Sends the SIP Connection username (credential auth only).

### ANI Options

- **+E.164** — Number with `+`.
- **E.164** — Number without `+`.
- **National (10 digits)** — Local 10-digit format.
- **+E.164 / National (10 digits)** — If both origin and dialed number are US-based, sends 10 digits; otherwise sends +E.164.
- **E.164 / National (10 digits)** — Same logic as above, but without `+` for international.

For **outbound** calls, all formats are supported. The Localization Country setting allows dialing with local exit codes and local numbers without the country code prefix.

For WebRTC applications using credential authentication, set DNIS to SIP Username and select VP8/9 codecs in the advanced inbound settings for video support.

## Supported SIP Protocols

Telnyx Mission Control supports three SIP transport protocols:

- **UDP**
- **TCP**
- **TLS**

The transport protocol is configured within the user agent; credential-based connections do not expose a transport setting because it is defined by the registering device. See [sip.telnyx.com](https://sip.telnyx.com/) for port details.

## STUN and TURN Servers

Telnyx provides STUN and TURN servers to help navigate NAT issues in VoIP environments:

- **STUN server:** `stun.telnyx.com:3478` — Enables devices behind NAT to discover their public IP and port for direct media paths.
- **TURN server:** `turn.telnyx.com:3478` — Relays data when a direct connection is not possible. Contact Telnyx support for the username and password.

## SIP URI Calling

SIP URI calling allows receiving inbound calls directly to a SIP URI on credential-based connections, removing the need for a phone number. Callers reach you by dialing `your-username@sip.telnyx.com`.

### Enabling SIP URI Calling

1. Navigate to **Voice Suite → SIP Trunking**.
2. Edit the desired connection.
3. Open **Authentication and routing**.
4. Under **Receive SIP URI calls**, choose: *From anyone* (unrestricted) or *Only from my Connections* (internal).

This can also be configured via the API by setting `sip_uri_calling_preference` to `"disabled"`, `"unrestricted"`, or `"internal"`.

### Billing

- Calls from unidentified sources: **$0.002/minute**, charged to the connection owner.
- Calls from a matched Telnyx SIP Connection: treated as **On-Net**, billed per your rate deck.
- Only SIP usernames beginning with a **non-numeric character** are considered valid (fraud prevention against number spoofing).
