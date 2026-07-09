---
source_url: https://support.telnyx.com/en/articles/3679260-frequently-asked-questions-about-10dlc
scraped: 2026-07-08
content_hash: 1137a07baf13fe64132a3219624937bbbc57bba59e3b758b65c2af66d4e002f7
---

Frequently asked questions about 10DLC | Telnyx Help Center

[Skip to main content](#main-content)

# Frequently asked questions about 10DLC

10DLC is the mandatory compliance framework for USA long-code SMS & MMS traffic

Written by Telnyx Engineering

January 23, 2025

Table of contents

***⚠️ Looking for 10DLC costs / fees? Check out [10DLC Fees and Charges](https://support.telnyx.com/en/articles/5634625-10dlc-fees-and-charges)***

---

# **10 Digit Long Code (10DLC) Introduction & Contents**

***UPDATE: From February 3rd 2025, any 10DLC traffic which is not registered will be blocked altogether.***

10DLC helps protect customers from unwanted spam while allowing businesses to better connect with their customers. Introduced in 2021, **10DLC has become virtually mandatory** for businesses **sending local text messaging traffic via US (+1) long code numbers** in the United States.

**Telnyx highly recommends customers complete 10DLC registration checks** by setting up a **Brand** and **Campaign** to avoid significant extra charges and even fines from Carriers.

**Contents**

* [What is 10DLC and Why It Exists](#h_4d065f245c)
* [Who 10DLC Applies To](#h_71a789b881)
* [How to Register for 10DLC](#h_7900185bc6)
* [Relationship Between Brands, Numbers and Campaigns](#h_2b21b8a24f)
* [Brand Score, Tier & Vetting Score](#h_d41e133838) [including *why Vetting is strongly recommended*]
* [Throughput - What It Is and How Carriers Determine It](#h_133c9a87d6)
* [Messaging Throughput Estimate Tables](#h_1168826227)
* [10DLC Definitions / Acronyms](#h_b610fc2119)
* [Fees, Charges & Other Questions](#h_7411bcf43c)

---

## *What 10DLC is and Why It Exists*

---

### **What is 10 DLC?**

10DLC allows businesses to send application-to-person text messages (A2P) using long local codes in the United States.

### **Why was 10DLC introduced?**

Carriers introduced 10DLC to provide a sanctioned platform for businesses to send SMS and MMS messages using long codes. Their objective is to protect consumers from unwanted spam while still allowing businesses to better connect with their customers. This change will also improve deliverability because 10DLC allows for higher messaging throughput than P2P long code traffic.

### **Does 10DLC allow handset receipts?**

No. We recommend exploring short code or toll-free messaging if handset receipts are required.

### **Does 10DLC allow Free To End User programs?**

No, this program is not currently available, and there are no known plans to change this.

---

## *Who 10DLC Applies To*

---

### **How do I know if 10DLC applies to me?**

Generally, all traffic sent by - or on behalf of - businesses from +1 long code numbers (not Toll Free or Short Code) is governed under 10DLC. Specifically, 10DLC applies to the below types of businesses:

1. Currently sending A2P (Application to Person) traffic over long codes. Generally, all traffic sent by - or on behalf of - businesses is considered A2P.
2. A reseller or independent service vendor (ISV) with customers sending A2P traffic over long codes. If you're an ISV, find more information on how 10DLC applies to you in [this support article](https://support.telnyx.com/en/articles/5593977-isvs-10dlc).

### **What do I need to do to comply with 10DLC?**

You must:

* Register a Brand
* (optional but recommended) Vet the Brand
* Register a campaign
* Assign numbers to the campaign
* Await results of manual review
* Send traffic under those campaign numbers according to 10DLC guidelines and your specific declared Use Case(s).

Failure to do the above can result in throttled traffic, higher fees, and even fines.

### **Does 10DLC affect (person-to-person) P2P traffic?**

According to guidelines as of 2023, virtually all SMS and MMS sent by a business—even if manually triggered by a human—is considered A2P. Therefore, while 10DLC isn’t strictly required for P2P traffic, Telnyx has observed that most “P2P” Use Cases are often, in fact, A2P and should be registered.

You may qualify for P2P registration ONLY if the following conditions are true:

* The messages are not sent on behalf of any business or agent of a business
* You are not a cloud communication service suite
* All messages are written and sent by individuals to other individuals
* Traffic is roughly symmetrical (1:1 or 1:3 max) and, therefore, resembles normal human-to-human communication
* Your business has an excellent compliance history.

  + Note: Telnyx determines this history by reviewing your traffic history with us. Therefore, this process is typically only offered to long-term committed customers.

If you believe your business meets all the above conditions and qualifies for P2P Carrier Approval, please contact support to request a Carrier P2P Use Case Questionnaire.

### **Will toll-free numbers (TFNs) be affected by 10DLC?**

No. Toll-free numbers require registration but are not explicitly covered under 10DLC guidelines. We recommend referring to our [Toll-Free Messaging FAQs](https://support.telnyx.com/en/articles/5353868-toll-free-messaging) for more details.

---

## *How to register for 10DLC*

---

### **What are the basic requirements for 10DLC registration?**

10DLC requires businesses to register a Brand (business) and Campaigns (Use Cases) to increase transparency regarding who is sending what. You can submit requests to [register your Brand(s) and Campaign(s)](https://telnyx.com/release-notes/10DLC-mcp) via:

* Our [Mission Control Portal](https://portal.telnyx.com/).
* Our [10DLC API endpoints](https://developers.telnyx.com/docs/messaging/10dlc).

### **Can I create more than one brand?**

You can only create one Brand per EIN (Employer Identification Number or Federal Tax Identification Number). Additional Brands require their own unique EIN.

### **Can non-US brands be added while using the portal?**

Yes. Please note all 10DLC rules (and possible penalties) still apply to non-US entities.

### **What happens after I submit my Brand and Campaign for approval?**

Brand and Campaign information submitted via Telnyx is passed on for manual review by The Campaign Registry (TCR), the third party that administers carriers' 10DLC registration system.

In addition, Campaigns (but not Brands) are manually reviewed by Carriers. This review is an industry-wide mandatory step for all A2P 10DLC registrations.

### **Are any Campaigns treated differently?**

Yes, the following Campaign Use Cases are treated differently:

1. Agents and Franchises
2. Carrier Exemptions
3. Charity
4. Conversational Messaging
5. Emergency
6. Political
7. Social
8. Sweepstake

These types of campaigns often require pre-approval, post-approval, and/or vetting. In some cases, they require a different vetting agent (such as Aegis or Campaign Registry for political campaigns).

This information will be displayed when transitioning from the “Use Case Selection” page.

### **If my campaign falls under a political Use Case, how can I be vetted for it?**

Federal political campaigns can be verified via [Campaign Verify](https://www.campaignverify.org/) or [Aegis](https://aegismobile.com/). If you did not register via Telnyx, you can also import the verification token they provided you with after completing their verification process.

### **What is the purpose of a Mixed Campaign Use Case?**

A phone number can be assigned to one Campaign at most. However, a Campaign can have many assigned phone numbers.

Many businesses that want to use just one phone number register with a Mixed Use Case, which allows up to five Sub-Use Cases. A common example might be registering for a Marketing and Notifications Mixed Use Case.

### **How do I minimise downtime if I want to port numbers to Telnyx and use 10DLC?**

Before you port your numbers to Telnyx, you'll want to make sure to create the 10DLC campaigns in your Telnyx Portal account and wait until they are in an approved state. After this, you can start the porting process but before the numbers fully port, please ensure you work with your old carrier to have the 10DLC campaigns removed from their system. Otherwise, you will not be able to assign the newly ported numbers to your 10DLC campaigns as they will still be tied with the losing carrier.

---

## *Relationship between Brands, Numbers, and Campaigns*

---

### **How many Brands per organization?**

An EIN (Employer Identification Number) can only have one Brand assigned to it.

### **How many Campaigns per Brand?**

A Brand can have multiple Campaigns, with a maximum of five Campaigns per Brand.

### **How many Numbers per Campaign?**

A Campaign can have multiple Numbers. As of September 2023, the T-Mobile Limit is 49 numbers.

### **I have less than 49 numbers on my Campaign but was unable to add more. Why?**

You may have encountered the industry’s daily number-adding limit. 10DLC intermediaries cap the amount of numbers that can be added to a given Campaign due to downstream processing constraints. We advise you to try again in one business day.

### **How many Campaigns or Brands per Number?**

A Number can only be used in one Campaign and its parent Brand.

---

## *Brand Score, Brand Tier, and Vetting Score*

---

### **What is the difference between a Brand Score and a Brand Tier?**

As of mid-2023, Brand Score has been deprecated in favor of Brand Tier, which is determined by Vetting Score.

Brand Tier is used by Carriers - especially T-Mobile & AT&T to help calculate your throughput.

### **What is Throughput and how is it calculated?**

Refer to the [below section.](#h_18938720b5)

### **What is a Vetting Score, and why is it strongly recommended?**

As of mid-2023, a Brand without a Vetting Score will tend to lead to low throughput for complex Campaign Use Cases like Marketing. Therefore, Telnyx highly recommends Vetting Scores for any Campaigns with material traffic or similarly complex compliance requirements.

### **How do I get a Vetting Score?**

You can order Brand Vetting by:

1. Editing a Verified Brand in the Portal and

   1. Completing a Brand
   2. Entering your Vetting ID or Vetting token from a completed External Vetting
2. Using the [Vetting Endpoints](https://developers.telnyx.com/api/messaging/10dlc/create-brand-post) in the 10DLC API to complete the above.

---

## *Throughput - What it is and How Carriers Determine It*

---

## **What is messaging throughput?**

Throughput is the maximum number of messages you can send in a given period - either segments per second (MPS), per minute (MPM) or per day.

T-Mobile determines throughput as a daily messaging limit at the Brand level, meaning that all your Campaigns combined must share the daily limit.

A message segment consists of up to 160 standard characters. An SMS with more characters and/or nonstandard characters (such as emojis) can count as multiple message segments. We support up to 10 segments before messages will be rejected for being too long.

1. **Standard SMS Limit**: A standard SMS using GSM-7 encoding can contain up to 160 characters. This is the maximum size that can fit within the 140-byte (1120 bits) payload of a standard SMS.
2. **Segmentation for Longer Messages**: When an SMS exceeds 160 characters, it needs to be split into multiple segments. Each of these segments is sent as a separate SMS and then reassembled into a single message on the recipient's device.
3. **User Data Header (UDH)**: To facilitate this reassembly, each segment of a multi-part SMS must contain a header, known as the User Data Header. The UDH includes information such as the total number of segments and the position of each segment within the original message. This is necessary so the receiving device knows how to piece the message back together in the correct order.
4. **UDH Size and Its Impact**: The UDH typically takes up 7 bytes (56 bits) of the standard 140-byte SMS payload. This reduces the available space for the actual text of the message.
5. **Reduced Character Count per Segment**: When the 7-byte UDH is accounted for, the remaining space in each SMS segment is reduced. For GSM-7 encoded messages, this leaves room for 153 characters per segment (instead of the full 160).

So, in a multi-part message, each segment can only contain 153 characters due to the space required for the UDH. This is why, in practice, when you send a long SMS that needs to be segmented, each segment has a slightly reduced character limit.

### **How is my MPS (message segments per second) determined?**

Each of your registered Campaigns will be assigned a maximum MPS based on your Brand Tier (derived from your Vetting Score) and the type of Campaign. This MPS limit is shared across all numbers attached to your Campaign and all wireless Carriers.

The same MPS limit applies whether you send all traffic through one number or split it up across multiple numbers.

Campaign Use Cases fall into four categories:

* **Declared:** Specific Use Cases. Ex., two-factor authentication (2FA)
* **Mixed:** A combination of multiple Use Cases
* **Marketing:** Marketing-related content
* **Special:** Charity, emergency, political, and other.

Declared Use Case Campaigns may receive a higher MPS than a Mixed or Marketing Campaign with the same Brand Score. However, **it is important to correctly classify your Use Case.** Incorrectly classified use cases can result in Deactivated Campaigns and hefty fines from industry organizations.

Notably, there are undeclared industry limits for MMS. As of April 2023, we estimated these to be:

|  |  |  |
| --- | --- | --- |
|  | AT & T / T-Mobile | Verizon |
| MMS Per Second Max | 0.84 | 25 |
| MMS Per Minute Max | 50 (per number) |  |

### **How do I register my MMS for 10DLC?**

10DLC Campaigns include both SMS and MMS. While MMS throughput does not change, the carrier surcharge for MMS is higher than that of SMS. Details of MMS charges are available on the [Portal Pricing](https://portal.telnyx.com/#/app/pricing/messaging) page.

Refer to the above question for specific 10DLC rate limit estimates for MMS.

---

## *Messaging throughput Estimate Tables*

---

### **How much throughput should I expect?**

Carriers have different approaches to throughput. In summary:

1. AT&T sets throughput based on Campaign. Each Campaign’s throughput is determined by its AT&T “Message Class” (a score determined by Use Case and, in many cases, a Vetting Score). You typically need to Vet your brand to achieve a high score, though Russell 3000 brands may default to a high score immediately.
2. T-Mobile sets throughput based on Brand, and each Brand has a Daily Allowance
3. Verizon has not declared a method as of September 2023, though they are part of 10DLC, so following the guidelines is required to send to their customers anyway

### **What are the throughputs for AT&T’s Message Class-based throughput system?**

As of September 2023, there are over 20 categories in AT&T’s throughput system, with only a few of these being in the Standard category. Use Cases in the Standard category include Dedicated (e.g., notifications), Marketing (e.g., promotions), and Mixed (e.g., an account used for promotions and notifications).

We have attempted to simplify these into the following table:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Class** | **Use Case** | **Vetting Score Requirement** | **TPM (SMS)** | **TPM**  **(MMS)** | **Variable Rate depending on score** |
| A, B | Dedicated, Mixed / Marketing | 75-100 | 4500 | 2400 | Y |
| C, D | Dedicated, Mixed / Marketing | 50-74 | 2400 | 1200 | Y |
| E, F | Dedicated, Mixed / Marketing | 1-49 | 240 | 150 | Y |
| T | Basic / Unregistered | 0 / NA | 75 | 50 | N/A |

There are over 15 Classes for Special Use Cases with a wide variety of throughput limits, limit methods (from per number to per Campaign), and Use Cases. Below are some of the most common Special Use Cases and their throughputs according to AT&T rules:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Message Class** | **Use Case** | **Vetting Score Reqmt** | **AT&T TPM (SMS)** | **AT&T TPM (MMS)** | **Variable Rate Based on Score** |
| K | Political |  | 4500 | 2400 | N\* |
| T | UCaaS Low Vol |  | 75 | 50 | N |
| B / D / F | UCaaS High Vol |  | 240 (B) / 2400 (D) / 4500 (F) | 150 (B) / 1200 (D) / 2400 (F) | Y |

*\*Vetting is mandatory for Brands conducting political Campaigns*

### **What are the throughput limits for T-Mobile’s Brand-based throughput system?**

T-Mobile sets limits at the Brand level, not Campaign. For Standard Campaigns, these limits are as follows:

|  |  |  |
| --- | --- | --- |
| **Brand Tier** | **Vetting Score Requirements** | **T-Mobile Daily Cap** |
| Top | 75-100 | 200,000 |
| High Mid | 50-74 | 40,000 |
| Low Mid | 25-49 | 10,000 |
| Low | 1-24 | 2,000 |

Brands which are not Vetted and are not on the Russell 3000 may default to a Low Brand Tier for T-Mobile throughput.

### **What are Verizon’s throughput limits?**

Verizon has not declared any throughput guidance as of September 2023. However, since Verizon has joined the TCR (the 10DLC oversight body), Telnyx highly recommends following 10DLC best practices.

---

## *10DLC Definitions / Acronyms*

---

* **10DLC:** 10 Digit Long Code. The protocol under which local long code A2P messages are regulated in the United States
* **A2P:** Application To Person Messaging. This typically covers ALL messages sent by or on behalf of a business.
* **Brand:** The trading name of the company sending messages to a customer
* **Campaign:** A way to organize 10DLC-registered numbers and their use cases, as governed by the TCR
* **MO:** Messaging Origination. A message sent to an A2P number. An MO fee determines the charges Carriers apply for receiving messages from one of their customers.
* **MT:** Messaging Termination. A message sent from an A2P number and terminating on and end user's handset. MT fees determine the charges Carriers apply for sending to their customers.
* **P2P:** Person-to-person. Messaging that is sent manually from one person’s phone to another, and is not on behalf of a business. P2P is subject to some special exemptions, but as a general rule Telnyx notes that ALL messages sent by businesses are considered A2P
* **TCR:** The Campaign Registry, an entity appointed by the Carriers to manage 10DLC registration records.

---

## *Fees, Charges and Other Questions*

---

### **I have questions about Fees. Where should I go?**

Head to our [10DLC Fees and Charges](https://support.telnyx.com/en/articles/5634625-10dlc-fees-and-charges) page.

### **I have another question or concern not covered in this document, where should I go?**

If you have any other questions, you can chat to our support team 24/7 via your [Mission Control Portal](https://portal.telnyx.com/#/login/sign-in), or on our Contact Us page. If you have specific messaging compliance questions please reach out to [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com).

---

Related Articles

[ISVs & 10DLC](https://support.telnyx.com/en/articles/5593977-isvs-10dlc)[10DLC Fees and Charges](https://support.telnyx.com/en/articles/5634625-10dlc-fees-and-charges)[Telnyx & 10DLC Compliance](https://support.telnyx.com/en/articles/5664840-telnyx-10dlc-compliance)[10DLC: Trust Scores & Use Cases](https://support.telnyx.com/en/articles/6325747-10dlc-trust-scores-use-cases)[Telnyx 10DLC Compliance Directory](https://support.telnyx.com/en/articles/6417677-telnyx-10dlc-compliance-directory)

Did this answer your question?

😞😐😃

Table of contents
