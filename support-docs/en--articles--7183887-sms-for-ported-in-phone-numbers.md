---
source_url: https://support.telnyx.com/en/articles/7183887-sms-for-ported-in-phone-numbers
scraped: 2026-07-08
content_hash: de8cf04d1f23598efe7a7e230d686cba2855b80160f1d903a6cd5a980b89ed41
---

SMS for Ported In Phone Numbers | Telnyx Help Center

[Skip to main content](#main-content)

# SMS for Ported In Phone Numbers

Discover the intricacies of phone numbers, ordering processes, and numbering team coordination with Telnyx.

Written by Telnyx Engineering

June 6, 2024

Table of contents

# **SMS for Ported In Phone Numbers**

For local and toll-free phone numbers in the US and Canada, porting voice and porting SMS are two completely separate processes.

A porting order transitioning into a “ported” status indicates that voice has ported over to Telnyx. However, this status change does not take SMS into consideration at all. In some cases, it is possible that after a phone number ports, messaging will continue to route through the losing carrier for a period of time.

To understand this, let's take a step back. A NetNumber ID (NNID) is the identifier for the provider that owns the SMS routing of a telephone number. [NetNumber](https://netnumber.com/) manages NNIDs. A local or toll-free phone number in the US or Canada must always have an NNID assigned before sending and receiving messages.

At the FOC date/time when the phone number ports, the losing carrier is expected to release the NNID, and the phone number should update to the winning carrier’s NNID. As a result, both voice and SMS would be routed through the winning carrier. This is how porting works in the majority of cases.

If the losing carrier fails to release the NNID even after the phone number ports, the losing carrier will continue to send and receive messages for the phone number. There are generally three instances where this could occur:

* This may be similar to what is known as a porting "translations" issue. Once the port completes, the losing carrier may have unintentionally failed to release the NNID. It's possible there was an error or bug in the losing carrier’s internal systems. It’s also possible that their internal systems needed some additional time to recognize that the phone number was ported out and subsequently release the NNID.
* Some carriers have block policies in place such that if a phone number ports, they will be able to retain SMS for a brief period of time. The winning carrier needs to open a support ticket to have the NNID overridden from the losing carrier.
* You are planning on hosting your SMS elsewhere and only plan on porting over voice to Telnyx. In this case, the other carrier will reject any attempted NNID overrides.

Telnyx cannot guarantee that the losing carrier will immediately release the NNID when a phone number ports. Instead, Telnyx can provide additional visibility into when SMS successfully ports, and act swiftly when there are any issues with the messaging activation. Take a look at [this developer guide](https://developers.telnyx.com/docs/numbers/porting/messaging-porting) to learn more about enabling this porting feature.

## **FAQ: How much time does it normally take before I receive confirmation that SMS is ported over?**

For US/CA local phone numbers, roughly 90% of port orders have SMS activated within 10 minutes of a phone number porting. The remaining 10% of phone numbers usually finish SMS porting within 1-2 business days.

For US/CA toll-free phone numbers, SMS will usually port within 10 minutes of a phone number porting. However if it doesn’t activate within that 10 minute window, it may take 4-5 business days before SMS ports over.

For all other phone numbers, it is expected that SMS will port at the same time as voice.

## **FAQ: My order says that the SMS ported, but my numbers are failing to deliver messages. What is the issue?**

Please confirm that you have a working messaging profile ID associated with the phone number. If you do and you are still experiencing issues, please cut a support ticket for our team to investigate.

---

Related Articles

[New Zealand Number Porting](https://support.telnyx.com/en/articles/3267206-new-zealand-number-porting)[Hosted SMS Messaging Process](https://support.telnyx.com/en/articles/5336668-hosted-sms-messaging-process)[Porting Requirements](https://support.telnyx.com/en/articles/6460777-porting-requirements)[Verified Numbers](https://support.telnyx.com/en/articles/6988813-verified-numbers)[US / CA Toll Free Number Porting](https://support.telnyx.com/en/articles/8673249-us-ca-toll-free-number-porting)

Did this answer your question?

😞😐😃

Table of contents
