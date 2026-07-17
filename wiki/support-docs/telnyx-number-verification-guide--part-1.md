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

*Part 1 of 3 — see also: [Part 2](telnyx-number-verification-guide--part-2.md), [Part 3](telnyx-number-verification-guide--part-3.md)*

Telnyx provides several verification mechanisms for phone numbers used on its platform, including Verified Numbers for non-Telnyx numbers used as outbound CLI, Toll-Free Verification for outbound SMS from toll-free numbers, and Number Lookup for retrieving carrier and CNAM data. This page consolidates the verification workflows, API usage, pricing, error codes, and related number management resources.

## Overview

Telnyx offers several verification mechanisms to confirm ownership and authorization of phone numbers used on its platform. These include [Verified Numbers](verified-numbers.md) for non-Telnyx numbers used as outbound CLI, [Toll-Free Verification](toll-free-verification.md) for sending outbound SMS from toll-free numbers, and supplementary tools such as [Number Lookup](number-lookup.md) and the now-sunset Google Verified Calls program.

## Verified Numbers

A Verified Number is a phone number that has not been ported to Telnyx but whose owner has authenticated ownership through the Mission Control Portal. Verified Numbers continue to receive incoming calls and messages through their original external provider, but can be used as the CLI on outbound calls made through Telnyx.

After February 15, 2023, Telnyx users cannot make calls from unverified numbers that have not been ported to Telnyx. A call attempt using a non-Telnyx number that has not been verified is rejected with a `403 Unverified Caller Origination Number D51` SIP error.

### Verification Methods

Telnyx supports three verification methods:

- **SMS** — A validation code is sent to the non-Telnyx number via SMS.
- **Voice call** — A voice call is placed to the non-Telnyx number and an IVR plays the validation code twice.
- **DTMF (Press 1 to Verify)** — An automated call is placed to the phone number, and the recipient simply presses 1 to authorize. No verification code is needed. This is useful when coordinating verification with a third party who controls the number, or when verifying numbers in bulk.

### Verifying via the Mission Control Portal

1. Log into the Mission Control Portal and select **Phone Numbers** in the Voice Suite from the navigation menu.
2. Choose **My Numbers** to view all Telnyx numbers associated with your account.
3. Back to the navigation menu, select **Verified Numbers** to access the Verified Numbers section.
4. Enter the non-Telnyx number you want to verify and select your preferred method (SMS or Call).
5. Enter the verification code and press **Verify Number**.
6. The number will now appear on the list of Verified Numbers and is authorized to display as the CLI on calls made through the Telnyx platform.

### Verifying via the API

Use the [Create Verified Number](https://developers.telnyx.com/api/messaging/toll-free-verification/submit-verification-request) endpoint. The `phone_number` must be in E.164 format (e.g., `+15412345678`).

Single number verification:

```
POST /v2/verified_numbers
{
  "phone_number": "+1541234567",
  "verification_method": "dtmf"
}
```

cURL example:

```
curl --location 'https://api.telnyx.com/v2/verified_numbers' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --data '{
    "phone_number": "+15412345678",
    "verification_method": "dtmf"
  }'
```

To verify multiple phone numbers at once, loop through your list and make individual API calls for each. Add a delay (e.g., `time.sleep(1)` in Python or `sleep 1` in Bash) between requests to avoid rate limiting.

### Checking Verification Status

```
curl --location 'https://api.telnyx.com/v2/verified_numbers/+1541234567' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

### Receiving Verification Events via Webhooks

Register a webhook to receive verification events automatically instead of polling the API. Include a `verification_webhook_url` in your request:

```
POST /v2/verified_numbers
{
  "phone_number": "+1541234567",
  "verification_method": "dtmf",
  "verification_webhook_url": "https://your-api.com/api/verification_webhook"
}
```

Verification events are pushed to the webhook URL in the following format:

```
{
  "data": {
    "event_type": "caller_id_verification.completed",
    "id": "evt_abcd-456-hijsk-123",
    "occurred_at": "YYYY-MM-DDT14:22:07.123456Z",
    "payload": {
      "phone_number": "+1245456784",
      "record_type": "caller_id_verification",
      "verification_method": "outbound_call",
      "verified_at": "YYYY-MM-DDT14:21:58.654321Z"
    },
    "record_type": "event"
  }
}
```

### Verifying Numbers Behind an IVR

Some phone numbers sit behind an IVR (interactive voice response) system and require dialing an extension to reach the right person. Telnyx supports verifying numbers behind an IVR automatically through the API and the Mission Control Portal.

Standard behavior:

1. Verification call is initiated.
2. Telnyx calls the target phone number.
3. Call is answered.
4. Verification code is played.
5. User enters the code to complete verification.

New behavior (with IVR extensions):

1. Verification call is initiated, including IVR navigation digits.
2. Telnyx calls the target phone number.
3. Call is answered by the IVR.
4. Telnyx waits, then dials the extension.
5. Extension answers the call.
6. Verification code is played.
7. User enters the code to complete verification.

The `extension` parameter accepts a DTMF sequence to navigate the IVR:

- `w` = wait 0.5 seconds
- `W` = wait 1 second
- Digits `0–9` and letters `A–D`
- Example: `www2wW4w53ww3`

cURL example:

```
curl --location --request POST 'https://api.telnyx.com/v2/verified_numbers' \
  --header 'phone_number: +15741156782' \
  --header 'verification_method: call' \
  --header 'extension: www2wW4w53ww3' \
  --header 'Authorization: Bearer KEYXXXXXXXXXXXXXX'
```

In the Mission Control Portal, navigate to **Real-Time Communications → Numbers → Manage Numbers**, switch to the **Verified Numbers** tab, add the number and extension, and select **Call me with a code**.

### Pricing

There is a one-off charge of $0.03 for each number verified, plus a separate charge based on the user destination and channel used to send the verification request.

| Method | Cost |
| --- | --- |
| Verified Number via SMS | $0.03 per successful verification + SMS API pricing |
| Verified Number via Voice call | $0.03 per successful verification + Voice API pricing |
| Verified Number via Flash call | $0.03 per successful verification + Flash pricing |

### Sharing Verified Numbers Across an Organization

- If the account owner adds a verified number, the number is available to be used by all users in the organization.
- If a sub-user adds a verified number, the number is available exclusively for that particular user only.
- To share verified numbers across the organization, ask the account admin user to verify the number.

### Bulk Verification

If you have over 200 non-Telnyx numbers on calls through the Telnyx platform, Telnyx will assist you through a bulk verification process. This is a reinforced KYC process carried out with the help of your account manager.

### Caller ID Headers

Once numbers are verified and used for outbound calls, Telnyx's caller ID policy applies. The following SIP headers can carry the Caller ID Number, ordered by priority (1 highest, 4 lowest):

1. `P-Preferred-Identity` User
2. `P-Asserted-Identity` User
3. `Remote-Party-Id` User
4. `FROM` User

Send the verified number in one of these headers, taking into account the order priority.

### Tips for Success

- Always format phone numbers in E.164 (e.g., `+1` for US numbers).
- Test your extension sequence manually with the IVR before automating.
- Use `w` to add short waits when the IVR is slow to respond.
- Keep your API key private — never share it publicly.
- Add delays between bulk verification requests to avoid rate limiting.
- Implement error handling for failed verification attempts.
- If a user doesn't answer or press 1, retry the verification call.

### Troubleshooting

- **Verification call not received:** Verify the phone number is correct and can receive calls.
- **User didn't press 1 in time:** Retry the verification call.
- **Rate limit exceeded:** Add delays between requests.
- **Invalid phone number format:** Ensure phone numbers are in E.164 format (e.g., `+15412345678`).
