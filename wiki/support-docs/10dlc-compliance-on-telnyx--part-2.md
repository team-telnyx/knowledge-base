---
title: 10DLC Compliance on Telnyx
summary: 10DLC (10 Digit Long Code) is the mandatory US industry framework for application-to-person
  (A2P) SMS and MMS sent from standard 10-digit long code numbers. This page consolidates
  Telnyx's guidance on registration deadlines, brand and campaign setup, use cases,
  throughput, prohibited content, carrier error codes, and related compliance obligations.
sources:
- url: https://support.telnyx.com/en/articles/10509796-10dlc-registration-deadline-february-3
- url: https://support.telnyx.com/en/articles/10547022-10dlc-carrier-error-codes-explanations
- url: https://support.telnyx.com/en/articles/10684248-10dlc-use-cases
- url: https://support.telnyx.com/en/articles/11421359-10dlc-for-chiropractors
- url: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging
- url: https://support.telnyx.com/en/articles/14286763-forbidden-messaging-use-cases-in-the-us-and-canada-10dlc-toll-free-and-short-code
- url: https://support.telnyx.com/en/articles/3679260-frequently-asked-questions-about-10dlc
- url: https://support.telnyx.com/en/articles/5664840-telnyx-10dlc-compliance
- url: https://support.telnyx.com/en/articles/6228388-aca-feedback-process
- url: https://support.telnyx.com/en/articles/6325731-register-for-10dlc-messaging
- url: https://support.telnyx.com/en/articles/6417677-telnyx-10dlc-compliance-directory
updated_at: 2026-08-05T13:24:50Z
---

# 10DLC Compliance on Telnyx

*Part 2 of 3 — see also: [Part 1](10dlc-compliance-on-telnyx--part-1.md), [Part 3](10dlc-compliance-on-telnyx--part-3.md)*

10DLC (10 Digit Long Code) is the mandatory US industry framework for application-to-person (A2P) SMS and MMS sent from standard 10-digit long code numbers. This page consolidates Telnyx's guidance on registration deadlines, brand and campaign setup, use cases, throughput, prohibited content, carrier error codes, and related compliance obligations.

## Standard 10DLC Use Cases

The following standard use cases are available when registering a campaign:

- **2FA** — Authentication, verification, or one-time passcodes.
- **Account Notification** — Account-related notifications such as password resets, low-balance alerts, suspicious login attempts, or transaction alerts.
- **Customer Care** — Account management and customer support interactions.
- **Delivery Notifications** — Status updates about the delivery of a product or service.
- **Fraud Alert Messaging** — Notifications about potential fraudulent activity on a user's account.
- **Higher Education** — Messaging on behalf of colleges, universities, school districts, and education institutions. Not for the "free to the consumer" model.
- **Low Volume Mixed** — For brands with multiple use cases and very low throughput (test/demo accounts, single-location small businesses). Maximum of 5 sub-standard use cases.
- **Machine-to-Machine (M2M)** — Wireless communication between physical assets with no human interaction. Subscriber-facing campaigns are prohibited. Dedicated use case.
- **Marketing** — Any communication that includes marketing or promotional content.
- **Mixed** — Multiple use cases on one campaign. Minimum of 2 and maximum of 5 sub-use cases.
- **Polling and Voting** — Surveys and polling/voting campaigns.
- **Public Service Announcement** — Informational messaging to raise awareness about important issues.
- **Security Alert** — Notifications that the security of a system has been compromised and an action is required.

Some campaign use cases are treated differently and may require pre-approval, post-approval, or vetting by a different agent (such as Aegis or CampaignVerify for political campaigns): Agents and Franchises, Carrier Exemptions, Charity, Conversational Messaging, Emergency, Political, Social, and Sweepstake.

Federal political campaigns can be verified via [CampaignVerify](https://www.campaignverify.org/) or [Aegis](https://aegismobile.com/). Verification tokens from these providers can be imported into Telnyx.

## Prohibited and Forbidden Messaging Content

Telnyx enforces strict content rules across all messaging channels (10DLC, toll-free, and short code) in the US and Canada. Sending prohibited content can lead to carrier filtering, increased error rates, or suspension of messaging capabilities.

### Prohibited Categories

- **Illegal products and substances** — Controlled or prescription drugs without authorization, substances not legally approved for sale, unregulated or prohibited supplements.
- **Gambling and betting** — Online casinos, sports betting, betting tips, odds promotion. Some exceptions exist for approved short code programs with prior carrier approval.
- **SHAFT categories** — Sex (adult content/services), Hate (hate speech or discriminatory content), Alcohol (subject to regional and carrier rules), Firearms (weapons and related products), Tobacco (including vape and e-cigarettes). Firearms, tobacco, and vaping are not permitted on standard channels; alcohol may be allowed in the US with proper age verification.
- **Age-restricted content in Canada** — Requires explicit approval and may need additional registration or exemptions.
- **Deceptive or high-risk content** — Phishing, impersonation, misleading financial offers, "guaranteed" returns, lead generation that obscures intent, or any content designed to manipulate or deceive.
- **Restricted business models** — Businesses operating primarily in prohibited verticals, or use cases attempting to evade carrier or regulatory safeguards.

### Acceptable Use Restrictions

Telnyx's Acceptable Use Policy additionally prohibits:

- **Unsolicited messages** — Recipients must have explicitly opted in. Collecting a number for one purpose (e.g., payment validation) and then messaging it, purchasing or renting lead lists, or subscribing a transactional opt-in to a recurring campaign are not valid opt-ins. Telnyx may request proof of opt-in at any time.
- **Inappropriate content** — Sexual or pornographic, abusive or harassing, firearms (including fireworks), alcohol, tobacco, illegal drugs, high-risk financial content (loans, loan forgiveness, credit repair, debt collection, tax-related content, cryptocurrency including OTPs), gambling, investment opportunities, unsolicited real estate enquiries (e.g., WeBuyHomes), multilevel marketing, and persistent sending/receiving of OTPs on behalf of other service providers.
- **Failure to honor unsubscribe requests** — Recipients may opt out with STOP or UNSUBSCRIBE. These are delivered via webhook, and the recipient must be removed within 24 hours.
- **High-frequency messaging** — More than 10 messages to a recipient in 24 hours is prohibited unless the recipient has engaged in two-way SMS communication or has explicitly opted in to frequent messages.
- **Identity misrepresentation (spoofing)** — Sending messages that misrepresent the sender's identity.
- **Fraud or phishing** — Sending fraudulent information or phishing for confidential information.

### Additional Compliance Considerations

- **Links and URLs** — Avoid generic or public URL shorteners; use branded, recognizable domains.
- **Consent and opt-in** — All recipients must provide clear and verifiable consent, and messaging must align with registered use cases.
- **Carrier enforcement** — Carriers may act based on content classification, end-user complaints, opt-out rates, sending patterns, and traffic anomalies, even if the content is not explicitly listed.

### Best Practices

- Register campaigns where required (e.g., 10DLC).
- Clearly identify your brand in each message.
- Provide transparent opt-in and opt-out mechanisms.
- Use compliant language and avoid misleading claims.
- Send only relevant, expected communications to opted-in users.
