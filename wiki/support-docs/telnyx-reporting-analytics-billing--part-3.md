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

*Part 3 of 5 — see also: [Part 1](telnyx-reporting-analytics-billing--part-1.md), [Part 2](telnyx-reporting-analytics-billing--part-2.md), [Part 4](telnyx-reporting-analytics-billing--part-4.md), [Part 5](telnyx-reporting-analytics-billing--part-5.md)*

This page consolidates Telnyx's reporting, analytics, and billing-related documentation, covering the Mission Control Portal Reporting section (Detail Records, Usage Reports, Monthly Charges, Message Deliverability, Outbound Declined Calls, and On-Demand Reports), per-product detail records (MDRs for SMS, WDRs for Wireless), real-time dashboards, Calls Per Second (CPS) limits and surcharges, short duration call penalties, abandoned call surcharges, post dial delay, and the Telnyx Status Page.

## Calls Per Second (CPS) Limits

CPS limits protect the Telnyx voice network and customer traffic from sudden bursts that could overload SIP proxies, B2BUAs, downstream carriers, or customer systems. Limits are enforced in real time — when outbound SIP traffic exceeds the applicable limit, Telnyx may reject excess SIP requests with a SIP 503 response and a CPS-limit response reason, for example:

```
SIP/2.0 503 CPS Limit reached P05
```

### Why CPS Limits Are Applied

CPS limits help ensure voice traffic remains stable and reliable by:

- Protecting shared SIP infrastructure from sudden bursts of call attempts
- Preventing a single customer or endpoint from consuming disproportionate proxy or media-routing capacity
- Reducing the risk of cascading failures during traffic spikes
- Encouraging controlled retry behavior from PBXs, dialers, and SIP applications
- Maintaining service quality for both high-volume customers and normal production traffic

CPS limits are not intended to restrict legitimate high-volume use cases. Customers with approved higher-volume requirements may be eligible for custom CPS limits.

### How CPS Limits Are Applied

On the standard SIP Trunking proxy path, outbound SIP INVITE requests are limited by default to 20 calls per second (CPS) from the same source IP address. For credential-authenticated traffic, Telnyx also enforces CPS limits per SIP username to prevent customers from exceeding the intended limit by distributing traffic across multiple source IP addresses using the same SIP credentials.

CPS enforcement may apply across multiple dimensions, including source IP address, SIP username (for credential-authenticated traffic), customer-specific CPS overrides, and global protection limits on Telnyx proxy infrastructure. Some traffic profiles or approved high-volume deployments may use different CPS limits — contact Telnyx Support or your account team to review options.

### Dials Per Second vs. SIP INVITEs Per Second

Dials per second (DPS) refers to the API rate limits applied to Programmable Voice Dial command requests. This is a Programmable Voice / Call Control concept and is separate from SIP Trunking CPS limits.

SIP INVITEs per second refers to the number of SIP INVITE requests received by the Telnyx SIP infrastructure each second. This is the metric used for real-time SIP Trunking CPS enforcement because limits are enforced at the SIP signaling layer.

A single dial typically generates one outbound SIP INVITE toward Telnyx, but CPS enforcement is based on the number of SIP INVITE requests received, not the number of logical dials. This can happen when a PBX or dialer rapidly retries failed attempts, SIP retransmissions occur due to network issues, multiple PBXs/SBCs/application workers send traffic simultaneously, or routing/call-forking logic generates multiple SIP INVITE requests for a single intended call. Customers should monitor the rate of SIP INVITE requests sent to Telnyx, not only the number of logical dials initiated.

### How CPS Is Calculated for Real-Time Limits

Telnyx evaluates outbound SIP INVITE traffic over short time intervals, typically one second. On the standard SIP Trunking proxy path, Telnyx determines whether the number of outbound SIP INVITE requests exceeds the applicable CPS limit for the relevant source (source IP address or SIP username). If the limit is exceeded during the enforcement interval, excess SIP INVITE requests may be rejected with a SIP 503 response and a CPS-limit response reason.

Example:

```
Default limit: 20 SIP INVITEs from the same source IP per second
Observed traffic: 35 SIP INVITEs from the same source IP in one second
Result: 15 SIP INVITEs will be rejected with SIP 503 CPS Limit reached P05
```

### Identifying CPS Limit Events

When an outbound SIP INVITE is rejected because of CPS limiting, the response is:

```
SIP/2.0 503 CPS Limit reached P05
```

If this response appears in a SIP trace, packet capture, PBX log, SBC log, or dialer log, the applicable CPS limit was reached. Before contacting Telnyx Support, collect:

- Approximate timestamp and timezone of the failed attempts
- Source IP address used to send the SIP traffic
- SIP username, if using credential authentication
- SIP Call-ID values for failed examples, if available
- SIP traces, packet captures, or PBX/SBC logs showing the 503 response
- Estimated dials per second and SIP INVITEs per second at the time

### Best Practices to Avoid CPS Limit Rejections

- Spread outbound call attempts more evenly over time
- Avoid launching large dialer batches simultaneously
- Add pacing or rate limiting to the PBX, dialer, or application
- Avoid aggressive retry loops after failures
- Monitor SIP INVITE requests per second, not only successful calls or logical dials
- Coordinate with Telnyx before planned high-volume campaigns or traffic spikes

### Requesting a CPS Increase

Request a CPS increase before sending planned high-volume production traffic to Telnyx — especially for new campaigns, contact center launches, traffic migrations, seasonal events, or any expected increase in outbound call attempts. Before submitting, review current outbound traffic and estimate future requirements, including normal and peak traffic periods, expected future volume and reason for the increase, source IP addresses and SIP usernames that will originate traffic, traffic type and destination profile, and evidence that the current CPS limit has been reached (such as SIP traces or logs showing 503 CPS Limit reached P05). Submit the request through Telnyx Support or your account team.
