---
title: 'Europe: SMS Guidelines'
summary: A consolidated reference for sending A2P SMS to select European destinations
  via Telnyx. It covers MCC/dial codes, alphanumeric Sender ID rules, registration
  and brand‑protection programs, content and timing restrictions, and important compliance
  deadlines in Ireland (2025) and Spain (2026).
sources:
- url: https://support.telnyx.com/en/articles/6531704-united-kingdom-sms-guidelines
- url: https://support.telnyx.com/en/articles/6545161-ireland-sms-guidelines
- url: https://support.telnyx.com/en/articles/6545130-portugal-sms-guidelines
- url: https://support.telnyx.com/en/articles/6545140-spain-sms-guidelines
- url: https://support.telnyx.com/en/articles/6531603-france-sms-guidelines
- url: https://support.telnyx.com/en/articles/6531675-belgium-sms-guidelines
- url: https://support.telnyx.com/en/articles/6531581-the-netherlands-sms-guidelines
- url: https://support.telnyx.com/en/articles/6564006-luxembourg-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670878-gibraltar-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670869-germany-sms-guidelines
- url: https://support.telnyx.com/en/articles/6561154-switzerland-sms-guidelines
- url: https://support.telnyx.com/en/articles/6560660-austria-sms-guidelines
updated_at: 2026-05-21T08:11:43Z
---

# Europe: SMS Guidelines

A consolidated reference for sending A2P SMS to select European destinations via Telnyx. It covers MCC/dial codes, alphanumeric Sender ID rules, registration and brand‑protection programs, content and timing restrictions, and important compliance deadlines in Ireland (2025) and Spain (2026).

## Overview
Most European destinations listed here support alphanumeric Sender IDs without prior registration. Notable exceptions include Belgium (alphas overwritten), France (time-of-day and format rules plus anti‑phishing whitelisting), the United Kingdom (MEF brand protection for certain names), Ireland (mandatory registration phased in during 2025), and Spain (mandatory registration from June 2026). Always ensure your use case complies with local rules and Telnyx’s Acceptable Use Policy for Messaging.

## United Kingdom (UK)
- MCC: 234–235 | Dial code: +44
- Sender ID: Alphanumeric Sender IDs are supported; no general registration.
- Brand protection: The MEF Registry protects certain high‑risk/brand Sender IDs against spoofing. Only authorized senders may use protected names; a Letter of Authorization (LOA) is required.

## Ireland
- MCC: 272 | Dial code: +353
- Registration: ComReg is implementing mandatory registration for alphanumeric Sender IDs.
  - From July 3, 2025: Unregistered alphanumeric Sender IDs will be overwritten to “Likely Scam”.
  - From October 3, 2025: Unregistered alphanumeric Sender IDs will be blocked (messages will not deliver).
- Process: First register as a Sender ID Owner (SIDO) with ComReg and select Telnyx as your Participating Aggregator/OPA. Only the Sender ID owner may register its alphanumeric IDs (ISVs/resellers cannot register on behalf of clients).
- Help: alpha_sender_id@telnyx.com
- ComReg SIDO portal: https://www.comreg.ie/industry/electronic-communications/nuisance-communications/sms-sender-id-registry/

## Spain
- MCC: 214 | Dial code: +34
- Registration: Under CNMC Circular 1/2026, alphanumeric Sender IDs must be registered to send SMS to Spain starting June 7, 2026.
- What to provide (per alias) to alpha_sender_id@telnyx.com:
  - Company details: legal name, NIF/CIF (or EU‑VAT if outside Spain), registered address.
  - Legal representative: full name, NIF/passport, mobile number, email.
  - Sender ID details: exact alias, use case (e.g., transactional/OTP/marketing), planned start/end date (registrations valid max 24 months).
  - Proof of ownership (one): trademark/trade name certificate (OEPM/EUIPO), company name certificate (Spanish Mercantile Registry), or matching domain ownership (.es or ICANN‑registered domain).

## France
- MCC: 208 | Dial code: +33
- Sender ID: Alphanumeric Sender IDs supported; no general registration.
- Format: Special characters in alphanumeric Sender IDs are prohibited as of March 1, 2026.
- Operator handling: For MVNO NRJ (20826) and Truphone (20812), alphanumeric Sender IDs may be replaced by a random local number or a short code.
- Marketing timing: Promotional/marketing SMS are not allowed on Sundays and French public holidays, and between 22:00 and 08:00. Messages sent during restricted times are queued for later delivery.
- Opt‑out: Marketing messages must include a clear opt‑out. The fragment “STOP au 36179” must be appended and will be auto‑added if missing.
- Anti‑phishing: Certain alphanumeric Sender IDs are whitelisted; use requires an LOA.

## Belgium
- MCC: 206 | Dial code: +32
- Sender ID: All alphanumeric Sender IDs are overwritten to a random local long code or a short code to ensure delivery.

## Germany
- MCC: 262 | Dial code: +49
- Sender ID: Alphanumeric Sender IDs supported; no registration required.
- Content: No additional content restrictions noted.

## The Netherlands
- MCC: 204 | Dial code: +31
- Sender ID: Alphanumeric Sender IDs supported; no registration required.
- Content: No additional content restrictions noted.

## Portugal
- MCC: 268 | Dial code: +351
- Sender ID: Alphanumeric Sender IDs supported; no registration required.
- Content: No additional content restrictions noted.

## Luxembourg
- MCC: 270 | Dial code: +352
- Sender ID: Alphanumeric Sender IDs supported; no registration required.
- Content: No additional content restrictions noted.

## Switzerland
- MCC: 228 | Dial code: +41
- Sender ID: Alphanumeric Sender IDs supported; no registration required.
- Content: No additional content restrictions noted.

## Austria
- MCC: 232 | Dial code: +43
- Sender ID: Alphanumeric Sender IDs supported; no registration required.
- Content: No additional content restrictions noted.

## Gibraltar
- MCC: 266 | Dial code: +350
- Sender ID: Alphanumeric Sender IDs supported; no registration required.
- Content: No additional content restrictions noted.

## Best practices and references
- Register early where required: Complete Ireland SIDO and Spain alias submissions well in advance of enforcement dates to avoid overwriting or blocking.
- Use compliant Sender IDs: Avoid special characters in France; be prepared for operator‑side replacement in France (specific MVNOs) and Belgium (system‑wide).
- Include opt‑out where applicable: In France, ensure “STOP au 36179” is present for marketing messages.
- Brand protection: If your brand appears in protected/whitelisted programs (UK MEF, France anti‑phishing list), obtain and submit the required LOA before sending.
- Policy: Review Telnyx’s Acceptable Use Policy for Messaging: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging
- Products and definitions: Learn about A2P messaging and short codes:
  - A2P overview: https://telnyx.com/resources/what-is-a2p-messaging
  - SMS short codes: https://telnyx.com/products/sms-short-code
