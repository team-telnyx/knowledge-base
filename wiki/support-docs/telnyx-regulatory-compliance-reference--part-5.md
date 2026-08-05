---
title: Telnyx Regulatory & Compliance Reference
summary: A consolidated reference for Telnyx customers covering U.S. and state regulatory
  requirements, FCC compliance programs (STIR/SHAKEN, RMD, RND, DNO), Telnyx security
  certifications, traffic surcharges, and number lifecycle policies that affect voice
  and messaging services.
sources:
- url: https://support.telnyx.com/en/articles/10806916-understanding-the-fcc-s-eighth-report-and-order-on-third-party-authentication
- url: https://support.telnyx.com/en/articles/1130616-number-not-portable-tn-not-portable-error
- url: https://support.telnyx.com/en/articles/11358700-what-is-the-u-s-reassigned-numbers-database
- url: https://support.telnyx.com/en/articles/12141904-legal-update-texas-s-mini-tcpa-now-applies-to-texts
- url: https://support.telnyx.com/en/articles/12397834-understanding-telnyx-soc-compliance-and-certifications
- url: https://support.telnyx.com/en/articles/12805746-surcharge-for-high-abandoned-call-rates
- url: https://support.telnyx.com/en/articles/12933869-understanding-the-fcc-s-new-do-not-originate-dno-requirements-effective-december-15-2025
- url: https://support.telnyx.com/en/articles/15668484-calls-per-second-cps-limits
- url: https://support.telnyx.com/en/articles/5883839-what-is-the-reassigned-numbers-database
- url: https://support.telnyx.com/en/articles/7834487-calls-per-second-cps-surcharge
- url: https://support.telnyx.com/en/articles/8648864-what-happens-with-my-numbers-after-my-account-gets-abolished-for-negative-balance
- url: https://support.telnyx.com/en/collections/12044103-regulatory
updated_at: 2026-08-05T13:26:15Z
---

# Telnyx Regulatory & Compliance Reference

*Part 5 of 5 — see also: [Part 1](telnyx-regulatory-compliance-reference--part-1.md), [Part 2](telnyx-regulatory-compliance-reference--part-2.md), [Part 3](telnyx-regulatory-compliance-reference--part-3.md), [Part 4](telnyx-regulatory-compliance-reference--part-4.md)*

A consolidated reference for Telnyx customers covering U.S. and state regulatory requirements, FCC compliance programs (STIR/SHAKEN, RMD, RND, DNO), Telnyx security certifications, traffic surcharges, and number lifecycle policies that affect voice and messaging services.

## Surcharge for High Abandoned Call Rates

Starting **November 1, 2025**, Telnyx applies a surcharge to outbound traffic with high abandoned call rates to reduce brief, dropped call patterns that strain network capacity.

If more than 20% of outbound calls are dropped by the originating side before being answered, the account is subject to an **abandoned call surcharge of $0.005** per abandoned call. An "abandoned call" is any call where the originating user initiates disconnection during the ringing or call set-up process, including calls to disconnected numbers.

### Tracking

There are two options to track the abandoned call percentage:

1. A new pie chart in the [dashboard page](https://portal.telnyx.com/#/reports/dashboard) showing abandoned vs. not abandoned calls in the reporting section of the portal.
2. Generate a Usage Report and filter for abandoned calls:
   - Go to **Reporting > Usage Reports**
   - Switch to the **Advanced Version** view
   - Select **SIP Trunking** as the product
   - Under dimensions, check **Direction** and **Hangup Details**
   - Under metrics, check **Attempted**
   - Filter by **Direction = outbound**
   - Breakout with **recv_cancel** contains abandoned calls

### Frequently Asked Questions

- **If my account had 21% abandoned calls, will the surcharge apply to the percentage that exceeds the threshold or all the abandoned calls?** The surcharge applies to all abandoned calls, not just those that exceeded the threshold. If an account makes 100 calls in one month and 21 are abandoned, the surcharge is applied to all 21 abandoned calls.
- **Does this apply to inbound or outbound or both?** This only applies to outbound calls.
- **What is the rate charged if an account exceeds the 20% threshold?** $0.005 USD per call.

## Number Lifecycle After Account Abolishment

If a Telnyx account is left with a negative balance for a period of one month, an abolishing process takes place and the numbers in the account are deleted. After deletion, numbers are set to a "hold" status for two weeks. During this period, only the original account holder can search for and purchase the numbers back via the [Search and Buy Numbers](https://portal.telnyx.com/#/app/numbers/search-numbers) section of the portal.

If the numbers are not bought back during the "hold" period, the status changes to "Aging" and remains so for two weeks. While in "Aging," no one (including the original account holder) can buy the numbers. This is part of the FCC-required number recycling process. After two weeks in "Aging," the numbers are released and become generally available to any Telnyx account.

If the account was abolished, simply adding balance to the account will not bring the numbers back. If the numbers are still in "hold" status, they must be bought back after adding balance. If the numbers are in "Aging" status, the numbering team can still retrieve them, but the request must be made directly. The numbering team can be reached at [numbering@telnyx.com](mailto:numbering@telnyx.com); the support team is available at [support@telnyx.com](mailto:support@telnyx.com).

This general process also applies when a number is accidentally deleted from an account: it immediately goes to "hold" status, then "Aging" after two weeks, and is released after another two weeks.

### Auto-Recharge and Notifications

Numbers are charged a Monthly Recurring Cost (MRC) at the beginning of every month. Even with a positive balance, an account can fall into the negative if it is abandoned for several months without auto-recharge configured. See the [Billing setup article](https://support.telnyx.com/en/articles/4280500-billing-setup-billing-groups) for instructions on configuring Auto-Recharge. Recurring payments can fail due to card expiry or other issues, so notification settings should be configured to alert the appropriate contacts about low balance and number deletion events. See the [Notification settings article](https://support.telnyx.com/en/articles/4277896-notification-settings) for details.

## Number Portability: "TN Not Portable" Errors

The "TN Not Portable" error is a catch-all error returned when a number cannot be ported. The losing carrier is often intentionally unspecific about the reason. Common causes include:

- The number may be inactive with the losing carrier (no longer assigned to the account or deactivated).
- The number is stuck in a "pending" state because another action was recently initiated.
- The number has a special feature associated with it, such as a signal ring.
- The number is on a special rate plan, often a bundled TV, voice, and Internet plan.
- A recent informational update was made to the account.

To resolve this type of error, contact the existing carrier and ask if any numbers on the account may not be portable. They can quickly identify any features or inactive numbers that might hold up a port request. If a number is inactive, it will likely need to be re-activated before a port out can continue.

## Disclaimer

The information provided in this Telnyx support article is for general informational purposes only and should not be construed as legal advice. Please consult with a qualified attorney for guidance on legal or regulatory compliance.
