---
source_url: https://support.telnyx.com/en/articles/15668484-calls-per-second-cps-limits
scraped: 2026-07-08
content_hash: 4fefa00a08c18143b2507c5082b93ff30ea8d22348fd5b332c6578ab74a84f40
---

Calls Per Second (CPS) Limits | Telnyx Help Center

[Skip to main content](#main-content)

# Calls Per Second (CPS) Limits

Calls Per Second Limits

Written by Telnyx Engineering

Updated over a week ago

Table of contents

This article explains how Telnyx applies Calls Per Second (CPS) limits for SIP Trunking traffic, why these limits exist, how CPS is measured, how to identify when a CPS limit has been reached, and the difference between dials per second and SIP INVITEs per second.

## **Overview**

Calls Per Second (CPS) limits protect the Telnyx voice network and customer traffic from sudden traffic bursts that could overload SIP proxies, B2BUAs, downstream carriers, or customer systems.

CPS limits are enforced in real time. When outbound SIP traffic exceeds the applicable CPS limit, Telnyx may reject excess SIP requests with a **SIP 503** response and a CPS-limit response reason, for example:

```
SIP/2.0 503 CPS Limit reached P05
```

## **Why Telnyx applies CPS limits**

CPS limits help ensure that voice traffic remains stable and reliable for all customers. They are used to:

* Protect shared SIP infrastructure from sudden bursts of call attempts.
* Prevent a single customer or endpoint from consuming disproportionate proxy or media-routing capacity.
* Reduce the risk of cascading failures during traffic spikes.
* Encourage controlled retry behavior from PBXs, dialers, and SIP applications.
* Maintain service quality for both high-volume customers and normal production traffic.

CPS limits are not intended to restrict legitimate high-volume use cases. Customers with approved higher-volume requirements may be eligible for custom CPS limits.

## **How CPS limits are applied**

On the standard SIP Trunking proxy path, outbound SIP INVITE requests are limited by default to **20 calls per second (CPS)** from the same source IP address.

For credential-authenticated traffic, Telnyx also enforces CPS limits per SIP username.   
This prevents customers from exceeding the intended limit by distributing traffic across multiple source IP addresses while using the same SIP credentials.

Depending on the traffic profile, CPS enforcement may apply across multiple dimensions, including:

* Source IP address
* SIP username (for credential-authenticated traffic)
* Customer-specific CPS overrides
* Global protection limits on Telnyx proxy infrastructure

Some traffic profiles or approved high-volume deployments may use different CPS limits.   
If your use case requires a higher CPS limit, contact Telnyx Support or your account team to review your traffic profile and available options.

## **Dials per second vs. SIP INVITEs per second**

When discussing CPS limits, it is important to distinguish between **dials per second (DPS)** and **SIP INVITEs per second**.

## **Dials per second (DPS)**

Dials per second (DPS) refers to the API rate limits applied to Programmable Voice **[Dial](https://developers.telnyx.com/api-reference/call-commands/dial#dial)** command requests.

This is a Programmable Voice / Call Control concept and is separate from SIP Trunking CPS limits.   
It is therefore outside the scope of this article and is not affected by SIP Trunking CPS limits.

## **SIP INVITEs per second**

SIP INVITEs per second refers to the number of SIP INVITE requests received by the Telnyx SIP infrastructure each second.

This is the metric used for real-time SIP Trunking CPS enforcement because limits are enforced at the SIP signaling layer.

## **Why this distinction matters**

A single dial typically generates one outbound SIP INVITE toward Telnyx. However, CPS enforcement is based on the number of SIP INVITE requests received by Telnyx, not simply the number of calls your application intended to place.

For example, a dialer may initiate 20 calls in one second, while the SIP equipment sending traffic to Telnyx generates more than 20 SIP INVITE requests during that same second.

This can happen when:

* A PBX or dialer rapidly retries failed call attempts.
* SIP retransmissions occur because of network issues or timeout handling.
* Multiple PBXs, SBCs, or application workers send traffic simultaneously.
* Routing or call-forking logic generates multiple SIP INVITE requests for a single intended call.

For this reason, customers should monitor the rate of SIP INVITE requests sent to Telnyx, not only the number of logical dials initiated by their application.

## **How CPS is calculated for real-time limits**

For real-time CPS enforcement, Telnyx evaluates outbound SIP INVITE traffic over short time intervals, typically one second.

On the standard SIP Trunking proxy path, Telnyx determines whether the number of outbound SIP INVITE requests exceeds the applicable CPS limit for the relevant source, such as the source IP address or SIP username.

If the limit is exceeded during the enforcement interval, excess SIP INVITE requests may be rejected with a **SIP 503** response and a CPS-limit response reason.

Example:

```
Default limit: 20 SIP INVITEs from the same source IP per second  
Observed traffic: 35 SIP INVITEs from the same source IP in one second  
Result: 15 SIP INVITEs will be rejected with SIP 503 CPS Limit reached P05
```

The applicable limit may differ if a custom CPS limit has been approved and configured.

## **How to know if CPS limits were reached**

CPS limit events can be identified from the SIP response returned by Telnyx.

When an outbound SIP INVITE is rejected because of CPS limiting, the response is:

```
SIP/2.0 503 CPS Limit reached P05
```

If you see this response in a SIP trace, packet capture, PBX log, SBC log, or dialer log, the applicable CPS limit was reached for that traffic.

If you suspect CPS limiting, collect the following information before contacting Telnyx Support:

* Approximate timestamp and timezone of the failed attempts.
* Source IP address used to send the SIP traffic.
* SIP username, if using credential authentication.
* SIP Call-ID values for failed examples, if available.
* SIP traces, packet captures, or PBX/SBC logs showing the `503 CPS Limit reached P05` response.
* The estimated number of dials per second and SIP INVITEs per second at the time.

## **Best practices to avoid CPS limit rejections**

To reduce the likelihood of reaching CPS limits:

* Spread outbound call attempts more evenly over time.
* Avoid launching large dialer batches simultaneously.
* Add pacing or rate limiting to your PBX, dialer, or application.
* Avoid aggressive retry loops after failures.
* Monitor SIP INVITE requests per second, not only successful calls or logical dials.
* Coordinate with Telnyx before planned high-volume campaigns or traffic spikes.

## **When and how to request a CPS increase**

Request a CPS increase before sending planned high-volume production traffic to Telnyx. This is especially important for new campaigns, contact center launches, traffic migrations, seasonal events, or any expected increase in outbound call attempts.

Before submitting a request, review your current outbound traffic and estimate your future requirements. Include both your current usage patterns and your expected traffic forecast.

Useful information to provide includes:

* Current outbound SIP traffic patterns, including normal and peak traffic periods.
* Expected future traffic volume and the reason for the increase.
* Source IP addresses and SIP usernames that will originate traffic.
* Traffic type and destination profile.
* Evidence that the current CPS limit has already been reached, such as SIP traces, packet captures, or PBX/SBC logs showing 503 CPS Limit reached P05.

Submit the request through Telnyx Support or your account team. Telnyx will review the information and determine whether a custom CPS limit can be approved.

## **CPS limits and CPS surcharge**

Real-time CPS limits and the monthly CPS Peak surcharge are related, but they are separate concepts.

Real-time CPS limits determine whether outbound SIP requests are accepted or rejected in real time. Enforcement is typically applied on a per-source basis, such as source IP address or SIP username.

The monthly CPS Peak surcharge is calculated separately at the account level based on the 95th percentile of outbound SIP Trunking peak CPS usage.

Reaching a real-time CPS limit is **not** required to incur a CPS Peak surcharge, and calls rejected because of CPS limiting are **not included** in the monthly surcharge calculation.

For details about the monthly CPS Peak surcharge calculation and billing, see: **[CPS surcharge article](https://support.telnyx.com/en/articles/7834487-calls-per-second-cps-surcharge)***.*

---

Related Articles

[Sansay: SBC VSXi Setup](https://support.telnyx.com/en/articles/4301888-sansay-sbc-vsxi-setup)[Grandstream UCM6xxx: SIP Trunks](https://support.telnyx.com/en/articles/5748258-grandstream-ucm6xxx-sip-trunks)[Calls per second (CPS) surcharge](https://support.telnyx.com/en/articles/7834487-calls-per-second-cps-surcharge)[Configure P-Charge-Info for Private PBX (Example: FreePBX)](https://support.telnyx.com/en/articles/12580765-configure-p-charge-info-for-private-pbx-example-freepbx)[Configure Token Authentication Header (X-Telnyx-Token) in FreePBX](https://support.telnyx.com/en/articles/12580952-configure-token-authentication-header-x-telnyx-token-in-freepbx)

Did this answer your question?

😞😐😃

Table of contents
