---
title: Toll-Free Verification with Business Registration Fields
summary: New Business Registration Number (BRN) fields for toll-free SMS/MMS verification, including mandatory requirements starting February 2026.
sources:
  - url: https://developers.telnyx.com/docs/messaging/toll-free-verification/index
    content_hash: f7546e98b7b5ed455814a4fb1ece85160f58ee4b941b460b88374053d3f04ae8
updated_at: 2026-04-10T00:00:00Z
---

# Toll-Free Verification with Business Registration Fields

New Business Registration Number (BRN) fields for toll-free SMS/MMS verification, including mandatory requirements starting February 2026.

Telnyx toll-free verification now supports Business Registration Number (BRN) fields to strengthen business verification and compliance. Starting **February 17th, 2026**, three BRN fields will be required for all new toll-free verification submissions.

> **Warning:** The following fields are **required** for all new toll-free verification requests:
> 
>   * `businessRegistrationNumber`
>   * `businessRegistrationType`
>   * `businessRegistrationCountry`
> 
>   Submissions missing these fields will be rejected.

## Why This Matters

U.S. wireless carriers require toll-free numbers (800, 888, 877, 866, 855, 844, 833) used for SMS/MMS to complete verification. The new BRN fields provide carriers with verified business identity information, helping to:

* Reduce verification processing time
* Improve approval rates
* Ensure compliance with carrier policies
* Prevent fraudulent messaging

## New Business Registration Fields

### Required Fields (February 17th, 2026)

#### businessRegistrationNumber

The official government-issued business registration identifier.

| Property       | Value                            |
| -------------- | -------------------------------- |
| **Type**       | String                           |
| **Max Length** | 500 characters                   |
| **Required**   | February 17th, 2026              |
| **Nullable**   | Currently yes, no after Feb 2026 |

**Examples by Country**:

| Country        | Type            | Example Format              |
| -------------- | --------------- | --------------------------- |
| United States  | EIN             | `12-3456789` or `123456789` |
| Canada         | Business Number | `123456789RC0001`           |
| United Kingdom | Companies House | `12345678`                  |
| Australia      | ABN             | `51824753556`               |
| Germany        | VAT             | `DE123456789`               |

**Where to Find**:

* **US**: [IRS EIN Lookup](https://www.irs.gov/) - Check your EIN confirmation letter or SS-4 form
* **Canada**: CRA Business Number from your registration documents
* **UK**: [Companies House](https://www.gov.uk/get-information-about-a-company) registration certificate
* **Australia**: [ABN Lookup](https://abr.business.gov.au/)
* **EU**: VAT registration certificate from your national tax authority

#### businessRegistrationType

The type or classification of your business registration.

| Property       | Value                            |
| -------------- | -------------------------------- |
| **Type**       | String                           |
| **Max Length** | 500 characters                   |
| **Required**   | February 17, 2026                |
| **Nullable**   | Currently yes, no after Feb 2026 |

**Common Values**:

* `EIN` - U.S. Employer Identification Number
* `CRA` - Canadian Revenue Agency Business Number
* `Companies House` - UK company registration
* `ABN` - Australian Business Number
* `VAT` - European Union VAT registration
* `SSN` - For U.S. sole proprietors without EIN

#### businessRegistrationCountry

ISO 3166-1 alpha-2 country code of the authority that issued the registration.

| Property     | Value                            |
| ------------ | -------------------------------- |
| **Type**     | String                           |
| **Length**   | Exactly 2 characters             |
| **Format**   | ISO 3166-1 alpha-2               |
| **Required** | February 17, 2026                |
| **Nullable** | Currently yes, no after Feb 2026 |

**Validation**:

* Must be exactly 2 letters
* Only alphabetic characters (A-Z)
* Automatically converted to uppercase (`"us"` → `"US"`)
* Returns HTTP 400 if invalid

**Example Values**: `US`, `CA`, `GB`, `AU`, `DE`, `FR`, `JP`

See complete list: [ISO 3166-1 country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

### Optional Fields

These fields are optional but recommended for faster verification processing.

#### doingBusinessAs

DBA, trade name, or brand name if different from your legal business name.

| Property       | Value          |
| -------------- | -------------- |
| **Type**       | String         |
| **Max Length** | 500 characters |
| **Required**   | No             |

**Example**: Legal name "Acme Corporation Inc.", DBA "Acme Services"

#### entityType

Legal business entity classification.

| Property           | Value                                                                            |
| ------------------ | -------------------------------------------------------------------------------- |
| **Type**           | Enum                                                                             |
| **Required**       | No                                                                               |
| **Allowed Values** | `SOLE_PROPRIETOR`, `PRIVATE_PROFIT`, `PUBLIC_PROFIT`, `NON_PROFIT`, `GOVERNMENT` |

**Value Descriptions**:

| Value             | Description                                  |
| ----------------- | -------------------------------------------- |
| `SOLE_PROPRIETOR` | Individual or sole proprietorship            |
| `PRIVATE_PROFIT`  | Private for-profit corporation (most common) |
| `PUBLIC_PROFIT`   | Publicly traded for-profit company           |
| `NON_PROFIT`      | 501(c) or charitable organization            |
| `GOVERNMENT`      | Government entity or agency                  |

#### optInConfirmationResponse

Message sent to subscribers confirming their opt-in.

| Property       | Value          |
| -------------- | -------------- |
| **Type**       | String         |
| **Max Length** | 500 characters |
| **Required**   | No             |

**Example**: `"You are now subscribed to Acme alerts. Reply STOP to unsubscribe. Msg&data rates may apply."`

#### helpMessageResponse

Automated response when subscribers text HELP.

| Property       | Value          |
| -------------- | -------------- |
| **Type**       | String         |
| **Max Length** | 500 characters |
| **Required**   | No             |

**Example**: `"Acme Support: Call 1-800-555-0123 or email help@acme.com. Reply STOP to unsubscribe."`

#### privacyPolicyURL

URL to your business privacy policy.

| Property       | Value          |
| -------------- | -------------- |
| **Type**       | String         |
| **Max Length** | 500 characters |
| **Required**   | No             |

**Example**: `"https://www.acme.com/privacy"`

<info>
  URL format validation is not enforced. Provide a publicly accessible URL.
</info>

#### termsAndConditionURL

URL to your business terms and conditions.

| Property       | Value          |
| -------------- | -------------- |
| **Type**       | String         |
| **Max Length** | 500 characters |
| **Required**   | No             |

**Example**: `"https://www.acme.com/terms"`

#### ageGatedContent

Indicates if messaging content requires age verification (18+ or 21+).

| Property     | Value   |
| ------------ | ------- |
| **Type**     | Boolean |
| **Default**  | `false` |
| **Required** | No      |

Set to `true` for alcohol, tobacco, cannabis, or other age-restricted content.

#### optInKeywords

Keywords subscribers use to opt-in to your messaging program.

| Property       | Value          |
| -------------- | -------------- |
| **Type**       | String         |
| **Max Length** | 500 characters |
| **Required**   | No             |

**Example**: `"START, YES, SUBSCRIBE, JOIN"`

## API Usage

### Create Verification Request with BRN Fields

**Endpoint**: `POST /public/api/v2/requests`

**Request with BRN Fields**:

```bash theme={null}
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
  "optInWorkflow": "User signs into the Telnyx portal, enters a number and is prompted to select whether they want to use 2FA verification for security purposes. If they'\''ve opted in a confirmation message is sent out to the handset",
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

```json theme={null}
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

```bash theme={null}
curl -X GET https://api.telnyx.com/public/api/v2/requests/550e8400-e29b-41d4-a716-446655440000 \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Response** (HTTP 200):

```json theme={null}
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

```bash theme={null}
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

```python theme={null}
import requests
