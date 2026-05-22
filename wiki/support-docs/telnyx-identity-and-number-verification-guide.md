---
title: Telnyx Identity and Number Verification Guide
summary: 'A practical guide to Telnyx identity and verification tools: verifying third‑party
  phone numbers to your account (including IVR and Press‑1 DTMF flows), building user
  2FA with the Verify API, validating numbers with Number Lookup, and understanding
  CLI/CLD validation impacts—across both API and Mission Control Portal paths.'
sources:
- url: https://support.telnyx.com/en/articles/12386088-how-to-verify-phone-numbers-behind-an-ivr
  content_hash: 44437388e6d35cdce46da0db26cf25afb62d80c30ecae1ffb328c69e862f595d
- url: https://support.telnyx.com/en/articles/13854980-beta-how-to-verify-phone-numbers-using-dtmf-press-1-to-verify
  content_hash: e341a94ed95d3191bf9aac69be438176f7fb9049b57e7b4bf72e8033b5cf9dc9
- url: https://support.telnyx.com/en/articles/5367966-introducing-the-verify-api
  content_hash: 0c05734469ef708e370c9f622e21b40e6de2eda986d641aee6559ecc94844e3a
- url: https://support.telnyx.com/en/articles/5701653-telnyx-verify-2fa-made-easy
  content_hash: ac2201395e46f225749a12f39260659c073130a43a716f2a96858b52aded99b6
- url: https://support.telnyx.com/en/articles/4366901-your-number-lookup-guide
  content_hash: 5939b3d259d25caf42354ca72481ba9603f80feaeac9e1e05a017de288220983
- url: https://support.telnyx.com/en/articles/6247033-cli-cld-validation-faq
  content_hash: 991377ab37de3041ed711fa52b1f77b135ad869a2fc5e7ab5b2039a8ab616606
- url: https://support.telnyx.com/en/collections/3968260-telnyx-identity-verification-tools
  content_hash: cc52e5b259243aabae24498466f5998983010078d03118b31185f140db586c31
updated_at: 2026-05-20T15:33:12Z
---

# Telnyx Identity and Number Verification Guide

A practical guide to Telnyx identity and verification tools: verifying third‑party phone numbers to your account (including IVR and Press‑1 DTMF flows), building user 2FA with the Verify API, validating numbers with Number Lookup, and understanding CLI/CLD validation impacts—across both API and Mission Control Portal paths.

## Choosing the right tool
- Verified Numbers: Proves you control a phone number so it can be associated with your Telnyx account (e.g., for caller ID/caller verification). Triggered as an outbound verification call to that number.
- Press‑1 (DTMF) verification: A simplified Verified Numbers method where the callee just presses 1 to confirm.
- IVR extension support: Lets Telnyx auto‑navigate an IVR before playing the verification prompt/code.
- Verify API (2FA): A separate product to send and check one‑time codes to your end users over SMS, voice, or flash call.
- Number Lookup: Retrieves LRN, carrier, and CNAM data to validate/clean numbers and reduce failures.
- CLI/CLD validation: Network‑level checks that can block calls if caller/destination numbers are invalid in NANP databases.

## Verified Numbers via API
Prerequisites:
- Telnyx API key (include Authorization: Bearer YOUR_API_KEY)
- Destination phone number in E.164 format

Create a verification: POST /v2/verified_numbers
- phone_number: E.164 destination (e.g., +15741156782)
- verification_method: "call" (code prompt) or "dtmf" (Press‑1)
- extension (optional): DTMF to traverse IVR; supports 0–9, A–D, plus waits:
  - w = 0.5s pause; W = 1s pause (e.g., www2wW4w53ww3)
- verification_webhook_url (optional, for event callbacks)

Behavior:
- Standard call (method "call"): Telnyx calls, plays a verification code, and the recipient types the code to complete.
- With IVR extension: Telnyx waits/dials the provided sequence to reach the right party, then plays the prompt/code.
- Press‑1 (method "dtmf"): Callee is prompted to press 1 to authorize. The call does not mention Telnyx.

Check status: GET /v2/verified_numbers/{E.164}

Webhooks: When using verification_webhook_url, you’ll receive completion events (e.g., caller_id_verification.completed) including timestamps.

Tips:
- Always use E.164 formatting.
- Test your IVR DTMF sequence manually; add w/W delays for reliability.
- Add small delays when bulk‑initiating verifications to avoid rate limits.
- Keep API keys private.

## Verified Numbers in Mission Control Portal
- Go to Numbers > Verified Numbers (direct: https://portal.telnyx.com/#/numbers/verified-numbers).
- Add the target number and (if needed) the IVR extension sequence using w/W as required.
- Choose “Call me with a code” or “Press 1 to verify” (DTMF). The number appears under the Verified Numbers tab once completed.

## Press‑1 (DTMF) verification specifics
- API: POST /v2/verified_numbers with verification_method="dtmf".
- Bulk flows: Loop through numbers and space requests (e.g., 1s) to prevent rate limiting.
- Troubleshooting: If the user doesn’t press 1 or misses the prompt, retry. Ensure the number can receive calls and is correctly formatted.

## Telnyx Verify API (user 2FA)
Purpose: Build app‑level user verification flows with one‑time codes. This is distinct from Verified Numbers.

Setup:
- Create a Verify Profile in the Portal (Verify > Profiles). The profile controls channel, timeouts, templates, webhooks, and spend controls.

Send a code:
- Use the Verify API for your chosen channel (e.g., POST /v2/verifications/sms) with phone_number and verify_profile_id. Voice and flash call channels are supported when enabled on your profile.

Check a code:
- Submit the received code with the same verify_profile_id (e.g., POST /v2/verifications/by_phone_number/%2B<number>/actions/verify).

Webhooks:
- Optionally configure a webhook URL in the Verify Profile to receive real‑time status updates.

Production recommendations:
- Rate‑limit by user/number/IP/session; add CAPTCHA or other abuse checks.
- Set sensible code expiry/retry limits; monitor for SMS pumping/toll fraud.
- Avoid leaks that confirm account existence; review spend controls and alerts.

Pricing: https://telnyx.com/pricing/verify-api

Docs:
- Quickstart: https://developers.telnyx.com/docs/identity/verify/quickstart
- DTMF confirmations: https://developers.telnyx.com/docs/identity/verify/dtmf-confirm
- Custom templates: https://developers.telnyx.com/docs/identity/verify/custom-templates
- Verify webhooks: https://developers.telnyx.com/docs/identity/verify/receiving-webhooks
- Verify code check reference: https://developers.telnyx.com/api-reference/verify/verify-verification-code-by-phone-number.md

## Number Lookup essentials
What it does: Returns Local Routing Number (LRN), carrier (MCC/MNC), and CNAM to validate numbers, reduce undeliverables, and help defend against fraud.

Portal path:
- Sign in, open https://portal.telnyx.com/#/lookup, enter a number, choose Lookup Type (None/LRN, Carrier, Caller Name, Both), then Lookup Number.

Prerequisites and access:
- Telnyx account, positive balance, API key for API access.
- Full LRN data requires enabling “Permitted NPAC User” in Account Settings > Profile (allow ~15 minutes).
- Owner‑only access (not available to sub‑accounts). US Toll‑Free Resporg ID is not returned.

Costs (indicative; check your rates):
- LRN: $0.0015/query; Carrier (mobile): $0.0025/query; CNAM: $0.003/query; Inbound CNAM: $0.40/number/month; Outbound CNAM listing: Free.

API docs:
- Quickstart: https://developers.telnyx.com/docs/identity/number-lookup/quickstart
- Pricing/rates: https://portal.telnyx.com/#/pricing/telco

Usage review:
- Invoices monthly; usage under Reporting > Usage Reports. Reports are not real‑time (today’s appear tomorrow).

Troubleshooting:
- Service unavailable: Add funds.
- Incomplete LRN: Enable NPAC user.
- 401 Unauthorized: Verify API key/headers.
- Sub‑user denied: Use organization owner credentials.

## CLI & CLD validation (call blocking basics)
Definitions:
- CLI (Calling Line Identity): the calling number.
- CLD (Calling Line Destination): the called number.

What’s enforced:
- For outbound calls between NANP geographies (excluding toll‑free), Telnyx checks number format and presence in North American numbering databases. Invalid CLI/CLD calls are rejected at the network edge.

Valid NANP format:
- Ten digits NXX‑NXX‑XXXX (N=2–9, X=0–9), prefixed with country code +1 in E.164 for APIs.

Errors you’ll see:
- CLI invalid: SIP 403 “The origination number does not have a subscriber assigned. The number is invalid.”
- CLD invalid: SIP 404 “The destination number does not have a subscriber assigned. The number is invalid.”

Notes:
- This validation is service‑wide and cannot be disabled.
- Use Number Lookup proactively to check numbers before placing calls.
- If you believe a valid call was blocked, gather details and contact Telnyx Support: https://support.telnyx.com/en/articles/5170721-best-practices-for-contacting-support

## Putting it together: recommended flow
- Clean and validate numbers first with Number Lookup (format, carrier, CNAM as needed).
- If you need account‑level control of a third‑party number: use Verified Numbers (Press‑1 for simplicity, or IVR DTMF when behind an IVR).
- If you need user authentication in your product: implement the Verify API with a Verify Profile.
- Monitor CLI/CLD validation outcomes and debug call failures in Mission Control’s debugging tools: https://support.telnyx.com/en/articles/4304872-telnyx-debugging-tools

## Quick links
- Verified Numbers API (create): https://developers.telnyx.com/api/verified-numbers/create-verified-number
- Verified Numbers (request phone number verification): https://developers.telnyx.com/api-reference/verified-numbers/request-phone-number-verification
- Mission Control Portal: https://portal.telnyx.com/
- Release Notes: https://telnyx.com/release-notes
