---
title: 'SMS Guidelines: Asia-Pacific and Selected Destinations'
summary: Consolidated Telnyx SMS guidelines for Australia, Philippines, Ireland, China,
  Hong Kong, India, Macao, Malaysia, Mauritius, Mozambique, Nepal, New Caledonia,
  Singapore, Taiwan, and Trinidad & Tobago, covering MCC/dial codes, Alphanumeric
  Sender ID registration and overwrite rules, content restrictions, and links to the
  Acceptable Use Policy for Messaging.
sources:
- url: https://support.telnyx.com/en/articles/6531656-australia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6531682-philippines-sms-guidelines
- url: https://support.telnyx.com/en/articles/6545161-ireland-sms-guidelines
- url: https://support.telnyx.com/en/articles/6601144-china-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674367-hong-kong-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674383-india-sms-guidelines
- url: https://support.telnyx.com/en/articles/6675024-macao-sms-guidelines
- url: https://support.telnyx.com/en/articles/6675110-malaysia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6677919-mauritius-sms-guidelines
- url: https://support.telnyx.com/en/articles/6677999-mozambique-sms-guidelines
- url: https://support.telnyx.com/en/articles/6678903-nepal-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679031-new-caledonia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680103-singapore-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683277-taiwan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683379-trinidad-tobago-sms-guidelines
updated_at: 2026-07-17T09:11:00Z
---

# SMS Guidelines: Asia-Pacific and Selected Destinations

*Part 1 of 2 — see also: [Part 2](sms-guidelines-asia-pacific-and-selected-destinations--part-2.md)*

Consolidated Telnyx SMS guidelines for Australia, Philippines, Ireland, China, Hong Kong, India, Macao, Malaysia, Mauritius, Mozambique, Nepal, New Caledonia, Singapore, Taiwan, and Trinidad & Tobago, covering MCC/dial codes, Alphanumeric Sender ID registration and overwrite rules, content restrictions, and links to the Acceptable Use Policy for Messaging.

## Overview

This page consolidates Telnyx SMS guidelines for the following destinations: Australia, Philippines, Ireland, China, Hong Kong, India, Macao, Malaysia, Mauritius, Mozambique, Nepal, New Caledonia, Singapore, Taiwan, and Trinidad & Tobago. Each section lists the country MCC and dial code, the Alphanumeric Sender ID policy, any content or registration requirements, and links to the [Acceptable Use Policy for Messaging](acceptable-use-policy-for-messaging.md).

## Australia

- **MCC:** 505
- **Dial code:** 61

The Australian Communications and Media Authority (ACMA) has introduced new requirements for alphanumeric sender IDs under the Telecommunications (SMS Sender ID Register) Industry Standard 2025, effective from 1 July 2026. Under the new framework, alphanumeric sender IDs used for messaging traffic sent to Australia must be registered with the ACMA Sender ID Register.

**What's changing**

- All sender IDs must be registered with the ACMA Sender ID Register.
- Existing registrations under the current carrier-based system will no longer be valid.
- Messages sent using unregistered sender IDs will be transmitted with the sender ID "Unverified".

**Sender ID requirements:** Your sender ID must be clearly linked to your business and meet ACMA requirements. Acceptable sender IDs include:

- Your registered business name (or a clear abbreviation);
- A registered trademark; or
- A domain name that you own.

If your sender ID does not directly match one of the above, you must provide supporting evidence demonstrating its connection to your business, such as branding usage, domain ownership, or another verifiable association. If the registration is being made on behalf of a customer, a signed Letter of Authorisation (LOA) must also be provided confirming the authority to submit the registration.

**What you need to do:** Complete the registration form and return it to [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com), together with a copy of your business registration. Telnyx will submit the sender ID registration on your behalf via the ACMA portal. Once the registration has been submitted, you will be required to confirm it before it becomes effective. If you have previously registered a sender ID with Telnyx, Telnyx will contact you directly with the next steps. After 1 July 2026, messages sent using sender IDs that have not completed registration will be transmitted with the sender ID "Unverified" until the registration process has been completed.

**Additional recommendations:**

- Consent (Proof for Opt-in) should be obtained before sending any communications, e.g. Marketing SMS.
- Traffic should include clear Opt-Out options.

## Philippines

- **MCC:** 515
- **Dial code:** 63

Alphanumeric Sender IDs must be pre-registered. A Letter of Authorization (LOA) must be provided for Banking and Financial Institutions. In some instances, Alpha Sender IDs will be overwritten by local operators to optimize delivery despite being registered. The use of Generic Alpha Sender IDs (e.g. Verify, OTP, InfoSMS) for transactional traffic is not allowed; submissions with generic alpha Sender IDs will be rejected by local operators. Due to high volumes of spam and phishing attempts, the use of branded URLs is highly advised instead of shortened URLs (e.g. bit.links).

## Ireland

- **MCC:** 272
- **Dial code:** 353

Ireland's Commission for Communications Regulation (ComReg) is implementing mandatory registration for Alphanumeric Sender IDs. Starting from 3 July 2025, all unregistered Alphanumeric Sender IDs will be overwritten with the Sender ID "Likely Scam". From 3 October 2025, all unregistered Alphanumeric Sender IDs will be blocked, resulting in messages not reaching the intended recipients.

To register, you must first register as an Alphanumeric Sender ID owner (SIDO) with ComReg via the [ComReg SMS Sender ID Registry](https://www.comreg.ie/industry/electronic-communications/nuisance-communications/sms-sender-id-registry/). As part of the process, select Telnyx as your Participating Aggregator or OPA. Once registered as an SIDO, you can register your own Alphanumeric Sender IDs.

> **Note:** If you are an ISV or reseller, you cannot register Alphanumeric Sender IDs on your clients' behalf. Only the Alphanumeric Sender ID owner can register their respective Alphanumeric Sender IDs.

## China

- **MCC:** 460
- **Dial code:** 86

Alphanumeric Sender IDs are not supported. All Alphanumeric Sender IDs will be overwritten to either a random Local Long Code or [Short Code](https://telnyx.com/products/sms-short-code) to ensure delivery. All message content has to be whitelisted by local operators; it is highly advised to pre-register message content templates.

## Hong Kong

- **MCC:** 454
- **Dial code:** 852

Alphanumeric Sender ID registration is required. All messages from unregistered Sender IDs will be rejected.

**Information on Alphanumeric Sender ID registration:** Provide the following details along with a copy of your Business Registration to [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com):

1. Sender ID to be registered
2. Message/Content type
3. Message/Content example
4. Company name (and Brand name if different)
5. Website of brand or company
6. Company country of origin
7. Expected volumes per month
8. Email linked to your Telnyx account

Companies must have a valid business case for the requested Alphanumeric Sender ID. If the relationship between your company/brand and the requested Alphanumeric Sender ID is not clear, please provide additional supporting documentation detailing your business case.

**Additional recommendations:**

- Consent (Proof for Opt-in) should be obtained before sending any communications, e.g. Marketing SMS.
- Traffic should include clear Opt-Out options.
- It is common for handsets in Hong Kong to follow the "2 numbers 1 SIM Card" model, with one Chinese number (+86) and one HK number (+85); this can cause delivery issues.

## India

- **MCC:** 404 - 405
- **Dial code:** 91

Alphanumeric Sender IDs are partially supported through registration. Only Local Alpha Sender IDs (Local Entities) can be registered via the DLT registration process, while no registration is possible for International Alpha Sender IDs. International Alphanumeric Sender IDs will be overwritten to a random [Short Code](https://telnyx.com/products/sms-short-code) to ensure delivery.

## Macao

- **MCC:** 455
- **Dial code:** 853

Alphanumeric Sender IDs are supported; registration is not necessary. Alphanumeric Sender IDs can be overwritten to a random Hong Kong Long Code to ensure delivery towards Network China Telecom (45507). There are no restrictions with regards to content towards this destination.

## Malaysia

- **MCC:** 502
- **Dial code:** 60

All Alphanumeric Sender IDs will be overwritten to a Short Code to ensure delivery. Message content should start with the header "RM0.00 ,", "RM0.0 ,", or "RM0 ". If this header is not included, it will be added by local operators, which can disrupt total message content length. Additionally, content should include a brand/identifier or company name; without this identifier, operators can filter traffic or impose fines for non-compliant traffic. Any messages containing URLs as part of the message body will be blocked.

## Mauritius

- **MCC:** 617
- **Dial code:** 230

Alphanumeric Sender IDs are supported and will be maintained, except towards network Orange Mauritius. No registration is required. Religious, political, or adult traffic is prohibited.

## Mozambique

- **MCC:** 643
- **Dial code:** 258

Alphanumeric Sender IDs are supported. Occasionally, an Alpha Sender ID might be replaced by a Generic Alpha Sender ID towards Network Movitel (64303) to ensure delivery. There are no restrictions with regards to content towards this destination.
