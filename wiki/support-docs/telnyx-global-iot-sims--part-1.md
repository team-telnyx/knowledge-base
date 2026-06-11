---
title: Telnyx Global IoT SIMs
summary: Comprehensive guide to Telnyx IoT SIM and eSIM products covering ordering,
  registration, device configuration, pricing, global coverage, fleet management features,
  troubleshooting, and device-specific router setup instructions.
sources:
- url: https://support.telnyx.com/en/articles/10067533-manual-esim-activation-guide
- url: https://support.telnyx.com/en/articles/10164784-using-telnyx-sim-with-ubiquiti-unifi-lte-pro
- url: https://support.telnyx.com/en/articles/10511105-using-telnyx-sim-with-inrouter300-series-cellular-routers
- url: https://support.telnyx.com/en/articles/10511646-using-telnyx-sim-with-teltonika-4g-lte-routers
- url: https://support.telnyx.com/en/articles/11017501-understanding-wireless-connectivity-states-telnyx-api
- url: https://support.telnyx.com/en/articles/3269973-adding-the-telnyx-sim-apn-to-your-device
- url: https://support.telnyx.com/en/articles/3270106-international-iot-sim-coverage
- url: https://support.telnyx.com/en/articles/3270136-telnyx-global-sims-faqs
- url: https://support.telnyx.com/en/articles/3296669-iot-sim-card-pricing
- url: https://support.telnyx.com/en/articles/3371977-international-roaming-partners
- url: https://support.telnyx.com/en/articles/3403998-sim-data-limits-notifications
- url: https://support.telnyx.com/en/articles/3679913-sim-reporting-analytics
- url: https://support.telnyx.com/en/articles/4298710-sim-setup-and-configuration
- url: https://support.telnyx.com/en/articles/5666594-sim-connectivity-logs
- url: https://support.telnyx.com/en/articles/5761437-sim-card-theft-prevention
- url: https://support.telnyx.com/en/articles/5812302-sim-card-location-and-device-details
- url: https://support.telnyx.com/en/articles/5812328-sim-card-actions
- url: https://support.telnyx.com/en/articles/7966416-telnyx-iot-sim-data-usage-zone-mapping
- url: https://support.telnyx.com/en/articles/7984783-certificate-error-api-telnyx-com
- url: https://support.telnyx.com/en/articles/8117401-how-to-setup-a-telnyx-esim-via-qr-code
- url: https://support.telnyx.com/en/articles/9183726-manual-imsi-selection-on-telnyx-sim
- url: https://support.telnyx.com/en/collections/1895859-telnyx-global-iot-sims
updated_at: 2026-06-11T11:34:01Z
---

# Telnyx Global IoT SIMs

*Part 1 of 3 — see also: [Part 2](telnyx-global-iot-sims--part-2.md), [Part 3](telnyx-global-iot-sims--part-3.md)*

Comprehensive guide to Telnyx IoT SIM and eSIM products covering ordering, registration, device configuration, pricing, global coverage, fleet management features, troubleshooting, and device-specific router setup instructions.

## Ordering and Registering SIM Cards

Order SIM cards from the Wireless section of the [Mission Control Portal](https://portal.telnyx.com/#/wireless/dashboard). Physical SIMs (triple-cut plastic and embedded MFF2 chips) cost $1 each; over-the-air eSIMs cost $0.70 each. For orders over 50 SIMs, contact the sales team to discuss expedited shipping. International orders outside the US may take longer than 7 business days.

You need a minimum of $2 USD in your account balance before registering new SIM cards. To register, navigate to the **Wireless → Register SIM Cards** section in the portal and enter the 10-digit registration code found on your SIM. Multiple codes can be entered at once, separated by commas. You can also assign tags and a SIM group during registration.

Registration can also be done programmatically via the API:

```
curl --request POST \
  --url https://api.telnyx.com/v2/actions/register/sim_cards \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "registration_codes": ["0000000001", "0000000002"],
    "sim_card_group_id": "<uuid>",
    "tags": ["personal", "customers"],
    "status": "enabled"
  }'
```

See the [API Reference](https://developers.telnyx.com/api-reference/sim-cards/register-sim-cards) for details. SIMs can be transferred between Telnyx accounts by deleting the SIM from one account and registering it with the registration code on another.

## eSIM Activation

### QR Code Activation

After purchasing an eSIM in the portal (click **Purchase eSIMs**, select quantity, SIM group, status, and tags), a QR code is displayed. Scan this QR code with your device's camera to begin activation. On mobile phones, the camera will highlight a "mobile plan" option beneath the QR code — select it to proceed. Follow the on-screen instructions; activation may take a few minutes. Verify the APN is set to `data00.telnyx` after activation.

### Manual eSIM Activation

Manual activation is used when QR code scanning isn't feasible — for devices without cameras (IoT devices, modems, routers) or when you can't display or print the QR code.

Retrieve the activation code via the [Get SIM Card Activation Code API](https://developers.telnyx.com/api-reference/sim-cards/get-sim-card-activation-code), passing the SIM's UUID as the `id` parameter. The UUID is visible in the SIM card view in the portal. If you cannot retrieve it via the API, contact the support team.

The activation code comprises two parts: the **SM-DP+ address** (identifies the SM-DP+ server managing eSIM profiles) and the **matching ID** (identifies the specific eSIM on that server). Enter both into your device to connect to the SM-DP+ server, which authenticates and downloads the eSIM profile.

> **Note:** The manual setup method depends on the modem manufacturer, not the eSIM provider.

**iOS:** Settings → Cellular/Mobile Data → Add eSIM → Enter Details Manually → input SM-DP+ address and activation code.

**Android:** Settings → Network & Internet → SIMs → Add eSIM → manually enter SM-DP+ address and activation code.

**Modems using AT Commands** (e.g. Quectel): Log into the modem interface and enter the required AT commands including the SM-DP+ address and activation code.

**GUI-based Routers** (e.g. Peplink): Open the router GUI, navigate to cellular settings, and manually enter the SM-DP+ address and activation code.

## APN Configuration

All Telnyx SIMs require the following APN settings:

- **Name:** `Telnyx`
- **APN:** `data00.telnyx`
- **Username/Password:** Leave blank
- **Authentication:** None

Leave all other fields unmodified. Save the APN and ensure it is selected as the active profile. Some devices may require a restart for changes to take effect.

On mobile devices:
- **Android:** Settings → Connections → Mobile Networks → Access Point Names → Add
- **iOS:** Settings → Cellular → Mobile Data → APN

**Important:** Enable data roaming on your device. Some providers no longer allow first-time registrations via 2G or 3G — complete the initial registration via 4G/LTE. After that, the SIM will be usable on 2G/3G.

## Pricing

There are three components to Telnyx IoT pricing:

### One-Time Charge (OTC)
$1 per SIM, incurred upon ordering. Additional shipping costs may apply for destinations outside the US or Canada.

### Monthly Recurring Charges (MRC)
- **Active SIMs:** $2/SIM/month
- **Standby or deactivated SIMs:** $0.20/SIM/month
- No additional fees for suspending or reactivating SIMs; there are no suspension or reactivation fees — only the MRC changes based on state.

### Data Usage Billing
Data is billed on a tiered, pay-as-you-go basis. The rate depends on the country of usage (mapped to a zone based on MCC) and the cumulative data volume across the account. Charging rounds to the nearest MB.

Each country is mapped to one of 9 pricing zones. Zone 1 tier rates (per MB) start at $0.0780 for the first 100 MB and drop to $0.0125 above 5 GB. Higher zones have progressively higher rates. For the full zone-by-country mapping and current rates, see the [Telnyx IoT Data Plans pricing page](https://telnyx.com/pricing/iot-data-plans).

**Zone 1 example** (25 GB account usage):

| Tier | Up To | Price/MB |
|------|-------|----------|
| Tier 1 | 100 MB | $0.0780 |
| Tier 2 | 500 MB | $0.0390 |
| Tier 3 | 2 GB | $0.0195 |
| Tier 4 | 5 GB | $0.0150 |
| Tier 5 | >5 GB | $0.0125 |

25 GB in Zone 1 totals approximately $347.65 across all tiers.

## Global Coverage and Roaming

Telnyx IoT SIMs provide connectivity in over 180 countries on 650+ networks worldwide. Each country is mapped to a pricing zone, and partner networks can be viewed on the [Telnyx Global Coverage](https://telnyx.com/iot-global-coverage) page.

Telnyx SIMs are data-only (no voice). Two-way SMS is supported via AT commands. SIMs auto-provision once registered to an account in standby or active state.

Unbranded SIMs for reselling are available with a minimum order of 5,000 units.

## SIM Data Limits and Notifications

Data limits can be set at both the SIM Group level and the individual SIM Card level to prevent bill shock. When consumption reaches 80% of the limit, the organization owner receives an email alert. When the limit is reached, another alert is sent and the affected SIMs are disabled.

**SIM Group data limits:** Portal → Wireless → SIM Groups → drill into a group → Data section → set Custom limit.

**Individual SIM data limits:** Portal → Wireless → SIM Cards → drill into a SIM → Data section → set Custom limit.

### Configuring Usage Notification Thresholds

1. **Create a Notification Profile** at [Telnyx Notifications](https://portal.telnyx.com/#/advanced-features/notifications).
2. **Select a Notification Channel** — choose from SMS, Voice, Email, or Webhook.
3. **Configure Notification Settings** — select "Data Usage Notifications" as the notification type.
4. **Link the Notification Profile** to the Usage Notification Threshold section on your SIM card.

Alerts are sent from portal@telnyx.com when thresholds are met.

## Reporting and Analytics

### Wireless Detail Records (WDRs)
WDRs represent individual data sessions. Download CSV reports from the **Reporting** tab in Mission Control Portal. Each WDR includes:

- Record Opening Time (UTC)
- Telephone Number
- Downlink/Uplink Data (MB)
- SIM Card ID, SIM Group ID, Data Plan ID
- MCC and MNC
- IMSI
- SIM Card Tags

### JSON API Analytics

```
curl --request GET \
  --url https://api.telnyx.com/v2/wireless/detail/records/reports/{id} \
  --header 'Authorization: Bearer <token>'
```

The API response includes additional fields such as `data_cost`, `data_rate`, `ip_address`, `sim_group_name`, and `closed_at`. See the [API specification](https://developers.telnyx.com/api-reference/reporting/get-a-wireless-detail-record-wdr-report) for details.
