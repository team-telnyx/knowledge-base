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

*Part 2 of 4 — see also: [Part 1](telnyx-sip-routing-registration-and-integration--part-1.md), [Part 3](telnyx-sip-routing-registration-and-integration--part-3.md), [Part 4](telnyx-sip-routing-registration-and-integration--part-4.md)*

This page consolidates Telnyx documentation on SIP routing, registration, and integration. It covers how Telnyx handles SRV records for SIP calls, the components and flow of SIP registration, round-robin load balancing across connection IPs, the role of Via and Record-Route headers in preventing call drops, and step-by-step configuration guides for connecting Skype for Business, Voice Elements, and Genesys Cloud to Telnyx SIP trunks.

## Round Robin Routing

Round Robin is a type of routing that distributes inbound calls evenly between all the IPs in a connection. This helps balance the load of incoming calls across multiple systems rather than sending all calls to a single system with the others acting only as backups.

### How It Works

With a connection configured with 3 IPs, calls are distributed as follows: the first call goes to IP 1, the second to IP 2, the third to IP 3, the fourth to IP 1, and so on.

Key behaviors:

- Only inbound calls are considered for load balancing, not active calls. A system keeping many active calls will still receive the same number of new calls as the others.
- All systems effectively act as failovers depending on the specific call. If a call sent to IP 1 fails, it is sent to IP 2, and so on down the list until all are exhausted or one answers. If a call is originally sent to IP 2 as a first attempt, the rest of the IPs (including IP 1) are still used as backups.

Round Robin can be selected from the **Default Routing Method** dropdown in the Basic Settings of a connection.

## SIP Record-Route and Via Headers

The Record-Route and Via headers are fundamental components of SIP, ensuring proper routing of requests and responses between SIP entities. Both have been part of SIP since its early standardization (RFC 2543 in 1999, with significant updates in RFC 3261 in 2002).

### Via Header

The Via header tracks the path of request messages as they traverse the network of SIP servers to reach the intended recipient and provides a route for responses to follow back to the originator. Each SIP proxy or server that forwards a request adds its address to the top of the Via header list. When the response is generated, it travels back through the list of Via headers, ensuring it follows the same path back to the originator.

### Record-Route Header

The Record-Route header is used by SIP proxies to ensure that signaling for subsequent SIP messages (such as mid-dialog requests) follows the same path as the initial request. When a SIP proxy wants to stay in the path of future requests in a dialog, it adds a Record-Route header to the initial INVITE request. This ensures that all subsequent messages within the same dialog traverse through the recorded route, enabling features like billing, call recording, or session management to be applied consistently.

### Why Calls Drop or Fail to Connect

A common issue during SIP transactions is the failure of ACK messages to reach the end device, confirming the final response to the initial SIP INVITE. This can prevent the establishment of media sessions, leading to call setup failures and calls being dropped with a SIP BYE message with the reason `ack_timeout`.

When a callee sends a 200 OK response to accept an INVITE request, this response should include Route headers that mirror the path taken by the initial INVITE. This inclusion ensures that the ACK message, which confirms receipt of the 200 OK, is routed back through the same network elements, reaching the callee and signaling that the session can proceed with media exchange.

If the 200 OK omits these Route headers, the network may not have the necessary information to route the ACK back to the callee correctly. Even though the call appears established from the perspective of the initiating party (such as Telnyx), the lack of ACK receipt at the callee's end means the session cannot transition to media exchange, and the call is eventually terminated with an `ack_timeout` hang-up cause.

### Order of Record-Route Headers

The order of Record-Route headers in the customer's 200 OK response is important. Record-Route headers are used by intermediate SIP proxies (like Telnyx's SIP Proxy) to insert themselves into the path of the request and its subsequent responses within a dialog.

- **Forward Path (INVITE)** — Record-Route headers are added in the order the request passes through each proxy. The first proxy the request encounters adds its Record-Route header first.
- **Backward Path (Responses)** — responses traverse the proxies in reverse order, following the Via headers back to the originator.
- **Subsequent Requests (ACK, BYE)** — the UAC constructs the Route header field based on the Record-Route headers received in the first final response (e.g., 200 OK), reversing the order to ensure subsequent messages follow the path back through the proxies in the correct sequence.

If headers are reordered incorrectly, SIP messages may take an inefficient path or fail to reach their destination at all.

### Other Common Causes of ACK Failures

- **Malformed ACK packet missing carriage return line feeds (CRLF)** — CRLF characters (`\r\n`) are essential for delineating the end of a line in SIP message headers. Without them, the receiving system may not recognize line boundaries, leading to parsing errors or the message being ignored.
- **CSeq mismatch** — the CSeq header maintains synchronization between SIP requests and responses. Each new SIP request within the same dialog must increment the CSeq number. A mismatch between the CSeq numbers in the INVITE, 200 OK, and ACK can lead to dropped calls or failures to establish media, even when Record-Route and Via headers are correct. For example, if a client sends an INVITE with `CSeq: 2 INVITE`, receives a 407 challenge, resends the INVITE with `CSeq: 3 INVITE`, gets a 200 OK with `CSeq: 3 INVITE`, but then sends an ACK with `CSeq: 2 ACK`, the server considers the transaction incomplete and does not establish media, resulting in an `ack_timeout` disconnect.

### Best Practices

- Check the configuration of SIP infrastructure, including SIP proxies and Session Border Controllers (SBCs), to ensure they correctly include Route headers in 200 OK responses.
- Use SIP tracing and logging tools to monitor call flows and diagnose issues with SIP message routing. Comparing successful and unsuccessful call logs can help identify discrepancies in Route header handling.
- Familiarize yourself with the intricacies of SIP signaling and how different network elements interact.
