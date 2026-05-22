---
title: Telnyx SIP Routing, DNS, and Protocol Behavior
summary: A practical guide to how Telnyx handles SIP signaling, DNS/SRV resolution,
  media anchoring, SDP/codecs, PRACK, and record-route/route handling—plus key connection
  settings and the most common Telnyx-specific SIP response codes to aid configuration
  and troubleshooting.
sources:
- url: https://support.telnyx.com/en/articles/10666839-how-telnyx-handles-srv-records-for-sip-calls
  content_hash: 0cef1f7259d091dd8343c8d758b0d2fa2b0c2d9bb5bb6134c784337542cb36f2
- url: https://support.telnyx.com/en/articles/1130705-sip-protocols-that-telnyx-uses
  content_hash: f72fabffb4f0bf1fec6909eaf338aba39094a0c122afbd248f92445626b1ec5d
- url: https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats
  content_hash: ae0249a568c6b4023a64a10eb36a37e2e06ae07df6836ed8b84e8046fdbd3a58
- url: https://support.telnyx.com/en/articles/1130723-voip-telecommunications-protocols
  content_hash: 4785f93c7e366ac4c135a982dd1406dea7921fff94dd16aec5199a5696c7603a
- url: https://support.telnyx.com/en/articles/2925713-sip-uri-calling
  content_hash: 4b83ab42762f3a83a072070bc3ea1dc1bb667ab4852be20c986cdeac3b4a65a9
- url: https://support.telnyx.com/en/articles/3192298-audio-and-codecs
  content_hash: 47e81daed07da1818e15109f33324839bf4e8fbce6e1df6a1477f224b0bf4bd1
- url: https://support.telnyx.com/en/articles/4304898-sip-trunking-methods-requests-responses
  content_hash: f394350a1694bd5825c36fc53574213f1bb18aeb3e450f5af3b0a55cbf551209
- url: https://support.telnyx.com/en/articles/4351104-sip-connection-settings
  content_hash: 6e9a14bde21a6bd404edbea4275b2cabec87df380f716828bc63fd76fa84453f
- url: https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings
  content_hash: f6aaa104aed9a071b32805abcb437662ae2e7f21a73c95bc937aafae9e0032ed
- url: https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes
  content_hash: bd541565829c264faa4b8da2da27a220bb6b5bb61b45d5e8c70c2acb346b84a0
- url: https://support.telnyx.com/en/articles/5271423-guide-to-sip-anchorsite-settings
  content_hash: 949be043d77cb281bce867aaa5ef90c7051ef00dbd55615b9966c28b7d21255f
- url: https://support.telnyx.com/en/articles/6902981-understanding-sip-prack-protocol
  content_hash: 6fa6164cd9b3d6093e2f0b2ca3eacd1c2cafde4ccc18fa2a6efa675a746eca9f
- url: https://support.telnyx.com/en/articles/9133298-sip-record-route-headers
  content_hash: fa5e0813406e921edf5ce6ea7b200b37a64f5f94d9cd4b45682591f23438ec67
- url: https://support.telnyx.com/en/collections/3968237-telnyx-sip-trunking-configurations
  content_hash: 2785ee7fa081385c678b18f041c58a71d09067754fb5fa8ffde7a8f41a7ed6ff
updated_at: 2026-05-20T14:34:53Z
---

# Telnyx SIP Routing, DNS, and Protocol Behavior

*Part 2 of 2 — see also: [Part 1](telnyx-sip-routing-dns-and-protocol-behavior--part-1.md)*

A practical guide to how Telnyx handles SIP signaling, DNS/SRV resolution, media anchoring, SDP/codecs, PRACK, and record-route/route handling—plus key connection settings and the most common Telnyx-specific SIP response codes to aid configuration and troubleshooting.

## Record-Route, Via, and correct ACK routing
- Via headers record the path of requests so responses can traverse back correctly.
- Record-Route headers inserted by proxies ensure all in-dialog requests (ACK, BYE, re-INVITEs) follow the same path. The UAC must reverse the Record-Route set received in the first final response to build Route headers in subsequent requests.
- Omitting mirrored Record-Route in your 200 OK or misordering/missing Route headers in your ACK can prevent the ACK from reaching the callee, leading to no media and an eventual disconnect with reason ack_timeout.
- Ensure ACK CSeq matches the final INVITE CSeq, especially after 407/401 challenges where you re-send the INVITE with an incremented CSeq.
- Ensure proper CRLF line endings; malformed headers can be ignored by SIP stacks.
- If NAT/ALG tampers with Contact/VIA, enable “Encode Contact Header” and ensure your BYE/ACK R-URI and Route set target Telnyx’s B2BUA contact, not the anycast proxy IP. Missing or reordered Route headers can also lead to 32-second post-answer drops.
See [SIP - Record Route Headers](sip-record-route-headers.md).

## Common SIP responses and Telnyx extended codes
Standard classes
- 1xx informational (e.g., 180 Ringing, 183 Session Progress)
- 2xx success (e.g., 200 OK)
- 3xx redirection, 4xx client errors, 5xx server errors, 6xx global failures
Telnyx-specific highlights (examples)
- B3 488 Media Encryption Required: your Connection requires SRTP but your SDP did not offer it.
- D21 480 Temporarily Unavailable: DID is pointed to a Connection that isn’t registered (credentials) or lacks IP/FQDN routing.
- D22 403 Channel limit exceeded: enforced at DID, Connection, or Outbound Profile as configured.
- D35 403 Invalid Caller Origination Number: Caller ID not valid; use +E.164 in From/PAID/RPID per policy.
- D38/D7 403 No Outbound Profile assigned: assign an Outbound Voice Profile to the Connection.
- D51 403 Unverified origination number: verify non-Telnyx numbers before use.
- RG1 480 Not Found: user not registered (inbound to credentials auth).
- PE1/PE2-PE6 503 No routes found: temporary routing unavailability (designed to allow failover to other carriers).
- P05/P15 503 CPS limit reached: reduce call or registration rate or request higher limits.
For the full matrix, see [Telnyx SIP Response Codes](telnyx-sip-response-codes.md) and [SIP Trunking - Methods/Requests & Responses](sip-trunking-methods-requests-responses.md).

## Troubleshooting checklist
DNS and addressing
- Remove ports from SIP URIs to use SRV; ensure SRV targets resolve; expect default 5060/5061 when no port is present. 478 Unresolvable Destination indicates DNS issues.
Registration and authorization
- For credential auth, confirm the device is registered; RG1 implies not registered. Ensure Outbound Voice Profile is assigned (D7/D38) and profiles/connections are enabled (D15/D16).
Signaling path integrity
- Preserve Record-Route: include mirrored Record-Route in 200 OK; reverse order into Route for ACK/BYE. Verify ACK CSeq matches final INVITE CSeq, and ensure proper CRLF line endings.
Media negotiation
- Offer/accept only supported codecs; prioritize G.711 for DTMF/fax. Keep ptime at 20 ms. Avoid private/IPv6 media addresses. Align SRTP settings on both sides.
PRACK
- Only advertise 100rel if your endpoint supports PRACK; otherwise disable to avoid 504 prack timeout.
NAT/ALG
- If you see 32-second drops or forbidden P01 on BYE/ACK, enable Encode Contact Header and ensure BYE/ACK target Telnyx’s B2BUA contact and include the full Route set.
Capacity and rate limits
- Monitor channel limits (Connection/DID/Outbound Profile) and CPS limits (P05/P15). Pace calls/registrations or request higher limits.
AnchorSite
- Prefer Latency; whitelist media IPs or select a fixed PoP if your signaling/media IP locality differs. Avoid setting a webhook URL on SIP trunking Connections unless you intend programmable control.
DTMF and fax
- Use RFC 2833 or SIP INFO for DTMF; for fax, use G.711 or T.38 and configure re-INVITE authority appropriately.

## Related configuration and reference
- [SIP Connection: Settings](sip-connection-settings.md)
- [SIP Connection: Inbound & Outbound Settings](sip-connection-inbound-outbound-settings.md)
- [SIP Connection: Number Formats](sip-connection-number-formats.md)
- [SIP URI Calling](sip-uri-calling.md)
- [Guide to SIP AnchorSite® Settings](guide-to-sip-anchorsite-settings.md)
- [Audio and Codecs](audio-and-codecs.md)
- [Understanding SIP PRACK Protocol](understanding-sip-prack-protocol.md)
- [SIP - Record Route Headers](sip-record-route-headers.md)
- [Telnyx SIP Response Codes](telnyx-sip-response-codes.md)
- [SIP Trunking - Methods/Requests & Responses](sip-trunking-methods-requests-responses.md)
- Telnyx specs and PoPs: [sip.telnyx.com](https://sip.telnyx.com/)
- SIP and SDP RFCs: [RFC 3261](https://www.rfc-editor.org/rfc/rfc3261), [RFC 4566](https://www.rfc-editor.org/rfc/rfc4566), [RFC 3262](https://www.rfc-editor.org/rfc/rfc3262)
