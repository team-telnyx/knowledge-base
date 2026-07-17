---
title: Telnyx Reporting, Analytics & Billing
summary: This page consolidates Telnyx's reporting, analytics, and billing-related
  documentation, covering the Mission Control Portal Reporting section (Detail Records,
  Usage Reports, Monthly Charges, Message Deliverability, Outbound Declined Calls,
  and On-Demand Reports), per-product detail records (MDRs for SMS, WDRs for Wireless),
  real-time dashboards, Calls Per Second (CPS) limits and surcharges, short duration
  call penalties, abandoned call surcharges, post dial delay, and the Telnyx Status
  Page.
sources:
- url: https://support.telnyx.com/en/articles/1130611-understand-telnyx-sms-mdr-report-log
- url: https://support.telnyx.com/en/articles/1130707-what-are-short-duration-calls
- url: https://support.telnyx.com/en/articles/1130708-how-to-download-reports-at-telnyx
- url: https://support.telnyx.com/en/articles/12805746-surcharge-for-high-abandoned-call-rates
- url: https://support.telnyx.com/en/articles/15668484-calls-per-second-cps-limits
- url: https://support.telnyx.com/en/articles/3679913-sim-reporting-analytics
- url: https://support.telnyx.com/en/articles/4305547-reporting-overview
- url: https://support.telnyx.com/en/articles/4307059-telnyx-dashboards
- url: https://support.telnyx.com/en/articles/4424926-reporting-detail-requests
- url: https://support.telnyx.com/en/articles/4425016-reporting-usage-reports
- url: https://support.telnyx.com/en/articles/4425088-reporting-monthly-charges
- url: https://support.telnyx.com/en/articles/4453840-post-dial-delay-pdd
- url: https://support.telnyx.com/en/articles/6707731-telnyx-status-page
- url: https://support.telnyx.com/en/articles/6969802-message-deliverability-dashboard
- url: https://support.telnyx.com/en/articles/7834487-calls-per-second-cps-surcharge
updated_at: 2026-07-17T09:02:33Z
---

# Telnyx Reporting, Analytics & Billing

*Part 5 of 5 — see also: [Part 1](telnyx-reporting-analytics-billing--part-1.md), [Part 2](telnyx-reporting-analytics-billing--part-2.md), [Part 3](telnyx-reporting-analytics-billing--part-3.md), [Part 4](telnyx-reporting-analytics-billing--part-4.md)*

This page consolidates Telnyx's reporting, analytics, and billing-related documentation, covering the Mission Control Portal Reporting section (Detail Records, Usage Reports, Monthly Charges, Message Deliverability, Outbound Declined Calls, and On-Demand Reports), per-product detail records (MDRs for SMS, WDRs for Wireless), real-time dashboards, Calls Per Second (CPS) limits and surcharges, short duration call penalties, abandoned call surcharges, post dial delay, and the Telnyx Status Page.

## Surcharge for High Abandoned Call Rates

Starting 1 November 2025, Telnyx applies surcharges to outbound traffic with high abandoned call rates to reduce misuse and keep the network reliable. If more than 20% of outbound calls are dropped by the originating side before being answered, an abandoned call surcharge of $0.005 per abandoned call applies.

### What Counts as an Abandoned Call

Whenever the originating user initiates the call disconnection during the ringing/call set-up process, the call is considered abandoned. Any call hung up by the caller while the call is connecting or still ringing counts. Calls to disconnected numbers also count as abandoned.

### Why This Is Being Done

Telnyx has seen an increase in traffic where numbers are called briefly and dropped. This kind of usage doesn't reflect typical calling behavior, utilizes network resources, puts additional strain on systems, and impacts other customers. The update helps keep capacity available for legitimate traffic.

### What Customers Need to Do

If an account might have more than 20% outbound calls being abandoned:

1. Review outbound traffic patterns
2. Adjust any systems that place brief or validation-style calls
3. Keep the abandoned call rate below 20% to avoid charges

### Tracking Abandoned Call Percentage

There are two options to track abandoned call percentage:

1. A new pie chart in the dashboard page shows abandoned vs not abandoned calls in the reporting section of the portal.
2. Generate a Usage Report and filter for abandoned calls:
   - Go to Reporting > Usage Reports
   - Switch to the Advanced Version view
   - Select SIP Trunking as the product
   - Under dimensions, check Direction and Hangup Details
   - Under metrics, check Attempted
   - Filter by Direction = outbound
   - Breakout with `recv_cancel` contains abandoned calls

### Frequently Asked Questions

- **If an account had 21% abandoned calls, does the surcharge apply to the % that exceeds the threshold or all abandoned calls?** The surcharge applies to all abandoned calls, not just those exceeding the threshold. If an account makes 100 calls in one month and 21 are abandoned, the surcharge applies to all 21.
- **Does this apply to inbound or outbound or both?** Outbound only.
- **What is the rate charged if an account exceeds the 20% threshold?** $0.005 USD per call.

## Post Dial Delay (PDD)

Post Dial Delay (PDD) is experienced by the originating caller as the time from the sending of the final dialed digit to the point at which they hear ring tone or other in-band information. Where the originating network is required to play an announcement before completing the call, this definition of PDD excludes the duration of such announcements. For SIP, PDD is the time from sending the INVITE to receiving the first ringing response (for example, a SIP/2.0 180 Ringing response).

### Why PDD Occurs

PDD can occur for several reasons. The most prevalent is that the carrier of the number being dialed has not received an indication that the end user's device is ringing. PDD is widely experienced on wireless devices with low signal that are far from their provider's closest cell tower, so it takes longer for the connection to be established.

Most carriers consider anything under 7 seconds as an acceptable amount of PDD, and most will not troubleshoot PDD that is less than 7 seconds. Telnyx partners with Tier 1 carriers and interconnects across the world — better quality routes reduce the likelihood of delay. The Telnyx telephony operations team monitors and tests carriers and interconnects to ensure there are no underlying issues with call completion. If PDD over 7 seconds is experienced, contact support@telnyx.com to verify whether there is an underlying issue and work with internal teams to further optimize routes.

## Telnyx Status Page

The Telnyx Status Page provides real-time updates on incidents and maintenance schedules, available at https://status.telnyx.com/. Updates can be subscribed to in real time through multiple channels.
