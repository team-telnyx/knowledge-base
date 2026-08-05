---
title: IoT Pricing
summary: 'Telnyx IoT pricing is composed of three components: a one-time charge per
  SIM, monthly recurring charges, and tiered data usage billed by country zone.'
sources:
- url: https://developers.telnyx.com/docs/iot-sim/iot-pricing
updated_at: 2026-08-05T13:46:52Z
---

# IoT Pricing

Telnyx IoT pricing is composed of three components: a one-time charge per SIM, monthly recurring charges, and tiered data usage billed by country zone.

## One Time Charge

Each SIM card has a one time charge of $1. If the destination for the SIM card is outside of the U.S. mainland there is a $10 shipping charge. eSIMs have a one time charge of $0.70 and no shipping charge (eSIMs are delivered over-the-air). These costs are incurred upon ordering SIMs in the Mission Control Portal.

## Monthly Recurring Charges

Once a SIM is registered and showing up in your Mission Control Portal it will incur a monthly charge of $2/SIM.

This charge is reduced to $0.20/SIM for SIMs that are deactivated. You can deactivate a SIM by disabling them in the Portal or using the [Request a SIM card disable](https://developers.telnyx.com/api-reference/sim-cards/request-a-sim-card-disable) endpoint.

## Data Usage

Data usage is billed on a tiered basis (upload and download) and the data rate is determined by the location in which the SIM is in use and the amount of data used across the account. Data usage on Telnyx SIMs is billed at a different rate depending on the country of usage — this is determined by the MCC that is being used by the SIM.

Each country that Telnyx Wireless operates in is mapped to a zone. Data usage is charged based on 9 zones and the amount of data consumed across the account. See the [full cost breakdown](https://support.telnyx.com/en/articles/3296669-programmable-wireless-pricing) of data usage, mapping each country to their relevant zone.
