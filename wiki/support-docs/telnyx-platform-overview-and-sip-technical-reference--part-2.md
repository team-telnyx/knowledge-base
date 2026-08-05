---
title: Telnyx Platform Overview and SIP Technical Reference
summary: Telnyx is a global Communications Platform as a Service (CPaaS) provider
  offering voice, messaging, real-time communications, AI inference, storage, and
  workflow automation over a privately-owned IP network. This page consolidates Telnyx's
  network specifications, supported SIP protocols and methods, interoperability partners,
  and configuration guidance for common PBX and softphone integrations.
sources:
- url: https://support.telnyx.com/en/articles/1130599-telnyx-tech-specs
- url: https://support.telnyx.com/en/articles/1130637-what-is-telnyx
- url: https://support.telnyx.com/en/articles/1130705-sip-protocols-that-telnyx-uses
- url: https://support.telnyx.com/en/articles/4304898-sip-trunking-methods-requests-responses
- url: https://support.telnyx.com/en/articles/5138185-bicom-pbxware-setup
- url: https://support.telnyx.com/en/articles/6128008-sipxecs-pbx-setup-config
- url: https://support.telnyx.com/en/articles/6133145-microsip-setup-with-telnyx
- url: https://support.telnyx.com/en/articles/6902981-understanding-sip-prack-protocol
updated_at: 2026-08-05T13:27:04Z
---

# Telnyx Platform Overview and SIP Technical Reference

*Part 2 of 4 — see also: [Part 1](telnyx-platform-overview-and-sip-technical-reference--part-1.md), [Part 3](telnyx-platform-overview-and-sip-technical-reference--part-3.md), [Part 4](telnyx-platform-overview-and-sip-technical-reference--part-4.md)*

Telnyx is a global Communications Platform as a Service (CPaaS) provider offering voice, messaging, real-time communications, AI inference, storage, and workflow automation over a privately-owned IP network. This page consolidates Telnyx's network specifications, supported SIP protocols and methods, interoperability partners, and configuration guidance for common PBX and softphone integrations.

## SIP Response Classes

There are six classes of SIP responses that indicate how a call is progressing and whether it has been established or whether there were any failures.

### 1xx — Informational

Provisional responses give feedback on the progression of a session establishment. A SIP endpoint can respond with multiple 1xx responses to inform the requester on how the call is progressing.

- **100 Trying** — Extended search is being performed so a forking proxy must send a 100 Trying response.
- **180 Ringing** — The Destination User Agent has received the INVITE message and is alerting the user of the call.
- **181 Call Is Being Forwarded** — Optional, sent by Server to indicate a call is being forwarded.
- **182 Queued** — Destination was temporarily unavailable; the server has queued the call until the destination is available.
- **183 Session Progress** — This response may be used to send extra information for a call which is still being set up.
- **199 Early Dialog Terminated** — Sent by the User Agent Server to indicate that an early dialogue has been terminated.

### 2xx — Success

Success responses occur when the SIP endpoint has received confirmation that the INVITE request was successful and that the call will be answered.

- **200 OK** — Shows that the request was successful.
- **202 Accepted** — Indicates that the request has been accepted for processing, mainly used for referrals.
- **204 No Notification** — Indicates that the request was successful but no response will be received.

### 3xx — Redirection

3xx responses give information about the SIP endpoint's new location (redirection), or about alternative services that might be able to satisfy the call.

- **300 Multiple Choices** — The address resolved to one of several options for the user or client to choose between.
- **301 Moved Permanently** — The original Request URI is no longer valid; the new address is given in the Contact header.
- **302 Moved Temporarily** — The client should try at the address in the Contact field. *Note: This SIP response is not accepted by Telnyx at this time.*
- **305 Use Proxy** — The Contact field details a proxy that must be used to access the requested destination.
- **380 Alternative Service** — The call failed, but alternatives are detailed in the message body.

### 4xx — Client Errors

The 4xx responses are the Client Error responses, used to indicate that something went wrong while processing the INVITE request. The most frequent request seen is generally a 404 Not Found.

- **400 Bad Request** — The request could not be understood due to malformed syntax.
- **401 Unauthorized** — The request requires user authentication. This response is issued by UASs and registrars.
- **402 Payment Required** — (Reserved for future use).
- **403 Forbidden** — The server understood the request, but is refusing to fulfil it.
- **404 Not Found** — The server has definitive information that the user does not exist at the domain.
- **405 Method Not Allowed** — The method specified in the Request-Line is understood, but not allowed.
- **406 Not Acceptable** — The resource is only capable of generating responses with unacceptable content.
- **407 Proxy Authentication Required** — The request requires user authentication.
- **408 Request Timeout** — Couldn't find the user in time.
- **409 Conflict** — User already registered (deprecated).
- **410 Gone** — The user existed once but is not available here any more.
- **411 Length Required** — The server will not accept the request without a valid content length (deprecated).
- **412 Conditional Request Failed** — The given precondition has not been met.
- **413 Request Entity Too Large** — Request body too large.
- **414 Request URI Too Long** — Server refuses to service the request; the Req-URI is longer than the server can interpret.
- **415 Unsupported Media Type** — Request body is in a non-supported format.
- **416 Unsupported URI Scheme** — Request-URI is unknown to the server.
- **417 Unknown Resource-Priority** — There was a resource-priority option tag, but no Resource-Priority header.
- **420 Bad Extension** — Bad SIP Protocol Extension used, not understood by the server.
- **421 Extension Required** — The server needs a specific extension not listed in the Supported header.
- **422 Session Interval Too Small** — The request contains a Session-Expires header field with a duration below the minimum.
- **423 Interval Too Brief** — Expiration time of the resource is too short.
- **424 Bad Location Information** — The request's location content was malformed or otherwise unsatisfactory.
- **428 Use Identity Header** — The server policy requires an Identity header, and one has not been provided.
- **429 Provide Referrer Identity** — The server did not receive a valid Referred-By token on the request.
- **430 Flow Failed** — A specific flow to a user agent has failed, although other flows may succeed.
- **433 Anonymity Disallowed** — The request has been rejected because it was anonymous.
- **436 Bad Identity Info** — The request has an Identity-Info header and the URI scheme contained cannot be de-referenced.
- **437 Unsupported Certificate** — The server was unable to validate a certificate for the domain that signed the request.
- **438 Invalid Identity Header** — Server obtained a valid certificate used to sign a request, was unable to verify the signature.
- **439 First Hop Lacks Outbound Support** — The first outbound proxy doesn't support the "outbound" feature.
- **440 Max-Breadth Exceeded** — A SIP proxy determined a response context had insufficient Incoming Max-Breadth to carry out a desired parallel fork.
- **469 Bad Info Package** — The UA received an INFO request associated with an Info Package that the UA has not indicated willingness to receive.
- **470 Consent Needed** — The source of the request did not have the permission of the recipient to make such a request.
- **480 Temporarily Unavailable** — Callee currently unavailable.
- **481 Call/Transaction Does Not Exist** — Server received a request that does not match any dialogue or transaction.
- **482 Loop Detected** — Server has detected a loop.
- **483 Too Many Hops** — Max-Forwards header has reached the value '0'.
- **484 Address Incomplete** — Request-URI incomplete.
- **485 Ambiguous** — Request-URI is ambiguous.
- **486 Busy Here** — Callee is busy.
- **487 Request Terminated** — Request has terminated by BYE or CANCEL.
- **488 Not Acceptable Here** — Some aspects of the session description of the Request-URI are not acceptable. If you are using SRTP, see the [TLS and SRTP example](https://support.telnyx.com/en/articles/4404575-tls-and-srtp#h_f545f23a76) for further details in case of a configuration issue.
- **489 Bad Event** — The server did not understand an event package specified in an Event header field.
- **491 Request Pending** — Server has some pending request from the same dialogue.
- **493 Undecipherable** — Request contains an encrypted MIME body, which recipient cannot decrypt.
- **494 Security Agreement Required** — The server has received a request that requires a negotiated security mechanism.

### 5xx — Server Errors

The 5xx responses are the "Server Error" responses, generated by proxy servers, location servers, and redirect servers.

- **500 Server Internal Error** — The server could not fulfil the request due to some unexpected condition.
- **501 Not Implemented** — The SIP request method is not implemented here.
- **502 Bad Gateway** — The server received an invalid response from a downstream server while trying to fulfil a request.
- **503 Service Unavailable** — The server is in maintenance or is temporarily overloaded and cannot process the request.
- **504 Server Time-out** — The server tried to access another server while trying to process a request, no timely response.
- **505 Version Not Supported** — The SIP protocol version in the request is not supported by the server.
- **513 Message Too Large** — The request message length is longer than the server can process.
- **555 Push Notification Service Not Supported** — The server does not support the push notification service specified in the pn-provider SIP URI parameter.
- **580 Precondition Failure** — The server is unable or unwilling to meet some constraints specified in the offer.

### 6xx — Global Failures

The 6xx responses are the "Global Error" responses, indicating that a server has definitive information about a particular user and not just the particular instance indicated by the Request-URI.

- **600 Busy Everywhere** — All possible destinations are busy.
- **603 Decline** — Destination cannot or does not wish to participate in the call, no alternative destinations.
- **604 Does Not Exist Anywhere** — The server has authoritative information that the requested user does not exist anywhere.
- **606 Not Acceptable** — The user's agent was contacted successfully but some aspects of the session description were not acceptable.
- **607 Unwanted** — The called party did not want this call from the calling party. Future attempts from the calling party are likely to be similarly rejected.
- **608 Rejected** — The terminating carrier has blocked a call due to suspected fraud, preventing it from reaching the intended end user. See [Telnyx: How to handle spam/scam likely](https://support.telnyx.com/en/articles/4088988-telnyx-how-to-handle-spam-scam-likely).
