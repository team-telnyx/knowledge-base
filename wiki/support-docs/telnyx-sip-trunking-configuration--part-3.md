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

*Part 3 of 4 — see also: [Part 1](telnyx-sip-trunking-configuration--part-1.md), [Part 2](telnyx-sip-trunking-configuration--part-2.md), [Part 4](telnyx-sip-trunking-configuration--part-4.md)*

A comprehensive guide to configuring and managing SIP trunking with Telnyx, covering connection types, authentication methods, inbound/outbound settings, failover and retry logic, SRV record handling, number formats, SIP protocols, STUN/TURN servers, SIP URI calling, response codes, and advanced features such as SHAKEN/STIR, PRACK, and Record-Route headers.

## SIP Methods and Responses

SIP uses request methods and response codes to manage call sessions. The six basic request methods are:

| Method | Purpose |
|---|---|
| INVITE | Establishes a session |
| ACK | Confirms an INVITE request |
| BYE | Ends a session |
| CANCEL | Cancels session establishment |
| REGISTER | Communicates user location |
| OPTIONS | Communicates capabilities |

Additional methods include PRACK, SUBSCRIBE, NOTIFY, PUBLISH, INFO, MESSAGE, and UPDATE.

### SIP Response Classes

| Class | Meaning | Example |
|---|---|---|
| 1xx | Informational (provisional) | 180 Ringing |
| 2xx | Success | 200 OK |
| 3xx | Redirection | 301 Moved Permanently |
| 4xx | Client error | 404 Not Found |
| 5xx | Server error | 503 Service Unavailable |
| 6xx | Global failure | 603 Decline |

**Note:** Telnyx does not send SIP OPTIONS to customer connections but does accept and respond to SIP OPTIONS from customer user agents.

## Telnyx-Specific SIP Response Codes

Telnyx extends standard SIP response codes with custom identifiers (format: D1X–D9X, plus PX, RX, TX, VX ranges) to provide more granular error context.

### Common Codes

| Code | SIP Response | Meaning |
|---|---|---|
| B3 | 488 | Media encryption required — connection configured for SRTP but INVITE lacks encrypted media |
| D1 | 403 | User channel limit exceeded — global account outbound limit reached |
| D2 | 403 | Outbound profile channel limit exceeded |
| D3 | 403 | Connection channel limit exceeded |
| D4 | 486 | User Busy — connection inbound channel limit exceeded |
| D7/D38 | 403 | Connection has no Outbound Profile assigned |
| D13 | 403 | Dialed number not in whitelisted countries |
| D14 | 404 | Dialed number is not valid |
| D15 | 403 | Outbound Profile is disabled |
| D16 | 403 | Connection is disabled |
| D17 | 403 | Account is disabled/blocked |
| D22 | 403 | Channel limits exceeded (user, profile, or connection) |
| D29 | 403 | Invalid X-Telnyx-Token or IP |
| D35 | 403 | Invalid Caller Origination Number (must be +E.164) |
| D51 | 403 | Unverified origination number — non-Telnyx number not verified |
| PE1–PE6 | 503 | Service Unavailable / No routes found |
| P01 | 403 | Invalid R-URI — Telnyx anycast IP in R-URI instead of B2BUA contact IP |
| P05/P15 | 503 | CPS (Calls Per Second) limit reached |
| P06 | 513 | SIP message too large (over 6144 bytes) |
| P81 | 403 | Username 3 characters or fewer (minimum 4) |
| P82 | 403 | Invalid characters in username |
| R47 | 403 | Too many contacts in REGISTER request |
| RG1 | 480 | User not registered |

### Special Note on SIP 488

A 488 Not Acceptable Here response with reason "incompatible destination" typically relates to SDP misconfiguration. Common causes include:

1. Private IP address in SDP (`c=10.10.10.10`)
2. T.38 re-invite without T.38 gateway enabled
3. IPv6 media IP address (not supported — use IPv4)
4. Unsupported codec
5. Encryption media attributes mismatch (offered when not configured, or not offered when configured)

## SHAKEN/STIR Parameters

Telnyx includes `verstat` (verification status) parameters in the `P-Asserted-Identity` SIP header to convey caller identity attestation and verification results:

| Verstat Value | Description |
|---|---|
| TN-Validation-Passed | A attestation — identity verification successful |
| TN-Validation-Passed-B | B attestation — identity verification successful |
| TN-Validation-Passed-C | C attestation — identity verification successful |
| TN-Validation-Failed | Identity header verification failed (invalid certificate) |
| No-TN-Validation | No Identity header was provided; no verification took place |

**Important:** Identity headers are not sent over UDP (to prevent fragmentation). To pass the identity header on the B-leg, both `shaken_stir_enabled` must be `true` on the CPB connection and `cpb_transport_protocol` must be `"TCP"` or `"TLS"`.

## PRACK Protocol

PRACK (Provisional Response Acknowledgement), defined in [RFC 3262](https://www.rfc-editor.org/rfc/rfc3262), ensures reliable delivery of provisional 1xx responses.

- When a client sends an INVITE with `Supported: 100rel`, Telnyx sends provisional responses with RSEQ headers and expects a PRACK in return.
- If a client advertises `100rel` support but doesn't send PRACK, the call times out with **504 Gateway Timeout** and reason "prack timeout".
- PRACK can be enabled on the SIP Connection's inbound Advanced settings, which causes Telnyx to send INVITEs with `Supported: 100rel` for inbound calls.

## Record-Route Headers

The **Via** header tracks the path of request messages and provides a route for responses back to the originator. The **Record-Route** header ensures that subsequent mid-dialog requests (ACKs, BYEs) follow the same path as the initial INVITE.

When Telnyx's INVITE includes Record-Route headers, the customer's 200 OK response must mirror these headers (in correct order) so that the ACK is routed back through the same proxies. If Route headers are omitted or reordered in the 200 OK, the ACK may not reach the callee, causing the call to drop with an **ack_timeout** hang-up cause.

### Common ACK Failure Causes

1. **Missing or reordered Route headers** — The client must reverse the order of Record-Route headers from the 200 OK when constructing Route headers in the ACK.
2. **Malformed ACK missing CRLF** — Carriage return/line feed characters are required for proper header delineation.
3. **CSeq mismatch** — The CSeq number in the ACK must match the CSeq in the 200 OK, not an earlier INVITE. For example, if authentication caused the INVITE CSeq to increment from 2 to 3, the ACK must use CSeq 3.

## Concurrent Call Limits

By default, new Telnyx accounts have a global concurrent outbound call limit of **2**. After Level 2 verification, this increases to **10**. To increase further, contact [support@telnyx.com](mailto:support@telnyx.com) with your use case (especially for limits above 100). When the limit is reached, Telnyx returns **D1 — 403 User channel limit exceeded D1**.

Channel limits can also be set at the SIP Connection level (inbound and outbound separately) and at the Outbound Voice Profile level.

## Multiple Device Registration

A credentials-based SIP Connection can be registered to any device, but **only one device can be actively registered at a time**. If you register to a softphone after registering to an IP phone, only the softphone will receive calls — the IP phone becomes unregistered. To ring multiple devices simultaneously, enable the **Simultaneous Ringing** feature in the SIP Connection's inbound settings.

## Telephony Credential Types

### SIP Connection Credentials

Standard username/password authentication created in the portal. Ideal for simple setups and softphone integration.

### On-Demand Credentials

Created programmatically via the Telnyx REST API (`POST /v2/telephony_credentials`). These credentials are for **outbound calls only** — inbound calls directly to on-demand credentials are not supported. The typical use case is call centers where agents log in with on-demand credentials via a WebRTC client, and a backend application uses the Call Control API to dial available agents when inbound calls arrive.

### JSON Web Tokens (JWTs)

Created programmatically by POSTing to `https://api.telnyx.com/v2/telephony_credentials/<credential_id>/token`. JWTs expire after **24 hours** and provide temporary, secure access — ideal for guest or onboarding scenarios.

You can test all credential types using the [Telnyx WebRTC test application](https://webrtc.telnyx.com/).
