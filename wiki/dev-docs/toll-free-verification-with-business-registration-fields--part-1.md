---
title: Toll-Free Verification with Business Registration Fields
summary: Telnyx toll-free verification now includes mandatory Business Registration
  Number (BRN) fields starting February 17, 2026, to improve carrier compliance, speed
  reviews, and reduce fraud. This guide explains required/optional fields, API usage,
  validation and error handling, migration steps, and includes troubleshooting guidance
  for rejections and post-verification delivery issues.
sources:
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/index
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/troubleshooting
updated_at: 2026-05-20T09:12:49Z
---

# Toll-Free Verification with Business Registration Fields

*Part 1 of 2 — see also: [Part 2](toll-free-verification-with-business-registration-fields--part-2.md)*

Telnyx toll-free verification now includes mandatory Business Registration Number (BRN) fields starting February 17, 2026, to improve carrier compliance, speed reviews, and reduce fraud. This guide explains required/optional fields, API usage, validation and error handling, migration steps, and includes troubleshooting guidance for rejections and post-verification delivery issues.

## Why BRN fields matter
U.S. carriers require verification for toll-free numbers (800, 888, 877, 866, 855, 844, 833) used for SMS/MMS. Adding BRN fields strengthens business identity checks, which can reduce processing time, improve approval rates, ensure policy compliance, and prevent fraudulent messaging.

## Required BRN fields (from February 17, 2026)
Provide all three in every new verification request. Requests missing any will be rejected.
- businessRegistrationNumber: Government-issued registration identifier (e.g., US EIN 12-3456789 or 123456789; CA Business Number 123456789RC0001; GB Companies House 12345678; AU ABN 51824753556; DE VAT DE123456789). Max length 500.
- businessRegistrationType: Registration system/type (e.g., EIN, CRA, Companies House, ABN, VAT, SSN for US sole proprietors without EIN). Max length 500.
- businessRegistrationCountry: Two-letter ISO 3166-1 alpha-2 code (e.g., US, CA, GB, AU, DE, FR, JP). Exactly 2 alphabetic chars; auto-upcased; invalid values return HTTP 400.

Where to find numbers (examples):
- US: IRS EIN documents or IRS.gov
- CA: CRA Business Number documents
- UK: Companies House records
- AU: ABN Lookup
- EU: National VAT registration certificate

## Optional verification fields
These are recommended to speed reviews.
- doingBusinessAs: DBA/trade name (if different from legal name). Max 500.
- entityType: SOLE_PROPRIETOR | PRIVATE_PROFIT | PUBLIC_PROFIT | NON_PROFIT | GOVERNMENT.
- optInConfirmationResponse: Text confirming subscriber opt-in. Max 500.
- helpMessageResponse: Text returned on HELP. Max 500.
- privacyPolicyURL: Link to privacy policy. Max 500.
- termsAndConditionURL: Link to terms. Max 500.
- ageGatedContent: Boolean; true for age-restricted content (alcohol, tobacco, cannabis, etc.). Default false.
- optInKeywords: Comma-separated keywords users can text to opt in (e.g., START, YES, SUBSCRIBE, JOIN). Max 500.

## API endpoints and examples
Create a verification (include BRN fields):

curl --request POST \
  --url https://api.telnyx.com/v2/messaging_tollfree/verification/requests \
  --header 'Authorization: Bearer <API_KEY>' \
  --header 'Content-Type: application/json' \
  --data '{
    "businessName": "Acme Corporation",
    "corporateWebsite": "https://www.acme.com",
    "businessAddr1": "123 Main Street",
    "businessCity": "Chicago",
    "businessState": "Illinois",
    "businessZip": "60601",
    "businessContactFirstName": "John",
    "businessContactLastName": "Doe",
    "businessContactEmail": "compliance@acme.com",
    "businessContactPhone": "+18005551234",
    "messageVolume": "100,000",
    "phoneNumbers": [{"phoneNumber": "+18773554398"}],
    "useCase": "Account Notifications",
    "useCaseSummary": "Security alerts and account updates",
    "productionMessageContent": "Your code is 123456",
    "optInWorkflow": "Users opt-in during registration",
    "optInWorkflowImageURLs": [{"url": "https://www.acme.com/opt-in.png"}],
    "isvReseller": "Yes",
    "businessRegistrationNumber": "12-3456789",
    "businessRegistrationType": "EIN",
    "businessRegistrationCountry": "US",
    "doingBusinessAs": "Acme Services",
    "entityType": "PRIVATE_PROFIT"
  }'

Retrieve a verification:

curl -X GET \
  https://api.telnyx.com/public/api/v2/requests/{id} \
  -H 'Authorization: Bearer <API_KEY>'

Update BRN fields or other details:

curl -X PATCH \
  https://api.telnyx.com/public/api/v2/requests/{id} \
  -H 'Authorization: Bearer <API_KEY>' \
  -H 'Content-Type: application/json' \
  -d '{
    "businessRegistrationNumber": "98-7654321",
    "businessRegistrationCountry": "US"
  }'

Responses include identifiers (id, verificationRequestId), status (e.g., Pending/Approved), the BRN fields, entityType, phoneNumbers, and timestamps (createdAt/updatedAt).

## Code examples
Python:

import requests

payload = {
  "businessName": "Acme Corporation",
  "corporateWebsite": "https://www.acme.com",
  "businessAddr1": "123 Main Street",
  "businessCity": "Chicago",
  "businessState": "Illinois",
  "businessZip": "60601",
  "businessContactFirstName": "John",
  "businessContactLastName": "Doe",
  "businessContactEmail": "compliance@acme.com",
  "businessContactPhone": "+18005551234",
  "messageVolume": "100,000",
  "phoneNumbers": [{"phoneNumber": "+18773554398"}],
  "useCase": "Account Notifications",
  "useCaseSummary": "Security alerts and account updates",
  "productionMessageContent": "Your Acme security code is: 123456",
  "optInWorkflow": "Users opt-in during registration",
  "optInWorkflowImageURLs": [{"url": "https://www.acme.com/opt-in.png"}],
  "isvReseller": "Yes",
  "businessRegistrationNumber": "12-3456789",
  "businessRegistrationType": "EIN",
  "businessRegistrationCountry": "US",
  "entityType": "PRIVATE_PROFIT"
}

r = requests.post(
  "https://api.telnyx.com/public/api/v2/requests",
  json=payload,
  headers={"Authorization": "Bearer YOUR_API_KEY"}
)
print(r.status_code, r.text)

JavaScript/TypeScript:

interface TollFreeVerificationRequest {
  businessName: string;
  corporateWebsite: string;
  businessAddr1: string;
  businessCity: string;
  businessState: string;
  businessZip: string;
  businessContactFirstName: string;
  businessContactLastName: string;
  businessContactEmail: string;
  businessContactPhone: string;
  messageVolume: string;
  phoneNumbers: Array<{ phoneNumber: string }>;
  useCase: string;
  useCaseSummary: string;
  productionMessageContent: string;
  optInWorkflow: string;
  optInWorkflowImageURLs: Array<{ url: string }>;
  additionalInformation?: string;
  isvReseller: string;
  businessRegistrationNumber: string;
  businessRegistrationType: string;
  businessRegistrationCountry: string;
  entityType?: 'SOLE_PROPRIETOR' | 'PRIVATE_PROFIT' | 'PUBLIC_PROFIT' | 'NON_PROFIT' | 'GOVERNMENT';
}

async function createVerification(req: TollFreeVerificationRequest, apiKey: string) {
  const res = await fetch('https://api.telnyx.com/public/api/v2/requests', {
    method: 'POST',
    headers: { 'Authorization': `Bearer ${apiKey}`, 'Content-Type': 'application/json' },
    body: JSON.stringify(req)
  });
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

## Validation and error handling
- Missing BRN fields after Feb 17, 2026 ⇒ HTTP 400 with field-specific error messages.
- Invalid country code ⇒ HTTP 400: country must be a 2-character ISO alpha-2 code; letters only; upcased automatically.
- Invalid entityType ⇒ HTTP 400 listing allowed values.
- Other status codes: 200 (GET/PATCH), 201 (POST), 204 (DELETE), 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), 422 (Unprocessable Entity).

## Migration plan
- Now through Dec 2025: BRN fields supported but optional.
- From February 17, 2026: All three BRN fields are required for new submissions.
Preparation checklist:
- Gather your registration number, registration type, and issuing country code.
- Add the three BRN fields to your integration and test end-to-end (submission, retrieval, validation errors, country code upcasing).
- Update error handling to surface 400 validation errors clearly.
- No resubmission needed for already-approved verifications.

## Verification lifecycle
- Submission: API validates and returns Created (201) or an error immediately.
- Under review: Carriers review business identity and use case (typically 1–2 weeks).
- Decision: Approved (full toll-free throughput) or Rejected (with reason).
- Resubmission: Fix issues and PATCH; there is no limit on attempts.
