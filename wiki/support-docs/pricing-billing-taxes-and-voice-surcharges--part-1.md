---
title: Pricing, Billing, Taxes, and Voice Surcharges
summary: A single guide to viewing Telnyx pricing, understanding how rates are determined
  and updated, how billing is calculated, which taxes and regulatory fees may apply,
  and how international spend limits and voice surcharges (CPS and abandoned calls)
  are assessed and monitored.
sources:
- url: https://support.telnyx.com/en/articles/1130658-how-do-i-know-if-a-rate-has-changed
- url: https://support.telnyx.com/en/articles/1130659-billing-increments
- url: https://support.telnyx.com/en/articles/2185372-where-can-i-see-pricing-options
- url: https://support.telnyx.com/en/articles/3317613-billing-decimal-values-considered
- url: https://support.telnyx.com/en/articles/5073043-the-rate-sheet-and-lrn-explained
- url: https://support.telnyx.com/en/articles/6420959-sales-gst-telecommunication-taxes-usf-fees-trf
- url: https://support.telnyx.com/en/articles/7834487-calls-per-second-cps-surcharge
- url: https://support.telnyx.com/en/articles/12805746-surcharge-for-high-abandoned-call-rates
- url: https://support.telnyx.com/en/articles/8228452-email-notification-international-spend-limit
- url: https://support.telnyx.com/en/articles/6974437-updates-to-global-conversational-rate-deck
updated_at: 2026-05-20T14:50:42Z
---

# Pricing, Billing, Taxes, and Voice Surcharges

*Part 1 of 2 — see also: [Part 2](pricing-billing-taxes-and-voice-surcharges--part-2.md)*

A single guide to viewing Telnyx pricing, understanding how rates are determined and updated, how billing is calculated, which taxes and regulatory fees may apply, and how international spend limits and voice surcharges (CPS and abandoned calls) are assessed and monitored.

## Viewing and adjusting pricing in Mission Control
- Go to the Pricing page in the Mission Control Portal from your account icon (top right). You can review pricing across five tabs: Voice, Numbers, Messaging, Telco Data, and Networking.
- Each tab includes a usage toggle so rates reflect your expected volume:
  - Voice: toggle bucketed monthly inbound (origination) minutes for Standard and Toll-Free DIDs.
  - Numbers: toggle quantity of phone numbers.
  - Messaging: toggle monthly message volumes.
  - Telco Data: view CNAM, LRN, and Switch Data pricing.
  - Networking: select Mbps bandwidth options.

## How rate changes are communicated
- Telnyx sends brief email notifications when rates change so you stay informed.
- For Global Conversational outbound voice profiles on Default Pricing, change notices are emailed 3 days before they go live. If an account has no outbound usage in the 30 days prior to a change, no notification is sent.

## Billing increments and decimal precision
- Telnyx uses 60/60 billing increments. Examples:
  - 11-second call → billed 60 seconds.
  - 96-second call → billed 120 seconds.
- International calling is billed in 60-second increments in most cases, but increments can vary by destination. Download international rates from the Portal for a country-by-country breakdown.
- Rates are calculated to 4 decimal places (e.g., $0.0025 per SMS). Call rates also consider 4 decimal places.
- 6-second billing increments are no longer offered.

## How rate sheets work: Destination Prefix vs LRN
- Rate sheets list a Destination Prefix, but pricing is based on the Location Routing Number (LRN) associated with the dialed number. In rare cases the dialed number’s prefix and its LRN prefix differ; the LRN determines the price.
- Use the Lookup tool in Mission Control to find a number’s LRN and match it to the correct prefix in the rate sheet before estimating cost.

## Global Conversational rate deck updates and origination types
- Telnyx is updating the Global Conversational rate deck in batches (outside the US and Canada) to refine:
  - Classification of origination types
  - Prefixes and their descriptions
  - Rate pricing and update frequency
- Origination types in scope:
  - Local: destination country called from a Telnyx-purchased originating number (CLI) in the same country. Using a non-Telnyx CLI is not Local.
  - EEA: a call to an EEA country from a different EEA-country CLI.
  - Non-surcharged: a call from a predefined set of origination countries for the given destination (see the Origination Prefixes column in the rate deck).
  - Surcharged: when none of the above apply (consult your rate deck).
- Rates track Telnyx’s cost basis in wholesale/local markets and may go up or down. Contact Sales for custom outbound rates.

## Taxes and regulatory fees in the United States
- Sales and telecommunication taxes
  - Telnyx collects applicable state, county, and municipal taxes where it has nexus, using your service address.
  - By default, the primary portal account address is used. You can add a distinct Service Address in Account Settings > Billing > Service Address in the Portal.
  - Tax amounts depend on service address, applicable regulations, products used, and your tax status.
  - Taxes are calculated daily and deducted from your balance the following day. Your monthly invoice shows a Summary line for total taxes plus a dedicated section with a tax-type breakdown.
  - Estimates aren’t available due to usage- and jurisdiction-based variability.
  - You can’t add a Tax ID/VAT in the Portal. Email support@telnyx.com with your account details and the tax registration number to add it to future invoices (past invoices won’t be regenerated).
  - For exemptions, email tax@telnyx.com with appropriate certificates. Address updates do not trigger retroactive invoice changes.
- USF (Universal Service Fund) fees
  - USF is a federal program funded as a percentage of end-user telecom revenues. Telnyx passes through USF fees on interconnected VoIP/telecom and Programmable Voice (US inbound/outbound) usage, where applicable.
  - USF shows as a dedicated line in the tax section of your invoice.
  - Providers filing FCC Form 499-A and contributing directly may qualify for exemption; email tax@telnyx.com. Exemptions must be renewed annually.
- TRS (Telecommunications Relay Service) fees
  - TRS funds relay services for individuals with hearing or speech challenges. Contributions are a percentage of end-user communications revenues and vary annually.
  - TRS applies similarly to USF (interconnected VoIP/telecom and Programmable Voice US inbound/outbound) and appears on invoices in the tax section.
  - 499-A filers may qualify for exemption; email tax@telnyx.com and renew annually.

## International spend limit notifications and enforcement
- Telnyx monitors international voice spend over rolling 24-hour periods. If combined international spend from SIP Connections or Voice API Applications exceeds $700, the account owner receives an email notification.
- Upon reaching the limit:
  - International calls are blocked for the account until reset; local (same-country) calling remains enabled.
  - Error response: 403 “International daily spent limit reached D39.”
  - The limit resets daily at 00:00 UTC.
- Telnyx Support can adjust this limit for your use case on request.
- International calls are outbound calls where the destination country differs from the origination country.
- To identify traffic driving spend, use Portal reporting: run a usage report broken down by connection; consider a detailed records report to see calling numbers and destinations; use the SIP call flow tool to trace source IPs.

## Calls per second (CPS) limits and monthly surcharges
- Enforced CPS limit: 20 outbound calls per second from the same IP address or SIP username for SIP Trunking. Calls exceeding the limit are rejected with 503 CPS limit. Telnyx can grant exceptions for justified use cases.
- Monitoring: the Outbound Peak CPS dashboard in Mission Control shows hourly peak attempts to help you spread load and avoid surcharges.
- 95th-percentile methodology (monthly):
  - Compute peak CPS in each hour.
  - Build a monthly dataset from hours with CPS > 0 (exclude zero hours).
  - The 95th-percentile value from this dataset is your billable peak CPS for surcharge calculation.
- Graduated monthly surcharge pricing (per CPS above thresholds):
  - First 5 CPS: free
  - >5 to 25 CPS: $12/CPS
  - >25 to 200 CPS: $16/CPS
  - >200 to 250 CPS: $24/CPS
  - 251+ CPS: $30/CPS
  Example: 95th-percentile CPS of 163 → (5×$0) + (20×$12) + (138×$16) = $2,448.
- Billing: the CPS surcharge appears as a line item on your monthly invoice. At this time, only SIP Trunking traffic is subject to CPS surcharges.

## Surcharge for high abandoned outbound call rates
- Policy: If more than 20% of your outbound calls are abandoned by the originator during ringing/call setup, a surcharge of $0.005 per abandoned call applies.
- Definition: An abandoned call is one the caller disconnects during setup/ringing; calls to disconnected numbers also count as abandoned. Applies to outbound only.
- Threshold application: Once the 20% threshold is exceeded in a period, the $0.005 fee applies to all abandoned calls (not just those above 20%).
- Monitoring:
  - Dashboard pie chart showing abandoned vs. not abandoned calls in Portal reporting.
  - Usage Report (Advanced): Product = SIP Trunking; Dimensions = Direction, Hangup Details; Metrics = Attempted; Filter Direction = outbound; Breakout where recv_cancel indicates abandoned.
- Recommendations: Review dialer logic or validation-call patterns to keep abandoned rates under 20%.
