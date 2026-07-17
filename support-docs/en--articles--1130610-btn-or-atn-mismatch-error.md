---
source_url: https://support.telnyx.com/en/articles/1130610-btn-or-atn-mismatch-error
title: "BTN or ATN Mismatch Error"
description: "In this article we will explain the billing telephone number or account telephone number mismatch error and how to… See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: dd197611f6deddd780556f81ed9ca2303f68532e11f7224ad133ea847da91cf8
---







# BTN or ATN Mismatch Error

In this article we will explain the billing telephone number or account telephone number mismatch error and how to… See Telnyx guidance and requirements.




## Billing Telephone Number or Account Telephone Number Mismatch

**All Countries**

## Related Errors (for BTN or ATN)

"Wrong BTN", "Wrong ATN"

**What does it mean?**

Carriers require that a single telephone number is designated as the primary number for the account. This is typically referred to as the Billing Telephone Number (BTN) or the Account Telephone Number (ATN). If you have multiple accounts, they will likely have different BTNs/ATNs.

When submitting a port request, your existing carrier may require that Telnyx provide the BTN or ATN as a way of validating the port request. A BTN/ATN mismatch error occurs when the number submitted doesn't match what the carrier has on the Customer Service Record (CSR). The BTN is typically not found on a bill copy (except in wireless porting or toll free porting).

If you submitted a large port request, it's possible that some of the telephone numbers listed belong to a different account which would in turn have a different BTN/ATN. So while you may have listed the correct BTN/ATN for some of the numbers, other numbers may not be on that account. In this case the carrier is unlikely to specify which numbers belong to another account.

## Next steps for BTN/ATN Errors

Look to see if the BTN/ATN is specified at the top of the most recent carrier bill or invoice. If the numbers are serviced by a reseller then the BTN/ATN listed may not be the same as what the underlying carrier has on file in the CSR.

If it was not found on the bill or invoice, you'll need to contact the carrier directly to request a CSR. You can read more about obtaining CSRs.

## Special note for resellers

In the case where the end customer purchased service through a reseller, mismatched BTNs can also happen because the end customer wrongly submits the reseller’s phone number as their own BTN. When a losing reseller is involved, the number might actually belong to the reseller instead of the end customer. The customer might not realize that. When submitting their BTN or service address they may use their own instead of the BTN and service address of the reseller.

---

Related Articles

[Obtaining a CSR From Your Carrier](https://support.telnyx.com/en/articles/1130614-obtaining-a-csr-from-your-carrier)[Invalid Reseller Error](https://support.telnyx.com/en/articles/1130619-invalid-reseller-error)[Porting Error Messages](https://support.telnyx.com/en/articles/1618776-porting-error-messages)[How to fill out an LOA](https://support.telnyx.com/en/articles/2034326-how-to-fill-out-an-loa)[Porting away from Bandwidth](https://support.telnyx.com/en/articles/3947875-porting-away-from-bandwidth)

Did this answer your question?

😞😐😃
