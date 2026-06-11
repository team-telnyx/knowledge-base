---
title: 'Southern Africa: SMS Guidelines'
summary: Consolidated Telnyx guidance for sending SMS across Botswana, Lesotho, Madagascar,
  Malawi, Mauritius, Mozambique, Namibia, South Africa, Zambia, and Zimbabwe, covering
  MCC/dial codes, Sender ID support and registration, content restrictions, and operator-specific
  behaviors.
sources:
- url: https://support.telnyx.com/en/articles/6545173-south-africa-sms-guidelines
- url: https://support.telnyx.com/en/articles/6600928-botswana-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674813-lesotho-sms-guidelines
- url: https://support.telnyx.com/en/articles/6675096-madagascar-sms-guidelines
- url: https://support.telnyx.com/en/articles/6675104-malawi-sms-guidelines
- url: https://support.telnyx.com/en/articles/6677919-mauritius-sms-guidelines
- url: https://support.telnyx.com/en/articles/6677999-mozambique-sms-guidelines
- url: https://support.telnyx.com/en/articles/6678890-namibia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683501-zambia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683504-zimbabwe-sms-guidelines
updated_at: 2026-05-21T08:24:36Z
---

# Southern Africa: SMS Guidelines

Consolidated Telnyx guidance for sending SMS across Botswana, Lesotho, Madagascar, Malawi, Mauritius, Mozambique, Namibia, South Africa, Zambia, and Zimbabwe, covering MCC/dial codes, Sender ID support and registration, content restrictions, and operator-specific behaviors.

## Overview
This page summarizes country-specific SMS requirements in Southern Africa based on Telnyx guidance. It highlights Sender ID policies, registration needs, content rules, and notable carrier behaviors for: Botswana, Lesotho, Madagascar, Malawi, Mauritius, Mozambique, Namibia, South Africa, Zambia, and Zimbabwe.

## Common compliance and best practices
- Always adhere to Telnyx’s Acceptable Use Policy for Messaging: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging
- Obtain and retain proof of opt-in before sending, and include clear opt-out instructions where applicable (especially for marketing traffic).
- Prefer brand-specific Alphanumeric Sender IDs that directly relate to message content; avoid generic Alpha Sender IDs as they may be blocked or replaced.
- Where registration is required, unregistered Alphanumeric Sender traffic will be rejected or altered (e.g., overwritten to generic IDs).

## Sender ID registration process
For destinations that require Alphanumeric Sender ID registration (see country sections), email alpha_sender_id@telnyx.com with:
- Sender ID to register
- Message/content type and example
- Company name (and brand name, if different)
- Company/brand website
- Company country of origin
- Expected monthly volumes
- Email linked to your Telnyx account
- Copy of your Business Registration
Notes:
- Provide a clear business case tying your company/brand to the requested Sender ID. If not obvious, include supporting documentation.

## Botswana
- MCC: 652 | Dial Code: +267
- Sender IDs: Alphanumeric supported; registration not possible.
- Guidance: Avoid generic Alpha Sender IDs; use IDs related to message content.

## Lesotho
- MCC: 651 | Dial Code: +266
- Sender IDs: Alphanumeric supported and maintained; no registration required.
- Content: No stated restrictions.

## Madagascar
- MCC: 646 | Dial Code: +261
- Sender IDs: Registration required; messages from unregistered Alpha IDs will be rejected.
- Compliance: Obtain opt-in and include opt-out options.
- Registration: See “Sender ID registration process.”

## Malawi
- MCC: 650 | Dial Code: +265
- Sender IDs: Registration required; messages from unregistered Alpha IDs will be rejected.
- Compliance: Obtain opt-in and include opt-out options.
- Registration: See “Sender ID registration process.”

## Mauritius
- MCC: 617 | Dial Code: +230
- Sender IDs: Alphanumeric supported and maintained, except toward network Orange Mauritius; no registration required.
- Content: Religious, political, or adult traffic is prohibited.

## Mozambique
- MCC: 643 | Dial Code: +258
- Sender IDs: Alphanumeric supported. Toward Movitel (64303), Alpha IDs may be replaced by a generic Alpha to ensure delivery.
- Content: No stated restrictions.

## Namibia
- MCC: 649 | Dial Code: +264
- Sender IDs: Alphanumeric supported and maintained; no registration required. May occasionally be replaced by a generic Alpha to ensure delivery.
- Content: No stated restrictions.

## South Africa
- MCC: 655 | Dial Code: +27
- Sender IDs: All Alphanumeric Sender IDs will be overwritten to a random local long code.

## Zambia
- MCC: 645 | Dial Code: +260
- Sender IDs: Alphanumeric supported. For network MTN (65402), Alphanumeric is supported only with registration; without registration, Alpha senders may be overwritten to generic or not deliver.
- Guidance: Avoid generic Alpha Sender IDs; use IDs related to message content.
- Registration: Contact alpha_sender_id@telnyx.com.

## Zimbabwe
- MCC: 648 | Dial Code: +263
- Sender IDs: Alphanumeric supported.
  - Local traffic: Registration required.
  - International traffic: Registration not required.
- Guidance: Avoid generic Alpha Sender IDs; use IDs related to message content.
- Registration: Contact alpha_sender_id@telnyx.com.

## Additional resources
- SMS API: https://telnyx.com/products/sms-api
- MMS API: https://telnyx.com/products/mms-api
- Messaging pricing: https://telnyx.com/pricing/messaging
- SMS opt-in guide: https://telnyx.com/resources/sms-opt-in
- SMS number types and traffic: https://telnyx.com/resources/sms-numbers-traffic-types
- Hosted SMS guide: https://telnyx.com/resources/hosted-sms-how-to-guide
- CTIA SMS guidelines overview: https://telnyx.com/resources/CTIA-SMS-guidelines
- Bulk SMS best practices: https://telnyx.com/resources/bulk-sms-guide
- SMS compliance and regulations: https://telnyx.com/resources/how-to-ensure-compliance-with-sms-regulations
