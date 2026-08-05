---
title: Telnyx SIP Voice Configuration and Routing
summary: This page consolidates Telnyx support guidance on SIP voice configuration,
  covering SRV record handling, call forwarding, external call transfers, SIP registration,
  post-dial delay, round-robin routing, and the role of Via and Record-Route headers
  in successful call setup.
sources:
- url: https://support.telnyx.com/en/articles/10666839-how-telnyx-handles-srv-records-for-sip-calls
- url: https://support.telnyx.com/en/articles/1130657-call-forwarding
- url: https://support.telnyx.com/en/articles/12538402-telnyx-vapi-integration
- url: https://support.telnyx.com/en/articles/13117410-how-external-call-transfers-work
- url: https://support.telnyx.com/en/articles/4363904-sip-registration
- url: https://support.telnyx.com/en/articles/4453840-post-dial-delay-pdd
- url: https://support.telnyx.com/en/articles/8174793-round-robin-routing
- url: https://support.telnyx.com/en/articles/9133298-sip-record-route-headers
updated_at: 2026-08-05T13:25:14Z
---

# Telnyx SIP Voice Configuration and Routing

*Part 2 of 4 — see also: [Part 1](telnyx-sip-voice-configuration-and-routing--part-1.md), [Part 3](telnyx-sip-voice-configuration-and-routing--part-3.md), [Part 4](telnyx-sip-voice-configuration-and-routing--part-4.md)*

This page consolidates Telnyx support guidance on SIP voice configuration, covering SRV record handling, call forwarding, external call transfers, SIP registration, post-dial delay, round-robin routing, and the role of Via and Record-Route headers in successful call setup.

## SIP Registration

SIP Registration is the process by which service providers identify the location of customer phones so they know where to send calls. The components involved are:

- **User Agent**: The SIP entity that interacts with the user (e.g. softphone). The transport (UDP, TCP, or TLS) is configured within the user agent and indicated to the SIP Registrar during registration, which is why transport cannot be set on SIP credential connections.
- **SIP URI**: The SIP address identifying a user, typically `username@domain` (e.g. `sip:bob@yourcompany.com`).
- **SIP Registrar Server**: Accepts REGISTER requests and maintains a binding table of user registrations, usually collocated with proxy and redirect servers.
- **Location Server**: Where registrar servers store customer locations.
- **Binding table**: Contains reachability details such as numbers, IP addresses, and ports.
- **Proxy Server**: Handles incoming invitations.
- **Redirect Server**: Provides alternative locations where the user can be reached.
- **IP Authentication**: A check by the Registrar to confirm user details.

A failed registration example using Zoiper against `sip.telnyx.com` shows repeated `401 Unauthorized` responses when the password is incorrect. A successful registration shows the same `401 Unauthorized` challenge followed by a `200 OK` once the correct credentials are supplied. Until registration completes successfully, numbers cannot receive inbound calls because the address of record (AOR) is not on file.

For SIP URI calling into credential-based SIP Connections, ensure the contact header specifies the username created on the SIP Connection; otherwise the system may reject calls.

For TCP and TLS, Telnyx re-uses the TCP connection established by the User Agent and uses port 5060 for TCP. User Agents typically send from ephemeral ports (RFC 6056 defines the range as 1024–65535). When the IP address and port in the contact header do not match the source IP and port of the REGISTER, Telnyx adds an "alias" to the AOR. If the contact header uses port 5060 but the message is received from an ephemeral port, Telnyx aliases the address so future INVITEs use port 5060 in the Request-URI while re-using the existing TCP connection. If port 5060 must be used for TCP, register directly from port 5060.

The high-volume short-duration product (`siphv.telnyx.com`) does not support SIP Registration for inbound calls; attempting to register there returns a `SIP 405 Method Not Allowed`. Use `sip.telnyx.com`, `sip.telnyx.ca`, `sip.telnyx.eu`, or `sip.telnyx.com.au` instead.

SIP registration is required only for inbound calls. Use a low expiry refresh of around 180 seconds so Telnyx can keep the AOR current. Outbound calling from credential-based SIP Connections requires SIP authentication: Telnyx issues a `407 Proxy Authentication` challenge, and the User Agent responds with a new INVITE containing hashed credentials. Inbound and outbound are decoupled and use different mechanisms.

## Post Dial Delay (PDD)

Post Dial Delay (PDD) is the time the originating caller experiences between sending the final dialed digit and hearing ring tone or other in-band information. If the originating network plays an announcement before completing the call, that announcement duration is excluded from this definition. For SIP, PDD is measured from sending the INVITE to receiving the first ringing response (e.g. `SIP/2.0 180 Ringing`).

PDD commonly occurs when the carrier of the dialed number has not received an indication that the end user's device is ringing. It is widely experienced on wireless devices with low signal that are far from their provider's closest cell tower. Most carriers consider anything under 7 seconds acceptable and will not troubleshoot PDD below that threshold.

Telnyx partners with Tier 1 carriers and interconnects worldwide, and its telephony operations team monitors and tests carriers and interconnects for call completion issues. For PDD over 7 seconds, contact [support@telnyx.com](mailto:support@telnyx.com) so the team can verify whether there is an underlying issue and work to optimize routes.

## Round Robin Routing

Round Robin is a routing method that distributes inbound calls evenly between all IPs in a connection, providing basic load balancing. With three IPs configured, the first call goes to IP 1, the second to IP 2, the third to IP 3, the fourth back to IP 1, and so on.

Only inbound calls are counted for load balancing — not active calls — so a system holding many active calls still receives the same share of new inbound calls as the others. Every system effectively acts as a failover for every call: if a call sent to IP 1 fails, it is retried on IP 2, then IP 3, and so on until one answers or all are exhausted. If a call is first attempted to IP 2, the remaining IPs (including IP 1) still serve as backups.

Round Robin is selected from the Default Routing Method drop-down in the Basic Settings of the connection.
