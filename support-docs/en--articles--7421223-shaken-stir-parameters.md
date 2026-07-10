---
source_url: https://support.telnyx.com/en/articles/7421223-shaken-stir-parameters
scraped: 2026-07-08
content_hash: c046bb41d844fe4c70629bd7afd01ab5819661455fb182a876a212d5a2607585
---

SHAKEN/STIR Parameters | Telnyx Help Center

[Skip to main content](#main-content)

# SHAKEN/STIR Parameters

Telnyx customers can now get more granular information on call attestation and verification results with new SHAKEN/STIR verstat parameters

Written by Telnyx Engineering

March 3, 2026

Table of contents

# **How to interpret SHAKEN/STIR verstat parameters and ensure secure call identity verification**

As part of our ongoing efforts to improve the SHAKEN/STIR framework, Telnyx has introduced additional values to the *verstat* parameter in our SIP headers.

This update provides Telnyx customers with more granular information regarding originating Caller ID attestation and verification results.

The *verstat* parameter is included in the P-Asserted-Identity SIP header and includes information about the caller identity validation and attestation level.

Previously, the possible values were *TN-Validation-Passed*, *TN-Validation-Failed*, or *No-TN-Validation* depending on verification results of the PASSPorT and attestation level.

This verification is done for inbound calls from the PSTN as well as on-net calls from Telnyx customers to other Telnyx customers.

## Introducing two additional *verstat* values:

* TN-Validation-Passed-B: Indicates that identity header verification is successful, and the call has a B attestation.
* TN-Validation-Passed-C: Indicates that identity header verification is successful, and the call has a C attestation.

With these new values, Telnyx customers will have more detailed information about the origin of incoming calls and the level of attestation.

This can be especially useful for customers who need to verify the identity of incoming calls to prevent fraud or for regulatory compliance.

It's important to note that these new *verstat* values will be included in the SIP headers passed along to Telnyx customers.   
This means that customers can access this information directly through their own systems and tools.

Note:  
When using SHAKEN/STIR, the `shaken_stir_param` controls whether the identity header is present in the B leg, it requires that the following conditions both be true to successfully pass the identity header.

* `shaken_stir_enabled` is `true` (from **CPB connection settings** — the B-leg)

* `cpb_transport_protocol` is `"TCP"` or `"TLS"`

Identity headers are **not** sent over UDP to prevent fragmentation issues.   
​

## Verstat Values Summary

|  |  |
| --- | --- |
| **Verstat value** | **Description** |
| TN-Validation-Passed | Identity header verification is successful, and the caller has an A attestation |
| TN-Validation-Failed | Identity header verification failed as the certificate Telnyx received was deemed invalid. |
| No-TN-Validation | No verification took place because the Identity header was not provided |
| TN-Validation-Passed-B | Identity header verification is successful, and the caller has a B attestation |
| TN-Validation-Passed-C | Identity header verification is successful, and the caller has a C attestation |

Below you can find a P-Asserted-Identity example:  
​

```
P-Asserted-Identity:"John Doe"<sip:+18889809750@sip.telnyx.com;verstat=TN-Validation-Passed>
```

For more information on the SHAKEN/STIR framework and how it works, please visit our [resource center](https://telnyx.com/resources).

---

Related Articles

[STIR/SHAKEN With Telnyx](https://support.telnyx.com/en/articles/5402969-stir-shaken-with-telnyx)[Robocall Mitigation Database](https://support.telnyx.com/en/articles/5544430-robocall-mitigation-database)[Canadian STIR/SHAKEN Implementation FAQs](https://support.telnyx.com/en/articles/5761463-canadian-stir-shaken-implementation-faqs)[Inbound Call Screening](https://support.telnyx.com/en/articles/8037040-inbound-call-screening)[Understanding SIP 603+ carrier rejections](https://support.telnyx.com/en/articles/15395095-understanding-sip-603-carrier-rejections)

Did this answer your question?

😞😐😃

Table of contents
