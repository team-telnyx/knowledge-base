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

*Part 3 of 3 — see also: [Part 1](telnyx-global-iot-sims--part-1.md), [Part 2](telnyx-global-iot-sims--part-2.md)*

Comprehensive guide to Telnyx IoT SIM and eSIM products covering ordering, registration, device configuration, pricing, global coverage, fleet management features, troubleshooting, and device-specific router setup instructions.

## TLS Certificate Configuration for API Access

Telnyx uses Cloudflare's Universal TLS certificates. If you encounter certificate errors when connecting to `api.telnyx.com`, ensure the Cloudflare CA bundle is in your trust store.

For Java applications using the default `cacerts` truststore (`${JAVA_HOME}/lib/security/cacerts`), no action is typically needed. If using a custom truststore, import the Cloudflare CA bundle:

```
curl -o cf-ca-bundle.crt -L https://raw.githubusercontent.com/cloudflare/cfssl_trust/master/ca-bundle.crt
csplit -f cf-ca-cert -z ca-bundle.crt '/-----BEGIN CERTIFICATE-----/' '{*}'
for ca in ls cf-ca-cert*; do keytool -import -storepass changeit -keystore myTrustStoreFile -alias $ca -file $ca -noprompt; done
```

Cloudflare currently uses the Baltimore CyberTrust Root CA to sign `api.telnyx.com`, but may change to other [supported CAs](https://developers.cloudflare.com/ssl/reference/certificate-authorities/) at any time. For assistance, contact [support@telnyx.com](mailto:support@telnyx.com).
