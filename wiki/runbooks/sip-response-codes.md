---
title: SIP Response Codes
summary: Telnyx-specific SIP response codes for diagnosing call failures.
sources:
  - url: https://developers.telnyx.com/docs/voice/sip-trunking/troubleshooting/response-codes/index
    content_hash: 3521ae365d4e42b84d2d70a0f88e4eb2736073a997135229c5cea28dfdf59a56
updated_at: 2026-04-10T00:00:00Z
---

# SIP Response Codes

Telnyx-specific SIP response codes for diagnosing call failures.

## D-Series Codes (4XX Responses)

Client-side errors related to account configuration, limits, and permissions.

### D1X: Account & Connection Issues

| Code    | SIP Status | Description                                        | Resolution                                                      |
| ------- | ---------- | -------------------------------------------------- | --------------------------------------------------------------- |
| D1      | 403        | Concurrent outbound calls exceed global limit      | Reduce active calls or increase limit in outbound voice profile |
| D10-D17 | 403        | Connection, profile, or account disabled/forbidden | Verify SIP connection and outbound voice profile are active     |
| D18     | 404        | SIP connection inactive                            | Enable the SIP connection                                       |
| D19     | 404        | Account blocked (billing)                          | Review account balance and payment method                       |

### D2X: Profile & Channel Limits

| Code    | SIP Status | Description                                          | Resolution                                     |
| ------- | ---------- | ---------------------------------------------------- | ---------------------------------------------- |
| D2      | 403        | Outbound profile concurrent call limit exceeded      | Reduce active calls or increase profile limit  |
| D21     | 480        | No destination/forwarding number associated          | Verify destination number is valid and active  |
| D22     | 403        | Channel limit exceeded (DID, connection, or profile) | Check channel allocations                      |
| D24     | 403        | Rate per minute exceeds profile maximum              | Adjust rate limits in outbound voice profile   |
| D25-D29 | 403        | Authentication or connection validation failed       | Verify SIP credentials and connection settings |

### D3X: Connection & URI Issues

| Code    | SIP Status | Description                                      | Resolution                                       |
| ------- | ---------- | ------------------------------------------------ | ------------------------------------------------ |
| D3      | 403        | Connection concurrent call limit exceeded        | Reduce active calls or increase connection limit |
| D30-D31 | 403        | Invalid SIP URI or subdomain                     | Verify SIP URI format and subdomain settings     |
| D35     | 403        | Invalid caller ID format                         | Use E.164 format (e.g., +12125551234)            |
| D36     | 403        | Using another account's DID as caller ID         | Use only assigned phone numbers                  |
| D38     | 403        | No outbound voice profile assigned to connection | Assign an outbound voice profile                 |

### D4X: Routing & Destination Issues

| Code | SIP Status | Description                                | Resolution                                   |
| ---- | ---------- | ------------------------------------------ | -------------------------------------------- |
| D40  | 404        | Destination exists but no route available  | Verify destination and routing configuration |
| D41  | 403        | Dialed prefix forbidden (fraud prevention) | Contact support to enable destination        |
| D42  | 405        | SIP REFER not allowed                      | Enable call transfer in connection settings  |
| D49  | 403        | NANPA origination number lacks valid LRN   | Ensure phone number has LRN data             |

### D5X: Channel Billing & Verification

| Code    | SIP Status | Description                                | Resolution                               |
| ------- | ---------- | ------------------------------------------ | ---------------------------------------- |
| D5      | 486        | Legacy channel billing limit exceeded      | Review channel billing settings          |
| D51     | 403        | Non-Telnyx number not verified             | Use Verified Numbers API                 |
| D52-D54 | 403        | Restricted origination number              | Verify number ownership and status       |
| D56     | 486        | Global channel billing limit exceeded      | Contact support                          |
| D57     | 403        | HD voice disabled for phone number         | Enable HD voice in phone number settings |
| D59     | 404        | Special/short number unsupported by region | Use supported number type                |

### D6X: Account Tier Restrictions

| Code    | SIP Status | Description                            | Resolution                             |
| ------- | ---------- | -------------------------------------- | -------------------------------------- |
| D60-D61 | 403        | Account tier requires verified numbers | Upgrade account tier or verify numbers |
| D63     | 403        | Number port pending                    | Wait for port completion               |
| D64-D65 | 403        | Regulatory requirement pending         | Complete regulatory documentation      |

### D7X, D8X, D9X: Additional Restrictions

| Code | SIP Status | Description                                  | Resolution                            |
| ---- | ---------- | -------------------------------------------- | ------------------------------------- |
| D7   | 403        | No outbound voice profile assigned           | Assign an outbound voice profile      |
| D8   | 404        | Missing E911 caller ID                       | Configure E911 caller ID              |
| D9   | 403        | International destination rate limit reached | Review rate limits or contact support |

## P-Series Codes (Protocol Issues)

SIP protocol violations or proxy-level issues.

### P0X: Protocol Violations

| Code    | SIP Status | Description                              | Resolution                                      |
| ------- | ---------- | ---------------------------------------- | ----------------------------------------------- |
| P01     | 403        | Invalid Request-URI (proxy anycast IP)   | Use correct contact header                      |
| P02     | 403        | CANCEL without matching INVITE           | Only send CANCEL for active INVITE transactions |
| P04     | 403        | REGISTER with To tag (RFC non-compliant) | Remove To tag from REGISTER requests            |
| P05-P06 | 403        | CPS limit or message size exceeded       | Reduce call rate or message size                |
| P14-P16 | 403        | Contact header length violation          | Shorten contact header to under 512 bytes       |
| P18     | 403        | Empty destination in Request-URI or To   | Include valid destination in SIP headers        |
| P29     | 500        | REGISTER processing failure              | Retry registration or contact support           |
| P51     | 403        | Contact header exceeds 512 bytes         | Reduce contact header length                    |
| P81-P83 | 403        | Username validation issues               | Verify SIP username format                      |
| P93     | 403        | Hop count exceeded                       | Check for routing loops                         |

## R-Series Codes (Registration & Authentication)

SIP registration and authentication issues.

| Code    | SIP Status | Description                                 | Resolution                                     |
| ------- | ---------- | ------------------------------------------- | ---------------------------------------------- |
| R14     | 403        | Empty authentication username               | Provide valid SIP username                     |
| R16-R18 | 403        | Invalid/short/mismatched username           | Use alphanumeric username matching credentials |
| R47     | 403        | Multiple Contact addresses in REGISTER      | Register one contact address per request       |
| RG1     | 480        | User not registered (credential connection) | Register SIP client before making calls        |

## Routing & Media Codes

### PE-Series: Routing Failures

| Code    | SIP Status | Description     | Resolution                      |
| ------- | ---------- | --------------- | ------------------------------- |
| PE1-PE6 | 503        | No routes found | Verify destination is reachable |

### T-Series: Termination Issues

| Code | SIP Status | Description                          | Resolution                            |
| ---- | ---------- | ------------------------------------ | ------------------------------------- |
| TV1  | 503        | Downstream carrier termination issue | Retry call or use alternative routing |
| TM1  | 403        | No rates for destination prefix      | Contact support about coverage        |

### B-Series: Media Issues

| Code | SIP Status | Description                              | Resolution                                         |
| ---- | ---------- | ---------------------------------------- | -------------------------------------------------- |
| B3   | 488        | SRTP mismatch - encrypted media expected | Enable SRTP in SIP client or disable in connection |

## 488 Not Acceptable Media

Media negotiation failures:

| Scenario                 | Resolution                       |
| ------------------------ | -------------------------------- |
| Private IP in SDP        | Use public IP addresses          |
| T.38 fax mismatch        | Verify T.38 settings match       |
| IPv6 media addresses     | Use IPv4 (IPv6 not supported)    |
| Unsupported codecs       | Use G.711, G.722, G.729, or Opus |
| SDP encryption conflicts | Ensure consistent SRTP settings  |


## Related Pages

- [Response](../runbooks/response.md)
- [API error codes](../reference/api-error-codes.md)
- [Response Format](../runbooks/response-format.md)
