---
title: "United States - N11 Codes"
summary: "In this guide we will explain N11 codes in the United States and their purpose. See Telnyx guidance and requirements."
sources:
- url: "https://support.telnyx.com/en/articles/4567969-united-states-n11-codes"
updated_at: 2026-09-28T18:12:50Z
tags: [support-docs]
source_path: "support-docs/en--articles--4567969-united-states-n11-codes.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/en--articles--4567969-united-states-n11-codes.md -->

# United States - N11 Codes

In this guide we will explain N11 codes in the United States and their purpose. See Telnyx guidance and requirements.




## **What Are N11 Codes?**

N11 codes are used to provide three-digit dialing access to special services.

In the United States, the FCC administers N11 codes. The FCC recognizes 211, 311, 511, 711, 811 and 911 as nationally assigned, but has not disturbed other traditional uses.

The table below summarizes N11 assignments, reservations, and traditional usage and what N11 assignments are supported for outbound dialing through Telnyx. Telnyx supports outbound calls to 411 directory assistance but does not provide directory listing services.

| N11 Code | Description | Supported |
| --- | --- | --- |
| 211 | Community Information and Referral Services | No |
| 311 | Non-Emergency Police and Other Governmental Services | Yes |
| 411 | Local Directory Assistance | Yes |
| 511 | Traffic and Transportation Information (US); Provision of Weather and Traveller Information Services (Canada) | Yes |
| 611 | Repair Service | Yes |
| 711 | Telecommunications Relay Service (TRS) | Yes |
| 811 | Access to One Call Services to Protect Pipeline and Utilities from Excavation Damage (US) | Yes |
| 911 | Emergency | Yes |
| [988](https://telnyx.com/resources/988-suicide-prevention-hotline) (call and text) | National Suicide Prevention Lifeline | Yes |

**Billing:** Supported does not mean free of charge. Calls to services such as 411 directory assistance may incur per-call charges. Contact Telnyx Support to confirm the applicable rate for your account.

## N11 Outbound Calls (More Info)

For N11 outbound calls there are no caller ID (CLI) validations enforced, as we prioritize connecting these calls. However for 911, if an invalid CLI or a CLI without an emergency address is used, this is classified as an unregistered call at a cost of $100 per call. Please ensure you send valid caller ID's from numbers on your account that have emergency services enabled and with an address.

​

![Breaking Line](_images/682991ade0be9812.png)
