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

*Part 1 of 5 — see also: [Part 2](telnyx-voice-services-overview--part-2.md), [Part 3](telnyx-voice-services-overview--part-3.md), [Part 4](telnyx-voice-services-overview--part-4.md), [Part 5](telnyx-voice-services-overview--part-5.md)*

This page consolidates Telnyx support documentation covering company locations, voice termination coverage, call completion (local and rural), rate sheets and LRN-based pricing, N11 and emergency dialing, inbound call screening, and PSTN replacement / local calling features.

## Company Locations

Telnyx was founded in 2009 and is headquartered in Austin, Texas, with additional offices in Denver, Dublin, and Amsterdam. The mailing address is:

600 Congress Avenue
14th Floor
Austin, TX 78701

Telnyx also has remote employees working around the globe.

## Voice Termination Coverage

Telnyx offers termination in every country. International termination pricing can be accessed through the [Telnyx Portal](https://portal.telnyx.com/#/pricing/voice) once you have a Mission Control account. To create an account, provide your email address and a few additional details.

## Rate Change Notifications

Whenever a Telnyx rate changes, customers receive a brief rate update email. Telnyx sends these notifications to all customers any time rates change, so there is no need to actively monitor for updates.

## Rate Sheets and LRN-Based Pricing

Call rates are based on the Location Routing Number (LRN), not always the number dialed. In rare cases where the LRN and the dialed number do not match, the LRN destination prefix determines the cost.

To find the LRN of a number, use the Lookup tool in the Mission Control Portal. Enter the number and the tool returns the associated LRN prefix, which should be used to look up the correct rate on the Rate Sheets.

For example, numbers with the prefix +1 941 529 have an LRN beginning with +1 813 568. Because rates are based on the LRN, the applicable pricing is listed under the +1 813 568 destination prefix, not the original number. See [Your Number Lookup Guide](your-number-lookup-guide.md) for more on the Lookup tool.

## Updates to the Global Conversational Rate Deck

Telnyx is introducing changes to its Global Conversational rate deck over the coming months. These changes affect:

- Classification of origination types
- Prefixes and prefix descriptions
- Rate pricing and frequency of updates

The changes apply to users on both the Global Conversational outbound voice profile rate deck and Default Pricing (which applies when a business has no committed usage or contracted rates). Changes are being introduced in batches of countries outside of the United States and Canada.

### Why the changes are happening

Telnyx rates are derived from cost basis, so rates must be adjusted in response to changes in wholesale and/or local markets.

### Change notifications

Customers on either the Global Conversational rate deck or default pricing are notified of future changes via email to the address associated with their Mission Control Portal account. Each notification is sent 3 days before the change goes live. Accounts with no outbound usage in the 30 days prior to a change are not notified.

### Origination type classifications

Four origination types are in scope:

- **Local origination** — A call to a specific country using a phone number of that country as the originating CLI, where the number was purchased on the Telnyx platform. Calls using a CLI not purchased from Telnyx are not considered local. Example: a French number (+33) purchased on Telnyx calling another French number (+33).
- **EEA (European Economic Area) origination** — A call to a country within the EEA using a phone number of another EEA country as the CLI. Example: a call to a Spanish number (+34) from an Irish number (+353).
- **Non-surcharged origination** — A call to country X using a phone number of country Z as the CLI, where country Z belongs to a predefined set. The set differs per destination country and is listed in the "Origination Prefixes" column of the rate deck.
- **Surcharged origination** — Applies when none of the above scenarios apply. Consult the rate deck for details.

### Prefixes and prefix descriptions

Changes to prefixes and prefix descriptions depend on the country. In some cases descriptions become more granular; in others, more compact. Customers are notified of updates that affect their communications per the timeline above.

### Rate pricing and update frequency

Because costs of service in wholesale and local markets change more frequently, customers should expect rate changes to occur more often. Rates do not always go up — when cost basis decreases, sell rates are adjusted accordingly. For fixed rates, contact the [Telnyx sales team](https://telnyx.com/contact-us).
