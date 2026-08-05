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

*Part 3 of 6 — see also: [Part 1](toll-free-verification--part-1.md), [Part 2](toll-free-verification--part-2.md), [Part 4](toll-free-verification--part-4.md), [Part 5](toll-free-verification--part-5.md), [Part 6](toll-free-verification--part-6.md)*

Telnyx toll-free verification requires Business Registration Number (BRN) fields for all new submissions starting February 17, 2026. This page covers the required and optional fields, API usage for creating, retrieving, and updating verification requests, common rejection reasons, the resubmission process, delivery troubleshooting, and guidance on choosing between toll-free and 10DLC messaging.

## Error Handling

### Validation Errors (HTTP 400)

**Missing Required Fields (After February 2026)**:

```
{
  "errors": [
    {
      "field": "businessRegistrationNumber",
      "message": "This field is required as of February 17th 2026"
    },
    {
      "field": "businessRegistrationType",
      "message": "This field is required as of February 17th 2026"
    },
    {
      "field": "businessRegistrationCountry",
      "message": "This field is required as of February 17th 2026"
    }
  ]
}
```

**Invalid Country Code**:

```
{
  "detail": "businessRegistrationCountry must be a 2-character ISO 3166-1 alpha-2 country code"
}
```

**Invalid Entity Type**:

```
{
  "detail": "entityType must be one of: SOLE_PROPRIETOR, PRIVATE_PROFIT, PUBLIC_PROFIT, NON_PROFIT, GOVERNMENT"
}
```

### Other Status Codes

| Code | Description |
| --- | --- |
| 200 | Success (GET, PATCH) |
| 201 | Created (POST) |
| 204 | Deleted (DELETE) |
| 400 | Bad Request — Invalid data |
| 401 | Unauthorized — Invalid API key |
| 404 | Not Found — Invalid request ID |
| 422 | Unprocessable Entity — Invalid format |

## Migration Guide

### Timeline

| Period | Status | Action |
| --- | --- |
| **Now – Dec 2025** | Optional | BRN fields can be included but not required |
| **Feb 1, 2026** | Mandatory | All 3 required BRN fields must be included |

### Preparation Steps

**1. Gather Business Registration Information**

Locate your:

- Business registration number (EIN, VAT, ABN, etc.)
- Registration type identifier
- Issuing country code

**2. Update Your Integration**

Add BRN fields to your API requests:

```
const request = {
  businessName: "Acme Corp",
  corporateWebsite: "https://acme.com",
  // ... other required fields
  businessRegistrationNumber: "12-3456789",
  businessRegistrationType: "EIN",
  businessRegistrationCountry: "US"
};
```

**3. Test Your Implementation**

- Submit test requests with BRN fields
- Verify fields are returned in responses
- Test validation error handling
- Confirm country code uppercase conversion

**4. Update Error Handling**

Prepare for validation errors after February 2026:

```
try {
  const result = await createVerification(request);
} catch (error) {
  if (error.status === 400) {
    console.error('Validation failed:', error.errors);
    // Handle missing BRN fields
  }
}
```

### Backward Compatibility

**Until February 17, 2026**:

- Requests without BRN fields continue to work
- No breaking changes to existing integrations
- BRN fields default to `null` if not provided

**After February 17, 2026**:

- Requests without 3 required BRN fields will be rejected (HTTP 400)
- Update your integration before this date

## Verification Lifecycle

Understanding where your verification can fail helps target the right fix:

| Stage | Timeline | What happens |
| --- | --- | --- |
| **Submission** | Instant | API validates fields, returns 201 or error |
| **Under review** | 1–2 weeks | Carriers review business identity and messaging use case |
| **Decision** | — | Approved (full throughput) or rejected (with reason) |
| **Resubmission** | Instant | Fix issues and resubmit — no limit on attempts |
