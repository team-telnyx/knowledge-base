---
title: Telnyx Global IoT SIMs
summary: Comprehensive guide to Telnyx IoT SIM and eSIM products covering ordering,
  registration, device configuration, pricing, global coverage, fleet management features,
  troubleshooting, and device-specific router setup instructions.
sources:
- url: https://support.telnyx.com/en/articles/10067533-manual-esim-activation-guide
  content_hash: a616b91d5439cbe98f156097dda4d3beb86fc91b4f7b764fe6d9e5d47c3c01c6
- url: https://support.telnyx.com/en/articles/10164784-using-telnyx-sim-with-ubiquiti-unifi-lte-pro
  content_hash: 41e3e2ccf5674f84244e661a1742912fb9e47f2f0c037fa57341df29782e2b86
- url: https://support.telnyx.com/en/articles/10511105-using-telnyx-sim-with-inrouter300-series-cellular-routers
  content_hash: 5c1fa2101b5e0864e028d35287647460cabfd8be7c848f5aa3128d70bf38938e
- url: https://support.telnyx.com/en/articles/10511646-using-telnyx-sim-with-teltonika-4g-lte-routers
  content_hash: 5dd1c518b39acad5921b9688636e96f6dc666446cbd595253d55d917713b644c
- url: https://support.telnyx.com/en/articles/11017501-understanding-wireless-connectivity-states-telnyx-api
  content_hash: 465bbf458fed9b3eb0ff40eefc2e14ff4f7e31fe3782b105e8ef71f89b96cbee
- url: https://support.telnyx.com/en/articles/3269973-adding-the-telnyx-sim-apn-to-your-device
  content_hash: 38f101921c67f11184c3c8c1abadb115b7c40348727d8d405a1a858dd3c098ff
- url: https://support.telnyx.com/en/articles/3270106-international-iot-sim-coverage
  content_hash: 83180d712506379386b145a1014a232299bed7eb95055cf48830bf4df42345a1
- url: https://support.telnyx.com/en/articles/3270136-telnyx-global-sims-faqs
  content_hash: a36c0ff9552c84fe88cd249ed7a6c3017611f268b0b4264362862c733c51f6fa
- url: https://support.telnyx.com/en/articles/3296669-iot-sim-card-pricing
  content_hash: f163316e5b3694506bb6c1c59cf11290083390fd4eaec10d4399f9469966f83b
- url: https://support.telnyx.com/en/articles/3371977-international-roaming-partners
  content_hash: be5e76ef4c9c71c5ecfa5b2d2fa00829f1d68a5d4cdf0ab3ba5f07d95862b8d3
- url: https://support.telnyx.com/en/articles/3403998-sim-data-limits-notifications
  content_hash: 33b8f561ad38378b63a3f818e20ed01fb178df37fdecb2c5afaf5c971cdcd322
- url: https://support.telnyx.com/en/articles/3679913-sim-reporting-analytics
  content_hash: db794bddb6024f985a569fd588fe5aa5bd9dc7f52d5e6fd8624e76c5407a5580
- url: https://support.telnyx.com/en/articles/4298710-sim-setup-and-configuration
  content_hash: 564c123b34bea07225b84032400ccac1db7f654186930558396dad4b02c736fb
- url: https://support.telnyx.com/en/articles/5666594-sim-connectivity-logs
  content_hash: 03322b39beba984d1ea925f7006d8353e6f5e1ec04bf8526791616678fd446e7
- url: https://support.telnyx.com/en/articles/5761437-sim-card-theft-prevention
  content_hash: 0ad361e1671f498e87f39b3c1c2ea3bcddd2628ccd9678c62e46e80a0df789e6
- url: https://support.telnyx.com/en/articles/5812302-sim-card-location-and-device-details
  content_hash: 574022b05ebac5fb8b46f6590b1cf211cf34385744cb3f513ac1b6647a9a3359
- url: https://support.telnyx.com/en/articles/5812328-sim-card-actions
  content_hash: d8d953d9e4f5a1afaddad58d54e6a9b9eb42b8fc1db96b9b02764d23307a0ee2
- url: https://support.telnyx.com/en/articles/7966416-telnyx-iot-sim-data-usage-zone-mapping
  content_hash: 0bec3694c3ea2cd99460f44bfce054fca3cda26d9ae9224e4ae230c28d2e8fd5
- url: https://support.telnyx.com/en/articles/7984783-certificate-error-api-telnyx-com
  content_hash: b8a0fe4f7ba0cc06092c1f03d8a8abf75fb1478976ea88d3b0f4a47d99208fe5
- url: https://support.telnyx.com/en/articles/8117401-how-to-setup-a-telnyx-esim-via-qr-code
  content_hash: e2adce0d467ff9af4492dfa40f306048e1b4ca53d743d3eebb68ad98f9a32989
- url: https://support.telnyx.com/en/articles/9183726-manual-imsi-selection-on-telnyx-sim
  content_hash: f9c16d22248d37590cc20644e6cc56e8cb34d993acecc5e5b344a695cfb28259
- url: https://support.telnyx.com/en/collections/1895859-telnyx-global-iot-sims
  content_hash: b968d583444c227a1fbf09c2d15cbf5da095d316764e00356188525dfb8f22df
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
