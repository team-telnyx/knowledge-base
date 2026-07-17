---
title: Telnyx Number Verification Guide
summary: Telnyx provides several verification mechanisms for phone numbers used on
  its platform, including Verified Numbers for non-Telnyx numbers used as outbound
  CLI, Toll-Free Verification for outbound SMS from toll-free numbers, and Number
  Lookup for retrieving carrier and CNAM data. This page consolidates the verification
  workflows, API usage, pricing, error codes, and related number management resources.
sources:
- url: https://support.telnyx.com/en/articles/10729979-toll-free-verification-request-guide
- url: https://support.telnyx.com/en/articles/12386088-how-to-verify-phone-numbers-behind-an-ivr
- url: https://support.telnyx.com/en/articles/13854980-beta-how-to-verify-phone-numbers-using-dtmf-press-1-to-verify
- url: https://support.telnyx.com/en/articles/4366901-your-number-lookup-guide
- url: https://support.telnyx.com/en/articles/5941652-google-verified-calls-faq
- url: https://support.telnyx.com/en/articles/6790265-verified-numbers-faq
- url: https://support.telnyx.com/en/articles/6988813-verified-numbers
- url: https://support.telnyx.com/en/collections/3968222-telnyx-number-management-guide
updated_at: 2026-07-17T09:01:33Z
---

# Telnyx Number Verification Guide

*Part 3 of 3 — see also: [Part 1](telnyx-number-verification-guide--part-1.md), [Part 2](telnyx-number-verification-guide--part-2.md)*

Telnyx provides several verification mechanisms for phone numbers used on its platform, including Verified Numbers for non-Telnyx numbers used as outbound CLI, Toll-Free Verification for outbound SMS from toll-free numbers, and Number Lookup for retrieving carrier and CNAM data. This page consolidates the verification workflows, API usage, pricing, error codes, and related number management resources.

## Number Lookup

The Telnyx Number Lookup API helps you retrieve details behind every phone number, making each call more productive, reducing undelivered messages, and protecting from spam and fraud.

### Prerequisites

- A Telnyx account
- A positive account balance (Number Lookup requires funds; it is not available if balance is negative)
- An API Key (for API access)

### Using Number Lookup in the Portal

1. Sign in to the [Telnyx portal](https://portal.telnyx.com/).
2. Navigate to <https://portal.telnyx.com/#/lookup>.
3. Enter the phone number and select a Lookup Type:
   - **None** — Basic info (LRN only).
   - **Carrier** — Adds carrier details.
   - **Caller Name** — Adds CNAM.
   - **Both** — Returns all available data.
4. Click **Lookup Number**.

### Lookup Types and Pricing

| Service | Cost |
| --- | --- |
| Local Routing Number (LRN) | $0.0015 per query |
| MCC/MNC (Carrier Codes) | $0.0025 per query (mobile only) |
| CNAM (Caller ID Name) | $0.003 per query |
| Inbound CNAM | $0.40 per number/month |
| Outbound CNAM Listing | Free |

Examples:

- Landline with Carrier + Caller Name: $0.0015 + $0.003 = $0.0045
- Mobile with Carrier + Caller Name: $0.0015 + $0.0025 + $0.003 = $0.007

### Reviewing Usage

- Charges appear at the start of each month on your invoice.
- Usage Reports are available at **Reporting → Usage Reports** for a selected date range. Reports are not real-time; today's lookups appear tomorrow.

### Important Notes

- To view full LRN data, go to **Account Settings → Profile** and enable **Permitted NPAC User** (allow ~15 minutes to apply).
- Access is restricted to Organization Owners only (no sub-accounts).
- US Toll-Free: Resporg ID is not returned.

### Troubleshooting

| Error | Cause | Solution |
| --- | --- | --- |
| Number Lookup unavailable | Zero/negative balance | Add funds |
| LRN data incomplete | NPAC User not enabled | Enable in Account Settings |
| 401 Unauthorized | Invalid API key | Verify key and header format |
| Sub-user access denied | Owner-only feature | Use org owner credentials |

## Google Verified Calls

Google Verified Calls is no longer offered by Telnyx. This product was sunset by Google.

Google Verified Calls was a way for businesses to display their business name, logo, and reason for calling on an end-user's Android device. A verification symbol showed the call had been verified by Google, increasing end-user trust. By showing brand logo and reason for calling, Google Verified Calls built user trust so more calls got answered. Verified Calls was available to consumers through Google's Phone app on Android.

Verified Calls is no longer available in the United States, India, Mexico, Brazil, and Spain, and is no longer available through Telnyx.

## Related Number Management Resources

The Telnyx Number Management Guide covers number searching, ordering, editing, porting, and requirements. Related collections include:

- [Phone Numbers](phone-numbers.md) — Ordering, DID types, global number types, and country-specific DID requirements.
- [International DID Requirements](international-did-requirements.md) — Country-by-country requirements for acquiring international numbers.
- [Porting Articles and Guides](porting-articles-and-guides.md) — Port request statuses, FastPort, porting to/from Telnyx, and international porting.
- [Bulk Edit Numbers](bulk-edit-numbers.md) — Bulk editing of messaging profiles, deletion, emergency services, tags, and voice settings.
- [Number Features](number-features.md) — Voicemail, call forwarding, caller ID, and inbound call screening.
