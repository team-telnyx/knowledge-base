---
title: STIR/SHAKEN Attestation Behavior
summary: Attestation levels assigned by Telnyx for outbound calls.
sources:
  - url: https://developers.telnyx.com/docs/voice/stir-shaken/attestation-behavior/index
    content_hash: f55d6fcd84ef5b77dd1a0022ed609b0b85a7a898c5028b56c82051384fbb5375
updated_at: 2026-04-10T00:00:00Z
---

# STIR/SHAKEN Attestation Behavior

Attestation levels assigned by Telnyx for outbound calls.

## Outbound calls

| Scenario                               | Attestation |
| -------------------------------------- | ----------- |
| Call from owned phone number           | A           |
| Call from non-owned or verified number | B           |

## Certificate selection

| Origin          | Destination     | Certificate |
| --------------- | --------------- | ----------- |
| US number       | Any             | US          |
| Canadian number | Canadian number | Canadian    |
| Canadian number | US number       | US          |

## Call forwarding

When call forwarding is enabled on a Telnyx number:

* Original STIR/SHAKEN passport preserved or passed through
* DIV (diversion) passport added for forwarded leg with **Attestation A**

| Route                      | Certificate |
| -------------------------- | ----------- |
| US → US                    | US          |
| Canada → Canada            | Canadian    |
| US ↔ Canada (cross-border) | US          |

## Call transfers

| Method                         | Origination Number   | Attestation | Original Passport |
| ------------------------------ | -------------------- | ----------- | ----------------- |
| SIP REFER                      | Original caller      | B           | Not preserved     |
| Call Control API (transfer)    | Specified in request | A or B\*    | Not preserved     |
| Call Control API (dial/bridge) | Specified in request | A or B\*    | Not preserved     |
| TeXML ``                 | Specified in request | A or B\*    | Not preserved     |

\*A if from number is owned, B otherwise.
