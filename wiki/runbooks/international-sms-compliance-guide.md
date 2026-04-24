---
title: International SMS Compliance Guide
summary: Country-specific SMS registration requirements, sender ID rules, opt-in regulations, and content restrictions for the top international messaging destinations.
sources:
  - url: https://developers.telnyx.com/docs/messaging/messages/international-sms-compliance/index
    content_hash: 2ddefd2ee6f44168860422fe2171e83858a16d40b5fe3cb97d46cb5a2d06ed44
updated_at: 2026-04-10T00:00:00Z
---

# International SMS Compliance Guide

Country-specific SMS registration requirements, sender ID rules, opt-in regulations, and content restrictions for the top international messaging destinations.

Sending SMS internationally requires compliance with country-specific regulations for sender IDs, opt-in consent, content restrictions, and registration requirements. This guide covers the top 10 international messaging destinations and their specific rules.

  **Quick links:** [Country-by-country reference](#country-by-country-reference) · [Sender ID types](#sender-id-types-by-country) · [Opt-in requirements](#opt-in-requirements-by-region) · [Content restrictions](#content-restrictions) · [Pre-registration](#countries-requiring-pre-registration)

> **Warning:** Regulations change frequently. This guide reflects requirements as of early 2026. Always verify current requirements with [Telnyx support](https://support.telnyx.com) before launching messaging in a new country.

***

## Sender ID types by country

Not every sender type works in every country. Here's what's supported in the top international destinations:

| Country             | Alphanumeric ID | Long Code | Short Code | Toll-Free |    Pre-Registration    |
| ------------------- | :-------------: | :-------: | :--------: | :-------: | :--------------------: |
| 🇺🇸 United States  |        ❌        | ✅ (10DLC) |      ✅     |     ✅     |     10DLC required     |
| 🇨🇦 Canada         |        ❌        |     ✅     |      ✅     |     ✅     |   Short code approval  |
| 🇬🇧 United Kingdom |        ✅        |     ✅     |      ✅     |     —     |       Recommended      |
| 🇩🇪 Germany        |        ✅        |     ✅     |      ✅     |     —     |           No           |
| 🇫🇷 France         |        ✅        |     ✅     |      ✅     |     —     |      OACP required     |
| 🇪🇸 Spain          |        ✅        |     ✅     |      ✅     |     —     |           No           |
| 🇦🇺 Australia      |        ✅        |     ✅     |      ✅     |     —     | Sender ID registration |
| 🇮🇳 India          |  ✅ (registered) |     ❌     |      ❌     |     —     |      DLT mandatory     |
| 🇧🇷 Brazil         |        ✅        |     ✅     |      ✅     |     —     |           No           |
| 🇲🇽 Mexico         |        ✅        |     ✅     |      ✅     |     —     |           No           |

<Callout type="info">
  **US/Canada note:** Alphanumeric sender IDs are **not supported** for US and Canadian destinations. Use [10DLC](../tutorial/getting-started-with-10dlc.md), [toll-free](toll-free-verification-with-business-registration-fields.md), or [short codes](short-codes.md).

***

## Countries requiring pre-registration

Several countries require sender ID or entity registration before you can send messages. Failing to register results in blocked traffic or filtered messages.

### Mandatory registration

**🇮🇳 India — DLT Registration (Mandatory)**

    India requires **Distributed Ledger Technology (DLT)** registration for all A2P SMS. This is the most complex international registration requirement.

    **What you need:**

    1. **Entity registration** on a DLT platform (JioConnect, Vodafone DLT, Airtel DLT, or BSNL DLT)
    2. **Header (sender ID) registration** — your alphanumeric sender ID must be approved
    3. **Template registration** — every message template must be pre-approved
    4. **Content category** — transactional, promotional, or service

    **Registration steps:**

    1. Register as a business entity on one of the DLT platforms
    2. Submit your sender ID (called "header") for approval
    3. Create and submit message templates
    4. Provide Telnyx with your DLT Entity ID, registered headers, and template IDs

    **Message categories:**

    | Category           | Allowed Hours   | DND Filtering | Example                               |
    | ------------------ | --------------- | ------------- | ------------------------------------- |
    | Transactional      | 24/7            | Exempt        | OTP, order confirmations              |
    | Service (Implicit) | 24/7            | Exempt        | Account updates to existing customers |
    | Promotional        | 9 AM – 9 PM IST | Applies       | Marketing, offers, discounts          |

    > **Warning:** **Promotional messages** to users on the Do Not Disturb (DND) registry will be blocked. Transactional and service messages are exempt from DND filtering.

    **Template format:**

    ```
    Dear {#var#}, your order {#var#} has been shipped.
    Track at {#var#}. Delivery by {#var#}.
    ```

    Variables are marked with `{#var#}` and the template must match exactly at delivery time.

---

**🇫🇷 France — OACP Registration**

    France requires registration through the **Off-net Application-to-Person (OACP)** framework for commercial SMS.

    **Requirements:**

    * Sender ID must be registered with French carriers
    * Opt-out must include "STOP" at no cost to the recipient
    * Commercial messages restricted to 8 AM – 8 PM local time
    * No commercial SMS on Sundays or public holidays
    * CNIL (French data authority) consent rules apply

    **Registration process:**

    1. Submit sender ID registration through Telnyx support
    2. Provide business documentation (SIRET number for French businesses)
    3. Allow 5–10 business days for approval

    > **Warning:** Unregistered sender IDs may be silently filtered by French carriers.

---

**🇦🇺 Australia — Sender ID Registration**

    Australia's ACMA requires sender ID registration for A2P messaging.

    **Requirements:**

    * Alphanumeric sender IDs must be registered with carriers
    * Messages must include opt-out instructions
    * Commercial messages must comply with the Spam Act 2003
    * Sender must have consent (express or inferred)

    **Registration:**

    1. Submit sender ID through Telnyx support
    2. Provide Australian Business Number (ABN) or equivalent
    3. Typical approval: 3–5 business days

---

**🇸🇬 Singapore — SSIR Registration**

    Singapore's SMS Sender ID Registry (SSIR) requires all organizations to register sender IDs.

    **Requirements:**

    * Mandatory SSIR registration since January 2023
    * Unregistered alphanumeric sender IDs display as "Likely-SCAM"
    * Registration through SGNIC (Singapore Network Information Centre)

    **Process:**

    1. Register on the SSIR portal (sgnic.sg)
    2. Submit sender ID with business documentation
    3. Link registered sender ID to Telnyx account via support

---

### Recommended (not mandatory) registration

| Country             | Registration               | Benefit                                  |
| ------------------- | -------------------------- | ---------------------------------------- |
| 🇬🇧 United Kingdom | Sender ID pre-registration | Higher delivery rates, reduced filtering |
| 🇩🇪 Germany        | None required              | —                                        |
| 🇪🇸 Spain          | None required              | —                                        |
| 🇧🇷 Brazil         | Sender ID registration     | Better deliverability                    |
| 🇲🇽 Mexico         | None required              | —                                        |

***

## Opt-in requirements by region

### Europe (GDPR + ePrivacy)

The EU's GDPR and ePrivacy Directive set the baseline for all EU/EEA countries:

1. **Explicit consent required**

    Recipients must actively opt in to receive messages. Pre-checked boxes are **not valid consent** under GDPR.

2. **Purpose limitation**

    Consent must specify what types of messages the user will receive. "We may contact you" is too vague.

3. **Right to withdraw**

    Users must be able to opt out at any time, and the process must be as easy as opting in.

4. **Record keeping**

    Maintain records of when and how consent was obtained. You must be able to prove consent if challenged.

**GDPR-compliant consent example:**

```
☐ I agree to receive appointment reminders and order updates from [Company]
  via SMS to the phone number provided. Message frequency: up to 4 msg/month.
  Reply STOP to unsubscribe. Msg & data rates may apply.
```

  **Country variations within the EU:**

  * **Germany:** Requires "double opt-in" (confirmation SMS after initial signup) as best practice
  * **France:** CNIL requires explicit, separate consent for marketing SMS
  * **Spain:** AEPD allows "soft opt-in" for existing customers (similar products/services only)
  * **Italy:** Garante requires clear separation between service and marketing consent

### North America

| Requirement       | United States                                         | Canada                         |
| ----------------- | ----------------------------------------------------- | ------------------------------ |
| Governing law     | TCPA + CTIA guidelines                                | CASL                           |
| Consent type      | Express written (marketing) / Express (transactional) | Express or implied             |
| Opt-out mechanism | STOP keyword mandatory                                | Unsubscribe mechanism required |
| Record retention  | Recommended 4+ years                                  | Duration of consent            |
| Pre-registration  | 10DLC / toll-free verification                        | Short code approval            |

### Asia-Pacific

| Country          | Key requirement                                                                                   |
| ---------------- | ------------------------------------------------------------------------------------------------- |
| 🇮🇳 India       | DLT registration + template approval. DND registry filtering for promotional.                     |
| 🇦🇺 Australia   | Express consent required (Spam Act 2003). Include sender identity + opt-out.                      |
| 🇸🇬 Singapore   | SSIR registration. PDPA consent rules. No SMS between 9 PM – 9 AM without consent.                |
| 🇯🇵 Japan       | Act on Specified Commercial Transactions. Opt-out link required. Sender identification mandatory. |
| 🇰🇷 South Korea | Pre-approved templates only. 080 opt-out number required for commercial messages.                 |

### Latin America

| Country        | Key requirement                                                          |
| -------------- | ------------------------------------------------------------------------ |
| 🇧🇷 Brazil    | LGPD consent required. No messages between 9 PM – 9 AM. Include opt-out. |
| 🇲🇽 Mexico    | LFPDPPP consent. Include sender identity. Opt-out mechanism required.    |
| 🇨🇴 Colombia  | SIC consent requirements. Habeas Data law. Pre-registration recommended. |
| 🇦🇷 Argentina | PDPA consent. National Do Not Call Registry must be checked.             |

***

## Content restrictions

### Universally restricted content

These content types are restricted or prohibited in most countries:

| Content type        | Status                          | Notes                                                    |
| ------------------- | ------------------------------- | -------------------------------------------------------- |
| Cannabis / CBD      | 🚫 Prohibited in most countries | Even where locally legal, carriers often block           |
| Gambling            | ⚠️ Heavily regulated            | Requires specific licensing in most jurisdictions        |
| Adult content       | 🚫 Prohibited                   | Blocked by most carriers globally                        |
| Phishing / fraud    | 🚫 Prohibited                   | Immediate account termination                            |
| Financial services  | ⚠️ Regulated                    | Must comply with local financial advertising laws        |
| Healthcare / pharma | ⚠️ Regulated                    | Prescription drug messaging restricted in many countries |
| Political campaigns | ⚠️ Varies by country            | Some countries ban political SMS entirely                |

### Country-specific restrictions

**🇬🇧 United Kingdom**

    * **Financial promotions:** Must be approved by an FCA-authorized firm
    * **Age-gated content:** Must use age verification for alcohol, gambling
    * **Charity messaging:** Regulated by the Fundraising Regulator
    * **Marketing hours:** No legal restriction, but industry best practice is 8 AM – 9 PM

---

**🇩🇪 Germany**

    * **UWG (Competition Law):** Strict consent requirements for all commercial messages
    * **Heilmittelwerbegesetz:** Restricts pharmaceutical advertising
    * **Glücksspielstaatsvertrag:** Strict gambling advertising rules
    * **Double opt-in:** Expected best practice for marketing consent

---

**🇫🇷 France**

    * **Loi Hamon:** Right to opt out of all commercial solicitation
    * **Time restrictions:** No commercial SMS 8 PM – 8 AM, Sundays, or public holidays
    * **CNIL enforcement:** Active enforcement with significant fines
    * **Language:** Commercial messages should be in French

---

**🇮🇳 India**

    * **Promotional hours:** 9 AM – 9 PM IST only (mandatory, not best practice)
    * **DND registry:** Promotional messages blocked to DND-registered numbers
    * **Template approval:** Every message must match a pre-approved template
    * **Scrubbing:** Numbers are checked against DND registry before delivery

---

**🇧🇷 Brazil**

    * **LGPD compliance:** Explicit consent with specific purpose
    * **Quiet hours:** 9 PM – 9 AM (industry standard)
    * **Consumer code:** Price/offer messages must include full terms
    * **Language:** Messages should be in Portuguese

---

***

## Country-by-country reference

### 🇬🇧 United Kingdom

| Setting                 | Value                                             |
| ----------------------- | ------------------------------------------------- |
| **Sender types**        | Alphanumeric (recommended), long code, short code |
| **Alphanumeric length** | 3–11 characters                                   |
| **Regulation**          | PECR + UK GDPR                                    |
| **Regulator**           | ICO (Information Commissioner's Office)           |
| **Pre-registration**    | Recommended (improves deliverability)             |
| **Opt-out**             | STOP keyword or unsubscribe link                  |
| **Time restrictions**   | None (best practice: 8 AM – 9 PM)                 |

**Send with alphanumeric sender ID:**

  ```bash
  curl -X POST https://api.telnyx.com/v2/messages \
    -H "Authorization: Bearer $TELNYX_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "from": "YourBrand",
      "to": "+447700900123",
      "text": "Hi! Your delivery is scheduled for tomorrow between 2-4 PM. Reply STOP to opt out.",
      "messaging_profile_id": "YOUR_MESSAGING_PROFILE_ID"
    }'
  ```

  ```python
  import telnyx
  import os

  telnyx.api_key = os.environ["TELNYX_API_KEY"]

  message = telnyx.Message.create(
      from_="YourBrand",
      to="+447700900123",
      text="Hi! Your delivery is scheduled for tomorrow between 2-4 PM. Reply STOP to opt out.",
      messaging_profile_id="YOUR_MESSAGING_PROFILE_ID",
  )
  print(f"Message ID: {message.id}")
  ```

  ```javascript
  import Telnyx from "telnyx";

  const telnyx = new Telnyx(process.env.TELNYX_API_KEY);

  const { data: message } = await telnyx.messages.create({
    from: "YourBrand",
    to: "+447700900123",
    text: "Hi! Your delivery is scheduled for tomorrow between 2-4 PM. Reply STOP to opt out.",
    messaging_profile_id: "YOUR_MESSAGING_PROFILE_ID",
  });
  console.log(`Message ID: ${message.id}`);
  ```

  ```ruby
  require "telnyx"

  Telnyx.api_key = ENV["TELNYX_API_KEY"]

  message = Telnyx::Message.create(
    from: "YourBrand",
    to: "+447700900123",
    text: "Hi! Your delivery is scheduled for tomorrow between 2-4 PM. Reply STOP to opt out.",
    messaging_profile_id: "YOUR_MESSAGING_PROFILE_ID"
  )
  puts "Message ID: #{message.id}"
  ```

  ```java
  import com.telnyx.sdk.client.TelnyxClient;
  import com.telnyx.sdk.client.okhttp.TelnyxOkHttpClient;
  import com.telnyx.sdk.models.messages.MessageCreateParams;

  TelnyxClient client = TelnyxOkHttpClient.fromEnv();

  var message = client.messages().create(MessageCreateParams.builder()
      .from("YourBrand")
      .to("+447700900123")
      .text("Hi! Your delivery is scheduled for tomorrow between 2-4 PM. Reply STOP to opt out.")
      .messagingProfileId("YOUR_MESSAGING_PROFILE_ID")
      .build());
  System.out.println("Message ID: " + message.id());
  ```

  ```csharp .NET theme={null}
  using Telnyx;

  var client = new TelnyxClient(Environment.GetEnvironmentVariable("TELNYX_API_KEY"));

  var message = await client.Messages.CreateAsync(new MessageCreateParams
  {
      From = "YourBrand",
      To = "+447700900123",
      Text = "Hi! Your delivery is scheduled for tomorrow between 2-4 PM. Reply STOP to opt out.",
      MessagingProfileId = "YOUR_MESSAGING_PROFILE_ID"
  });
  Console.WriteLine($"Message ID: {message.Id}");
  ```

  ```php
  $telnyx = new \Telnyx\TelnyxClient(getenv('TELNYX_API_KEY'));

  $message = $telnyx->messages->create([
      'from' => 'YourBrand',
      'to' => '+447700900123',
      'text' => 'Hi! Your delivery is scheduled for tomorrow between 2-4 PM. Reply STOP to opt out.',
      'messaging_profile_id' => 'YOUR_MESSAGING_PROFILE_ID',
  ]);
  echo "Message ID: " . $message->id . "\n";
  ```

  ```go
  package main

  import (
      "context"
      "fmt"
      "github.com/team-telnyx/telnyx-go"
      "github.com/team-telnyx/telnyx-go/option"
  )

  func main() {
      client := telnyx.NewClient(option.WithAPIKey("YOUR_API_KEY"))

      message, err := client.Messages.New(context.TODO(), telnyx.MessageNewParams{
          From: telnyx.String("YourBrand"),
          To:   telnyx.String("+447700900123"),
          Text: telnyx.String("Hi! Your delivery is scheduled for tomorrow between 2-4 PM. Reply STOP to opt out."),
          MessagingProfileID: telnyx.String("YOUR_MESSAGING_PROFILE_ID"),
      })
      if err != nil {
          panic(err)
      }
      fmt.Printf("Message ID: %s\n", message.ID)
  }
  ```

### 🇮🇳 India

| Setting               | Value                                                         |
| --------------------- | ------------------------------------------------------------- |
| **Sender types**      | Alphanumeric only (6 characters, registered header)           |
| **Regulation**        | TRAI + DLT framework                                          |
| **Regulator**         | TRAI (Telecom Regulatory Authority of India)                  |
| **Pre-registration**  | **Mandatory** — DLT entity, header, and template registration |
| **Opt-out**           | Handled via DLT/DND registry                                  |
| **Time restrictions** | Promotional: 9 AM – 9 PM IST only                             |

> **Warning:** India requires both **sender ID registration** and **message template approval** before any messages can be sent. Contact [Telnyx support](https://support.telnyx.com) to initiate India DLT registration.

### 🇩🇪 Germany

| Setting               | Value                                        |
| --------------------- | -------------------------------------------- |
| **Sender types**      | Alphanumeric, long code                      |
| **Regulation**        | GDPR + UWG (Competition Act) + TTDSG         |
| **Regulator**         | BfDI (Federal Data Protection Commissioner)  |
| **Pre-registration**  | Not required                                 |
| **Opt-out**           | Must be free and easy (STOP keyword or link) |
| **Time restrictions** | None legally, best practice 8 AM – 9 PM      |

### 🇫🇷 France

| Setting               | Value                                                           |
| --------------------- | --------------------------------------------------------------- |
| **Sender types**      | Alphanumeric (registered via OACP), long code, short code       |
| **Regulation**        | GDPR + Code des postes et des communications                    |
| **Regulator**         | CNIL + ARCEP                                                    |
| **Pre-registration**  | **Required** — OACP sender ID registration                      |
| **Opt-out**           | "STOP" at no cost to recipient (mandatory)                      |
| **Time restrictions** | **8 AM – 8 PM, no Sundays/holidays** (mandatory for commercial) |

### 🇦🇺 Australia

| Setting               | Value                                            |
| --------------------- | ------------------------------------------------ |
| **Sender types**      | Alphanumeric (registered), long code, short code |
| **Regulation**        | Spam Act 2003 + Privacy Act 1988                 |
| **Regulator**         | ACMA                                             |
| **Pre-registration**  | Required (sender ID registration)                |
| **Opt-out**           | Functional unsubscribe within 5 business days    |
| **Time restrictions** | None legally, best practice 9 AM – 8 PM AEST     |

### 🇧🇷 Brazil

| Setting               | Value                                       |
| --------------------- | ------------------------------------------- |
| **Sender types**      | Alphanumeric, long code, short code         |
| **Regulation**        | LGPD + Consumer Protection Code             |
| **Regulator**         | ANPD (National Data Protection Authority)   |
| **Pre-registration**  | Recommended                                 |
| **Opt-out**           | Easy mechanism required                     |
| **Time restrictions** | 9 PM – 9 AM quiet hours (industry standard) |

### 🇲🇽 Mexico

| Setting               | Value                                 |
| --------------------- | ------------------------------------- |
| **Sender types**      | Alphanumeric, long code, short code   |
| **Regulation**        | LFPDPPP (Federal Data Protection Law) |
| **Regulator**         | INAI                                  |
| **Pre-registration**  | Not required                          |
| **Opt-out**           | Mechanism required in privacy notice  |
| **Time restrictions** | None legally                          |

***

## Best practices for international messaging

5. **Check country requirements before launch**

    Review this guide and contact Telnyx support for any country not listed. Requirements vary significantly and change frequently.

6. **Use the right sender type**

    Alphanumeric sender IDs are preferred in most international markets (except US/Canada). They build brand recognition and improve open rates.

7. **Localize your messages**

    Send messages in the recipient's language. Many countries require or strongly recommend this for commercial messaging.

8. **Respect time zones and quiet hours**

    Even where not legally required, sending during business hours dramatically reduces complaints and opt-outs.

9. **Include opt-out in every message**

    Universal best practice. Use language appropriate to the country (e.g., "STOP" in English-speaking countries, "ARRÊT" in France).

10. **Maintain consent records**

    Store when and how each recipient consented. GDPR requires you to prove consent if challenged. Keep records for at least 4 years.

11. **Monitor delivery rates by country**

    Use [Message Detail Records](message-detail-records.md) to track delivery rates per country. Sudden drops may indicate registration issues or content filtering.

***

## Handling multi-country messaging

For platforms sending to multiple countries, implement country-aware routing:

```python
import telnyx
import os

telnyx.api_key = os.environ["TELNYX_API_KEY"]
