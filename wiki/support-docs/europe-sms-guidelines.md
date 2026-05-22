---
title: 'Europe: SMS Guidelines'
summary: A consolidated reference for sending A2P SMS to select European destinations
  via Telnyx. It covers MCC/dial codes, alphanumeric Sender ID rules, registration
  and brand‑protection programs, content and timing restrictions, and important compliance
  deadlines in Ireland (2025) and Spain (2026).
sources:
- url: https://support.telnyx.com/en/articles/6531704-united-kingdom-sms-guidelines
  content_hash: 1ae8c508095bca96547c4c528a573bd54c5455fb201f570abfc541856891a8d6
- url: https://support.telnyx.com/en/articles/6545161-ireland-sms-guidelines
  content_hash: e732fcf16b3a754f0ba462c75150648e807ab0d73505f04f61a537d4064ed9a6
- url: https://support.telnyx.com/en/articles/6545130-portugal-sms-guidelines
  content_hash: a71120ffdf120b6ea67af795a50318d44cb75013ce5309dbe5465b425e11ec66
- url: https://support.telnyx.com/en/articles/6545140-spain-sms-guidelines
  content_hash: 86db8581aa957d5625b33b9edead716bd4a7637bca256759518e1d27f11efabc
- url: https://support.telnyx.com/en/articles/6531603-france-sms-guidelines
  content_hash: c3606b16b184af3b2257d39faa1a6423b08ae48bce86a74b6525801e93ba825b
- url: https://support.telnyx.com/en/articles/6531675-belgium-sms-guidelines
  content_hash: b03b28d6431bd76de198b75bf19307673b98dc66834d14995848cfe25040877b
- url: https://support.telnyx.com/en/articles/6531581-the-netherlands-sms-guidelines
  content_hash: 0855d30d56865bcc78a4448c0db2e9dcdb5d1e953352abad43dbf22deb482759
- url: https://support.telnyx.com/en/articles/6564006-luxembourg-sms-guidelines
  content_hash: 929b00ff5d568cd32b9ef542114cda1057d0e04a5d9260c0cf90dd5a776ce2c4
- url: https://support.telnyx.com/en/articles/6670878-gibraltar-sms-guidelines
  content_hash: 1dccf2ff402cc7a1ce7a2d230122340ece542d2566edc3520f9951d7ff71969d
- url: https://support.telnyx.com/en/articles/6670869-germany-sms-guidelines
  content_hash: c9e0221deaf30a8c9333b93259f0e84d17819479ad3c76ee7c325f382f4fe025
- url: https://support.telnyx.com/en/articles/6561154-switzerland-sms-guidelines
  content_hash: e006933094b9559e6bfd72ddabe3e8d494da75404dc6aa860a8112f599d5a06b
- url: https://support.telnyx.com/en/articles/6560660-austria-sms-guidelines
  content_hash: 2879c3433705f97c5aa18f1278bddb8ddf683c1ae5ba4f209979e3f5c48e5813
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
