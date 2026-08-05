---
title: Telnyx Number Porting Guide
summary: A consolidated reference for porting phone numbers to and from Telnyx, covering
  best practices, FastPort® activation, port request statuses, common error messages,
  SMS porting behavior, Port Out PIN protection, bundle pre-configuration, and how
  to contact the Porting team.
sources:
- url: https://support.telnyx.com/en/articles/1130610-btn-or-atn-mismatch-error
- url: https://support.telnyx.com/en/articles/1130623-authorized-name-mismatch-error
- url: https://support.telnyx.com/en/articles/1618776-porting-error-messages
- url: https://support.telnyx.com/en/articles/2021334-your-guide-to-fastport
- url: https://support.telnyx.com/en/articles/2030770-port-in-best-practices
- url: https://support.telnyx.com/en/articles/2042977-porting-in-day-of-port-foc
- url: https://support.telnyx.com/en/articles/2054704-fastport-faqs
- url: https://support.telnyx.com/en/articles/3284588-port-request-statuses
- url: https://support.telnyx.com/en/articles/3561993-using-telnyx-fastport
- url: https://support.telnyx.com/en/articles/5170721-best-practices-for-contacting-support
- url: https://support.telnyx.com/en/articles/5820338-best-practices-for-contacting-porting
- url: https://support.telnyx.com/en/articles/7183887-sms-for-ported-in-phone-numbers
- url: https://support.telnyx.com/en/articles/8006189-port-out-pin-protection
- url: https://support.telnyx.com/en/articles/8340760-bundles-bundle-pricing
- url: https://support.telnyx.com/en/articles/8709331-porting-bundles
updated_at: 2026-08-05T13:27:12Z
---

# Telnyx Number Porting Guide

*Part 4 of 5 — see also: [Part 1](telnyx-number-porting-guide--part-1.md), [Part 2](telnyx-number-porting-guide--part-2.md), [Part 3](telnyx-number-porting-guide--part-3.md), [Part 5](telnyx-number-porting-guide--part-5.md)*

A consolidated reference for porting phone numbers to and from Telnyx, covering best practices, FastPort® activation, port request statuses, common error messages, SMS porting behavior, Port Out PIN protection, bundle pre-configuration, and how to contact the Porting team.

## Pre-Configuring Bundles on a Port Order

Bundles can be pre-configured on a porting order so that they are automatically applied when the numbers port in.

Key notes:

- Bundles may be pre-configured on a porting order at any point as long as the order has not completed (i.e., it is not in a `cancelled` or `ported` status).
- A bundle is not actually applied to a phone number until after the phone number ports in. After pre-configuring a bundle with a port order, do not use that same bundle in a number order.
- If an order is already ported, porting tooling cannot be used to associate bundles.
- Ensure the bundle is eligible for the port order (e.g., a US bundle being pre-configured with US phone numbers). If the bundle is not eligible (e.g., a US bundle being pre-configured with Australian phone numbers), it cannot be pre-configured.

### Through the Telnyx Portal

1. Navigate to the [Port Numbers page](https://portal.telnyx.com/#/app/numbers/port-numbers?status=both) in the Telnyx Portal.
2. Click on any order to pre-configure bundles with. This opens the `Port In Details` page for that order.
3. Scroll to the bottom of the `Port In Details` page and click the `Pre-configure Bundles` button.

   ![Porting requirements example](_images/2fbf81fa64ce45e1.png)

### Preconfigure Bundles

1. A modal appears with two tabs: `List` and `Add`. By default, the modal loads on the `List` tab.
   - `List`: Lists pre-configurations already created. If none have been created, the table is empty.
   - `Add`: Create new pre-configurations for bundles and phone numbers on the order.

   ![Preconfiguring bundles](_images/d7156dcfc47c8ed4.png)
2. Click the `Add` tab.

   ![Pre configuring list add](_images/49fb52df462b56c8.png)
3. Specify a phone number from the port order and the bundle to pre-configure with it, then click `Create`.
4. The pre-configuration appears on the `List` page. Repeat for every phone number to pre-configure. To change the bundle associated with a particular phone number, click the trash can in the `Delete` column to delete the pre-configuration, then repeat the steps for that phone number.

   ![Unique bundle ID example](_images/7f3436ac26ef92a8.png)
5. When the order ports, the pre-configured bundles are automatically applied with the specified phone numbers.

### Using the Porting API

Follow the [developer guide on bundles porting](https://developers.telnyx.com/docs/numbers/porting/bundles-porting) to integrate with the porting API for pre-configuring bundles on port orders.

## Contacting the Porting Team

The Porting team is available 9am–7pm CT, Monday–Friday. Communications outside those hours are resolved the following business day.

- **Chat:** Click the chat icon on the bottom right of the screen when signed into the Portal.
- **Email:** [porting@telnyx.com](mailto:porting@telnyx.com)
- **Phone:** 1-888-980-9750

All requests should be posted on the individual order, not just via chat or support ticket, so the team has cross-company visibility and clear communication throughout.

### Choosing a Support Method

- **Need a status update?** Chat or phone will provide a quick resolution.
- **Need to communicate about an expedite or context about a port?** A support ticket may be the best option.
