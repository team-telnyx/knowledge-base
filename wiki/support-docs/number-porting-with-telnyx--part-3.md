---
title: Number Porting with Telnyx
summary: This page consolidates Telnyx's number porting policies, procedures, and
  guidance for moving telephone numbers into and out of Telnyx. It covers submitting
  port requests via the Mission Control portal and API, SLA timelines for simple and
  non-simple ports, port request statuses, exception handling, reseller instructions,
  carrier-specific port-out tips, programmatic porting, and SMS considerations for
  ported-in numbers.
sources:
- url: https://support.telnyx.com/en/articles/1130630-porting-policy-procedure
- url: https://support.telnyx.com/en/articles/1130633-checking-a-port-request-status
- url: https://support.telnyx.com/en/articles/1130634-port-numbers-to-telnyx
- url: https://support.telnyx.com/en/articles/1130635-can-i-port-out-my-telnyx-number
- url: https://support.telnyx.com/en/articles/1130643-is-there-a-cancellation-fee
- url: https://support.telnyx.com/en/articles/1130661-does-telnyx-offer-post-paid-service
- url: https://support.telnyx.com/en/articles/1782930-port-request-rejected
- url: https://support.telnyx.com/en/articles/2033789-port-numbers-away-from-telnyx
- url: https://support.telnyx.com/en/articles/2047076-carrier-refusing-to-port-your-number
- url: https://support.telnyx.com/en/articles/2086149-number-porting-rules-and-guidelines
- url: https://support.telnyx.com/en/articles/3284588-port-request-statuses
- url: https://support.telnyx.com/en/articles/3947875-porting-away-from-bandwidth
- url: https://support.telnyx.com/en/articles/5386351-automating-ports-with-programmatic-api
- url: https://support.telnyx.com/en/articles/5595770-port-away-from-voip-ms
- url: https://support.telnyx.com/en/articles/7183887-sms-for-ported-in-phone-numbers
updated_at: 2026-07-17T09:03:47Z
---

# Number Porting with Telnyx

*Part 3 of 3 — see also: [Part 1](number-porting-with-telnyx--part-1.md), [Part 2](number-porting-with-telnyx--part-2.md)*

This page consolidates Telnyx's number porting policies, procedures, and guidance for moving telephone numbers into and out of Telnyx. It covers submitting port requests via the Mission Control portal and API, SLA timelines for simple and non-simple ports, port request statuses, exception handling, reseller instructions, carrier-specific port-out tips, programmatic porting, and SMS considerations for ported-in numbers.

## Porting Away from Specific Carriers

### Bandwidth

1. Raise a support ticket with Bandwidth porting support to request a copy of the CSR information for the numbers you wish to port away. If you do not leverage Bandwidth's port-out validation API, they do not confirm submitted information and grant automatic FOC; if you do leverage it, you must request a CSR.
2. Submit your port-in request to Telnyx (see [Port numbers to Telnyx](port-numbers-to-telnyx.md)).
3. When porting a large number of numbers, state "*Numbers provided in spreadsheet*" in the **Numbers to be ported** field of the LOA.
4. Use your own company information on the LOA (business name, address, authorized person's name and signature, and date).
5. Bandwidth does not use BTNs or account numbers; use any of the numbers being ported as both the BTN and Account Number.

### Voip.ms

Voip.ms leverages different providers depending on the number type (US, Canada, toll-free, international). Account information may vary based on whether you use sub-accounts.

To retrieve account information:

- **Company name and address** — listed on the top-left of your voip.ms invoice.
- **PIN Number** — under Main Menu → Account Settings → Security tab. Only required if you previously set one up.
- **Account number** — listed within the portal. Generally not required if no PIN is set.
- **Phone numbers** — available via the voip.ms portal and on your invoice.

If you have sub-accounts, you may need to submit individual ports for each sub-account. Once you have the information, fill out an LOA with Telnyx and submit your port via Numbers → Port Numbers.

Typical port times from voip.ms:

| Type | Average time to port | Possible expedite time | Expedite Fee |
| --- | --- | --- | --- |
| Canadian | 3 days | Same day (if submitted in the morning) | $150 per order |
| US | As little as 6 hours | As little as 6 business hours | No charge |
| Toll-free | 1–2 days | Same day | No charge |

To request an expedite, submit your port request and open a live chat with the porting team (bottom-right corner when logged into your Telnyx account). Expedites cannot guarantee same-day porting; the expedite fee still applies even if same-day porting is not possible.

## SMS for Ported-In Phone Numbers

For local and toll-free phone numbers in the US and Canada, porting voice and porting SMS are two completely separate processes. A porting order transitioning to a "ported" status indicates that voice has ported to Telnyx, but this does not take SMS into consideration. In some cases, messaging may continue to route through the losing carrier for a period of time after the port.

A NetNumber ID (NNID) is the identifier for the provider that owns the SMS routing of a telephone number. [NetNumber](https://netnumber.com/) manages NNIDs. A local or toll-free phone number in the US or Canada must always have an NNID assigned before sending and receiving messages.

At the FOC date/time when the phone number ports, the losing carrier is expected to release the NNID, and the phone number should update to the winning carrier's NNID. If the losing carrier fails to release the NNID, they will continue to send and receive messages for the number. This can occur in three instances:

- A porting "translations" issue — the losing carrier may have unintentionally failed to release the NNID due to an internal error or bug.
- Carrier block policies — some carriers retain SMS for a brief period after a port. The winning carrier must open a support ticket to override the NNID.
- You are hosting SMS elsewhere and only porting voice to Telnyx. In this case, the other carrier will reject any attempted NNID overrides.

Telnyx cannot guarantee that the losing carrier will immediately release the NNID when a phone number ports, but can provide visibility into when SMS successfully ports and act swiftly on messaging activation issues. See the [messaging porting developer guide](https://developers.telnyx.com/docs/numbers/porting/messaging-porting) for more information.

### SMS Porting Timelines

- **US/CA local numbers** — roughly 90% of port orders have SMS activated within 10 minutes of porting; the remaining 10% usually finish within 1–2 business days.
- **US/CA toll-free numbers** — SMS usually ports within 10 minutes; if not, it may take 4–5 business days.
- **All other phone numbers** — SMS is expected to port at the same time as voice.

If your order indicates SMS has ported but messages are failing to deliver, confirm that you have a working messaging profile ID associated with the phone number. If issues persist, open a support ticket for investigation.

## Billing and Account Notes

- **Cancellation fee** — Telnyx does not charge a cancellation fee. There is no contract.
- **Post-paid service** — Telnyx offers strictly pre-paid service at this time.

## Related Pages

- [Port numbers to Telnyx](port-numbers-to-telnyx.md)
- [Porting Policy & Procedure](porting-policy-procedure.md)
- [Can I port out my Telnyx number?](can-i-port-out-my-telnyx-number.md)
- [Port numbers away from Telnyx](port-numbers-away-from-telnyx.md)
- [Checking a Port Request Status](checking-a-port-request-status.md)
- [Port Request Statuses](port-request-statuses.md)
- [Port Request Rejected](port-request-rejected.md)
- [Carrier Refusing to Port Your Number](carrier-refusing-to-port-your-number.md)
- [Number Porting Rules and Guidelines](number-porting-rules-and-guidelines.md)
- [Automating Ports With Programmatic API](automating-ports-with-programmatic-api.md)
- [Porting away from Bandwidth](porting-away-from-bandwidth.md)
- [Port away from voip.ms](port-away-from-voip-ms.md)
- [SMS for Ported In Phone Numbers](sms-for-ported-in-phone-numbers.md)
- [Is there a cancellation fee?](is-there-a-cancellation-fee.md)
- [Does Telnyx offer post-paid service?](does-telnyx-offer-post-paid-service.md)
