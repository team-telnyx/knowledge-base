---
source_url: https://support.telnyx.com/en/articles/7834487-calls-per-second-cps-surcharge
scraped: 2026-06-11
---

Calls per second (CPS) surcharge | Telnyx Help Center

[Skip to main content](#main-content)

# Calls per second (CPS) surcharge

Understanding CPS surcharges, their impact, and how Telnyx manages high CPS rates.

Written by Telnyx Engineering

March 25, 2026

Table of contents

# **Are calls per second (CPS) limits changing?**

No. Currently, users who send [SIP Trunking](https://telnyx.com/products/sip-trunks) outbound calls are subject to a limit of 20 calls every second from the same IP address or SIP username – **this limit is not changing**.

Calls that exceed these limits are rejected with response code 503 CPS limit. Telnyx can extend these limits by setting exceptions for specific users who demonstrate they have a legitimate use case for this traffic.

## **How do I know if I am sending bursts of traffic?**

In order to help you understand your traffic patterns, we have added a new [Outbound Peak Calls Per Second (CPS) dashboard](https://portal.telnyx.com/#/app/reports/dashboard) to the Mission Control Portal that shows your outbound traffic patterns. This feature will allow you to view your peak outbound call attempts for every hour on a timeline report.

Monitoring your outbound traffic will help to ensure that your usage is spread out evenly throughout the day to avoid sending large bursts of outbound traffic and a high CPS surcharge.

## **What is the 95th percentile peak CPS value?**

95th percentile peak CPS value is calculated per customer on a monthly basis in the following way:

1. The peak CPS value per hour is calculated by determining the highest CPS value in a given hour.
2. The peak CPS value per hour is calculated for each hour of the month where CPS is greater than 0 to create the monthly dataset. Hours where CPS is 0 are not included in the dataset.
3. From this dataset, the 95th percentile peak CPS value is calculated for each customer, every month—this value is used to calculate the surcharge as described below.

**How are CPS surcharges calculated?**

CPS surcharges will be calculated based on a Graduated Pricing model.   
At the end of each month, we calculate the 95th percentile peak CPS value for each customer using only hours where CPS is greater than 0.   
This value is then used to calculate the monthly surcharge.

The outbound peak CPS pricing model is calculated as follows:

* First 5 CPS = free
* Any Additional CPS up to 25 = $12/CPS
* Any Additional CPS up to 200 = $16/CPS
* Any Additional CPS up to 250 = $24/CPS
* Any Additional CPS (251+) = $30/CPS

As an example, if the 95th percentile peak CPS is found to be 163 in a given month then the surcharge would be:

(5 CPS x $0) + (20 CPS x $12) + (138 CPS x $16) = $2,448

## **How will CPS surcharges be billed?**

CPS surcharges will appear on your monthly invoice as a new line item –reflecting any usage that exceeds the CPS limits that we currently enforce.

## **Will my programmable voice usage be subject to CPS surcharges?**

At this time only SIP Trunking traffic will be subject to CPS surcharges.

---

Related Articles

[Elastix 5: FQDN Trunk Setup](https://support.telnyx.com/en/articles/3284033-elastix-5-fqdn-trunk-setup)[Ribbon: EdgeMarc 6000 Setup](https://support.telnyx.com/en/articles/4215031-ribbon-edgemarc-6000-setup)[Telnyx Dashboards](https://support.telnyx.com/en/articles/4307059-telnyx-dashboards)[Telnyx SIP Response Codes](https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes)[Surcharge for High Abandoned Call Rates](https://support.telnyx.com/en/articles/12805746-surcharge-for-high-abandoned-call-rates)

Did this answer your question?

😞😐😃

Table of contents
