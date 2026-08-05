---
title: Caller ID, CNAM, and Branded Calling on Telnyx
summary: A consolidated reference covering how Telnyx handles Caller ID Number (CID),
  Caller ID Name (CNAM), Branded Calling, CLI/CLD validation, and related call-completion
  troubleshooting. It explains the differences between inbound and outbound CID and
  CNAM, how to configure each in Mission Control Portal, regional behavior in the
  US and Canada, supported number formats, anonymization, international spoofing restrictions,
  branded calling setup and limitations, and how to mitigate spam-likely flags and
  SIP errors.
sources:
- url: https://support.telnyx.com/en/articles/1130656-set-up-inbound-caller-id-name-incoming
- url: https://support.telnyx.com/en/articles/1130720-caller-id-outbound-vs-cnam
- url: https://support.telnyx.com/en/articles/15138152-making-calls-with-branded-calling
- url: https://support.telnyx.com/en/articles/3546251-caller-id-number-policy
- url: https://support.telnyx.com/en/articles/4088988-telnyx-how-to-handle-spam-scam-likely
- url: https://support.telnyx.com/en/articles/5025298-troubleshooting-call-completion
- url: https://support.telnyx.com/en/articles/6247033-cli-cld-validation-faq
updated_at: 2026-08-05T13:31:03Z
---

# Caller ID, CNAM, and Branded Calling on Telnyx

*Part 4 of 5 — see also: [Part 1](caller-id-cnam-and-branded-calling-on-telnyx--part-1.md), [Part 2](caller-id-cnam-and-branded-calling-on-telnyx--part-2.md), [Part 3](caller-id-cnam-and-branded-calling-on-telnyx--part-3.md), [Part 5](caller-id-cnam-and-branded-calling-on-telnyx--part-5.md)*

A consolidated reference covering how Telnyx handles Caller ID Number (CID), Caller ID Name (CNAM), Branded Calling, CLI/CLD validation, and related call-completion troubleshooting. It explains the differences between inbound and outbound CID and CNAM, how to configure each in Mission Control Portal, regional behavior in the US and Canada, supported number formats, anonymization, international spoofing restrictions, branded calling setup and limitations, and how to mitigate spam-likely flags and SIP errors.

## Handling Spam/Scam Likely Flags

If your phone number has been flagged as "Spam Likely":

1. **Register your phone number with the Free Caller Registry (FCR)** at [https://www.freecallerregistry.com/fcr/](https://www.freecallerregistry.com/fcr/).
2. **Add CNAM** — in Mission Control Portal, go to **Real-Time Communications → Numbers → Manage Numbers**, find the "spam likely" phone number, and click the pencil icon for advanced settings. In the advanced settings, enable **CNAM Listing** and add a custom name under the **Voice** tab. CNAM is not applicable for toll-free numbers. Having CNAM information is important to the engines that analyze and identify phone numbers as "spam likely".
3. **Be patient and start making calls** — wait for numbers to be aged. Aging time varies by carrier. There is no rule of thumb for aging length, but one week of healthy calls has been enough in certain cases for a number to heal its "spam likely" status. Making unsolicited calls is how numbers get flagged as "spam likely" to begin with.
4. **Push to the specific carrier** that is flagging your calls. The [USTelecom ITG Call Labeling and Blocking Points of Contact](https://www.ustelecom.org/the-industry-traceback-group-itg/call-labeling-and-blocking-points-of-contact/) page has a complete set of contact information and forms to submit to each terminating carrier.

### US Carrier Call Blocking

Major US carriers actively flag or block calls to their subscribers' devices, deeming them potentially fraudulent. End users may see labels such as "Fraud Risk", "Spam Risk", "Potential Spam", "Robocaller", or "Scam Likely" prepended onto caller IDs. High-volume calls from non-rotated caller IDs are experiencing a higher amount of user busy responses in the form of a SIP 480/486 Busy Here. In some cases, destination carriers use services that categorize calls as "Potential Spam" on user devices.

### SIP 608 Rejected

SIP Code 608 indicates that the terminating carrier has blocked a call due to suspected fraud, preventing it from reaching the intended end user. Key points:

- **Not used by all carriers** — the 608 code is not universally used, but it has been observed with major wireless carriers. Other 6XX errors may appear as well.
- **Under FCC review** — the 608 code is currently under review by the FCC, which may introduce a 603+ variance in the future.
- **Signifies call blocking** — the call was rejected before reaching its destination because the terminating provider believes the call is suspected fraud.
- **Suspicious traffic and corrective measures** — multiple instances of SIP Code 608 suggest suspicious traffic that needs to be corrected. Recommended steps include registering with the Free Caller Registry and pushing to the specific carrier that is flagging your calls.

### STIR/SHAKEN

Telnyx is committed to combating spoofing and illegal robocalling through implementing the industry-wide STIR/SHAKEN solution. See Telnyx's [STIR/SHAKEN explained](https://telnyx.com/resources/shaken-stir-explained) resources for more detail.
