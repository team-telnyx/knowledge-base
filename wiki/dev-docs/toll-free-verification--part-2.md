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

*Part 2 of 6 — see also: [Part 1](toll-free-verification--part-1.md), [Part 3](toll-free-verification--part-3.md), [Part 4](toll-free-verification--part-4.md), [Part 5](toll-free-verification--part-5.md), [Part 6](toll-free-verification--part-6.md)*

Telnyx toll-free verification requires Business Registration Number (BRN) fields for all new submissions starting February 17, 2026. This page covers the required and optional fields, API usage for creating, retrieving, and updating verification requests, common rejection reasons, the resubmission process, delivery troubleshooting, and guidance on choosing between toll-free and 10DLC messaging.

## API Usage

### Create Verification Request with BRN Fields

**Endpoint**: `POST /public/api/v2/requests`

```
curl --request POST \
  --url https://api.telnyx.com/v2/messaging_tollfree/verification/requests \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "businessName": "Telnyx LLC",
  "corporateWebsite": "http://example.com",
  "businessAddr1": "600 Congress Avenue",
  "businessAddr2": "14th Floor",
  "businessCity": "Austin",
  "businessState": "Texas",
  "businessZip": "78701",
  "businessContactFirstName": "John",
  "businessContactLastName": "Doe",
  "businessContactEmail": "email@example.com",
  "businessContactPhone": "+18005550100",
  "messageVolume": "100,000",
  "phoneNumbers": [
    {
      "phoneNumber": "+18773554398"
    },
    {
      "phoneNumber": "+18773554399"
    }
  ],
  "useCase": "2FA",
  "useCaseSummary": "This is a use case where Telnyx sends out 2FA codes to portal users to verify their identity in order to sign into the portal",
  "productionMessageContent": "Your Telnyx OTP is XXXX",
  "optInWorkflow": "User signs into the Telnyx portal, enters a number and is prompted to select whether they want to use 2FA verification for security purposes. If they have opted in a confirmation message is sent out to the handset",
  "optInWorkflowImageURLs": [
    {
      "url": "https://telnyx.com/sign-up"
    },
    {
      "url": "https://telnyx.com/company/data-privacy"
    }
  ],
  "additionalInformation": "<string>",
  "isvReseller": "Yes",
  "webhookUrl": "http://example-webhook.com",
  "businessRegistrationNumber": "12-3456789",
  "businessRegistrationType": "EIN",
  "businessRegistrationCountry": "US",
  "doingBusinessAs": "Acme Services",
  "entityType": "SOLE_PROPRIETOR",
  "optInConfirmationResponse": "You have successfully opted in to receive messages from Acme Corp",
  "helpMessageResponse": "Reply HELP for assistance or STOP to unsubscribe. Contact: support@example.com",
  "privacyPolicyURL": "https://example.com/privacy",
  "termsAndConditionURL": "https://example.com/terms",
  "ageGatedContent": false,
  "optInKeywords": "START, YES, SUBSCRIBE"
}'
```

**Response** (HTTP 201):

```
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "verificationRequestId": "TFV-ABC123",
  "verificationStatus": "Pending",
  "businessName": "Acme Corporation",
  "businessRegistrationNumber": "12-3456789",
  "businessRegistrationType": "EIN",
  "businessRegistrationCountry": "US",
  "entityType": "PRIVATE_PROFIT",
  "createdAt": "2025-10-13T12:00:00Z"
}
```

### Retrieve Verification with BRN Fields

**Endpoint**: `GET /public/api/v2/requests/{id}`

```
curl -X GET https://api.telnyx.com/public/api/v2/requests/550e8400-e29b-41d4-a716-446655440000 \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Response** (HTTP 200):

```
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "verificationRequestId": "TFV-ABC123",
  "verificationStatus": "Approved",
  "businessName": "Acme Corporation",
  "businessRegistrationNumber": "12-3456789",
  "businessRegistrationType": "EIN",
  "businessRegistrationCountry": "US",
  "entityType": "PRIVATE_PROFIT",
  "phoneNumbers": [{"phoneNumber": "+18773554398"}],
  "createdAt": "2025-10-13T12:00:00Z",
  "updatedAt": "2025-10-15T09:30:00Z"
}
```

### Update BRN Fields

**Endpoint**: `PATCH /public/api/v2/requests/{id}`

```
curl -X PATCH https://api.telnyx.com/public/api/v2/requests/550e8400-e29b-41d4-a716-446655440000 \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "businessRegistrationNumber": "98-7654321",
    "businessRegistrationCountry": "US"
  }'
```

## Code Examples

### Python

```
import requests

# Create verification with BRN fields
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
    "additionalInformation": "Messages to verified numbers only",
    "isvReseller": "Yes",

    # BRN Fields (required Feb 2026)
    "businessRegistrationNumber": "12-3456789",
    "businessRegistrationType": "EIN",
    "businessRegistrationCountry": "US",
    "entityType": "PRIVATE_PROFIT"
}

response = requests.post(
    "https://api.telnyx.com/public/api/v2/requests",
    json=payload,
    headers={"Authorization": "Bearer YOUR_API_KEY"}
)

if response.status_code == 201:
    data = response.json()
    print(f"Verification created: {data['verificationRequestId']}")
else:
    print(f"Error: {response.status_code} - {response.text}")
```

### JavaScript/TypeScript

```
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

  // BRN Fields (required Feb 2026)
  businessRegistrationNumber: string;
  businessRegistrationType: string;
  businessRegistrationCountry: string;
  entityType?: 'SOLE_PROPRIETOR' | 'PRIVATE_PROFIT' | 'PUBLIC_PROFIT' | 'NON_PROFIT' | 'GOVERNMENT';
}

async function createVerification(request: TollFreeVerificationRequest, apiKey: string) {
  const response = await fetch('https://api.telnyx.com/public/api/v2/requests', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(request)
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(`Verification failed: ${JSON.stringify(error)}`);
  }

  return response.json();
}

// Example usage
const request: TollFreeVerificationRequest = {
  businessName: "Acme Corporation",
  corporateWebsite: "https://www.acme.com",
  businessAddr1: "123 Main Street",
  businessCity: "Chicago",
  businessState: "Illinois",
  businessZip": "60601",
  businessContactFirstName: "John",
  businessContactLastName: "Doe",
  businessContactEmail: "compliance@acme.com",
  businessContactPhone: "+18005551234",
  messageVolume: "100,000",
  phoneNumbers: [{ phoneNumber: "+18773554398" }],
  useCase: "Account Notifications",
  useCaseSummary: "Security alerts and account updates",
  productionMessageContent: "Your code is: 123456",
  optInWorkflow: "Users opt-in during registration",
  optInWorkflowImageURLs: [{ url: "https://www.acme.com/opt-in.png" }],
  additionalInformation: "More context",
  isvReseller: "Yes",
  businessRegistrationNumber: "12-3456789",
  businessRegistrationType: "EIN",
  businessRegistrationCountry: "US",
  entityType: "PRIVATE_PROFIT"
};

createVerification(request, 'YOUR_API_KEY')
  .then(result => console.log('Created:', result.verificationRequestId))
  .catch(error => console.error('Error:', error.message));
```
