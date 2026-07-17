---
title: 'Telnyx Voice: Caller ID, Call Completion, and Pricing'
summary: A consolidated reference for Telnyx voice services covering Caller ID Number
  (CID) and Caller ID Name (CNAM) configuration, the Caller ID Number Policy, pricing
  and billing, LRN and number lookup, US local and rural call completion, PSTN replacement
  and local calling, and troubleshooting inbound and outbound call failures.
sources:
- url: https://support.telnyx.com/en/articles/1130656-set-up-inbound-caller-id-name-incoming
- url: https://support.telnyx.com/en/articles/1130720-caller-id-outbound-vs-cnam
- url: https://support.telnyx.com/en/articles/13795700-accessing-canadian-lrn-data
- url: https://support.telnyx.com/en/articles/2185372-where-can-i-see-pricing-options
- url: https://support.telnyx.com/en/articles/3317613-billing-decimal-values-considered
- url: https://support.telnyx.com/en/articles/3546251-caller-id-number-policy
- url: https://support.telnyx.com/en/articles/4096828-us-rural-call-completion
- url: https://support.telnyx.com/en/articles/4378813-us-local-call-completion
- url: https://support.telnyx.com/en/articles/5025298-troubleshooting-call-completion
- url: https://support.telnyx.com/en/articles/5073043-the-rate-sheet-and-lrn-explained
- url: https://support.telnyx.com/en/articles/6622229-pstn-replacement-local-calling-with-telnyx
updated_at: 2026-07-17T09:05:14Z
---

# Telnyx Voice: Caller ID, Call Completion, and Pricing

*Part 3 of 5 — see also: [Part 1](telnyx-voice-caller-id-call-completion-and-pricing--part-1.md), [Part 2](telnyx-voice-caller-id-call-completion-and-pricing--part-2.md), [Part 4](telnyx-voice-caller-id-call-completion-and-pricing--part-4.md), [Part 5](telnyx-voice-caller-id-call-completion-and-pricing--part-5.md)*

A consolidated reference for Telnyx voice services covering Caller ID Number (CID) and Caller ID Name (CNAM) configuration, the Caller ID Number Policy, pricing and billing, LRN and number lookup, US local and rural call completion, PSTN replacement and local calling, and troubleshooting inbound and outbound call failures.

## US Call Completion

### US Local Call Completion

After purchasing or porting a local number for a client in a particular rate center, callers within the same rate center or state may receive intercept recordings such as "The number you have dialed cannot be completed at this time, please check the number and try again." Like rural call completion issues, these local failures are often the byproduct of how local carriers route calls, typically following the least-cost routing model.

A typical local call flow is:

**Originating Carrier → Downstream Tandem → LEC → Upstream Tandem → Destination Carrier**

- **Originating Carrier**: the carrier of the calling party.
- **Downstream Tandem**: the interconnect the originating carrier uses to access the PSTN over TDM.
- **LEC**: the local exchange carrier (ILEC or CLEC) that owns the local telecoms equipment on the PSTN.
- **Upstream Tandem**: the interconnect Telnyx uses to access the PSTN and receive calls over IP.
- **Destination Carrier**: the carrier of the receiving party (Telnyx in this case).

Key terms:

- **LERG** (Local Exchange Routing Guide): a database managed by NPAC Iconectiv providing information regarding owned NPA-NXX at the block level. Updated monthly.
- **LATA** (Local Access Transport Area): the geographic area in which numbers are routed. LATAs typically do not cross states, but states can have multiple LATAs.
- **LRN** (Location Routing Number): a unique identification phone number that tells the industry how to route calls through the PSTN. Each carrier has at least one LRN per LATA. Created to support local number portability.
- **LNP** (Local Number Portability): the ability to retain a local phone number when switching carriers.
- **NPA** (Number Planning Area): a 3-digit area code. Calls to ported or pooled numbers are routed based on the NPA-NXX of the number's associated LRN.
- **Rate Center**: a geographical area used to determine boundaries for local calling, billing, and assigning phone numbers; can encompass multiple area codes.

When Telnyx loads numbers for customers, the numbering team ensures each NPA-NXX is assigned a particular LRN, which is broadcast to the industry via NPAC Iconectiv. Telnyx also provides NPA-NXX blocks and LRN information to upstream tandems so they can load the information into their switches.

Call completion issues are typically caused by translation issues, which usually occur after porting out or at tandem switches:

- **Porting Out**: the originating (losing) carrier has not removed old routing information from their network, so subscribers' calls never reach the new destination's network. Legacy telco providers can take at least one hour post-port-out to update routing information across their network.
- **Tandem Switches**: the downstream or upstream tandem provider has not mapped Telnyx's LRN's NPA-NXX correctly.

These issues typically occur only when Telnyx launches numbers in new markets or spins up new number blocks, and most carriers experience similar issues because not every carrier has the most up-to-date routing information.

Telnyx maintains "seasoned" LRNs that increase the likelihood of connectivity because carriers are familiar with the routing information, and has redundant coverage in most LATAs. LRNs can be updated between tandems in case of issues with tandem providers.

To report local US calling issues, contact [support@telnyx.com](mailto:support@telnyx.com) or call **+1.888.980.9750**. Include a description of the issue, from/to telephone numbers, date and time (with timezone) of the call, and any error messages the callers heard. Ideally, call examples are within 48 hours of occurrence and reproducible.

### US Rural Call Completion

Long-distance calls to rural areas of the United States can be frustrating for both callers and callees. Common symptoms include dead air, prolonged ringing, or recordings such as "Your call cannot be completed as dialed, please check the number and try again." These issues are often the byproduct of how long-distance carriers route calls, typically following the least-cost routing model.

To report rural call completion concerns, contact [support@telnyx.com](mailto:support@telnyx.com) or call **+1.888.980.9750**. Provide:

- A description of the issue or concern.
- From and To telephone numbers.
- Date and time (including timezone) of the call.
- A description of any testing the rural carrier has already conducted with their customer.
- Any contact information for a rural carrier representative.
