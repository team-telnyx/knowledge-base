---
source_url: https://support.telnyx.com/en/articles/12805746-surcharge-for-high-abandoned-call-rates
scraped: 2026-06-11
---

Surcharge for High Abandoned Call Rates | Telnyx Help Center

[Skip to main content](#main-content)

# Surcharge for High Abandoned Call Rates

Starting November 1, 2025 we will be applying surcharges to outbound traffic with high abandoned call rates to reduce misuse and keep the network reliable for everyone.

Written by David

November 19, 2025

Table of contents

## **What's Changing?**

We’re introducing a surcharge for traffic patterns that include high volumes of outbound calls that are abandoned by the originator before they connect.

If more than 20% of your outbound calls are dropped by the originating side before being answered, you will be subject to an **abandoned call surcharge of $0.005** per abandoned call.

## **What counts as an abandoned call?**

Whenever the originating user initiates the call disconnection during the ringing/call set-up process, the call will be considered “abandoned” for the purposes of the surcharge calculation.

So in other words, any call that is hanged up by the caller while the call is in the process of connecting or while it's still ringing.

**Calls to disconnected numbers also count as an abandoned call.**

## **Why Are We Doing This?**

We’ve seen an increase in traffic where numbers are called briefly and dropped. This kind of usage doesn’t reflect typical calling behavior. They utilize our network resources, putting additional strain on our systems and impacting other customers. This update helps keep capacity available for legitimate traffic.

## **What You Need to Do?**

If you believe your account might have more than 20% outbound calls being abandoned

1. Review your outbound traffic patterns
2. Adjust any systems that place brief or validation-style calls
3. Keep your abandoned call rate below 20% to avoid charges

## **How Can I Track this?**

There are two options to track your abandoned call percentage.

1. We have a new pie chart in the dashboard page showing the abandoned vs not abandoned call in our reporting section of the portal. Here's a direct link to the dashboard page <https://portal.telnyx.com/#/reports/dashboard>.
2. You can generate a Usage Report and filter for abandoned calls by following these steps:

* Go to **Reporting > Usage Reports**
* Switch to the **Advanced Version** view
* Select **SIP Trunking** as the product
* Under dimensions, check **Direction** and **Hangup Details**
* Under metrics, check **Attempted**
* Filter by **Direction = outbound**
* Breakout with **recv\_cancel** contains abandoned calls

# Frequently Asked Questions:

* **If my account had 21% of abandoned calls will the surcharge apply to the % that exceeds the threshold or all the abandoned calls?**

  The surcharge will apply to all the abandoned calls and not just those that exceeded the threshold. So if an account makes 100 calls in one month and there were 21 abandoned calls, the surcharge would be applied to all 21 abandoned calls.

* **Does this apply to inbound or outbound or both?**

  This only applies to outbound calls.

* **What is the rate that will be charged if an account exceeds the 20% threshold of abandoned calls?**

  $0.005 USD per call.

---

Related Articles

[More About Outbound Voice Profiles](https://support.telnyx.com/en/articles/4320411-more-about-outbound-voice-profiles)[Troubleshooting Call Completion](https://support.telnyx.com/en/articles/5025298-troubleshooting-call-completion)[Calls per second (CPS) surcharge](https://support.telnyx.com/en/articles/7834487-calls-per-second-cps-surcharge)

Did this answer your question?

😞😐😃

Table of contents
