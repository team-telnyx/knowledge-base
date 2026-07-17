---
title: 10DLC Compliance and Registration
summary: 10DLC is the mandatory US carrier framework for A2P SMS and MMS traffic sent
  from +1 long code numbers. This page consolidates Telnyx's 10DLC guidance — including
  who it applies to, how to register a Brand and Campaign, throughput and vetting
  rules, message flow templates, fees and non-compliance fines, and the February 3,
  2025 enforcement deadline after which unregistered traffic is blocked.
sources:
- url: https://support.telnyx.com/en/articles/10509796-10dlc-registration-deadline-february-3
- url: https://support.telnyx.com/en/articles/10562019-guide-to-10dlc-message-flow-field
- url: https://support.telnyx.com/en/articles/11072276-10dlc-number-assignment-status
- url: https://support.telnyx.com/en/articles/11421359-10dlc-for-chiropractors
- url: https://support.telnyx.com/en/articles/3679260-frequently-asked-questions-about-10dlc
- url: https://support.telnyx.com/en/articles/5634625-10dlc-fees-and-charges
- url: https://support.telnyx.com/en/articles/5664840-telnyx-10dlc-compliance
- url: https://support.telnyx.com/en/articles/6325731-register-for-10dlc-messaging
- url: https://support.telnyx.com/en/articles/6417677-telnyx-10dlc-compliance-directory
updated_at: 2026-07-17T09:00:19Z
---

# 10DLC Compliance and Registration

*Part 4 of 5 — see also: [Part 1](10dlc-compliance-and-registration--part-1.md), [Part 2](10dlc-compliance-and-registration--part-2.md), [Part 3](10dlc-compliance-and-registration--part-3.md), [Part 5](10dlc-compliance-and-registration--part-5.md)*

10DLC is the mandatory US carrier framework for A2P SMS and MMS traffic sent from +1 long code numbers. This page consolidates Telnyx's 10DLC guidance — including who it applies to, how to register a Brand and Campaign, throughput and vetting rules, message flow templates, fees and non-compliance fines, and the February 3, 2025 enforcement deadline after which unregistered traffic is blocked.

## 10DLC for Chiropractors

After creating and verifying your brand, chiropractors should fill in their 10DLC campaign registration as follows (replacing bracketed variables with your own info):

- **Vertical:** Healthcare
- **Use Case:** Low Volume Mixed with a Customer Care sub use case

**Campaign Description:**

Campaign to send SMS customer care messages to [Name of Practice] patients.

**CTA/Message Flow:**

When a [Name of Practice] patient calls [Front Desk Number] or walks in to the office at [Office Address], which is published at [Where Practice Address is published], the representative explains the consent process verbally:

> Office staff asks would you like to receive customer care messages via sms? If the patient says "yes" then the staff says "By providing your phone number, you agree to receive SMS customer care messages from [Name of Practice]. Message frequency may vary. Standard Message and Data Rates may apply. Reply STOP to opt out. Reply HELP for help. We will not share mobile information with third parties for promotional or marketing purposes."

Once the customer verbally agrees, the phone number is recorded, and a confirmation SMS is sent:

> "You have agreed to receive SMS customer care messages from [Name of Practice]. Msg freq may vary. Std msg & data rates apply. Reply STOP to opt out, HELP for help."

**Auto Responses:**

- **START — Opt In Auto Response:** *"You have agreed to receive SMS customer care messages from [Name of Practice]. Msg freq may vary. Std msg & data rates apply. Reply STOP to opt out, HELP for help."*
- **STOP — Opt Out Auto Response:** *[Name of Practice]: You are unsubscribed and will receive no further messages.*
- **HELP — Help Auto Response:** *[Name of Practice]: Please reach out to us at [Front Desk Phone Number] for help.*

**Sample Message:**

> Appointment Time: 2/6/2025 12:15 PM Appointment Type: Office Visit With: [Name of Practice]

**Compliance Links:** Leave blank.

**Campaign and content attributes:**

- Subscriber opt-in: Yes
- Subscriber help: Yes
- Direct lending or loan arrangement: No
- Embedded phone number: No
- Age-gated content: No
- Subscriber opt-out: Yes
- Number pooling: No
- Embedded link: No
- Affiliate marketing: No

**Webhooks:** You can leave these fields blank.

## Number Assignment Status

Assigning a number to an approved 10DLC campaign does not mean you are ready to start sending right away. The number assignment process can take anywhere from a few minutes to a few days, with a normal timeline of around 2 hours.

To check a number's assignment status:

1. Open the test endpoint at <https://developers.telnyx.com/api/messaging/10dlc/get-all-phone-number-campaigns>.
2. Enter your API key for the bearer token. The API key is located on the homepage of your Telnyx account.
3. Enter your search parameters. Easiest is to use the Telnyx or TCR Campaign ID that you assigned the number to.
4. If the status next to the number in question is `ASSIGNED`, the number is successfully assigned.
5. If it is assigned but you still have deliverability issues, check the timestamp of the undelivered message against the timestamp for the last update on the assigned number. Normally, you will see that it was all messages that were sent prior to the assignment process being complete.
6. If you still have deliverability issues, reach out to [support@telnyx.com](mailto:support@telnyx.com).

![](_images/804a9268cbc16073.png)

## Fees and Charges

Telnyx does not currently charge a markup on 10DLC fees. All 10DLC-related fees are passed on to the customer at cost.

### Registration Fees

| Item | Cost |
|------|------|
| Brand registration application fee | $4.5 |
| Campaign Review fee | $15 per Campaign Review (manual review fee passed through from carriers). During campaign registration, your campaign may be submitted multiple times for carrier review by the Telnyx Vetting Team. If you do not want this to happen, please give advance notice at [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com). |
| Monthly cost | $1.5/mo for Low Volume Mixed – $10/month for standard volume Campaigns, $3/mo for Charity Use Cases, $5 for Emergency Use Cases. Campaign fees are billed for three months initially, then subsequently on a monthly recurring basis. |

**Note:** Do not declare a false Use Case to achieve lower charges or higher throughput. Carriers and intermediaries inspect Campaigns and traffic and charge hefty fines for non-compliance including false declarations.

### Carrier Fees — Registered Traffic

| Carrier | SMS | MMS |
|---------|-----|-----|
| T-Mobile (including former Sprint network) | $0.003 to send and receive | $0.01 to send and receive |
| AT&T | $0.003 to send, free to receive | $0.0075 to send, free to receive |
| Verizon Wireless | $0.0031 to send, free to receive | $0.0052 to send, free to receive |
| US Cellular | $0.005 to send, free to receive | $0.01 to send, free to receive |

### Carrier Fees — Unregistered Traffic

Telnyx strongly recommends customers complete Brand and Campaign registration. Fees are higher for unregistered traffic, and Carriers may refuse to offer technical support in case of issues such as undelivered messages.

| Carrier | SMS | MMS |
|---------|-----|-----|
| T-Mobile (Traffic from numbers not registered for 10DLC) | $0.011 to send and receive (increasing to $0.012 by December 1, 2024) | $0.020 to send and receive (increasing to $0.021 by December 1, 2024) |
| AT&T (Traffic from numbers not registered for 10DLC) | $0.01 to send and receive | $0.015 to send and receive |

### T-Mobile Special Fees for High Volume

| Item | Details |
|------|---------|
| T-Mobile Special Business Review Request | Required if you require a daily maximum volume that exceeds 200,000 messages per Brand. **Cost:** $5,000, one time. *This fee is currently waived until further notice.* |
| T-Mobile Number Pool Request | Applies if your Campaign or Use Case requires 50 or more phone numbers attached to a given Brand. **Cost:** $50, one time. |
| T-Mobile Campaign Activation — Sole Proprietor use case | One-time fee for each Campaign registered. *(NOTE: this is no longer available.)* **Cost:** $1, one time. |

### T-Mobile 10DLC Non-Compliance Fines

| Violation | Cost |
|-----------|------|
| Text enablement | $10,000 per violation |
| Grey Route [on hold] | $10 per message (currently not being charged until further notice) |
| 10DLC Long Code Program Evasion | $1,000 per violation |
| Content Violation | $10,000 per violation |
| Fraud | $2,000 |
| Illegal content especially cannabis | $1,000 |
| Other illegal content, including SHAFT | $500 |

### TCR Campaign Fees (as of 7/22/2025)

| Fee Code | Amount |
|----------|--------|
| 10DLC-CAMPAIGN-FEE-AGENTS-AND-FRANCHISES-MRC | 30 |
| 10DLC-CAMPAIGN-FEE-CHARITY-MRC | 3 |
| 10DLC-CAMPAIGN-FEE-EMERGENCY-MRC | 5 |
| 10DLC-CAMPAIGN-FEE-LOW-VOLUME-MIXED-MRC | 1.5 |
| 10DLC-CAMPAIGN-FEE-PLATFORM-FREE-TRIAL-MRC | 0 |
| 10DLC-CAMPAIGN-FEE-SOLE-PROPRIETOR-MRC | 2 |
| 10DLC-CAMPAIGN-FEE-2FA-MRC | 10 |
| 10DLC-CAMPAIGN-FEE-ACCOUNT-NOTIFICATIONS-MRC | 10 |
| 10DLC-CAMPAIGN-FEE-CARRIER-EXEMPTIONS-MRC | 10 |
| 10DLC-CAMPAIGN-FEE-CUSTOMER-CARE-MRC | 10 |
| 10DLC-CAMPAIGN-FEE-DELIVERY-NOTIFICATIONS-MRC | 10 |
| 10DLC-CAMPAIGN-FEE-FRAUD-ALERT-MESSAGING-MRC | 10 |
| 10DLC-CAMPAIGN-FEE-HIGHER-EDUCATION-MRC | 10 |
| 10DLC-CAMPAIGN-FEE-K-12-EDUCATION-MRC | 10 |
| 10DLC-CAMPAIGN-FEE-MARKETING-MRC | 10 |
| 10DLC-CAMPAIGN-FEE-MIXED-MRC | 10 |
| 10DLC-CAMPAIGN-FEE-POLITICAL-MRC | 10 |
| 10DLC-CAMPAIGN-FEE-POLLING-AND-VOTING-MRC | 10 |
| 10DLC-CAMPAIGN-FEE-PROXY-MRC | 10 |
| 10DLC-CAMPAIGN-FEE-PUBLIC-SERVICE-ANNOUNCEMENTS-MRC | 10 |
| 10DLC-CAMPAIGN-FEE-REGULAR-MRC | 10 |
| 10DLC-CAMPAIGN-FEE-SECURITY-ALERT-MRC | 10 |
| 10DLC-CAMPAIGN-FEE-SOCIAL-MRC | 10 |
| 10DLC-CAMPAIGN-FEE-SWEEPSTAKES-MRC | 10 |
