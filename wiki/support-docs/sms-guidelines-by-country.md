---
title: SMS Guidelines by Country
summary: Country-specific SMS guidelines including MCC, dial codes, alphanumeric sender
  ID policies, registration requirements, and regulatory considerations for sending
  messages through Telnyx.
sources:
- url: https://support.telnyx.com/en/articles/6531656-australia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6531664-mexico-sms-guidelines
- url: https://support.telnyx.com/en/articles/6531712-brazil-sms-guidelines
- url: https://support.telnyx.com/en/articles/6564188-argentina-sms-guidelines
- url: https://support.telnyx.com/en/articles/6564226-costa-rica-sms-guidelines
- url: https://support.telnyx.com/en/articles/6564249-bolivia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6665730-dominican-republic-sms-guidelines
updated_at: 2026-06-11T11:19:10Z
---

# SMS Guidelines by Country

Country-specific SMS guidelines including MCC, dial codes, alphanumeric sender ID policies, registration requirements, and regulatory considerations for sending messages through Telnyx.

## Country Reference

| Country | MCC | Dial Code |
|---|---|---|
| Argentina | 722 | 53 |
| Australia | 505 | 61 |
| Bolivia | 736 | 591 |
| Brazil | 724 | 55 |
| Costa Rica | 712 | 506 |
| Dominican Republic | 370 | 1809 |
| Mexico | 334 | 52 |

## Alphanumeric Sender ID Policies

Alphanumeric sender ID handling varies significantly by destination. Policies fall into the following categories:

### Supported with Mandatory Registration

**Australia** requires mandatory registration of alphanumeric sender IDs with the Australia Communications and Media Authority (ACMA). Effective May 8, 2023, all messages sent with non-registered alphanumeric sender IDs are blocked. See the [Australia: Regulatory Requirements](#australia-regulatory-requirements) section below for full details.

### Supported without Registration (May Be Overwritten)

**Dominican Republic** supports alphanumeric sender IDs and no registration is required. However, alphanumeric sender IDs may occasionally be overwritten to a random short code to ensure delivery.

### Overwritten to Local Long Code or Short Code

In the following countries, alphanumeric sender IDs are not preserved on delivery. They will be overwritten to either a random local long code or short code:

- Argentina
- Brazil (registration is not possible)
- Costa Rica
- Mexico

### Not Supported

**Bolivia** does not support alphanumeric sender IDs. Registration is not possible, and all alphanumeric sender IDs are overwritten to a random local long code or short code.

## Australia: Regulatory Requirements

Australia has the most stringent regulatory requirements among the countries covered here. All commercial traffic must comply with the [Australian Spam Act 2003](https://www.acma.gov.au/avoid-sending-spam).

### Upcoming ACMA Regulation Changes

New SMS regulations were announced by ACMA on 9 October 2025, with an expected effective date of 1 July 2026. Telnyx will register sender IDs via the ACMA portal, and customers will be required to confirm the registration. If you have previously registered a sender ID with Telnyx, Telnyx will reach out directly with next steps.

### Alphanumeric Sender ID Registration Process

To register an alphanumeric sender ID for Australia:

1. Complete the Australia Alpha Sender ID Registration Form and return it to [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com), along with a copy of your Business Registration.
2. Companies must have a valid business case for the requested alphanumeric sender ID. If the relationship between your company/brand and the requested sender ID is not clear, provide additional supporting documentation detailing your business case.
3. If the registration is being made on behalf of a customer, a signed Letter of Authorisation (LOA) must be provided to confirm the legitimacy of the request.

For more information on alphanumeric sender ID registration, contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com).

### Additional Recommendations for Australia

- Obtain consent (proof of opt-in) before sending any communications, including marketing SMS.
- Traffic should include clear opt-out options.

## Delivery Receipts

**Brazil** supports SMSC-DLR only. Positive delivery receipts (DLRs) are to be expected, but handset delivery reports are not possible.

## General Compliance

Regardless of destination, all messaging traffic must comply with the [Acceptable Use Policy for Messaging](acceptable-use-policy-for-messaging.md). Always review the policy before sending messages to any country.
