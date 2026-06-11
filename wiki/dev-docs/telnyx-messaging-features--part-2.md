---
title: Telnyx Messaging Features
summary: Covers Telnyx messaging capabilities including MMS SMIL templates, Sticky
  Sender, URL Shortening, Zapier integration, toll-free verification, and the full
  WhatsApp Business messaging workflow from embedded signup through template management
  and message sending.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/smil-template
  content_hash: d29aa01a72d9457e2c15bca36d1a114fad0d8a8fd2d7b721484dbeb7d7ea9663
- url: https://developers.telnyx.com/docs/messaging/messages/sticky-sender/index
  content_hash: b60693e817349ec8df4be29ac868e8661434934e8c3047b7acc28151d7d666ae
- url: https://developers.telnyx.com/docs/messaging/messages/url-shortening/index
  content_hash: 4c488d1b1e1c401b24857bbee9b2dc380feeb3307e7bce07ecaa412fe56d304f
- url: https://developers.telnyx.com/docs/messaging/messages/zapier-integration
  content_hash: aad83743cb42ebbc89f6978b6f626af75781bd0d86f1dc76eec2c92463a1daa1
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/index
  content_hash: 4252b4aba3308d22e312c4bfc31ff2bf8b9dad3363bc6fa0d6dd8cc1765f4379
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/troubleshooting
  content_hash: 73f55d4531a2ff98fb6c9a7234dfb34e6b4429f9a1fdbc66b6c62d286cb29463
- url: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup
  content_hash: 2ed927e07af5e37713ddd6b340998cd8842b6303ef28e2428218537475463b8c
- url: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup/tech-provider
  content_hash: bb93e5d911b134f7064cd7997b82d901cca70eae5ee880c925434e16bb05f284
- url: https://developers.telnyx.com/docs/messaging/whatsapp/manage-templates
  content_hash: ed0efe6efb4a082f13f54662244ee901249886ad4eed11780a77d535efca8e89
- url: https://developers.telnyx.com/docs/messaging/whatsapp/quickstart/index
  content_hash: abd0f4264c0b578171e98a4800bc241b283f1640a411eb55d283297c41637ae9
- url: https://developers.telnyx.com/docs/messaging/whatsapp/send-messages/index
  content_hash: 6c916c387118b87a1258ad874d5461c0bf493edb141be63764cac4cb36a2cdcb
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
