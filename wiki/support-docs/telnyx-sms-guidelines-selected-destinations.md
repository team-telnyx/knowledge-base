---
title: 'Telnyx SMS Guidelines: Selected Destinations'
summary: Consolidated Telnyx SMS sending guidelines for France, the United Kingdom,
  Portugal, Spain, Denmark, Sweden, Finland, Iceland, Angola, Cape Verde, Cuba, the
  Faroe Islands, Greenland, Sao Tome and Principe, and the Republic of Korea, covering
  MCC/dial codes, Alphanumeric Sender ID support, registration and whitelisting requirements,
  content restrictions, and country-specific delivery rules.
sources:
- url: https://support.telnyx.com/en/articles/6531603-france-sms-guidelines
- url: https://support.telnyx.com/en/articles/6531704-united-kingdom-sms-guidelines
- url: https://support.telnyx.com/en/articles/6545130-portugal-sms-guidelines
- url: https://support.telnyx.com/en/articles/6545140-spain-sms-guidelines
- url: https://support.telnyx.com/en/articles/6560665-denmark-sms-guidelines
- url: https://support.telnyx.com/en/articles/6560689-sweden-sms-guidelines
- url: https://support.telnyx.com/en/articles/6560706-finland-sms-guidelines
- url: https://support.telnyx.com/en/articles/6560909-iceland-sms-guidelines
- url: https://support.telnyx.com/en/articles/6592456-angola-sms-guidelines
- url: https://support.telnyx.com/en/articles/6601074-cape-verde-sms-guidelines
- url: https://support.telnyx.com/en/articles/6665126-cuba-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670775-faroe-islands-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670885-greenland-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680003-sao-tome-and-principe-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683734-korea-sms-guidelines
updated_at: 2026-07-17T09:10:49Z
---

# Telnyx SMS Guidelines: Selected Destinations

Consolidated Telnyx SMS sending guidelines for France, the United Kingdom, Portugal, Spain, Denmark, Sweden, Finland, Iceland, Angola, Cape Verde, Cuba, the Faroe Islands, Greenland, Sao Tome and Principe, and the Republic of Korea, covering MCC/dial codes, Alphanumeric Sender ID support, registration and whitelisting requirements, content restrictions, and country-specific delivery rules.

## Overview

This page consolidates Telnyx SMS sending guidelines for a selection of European, African, and Asian destinations. Each country entry lists the Mobile Country Code (MCC), international dial code, Alphanumeric Sender ID support, content restrictions, and any registration or whitelisting requirements. All senders must comply with the [Acceptable Use Policy for Messaging](acceptable-use-policy-for-messaging.md).

## France

- **MCC:** 208
- **Dial Code:** 33
- Alphanumeric Sender IDs are supported and maintained; no registration is required.
- As of March 1, 2026, special characters in Alphanumeric Senders are not allowed.
- Telnyx recommends Alphanumeric Sender IDs for all A2P traffic to this destination.
- When sending to MVNO NRJ (20826) and Truphone (20812), Alphanumeric Sender IDs will be replaced by either a random local number or a [Short Code](short-code.md).
- Local operators do not allow marketing/promotional traffic on Sundays and French public holidays between 10 pm and 8 am. Messages attempted during these windows are queued and delivered afterwards.
- All marketing/promotional traffic must include a clear opt-out. The fragment `STOP au 36179` must be appended to the message; if missing, it is added automatically.
- **Anti-phishing:** French operators whitelist a group of Alphanumeric Sender IDs. Traffic using these IDs requires a duly signed Letter of Authorization (LOA).

## United Kingdom

- **MCC:** 234–235
- **Dial Code:** 44
- Alphanumeric Sender IDs are supported and maintained; no registration is required.
- A group of Alpha Sender IDs is protected under the MEF Registry against spam and fraud. Only authorized senders may use these IDs, and LOAs are required for approval.

## Portugal

- **MCC:** 268
- **Dial Code:** 351
- Alphanumeric Sender IDs are supported and maintained; no registration is required.
- No content restrictions apply to this destination.

## Spain

- **MCC:** 214
- **Dial Code:** 34
- Spain's telecoms regulator, the CNMC, is rolling out a new Alias Registry under Circular 1/2026. Starting **September 15, 2026**, any Alphanumeric Sender ID used to send messages to Spanish numbers (+34) must be registered.
- **Registration details** must be sent to [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com):
  1. **Company details** — full legal company name, NIF/CIF (Spanish tax ID) or EU-VAT number for non-Spanish companies, and registered company address.
  2. **Legal representative** — full name, NIF or passport number, mobile number, and email address.
  3. **Sender ID details** (one set per alias) — the exact alias as it appears in messages (e.g. `MYBRAND`), intended use (transactional, OTP, marketing, etc.), and planned start and end date. Registrations are valid for a maximum of 24 months.
  4. **Proof of ownership** (one per alias) — a trademark or trade name certificate from OEPM (Spain) or EUIPO (EU), a company name certificate from the Spanish Mercantile Registry, or proof of ownership of a matching `.es` or ICANN-registered domain.

## Denmark

- **MCC:** 238
- **Dial Code:** 45
- Alphanumeric Sender IDs are supported and maintained; no registration is required.
- Messages containing URLs are filtered by local operators. Valid URLs can be whitelisted to ensure delivery.
- Lottery and gambling traffic is not allowed and will be blocked.
- For URL whitelisting, contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com).

## Sweden

- **MCC:** 240
- **Dial Code:** 46
- Alphanumeric Sender IDs are supported and maintained; no registration is required.
- Messages containing URLs are filtered by local operators. Valid URLs can be whitelisted to ensure delivery.
- Lottery and gambling traffic is not allowed and will be blocked.
- For URL whitelisting, contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com).

## Finland

- **MCC:** 244
- **Dial Code:** 358
- Upcoming regulation **M28L** requires pre-registering all sender IDs used in SMS traffic in Finland starting **May 4, 2026**.
- Messages containing URLs are filtered by local operators. Valid URLs can be whitelisted to ensure delivery.
- Lottery and gambling traffic is not allowed and will be blocked.
- For URL whitelisting, contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com).

## Iceland

- **MCC:** 274
- **Dial Code:** 354
- Alphanumeric Sender IDs are supported and maintained; no registration is required.
- Messages containing URLs are filtered by local operators. Valid URLs can be whitelisted to ensure delivery.
- Lottery and gambling traffic is not allowed and will be blocked.
- For URL whitelisting, contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com).

## Angola

- **MCC:** 631
- **Dial Code:** 244
- Alphanumeric Sender IDs are supported and maintained; no registration is required.
- No content restrictions apply to this destination.

## Cape Verde

- **MCC:** 625
- **Dial Code:** 238
- Alphanumeric Sender IDs are supported and maintained; no registration is required.
- No content restrictions apply to this destination.

## Cuba

- **MCC:** 368
- **Dial Code:** 53
- Alphanumeric Sender IDs are supported **with registration**. Alpha Sender ID registration is required.
- Senders composed of a combination of letters and numbers are not supported.
- Provision times for Alphanumeric registration can take up to 6 months.
- For Alpha Sender ID registration, contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com).

## Faroe Islands

- **MCC:** 288
- **Dial Code:** 298
- Alphanumeric Sender IDs are supported and maintained; no registration is required.
- No content restrictions apply to this destination.

## Greenland

- **MCC:** 290
- **Dial Code:** 299
- Alphanumeric Sender IDs are supported and maintained; no registration is required.
- Generic Alpha Sender IDs are not recommended; Alpha Senders should be directly related to the message content.
- No content restrictions apply to this destination.

## Sao Tome and Principe

- **MCC:** 626
- **Dial Code:** 239
- Alphanumeric Sender IDs are supported and maintained; no registration is required.
- No content restrictions apply to this destination.

## Republic of Korea (South Korea)

- **MCC:** 450
- **Dial Code:** 82
- All Alphanumeric Sender IDs will be overwritten to a random Local Long Code to ensure delivery.
- All messages to this destination will have the following text added by default:
  - `[Web 발신]` — indicates A2P traffic.
  - `[국제발신]` — indicates that the message has been sent from abroad.
- Gambling and adult content are not permitted.
