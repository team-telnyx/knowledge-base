---
title: Toll-Free Verification
summary: Telnyx toll-free verification requires Business Registration Number (BRN)
  fields for all new submissions starting February 17, 2026. This page covers the
  required and optional fields, API usage for creating, retrieving, and updating verification
  requests, common rejection reasons, the resubmission process, delivery troubleshooting,
  and guidance on choosing between toll-free and 10DLC messaging.
sources:
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/index
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/troubleshooting
updated_at: 2026-08-05T13:58:33Z
---

# Toll-Free Verification

*Part 6 of 6 — see also: [Part 1](toll-free-verification--part-1.md), [Part 2](toll-free-verification--part-2.md), [Part 3](toll-free-verification--part-3.md), [Part 4](toll-free-verification--part-4.md), [Part 5](toll-free-verification--part-5.md)*

Telnyx toll-free verification requires Business Registration Number (BRN) fields for all new submissions starting February 17, 2026. This page covers the required and optional fields, API usage for creating, retrieving, and updating verification requests, common rejection reasons, the resubmission process, delivery troubleshooting, and guidance on choosing between toll-free and 10DLC messaging.

## Diagnostic Checklist

Use this checklist when troubleshooting verification issues.

### Before Submitting

- Business name matches exact legal name (including Inc./LLC/etc.)
- EIN/BRN is correct and matches the business name
- Website is live, accessible, and shows the business name
- Contact phone and email are valid and publicly associated with the business
- Entity type matches business registration
- Use case summary clearly describes messaging purpose
- Sample messages are realistic (not placeholder text)
- Every sample includes opt-out language ("Reply STOP to unsubscribe")
- Message flow describes how users consent to receive messages
- Volume estimate is reasonable for the use case

### After Rejection

- Read the rejection reason completely
- Cross-reference with the rejection reasons above
- Fix only the specific issue cited
- Double-check all information against official business records
- Resubmit via PATCH (don't create a new request)
- Set up webhooks to track the new review

### After Verification (Delivery Issues)

- Verify toll-free number is on an active messaging profile
- Check sending rate isn't exceeding throughput tier
- Review message content for spam trigger words
- Confirm opt-out keywords are being processed
- Check MDRs for carrier-specific delivery rates
- Monitor error codes for patterns

## Timeline Expectations

| Stage | Typical duration |
| --- | --- |
| Initial submission to review start | 1–3 business days |
| Carrier review | 5–10 business days |
| Total (first submission) | 1–2 weeks |
| Resubmission review | 5–10 business days |
| Multiple resubmissions | Each adds ~1 week |

**Expedited review** is not available for toll-free verification. The review timeline is set by carriers, not Telnyx. Ensure your first submission is complete and accurate to avoid resubmission delays.

## Toll-Free vs. 10DLC: When to Use Which

| Factor | Toll-Free | 10DLC |
| --- | --- | --- |
| **Setup time** | 1–2 weeks | Days (brand + campaign registration) |
| **Throughput** | Up to 20 MPS | Varies by vetting score (up to 240 MPS with enhanced) |
| **Cost** | Per-message only | Per-message + campaign fees ($10/mo) |
| **Number appearance** | 800/888/877/etc. | Local area code |
| **Registration** | Toll-free verification | TCR brand + campaign |
| **MMS** | ✅ Supported | ✅ Supported |
| **Best for** | Customer service, national reach | Local presence, high volume A2P |

Many businesses use **both**: toll-free for customer service and support lines, 10DLC for marketing and transactional messages with local presence.

## Frequently Asked Questions

**When do BRN fields become mandatory?**

February 17, 2026. All new verification requests must include `businessRegistrationNumber`, `businessRegistrationType`, and `businessRegistrationCountry`.

**Do I need to resubmit existing verifications?**

No. Approved verifications before February 2026 remain valid.

**Where do I find my business registration number?**

- **US**: IRS EIN confirmation letter or [IRS.gov](https://www.irs.gov/)
- **Canada**: CRA Business Number registration documents
- **UK**: [Companies House](https://www.gov.uk/get-information-about-a-company) certificate
- **Australia**: [ABN Lookup](https://abr.business.gov.au/)
- **EU**: VAT registration certificate

**What if I'm a sole proprietor without an EIN?**

U.S. sole proprietors can use their Social Security Number as `businessRegistrationNumber` with type `SSN`. Other countries may have similar individual tax identifiers.

**Can I update BRN fields after submission?**

Yes. Use `PATCH /public/api/v2/requests/{id}` to update BRN fields.

**Why are country codes converted to uppercase?**

For consistency. Sending `"us"` automatically becomes `"US"` in responses and storage.

**Which entity type should I choose?**

Choose the type matching your official business registration:

- `SOLE_PROPRIETOR` — Individual or sole proprietorship
- `PRIVATE_PROFIT` — Private corporation (most common)
- `PUBLIC_PROFIT` — Publicly traded company
- `NON_PROFIT` — 501(c) or charitable organization
- `GOVERNMENT` — Government entity

**How long does toll-free verification take?**

Verification typically takes **1–2 weeks**, depending on the carrier review queue and the completeness of your submission. Including accurate BRN fields can speed up the process.

**What happens if my verification is rejected?**

You'll receive a webhook notification with the rejection reason. Common causes:

- Incomplete or inaccurate business information
- Message samples don't match your declared use case
- Missing opt-out language in sample messages
- Business couldn't be verified with the provided registration number

Fix the issues and resubmit — there's no limit on resubmissions.

**Can I send messages before verification is complete?**

Unverified toll-free numbers have **limited throughput** and may experience carrier filtering. Complete verification to unlock full sending capabilities (up to 20 MPS).

**What's the difference between toll-free verification and 10DLC registration?**

| Aspect | Toll-Free Verification | 10DLC Registration |
| --- | --- | --- |
| **Number type** | Toll-free (800, 888, etc.) | Local 10-digit numbers |
| **Timeline** | 1–2 weeks | Days (plus 1–7 days for vetting) |
| **Registry** | Carrier-managed | The Campaign Registry (TCR) |
| **Throughput** | Up to 20 MPS | Varies by vetting score |
| **Cost** | Per-message | Per-message + campaign fees |

## Support

Need help with toll-free verification?

- **Support Portal**: [support.telnyx.com](https://support.telnyx.com)
- **Email**: [support@telnyx.com](mailto:support@telnyx.com)
- **Developer Community**: Join discussions and get help from other developers

## Related Resources

- [Toll-Free Verification API](toll-free-verification-api.md)
- [Messaging API](messaging-api.md)
- [10DLC Registration](10dlc-registration.md)
- [Advanced Opt-In/Out](advanced-opt-in-out.md)
