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

*Part 4 of 6 — see also: [Part 1](toll-free-verification--part-1.md), [Part 2](toll-free-verification--part-2.md), [Part 3](toll-free-verification--part-3.md), [Part 5](toll-free-verification--part-5.md), [Part 6](toll-free-verification--part-6.md)*

Telnyx toll-free verification requires Business Registration Number (BRN) fields for all new submissions starting February 17, 2026. This page covers the required and optional fields, API usage for creating, retrieving, and updating verification requests, common rejection reasons, the resubmission process, delivery troubleshooting, and guidance on choosing between toll-free and 10DLC messaging.

## Verification Rejection Reasons

Rejections come from carrier review. Each has specific causes and fixes.

### Business Information Issues

**Business name mismatch**

- **Rejection reason**: Business name does not match public records.
- **Root cause**: The `businessName` you submitted doesn't match what's on file with the Secretary of State, IRS, or similar authority for your registration number.
- **Fix**:
  1. Look up your exact legal name on your state's Secretary of State website
  2. Cross-reference with your EIN confirmation letter from the IRS
  3. Include suffixes exactly: "Inc.", "LLC", "Corp." — these matter
  4. Resubmit with the corrected name

```
curl -X PATCH https://api.telnyx.com/v2/tollFreeVerification/requests/{requestId} \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "businessName": "Acme Corporation Inc."
  }'
```

**Common mistakes**:

- Using a DBA/trade name instead of the legal entity name
- Missing "LLC", "Inc.", etc.
- Using an old company name after a legal name change

**Business registration number (BRN) cannot be verified**

- **Rejection reason**: Unable to verify business registration information.
- **Root cause**: The EIN, ABN, VAT number, or other registration number doesn't match the business name or doesn't exist in public records.
- **Fix**:
  1. Verify your EIN at [IRS.gov](https://www.irs.gov/) or on your SS-4 confirmation letter
  2. Ensure the `businessRegistrationType` matches the number format (e.g., "EIN" for US tax IDs)
  3. Confirm `businessRegistrationCountry` is correct (ISO alpha-2)
  4. For sole proprietors using SSN, ensure the name matches exactly

```
curl -X PATCH https://api.telnyx.com/v2/tollFreeVerification/requests/{requestId} \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "businessRegistrationNumber": "12-3456789",
    "businessRegistrationType": "EIN",
    "businessRegistrationCountry": "US"
  }'
```

**Website unreachable or doesn't match**

- **Rejection reason**: Corporate website could not be verified or does not match the business.
- **Root cause**: Carriers check that the website is live, matches the business name, and has content relevant to the declared use case.
- **Fix**:
  1. Ensure the URL is accessible (no authentication required, no redirects to a different domain)
  2. The website must show the company name prominently
  3. Website content should relate to the messaging use case
  4. HTTPS is strongly preferred
  5. Under construction / parking pages will cause rejection

**Before resubmitting, verify**:

```
# Check website is accessible
curl -sI https://yourbusiness.com | head -5

# Check it resolves to expected domain
curl -sL -o /dev/null -w '%{url_effective}' https://yourbusiness.com
```

**Contact information invalid**

- **Rejection reason**: Contact information could not be verified.
- **Root cause**: The phone number or email provided doesn't match public records for the business, or isn't reachable.
- **Fix**:
  1. Use a phone number that's publicly associated with the business (Google listing, website, etc.)
  2. Use a business email domain (not gmail.com, yahoo.com for corporations)
  3. Ensure the contact person is authorized to represent the business

**Entity type mismatch**

- **Rejection reason**: Entity type does not match business records.
- **Root cause**: You selected `PRIVATE_PROFIT` but the business is registered as a nonprofit, or vice versa.
- **Fix**: Choose the correct entity type based on your actual business registration:

| Entity Type | Use for |
| --- | --- |
| `SOLE_PROPRIETOR` | Individual / sole proprietorship |
| `PRIVATE_PROFIT` | Private corporation (most common) |
| `PUBLIC_PROFIT` | Publicly traded company |
| `NON_PROFIT` | 501(c)(3) or charitable organization |
| `GOVERNMENT` | Government entity at any level |

### Messaging Use Case Issues

**Sample messages don't match declared use case**

- **Rejection reason**: Message samples are inconsistent with the stated use case.
- **Root cause**: Your `useCaseSummary` says one thing (e.g., "appointment reminders") but your sample messages show something different (e.g., marketing promotions).
- **Fix**:
  1. Ensure every sample message directly relates to your declared use case
  2. Include realistic content — not placeholder text
  3. Show the full message including opt-out language
  4. If you have multiple use cases, describe all of them in `useCaseSummary`

**Good sample**:

```
Hi Sarah, this is Dr. Smith's office. Your appointment is confirmed
for March 15 at 2:00 PM. Reply STOP to opt out of reminders.
```

**Bad sample**:

```
Test message for verification purposes.
```

**Missing or inadequate opt-out language**

- **Rejection reason**: Sample messages must include opt-out instructions.
- **Root cause**: At least one sample message is missing STOP/opt-out language, or the opt-out mechanism isn't clear.
- **Fix**:
  1. Include "Reply STOP to unsubscribe" (or similar) in every sample
  2. The opt-out instruction should be natural, not buried
  3. STOP, CANCEL, UNSUBSCRIBE, QUIT, END should all work

**Required format examples**:

- "Reply STOP to opt out."
- "Text STOP to unsubscribe."
- "Reply STOP to end messages. Msg & data rates may apply."

**Message volume inconsistent with use case**

- **Rejection reason**: Declared message volume does not align with the use case.
- **Root cause**: Claiming a very high volume for a use case that typically doesn't generate it, or vice versa.
- **Fix**:
  1. Be honest about expected volumes — carriers cross-reference similar businesses
  2. If volume is high, explain why (large customer base, time-sensitive notifications)
  3. Start conservative and increase as your messaging matures

**Opt-in mechanism not described**

- **Rejection reason**: Opt-in process is unclear or not documented.
- **Root cause**: You didn't adequately describe how recipients consent to receive messages.
- **Fix**: Describe the full opt-in flow in your `messageFlow` field:

- Where users sign up (website form, checkout flow, in-app)
- What consent language they see
- Whether it's single or double opt-in
- How consent records are maintained

**Good example**:

```
Customers opt in during checkout at acme.com/checkout by checking
"I agree to receive order updates and shipping notifications via SMS."
Consent is recorded with timestamp and IP address. Customers can
opt out at any time by replying STOP.
```

**Bad example**:

```
Users sign up on our website.
```

**Prohibited or restricted content detected**

- **Rejection reason**: Message content contains prohibited or restricted material.
- **Root cause**: Sample messages or use case involves content types that carriers restrict:
  - Cannabis/CBD
  - Adult content
  - Gambling (without proper licensing documentation)
  - High-risk financial services (payday loans, crypto trading signals)
  - Third-party lead generation
- **Fix**:
  1. If your content is genuinely prohibited, toll-free may not be the right channel
  2. For regulated industries (gambling, financial services), include licensing documentation
  3. Remove any references to restricted content from samples
  4. Contact [Telnyx support](https://support.telnyx.com) for guidance on restricted use cases
