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

*Part 4 of 5 — see also: [Part 1](telnyx-regulatory-compliance-reference--part-1.md), [Part 2](telnyx-regulatory-compliance-reference--part-2.md), [Part 3](telnyx-regulatory-compliance-reference--part-3.md), [Part 5](telnyx-regulatory-compliance-reference--part-5.md)*

A consolidated reference for Telnyx customers covering U.S. and state regulatory requirements, FCC compliance programs (STIR/SHAKEN, RMD, RND, DNO), Telnyx security certifications, traffic surcharges, and number lifecycle policies that affect voice and messaging services.

## Calls Per Second (CPS) Limits and Surcharges

Telnyx uses Calls Per Second (CPS) in two related but separate ways: real-time outbound CPS limits that protect the network, and a monthly outbound peak CPS surcharge that applies charges for sustained or recurring high outbound CPS usage.

### Real-Time Outbound CPS Limits

CPS limits protect the Telnyx voice network and customer traffic from sudden traffic bursts that could overload SIP proxies, B2BUAs, downstream carriers, or customer systems. Limits are enforced in real time. When outbound SIP traffic exceeds the applicable CPS limit, Telnyx may reject excess SIP requests with a SIP 503 response and a CPS-limit response reason, for example:

```
SIP/2.0 503 CPS Limit reached P05
```

On the standard SIP Trunking proxy path, outbound SIP INVITE requests are limited by default to **20 calls per second (CPS)** from the same source IP address. For credential-authenticated traffic, Telnyx also enforces CPS limits per SIP username to prevent customers from exceeding the intended limit by distributing traffic across multiple source IP addresses while using the same SIP credentials. Enforcement may apply across source IP address, SIP username, customer-specific CPS overrides, and global protection limits on Telnyx proxy infrastructure. Customers with approved higher-volume requirements may be eligible for custom CPS limits.

#### Dials Per Second vs. SIP INVITEs Per Second

Dials per second (DPS) refers to the API rate limits applied to Programmable Voice [Dial](https://developers.telnyx.com/api-reference/call-commands/dial#dial) command requests and is separate from SIP Trunking CPS limits. SIP INVITEs per second refers to the number of SIP INVITE requests received by the Telnyx SIP infrastructure each second and is the metric used for real-time SIP Trunking CPS enforcement. A single dial typically generates one outbound SIP INVITE, but CPS enforcement is based on the number of SIP INVITE requests received, not the number of logical dials initiated. Customers should monitor the rate of SIP INVITE requests sent to Telnyx, not only the number of logical dials initiated by their application.

#### Identifying CPS Limit Events

When an outbound SIP INVITE is rejected because of CPS limiting, the response is:

```
SIP/2.0 503 CPS Limit reached P05
```

If this response appears in a SIP trace, packet capture, PBX log, SBC log, or dialer log, the applicable CPS limit was reached for that traffic. Before contacting Telnyx Support, collect the approximate timestamp and timezone, source IP address, SIP username (if using credential authentication), SIP Call-ID values for failed examples, SIP traces or logs showing the 503 response, and the estimated dials per second and SIP INVITEs per second at the time.

#### Best Practices

To reduce the likelihood of reaching CPS limits, spread outbound call attempts more evenly over time, avoid launching large dialer batches simultaneously, add pacing or rate limiting to the PBX, dialer, or application, avoid aggressive retry loops after failures, monitor SIP INVITE requests per second (not only successful calls or logical dials), and coordinate with Telnyx before planned high-volume campaigns or traffic spikes.

#### Requesting a CPS Increase

Request a CPS increase before sending planned high-volume production traffic to Telnyx, especially for new campaigns, contact center launches, traffic migrations, seasonal events, or any expected increase in outbound call attempts. Useful information to provide includes current outbound SIP traffic patterns (normal and peak), expected future traffic volume and the reason for the increase, source IP addresses and SIP usernames that will originate traffic, traffic type and destination profile, and evidence that the current CPS limit has already been reached (such as SIP traces or logs showing 503 CPS Limit reached P05). Submit the request through Telnyx Support or the account team.

### Monthly Outbound Peak CPS Surcharge

The Monthly Outbound Peak CPS surcharge is calculated independently of the real-time CPS limits. It is based only on outbound SIP Trunking call attempts that were accepted, and is measured at the account level, not by IP address or SIP username. The Monthly Outbound Peak CPS represents the highest number of outbound SIP Trunking call attempts initiated during the same second throughout the month, as derived from SIP Trunking CDRs. The following traffic is excluded from the surcharge calculation: Programmable Voice / Call Control traffic, Telnyx internal retry attempts, and SIP Trunking attempts blocked by CPS limits.

#### Monitoring

The Mission Control Portal includes an [Outbound Peak Calls Per Second (CPS) dashboard](https://portal.telnyx.com/#/voice/dashboard) to help monitor traffic patterns.

![Outbound Peak CPS dashboard](_images/46580913345880db.png)

#### How Monthly CPS Peak Usage Is Measured

For each active hour during the billing month, Telnyx identifies the highest outbound SIP Trunking CPS value recorded within that hour. These hourly peak values form the dataset used to calculate the monthly CPS Peak. Hours with no outbound SIP Trunking call attempts are excluded from the calculation rather than being counted as 0 CPS. The monthly CPS Peak surcharge is based on the **95th percentile** of the active hourly peak CPS values, reflecting sustained or recurring periods of high outbound CPS usage rather than a single exceptional burst or the customer's average CPS throughout the month.

#### Calculation

Each month, Telnyx calculates the CPS Peak value as follows:

1. For each active hour, determine the highest outbound CPS value recorded during that hour.
2. Exclude hours with no outbound CPS activity.
3. Calculate the 95th percentile of the remaining hourly peak CPS values.
4. Use the resulting 95th percentile CPS value to calculate the monthly surcharge.

For example, if a customer has 100 active hours in a month and only 5 hours contain unusually high CPS peaks, those hours are treated as outliers and have little effect on the 95th percentile calculation. If elevated CPS levels occur across many more active hours, the monthly CPS Peak value increases because the pattern represents sustained usage rather than isolated events.

#### Pricing Model

CPS Peak surcharges use a graduated pricing model:

- First 5 CPS = free
- Any additional CPS up to 25 = $12/CPS
- Any additional CPS up to 200 = $16/CPS
- Any additional CPS up to 250 = $24/CPS
- Any additional CPS 251+ = $30/CPS

For example, if the monthly 95th percentile peak CPS value is 163, the surcharge is calculated as:

(5 CPS × $0) + (20 CPS × $12) + (138 CPS × $16) = $2,448

CPS surcharges appear on the monthly invoice as an "Outbound Calls-Per-Second Peak Usage Surcharge."
