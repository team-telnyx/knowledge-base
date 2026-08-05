---
title: SMS Guidelines by Country
summary: Telnyx SMS guidelines for 15 countries, covering MCC, dial codes, alphanumeric
  sender ID registration requirements, content restrictions, and operator filtering
  rules.
sources:
- url: https://support.telnyx.com/en/articles/6531656-australia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6531682-philippines-sms-guidelines
- url: https://support.telnyx.com/en/articles/6531704-united-kingdom-sms-guidelines
- url: https://support.telnyx.com/en/articles/6545161-ireland-sms-guidelines
- url: https://support.telnyx.com/en/articles/6560665-denmark-sms-guidelines
- url: https://support.telnyx.com/en/articles/6560689-sweden-sms-guidelines
- url: https://support.telnyx.com/en/articles/6560706-finland-sms-guidelines
- url: https://support.telnyx.com/en/articles/6560909-iceland-sms-guidelines
- url: https://support.telnyx.com/en/articles/6561237-czech-republic-czechia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6600934-brunei-darussalam-sms-guidelines
- url: https://support.telnyx.com/en/articles/6675110-malaysia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6677919-mauritius-sms-guidelines
- url: https://support.telnyx.com/en/articles/6677954-monaco-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679378-reunion-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680103-singapore-sms-guidelines
updated_at: 2026-08-05T13:36:37Z
---

# SMS Guidelines by Country

*Part 1 of 2 — see also: [Part 2](sms-guidelines-by-country--part-2.md)*

Telnyx SMS guidelines for 15 countries, covering MCC, dial codes, alphanumeric sender ID registration requirements, content restrictions, and operator filtering rules.

## Overview

This page consolidates Telnyx SMS guidelines for the following destinations: Australia, Philippines, United Kingdom, Ireland, Denmark, Sweden, Finland, Iceland, Czech Republic (Czechia), Brunei Darussalam, Malaysia, Mauritius, Monaco, Reunion, and Singapore. Each country entry lists the Mobile Country Code (MCC), international dial code, sender ID support and registration requirements, content restrictions, and any operator-level filtering or whitelisting rules.

For general messaging compliance, always refer to the [Acceptable Use Policy for Messaging](acceptable-use-policy-for-messaging.md). For questions about alphanumeric sender ID registration or URL whitelisting, contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com).

## Australia

- **MCC:** 505
- **Dial code:** 61

The Australian Communications and Media Authority (ACMA) has introduced new requirements for alphanumeric sender IDs under the Telecommunications (SMS Sender ID Register) Industry Standard 2025, effective from 1 July 2026. Under the new framework, alphanumeric sender IDs used for messaging traffic sent to Australia must be registered with the ACMA Sender ID Register.

**What's changing:**

- All sender IDs must be registered with the ACMA Sender ID Register.
- Existing registrations under the current carrier-based system will no longer be valid.
- Messages sent using unregistered sender IDs will be transmitted with the sender ID "Unverified".

**Sender ID requirements:**

The sender ID must be clearly linked to your business and meet ACMA requirements. Acceptable sender IDs include:

- Your registered business name (or a clear abbreviation).
- A registered trademark.
- A domain name that you own.

If the sender ID does not directly match one of the above, supporting evidence must be provided demonstrating its connection to your business (such as branding usage, domain ownership, or another verifiable association). If the registration is being made on behalf of a customer, a signed Letter of Authorisation (LOA) must also be provided.

**What you need to do:**

Complete the [Australia Alpha Sender ID Registration Form](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/ltcafuzd/2495643318/be2e9882bb9dbbe4a5db251a18bb/Australia_Alpha_Sender_ID_Registration-Form.docx?expires=1783507500&signature=2f8c792dd1229a63b2017091fc13fecf357de103aee185a5176d3ee13611eb19&req=diQuE896noJeUfMW1HO4zeDBNZySywTSuoh0AFZBoLFrqz1tofyy0FqLdbp%2F%0ARVdYR8bEFxU%3D%0A) and return it to [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com) together with a copy of your business registration. Telnyx will submit the sender ID registration on your behalf via the ACMA portal; once submitted, you will be required to confirm it before it becomes effective. If you have previously registered a sender ID with Telnyx, Telnyx will contact you directly with the next steps. After 1 July 2026, messages sent using sender IDs that have not completed registration will be transmitted with the sender ID "Unverified" until the registration process has been completed.

**Additional recommendations:**

- Consent (proof of opt-in) should be obtained before sending any communications, including marketing SMS.
- Traffic should include clear opt-out options.

## Philippines

- **MCC:** 515
- **Dial code:** 63

Alphanumeric sender IDs must be pre-registered. A Letter of Authorization (LOA) must be provided for banking and financial institutions. In some instances, alpha sender IDs will be overwritten by local operators to optimize delivery despite being registered.

The use of generic alpha sender IDs (e.g. Verify, OTP, InfoSMS) for transactional traffic is not allowed; submissions with generic alpha sender IDs will be rejected by local operators. Due to high volumes of spam and phishing attempts, the use of branded URLs is highly advised instead of shortened URLs (e.g. bit.links).

## United Kingdom

- **MCC:** 234–235
- **Dial code:** 44

Alphanumeric sender IDs are supported and will be maintained; no registration is required. The MEF Registry is enforced against potential spam and fraud traffic. A group of alpha sender IDs are protected under this registry to combat fraud, so only authorized senders are allowed to send this traffic. LOAs are required for approval.

## Ireland

- **MCC:** 272
- **Dial code:** 353

Ireland's Commission for Communications Regulation (ComReg) is implementing mandatory registration for alphanumeric sender IDs.

- From 3 July 2025, all unregistered alphanumeric sender IDs will be overwritten with the sender ID "Likely Scam".
- From 3 October 2025, all unregistered alphanumeric sender IDs will be blocked, resulting in messages not reaching the intended recipients.

To register, you must first register as an alphanumeric sender ID owner (SIDO) with ComReg via the [ComReg SMS Sender ID Registry](https://www.comreg.ie/industry/electronic-communications/nuisance-communications/sms-sender-id-registry/). As part of the process, select Telnyx as your Participating Aggregator or OPA. Once registered as an SIDO, you can register your own alphanumeric sender IDs.

> **Note:** If you are an ISV or reseller, you cannot register alphanumeric sender IDs on your clients' behalf. Only the alphanumeric sender ID owner can register their respective alphanumeric sender IDs.

## Denmark

- **MCC:** 238
- **Dial code:** 45

Alphanumeric sender IDs are supported and will be maintained; no registration is required. Messages containing URLs as part of their content are filtered by local operators; valid URLs can be whitelisted to ensure delivery. Lottery and gambling-related traffic is not allowed and will be blocked by local operators.

## Sweden

- **MCC:** 240
- **Dial code:** 46

Alphanumeric sender IDs are supported and will be maintained; no registration is required. Messages containing URLs as part of their content are filtered by local operators; valid URLs can be whitelisted to ensure delivery. Lottery and gambling-related traffic is not allowed and will be blocked by local operators.

## Finland

- **MCC:** 244
- **Dial code:** 358

Upcoming regulation M28L requires pre-registering all sender IDs used in SMS traffic in Finland starting from 4 May 2026. Messages containing URLs as part of their content are filtered by local operators; valid URLs can be whitelisted to ensure delivery. Lottery and gambling-related traffic is not allowed and will be blocked by local operators.

## Iceland

- **MCC:** 274
- **Dial code:** 354

Alphanumeric sender IDs are supported and will be maintained; no registration is required. Messages containing URLs as part of their content are filtered by local operators; valid URLs can be whitelisted to ensure delivery. Lottery and gambling-related traffic is not allowed and will be blocked by local operators.

## Czech Republic (Czechia)

- **MCC:** 230
- **Dial code:** 420

Alphanumeric sender IDs are partially supported. Alphanumeric sender ID registration is possible towards T-Mobile (23001) and O2 (23002). Without registration to these networks, alphanumeric sender IDs can be overwritten to a random short code or a generic sender to ensure delivery.

## Brunei Darussalam

- **MCC:** 528
- **Dial code:** 673

Alphanumeric sender IDs are supported and will be maintained; no registration is required. There are no restrictions with regards to content towards this destination.

## Malaysia

- **MCC:** 502
- **Dial code:** 60

All alphanumeric sender IDs will be overwritten to short code to ensure delivery. Message content should start with the header "RM0.00 ,", "RM0.0 ,", or "RM0 ". If this header is not included, it will be added by local operators, which can disrupt total message content length. Additionally, content should include a brand/identifier or company name; without this identifier, operators can filter traffic or impose fines for non-compliant traffic. Any messages containing URLs as part of the message body will be blocked.
