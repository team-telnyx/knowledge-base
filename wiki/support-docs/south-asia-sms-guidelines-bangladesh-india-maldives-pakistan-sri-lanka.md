---
title: 'South Asia SMS Guidelines: Bangladesh, India, Maldives, Pakistan, Sri Lanka'
summary: A consolidated guide to Telnyx SMS rules for Bangladesh, India, Maldives,
  Pakistan, and Sri Lanka, covering MCC/dial codes, Sender ID support and registration,
  delivery behaviors, content/network restrictions, and how to register an Alphanumeric
  Sender ID.
sources:
- url: https://support.telnyx.com/en/articles/6596161-bangladesh-sms-guidelines
  content_hash: b173d813c4eea1fd4e68775fe5a745d4bc34c85a5b1cddca58ee9a89507fb014
- url: https://support.telnyx.com/en/articles/6674383-india-sms-guidelines
  content_hash: ed219859b270de805c8ec44907e8284845f9ad574c8de00e582b0fc73c103eff
- url: https://support.telnyx.com/en/articles/6675222-maldives-sms-guidelines
  content_hash: f013c24dc419924aecd1d2d6ed35fda07f40ab4b4fbfd4b819895848ed0b9eea
- url: https://support.telnyx.com/en/articles/6679149-pakistan-sms-guidelines
  content_hash: e5dbedc0b90d8a7d809b04149860e5aa7362db57490119e71e3ed71a16c51907
- url: https://support.telnyx.com/en/articles/6680171-sri-lanka-sms-guidelines
  content_hash: 34db58ffd638b8d077264cf95a4b27b13e5ecbd4047ff47da4ad7d0dd37af90e
updated_at: 2026-05-21T08:27:41Z
---

# South Asia SMS Guidelines: Bangladesh, India, Maldives, Pakistan, Sri Lanka

A consolidated guide to Telnyx SMS rules for Bangladesh, India, Maldives, Pakistan, and Sri Lanka, covering MCC/dial codes, Sender ID support and registration, delivery behaviors, content/network restrictions, and how to register an Alphanumeric Sender ID.

## Alpha Sender ID registration requirements
Alphanumeric Sender ID (Alpha) registration is required in several South Asian destinations. To request registration, email alpha_sender_id@telnyx.com with a copy of your Business Registration and the following details:

- Sender ID to be registered
- Message/content type
- Message/content example
- Company name (and Brand name if different)
- Website of brand or company
- Company country of origin
- Expected monthly volumes
- Email linked to your Telnyx account

A valid business case is required. If the relationship between your company/brand and the requested Sender ID is not obvious, include supporting documentation that clarifies your use case.

## Compliance and best practices
- Obtain consent (proof of opt-in) before sending communications, especially for marketing.
- Include clear opt-out instructions in your messages.
- Use brand-specific Sender IDs; avoid generic Sender IDs where discouraged by local policy.
- Always follow Telnyx’s Acceptable Use Policy for Messaging: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging

## Bangladesh (MCC 470, Dial 880)
- Alpha Sender ID registration is required; messages from unregistered Sender IDs will be rejected.
- Follow the registration requirements above (Alpha Sender ID registration requirements).
- Consent and clear opt-out are recommended.

## India (MCC 404–405, Dial 91)
- Alpha Sender IDs are partially supported via registration: only Local Alpha Sender IDs (local entities) can be registered through the DLT process.
- International Alpha Sender IDs cannot be registered; they will be overwritten to a random Short Code to ensure delivery: https://telnyx.com/products/sms-short-code

## Maldives (MCC 472, Dial 960)
- Alpha Sender IDs are supported and preserved; no registration required.
- No content restrictions are specified for this destination.

## Pakistan (MCC 410, Dial 92)
- Alpha Sender ID registration is required.
- Gambling-related traffic is not permitted.
- Consent and clear opt-out are recommended.

## Sri Lanka (MCC 413, Dial 94)
- Alpha Sender ID registration is required; messages from unregistered Sender IDs will be rejected.
- Network-specific rule: Mobitel (41301) allows only OTP/transactional traffic; non-OTP messages will be rejected by the network.
- Avoid generic Alpha Sender IDs; the Sender ID should directly reflect the brand/content.
- Consent and clear opt-out are recommended.

## Support
For questions or to start Sender ID registration, email alpha_sender_id@telnyx.com.
