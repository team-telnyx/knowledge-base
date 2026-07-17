---
title: 'Telnyx Phone Numbers: Ordering, E911, and Number Management'
summary: This page consolidates Telnyx guidance on phone number ordering, including
  account verification restrictions, searching and buying numbers, requirement groups,
  working with the numbering team, E911 address registration and setup, testing E911
  with 933, handling spam/scam-likely flags, and managing numbers through the My Numbers
  Page.
sources:
- url: https://support.telnyx.com/en/articles/10715715-phone-number-ordering-restrictions
- url: https://support.telnyx.com/en/articles/1130647-register-e911-addresses
- url: https://support.telnyx.com/en/articles/1130683-e911-setup-guide
- url: https://support.telnyx.com/en/articles/1130709-how-do-i-test-e911-service
- url: https://support.telnyx.com/en/articles/4088988-telnyx-how-to-handle-spam-scam-likely
- url: https://support.telnyx.com/en/articles/4294429-addresses-overview
- url: https://support.telnyx.com/en/articles/4349113-my-numbers-page
- url: https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers
- url: https://support.telnyx.com/en/articles/7205411-numbering-team-best-practices
- url: https://support.telnyx.com/en/articles/9801714-requirement-groups-for-ordering-phone-numbers
updated_at: 2026-07-17T09:01:25Z
---

# Telnyx Phone Numbers: Ordering, E911, and Number Management

*Part 5 of 6 — see also: [Part 1](telnyx-phone-numbers-ordering-e911-and-number-management--part-1.md), [Part 2](telnyx-phone-numbers-ordering-e911-and-number-management--part-2.md), [Part 3](telnyx-phone-numbers-ordering-e911-and-number-management--part-3.md), [Part 4](telnyx-phone-numbers-ordering-e911-and-number-management--part-4.md), [Part 6](telnyx-phone-numbers-ordering-e911-and-number-management--part-6.md)*

This page consolidates Telnyx guidance on phone number ordering, including account verification restrictions, searching and buying numbers, requirement groups, working with the numbering team, E911 address registration and setup, testing E911 with 933, handling spam/scam-likely flags, and managing numbers through the My Numbers Page.

## Handling Spam/Scam Likely Flags

If your phone number has been flagged as "Spam Likely":

1. **Register your phone number with the Free Caller Registry (FCR)** at [freecallerregistry.com/fcr](https://www.freecallerregistry.com/fcr/).
2. **Add CNAM** by going to Mission Control Portal under Real-Time Communications → Numbers → [Manage Numbers](https://portal.telnyx.com/#/numbers/my-numbers), find the flagged number, and click the pencil icon for advanced settings. In the Voice tab, enable CNAM Listing and add a custom name. CNAM is not applicable for toll-free numbers. CNAM information is important to the engines that analyze and identify phone numbers as "spam likely".

   ![](_images/15c5c16951a3335e.png)
3. **Be patient and age the number.** Start making calls and wait for numbers to be aged. Aging time varies by carrier; 1 week of healthy calls has been enough in certain cases for a number to heal its "spam likely" status. Making unsolicited calls is how numbers get flagged as "spam likely" to begin with.
4. **Push to the specific carrier** that is flagging your calls. The [USTelecom ITG contact page](https://www.ustelecom.org/the-industry-traceback-group-itg/call-labeling-and-blocking-points-of-contact/) provides contact information and forms for each terminating carrier.

### US Carrier Call Blocking

Major US carriers actively flag or block calls deemed potentially fraudulent. End users may see labels such as "Fraud Risk", "Spam Risk", "Potential Spam", "Robocaller", or "Scam Likely" prepended onto caller IDs. High-volume calls from non-rotated caller IDs are experiencing higher amounts of user busy responses in the form of SIP 480/486 Busy Here. In some cases, destination carriers use services that categorise calls as "Potential Spam" on user devices.

### SIP 608 Rejected

SIP Code 608 indicates that the terminating carrier has blocked a call due to suspected fraud, preventing it from reaching the intended end user:

- **Not Used by All Carriers:** The 608 code is not universally used, but it has been observed with major wireless carriers. Other 6XX errors may also appear.
- **Under FCC Review:** The 608 code is currently under FCC review. A 603+ variance may be introduced in the future, potentially replacing the 608 code.
- **Signifies Call Blocking:** A SIP Code 608 means the call was rejected before reaching its destination because the terminating provider suspects fraud.
- **Suspicious Traffic and Corrective Measures:** Multiple instances of SIP Code 608 suggest suspicious traffic that needs correction. Register with the Free Caller Registry and push to the specific carrier that is flagging your calls.

### STIR/SHAKEN

Telnyx is committed to combating spoofing and illegal robocalling through implementing the industry-wide STIR/SHAKEN solution. See the [STIR/SHAKEN explained article](https://telnyx.com/resources/shaken-stir-explained) for implementation details.
