---
title: 10DLC Compliance and Error Codes
summary: A comprehensive reference for 10DLC campaign compliance, covering carrier
  error codes and their resolutions, required keywords and confirmation messages,
  privacy policy verbiage, brand verification requirements, campaign suspension for
  inactivity, and SMS porting considerations for ported-in phone numbers.
sources:
- url: https://support.telnyx.com/en/articles/10547022-10dlc-carrier-error-codes-explanations
- url: https://support.telnyx.com/en/articles/10645338-10dlc-keywords-and-confirmation-messages
- url: https://support.telnyx.com/en/articles/10645583-10dlc-privacy-policy
- url: https://support.telnyx.com/en/articles/10715016-10dlc-inaccurate-or-inconsistency-error
- url: https://support.telnyx.com/en/articles/10715184-10dlc-unverified-brand
- url: https://support.telnyx.com/en/articles/10723378-10dlc-campaign-suspended
- url: https://support.telnyx.com/en/articles/10744086-10dlc-error-806
- url: https://support.telnyx.com/en/articles/7183887-sms-for-ported-in-phone-numbers
updated_at: 2026-06-11T11:10:54Z
---

# 10DLC Compliance and Error Codes

*Part 3 of 3 — see also: [Part 1](10dlc-compliance-and-error-codes--part-1.md), [Part 2](10dlc-compliance-and-error-codes--part-2.md)*

A comprehensive reference for 10DLC campaign compliance, covering carrier error codes and their resolutions, required keywords and confirmation messages, privacy policy verbiage, brand verification requirements, campaign suspension for inactivity, and SMS porting considerations for ported-in phone numbers.

## SMS Porting for Ported-In Phone Numbers

For local and toll-free phone numbers in the US and Canada, porting voice and porting SMS are two completely separate processes. A porting order transitioning to a "ported" status means voice has ported — it does not mean SMS has ported.

A NetNumber ID (NNID) is the identifier for the provider that owns the SMS routing of a telephone number, managed by [NetNumber](https://netnumber.com/). A local or toll-free phone number in the US or Canada must always have an NNID assigned before sending and receiving messages.

At the FOC date/time, the losing carrier is expected to release the NNID and the number should update to the winning carrier's NNID. If the losing carrier fails to release the NNID, they will continue to send and receive messages for the number. This can happen in three scenarios:

- **Translations issue:** The losing carrier unintentionally failed to release the NNID, possibly due to an internal error or simply needing additional time to recognize the port-out.
- **Block policy:** Some carriers retain SMS for a brief period after a port; the winning carrier must open a support ticket to override the NNID.
- **Intentional split:** You are hosting SMS elsewhere and only porting voice to Telnyx. The other carrier will reject any NNID override attempts.

Telnyx cannot guarantee the losing carrier will immediately release the NNID. See the [Telnyx messaging porting developer guide](https://developers.telnyx.com/docs/numbers/porting/messaging-porting) for enabling porting features that provide additional visibility.

### SMS Porting Timelines

| Number Type | Typical Time to SMS Activation |
|-------------|-------------------------------|
| US/CA local | ~90% within 10 minutes; remaining 10% within 1–2 business days |
| US/CA toll-free | Usually within 10 minutes; if not, may take 4–5 business days |
| All other numbers | SMS ports at the same time as voice |

If your order says SMS has ported but messages are failing to deliver, confirm you have a working messaging profile ID associated with the phone number. If the issue persists, open a support ticket for investigation.
