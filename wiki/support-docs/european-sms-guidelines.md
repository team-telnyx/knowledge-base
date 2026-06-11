---
title: European SMS Guidelines
summary: Country-specific SMS guidelines for European destinations on the Telnyx platform,
  covering Alphanumeric Sender ID registration requirements, content restrictions,
  URL filtering, and other regulatory considerations.
sources:
- url: https://support.telnyx.com/en/articles/6531704-united-kingdom-sms-guidelines
  content_hash: a996136827a304a171c2072c61ed424bf0d98acc2dcc793f229a37fab4d6655b
- url: https://support.telnyx.com/en/articles/6545161-ireland-sms-guidelines
  content_hash: 8a430509e2eafe42c49d6ede0739a849fde6fea76965b55fdc48135ae8b092b8
- url: https://support.telnyx.com/en/articles/6560665-denmark-sms-guidelines
  content_hash: 48cdbf4def4bebcb092bdfeb72356e6b6ce289ed8fd6a823015965f9562efcdf
- url: https://support.telnyx.com/en/articles/6560689-sweden-sms-guidelines
  content_hash: 554e108df44973a2ebdcf7a0765127724298a604ec11c5042c2a4ffc61e0c9cf
- url: https://support.telnyx.com/en/articles/6560704-norway-sms-guidelines
  content_hash: 68deba9fb8d00eaf27beb086323853aac7ad3cbb6c07d0ae3395276184111826
- url: https://support.telnyx.com/en/articles/6560706-finland-sms-guidelines
  content_hash: c04931a0f135129f242aae730fa4bb4e517f8066aef69ea6563c7dc213c691c7
- url: https://support.telnyx.com/en/articles/6560909-iceland-sms-guidelines
  content_hash: cb2c9051df3ca8988b42358502e644f1f54feb408db50aebcfa1a7332a9f8c75
- url: https://support.telnyx.com/en/articles/6560919-estonia-sms-guidelines
  content_hash: 213539a46a382e0ff46cc6b6780e7737acfbd33c62988b8c9abdc7155316f27c
- url: https://support.telnyx.com/en/articles/6560973-lithuania-sms-guidelines
  content_hash: 9bbb78fa6698b9a67d2f6ab895caf45dc38f93687078a48826f565921c3954e1
- url: https://support.telnyx.com/en/articles/6561115-latvia-sms-guidelines
  content_hash: c64d770583340859f5fbf027b4c37503a41081ca4add30e8b07baed1d5092751
- url: https://support.telnyx.com/en/articles/6670775-faroe-islands-sms-guidelines
  content_hash: 80bc4f7ae4193cb20fb9713a5a1549c4f0c7be13d9856fa21182b74067b0ea3f
- url: https://support.telnyx.com/en/articles/6670885-greenland-sms-guidelines
  content_hash: 06997ecbdd4190d40ba324a2c67fa6c92a163bd353ce95f21b39fc0c23336a6f
- url: https://support.telnyx.com/en/articles/6674651-kosovo-sms-guidelines
  content_hash: c84ccd1e51cf09c643eb1cc92365b27e80000ab0f3e5fce9021b5a3251ce2794
- url: https://support.telnyx.com/en/articles/6680109-slovakia-sms-guidelines
  content_hash: cadc91aefedee604d6688509ef691867cc2d869fd385a94e525f8dd209b45bf9
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
