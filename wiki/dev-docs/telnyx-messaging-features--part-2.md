---
title: Telnyx Messaging Features
summary: Covers Telnyx messaging capabilities including MMS SMIL templates, Sticky
  Sender, URL Shortening, Zapier integration, toll-free verification, and the full
  WhatsApp Business messaging workflow from embedded signup through template management
  and message sending.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/smil-template
- url: https://developers.telnyx.com/docs/messaging/messages/sticky-sender/index
- url: https://developers.telnyx.com/docs/messaging/messages/url-shortening/index
- url: https://developers.telnyx.com/docs/messaging/messages/zapier-integration
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/index
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/troubleshooting
- url: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup
- url: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup/tech-provider
- url: https://developers.telnyx.com/docs/messaging/whatsapp/manage-templates
- url: https://developers.telnyx.com/docs/messaging/whatsapp/quickstart/index
- url: https://developers.telnyx.com/docs/messaging/whatsapp/send-messages/index
updated_at: 2026-06-11T10:38:44Z
---

# Telnyx Messaging Features

*Part 2 of 5 — see also: [Part 1](telnyx-messaging-features--part-1.md), [Part 3](telnyx-messaging-features--part-3.md), [Part 4](telnyx-messaging-features--part-4.md), [Part 5](telnyx-messaging-features--part-5.md)*

Covers Telnyx messaging capabilities including MMS SMIL templates, Sticky Sender, URL Shortening, Zapier integration, toll-free verification, and the full WhatsApp Business messaging workflow from embedded signup through template management and message sending.

## Toll-Free Verification

U.S. wireless carriers require toll-free numbers (800, 888, 877, 866, 855, 844, 833) used for SMS/MMS to complete verification. Starting **February 17, 2026**, three Business Registration Number (BRN) fields are required for all new submissions: `businessRegistrationNumber`, `businessRegistrationType`, and `businessRegistrationCountry`.

### Required BRN Fields

**businessRegistrationNumber** — The official government-issued business registration identifier (e.g., US EIN `12-3456789`, Canada Business Number `123456789RC0001`, UK Companies House `12345678`, Australia ABN `51824753556`, Germany VAT `DE123456789`). Max 500 characters.

**businessRegistrationType** — The classification of the registration (e.g., `EIN`, `CRA`, `Companies House`, `ABN`, `VAT`, `SSN` for US sole proprietors). Max 500 characters.

**businessRegistrationCountry** — ISO 3166-1 alpha-2 country code, exactly 2 characters, automatically uppercased. Examples: `US`, `CA`, `GB`, `AU`, `DE`.

### Optional Fields

| Field | Description |
|---|---|
| `doingBusinessAs` | DBA/trade name if different from legal name (max 500 chars) |
| `entityType` | `SOLE_PROPRIETOR`, `PRIVATE_PROFIT`, `PUBLIC_PROFIT`, `NON_PROFIT`, or `GOVERNMENT` |
| `optInConfirmationResponse` | Message confirming opt-in (max 500 chars) |
| `helpMessageResponse` | Automated HELP reply (max 500 chars) |
| `privacyPolicyURL` | Privacy policy URL |
| `termsAndConditionURL` | Terms and conditions URL |
| `ageGatedContent` | Boolean, indicates 18+/21+ content |
| `optInKeywords` | Opt-in keywords like `START, YES, SUBSCRIBE` |

### API Usage

Create a verification request:

```bash
curl --request POST \
  --url https://api.telnyx.com/v2/messaging_tollfree/verification/requests \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "businessName": "Acme Corp",
    "businessAddr1": "600 Congress Avenue",
    "businessCity": "Austin",
    "businessState": "Texas",
    "businessZip": "78701",
    "businessContactFirstName": "John",
    "businessContactLastName": "Doe",
    "businessContactEmail": "email@example.com",
    "businessContactPhone": "+18005550100",
    "messageVolume": "100,000",
    "phoneNumbers": [{"phoneNumber": "+18773554398"}],
    "useCase": "2FA",
    "useCaseSummary": "...",
    "productionMessageContent": "Your OTP is XXXX",
    "optInWorkflow": "...",
    "businessRegistrationNumber": "12-3456789",
    "businessRegistrationType": "EIN",
    "businessRegistrationCountry": "US",
    "entityType": "PRIVATE_PROFIT"
  }'
```

Retrieve a verification: `GET /public/api/v2/requests/{id}`

Update BRN fields: `PATCH /public/api/v2/requests/{id}`

### Migration Timeline

| Period | Status |
|---|---|
| Now – Dec 2025 | BRN fields optional, requests without them still work |
| February 17, 2026 | All 3 BRN fields required; submissions missing them return HTTP 400 |

Approved verifications before February 2026 remain valid. No need to resubmit existing verifications.

## Toll-Free Verification Troubleshooting

Verification typically takes 1–2 weeks. Understanding common rejection reasons speeds up approval.

### Verification Lifecycle

| Stage | Timeline | What Happens |
|---|---|---|
| Submission | Instant | API validates fields, returns 201 or error |
| Under review | 1–2 weeks | Carriers review business identity and use case |
| Decision | — | Approved (full throughput) or rejected (with reason) |
| Resubmission | Instant | Fix issues and resubmit — no limit on attempts |

### Common Rejection Reasons

**Business information issues**:
- **Name mismatch**: The `businessName` must exactly match public records including suffixes (Inc., LLC, etc.)
- **BRN cannot be verified**: Ensure the registration number matches the business name and the type/country are correct
- **Website unreachable or doesn't match**: Website must be live, show the business name, and relate to the use case; no parking pages
- **Contact information invalid**: Use publicly associated phone/email; business email domains preferred over personal
- **Entity type mismatch**: Choose the correct type matching your actual registration

**Messaging use case issues**:
- **Sample messages don't match declared use case**: Every sample must directly relate to the declared use case with realistic content
- **Missing opt-out language**: Every sample must include instructions like "Reply STOP to unsubscribe"
- **Message volume inconsistent**: Be honest about volumes; carriers cross-reference similar businesses
- **Opt-in mechanism not described**: Fully document how recipients consent (where they sign up, consent language, single/double opt-in, record-keeping)
- **Prohibited or restricted content**: Cannabis, adult content, gambling, high-risk financial services, third-party lead generation

### Resubmission Best Practices

| Do | Don't |
|---|---|
| Fix only the cited rejection reason | Change everything at once |
| Use exact legal business name | Use informal names or abbreviations |
| Provide realistic sample messages | Use generic placeholder text |
| Include opt-out in every sample | Assume opt-out is implied |
| Wait for the full review cycle | Submit multiple times in rapid succession |

After fixing issues, PATCH the request. The update automatically triggers re-review—no separate submit action needed.

### Throughput After Verification

| Verification Status | Throughput | Notes |
|---|---|---|
| Unverified | ~0.25 MPS | Heavy carrier filtering |
| Pending review | ~1 MPS | Some filtering may apply |
| Verified | Up to 20 MPS | Full throughput, minimal filtering |

### Common Delivery Errors

- **40002 (spam block)**: Review content for trigger words, avoid third-party URL shorteners, use [Telnyx URL Shortening](telnyx-url-shortening.md) instead
- **40005 (unreachable)**: Validate recipient numbers, remove landlines
- **40011 (rate limit)**: Implement client-side rate limiting, spread traffic across numbers
- **40014 (expired in queue)**: Reduce sending rate, check for carrier outages

### Toll-Free vs. 10DLC

| Factor | Toll-Free | 10DLC |
|---|---|---|
| Setup time | 1–2 weeks | Days |
| Throughput | Up to 20 MPS | Up to 240 MPS (enhanced) |
| Cost | Per-message only | Per-message + campaign fees |
| Number appearance | 800/888/877 etc. | Local area code |
| MMS | Supported | Supported |

Many businesses use both: toll-free for customer service and 10DLC for local presence marketing.
