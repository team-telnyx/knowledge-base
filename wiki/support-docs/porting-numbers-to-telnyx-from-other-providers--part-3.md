---
title: Porting Numbers to Telnyx from Other Providers
summary: A comprehensive guide to porting phone numbers into Telnyx from carriers
  and resellers including Skype, Twilio, Bandwidth, Aircall, Intercom, RingCentral,
  Vonage, Grasshopper, Microsoft Teams, and voip.ms — covering required credentials,
  provider-specific steps, common rejection reasons, timelines, and how to get help.
sources:
- url: https://support.telnyx.com/en/articles/10715399-porting-away-from-skype
- url: https://support.telnyx.com/en/articles/14708128-porting-numbers-away-from-aircall-to-telnyx
- url: https://support.telnyx.com/en/articles/14708129-porting-numbers-away-from-intercom-to-telnyx
- url: https://support.telnyx.com/en/articles/14708130-porting-numbers-away-from-resellers-aircall-intercom-ringcentral-vonage-etc
- url: https://support.telnyx.com/en/articles/14790558-how-to-find-your-porting-pin-or-passcode
- url: https://support.telnyx.com/en/articles/3947850-porting-away-from-twilio
- url: https://support.telnyx.com/en/articles/3947875-porting-away-from-bandwidth
- url: https://support.telnyx.com/en/articles/5104103-port-your-microsoft-ms-teams-numbers
- url: https://support.telnyx.com/en/articles/5595770-port-away-from-voip-ms
- url: https://support.telnyx.com/en/articles/5820338-best-practices-for-contacting-porting
updated_at: 2026-06-11T11:12:50Z
---

# Porting Numbers to Telnyx from Other Providers

*Part 3 of 3 — see also: [Part 1](porting-numbers-to-telnyx-from-other-providers--part-1.md), [Part 2](porting-numbers-to-telnyx-from-other-providers--part-2.md)*

A comprehensive guide to porting phone numbers into Telnyx from carriers and resellers including Skype, Twilio, Bandwidth, Aircall, Intercom, RingCentral, Vonage, Grasshopper, Microsoft Teams, and voip.ms — covering required credentials, provider-specific steps, common rejection reasons, timelines, and how to get help.

## Common Rejection Reasons

| Rejection | Cause | Fix |
|---|---|---|
| `PASSCODE_PIN_INVALID` | Wrong PIN submitted | Contact your provider for the correct carrier-level PIN |
| `ACCOUNT_NUMBER_MISMATCH` | Wrong account number | Reseller account IDs ≠ carrier account numbers — confirm with provider |
| `BUSINESS_NAME_MISMATCH` | Name doesn't match carrier records | Get the exact legal name from your provider |
| `SERVICE_ADDRESS_MISMATCH` | Address doesn't match carrier records | Use the address on file with the carrier, not your billing address |

Each rejection typically adds 3–5 business days of delay. Always verify credentials before submitting.

## Pre-Submission Checklist

- ☐ Confirmed the underlying carrier with your current provider
- ☐ Obtained the correct account number (carrier-level, not reseller login)
- ☐ Obtained the correct PIN/passcode
- ☐ Verified the authorized name matches exactly what's on the carrier account
- ☐ Verified the service address matches the carrier's records
- ☐ LOA signed and ready to upload (if required by the losing carrier)

## Porting Timelines

Timelines vary by provider and complexity:

| Scenario | Typical Timeline |
|---|---|
| Simple ports (1–5 numbers, US/CA) | 3–7 business days |
| Complex ports (6+ numbers or mixed rate centers) | 5–15 business days |
| MS Teams | As little as 1 business day |
| Skype | A few days to a week or longer |
| voip.ms US numbers | As little as 6 hours |
| voip.ms Canadian numbers | ~3 days (same-day expedite available for $150/order) |
| voip.ms Toll-free | 1–2 days (same-day expedite available) |

**Expediting:** To request an expedite, submit your port request and open a live chat with the porting team. Expedites cannot guarantee same-day porting and depend on the losing carrier. Expedite fees apply even if same-day porting isn't achieved.

## Contacting Telnyx Porting Support

The Telnyx Porting team is available **9 AM – 7 PM CT, Monday–Friday**. Communications outside those hours are resolved the next business day.

| Method | Details |
|---|---|
| **Chat** | Click the chat icon (bottom-right of the screen when signed into the Portal) |
| **Email** | [porting@telnyx.com](mailto:porting@telnyx.com) |
| **Phone** | 1-888-980-9750 |

**Choosing the right method:**
- **Status update** → Chat or phone for quickest resolution.
- **Expedite request or detailed context** → Support ticket for a documented trail.
- **Reporting/correcting issues on a specific order** → Post on the individual port order rather than just via chat or a general ticket — this ensures cross-company visibility and clear communication.

If you need help identifying an underlying carrier, resolving a rejection, or escalating with an unresponsive provider, contact [porting@telnyx.com](mailto:porting@telnyx.com) with your port order number.
