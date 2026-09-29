---
title: "Porting Numbers Away from Aircall to Telnyx"
summary: "Step-by-step guide for porting numbers from Aircall, including how to get your carrier-level account number and PIN. See Telnyx guidance and requirements."
sources:
- url: "https://support.telnyx.com/en/articles/14708128-porting-numbers-away-from-aircall-to-telnyx"
updated_at: 2026-07-08T00:00:00Z
tags: [support-docs]
source_path: "support-docs/en--articles--14708128-porting-numbers-away-from-aircall-to-telnyx.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/en--articles--14708128-porting-numbers-away-from-aircall-to-telnyx.md -->

# Porting Numbers Away from Aircall to Telnyx

Step-by-step guide for porting numbers from Aircall, including how to get your carrier-level account number and PIN. See Telnyx guidance and requirements.




## Overview

Porting numbers away from Aircall to Telnyx is possible, but requires a few extra steps because Aircall is a **reseller** — they don't own the underlying phone numbers directly. The numbers sit on Aircall's underlying carrier infrastructure (typically Twilio), which means the port authorization must come from the underlying carrier, not Aircall itself.

## What You Need Before Submitting

To successfully port numbers away from Aircall, you'll need to gather information from **two places**: Aircall and the underlying carrier.

### 1. Contact Aircall Support First

Before submitting your port request in Telnyx, contact Aircall and ask them for:

* The **underlying carrier** for your numbers (most commonly Twilio, but can vary by country/region)
* Your **account number** as it appears on their carrier records
* The **PIN or passcode** required to authorize the port

**⚠️ Important:** The PIN you need is NOT your Aircall login password. It's a carrier-level passcode associated with your account on Aircall's underlying infrastructure. Aircall support can provide this.

### 2. Information to Include in Your Telnyx Port Request

|  |  |
| --- | --- |
| Field | What to Enter |
| Account Number | The account number provided by Aircall (not your Aircall account ID) |
| PIN / Passcode | The carrier-level PIN provided by Aircall |
| Authorized Name | The name on the Aircall account (exactly as it appears) |
| Service Address | The address on file with Aircall |

## Common Rejection Reasons

|  |  |  |
| --- | --- | --- |
| Rejection | Cause | Fix |
| PASSCODE\_PIN\_INVALID | Wrong PIN submitted | Contact Aircall support for the correct carrier-level PIN |
| ACCOUNT\_NUMBER\_MISMATCH | Wrong account number | Confirm the account number with Aircall — it may differ from your Aircall customer ID |
| BUSINESS\_NAME\_MISMATCH | Name doesn't match carrier records | Use the exact legal name on the Aircall account |
| SERVICE\_ADDRESS\_MISMATCH | Address doesn't match | Use the address registered on the Aircall account, not your billing address |

## Estimated Timeline

Aircall number ports typically follow standard US/CA porting timelines:

* **Simple ports (1–5 numbers):** 3–7 business days
* **Complex ports (6+ numbers or mixed rate centers):** 5–15 business days

## Tips for a Smooth Port

1. **Don't cancel Aircall before the port completes.** Keep your Aircall account active until all numbers have successfully ported to Telnyx.
2. **Gather credentials before submitting** — incorrect information causes rejections and delays of 3–5 business days per attempt.
3. If Aircall is unresponsive, contact [porting@telnyx.com](mailto:porting@telnyx.com) — we can help identify the underlying carrier.
