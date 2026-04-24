---
title: P-Charge-Info Header
summary: A SIP header that identifies the billing number (DID) for outbound calls, enabling accurate call attribution and routing through Telnyx SIP trunks.
sources:
  - url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/p-charge-info-header/index
    content_hash: f7435cbd4cc60c0c877b14a3f861bbb2a2fae9854b13f1cea8b0e2cec03d8b99
updated_at: 2026-04-10T00:00:00Z
---

# P-Charge-Info Header

A SIP header that identifies the billing number (DID) for outbound calls, enabling accurate call attribution and routing through Telnyx SIP trunks.

## Header format

```
P-Charge-Info: <sip:+15551234567@sip.telnyx.com>
```

The value must be:

* A valid DID associated with the Telnyx SIP connection
* In E.164 format (e.g., `+15551234567`)
* Wrapped in SIP URI format

## Use cases

* Multiple DIDs on a single SIP connection
* Call detail record (CDR) attribution per DID
* Billing and usage tracking per number
* Carrier-side call routing based on originating number

## Requirements

* Telnyx SIP connection configured for outbound calling
* Valid DID ownership and assignment to the connection
* PBX access to modify dialplan or trunk configuration

## Troubleshooting

| Issue                              | Solution                                              |
| ---------------------------------- | ----------------------------------------------------- |
| Header not appearing in SIP INVITE | Verify dialplan reload completed successfully         |
| Call rejected by Telnyx            | Confirm DID is associated with the SIP connection     |
| Wrong number in header             | Check variable substitution in dynamic configurations |
| FreePBX updates overwrite config   | Use `extensions_custom.conf` to persist changes       |

## Alternative identification methods

For connections sharing authentication credentials:

| Method                  | Description                                 |
| ----------------------- | ------------------------------------------- |
| P-Charge-Info header    | SIP header identifying billing number       |
| Tech prefix             | 4-digit identifier prepended to destination |
| IP authentication token | Token-based connection validation           |
