---
source_url: https://support.telnyx.com/en/articles/5402969-stir-shaken-with-telnyx
scraped: 2026-07-08
content_hash: 8c2fe3385a179f19439ad85e35c843053c52177d9b68d2867c369d75c40fe2cb
---

STIR/SHAKEN With Telnyx | Telnyx Help Center

[Skip to main content](#main-content)

# STIR/SHAKEN With Telnyx

SHAKEN/STIR is an authentication framework that aims to curb the robocall trend.

Written by Dillin

May 5, 2026

Table of contents

---

# **STIR/SHAKEN**

---

STIR/SHAKEN is an industry framework that is mandated by the Federal Communications Commission (FCC) to reduce the number of fraudulent calls and robocalls made over IP networks. STIR/SHAKEN was implemented on June 30th 2021, so it is a new and different system, and this article is for you if you are wondering what this means for your business.

**More recently, the FCC has moved up the deadline for small Service Providers to sign their own calls. Starting June 30, 2022, small service providers will be expected to sign their outbound calls with their own SHAKEN tokens. Telnyx will continue to sign calls we receive that are unsigned, but Telnyx is not responsible for your compliance with FCC regulations.**

To start, STIR/SHAKEN is shorthand for **Secure Telephony Identity Revisited (STIR) and / Secure Handling of Asserted information using toKENs (SHAKEN)**.

Originating service providers assign what is called an **Attestation** level to calls made on their network, and assign a token to these calls that is included in the SIP INVITE header, and then this is passed to the terminating service provider. The signature on this token is validated and the call is connected to the recipient.

The terminating provider can also pass along the validation results on the token for additional action such as blocking the call.

## **What is Attestation?**

There are three levels of Attestation within STIR/SHAKEN, signified by A, B and C from highest to lowest safety.

**Full Attestation (A)** means the provider knows the customer and knows they have a right to use the originating number, and that the call originated on their network. For numbers purchased in the Telnyx portal you should expect this level of Attestation.

**Partial Attestation (B)** means the provider knows the customer but may not know the number they are using. The call is legitimate but the provider is missing information that would classify the call as Full Attestation. If the number you are using with Telnyx was not bought on our portal, then you can expect this level of Attestation.

**Gateway Attestation (C)** means that the origination provider cannot verify the customer *or* the phone number they are using, and thus has no way to verify if the traffic they see is legitimate. The call is still given a token to mark that it originated on the provider's network.

​

**Unavailable** means the origination provider did not add the necessary information for the call to be verified or the call hit the PSTN so the token was lost, thus, having no way to verify if the traffic they see is legitimate.

**Invalid** means the origination provider did not properly authenticate the customer or the phone number they are using, the call has a token but Telnyx was not able to verify its authenticity, thus, having no way to verify if the traffic they see is legitimate.

Attestation values are available for review via the CSV files you can download from your [reporting section](https://portal.telnyx.com/#/reporting/detailed-records) in the mission control portal.

## **How This Affects You**

Telnyx is fully compliant with STIR/SHAKEN and all calls originating on our network will receive attestation, with **no action required** by the customer. Customers are notified of the attestation level their calls receive, but they should know what to expect given the guidelines above. The implementation of this service will not incur additional charges to any of our customers.

If you’re getting Telnyx to sign your business calls, you can sit back & relax, we’ve taken care of everything for you. As a carrier, we have been approved by the STI-PA to participate in the SHAKEN/ STIR framework and are [fully SHAKEN/STIR compliant](https://fccprod.servicenowservices.com/rmd?id=rmd_listings).

Today, Telnyx is authenticates every outbound call with a valid U.S. Caller ID that originates on the Telnyx platform and is abiding by the attestation levels listed above. We are also passing on SHAKEN/STIR headers of customers who have their authorization toKENs along the PSTN. Inbound calls with A attestation and a valid token will now have the 'verstat' parameter added to P-Asserted-Identity headers.

## **How to increase attestation**

Customers who would like to receive an A attestation should consider porting their numbers over using the Telnyx portal. With [Fastport](https://telnyx.com/products/number-porting), customers can port their numbers to Telnyx in just a few clicks while maintaining complete control and transparency throughout the porting process.

## **Can I sign my own calls?**

As expected, the FCC has devised very clear standards to govern who is able to partake in the framework and in what capacity. Most customers will require their telephony provider to carry out call signing to comply with SHAKEN/STIR. However, some service providers are eligible to sign their own calls, even if they buy their numbers from Telnyx.

You can sign your own calls and Telnyx will simply pass your certificate onto our terminating provider.

## **What do I need to sign my own calls?**

Some companies may think that signing their own calls will result in a greater transparency over which attestation level they receive. There are a number of steps you’ll have to take if planning on signing your own calls. Firstly the company needs to be approved by the [Secure Telephone Identity Policy Administrator](https://authenticate.iconectiv.com/) (STI-PA) who is in turn vetted by the [Secure Telephone Identity Governance Administrator](https://sti-ga.atis.org/) (STI-GA). But it doesn’t stop there, the company will also need to fulfill the following requirements:

1. Have a 499A (A Telecommunications Reporting Worksheet) on file with the FCC;
2. Have an Operating Company Number (OCN), this is used to identify CLEC and Reseller usage data
3. Have a robocalling mitigation plan filed with the FCC
4. Have obtained valid certificates from an approved Certificate Authority
5. Have implemented a SHAKEN/STIR solution on their network.

For many smaller providers, it can be a lot of time and effort to get these docs and solutions in order. That’s where Telnyx comes in.

## **On-net calling**

Where customers receiving calls from other Telnyx customers and want to receive identity headers, please ensure you register with your credentials connection via TCP or for IP/FQDN connection please specify TCP as the inbound transport protocol.   
​  
The reason for this is to prevent packet fragmentation and call completion issues for customers since the Identity header is very large and as such only this transport protocol is supported.

![Breaking Line](_images/682991ade0be9812.png)

## If you have any further questions regarding the STIR/SHAKEN infrastructure and what it means, do not hesitate to reach out to [support@telnyx.com](mailto:support@telnyx.com)

---

Related Articles

[Robocall Mitigation Database](https://support.telnyx.com/en/articles/5544430-robocall-mitigation-database)[Canadian STIR/SHAKEN Implementation FAQs](https://support.telnyx.com/en/articles/5761463-canadian-stir-shaken-implementation-faqs)[SHAKEN/STIR Parameters](https://support.telnyx.com/en/articles/7421223-shaken-stir-parameters)[Inbound Call Screening](https://support.telnyx.com/en/articles/8037040-inbound-call-screening)[Understanding the FCC’s Eighth Report and Order on Third-Party Authentication](https://support.telnyx.com/en/articles/10806916-understanding-the-fcc-s-eighth-report-and-order-on-third-party-authentication)

Did this answer your question?

😞😐😃

Table of contents
