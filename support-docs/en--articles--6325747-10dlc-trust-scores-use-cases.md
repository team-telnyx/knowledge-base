---
source_url: https://support.telnyx.com/en/articles/6325747-10dlc-trust-scores-use-cases
title: "10DLC: Trust Scores & Use Cases"
description: "Master the intricacies of 10DLC messaging. See Telnyx guidance and requirements Learn more about 10DLC: Trust Scores & Use Cases with Telnyx."
scraped: 2026-07-08
content_hash: d6bd1ec81d473ca63ef7c249bc414517b46feea43b2132519727076e3bfa6773
---

# 10DLC: Trust Scores & Use Cases

Master the intricacies of 10DLC messaging. See Telnyx guidance and requirements Learn more about 10DLC: Trust Scores & Use Cases with Telnyx.

## 10DLC Messaging Throughput, Trust Scores, Campaign Use Cases and Vetting

In the US, [A2P](https://telnyx.com/resources/what-is-a2p-messaging) 10DLC message sending throughput is set based on your Trust Score and your Use Case ("Campaign") type. In this article you will find a guide to what these are, how they are allocated, and the third parties involved in the process.

---

## **What is Throughput?**

Throughput refers to the rate at which messages can be sent, measured in messages per second (MPS). Each carrier sets its own throughput limits based on your brand trust score and campaign use case.

On top of throughput per second limitations, T-Mobile imposes separate daily message limits toward their subscribers which cannot be exceeded without a special business review. You can read more about these limits in [10DLC Fees and Charges](https://support.telnyx.com/en/articles/5634625-10dlc-fees-and-charges).

---

## **Brand Tiers and Trust Scores**

10DLC brands are categorized into different tiers, each with different throughput characteristics:

|  |  |  |
| --- | --- | --- |
| Brand Tier | Description | Vetting |
| Standard | For businesses with an EIN. Most common brand type. | Optional third-party vetting available |
| Low Volume Standard | For businesses with an EIN but lower message volume needs. | Optional third-party vetting available |
| Sole Proprietor | For individuals/small businesses without an EIN. Limited use cases. | No third-party vetting available |

Trust Scores are assigned when a Brand is registered via a reputation algorithm run by The Campaign Registry (TCR). The score is primarily determined by:

* **Brand footprint** — Larger, more established brands tend to receive higher trust scores
* **Registration quality** — Accuracy and consistency of your brand information with government database information
* **Entity type** — Public companies and large enterprises typically score higher

Third-party vetting can improve your trust score, which in turn can increase your throughput limits with carriers.

---

## **Campaign Use Cases**

Your campaign use case determines your monthly recurring cost and affects your throughput. Here are the main use cases:

|  |  |  |
| --- | --- | --- |
| Use Case | Monthly Fee | Notes |
| 2FA / OTP | $10 | One-time passwords/Verification Codes |
| Account Notifications | $10 | Account-related messaging |
| Customer Care | $10 | Conversational messaging |
| Delivery Notifications | $10 | Shipping/delivery messaging |
| Marketing | $10 | Promotional content |
| Mixed | $10 | Multiple use cases on one campaign |
| Political | $10 | Requires CampaignVerify token |
| Fraud Alert Messaging | $10 | Account fraud notifications |
| Higher Education | $10 | College and University notifications for students |
| Polling and voting | $10 | Surveys and Polling |
| Public Service Announcement | $10 | Only for government usage |
| Security Alert | $10 | Notifications of systems security |
| K-12 Education | $10 | School notifications for students/parents |
| Emergency Alerts | $5 | Emergency messaging for government agencies and first responders only |
| Charity | $3 | Non-profit/donation solicitation messaging |
| Sole Proprietor | $2 | Limited use cases |
| Low Volume Mixed | $1.50 | Lower volume, mixed use. Can be used for testing and demo campaigns |

**Political Campaigns:** Political campaigns must be verified at [CampaignVerify.com](https://www.campaignverify.org/), who will supply you with a token upon successful verification.

To confirm if your campaign use case is acceptable for your brand, you can use the Qualify By Use Case endpoint, detailed [here>>](https://developers.telnyx.com/api/messaging/10dlc/get-campaigns)

---

## **Carrier-Specific Throughput**

Throughput varies by carrier. Below is a basic and general guide — actual throughput depends on your brand tier, trust score, and whether your brand has been vetted:

**AT&T:**

* Standard vetted brands: Higher MPS
* Unvetted brands: Lower MPS
* Throughput scales with trust score

**T-Mobile:**

* Throughput based on brand tier and use case
* Daily message limits apply (separate from per-second limits)
* Higher limits for vetted brands

**Verizon:**

* Throughput based on use case
* Less dependent on trust score than AT&T/T-Mobile

**UScellular:**

* Throughput based on use case and brand tier

For the most current throughput numbers, contact your Telnyx account manager or refer to the TCR portal.

---

## **Requesting Third-Party Vetting**

Third-party vetting can improve your brand trust score, leading to higher throughput from carriers.

Approved vetting partners:

|  |  |  |
| --- | --- | --- |
| Partner | Specialty | Notes |
| Aegis Mobile | General brand vetting | Commercial brand reputation vetting |
| WMC Global | General brand vetting | Commercial brand reputation vetting |
| CampaignVerify | Political campaigns | Required for political use cases only |

To request brand vetting, use the Brand API, which is documented [here>>](https://developers.telnyx.com/api/messaging/10dlc/create-brand-post). The vetting fee is $15 per submission.

---

Related Articles

[Frequently asked questions about 10DLC](https://support.telnyx.com/en/articles/3679260-frequently-asked-questions-about-10dlc)[10DLC Fees and Charges](https://support.telnyx.com/en/articles/5634625-10dlc-fees-and-charges)[Telnyx & 10DLC Compliance](https://support.telnyx.com/en/articles/5664840-telnyx-10dlc-compliance)[How to create a 10DLC campaign](https://support.telnyx.com/en/articles/6339152-how-to-create-a-10dlc-campaign)[Telnyx 10DLC Compliance Directory](https://support.telnyx.com/en/articles/6417677-telnyx-10dlc-compliance-directory)

Did this answer your question?

😞😐😃
