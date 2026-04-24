---
title: External Call Transfers
summary: External transfers move an inbound PSTN call to an external destination while preserving the original caller's identity.
sources:
  - url: https://developers.telnyx.com/docs/voice/sip-trunking/features/external-transfers/index
    content_hash: 9c56519556272d0e8e72712e0f4ed965f43f1d82674a0bf2d0f1acfa909039cf
updated_at: 2026-04-10T00:00:00Z
---

# External Call Transfers

External transfers move an inbound PSTN call to an external destination while preserving the original caller's identity.

## Call flow

1. Caller A dials Telnyx number B
2. Telnyx routes the call to the SIP endpoint (A → B)
3. The endpoint initiates a transfer to external number C
4. Telnyx places a new outbound call (A → C)

## Validation requirements

Telnyx validates external transfers to prevent unauthorized call spoofing:

* **Active call verification**: An active inbound call must exist from the original caller to the Telnyx number
* **Diversion header**: The outbound call leg must include a SIP `Diversion` header containing the Telnyx number

**Required Diversion header format:**

```
Diversion: <sip:+12125551234@sip.telnyx.com>
```

Transfers are rejected when no active call can be matched, the Diversion header is missing, or the header contains an unauthorized number.

## Transfer types

### Blind transfer

Immediate transfer without announcement:

```
REFER sip:+13035559876@sip.telnyx.com SIP/2.0
Refer-To: <sip:+13035559876@sip.telnyx.com>
```

### Attended transfer

1. Place the original call on hold
2. Dial the transfer destination
3. Announce the transfer
4. Complete with SIP REFER

## Programmable Voice implementation

### Transfer command

[POST /v2/calls//actions/transfer](https://developers.telnyx.com/api-reference/call-commands/transfer-call):

```json theme={null}
{
  "to": "+13035559876",
  "from": "+12125551234"
}
```

### Dial with bridge

[POST /v2/calls](https://developers.telnyx.com/api-reference/call-commands/dial) with `link_to` and `bridge_intent`:

```json theme={null}
{
  "connection_id": "1234567890",
  "to": "+13035559876",
  "from": "+12125551234",
  "link_to": "v3:abc123def456",
  "bridge_intent": true
}
```

### TeXML Dial

[\ verb](dial.md):

```xml theme={null}

  <Dial callerId="+12125551234">
    +13035559876

```

## Troubleshooting

If transfers fail, verify:

1. An active inbound call exists on the Telnyx number
2. The Diversion header includes the correct Telnyx number
3. The outbound voice profile allows calls to the destination
4. The destination number is in E.164 format
