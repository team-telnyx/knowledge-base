---
source_url: https://support.telnyx.com/en/articles/6325747-10dlc-trust-scores-use-cases
scraped: 2026-06-11
---

10DLC: Trust Scores & Use Cases | Telnyx Help Center

[Skip to main content](#main-content)

# 10DLC: Trust Scores & Use Cases

Master the intricacies of 10DLC messaging. Trust scores, campaign use cases: ensure optimal SMS throughput and brand reputation with Telnyx.

Written by Telnyx Sales

June 6, 2024

Table of contents

# 10DLC Messaging throughput, Trust Scores, Campaign Use Cases and Vetting

In the US, [A2P](https://telnyx.com/resources/what-is-a2p-messaging) 10DLC message sending throughput is set based on your Trust Score and your Use Case (“Campaign”) type. In this article you will find a guide of what these are, how they are allocated, and the third parties involved in the process.

## **What is Throughput?**

Message sending throughput for SMS is measured in message segments per second (MPS). [Each message segment consists of up to 160 GSM-7 encoded characters, so an SMS with more characters and/or different character encoding can be comprised of multiple segments.](https://support.telnyx.com/en/articles/3679260-frequently-asked-questions-about-10dlc#h_8f1ead6b93)

On top of throughput per second limitations, T-Mobile imposes separate daily message limits toward their subscribers which cannot be exceeded without a special business review. You can read more about these limits [here>>](https://support.telnyx.com/en/articles/5634625-10dlc-fees-and-charges)

## **What are Trust Scores?**

Trust Scores are assigned when a Brand is registered via a reputation algorithm. The score does NOT change over time, so having a good Trust Score is important. While the exact algorithm has not been released, it is believed that it is primarily determined by brand footprint (larger brands = higher trust) and quality / consistency of your Brand’s registration request (less discrepancies = better score).

## **Campaign Use Cases and important note about Political Campaigns**

Specific Campaign Use Cases also determine MPS. Typically use cases range from marketing types to operational ones (such as notifications). You can select Mixed use campaigns (in order to reuse the same phone number), however it's worth noting that fees tend to be higher for Mixed campaigns than those with specific use cases. Crucially, political campaigns must also be verified at campaignverify.com, who will supply you with a token upon successful verification. Following this, you can set up a new token.

To confirm if your campaign use case is acceptable for your brand, you can use the Qualify By Use Case Endpoint, detailed [here>>](https://developers.telnyx.com/api/messaging/10dlc/get-campaigns)

## **Requesting third-party vetting**

Any brand registration request submitted to Telnyx is sent to the TCR for review, who gives a score based on a reputation algorithm. This is assigned by The Campaign Registry (TCR), the 3rd party administrator of the carriers’ new registration system.

To request brand vetting, use the Brand API, which is documented [here>>](https://developers.telnyx.com/api/messaging/10dlc/create-brand-post).

---

Related Articles

[Frequently asked questions about 10DLC](https://support.telnyx.com/en/articles/3679260-frequently-asked-questions-about-10dlc)[10DLC Fees and Charges](https://support.telnyx.com/en/articles/5634625-10dlc-fees-and-charges)[Telnyx & 10DLC Compliance](https://support.telnyx.com/en/articles/5664840-telnyx-10dlc-compliance)[How to create a 10DLC campaign](https://support.telnyx.com/en/articles/6339152-how-to-create-a-10dlc-campaign)[Telnyx 10DLC Compliance Directory](https://support.telnyx.com/en/articles/6417677-telnyx-10dlc-compliance-directory)

Did this answer your question?

😞😐😃

Table of contents
