---
title: Telnyx Voice Services Overview
summary: This page consolidates Telnyx support documentation covering company locations,
  voice termination coverage, call completion (local and rural), rate sheets and LRN-based
  pricing, N11 and emergency dialing, inbound call screening, and PSTN replacement
  / local calling features.
sources:
- url: https://support.telnyx.com/en/articles/1130646-where-is-telnyx-located
- url: https://support.telnyx.com/en/articles/1130658-how-do-i-know-if-a-rate-has-changed
- url: https://support.telnyx.com/en/articles/1130664-countries-that-telnyx-offers-termination-in
- url: https://support.telnyx.com/en/articles/13795700-accessing-canadian-lrn-data
- url: https://support.telnyx.com/en/articles/4096828-us-rural-call-completion
- url: https://support.telnyx.com/en/articles/4378813-us-local-call-completion
- url: https://support.telnyx.com/en/articles/4567969-united-states-n11-codes
- url: https://support.telnyx.com/en/articles/5073043-the-rate-sheet-and-lrn-explained
- url: https://support.telnyx.com/en/articles/6622229-pstn-replacement-local-calling-with-telnyx
- url: https://support.telnyx.com/en/articles/6974437-updates-to-global-conversational-rate-deck
- url: https://support.telnyx.com/en/articles/8037040-inbound-call-screening
- url: https://support.telnyx.com/en/articles/8712528-dialing-emergency-services
- url: https://support.telnyx.com/en/articles/8797623-supported-emergency-numbers
- url: https://support.telnyx.com/en/articles/9039036-emergency-services-and-ipnd-in-australia
updated_at: 2026-08-05T13:30:13Z
---

# Telnyx Voice Services Overview

*Part 2 of 5 — see also: [Part 1](telnyx-voice-services-overview--part-1.md), [Part 3](telnyx-voice-services-overview--part-3.md), [Part 4](telnyx-voice-services-overview--part-4.md), [Part 5](telnyx-voice-services-overview--part-5.md)*

This page consolidates Telnyx support documentation covering company locations, voice termination coverage, call completion (local and rural), rate sheets and LRN-based pricing, N11 and emergency dialing, inbound call screening, and PSTN replacement / local calling features.

## US Local Call Completion

After purchasing or porting a local number for a client in a particular US rate center, customers sometimes report that other local callers within the same rate center or state receive intercept recordings (such as "The number you have dialed cannot be completed at this time") when dialing the client's number. Like [US Rural Call Completion](us-rural-call-completion.md), local calls across the United States — especially to VoIP numbers — can be a frustrating experience for both caller and callee. These issues are often the byproduct of how local carriers choose to route calls, typically following the least-cost routing model.

### US local calling components

A typical local call flow is:

Originating Carrier → Downstream Tandem → LEC → Upstream Tandem → Destination Carrier

- **Originating Carrier** — The carrier of the calling party.
- **Downstream Tandem** — The interconnect the originating carrier uses to access the PSTN over TDM.
- **LEC** — The local exchange carrier (ILEC or CLEC) that owns the local telecoms equipment on the PSTN and interconnects with many tandem providers.
- **Upstream Tandem** — The interconnect Telnyx uses to access the PSTN and receive calls over IP.
- **Destination Carrier** — The carrier of the receiving party (Telnyx in this case).

### Key terms

- **LERG** — Local Exchange Routing Guide. A database managed by NPAC Iconectiv that provides information regarding owned NPA-NXX at the block level. Updated monthly, it highlights call routing activity over the PSTN.
- **LATA** — Local Access Transport Area. The geographic area in which numbers are routed. LATAs typically do not cross states, but states can have multiple LATAs.
- **LRN** — Location Routing Number. A unique identification phone number that tells the industry how to route calls through the PSTN. Each carrier has at least one LRN per LATA. LRNs enable local number portability — only the LRN must change when a number moves carriers.
- **LNP** — Local Number Portability. The ability to retain a local phone number when switching carriers.
- **NPA** — Number Planning Area. Calls to ported or pooled numbers are routed based on the NPA-NXX of the number's associated LRN. The NPA is a 3-digit area code; a single NPA can be available in more than one rate center.
- **Rate Center** — A geographic area used to determine boundaries for local calling, billing, and assigning specific phone numbers. A rate center can encompass multiple area codes.

### How components relate

Carriers are typically assigned thousand-block NPA-NXX ranges they can provide to subscribers. When Telnyx loads numbers for customers to purchase, the numbering team ensures each NPA-NXX is assigned a particular LRN. This LRN is broadcast to the industry via NPAC Iconectiv, and Telnyx also provides NPA-NXX blocks and LRN information to upstream tandems so they can load the data into their switches.

Call completion issues are typically caused by translations issues, which usually occur after porting out or at tandem switches:

- **Porting Out** — The originating (losing) carrier has not removed old routing information from its network, so subscriber calls never reach the new destination network. Legacy telco providers can take at least one hour post-port-out to update routing across their network.
- **Tandem Switches** — Either the downstream or upstream tandem provider has not mapped Telnyx's LRN's NPA-NXX correctly.

These issues typically occur only when launching numbers in new markets or spinning up new number blocks, and affect most carriers because not every carrier has the most up-to-date routing information.

### Telnyx's solution

Telnyx maintains many "seasoned" LRNs, which increases the likelihood of connectivity because carriers are familiar with the routing information. Telnyx also has redundant coverage in most LATAs (and is expanding to all LATAs) and can update LRNs between tandems in case of tandem provider issues.

When the issue is not with Telnyx's tandem providers — and they have verified calls never reached their network from the PSTN — the cause may be intermittent, at the LEC, at the downstream tandem, or with the originating carrier. Outreach to originating carriers often yields CPNI compliance restrictions and requests for the subscriber to log a fault directly.

### Reporting local US calling issues

Contact Telnyx support by email at [support@telnyx.com](mailto:support@telnyx.com) or by phone at [+1.888.980.9750](tel:+18889809750). Include the following details (ideally within 48 hours of occurrence and reproducible):

- A description of the issue or concern
- From and To telephone numbers
- Date and time (including timezone) of the call
- Any error messages the callers heard that may indicate switching errors

## US Rural Call Completion

Long-distance calls to rural areas of the United States can be frustrating for both caller and callee. Common issues include dead air, prolonged ringing, or recordings such as "Your call cannot be completed as dialed, please check the number and try again." These issues are often the byproduct of how long-distance carriers choose to route calls, typically following the least-cost routing model.

### Solution for rural calling

Telnyx aims to connect people globally regardless of location. For rural call completion concerns, contact the rural call completion support team by email at [support@telnyx.com](mailto:support@telnyx.com) or by phone at +1 888 980 9750.

### Information to provide

To help the team investigate, include:

- A description of the issue or concern
- From and To telephone numbers
- Date and time (including timezone) of the call
- A description of any testing the rural carrier has already conducted with their customer to rule out local network, tandem, or end-user premise issues
- Contact information for a rural carrier representative so Telnyx can obtain more information, provide updates, or engage in troubleshooting or cooperative testing
