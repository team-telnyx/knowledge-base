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

*Part 3 of 4 — see also: [Part 1](telnyx-sip-voice-configuration-and-routing--part-1.md), [Part 2](telnyx-sip-voice-configuration-and-routing--part-2.md), [Part 4](telnyx-sip-voice-configuration-and-routing--part-4.md)*

This page consolidates Telnyx support guidance on SIP voice configuration, covering SRV record handling, call forwarding, external call transfers, SIP registration, post-dial delay, round-robin routing, and the role of Via and Record-Route headers in successful call setup.

## Via and Record-Route Headers

SIP headers act as GPS markers guiding messages through the network. The Via and Record-Route headers are critical for routing SIP messages and ensuring seamless call setup and media exchange.

The **Via header** tracks the path of request messages as they traverse SIP servers to reach the recipient and provides the route for responses to follow back to the originator. Each proxy or server that forwards a request adds its address to the top of the Via header list, and responses travel back through that list. The Via header has been part of SIP since RFC 2543 in 1999 and was designed to solve response routing in IP networks.

The **Record-Route header** is used by SIP proxies to ensure that signaling for subsequent SIP messages (such as mid-dialog requests) follows the same path as the initial request. When a proxy wants to stay in the path of future requests in a dialog, it adds a Record-Route header to the initial INVITE, so all subsequent messages traverse the recorded route. This enables features like billing, call recording, and session management to be applied consistently. Both headers were solidified in RFC 3261 in 2002.

A common failure mode is the ACK message not reaching the end device after a 200 OK, which prevents media sessions from establishing and causes calls to drop with a SIP BYE and the reason `ack_timeout`. When a callee sends a 200 OK to accept an INVITE, the response should include Route headers that mirror the path taken by the initial INVITE so the ACK is routed back through the same network elements. If the 200 OK omits these Route headers, the network may not route the ACK correctly, the session cannot transition to media exchange, and the call is terminated with `ack_timeout`.

For example, a Telnyx INVITE to a customer includes `Record-Route` headers pointing at `192.76.120.10` and `10.255.0.1`. If the customer's 200 OK omits those `Record-Route` headers, the ACK may not follow the intended path and the call may fail. Including the `Record-Route` headers in the 200 OK ensures the ACK follows the predefined path through any intermediate proxies.

In the reverse direction, when a client sends an INVITE to Telnyx and Telnyx responds with a 200 OK containing `Record-Route` headers, the client must reverse the order of those headers and construct the correct Route headers in its ACK. An ACK that omits or reorders the Route headers will fail; the correct ACK reverses the Record-Route order so messages traverse the proxies in the right sequence.

The order of Record-Route headers in the 200 OK is important. For the initial INVITE, Record-Route headers are added in the order the request passes through each proxy. For subsequent requests within the dialog (ACK, BYE), the UAC constructs the Route header field by reversing the order of the Record-Route headers received in the first final response, so messages follow the path back through the proxies in the correct sequence. Reordering them incorrectly can cause inefficient routing or messages not reaching their destination.

Even with correct R-URI and Route headers, calls can still fail due to other issues:

- **Malformed ACK missing CRLF**: Missing carriage return/line feed characters can cause parsing errors or the message being ignored. Ensure strict adherence to protocol specifications, including proper CRLF line endings.
- **CSeq mismatch**: The CSeq header maintains synchronization between SIP requests and responses. Each new request within the same dialog must increment the CSeq number. A mismatch between the CSeq numbers in the INVITE, 200 OK, and ACK (for example, sending `CSeq: 2 ACK` when the server expects `CSeq: 3 ACK` after a re-INVITE with authentication) causes the server to consider the transaction incomplete and not establish media, leading to an `ack_timeout` disconnect.

Best practices include verifying that SIP proxies and Session Border Controllers correctly include Route headers in 200 OK responses, using SIP tracing and logging tools to compare successful and unsuccessful call flows, and developing familiarity with SIP signaling to aid troubleshooting.
