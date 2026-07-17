---
title: Telnyx SIP Routing, Registration, and Integration
summary: This page consolidates Telnyx documentation on SIP routing, registration,
  and integration. It covers how Telnyx handles SRV records for SIP calls, the components
  and flow of SIP registration, round-robin load balancing across connection IPs,
  the role of Via and Record-Route headers in preventing call drops, and step-by-step
  configuration guides for connecting Skype for Business, Voice Elements, and Genesys
  Cloud to Telnyx SIP trunks.
sources:
- url: https://support.telnyx.com/en/articles/10666839-how-telnyx-handles-srv-records-for-sip-calls
- url: https://support.telnyx.com/en/articles/1130698-skype-set-up-skype-for-biz-sip-trunk
- url: https://support.telnyx.com/en/articles/4363904-sip-registration
- url: https://support.telnyx.com/en/articles/6145484-voice-elements-telnyx-sip
- url: https://support.telnyx.com/en/articles/8174793-round-robin-routing
- url: https://support.telnyx.com/en/articles/8268122-byoc-telnyx-genesys
- url: https://support.telnyx.com/en/articles/9133298-sip-record-route-headers
updated_at: 2026-07-17T09:00:56Z
---

# Telnyx SIP Routing, Registration, and Integration

*Part 1 of 4 — see also: [Part 2](telnyx-sip-routing-registration-and-integration--part-2.md), [Part 3](telnyx-sip-routing-registration-and-integration--part-3.md), [Part 4](telnyx-sip-routing-registration-and-integration--part-4.md)*

This page consolidates Telnyx documentation on SIP routing, registration, and integration. It covers how Telnyx handles SRV records for SIP calls, the components and flow of SIP registration, round-robin load balancing across connection IPs, the role of Via and Record-Route headers in preventing call drops, and step-by-step configuration guides for connecting Skype for Business, Voice Elements, and Genesys Cloud to Telnyx SIP trunks.

## Overview of Telnyx SIP Routing and Registration

Telnyx's SIP service relies on several interconnected mechanisms to deliver reliable voice traffic: DNS-based routing using SRV records, SIP registration for inbound reachability, round-robin load balancing across multiple endpoints, and proper SIP header handling (Via and Record-Route) to keep signaling paths intact. Together these features let customers configure resilient trunks, integrate with platforms like Skype for Business, Genesys Cloud, and Voice Elements, and troubleshoot common call-setup failures.

## How Telnyx Handles SRV Records for SIP Calls

SRV (Service) records in DNS specify the location of servers for specific services. For SIP traffic, they enable distribution of SIP requests across multiple hosts, providing load balancing and failover. Telnyx honors SRV records in two scenarios:

- **SIP FQDN Connections** — the FQDN(s) of the Connection indicate Telnyx where to route inbound calls.
- **Voice API calls to external domains** — customers can dial or transfer calls to external non-Telnyx FQDNs.

Telnyx selects the appropriate SRV record based on the transport protocol used in the SIP request.

### RURI with a Port Number

If the RURI contains a port number (e.g. `sip:+1234567890@sip.example.com:5060`):

1. Telnyx performs an A-record lookup, bypassing the SRV record.
2. The call is routed to the IP address returned by the A-record lookup.

### RURI Without a Port Number

If the RURI does not contain a port number (e.g. `sip:+1234567890@sip.example.com`):

1. Telnyx performs an SRV-record lookup.
2. The SRV record dictates the server to which the call should be routed. If no SRV record exists, Telnyx falls back to an A-record lookup and uses the default SIP port (5060 for UDP/TCP or 5061 for TLS). If the first SRV target fails with a SIP 503 response, Telnyx attempts the next highest priority target in the SRV list.

### Key Configuration Considerations

- **Remove port numbers for SRV record range** — to leverage SRV records, ensure the `to` header in your dial command does not include a port number. For example:
  - Incorrect: `"to" => "sip:+1234567890@sip.example.com:5060"`
  - Correct: `"to" => "sip:+1234567890@sip.example.com"`
- **Fallback behavior** — if an SRV record is not found, Telnyx attempts an A-record lookup. If no A-record exists, the call fails with a `SIP 478 (Unresolvable Destination)` response.
- **DNS resolvability** — ensure your DNS configuration is correct and resolvable globally, and that SRV targets are properly configured with resolvable A records.

### Example Use Case

A customer configures their `to` header with a domain and port, where the domain `sip.example.com` is an SRV record:

`"to" => "sip:+1234567890@sip.example.com:5060"`

This results in an A-record lookup, which fails because there is no A-record for `sip.example.com`. The solution is to remove the port number to allow SRV record processing:

`"to":"sip:+1234567890@sip.example.com"`

This change enables Telnyx to perform an SRV lookup, correctly routing the call based on the SRV record.

## SIP Registration

SIP Registration is the process by which service providers identify the phones of their customers, providing insight into where to send phone calls. Registration is required only for receiving inbound calls; outbound calling uses SIP authentication instead.

### Components of SIP Registration

- **User Agent** — the SIP entity that interacts with the user (e.g. soft phone).
- **SIP URI** — the SIP address that identifies a user, usually consisting of a username and domain name (e.g. `sip:bob@yourcompany.com`). The transport used (UDP, TCP, or TLS) is configured within the user agent and indicated to the SIP Registrar during registration. This is why transport cannot be set on SIP credential connections — it is defined and controlled by the user agent.
- **SIP Registrar Server** — a server belonging to the service provider that accepts REGISTER requests and maintains a binding table of user registrations. Usually collocated with proxy and redirect servers.
- **Location Server** — registrar servers store their customers' locations to this server.
- **Binding table** — contains details on where to reach the user such as numbers, IP address, and ports.
- **Proxy Server** — handles incoming invitations.
- **Redirect Server** — provides alternative locations where the user can be reachable.
- **IP Authentication** — a check by the Registrar to confirm the user's details.

### Registration Flow

A typical registration exchange (using Zoiper registering to `sip.telnyx.com` from public IP `80.111.117.202`, which resolves to the Telnyx anycast IP `192.76.120.10`):

1. `80.111.117.202 -> 192.76.120.10 REGISTER sip:sip.telnyx.com;transport=UDP SIP/2.0`
2. `192.76.120.10 -> 80.111.117.202 401 Unauthorized`
3. `80.111.117.202 -> 192.76.120.10 REGISTER sip:sip.telnyx.com;transport=UDP SIP/2.0`
4. `192.76.120.10 -> 80.111.117.202 200 OK`

The 401 Unauthorized response is a challenge from the registrar. A second 401 indicates incorrect credentials (username or password). A 200 OK confirms successful registration. Until registration completes, numbers cannot receive inbound calls because the address of record (AOR) is not on file.

### SIP URI Calling

When expecting inbound calls via SIP URI calling from another service to credential-based SIP Connections, ensure the contact header specifies the username created on the SIP Connection. Most systems expect the SIP INVITE URI to contact `username@ipaddress` of your system; if the username differs from the SIP Connection username, your system may reject calls.

### SIP Registration Using TCP or TLS

For TCP and TLS (which runs over TCP), Telnyx re-uses the TCP connection established by the User Agent. Telnyx uses port 5060 for TCP. User Agents are unlikely to establish connections from port 5060 to port 5060 and are more likely to use an ephemeral port (RFC 6056 defines the range as 1024–65535).

When a User Agent sends a REGISTER message to Telnyx and the IP address and port in the contact header do not match the IP address and port the message was received from, Telnyx adds an "alias" to the AOR on file. This can be seen in the 200 OK Telnyx sends back. If the REGISTER request uses port 5060 in its contact header and the message is received from an ephemeral port, Telnyx aliases the address, so future INVITEs sent to the User Agent after registration will have port 5060 in the Request-URI but will re-use the existing TCP connection.

If it is required that port 5060 is used for TCP with a User Agent, it is necessary to register directly from port 5060.

### SIP Registration via siphv.telnyx.com

The high volume short duration product (`siphv.telnyx.com`) does not currently support SIP Registration for inbound calls. To receive inbound calls, register with the other FQDNs: `sip.telnyx.com`, `sip.telnyx.ca`, `sip.telnyx.eu`, and `sip.telnyx.com.au`. Attempting to register via the high volume short duration domain results in a `SIP 405 Method Not Allowed` response.

### Special Notes on SIP Registration

- SIP registration is required only for receiving inbound calls. Outbound calling from credential-based SIP Connections uses SIP authentication (a SIP 407 proxy authentication challenge) rather than registration.
- Use a low expiry refresh of around 180 seconds so Telnyx knows where to route calls via the AOR on file.
- Monitor trunk status and attempt a soft reload if the trunk shows as down. A full restart of the phone system can also resolve SIP Registration problems.
- Take a network capture trace on the LAN to review SIP behavior; Telnyx support can help review captures if shared.
- Inbound and outbound are decoupled and use different methods to receive and make calls.
