---
title: Alphanumeric Sender ID
summary: Send branded SMS messages using custom alphanumeric sender IDs instead of phone numbers.
sources:
  - url: https://developers.telnyx.com/docs/messaging/messages/alphanumeric-sender-id/index
    content_hash: 1353f5fb08b7bbb19e99d403982e7f57ef9665d2c6e6c38b921931d70fd21de8
updated_at: 2026-04-10T00:00:00Z
---

# Alphanumeric Sender ID

Send branded SMS messages using custom alphanumeric sender IDs instead of phone numbers.

Alphanumeric Sender IDs allow you to send SMS messages using a custom text identifier (like your brand name) instead of a phone number. This makes messages instantly recognizable to recipients—they see "TELNYX" instead of a random number.

<Callout type="info">
  Alphanumeric Sender IDs are **one-way only**. Recipients cannot reply to messages sent from alphanumeric senders.

## Format requirements

Your alphanumeric sender ID must follow these rules:

| Requirement        | Value                                     |
| ------------------ | ----------------------------------------- |
| Length             | 1–11 characters                           |
| Allowed characters | Letters (A-Z, a-z), numbers (0-9), spaces |
| Must contain       | At least one letter                       |

<Callout type="warning">
  **Country restrictions**: Alphanumeric senders **cannot send to the United States, Canada, or Puerto Rico**. Use a [long code](../tutorial/choosing-a-sender-type.md) or [toll-free number](toll-free-verification-with-business-registration-fields.md) for these destinations.

## Before you begin

To use alphanumeric sender IDs, you need:

* A [Telnyx account](https://telnyx.com/sign-up) with **Level 2 verification**
* A [Messaging Profile](https://portal.telnyx.com/#/app/messaging) configured with your alphanumeric sender ID
* An [API key](https://portal.telnyx.com/#/app/api-keys)

<Callout type="tip">
  Some countries require sender ID pre-registration. Check with [Telnyx support](https://support.telnyx.com) for destination-specific requirements.

## Send a message

Use the [send message endpoint](https://developers.telnyx.com/api-reference/messages/send-a-message) with your alphanumeric sender ID in the `from` field.

  ```bash
  curl -X POST https://api.telnyx.com/v2/messages \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -d '{
      "from": "YourBrand",
      "to": "+447700900123",
      "text": "Your order has shipped!",
      "messaging_profile_id": "YOUR_MESSAGING_PROFILE_ID"
    }'
  ```

  ```python
  import telnyx

  telnyx.api_key = "YOUR_API_KEY"

  telnyx.Message.create(
      from_="YourBrand",
      to="+447700900123",
      text="Your order has shipped!",
      messaging_profile_id="YOUR_MESSAGING_PROFILE_ID"
  )
  ```

  ```javascript
  import Telnyx from 'telnyx';

  const telnyx = new Telnyx('YOUR_API_KEY');

  const message = await telnyx.messages.create({
    from: 'YourBrand',
    to: '+447700900123',
    text: 'Your order has shipped!',
    messaging_profile_id: 'YOUR_MESSAGING_PROFILE_ID'
  });

  console.log(message.data);
  ```

  ```ruby
  require 'telnyx'

  Telnyx.api_key = 'YOUR_API_KEY'

  Telnyx::Message.create(
    from: 'YourBrand',
    to: '+447700900123',
    text: 'Your order has shipped!',
    messaging_profile_id: 'YOUR_MESSAGING_PROFILE_ID'
  )
  ```

  ```php
  \Telnyx\Telnyx::setApiKey('YOUR_API_KEY');

  \Telnyx\Message::Create([
    'from' => 'YourBrand',
    'to' => '+447700900123',
    'text' => 'Your order has shipped!',
    'messaging_profile_id' => 'YOUR_MESSAGING_PROFILE_ID'
  ]);
  ```

  ```java
  import com.telnyx.sdk.ApiClient;
  import com.telnyx.sdk.Configuration;
  import com.telnyx.sdk.auth.HttpBearerAuth;
  import com.telnyx.sdk.model.CreateMessageRequest;
  import com.telnyx.sdk.api.MessagesApi;

  public class SendAlphanumeric {
      public static void main(String[] args) {
          ApiClient client = Configuration.getDefaultApiClient();
          client.setBasePath("https://api.telnyx.com/v2");

          HttpBearerAuth auth = (HttpBearerAuth) client.getAuthentication("bearerAuth");
          auth.setBearerToken("YOUR_API_KEY");

          MessagesApi api = new MessagesApi(client);
          CreateMessageRequest request = new CreateMessageRequest()
              .from("YourBrand")
              .to("+447700900123")
              .text("Your order has shipped!");

          api.createMessage(request);
      }
  }
  ```

  ```csharp .NET theme={null}
  using Telnyx;

  TelnyxConfiguration.SetApiKey("YOUR_API_KEY");

  var service = new MessagingSenderIdService();
  var response = await service.CreateAsync(new NewMessagingSenderId
  {
      From = "YourBrand",
      To = "+447700900123",
      Text = "Your order has shipped!"
  });
  ```

Replace:

* `YOUR_API_KEY` with your [API key](https://portal.telnyx.com/#/app/api-keys)
* `YourBrand` with your alphanumeric sender ID (1–11 characters)
* `YOUR_MESSAGING_PROFILE_ID` with your [messaging profile ID](https://portal.telnyx.com/#/app/messaging)

## US and Canada fallback

If you need to reach US or Canadian recipients, configure a **fallback long code** on your messaging profile. Telnyx will automatically use this number instead of the alphanumeric sender for restricted destinations.

Configure this in the [Messaging Portal](https://portal.telnyx.com/#/app/messaging) or via the [Messaging Profiles API](https://developers.telnyx.com/api-reference/profiles/update-a-messaging-profile).

## Limitations

| Feature               | Supported         |
| --------------------- | ----------------- |
| SMS                   | Yes               |
| MMS                   | No                |
| Inbound messages      | No                |
| US/CA/PR destinations | No (use fallback) |

## Rate limits

| Account level        | Rate limit         |
| -------------------- | ------------------ |
| Level 1 (unverified) | 6 messages/minute  |
| Level 2 (verified)   | 60 messages/minute |

Need higher throughput? Contact [sales@telnyx.com](mailto:sales@telnyx.com).

## Failover behavior

Telnyx attempts to deliver your message whenever possible. If alphanumeric delivery fails for a destination:

1. If a US fallback long code is configured, Telnyx uses that number
2. Otherwise, Telnyx may use a generic alphanumeric sender ID to complete delivery

## Common errors

| Error                      | Cause                             | Solution                                       |
| -------------------------- | --------------------------------- | ---------------------------------------------- |
| `InvalidFromAddress`       | Invalid sender format             | Use 1–11 characters with at least one letter   |
| `AlphaSenderNotConfigured` | No alphanumeric sender on profile | Configure sender ID on your messaging profile  |
| `UnsupportedDestination`   | Sending to US/CA/PR               | Use a long code or configure a fallback number |

## Next steps

  - [Messaging Profiles API](https://developers.telnyx.com/api-reference/profiles/list-messaging-profiles) — Create and configure messaging profiles via API

  - [Send Your First Message](send-your-first-message.md) — Complete messaging quickstart guide

  - [Sender Types](../tutorial/choosing-a-sender-type.md) — Compare alphanumeric, long code, toll-free, and short codes

  - [API Reference](https://developers.telnyx.com/api-reference/messages/send-a-message) — Full send message API documentation
