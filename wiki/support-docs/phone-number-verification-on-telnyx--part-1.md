---
title: Phone Number Verification on Telnyx
summary: 'Telnyx offers multiple verification features: Verified Numbers let you confirm
  ownership of non-Telnyx phone numbers so they can be used as Caller ID on outbound
  calls, the Verify API enables you to add phone-based verification codes to your
  own applications, and Portal 2FA/TOTP protects your Mission Control Portal account
  login.'
sources:
- url: https://support.telnyx.com/en/articles/12386088-how-to-verify-phone-numbers-behind-an-ivr
  content_hash: e9a69a9acd1ccab089c3a1d6138e81c2a73821908ba8feb1a3a75c4c4bd8a245
- url: https://support.telnyx.com/en/articles/13854980-beta-how-to-verify-phone-numbers-using-dtmf-press-1-to-verify
  content_hash: 9aabcc488a22709ea2cc80cec9e9d4661723bcc82e09aa2daa0820b199806657
- url: https://support.telnyx.com/en/articles/3739748-2fa-totp-setup
  content_hash: f113a7ed6e199ae37151faba0b055d460f53044b520705c62176d963dd581630
- url: https://support.telnyx.com/en/articles/5367966-introducing-the-verify-api
  content_hash: cee0692d25130887bdedfecbb3e4a5fba0d8d0af290f222e937ccc629d3e101c
- url: https://support.telnyx.com/en/articles/5701653-telnyx-verify-2fa-made-easy
  content_hash: 6694db0932af7533a5e86b20846863796f969a8fe5f2b08b2e6aa4b05bbcfdaf
- url: https://support.telnyx.com/en/articles/6790265-verified-numbers-faq
  content_hash: a4a018a51997db5c535a2208f7e7d9d27fe35f91d8c61328f5e4d0c7793ee5a8
- url: https://support.telnyx.com/en/articles/6988813-verified-numbers
  content_hash: a5b09b58059e19c33e4972765182cbe21611220ee85d6cf2fc67e6882b4f4f68
updated_at: 2026-06-11T11:43:04Z
---

# Phone Number Verification on Telnyx

*Part 1 of 2 — see also: [Part 2](phone-number-verification-on-telnyx--part-2.md)*

Telnyx offers multiple verification features: Verified Numbers let you confirm ownership of non-Telnyx phone numbers so they can be used as Caller ID on outbound calls, the Verify API enables you to add phone-based verification codes to your own applications, and Portal 2FA/TOTP protects your Mission Control Portal account login.

## Verified Numbers (Caller ID Verification)

A Verified Number is a phone number that has not been ported to Telnyx but whose owner has authenticated ownership through the Mission Control Portal. Once verified, the number is authorized to display as the calling line identification (CLI) on outbound calls made through the Telnyx platform (SIP Trunking and Programmable Voice). This applies to voice services only, not SMS.

After February 15, 2023, Telnyx users cannot make calls from unverified, non-Telnyx numbers. A call attempt using an unverified non-Telnyx number will be rejected with a **403 Unverified Caller Origination Number D51** SIP error.

Verified Numbers continue to receive incoming calls and messages through the original external provider. If the account owner adds a verified number, it is available to all users in the organization. If a sub-user adds one, it is available exclusively to that user.

### Verifying a Number in the Mission Control Portal

1. Log into the [Mission Control Portal](https://portal.telnyx.com/).
2. Navigate to **Phone Numbers → Verified Numbers** (or use the [direct link](https://portal.telnyx.com/#/numbers/verified-numbers)).
3. Enter the non-Telnyx number in E.164 format (e.g., `+15741156782`).
4. Choose a verification method: **SMS** or **Call**.
5. Receive the validation code and enter it, then press **Verify Number**.

If you choose SMS, a code is sent via text. If you choose Call, a voice call plays the validation code twice.

### Caller ID SIP Header Priority

Once a number is verified, outbound calls must include it in the correct SIP header. The accepted headers, ordered by priority (highest to lowest), are:

1. `P-Preferred-Identity` User
2. `P-Asserted-Identity` User
3. `Remote-Party-Id` User
4. `From` User

See the [Caller ID Number Policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy) for full details.

### Bulk Verification for Large Organizations

If your organization uses over 200 non-Telnyx numbers, Telnyx offers a bulk verification process through a reinforced KYC procedure. Contact your account manager for assistance.

## Verification Methods for Verified Numbers

There are four ways to verify a non-Telnyx number for Caller ID use:

| Method | Description |
|---|---|
| SMS | Receive a code via text message |
| Call | Receive a code via voice call |
| DTMF (Press 1) | Press 1 during an automated call — no code entry needed |
| IVR Extension | Navigate an IVR system to reach the verification target |

All methods can be triggered through the Mission Control Portal or the Verified Numbers API (`POST /v2/verified_numbers`).

## Verifying Numbers Behind an IVR

Some phone numbers sit behind an interactive voice response (IVR) system that requires dialing an extension. Telnyx supports verifying these numbers by including IVR navigation digits in the `extension` parameter.

### How It Works

1. A verification call is initiated with IVR navigation digits included.
2. Telnyx calls the target number.
3. The IVR answers.
4. Telnyx waits and dials the extension.
5. The extension answers.
6. The verification code is played.
7. The user enters the code to complete verification.

### Extension Parameter Syntax

The `extension` parameter is a DTMF sequence:

- `w` = wait 0.5 seconds
- `W` = wait 1 second
- Digits `0–9` and letters `A–D`
- Example: `www2wW4w53ww3`

### API Request

```
curl --location --request POST 'https://api.telnyx.com/v2/verified_numbers' \
  --header 'phone_number: +15741156782' \
  --header 'verification_method: call' \
  --header 'extension: www2wW4w53ww3' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

### Tips

- Always format phone numbers in **E.164**.
- Test your extension sequence manually with the IVR before automating.
- Use `w` to add short waits when the IVR is slow to respond.

## Verifying Numbers Using DTMF (Press 1 to Verify)

DTMF-based verification simplifies the process by eliminating the need to receive and enter a code manually. The recipient simply presses 1 during the verification call to authorize it.

This is useful when coordinating verification with a third party who controls the number, or when verifying numbers in bulk. The verification call does not mention Telnyx, maintaining privacy.

### How It Works

1. You trigger a verification call via the API using the DTMF method.
2. The person receives a call and is prompted to press 1.
3. If they press 1, the number is verified. If not, the verification fails and can be retried.

### API Request

```
curl --location 'https://api.telnyx.com/v2/verified_numbers' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --data '{
    "phone_number": "+15412345678",
    "verification_method": "dtmf"
  }'
```

### Checking Verification Status

```
curl --location 'https://api.telnyx.com/v2/verified_numbers/+1541234567' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

### Receiving Verification Events via Webhooks

Include a `verification_webhook_url` in your request to receive events automatically instead of polling:

```
POST /v2/verified_numbers
{
  "phone_number": "+1541234567",
  "verification_method": "dtmf",
  "verification_webhook_url": "https://your-api.com/api/verification_webhook"
}
```

Webhook payload example:

```json
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

## Bulk Verification

To verify multiple numbers with the DTMF method, loop through your list and make individual API calls for each. Add a delay (e.g., 1 second) between requests to avoid rate limiting.

**Python example:**

```python
import requests
import time

API_KEY = "YOUR_API_KEY"
API_ENDPOINT = "https://api.telnyx.com/v2/verified_numbers"
phone_numbers = ["+15412345678", "+15412345679", "+15412345680"]

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

for phone_number in phone_numbers:
    payload = {
        "phone_number": phone_number,
        "verification_method": "dtmf"
    }
    response = requests.post(API_ENDPOINT, json=payload, headers=headers)
    print(f"Verification initiated for {phone_number}")
    time.sleep(1)
```

**Bash script (CSV input):**

```bash
#!/bin/bash
API_KEY="YOUR_API_KEY"
API_ENDPOINT="https://api.telnyx.com/v2/verified_numbers"

while IFS= read -r phone_number; do
  curl -s --location "$API_ENDPOINT" \
    --header 'Content-Type: application/json' \
    --header "Authorization: Bearer $API_KEY" \
    --data '{"phone_number": "'$phone_number'", "verification_method": "dtmf"}'
  sleep 1
done < phone_numbers.csv
```
