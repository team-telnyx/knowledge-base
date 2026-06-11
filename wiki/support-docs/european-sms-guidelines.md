---
title: European SMS Guidelines
summary: Country-specific SMS guidelines for European destinations on the Telnyx platform,
  covering Alphanumeric Sender ID registration requirements, content restrictions,
  URL filtering, and other regulatory considerations.
sources:
- url: https://support.telnyx.com/en/articles/6531704-united-kingdom-sms-guidelines
- url: https://support.telnyx.com/en/articles/6545161-ireland-sms-guidelines
- url: https://support.telnyx.com/en/articles/6560665-denmark-sms-guidelines
- url: https://support.telnyx.com/en/articles/6560689-sweden-sms-guidelines
- url: https://support.telnyx.com/en/articles/6560704-norway-sms-guidelines
- url: https://support.telnyx.com/en/articles/6560706-finland-sms-guidelines
- url: https://support.telnyx.com/en/articles/6560909-iceland-sms-guidelines
- url: https://support.telnyx.com/en/articles/6560919-estonia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6560973-lithuania-sms-guidelines
- url: https://support.telnyx.com/en/articles/6561115-latvia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670775-faroe-islands-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670885-greenland-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674651-kosovo-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680109-slovakia-sms-guidelines
updated_at: 2026-06-11T11:18:28Z
---

# European SMS Guidelines

Country-specific SMS guidelines for European destinations on the Telnyx platform, covering Alphanumeric Sender ID registration requirements, content restrictions, URL filtering, and other regulatory considerations.

## Quick-Reference Table

| Country | MCC | Dial Code | Sender ID Registration |
|---|---|---|---|
| Denmark | 238 | 45 | Not required |
| Estonia | 248 | 372 | Not required |
| Faroe Islands | 288 | 298 | Not required |
| Finland | 244 | 358 | Required (from May 4, 2026) |
| Greenland | 290 | 299 | Not required |
| Iceland | 274 | 354 | Not required |
| Ireland | 272 | 353 | Required (phased enforcement from Jul 2025) |
| Kosovo | 221 | 383 | Not required |
| Latvia | 247 | 371 | Not required |
| Lithuania | 246 | 370 | Not required |
| Norway | 242 | 47 | Required |
| Slovakia | 231 | 421 | Not required |
| Sweden | 240 | 46 | Not required |
| United Kingdom | 234–235 | 44 | Not required (but MEF Registry applies) |

## Countries Requiring Sender ID Registration

### Ireland

Ireland's Commission for Communications Regulation (ComReg) is implementing mandatory registration for Alphanumeric Sender IDs under a phased enforcement schedule:

- **From July 3, 2025:** All unregistered Alphanumeric Sender IDs will be overwritten with the Sender ID "Likely Scam."
- **From October 3, 2025:** All unregistered Alphanumeric Sender IDs will be blocked entirely, and messages will not reach recipients.

**How to register:**

1. Register as an Alphanumeric Sender ID owner (SIDO) with ComReg via [ComReg's SMS Sender ID Registry](https://www.comreg.ie/industry/electronic-communications/nuisance-communications/sms-sender-id-registry/).
2. During registration, select **Telnyx** as your Participating Aggregator (OPA).
3. Once registered as a SIDO, register your individual Alphanumeric Sender IDs.

> **Note:** ISVs and resellers cannot register Alphanumeric Sender IDs on their clients' behalf. Only the Sender ID owner can register their respective IDs.

For more information, contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com).

### Finland

Upcoming regulation **M28L** requires pre-registering all sender IDs used in SMS traffic in Finland, effective from **May 4, 2026**.

### Norway

Alphanumeric Sender ID registration is required. All messages from unregistered Sender IDs will be rejected.

**To register, provide the following details along with a copy of your Business Registration to [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com):**

1. Sender ID to be registered
2. Message/content type
3. Message/content example
4. Company name (and brand name if different)
5. Website of brand or company
6. Company country of origin
7. Expected volumes per month
8. Email linked to your Telnyx account

Companies must have a valid business case for the requested Alphanumeric Sender ID. If the relationship between your company/brand and the requested Sender ID is not clear, provide additional supporting documentation detailing your business case.

**Additional recommendations for Norway:**

- Consent (proof of opt-in) should be obtained before sending any marketing SMS.
- Traffic should include clear opt-out options.

## Countries Without Mandatory Registration

The following countries support Alphanumeric Sender IDs without requiring registration. Sender IDs will be maintained as provided:

- Denmark
- Estonia
- Faroe Islands
- Greenland (generic Alpha Sender IDs are not recommended; senders should be directly related to message content)
- Iceland
- Kosovo
- Latvia
- Lithuania
- Slovakia
- Sweden
- United Kingdom

### United Kingdom — MEF Registry

Although registration is not generally required in the UK, the **MEF Registry** applies against potential spam and fraud traffic. A group of Alpha Sender IDs are protected under this registry to combat fraud; only authorized senders are allowed to send this traffic. Letters of Authorization (LOAs) are required for approval.

## URL Filtering

In the following countries, messages containing URLs are filtered by local operators. Valid URLs can be whitelisted to ensure delivery. Contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com) for URL whitelisting:

- Denmark
- Finland
- Iceland
- Norway
- Sweden

## Lottery and Gambling Restrictions

In the following countries, lottery and gambling related traffic is not allowed and will be blocked by local operators:

- Denmark
- Finland
- Iceland
- Norway
- Sweden

## Countries With No Content Restrictions

The following countries have no specific content restrictions beyond the general [Acceptable Use Policy for Messaging](acceptable-use-policy-for-messaging.md):

- Estonia
- Faroe Islands
- Kosovo
- Latvia
- Lithuania
- Slovakia

## General Policy

All messaging traffic must comply with the [Acceptable Use Policy for Messaging](acceptable-use-policy-for-messaging.md). For questions about Alpha Sender ID registration or URL whitelisting, contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com).
