---
title: STIR/SHAKEN SIP Header Parameters
summary: Telnyx provides call attestation information through the `verstat` parameter in the `P-Asserted-Identity` SIP header.
sources:
  - url: https://developers.telnyx.com/docs/voice/stir-shaken/sip-header-parameters/index
    content_hash: 6876f5b530e1f8fdc0d064d35368c7141de717fb974a89330a14cce8b96bff73
updated_at: 2026-04-10T00:00:00Z
---

# STIR/SHAKEN SIP Header Parameters

Telnyx provides call attestation information through the `verstat` parameter in the `P-Asserted-Identity` SIP header.

## Verstat parameter

```
P-Asserted-Identity: "John Doe" <sip:+18889809750@sip.telnyx.com;verstat=TN-Validation-Passed>
```

| Value                    | Description                                 |
| ------------------------ | ------------------------------------------- |
| `TN-Validation-Passed`   | Verification succeeded, A-level attestation |
| `TN-Validation-Passed-B` | Verification succeeded, B-level attestation |
| `TN-Validation-Passed-C` | Verification succeeded, C-level attestation |
| `TN-Validation-Failed`   | Verification failed (invalid certificate)   |
| `No-TN-Validation`       | No Identity header provided                 |

## Call scope

The `verstat` parameter is included for:

* Inbound calls from the PSTN
* On-net calls between Telnyx customers
