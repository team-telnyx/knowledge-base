---
title: Telnyx Wireless and Messaging Reference
summary: A consolidated reference covering Telnyx eSIM setup (QR code and manual activation),
  manual IMSI selection, SIM connectivity logs and wireless connectivity states, SIM
  data limits and notifications, SIM theft prevention via IMEI authorization, MMS
  sending/receiving with FAQs, group messaging, bulk messaging via Google Sheets,
  number pooling, and the international voice spend limit.
sources:
- url: https://support.telnyx.com/en/articles/10067533-manual-esim-activation-guide
- url: https://support.telnyx.com/en/articles/11017501-understanding-wireless-connectivity-states-telnyx-api
- url: https://support.telnyx.com/en/articles/3102823-mms-sending-and-receiving
- url: https://support.telnyx.com/en/articles/3154822-number-pooling
- url: https://support.telnyx.com/en/articles/3403998-sim-data-limits-notifications
- url: https://support.telnyx.com/en/articles/4450150-faqs-about-mms-at-telnyx
- url: https://support.telnyx.com/en/articles/5666594-sim-connectivity-logs
- url: https://support.telnyx.com/en/articles/5761437-sim-card-theft-prevention
- url: https://support.telnyx.com/en/articles/8117401-how-to-setup-a-telnyx-esim-via-qr-code
- url: https://support.telnyx.com/en/articles/8228452-email-notification-international-spend-limit
- url: https://support.telnyx.com/en/articles/8255134-group-messaging-bulk-sending-mms
- url: https://support.telnyx.com/en/articles/8268223-bulk-messaging-with-sheets
- url: https://support.telnyx.com/en/articles/9183726-manual-imsi-selection-on-telnyx-sim
updated_at: 2026-07-17T08:59:32Z
---

# Telnyx Wireless and Messaging Reference

*Part 4 of 4 — see also: [Part 1](telnyx-wireless-and-messaging-reference--part-1.md), [Part 2](telnyx-wireless-and-messaging-reference--part-2.md), [Part 3](telnyx-wireless-and-messaging-reference--part-3.md)*

A consolidated reference covering Telnyx eSIM setup (QR code and manual activation), manual IMSI selection, SIM connectivity logs and wireless connectivity states, SIM data limits and notifications, SIM theft prevention via IMEI authorization, MMS sending/receiving with FAQs, group messaging, bulk messaging via Google Sheets, number pooling, and the international voice spend limit.

## International Spend Limit

Telnyx monitors international voice spend as a fraud preventative measure. During every 24-hour period, if SIP Connections or Voice API Applications spend more than $700 in international calling, Telnyx sends the account owner an email notification.

### What counts as international

An outbound call where the destination number country differs from the origination number country (e.g. Ireland +353 origination to United States +1 destination).

### When the limit is reached

Telnyx disables further international calls from terminating on the account. Local calling (where origination and destination countries match) is not disabled.

### Error code

The error returned is `403 International daily spent limit reached D39`. See the [Telnyx SIP response codes](https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes) for a full list.

### Reset

The international spend limit resets at 00:00 UTC each day.

### Adjusting the limit

This is a global default limit that applies to all Telnyx customers and cannot be adjusted from the account. Telnyx Support can increase or decrease it for specific use cases.

### Identifying traffic

Run a [usage report](https://portal.telnyx.com/#/app/reporting/usage-reports) broken down by connection to identify which connections have the highest spend. Run a [detail records report](https://portal.telnyx.com/#/app/reporting/detailed-records) to see which numbers are making calls and to which destinations. Use example numbers to check [call flows](https://portal.telnyx.com/#/app/next/debugging/sip-call-flow-tool) and determine source IP addresses.
