---
source_url: "https://support.telnyx.com/en/articles/2026102601-how-graduated-volume-pricing-works-for-phone-numbers"
title: "How graduated volume pricing works for phone numbers"
description: "How Telnyx volume tiers apply to US local and toll-free phone numbers, with a worked example showing how your monthly cost adds up across tiers."
updated_at: "2026-10-26T12:00:00Z"
modified_at: "2026-10-26T12:00:00Z"
content_hash: b36e99def06a7585f682ffce57c06ab115d887e1bdff50affb1688233bb7a3a2
---

# How graduated volume pricing works for phone numbers

Phone number pricing at Telnyx uses graduated volume tiers. Each tier has its own rate, and each tier's rate applies only to the numbers that fall inside that tier. Reaching a higher tier doesn't reprice all of your numbers at the lower rate. Your total cost is the sum of each tier's numbers multiplied by that tier's rate.

## Current tiers for US numbers

At the time of writing, US local and US toll-free numbers use these monthly tiers:

| Numbers | Monthly rate per number |
|---|---|
| First 50 | \$1.00 |
| 51 to 250 | \$0.79 |
| 251 to 1,000 | \$0.50 |
| 1,001 to 5,000 | \$0.39 |
| Over 5,000 | \$0.25 |

Rates change over time and differ by country and number type. For current rates, see the [Numbers pricing page](https://portal.telnyx.com/#/pricing/numbers) in the Mission Control Portal. See also [Where can I see Pricing options?](https://support.telnyx.com/en/articles/2185372-where-can-i-see-pricing-options)

## Worked example: 328 numbers

With 328 US local numbers, your monthly cost is calculated tier by tier:

| Tier | Numbers in this tier | Rate | Cost |
|---|---|---|---|
| First 50 | 50 | \$1.00 | \$50.00 |
| 51 to 250 | 200 | \$0.79 | \$158.00 |
| 251 to 1,000 | 78 | \$0.50 | \$39.00 |
| **Total** | **328** | | **\$247.00** |

That works out to an average of about \$0.75 per number per month.

Two things to notice:

- **Not every number is billed at \$0.50.** Being in the 251 to 1,000 tier means the numbers in that tier are billed at \$0.50. Your first 50 numbers are still billed at \$1.00, and the next 200 at \$0.79. Seeing \$1.00 and \$0.79 charges on your invoice is expected.
- **The next number you add costs the rate of the tier it lands in.** Your 329th number falls in the 251 to 1,000 tier, so it adds \$0.50 a month.

## A smaller example: 120 numbers

| Tier | Numbers in this tier | Rate | Cost |
|---|---|---|---|
| First 50 | 50 | \$1.00 | \$50.00 |
| 51 to 250 | 70 | \$0.79 | \$55.30 |
| **Total** | **120** | | **\$105.30** |

## Upfront (one-time) costs

Numbers also have an upfront cost when you buy them. This uses its own set of graduated tiers, shown alongside the monthly rates on the [Numbers pricing page](https://portal.telnyx.com/#/pricing/numbers).

## Lowering your rates with a pricing plan

The tiers above are the standard pay-as-you-go rates. If you buy numbers regularly or at volume, a pricing plan can lower your rates further. Plans add a discount on Numbers, Voice, and Messaging in exchange for a minimum monthly spend, and the automatic volume tiers still apply on top.

To compare plans and opt in, see [Pricing Plans](https://portal.telnyx.com/#/pricing/plans) in the Mission Control Portal.

## Checking what you're actually charged

- In the Mission Control Portal, see [Reporting: Monthly Charges](https://support.telnyx.com/en/articles/4425088-reporting-monthly-charges) for the charges applied to your numbers.
- Through the API, [Get monthly charges breakdown](https://developers.telnyx.com/api-reference/get-monthly-charges-breakdown) (`GET /v2/charges_breakdown`) returns the monthly and one-time cost charged for each of your numbers over a date range.

If your charges don't match what you expect from the tiers above, contact [support@telnyx.com](mailto:support@telnyx.com).

If you'd like to discuss pricing beyond the published rates, volume tiers, and self-serve plans, for example for a large order, [contact our sales team](https://telnyx.com/contact-us).
