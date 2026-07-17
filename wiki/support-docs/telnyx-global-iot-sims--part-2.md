---
title: Telnyx Global IoT SIMs
summary: Telnyx Global IoT SIMs provide data-only cellular connectivity across 180+
  countries on hundreds of networks. This page covers ordering, registration, APN
  configuration, router integration (InRouter300 and Teltonika), SIM lifecycle management,
  location and device details, international coverage, and tiered zone-based pricing.
sources:
- url: https://support.telnyx.com/en/articles/10511105-using-telnyx-sim-with-inrouter300-series-cellular-routers
- url: https://support.telnyx.com/en/articles/10511646-using-telnyx-sim-with-teltonika-4g-lte-routers
- url: https://support.telnyx.com/en/articles/1130664-countries-that-telnyx-offers-termination-in
- url: https://support.telnyx.com/en/articles/1424680-international-coverage
- url: https://support.telnyx.com/en/articles/3269600-how-to-set-up-a-telnyx-sim-card
- url: https://support.telnyx.com/en/articles/3269973-adding-the-telnyx-sim-apn-to-your-device
- url: https://support.telnyx.com/en/articles/3270106-international-iot-sim-coverage
- url: https://support.telnyx.com/en/articles/3270136-telnyx-global-sims-faqs
- url: https://support.telnyx.com/en/articles/3296669-iot-sim-card-pricing
- url: https://support.telnyx.com/en/articles/3371977-international-roaming-partners
- url: https://support.telnyx.com/en/articles/4298710-sim-setup-and-configuration
- url: https://support.telnyx.com/en/articles/5812302-sim-card-location-and-device-details
- url: https://support.telnyx.com/en/articles/5812328-sim-card-actions
- url: https://support.telnyx.com/en/articles/7966416-telnyx-iot-sim-data-usage-zone-mapping
- url: https://support.telnyx.com/en/collections/1895859-telnyx-global-iot-sims
updated_at: 2026-07-17T08:59:59Z
---

# Telnyx Global IoT SIMs

*Part 2 of 2 — see also: [Part 1](telnyx-global-iot-sims--part-1.md)*

Telnyx Global IoT SIMs provide data-only cellular connectivity across 180+ countries on hundreds of networks. This page covers ordering, registration, APN configuration, router integration (InRouter300 and Teltonika), SIM lifecycle management, location and device details, international coverage, and tiered zone-based pricing.

## International Coverage and Roaming

The Telnyx IoT SIM card has access to hundreds of networks in over 180 countries. Each country is mapped to one of 9 pricing zones, with a discrete per-MB rate per zone. Partner networks can be viewed on the [Telnyx Global Coverage](https://telnyx.com/iot-global-coverage) page.

## Pricing

Telnyx IoT pricing has three components:

1. **One-time charge (OTC):** $1 per SIM, charged at order time. International destinations may incur additional shipping.
2. **Monthly recurring charge (MRC):** $2 per active SIM, reduced to $0.20 per SIM in standby or deactivated state. No MRC is charged for disabled SIMs.
3. **Data usage:** Billed on a tiered basis (upload and download) at rates determined by the country zone and total account usage. Data is charged to the nearest MB. Pay-as-you-go is available, starting at $0.0125/MB.

### Tiered Pricing by Zone

Each zone has five tiers based on cumulative account-wide usage:

| Zone | Tier 1 (up to 100MB) | Tier 2 (up to 500MB) | Tier 3 (up to 2GB) | Tier 4 (up to 5GB) | Tier 5 (>5GB) |
|------|----------------------|----------------------|--------------------|--------------------|---------------|
| 1 | $0.0780 | $0.0390 | $0.0195 | $0.0150 | $0.0125 |
| 2 | $0.2028 | $0.1014 | $0.0507 | $0.0390 | $0.0325 |
| 3 | $0.3900 | $0.1950 | $0.0975 | $0.0750 | $0.0625 |
| 4 | $0.7800 | $0.3900 | $0.1950 | $0.1500 | $0.1250 |
| 5 | $2.0280 | $1.0140 | $0.5070 | $0.3900 | $0.3250 |
| 6 | $3.9000 | $1.9500 | $0.9750 | $0.7500 | $0.6250 |
| 7 | $7.8000 | $3.9000 | $1.9500 | $1.5000 | $1.2500 |
| 8 | $20.2800 | $10.1400 | $5.0700 | $3.9000 | $3.2500 |
| 9 | $39.0000 | $19.5000 | $9.7500 | $7.5000 | $6.2500 |

### Calculation Example

A US-based account consuming 25 GB in Zone 1 in a month would be billed as follows:

- First 100MB at $0.078/MB = $7.80
- Next 400MB (100MB–500MB) at $0.039/MB = $15.60
- Next 1,500MB (500MB–2GB) at $0.0195/MB = $29.25
- Next 3,000MB (2GB–5GB) at $0.015/MB = $45.00
- Next 20,000MB (5GB–25GB) at $0.0125/MB = $250.00

**Total: $347.65**

For up-to-date zone pricing by country, see the [IoT Data Plans pricing page](https://telnyx.com/pricing/iot-data-plans).

## Frequently Asked Questions

- **Voice support:** Telnyx SIMs are data only.
- **SMS:** Two-way SMS is supported via AT commands.
- **International use:** Yes, in over 180 countries.
- **Shipping:** USPS for orders under 50 SIMs within the 48 states; longer for Alaska, Hawaii, and international destinations.
- **SIM costs:** $1 per triple-cut plastic SIM or MFF2 chip, $0.70 per over-the-air eSIM.
- **Pay-as-you-go:** Yes, with data starting at $0.0125/MB.
- **Rounding:** Data is charged to the nearest MB.
- **Suspension/reactivation:** No additional fees for changing SIM state; MRC applies only to active and standby SIMs.
- **Auto-provisioning:** SIMs are provisioned upon registration in standby or active state.
- **Data management:** Data limits can be set at SIM and SIM Group levels via the portal and API, with near real-time usage reporting.
- **Analytics:** Real-time data usage analytics are available; see [SIM Reporting & Analytics](https://support.telnyx.com/en/articles/3679913-sim-reporting-analytics).
- **Unbranded SIMs:** Available for resellers with a minimum order quantity of 5,000.
- **SIM transfer between accounts:** Delete the SIM from the source account and re-register it on the destination account using the registration code. Contact [support@telnyx.com](mailto:support@telnyx.com) if the registration code is needed.

## Related Resources

- [How to set up a Telnyx SIM Card](how-to-set-up-a-telnyx-sim-card.md)
- [Adding the Telnyx SIM APN to your device](adding-the-telnyx-sim-apn-to-your-device.md)
- [SIM Setup and Configuration](sim-setup-and-configuration.md)
- [SIM Card Actions](sim-card-actions.md)
- [SIM Card Location and Device Details](sim-card-location-and-device-details.md)
- [International IoT SIM Coverage](international-iot-sim-coverage.md)
- [International Roaming Partners](international-roaming-partners.md)
- [IoT SIM Card Pricing](iot-sim-card-pricing.md)
- [Telnyx IoT SIM Data Usage Zone Mapping](telnyx-iot-sim-data-usage-zone-mapping.md)
- [Telnyx Global SIMs FAQs](telnyx-global-sims-faqs.md)
- [Using Telnyx SIM with InRouter300 Series Cellular Routers](using-telnyx-sim-with-inrouter300-series-cellular-routers.md)
- [Using Telnyx SIM with Teltonika 4G/LTE Routers](using-telnyx-sim-with-teltonika-4g-lte-routers.md)
