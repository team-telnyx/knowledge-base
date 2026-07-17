---
title: Telnyx SIP Protocols, Methods, and Response Codes
summary: This page consolidates Telnyx's SIP protocol documentation, covering supported
  transport protocols (UDP, TCP, TLS), the full set of SIP request methods and response
  classes defined in RFC 3261, Telnyx-specific custom response codes (D1X–D9X, PE,
  P0X, R1X, RG1, TV1, TM1), ISDN cause codes, the PRACK extension (RFC 3262), and
  step-by-step configuration of an Audiocodes 400HD IP phone with Telnyx Mission Control.
sources:
- url: https://support.telnyx.com/en/articles/1130705-sip-protocols-that-telnyx-uses
- url: https://support.telnyx.com/en/articles/4304898-sip-trunking-methods-requests-responses
- url: https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes
- url: https://support.telnyx.com/en/articles/5819923-audiocodes-400hd
- url: https://support.telnyx.com/en/articles/6902981-understanding-sip-prack-protocol
updated_at: 2026-07-17T09:06:54Z
---

# Telnyx SIP Protocols, Methods, and Response Codes

*Part 1 of 5 — see also: [Part 2](telnyx-sip-protocols-methods-and-response-codes--part-2.md), [Part 3](telnyx-sip-protocols-methods-and-response-codes--part-3.md), [Part 4](telnyx-sip-protocols-methods-and-response-codes--part-4.md), [Part 5](telnyx-sip-protocols-methods-and-response-codes--part-5.md)*

This page consolidates Telnyx's SIP protocol documentation, covering supported transport protocols (UDP, TCP, TLS), the full set of SIP request methods and response classes defined in RFC 3261, Telnyx-specific custom response codes (D1X–D9X, PE, P0X, R1X, RG1, TV1, TM1), ISDN cause codes, the PRACK extension (RFC 3262), and step-by-step configuration of an Audiocodes 400HD IP phone with Telnyx Mission Control.

## SIP Protocols and Transports

Telnyx Mission Control supports the following SIP transport protocols:

- UDP
- TCP
- TLS

Refer to [sip.telnyx.com](https://sip.telnyx.com/) for additional detail.

## SIP Methods and Requests

SIP Trunking is a popular form of voice and fax communications over the Internet. The SIP specification is defined in [RFC 3261](https://tools.ietf.org/html/rfc3261), which describes Session Initiation Protocol (SIP) as an application-layer control (signalling) protocol for creating, modifying, and terminating sessions with one or more participants. These sessions include Internet telephone calls, multimedia distribution, and multimedia conferences.

There are fourteen SIP request methods. The first six are the most basic:

- **INVITE** — Establishes a session.
- **ACK** — Confirms an INVITE request.
- **BYE** — Ends a session.
- **CANCEL** — Cancels establishing of a session.
- **REGISTER** — Communicates user location (host name, IP).
- **OPTIONS** — Communicates information about the capabilities of the calling and receiving SIP phones.
- **PRACK** — Provisional Acknowledgement.
- **SUBSCRIBE** — Subscribes for Notification from the notifier.
- **NOTIFY** — Notifies the subscriber of a new event.
- **PUBLISH** — Publishes an event to the Server.
- **INFO** — Sends mid session information.
- **MESSAGE** — Transports Instant Messages.
- **UPDATE** — Modifies the state of a session.

### SIP OPTIONS Notes

SIP OPTIONS is used to determine if a user agent (e.g., a SIP phone or server) is available or reachable, and to query the capabilities of the user agent, such as which methods it supports. Telnyx's systems do not send SIP OPTIONS to customer SIP Connections, but Telnyx does accept and respond to SIP OPTIONS requests to its SIP Proxies from customer user agents.
