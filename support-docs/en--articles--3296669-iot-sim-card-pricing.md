---
source_url: https://support.telnyx.com/en/articles/3296669-iot-sim-card-pricing
scraped: 2026-07-08
content_hash: f163316e5b3694506bb6c1c59cf11290083390fd4eaec10d4399f9469966f83b
---

IoT SIM Card Pricing | Telnyx Help Center

[Skip to main content](#main-content)

# IoT SIM Card Pricing

What are the rate plans and associated costs for Telnyx programmable wireless?

Written by Telnyx Engineering

June 6, 2024

Table of contents

# There are 3 components to Telnyx IoT pricing:

1. One-time charge (OTC)
2. Monthly recurring charges (MRC)
3. Data usage

Questions? Get in touch with our [team of experts](https://telnyx.com/contact-us) for more information or to get started with [IoT SIM cards](https://telnyx.com/products/iot-sim-card).

## One-Time Charge for Wireless

Each SIM has a one-time charge of $1. This cost is incurred upon ordering a SIM card in the Mission Control Portal. If the destination for the SIM card is outside of the US or Canada there may also be a shipping cost incurred here.

## Monthly Recurring Charges for Wireless

Once a SIM is registered and showing up in your Mission Control Portal it will incur a monthly charge of $2/SIM.

Note: This charge is reduced to $0.20/SIM for SIMs that are on standby or deactivated. You can change the state of a SIM in the Portal or using [this endpoint](https://developers.telnyx.com/api/wireless/get-sim-cards).

## Data Usage Billing Explained

Data usage is billed on a tiered basis (upload and download) and the data rate is determined by the location in which the SIM is in use and the amount of data used across the account. Data usage on Telnyx SIMs is billed at a different rate depending on the country of usage - this is determined by the MCC that is being used by the SIM.

Each country that Telnyx Wireless operates in is mapped to a zone. Data usage is charged based on 9 zones and the amount of data consumed across the account.

## Calculation Example:

As usage charges are calculated in near real-time, all users would start at the lowest volume Tier. i.e. for the first 100MB of usage **on the account** (not an individual SIM) all PAYG users would pay the rate at that Tier.

Let’s take the example of Acme IoT Solutions, a Wireless Customer of Telnyx in the US. They have 40 SIMs on their account. In the month of April, they consume 25 GB of data. They will be charged for Zone 1 usage as follows:

**First 100MB** - Until the total consumption across all SIMs on their account reaches 100MB they will be charged the Zone-1:Tier-1 rate of $0.0780/MB

*So, 100MB x $0.078/MB = $7.8*

**Between 100 and 500MB** - Between 100MB and 500MB (again, measured for the whole account, i.e total usage across all SIMs consuming data) they will be charged the Zone-1-Tier-2 rate of $0.0390/MB

*So, 400MB x $0.039/MB = $15.6*

**Between 500 and 2GB** -This will be charged the Zone-1:Tier-3 rate of $0.0195

*So, 1,500MB x $0.0195/MB = $29.25*

**Between 2 GB and 5GB** -This will be charged the Zone-1:Tier-4 rate of 0.0150

*So, 3,000MB x $0.015/MB = $45*

**Between 5GB and 25GB** - This will be charged at the Zone-1:Tier-5 rate of 0.0125

*So, 20,000MB x $0.0125/MB = $250*  
​

Total spent for **25GB** usage in **Zone1** -> $7.8 + $15.6 + $29.25+ $45 + $250 = **$347.65**

The zone and usage rates can be found below:

Zone 1:

|  |  |  |
| --- | --- | --- |
| **Tier Price/MB** | **Up To** | **TIER** |
| 0.0780 | 100MB | TIER-1 |
| 0.0390 | 500MB | TIER-2 |
| 0.0195 | 2GB | TIER-3 |
| 0.0150 | 5GB | TIER-4 |
| 0.0125 | >5GB | TIER-5 |

Zone 2:

|  |  |  |
| --- | --- | --- |
| **Tier Price/MB** | **Up To** | **TIER** |
| 0.2028 | 100MB | TIER-1 |
| 0.1014 | 500MB | TIER-2 |
| 0.0507 | 2GB | TIER-3 |
| 0.0390 | 5GB | TIER-4 |
| 0.0325 | >5GB | TIER-5 |

Zone 3:

|  |  |  |
| --- | --- | --- |
| **Tier Price/MB** | **Up To** | **TIER** |
| 0.3900 | 100MB | TIER-1 |
| 0.1950 | 500MB | TIER-2 |
| 0.0975 | 2GB | TIER-3 |
| 0.0750 | 5GB | TIER-4 |
| 0.0625 | >5GB | TIER-5 |

Zone 4:

|  |  |  |
| --- | --- | --- |
| **Tier Price/MB** | **Up To** | **TIER** |
| 0.7800 | 100MB | TIER-1 |
| 0.3900 | 500MB | TIER-2 |
| 0.1950 | 2GB | TIER-3 |
| 0.1500 | 5GB | TIER-4 |
| 0.1250 | >5GB | TIER-5 |

Zone 5:

|  |  |  |
| --- | --- | --- |
| **Tier Price/MB** | **Up To** | **TIER** |
| 2.0280 | 100MB | TIER-1 |
| 1.0140 | 500MB | TIER-2 |
| 0.5070 | 2GB | TIER-3 |
| 0.3900 | 5GB | TIER-4 |
| 0.3250 | >5GB | TIER-5 |

Zone 6:

|  |  |  |
| --- | --- | --- |
| **Tier Price/MB** | **Up To** | **TIER** |
| 3.9000 | 100MB | TIER-1 |
| 1.9500 | 500MB | TIER-2 |
| 0.9750 | 2GB | TIER-3 |
| 0.7500 | 5GB | TIER-4 |
| 0.6250 | >5GB | TIER-5 |

Zone 7:

|  |  |  |
| --- | --- | --- |
| **Tier Price/MB** | **Up To** | **TIER** |
| 7.8000 | 100MB | TIER-1 |
| 3.9000 | 500MB | TIER-2 |
| 1.9500 | 2GB | TIER-3 |
| 1.5000 | 5GB | TIER-4 |
| 1.2500 | >5GB | TIER-5 |

Zone 8:

|  |  |  |
| --- | --- | --- |
| **Tier Price/MB** | **Up To** | **TIER** |
| 20.2800 | 100MB | TIER-1 |
| 10.1400 | 500MB | TIER-2 |
| 5.0700 | 2GB | TIER-3 |
| 3.9000 | 5GB | TIER-4 |
| 3.2500 | >5GB | TIER-5 |

Zone 9:

|  |  |  |
| --- | --- | --- |
| **Tier Price/MB** | **Up To** | **TIER** |
| 39.0000 | 100MB | TIER-1 |
| 19.5000 | 500MB | TIER-2 |
| 9.7500 | 2GB | TIER-3 |
| 7.5000 | 5GB | TIER-4 |
| 6.2500 | >5GB | TIER-5 |

## Telnyx Wireless Zone Mapping

For up-to-date zone pricing by country please check [here](https://telnyx.com/pricing/iot-data-plans).

**Helpful Links**

Get flexible and transparent pricing with automatic discounts as you scale. [Talk to our sales team about volume pricing](https://telnyx.com/contact-us).

---

Related Articles

[International IoT SIM Coverage](https://support.telnyx.com/en/articles/3270106-international-iot-sim-coverage)[Telnyx Global SIMs FAQs](https://support.telnyx.com/en/articles/3270136-telnyx-global-sims-faqs)[Telnyx IoT SIM Data Usage Zone Mapping](https://support.telnyx.com/en/articles/7966416-telnyx-iot-sim-data-usage-zone-mapping)

Did this answer your question?

😞😐😃

Table of contents
