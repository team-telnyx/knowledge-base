---
title: Americas Number Porting & DID Requirements
summary: This page consolidates Telnyx's number porting and DID acquisition requirements
  for the Americas region, covering Brazil, Canada, Chile, Panama, Peru, Puerto Rico,
  the United States, the Dominican Republic, Malta, Anguilla, and Argentina. Each
  country section lists the required documentation, porting hours, expected timeframes,
  and links to downloadable LOA templates, with additional guidance on US/CA toll-free
  porting and SMS migration best practices.
sources:
- url: https://support.telnyx.com/en/articles/3266425-brazil-number-porting
- url: https://support.telnyx.com/en/articles/3266430-canada-number-porting
- url: https://support.telnyx.com/en/articles/3266652-chile-number-porting
- url: https://support.telnyx.com/en/articles/3267250-panama-number-porting
- url: https://support.telnyx.com/en/articles/3267436-peru-number-porting
- url: https://support.telnyx.com/en/articles/3267535-puerto-rico-number-porting
- url: https://support.telnyx.com/en/articles/3267816-united-states-number-porting
- url: https://support.telnyx.com/en/articles/5190458-the-dominican-republic-number-porting
- url: https://support.telnyx.com/en/articles/5190478-malta-number-porting
- url: https://support.telnyx.com/en/articles/5464041-brazil-did-requirements
- url: https://support.telnyx.com/en/articles/5464057-chile-did-requirements
- url: https://support.telnyx.com/en/articles/5464157-dominican-republic-did-requirements
- url: https://support.telnyx.com/en/articles/5856747-anguilla-did-requirements
- url: https://support.telnyx.com/en/articles/8673249-us-ca-toll-free-number-porting
- url: https://support.telnyx.com/en/articles/9271183-argentina-number-portability
updated_at: 2026-07-17T09:09:35Z
---

# Americas Number Porting & DID Requirements

*Part 2 of 2 — see also: [Part 1](americas-number-porting-did-requirements--part-1.md)*

This page consolidates Telnyx's number porting and DID acquisition requirements for the Americas region, covering Brazil, Canada, Chile, Panama, Peru, Puerto Rico, the United States, the Dominican Republic, Malta, Anguilla, and Argentina. Each country section lists the required documentation, porting hours, expected timeframes, and links to downloadable LOA templates, with additional guidance on US/CA toll-free porting and SMS migration best practices.

## Anguilla

Anguilla only offers toll-free numbers, and business use is required (private use is not allowed). For business identity verification, Telnyx requires the company name and a signed LOI dated within 1 month. For address verification, Telnyx requires a worldwide address (street, building number, postal code, city, and country).

See [Anguilla DID Requirements](anguilla-did-requirements.md) for the full acquisition guide.

## Argentina

For local and national numbers, Argentina requires:

- LOA (contact email must be included)
- CUIT / CUIL / VAT (if the number belongs to a company)
- Attorney's authorization for the representative (if the number belongs to a company)
- Copy of ID / Passport / DNI
- Latest Invoice with the current provider

Reach out to [porting.intl@telnyx.com](mailto:porting.intl@telnyx.com) for the template LOA for Argentina. The porting process typically takes 1 to 7 business days.

## US / CA Toll-Free Porting

Toll-free or "8YY" numbers (including 800, 844, 855, 866, 877, and 888 exchanges) follow a distinct porting process that deviates from FCC Local Number Portability mandates. Toll-free porting uses a centralized portal for all requests, allowing a typically quicker timeframe than standard porting. Telnyx recommends initiating toll-free port requests at least two weeks before the desired number activation.

Toll-free numbers face the risk of disconnection if not activated within 1–2 weeks following their release by the RespOrg (Responsible Organization). To mitigate accidental disconnects, customers should delay submitting port requests until they are within the 2-week timeframe. The timeline for toll-free port requests can span 7 days, assuming no rejections occur and a suitable first available date is selected.

Required documentation for toll-free porting:

- LOA
- Latest Invoice

Download the toll-free LOA from the [Telnyx LOA PDF](https://portal.telnyx.com/downloads/other/Telnyx-LOA.pdf). Toll-free porting should take approximately 2 business days, though the process can vary from 1 to 7 business days.

### SMS Porting Best Practices

When an order transitions into a `ported` status, voice services will have migrated to Telnyx. However, Telnyx cannot guarantee that SMS will migrate at the same time. It may take several hours after the scheduled FOC date/time before the losing carrier releases SMS to Telnyx.

To minimize downtime with SMS services, Telnyx recommends porting SMS prior to porting voice. To port SMS only, submit a hosted SMS request at least 5 business days prior to the desired FOC date.

An example porting process for toll-free phone numbers with SMS:

1. Create a hosted SMS request for the phone numbers you are attempting to port.
2. Create a porting order for the same phone numbers. Request a FOC date at least 5 business days in advance.
3. After 3–4 business days, the hosted SMS request will be completed. SMS will be migrated to Telnyx and active. Voice will still be routing through the losing carrier.
4. When the scheduled FOC date/time arrives, voice ports in and the phone numbers are fully activated on the Telnyx account. Both voice and SMS route through Telnyx with no downtime.

See [US / CA Toll Free Number Porting](us-ca-toll-free-number-porting.md) for the full guide.

## Related Resources

- [Brazil Number Porting](brazil-number-porting.md)
- [Canada Number Porting](canada-number-porting.md)
- [Chile Number Porting](chile-number-porting.md)
- [Panama Number Porting](panama-number-porting.md)
- [Peru Number Porting](peru-number-porting.md)
- [Puerto Rico Number Porting](puerto-rico-number-porting.md)
- [United States Number Porting](united-states-number-porting.md)
- [The Dominican Republic Number Porting](the-dominican-republic-number-porting.md)
- [Malta Number Porting](malta-number-porting.md)
- [Anguilla DID Requirements](anguilla-did-requirements.md)
- [Argentina Number Portability](argentina-number-portability.md)
- [US / CA Toll Free Number Porting](us-ca-toll-free-number-porting.md)
- [Porting Policy & Procedure](https://support.telnyx.com/en/articles/1130630-porting-policy-procedure)
- [Porting Error Messages](https://support.telnyx.com/en/articles/1618776-porting-error-messages)
- [Porting Requirements](https://support.telnyx.com/en/articles/6460777-porting-requirements)
- [Best Practices for Contacting Porting Support](https://support.telnyx.com/en/articles/5820338-best-practices-for-contacting-porting)
- [Porting Away from Twilio](https://support.telnyx.com/en/articles/3947850-porting-away-from-twilio)
- [How to Fill Out an LOA](https://support.telnyx.com/en/articles/2034326-how-to-fill-out-an-loa)
- [Hosted SMS Messaging Process](https://support.telnyx.com/en/articles/5336668-hosted-sms-messaging-process)
- [Why porting phone numbers takes so long](https://telnyx.com/resources/porting-phone-numbers-take-long)
- [Telnyx Number Porting product page](https://telnyx.com/products/number-porting)
