---
title: Grandstream Device Setup and Telnyx Rate Change Notifications
summary: This page consolidates Telnyx setup guides for several Grandstream devices
  (DP752, GRP260x, GRP2612, GXP1700, and GXV3370) along with information about how
  Telnyx notifies customers of rate changes and upcoming updates to the Global Conversational
  rate deck. Each device section walks through prerequisites, SIP trunk configuration,
  codec settings, and account setup, while the rate change sections explain notification
  timelines, origination type classifications, and pricing update frequency.
sources:
- url: https://support.telnyx.com/en/articles/1130658-how-do-i-know-if-a-rate-has-changed
- url: https://support.telnyx.com/en/articles/5808368-grandstream-dp752
- url: https://support.telnyx.com/en/articles/6169513-grandstream-grp260x-sip-trunk
- url: https://support.telnyx.com/en/articles/6184147-grandstream-grp2612-sip-trunk
- url: https://support.telnyx.com/en/articles/6184520-grandstream-gxp1700-sip-trunk
- url: https://support.telnyx.com/en/articles/6187576-grandstream-gxv3370
- url: https://support.telnyx.com/en/articles/6974437-updates-to-global-conversational-rate-deck
updated_at: 2026-07-17T09:05:40Z
---

# Grandstream Device Setup and Telnyx Rate Change Notifications

*Part 6 of 6 — see also: [Part 1](grandstream-device-setup-and-telnyx-rate-change-notifications--part-1.md), [Part 2](grandstream-device-setup-and-telnyx-rate-change-notifications--part-2.md), [Part 3](grandstream-device-setup-and-telnyx-rate-change-notifications--part-3.md), [Part 4](grandstream-device-setup-and-telnyx-rate-change-notifications--part-4.md), [Part 5](grandstream-device-setup-and-telnyx-rate-change-notifications--part-5.md)*

This page consolidates Telnyx setup guides for several Grandstream devices (DP752, GRP260x, GRP2612, GXP1700, and GXV3370) along with information about how Telnyx notifies customers of rate changes and upcoming updates to the Global Conversational rate deck. Each device section walks through prerequisites, SIP trunk configuration, codec settings, and account setup, while the rate change sections explain notification timelines, origination type classifications, and pricing update frequency.

## Updates to the Global Conversational Rate Deck

Over the coming months, Telnyx is introducing changes to its **Global Conversational** rate deck. These changes affect:

- Classification of origination types
- Prefixes and prefix descriptions
- Rate pricing and frequency of updates

These upcoming changes apply to Telnyx users on both the **Global Conversational** outbound voice profile rate deck and **Default Pricing** (which applies if your business does not have committed usage or contracted rates). Changes have been—and will continue to be—introduced in batches of countries outside of the United States and Canada.

### Why is Telnyx making these changes?

As Telnyx rates are derived from its cost basis, rates must be adjusted in response to rate changes in wholesale and/or local markets.

### Classification of Origination Types

There are 4 origination types in scope of this change: Local, EEA, Non-surcharged, and Surcharged.

#### Local origination

Local origination applies when a call is made to a specific country with a phone number of that country as an originating number (CLI), that was purchased on the Telnyx platform. If you use an originating number that is NOT purchased from Telnyx, that call is NOT considered local.

*Example:* Purchasing a French number (+33) on the Telnyx platform and placing a call to another French number (+33) from that CLI.

#### EEA (European Economic Area) origination

EEA origination applies when a call is made to a country within the EEA with a phone number of another country within the EEA as the originating number (CLI).

*Example:* Making a call to a Spanish number (+34) from an Irish number (+353).

#### Non-surcharged origination

Non-surcharged origination applies when a call is made to country X with a phone number of country Z as the originating number (CLI), where country Z belongs to a set of predefined countries. This set of predefined countries is different for each applicable country X and can be obtained from the "Origination Prefixes" column in the rate deck.

#### Surcharged origination

Surcharged origination applies when none of the above three scenarios apply to your call. In this case, consult your rate deck for more details.

### Prefixes and Prefix Descriptions

Changes to prefixes and prefix descriptions depend on the country in question. In some cases, prefix descriptions will be expanded and more granular; in others, they will become more compact. You will be notified of updates to prefixes and prefix descriptions that affect your communications as per the standard notification timeline.

### Rate Pricing and Frequency of Updates

As a result of the increased frequency of changes to Telnyx's costs of service in wholesale and local markets where it does business, customers should expect rate changes to be more frequent.

### FAQ

**Q: Do rates always go up?**

A: No. Telnyx bases its sell rates on its cost basis in the wholesale and/or local market. When that cost basis goes down, rates are adjusted accordingly.

**Q: Is there a way I can get fixed rates with Telnyx?**

A: [Reach out](https://telnyx.com/contact-us) to the sales team to talk about custom outbound rates.
