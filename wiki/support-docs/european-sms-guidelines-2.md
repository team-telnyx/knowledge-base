---
title: European SMS Guidelines
summary: A consolidated reference for SMS guidelines across European countries supported
  by Telnyx, covering MCC, dial codes, alphanumeric sender ID support, registration
  requirements, and specific content or routing restrictions.
sources:
- url: https://support.telnyx.com/en/articles/6531581-the-netherlands-sms-guidelines
- url: https://support.telnyx.com/en/articles/6531603-france-sms-guidelines
- url: https://support.telnyx.com/en/articles/6531675-belgium-sms-guidelines
- url: https://support.telnyx.com/en/articles/6545130-portugal-sms-guidelines
- url: https://support.telnyx.com/en/articles/6545140-spain-sms-guidelines
- url: https://support.telnyx.com/en/articles/6560660-austria-sms-guidelines
- url: https://support.telnyx.com/en/articles/6561154-switzerland-sms-guidelines
- url: https://support.telnyx.com/en/articles/6564006-luxembourg-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670869-germany-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670878-gibraltar-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674999-liechtenstein-sms-guidelines
- url: https://support.telnyx.com/en/articles/6677954-monaco-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679992-san-marino-sms-guidelines
updated_at: 2026-06-11T11:19:55Z
---

# European SMS Guidelines

A consolidated reference for SMS guidelines across European countries supported by Telnyx, covering MCC, dial codes, alphanumeric sender ID support, registration requirements, and specific content or routing restrictions.

## Standard Sender ID and Content Guidelines
For the following countries, Alphanumeric Sender IDs are supported and will be maintained without registration. There are no restrictions on message content towards these destinations.

| Country | MCC | Dial Code |
|---|---|---|
| Austria | 232 | +43 |
| Germany | 262 | +49 |
| Gibraltar | 266 | +350 |
| Liechtenstein | 295 | +423 |
| Luxembourg | 270 | +352 |
| Monaco | 212 | +377 |
| Netherlands | 204 | +31 |
| Portugal | 268 | +351 |
| San Marino | 292 | +378 |
| Switzerland | 228 | +41 |

## Belgium
**MCC:** 206 | **Dial Code:** +32

All Alphanumeric Sender IDs will be overwritten to either a random Local Long Code or Short Code to ensure delivery.

## France
**MCC:** 208 | **Dial Code:** +33

Alphanumeric Sender IDs are supported and maintained without registration. Telnyx advises using Alphanumeric Sender IDs for all A2P traffic towards France. However, there are several specific requirements and restrictions:

- **Special Characters:** As of March 1, 2026, the use of special characters in Alphanumeric Sender IDs is not allowed.
- **MVNO Routing:** When sending towards MVNO NRJ (20826) and Truphone (20812), Alphanumeric Sender IDs will be replaced by either a random local number or a Short Code.
- **Marketing Restrictions:** Local operators do not allow marketing or promotional traffic on Sundays and French Public Holidays between 10 pm and 8 am. Messages attempted during this time are queued and delivery is attempted afterward.
- **Opt-Out Requirement:** All marketing or promotional traffic must include a clear option to opt-out. The fragment `STOP au 36179` must be added at the end of the message; if missing, it will be added automatically.
- **Anti-Phishing Measures:** French operators have implemented an additional whitelisting check on a group of Alphanumeric Sender IDs. Traffic using these IDs is only possible through the submission of a duly signed Letter of Authorization.

## Spain
**MCC:** 214 | **Dial Code:** +34

Spain's telecoms regulator (CNMC) is rolling out a new Alias Registry as part of Circular 1/2026. Starting **June 7, 2026**, any Alphanumeric Sender ID must be registered before it can be used to send messages to Spanish numbers (+34).

To register, provide the following details to [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com):

1. **Company Details**
   - Full legal company name
   - NIF/CIF (Spanish tax ID) or EU-VAT number (if based outside Spain)
   - Registered company address
2. **Legal Representative**
   - Full name
   - NIF or passport number
   - Mobile number and email address
3. **Sender ID Details** (one set per alias)
   - The exact alias as it appears in messages (e.g., MYBRAND)
   - Use case (transactional, OTP, marketing, etc.)
   - Planned start and end date (valid for a maximum of 24 months)
4. **Proof of Ownership** (one per alias)
   - Trademark or trade name: certificate from OEPM (Spain) or EUIPO (EU)
   - Company name: certificate from the Spanish Mercantile Registry
   - Domain name: proof of ownership of a .es or ICANN-registered domain matching the alias

## Acceptable Use Policy
Always refer to the [Acceptable Use Policy for Messaging](https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging) when sending SMS to any destination.
