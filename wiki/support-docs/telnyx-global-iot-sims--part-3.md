---
title: Telnyx Global IoT SIMs
summary: A consolidated reference for Telnyx IoT SIM cards covering ordering, registration,
  APN configuration, device-specific router setup, connectivity states, pricing and
  zone mapping, international coverage, troubleshooting, and portal/API observability
  features.
sources:
- url: https://support.telnyx.com/en/articles/10164784-using-telnyx-sim-with-ubiquiti-unifi-lte-pro
- url: https://support.telnyx.com/en/articles/10511105-using-telnyx-sim-with-inrouter300-series-cellular-routers
- url: https://support.telnyx.com/en/articles/10511646-using-telnyx-sim-with-teltonika-4g-lte-routers
- url: https://support.telnyx.com/en/articles/11017501-understanding-wireless-connectivity-states-telnyx-api
- url: https://support.telnyx.com/en/articles/3269600-how-to-set-up-a-telnyx-sim-card
- url: https://support.telnyx.com/en/articles/3269973-adding-the-telnyx-sim-apn-to-your-device
- url: https://support.telnyx.com/en/articles/3270106-international-iot-sim-coverage
- url: https://support.telnyx.com/en/articles/3296669-iot-sim-card-pricing
- url: https://support.telnyx.com/en/articles/3371977-international-roaming-partners
- url: https://support.telnyx.com/en/articles/4298710-sim-setup-and-configuration
- url: https://support.telnyx.com/en/articles/5666594-sim-connectivity-logs
- url: https://support.telnyx.com/en/articles/5812302-sim-card-location-and-device-details
- url: https://support.telnyx.com/en/articles/5812328-sim-card-actions
- url: https://support.telnyx.com/en/articles/7966416-telnyx-iot-sim-data-usage-zone-mapping
- url: https://support.telnyx.com/en/collections/1895859-telnyx-global-iot-sims
updated_at: 2026-08-05T13:24:07Z
---

# Telnyx Global IoT SIMs

*Part 3 of 3 — see also: [Part 1](telnyx-global-iot-sims--part-1.md), [Part 2](telnyx-global-iot-sims--part-2.md)*

A consolidated reference for Telnyx IoT SIM cards covering ordering, registration, APN configuration, device-specific router setup, connectivity states, pricing and zone mapping, international coverage, troubleshooting, and portal/API observability features.

## IoT SIM Card Pricing

Telnyx IoT pricing has three components:

1. **One-time charge (OTC):** $1 per SIM, charged when the SIM is ordered in the Mission Control Portal. International destinations may incur additional shipping costs.
2. **Monthly recurring charge (MRC):** $2 per SIM per month once the SIM is registered and visible in the portal. This is reduced to $0.20 per SIM for SIMs in standby or deactivated state. SIM state can be changed in the portal or via the [SIM Cards API](https://developers.telnyx.com/api/wireless/get-sim-cards).
3. **Data usage:** Billed on a tiered basis (upload and download) at a rate determined by the country of use (based on the MCC) and total account-wide consumption. There are 9 zones, each with 5 tiers.

### Tiered Pricing Example (Zone 1)

For an account consuming 25 GB in Zone 1 during a month:

- First 100 MB at $0.0780/MB = $7.80
- Next 400 MB (100 MB–500 MB) at $0.0390/MB = $15.60
- Next 1,500 MB (500 MB–2 GB) at $0.0195/MB = $29.25
- Next 3,000 MB (2 GB–5 GB) at $0.0150/MB = $45.00
- Next 20,000 MB (5 GB–25 GB) at $0.0125/MB = $250.00
- **Total:** $347.65

### Zone Tier Rates (USD per MB)

| Zone | Tier 1 (≤100 MB) | Tier 2 (≤500 MB) | Tier 3 (≤2 GB) | Tier 4 (≤5 GB) | Tier 5 (>5 GB) |
|------|------------------|------------------|----------------|----------------|----------------|
| 1 | 0.0780 | 0.0390 | 0.0195 | 0.0150 | 0.0125 |
| 2 | 0.2028 | 0.1014 | 0.0507 | 0.0390 | 0.0325 |
| 3 | 0.3900 | 0.1950 | 0.0975 | 0.0750 | 0.0625 |
| 4 | 0.7800 | 0.3900 | 0.1950 | 0.1500 | 0.1250 |
| 5 | 2.0280 | 1.0140 | 0.5070 | 0.3900 | 0.3250 |
| 6 | 3.9000 | 1.9500 | 0.9750 | 0.7500 | 0.6250 |
| 7 | 7.8000 | 3.9000 | 1.9500 | 1.5000 | 1.2500 |
| 8 | 20.2800 | 10.1400 | 5.0700 | 3.9000 | 3.2500 |
| 9 | 39.0000 | 19.5000 | 9.7500 | 7.5000 | 6.2500 |

For up-to-date zone pricing by country, see the [IoT data plans pricing page](https://telnyx.com/pricing/iot-data-plans). Volume pricing is available by contacting the [Telnyx sales team](https://telnyx.com/contact-us).

## Related Resources

- [How to set up a Telnyx SIM Card](how-to-set-up-a-telnyx-sim-card.md)
- [SIM Setup and Configuration](sim-setup-and-configuration.md)
- [Adding the Telnyx SIM APN to your device](adding-the-telnyx-sim-apn-to-your-device.md)
- [Using Telnyx SIM with Ubiquiti UniFi LTE Pro](using-telnyx-sim-with-ubiquiti-unifi-lte-pro.md)
- [Using Telnyx SIM with InRouter300 Series Cellular Routers](using-telnyx-sim-with-inrouter300-series-cellular-routers.md)
- [Using Telnyx SIM with Teltonika 4G/LTE Routers](using-telnyx-sim-with-teltonika-4g-lte-routers.md)
- [SIM Connectivity Logs](sim-connectivity-logs.md)
- [SIM Card Location and Device Details](sim-card-location-and-device-details.md)
- [SIM Card Actions](sim-card-actions.md)
- [Understanding Wireless Connectivity States (Telnyx API)](understanding-wireless-connectivity-states-telnyx-api.md)
- [International IoT SIM Coverage](international-iot-sim-coverage.md)
- [International Roaming Partners](international-roaming-partners.md)
- [IoT SIM Card Pricing](iot-sim-card-pricing.md)
- [Telnyx IoT SIM Data Usage Zone Mapping](telnyx-iot-sim-data-usage-zone-mapping.md)
