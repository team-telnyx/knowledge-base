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

*Part 3 of 4 — see also: [Part 1](telnyx-platform-overview-and-sip-technical-reference--part-1.md), [Part 2](telnyx-platform-overview-and-sip-technical-reference--part-2.md), [Part 4](telnyx-platform-overview-and-sip-technical-reference--part-4.md)*

Telnyx is a global Communications Platform as a Service (CPaaS) provider offering voice, messaging, real-time communications, AI inference, storage, and workflow automation over a privately-owned IP network. This page consolidates Telnyx's network specifications, supported SIP protocols and methods, interoperability partners, and configuration guidance for common PBX and softphone integrations.

## SIP PRACK Protocol

PRACK (Provisional Response Acknowledgement) is defined in [RFC 3262](https://www.rfc-editor.org/rfc/rfc3262), "Reliability of Provisional Responses in the Session Initiation Protocol (SIP)", published by the IETF in June 2002. PRACK is a SIP extension that allows for the reliable delivery of provisional responses (1xx) in a SIP call. By default, provisional responses in a transaction are not acknowledged. PRACK is used to ensure that provisional responses (generally excluding 100 Trying) are received by the client and to handle any lost or delayed responses, especially when communicating with the PSTN.

PRACK works by sending a PRACK request, which is a SIP request similar to an INVITE or ACK, to acknowledge receipt of a provisional response.

### Telnyx PRACK Behaviour

Telnyx supports PRACK for inbound and outbound calls through its network.

- When a SIP INVITE message is sent by a client with the "Supported" header containing the value "100rel", it indicates that the sender supports PRACK. Telnyx will send provisional responses with RSEQ header values and expects the customer's client to respond with a PRACK.
- If the customer's client sends "100rel" as a value in the "Supported" header but doesn't actually support or send PRACK, Telnyx will eventually time the call out with a **504 gateway timeout** response, and the reason header will contain "prack timeout" as the reason for the call ending.

### Enabling PRACK on a SIP Connection

Customers can enable PRACK on their [SIP Connection](sip-connection.md) inbound settings, specifically under "Advanced":

![Prack Setup screenshot](_images/c44dce9de72458c2.png)

When enabled, for any inbound calls the customer receives, Telnyx will send a SIP INVITE with "100rel" as a value in the "Supported" header. If the customer's device supports PRACK, Telnyx expects to receive provisional responses containing RSEQ header and values, which Telnyx will then PRACK.

## Interoperability Partners

Telnyx interoperates with a wide range of PBX, softphone, and unified communications platforms. Refer to the [configuration guides collection](https://support.telnyx.com/en/collections/133118-configuration-guides) for detailed setup instructions.

- 3CX
- Adtran
- AudioCodes
- Asterisk
- Avaya
- Broadsoft
- Cisco CallManager
- Counterpath
- Edgewater Networks
- Elastix
- Fonality
- FreePBX
- FreeSWITCH
- Grandstream
- IAUG - International Avaya Users Group
- Mitel
- Patton
- PBX in a Flash
- Switchvox
- Thirdlane
- Vicidial
- Yealink
- [Zoiper](https://support.telnyx.com/en/articles/6133517-zoiper-communicator)
