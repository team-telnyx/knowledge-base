---
source_url: https://support.telnyx.com/en/articles/5761463-canadian-stir-shaken-implementation-faqs
scraped: 2026-06-11
---

Canadian STIR/SHAKEN Implementation FAQs | Telnyx Help Center

[Skip to main content](#main-content)

# Canadian STIR/SHAKEN Implementation FAQs

Find answers to your questions about compliance, required actions, attestations, and more.

Written by Telnyx Engineering

April 8, 2026

Table of contents

# **Canadian STIR/SHAKEN Implementation FAQs**

## **What do I need to do to be SHAKEN/STIR compliant in Canada?**

Simple! Nothing! Telnyx is taking care of all compliance requirements. Your outbound calls originating with Canadian CLI will receive appropriate signings from Telnyx’s Canadian partners.

## **Are attestation definitions the same in Canada as in the US?**

Yes, the attestation definitions we use in the US are applicable in Canada SHAKEN/STIR.

* Full Attestation (A): The provider knows the customer, knows they have a right to use the originating number, and knows that the call originated on their network. For numbers purchased in the Telnyx portal, you should expect to receive an 'A Attestation'.
* Partial Attestation (B): The provider knows the customer but the customer may be using another provider's phone number. The call is legitimate but the provider can’t fully attest because of missing information.
* Gateway Attestation (C): The provider can’t verify the customer or the phone number and has no way of knowing whether the call is legitimate. The originating provider will still attest to the call in order to mark that the call originated on their network.

## **What will my attestation be for Canadian SHAKEN/STIR?**

If you have your Canadian CLI listed in your Telnyx Mission Control Portal (whether the number was purchased from Telnyx or ported into Telnyx), you will receive an A attestation, since we know you have the right to use that particular Canadian number. If your CLI is not listed in your Telnyx Mission Control Portal (you neither purchased the number from Telnyx nor ported it into Telnyx), you will receive a B attestation.

## **Is there an additional cost for customers who want to authenticate traffic?**

There is no additional charge for SHAKEN/ STIR services, so it will be free to all Telnyx customers.

## **Will I be notified if Telnyx adds attestations to my calls, and what attestation I received?**

All calls originating on the Telnyx network with Canadian CLI will receive an attestation. There is no action required from the customer.

The customer will not be notified of the attestation it receives from Telnyx, but customers should be able to predict the attestation level based on the requirements outlined in the above questions.

---

Related Articles

[STIR/SHAKEN With Telnyx](https://support.telnyx.com/en/articles/5402969-stir-shaken-with-telnyx)[SHAKEN/STIR Parameters](https://support.telnyx.com/en/articles/7421223-shaken-stir-parameters)[Inbound Call Screening](https://support.telnyx.com/en/articles/8037040-inbound-call-screening)[Understanding the FCC’s Eighth Report and Order on Third-Party Authentication](https://support.telnyx.com/en/articles/10806916-understanding-the-fcc-s-eighth-report-and-order-on-third-party-authentication)[Understanding SIP 603+ carrier rejections](https://support.telnyx.com/en/articles/15395095-understanding-sip-603-carrier-rejections)

Did this answer your question?

😞😐😃

Table of contents
