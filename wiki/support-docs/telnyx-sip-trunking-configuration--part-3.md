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
