---
title: Telnyx 10DLC Process
summary: A consolidated guide to registering, managing, and troubleshooting 10DLC
  brands, campaigns, and number assignments on the Telnyx platform, including fees,
  ISV requirements, sole proprietor registration, mock testing, suspension handling,
  and publicly traded brand authentication.
sources:
- url: https://support.telnyx.com/en/articles/10646301-telnyx-10dlc-process
- url: https://support.telnyx.com/en/articles/10723378-10dlc-campaign-suspended
- url: https://support.telnyx.com/en/articles/11072276-10dlc-number-assignment-status
- url: https://support.telnyx.com/en/articles/11788086-10dlc-authentication-for-publicly-traded-brands
- url: https://support.telnyx.com/en/articles/12812898-10dlc-mock-brands-and-campaigns
- url: https://support.telnyx.com/en/articles/13545282-guide-to-sole-proprietor-10dlc-brand-and-campaign-registration
- url: https://support.telnyx.com/en/articles/5593977-isvs-10dlc
- url: https://support.telnyx.com/en/articles/5634625-10dlc-fees-and-charges
- url: https://support.telnyx.com/en/articles/5896911-how-to-create-a-10dlc-brand
- url: https://support.telnyx.com/en/articles/6325734-how-to-assign-a-number-to-a-campaign
- url: https://support.telnyx.com/en/articles/6339152-how-to-create-a-10dlc-campaign
- url: https://support.telnyx.com/en/articles/8269151-assigning-did-to-a-10dlc-campaign-fails
updated_at: 2026-08-05T13:25:29Z
---

# Telnyx 10DLC Process

*Part 6 of 6 — see also: [Part 1](telnyx-10dlc-process--part-1.md), [Part 2](telnyx-10dlc-process--part-2.md), [Part 3](telnyx-10dlc-process--part-3.md), [Part 4](telnyx-10dlc-process--part-4.md), [Part 5](telnyx-10dlc-process--part-5.md)*

A consolidated guide to registering, managing, and troubleshooting 10DLC brands, campaigns, and number assignments on the Telnyx platform, including fees, ISV requirements, sole proprietor registration, mock testing, suspension handling, and publicly traded brand authentication.

## Fees and Charges

Telnyx does not currently charge a markup on 10DLC fees. All 10DLC-related fees are passed on to the customer at cost. See [10DLC Fees and Charges](10dlc-fees-and-charges.md).

### 10DLC Registration Fees

| Item | Cost |
| --- | --- |
| Brand registration application fee | $4.5 |
| Campaign Review fee | $15 per Campaign Review (manual review fee passed through from carriers). During campaign registration, your campaign may be submitted multiple times for carrier review by the Telnyx Vetting Team. If you do not want this to happen then please give advance notice at 10dlcquestions@telnyx.com. |
| Monthly cost | $1.5/mo for Low Volume Mixed – $10/month for standard volume Campaigns, $3/mo for Charity Use Cases, $5 for Emergency Use cases. Campaign fees are billed for three months initially, then subsequently on a monthly recurring basis. Do not declare a false Use Case to achieve lower charges or higher throughput. Carriers and intermediaries inspect Campaigns and traffic and charge hefty fines for non-compliance including false declarations. |

### 10DLC Carrier Fees (Registered Traffic)

| Carrier | SMS | MMS |
| --- | --- | --- |
| T-Mobile (including former Sprint network) | $0.003 to send and receive | $0.01 to send and receive |
| AT&T | $0.003 to send, Free to receive | $0.0075 to send, Free to receive |
| Verizon Wireless | $0.0031 to send, Free to receive | $0.0052 to send, Free to receive |
| US Cellular | $0.005 to send, Free to receive | $0.01 to send, Free to receive |

### 10DLC Carrier Fees (Unregistered Traffic)

Telnyx strongly recommends customers complete Brand and Campaign registration. Fees are higher for unregistered traffic, and Carriers may refuse to offer technical support in case of issues such as undelivered messages. In 2023, AT&T and T-Mobile notified customers of further increasing fees for outbound and inbound traffic for phone numbers not registered for 10DLC.

| Carrier | SMS | MMS |
| --- | --- | --- |
| T-Mobile (Traffic from numbers not registered for 10DLC) | $0.011, to send and receive (Increasing to $0.012 by December 1, 2024) | $0.020, to send and receive (Increasing to $0.021 by December 1, 2024) |
| AT&T (Traffic from numbers not registered for 10DLC) | $0.01 to send and receive | $0.015 to send and receive |

### T-Mobile Special Fees for High Volume

These fees describe special fees charged by T-Mobile for Use Cases that typically apply to very large-scale activities. Examples include very high volume traffic, or a high number count. If this applies to you, consider alternative number types such as Short Code.

| Item | Cost |
| --- | --- |
| T-Mobile Special Business Review Request | T-Mobile requires this review if you require a daily maximum volume that exceeds 200,000 messages per Brand. Cost: $5,000, one time. This fee is currently waived until further notice. |
| T-Mobile Number Pool Request | This fee applies if your Campaign or Use Case requires 50 or more phone numbers (10DLC addresses) attached to a given Brand. Cost: $50, one time. |
| T-Mobile Campaign Activation - Sole Proprietor use case | One-time fee for each Campaign registered. (NOTE: this is no longer available.) Cost: $1, one time. |

### T-Mobile 10DLC Non-Compliance Fines

T-Mobile fines customers for major compliance violations, such as using techniques to circumvent compliance and customer protection controls.

| Violation | Cost |
| --- | --- |
| Text enablement | This pass-through fine is applied if T-Mobile receives a complaint where you or your message sender text-enables a 10-digit NANP telephone number and sends messages prior to verification of message sender ownership and/or letter of authorization. Cost: $10,000 per violation. |
| Grey Route [on hold] | This pass-through fee is applied if A2P messages are sent over P2P routes. (NOTE: this fee is currently on hold.) Cost: $10 per message. This fee is currently not being charged until further notice. |
| 10DLC Long Code Program Evasion | This pass-through fine is applied if a program is found to be using techniques like snowshoeing, dynamic routing, or non-approved number replacement. Cost: $1,000 per violation. |
| Content Violation | This pass-through fee is applied for each unique instance of the third or any subsequent notification of content violating the T-Mobile Code of Conduct involving the same content provider. This content includes SHAFT-C (sex, hate, alcohol, firearms, tobacco, cannabis) violations, spam, phishing, and messaging that meets the Severity 0 violation threshold. Cost: $10,000 per violation. |
| Fraud | Attempted phishing, smishing, social engineering or similar practices that manipulate individuals to reveal credit card details, social security numbers or other private information. Cost: $2,000. |
| Illegal content especially cannabis | Any content which is not legal according to Federal or State (must be all 50 states) law. This includes Cannabis, Marijuana, Illegal Prescriptions and Solicitation. Cost: $1,000. |
| Other illegal content, including SHAFT | Other content violations, including SHAFT, that does not follow federal and state law / regulations. Cost: $500. |

### TCR Campaign Fees (as of 7/22/2025)

| Fee Code | Amount |
| --- | --- |
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

## Additional Notes

- To add email addresses to receive campaign status notifications, email 10dlcquestions@telnyx.com with your main Telnyx username email.
- For non-compliance or portal issues, contact support@telnyx.com.
- If you are unsure if a campaign was ever approved, reach out to 10dlcquestions@telnyx.com.
- For additional assistance, contact the Telnyx Support Portal or email support@telnyx.com.
