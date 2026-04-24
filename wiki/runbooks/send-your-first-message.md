---
title: Send Your First Message
summary: Send your first SMS in 5 minutes using the Telnyx Messaging API.
sources:
  - url: https://developers.telnyx.com/docs/messaging/messages/send-message/index
    content_hash: aa50fc40fc10a45deefcacea397842fc229e6396181ecfddf10b123e4ac3f71c
updated_at: 2026-04-10T00:00:00Z
---

# Send Your First Message

Send your first SMS in 5 minutes using the Telnyx Messaging API.

Send your first SMS using the Telnyx Messaging API. This guide takes you from zero to sending a message in about 5 minutes by testing between two Telnyx numbers—no carrier registration required.

## Prerequisites

* A [Telnyx account](https://telnyx.com/sign-up) (free to create)

## 1. Get two phone numbers

Purchase two Telnyx numbers so you can test messaging between them without registration requirements.

1. **Go to Numbers**

    Navigate to [Numbers > Search & Buy](https://portal.telnyx.com/#/app/numbers/search-numbers) in the portal.

2. **Search for numbers**

    Enter your preferred area code or region, check **SMS** under features, and click **Search**.

3. **Purchase two numbers**

    Click **Add to Cart** on two numbers, then **Place Order**.

<Callout type="tip">
  Having two numbers lets you test on-net (Telnyx-to-Telnyx) messaging immediately, and also test receiving inbound messages.

## 2. Create a Messaging Profile

4. **Go to Messaging**

    Navigate to [Messaging](https://portal.telnyx.com/#/app/messaging) in the portal.

5. **Create a profile**

    Click **Add new profile**, give it a name (e.g., "My App"), and click **Save**.

6. **Assign both numbers**

    Go to [My Numbers](https://portal.telnyx.com/#/app/numbers/my-numbers), and for each number, click the **Messaging Profile** dropdown, select your profile, and save.

## 3. Get your API key

Go to [API Keys](https://portal.telnyx.com/#/app/api-keys) and copy your API key (or create one if needed).

## 4. Send a message

### SMS

      ```bash
      curl -X POST https://api.telnyx.com/v2/messages \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -d '{
          "from": "+15551234567",
          "to": "+15559876543",
          "text": "Hello, world!"
        }'
      ```

      ```javascript
      import Telnyx from 'telnyx';

      const client = new Telnyx({
        apiKey: process.env['TELNYX_API_KEY'],
      });

      const response = await client.messages.send({
        from: '+15551234567',
        to: '+15559876543',
        text: 'Hello, world!'
      });

      console.log(response.data);
      ```

      ```python
      import os
      from telnyx import Telnyx

      client = Telnyx(
          api_key=os.environ.get("TELNYX_API_KEY"),
      )

      response = client.messages.send(
          from_="+15551234567",
          to="+15559876543",
          text="Hello, world!"
      )

      print(response.data)
      ```

      ```ruby
      require "telnyx"

      client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

      response = client.messages.send_(
        from: "+15551234567",
        to: "+15559876543",
        text: "Hello, world!"
      )

      puts(response)
      ```

      ```go
      package main

      import (
        "context"
        "fmt"
        "os"

        "github.com/team-telnyx/telnyx-go"
        "github.com/team-telnyx/telnyx-go/option"
      )

      func main() {
        client := telnyx.NewClient(
          option.WithAPIKey(os.Getenv("TELNYX_API_KEY")),
        )
        response, err := client.Messages.Send(context.TODO(), telnyx.MessageSendParams{
          From: "+15551234567",
          To:   "+15559876543",
          Text: "Hello, world!",
        })
        if err != nil {
          panic(err.Error())
        }
        fmt.Printf("%+v\n", response.Data)
      }
      ```

      ```java
      package com.telnyx.example;

      import com.telnyx.sdk.client.TelnyxClient;
      import com.telnyx.sdk.client.okhttp.TelnyxOkHttpClient;
      import com.telnyx.sdk.models.messages.MessageSendParams;
      import com.telnyx.sdk.models.messages.MessageSendResponse;

      public final class Main {
          public static void main(String[] args) {
              TelnyxClient client = TelnyxOkHttpClient.fromEnv();

              MessageSendParams params = MessageSendParams.builder()
                  .from("+15551234567")
                  .to("+15559876543")
                  .text("Hello, world!")
                  .build();

              MessageSendResponse response = client.messages().send(params);
              System.out.println(response);
          }
      }
      ```

      ```csharp .NET theme={null}
      using Telnyx;

      TelnyxConfiguration.SetApiKey(Environment.GetEnvironmentVariable("TELNYX_API_KEY"));

      var service = new MessageService();
      var response = await service.SendAsync(new MessageSendOptions
      {
          From = "+15551234567",
          To = "+15559876543",
          Text = "Hello, world!"
      });

      Console.WriteLine(response.Data);
      ```

      ```php
      <?php
      require_once 'vendor/autoload.php';

      \Telnyx\Telnyx::setApiKey(getenv('TELNYX_API_KEY'));

      $response = \Telnyx\Message::Create([
          'from' => '+15551234567',
          'to' => '+15559876543',
          'text' => 'Hello, world!'
      ]);

      print_r($response);
      ```

### MMS

    MMS messages support media attachments. Your number must be MMS-enabled.

      ```bash
      curl -X POST https://api.telnyx.com/v2/messages \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -d '{
          "from": "+15551234567",
          "to": "+15559876543",
          "text": "Check out this image!",
          "subject": "Picture",
          "media_urls": ["https://example.com/image.jpg"]
        }'
      ```

      ```javascript
      import Telnyx from 'telnyx';

      const client = new Telnyx({
        apiKey: process.env['TELNYX_API_KEY'],
      });

      const response = await client.messages.send({
        from: '+15551234567',
        to: '+15559876543',
        text: 'Check out this image!',
        subject: 'Picture',
        media_urls: ['https://example.com/image.jpg']
      });

      console.log(response.data);
      ```

      ```python
      import os
      from telnyx import Telnyx

      client = Telnyx(
          api_key=os.environ.get("TELNYX_API_KEY"),
      )

      response = client.messages.send(
          from_="+15551234567",
          to="+15559876543",
          text="Check out this image!",
          subject="Picture",
          media_urls=["https://example.com/image.jpg"]
      )

      print(response.data)
      ```

      ```ruby
      require "telnyx"

      client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

      response = client.messages.send_(
        from: "+15551234567",
        to: "+15559876543",
        text: "Check out this image!",
        subject: "Picture",
        media_urls: ["https://example.com/image.jpg"]
      )

      puts(response)
      ```

      ```go
      package main

      import (
        "context"
        "fmt"
        "os"

        "github.com/team-telnyx/telnyx-go"
        "github.com/team-telnyx/telnyx-go/option"
      )

      func main() {
        client := telnyx.NewClient(
          option.WithAPIKey(os.Getenv("TELNYX_API_KEY")),
        )
        response, err := client.Messages.Send(context.TODO(), telnyx.MessageSendParams{
          From:      "+15551234567",
          To:        "+15559876543",
          Text:      "Check out this image!",
          Subject:   "Picture",
          MediaURLs: []string{"https://example.com/image.jpg"},
        })
        if err != nil {
          panic(err.Error())
        }
        fmt.Printf("%+v\n", response.Data)
      }
      ```

      ```java
      package com.telnyx.example;

      import com.telnyx.sdk.client.TelnyxClient;
      import com.telnyx.sdk.client.okhttp.TelnyxOkHttpClient;
      import com.telnyx.sdk.models.messages.MessageSendParams;
      import com.telnyx.sdk.models.messages.MessageSendResponse;
      import java.util.List;

      public final class Main {
          public static void main(String[] args) {
              TelnyxClient client = TelnyxOkHttpClient.fromEnv();

              MessageSendParams params = MessageSendParams.builder()
                  .from("+15551234567")
                  .to("+15559876543")
                  .text("Check out this image!")
                  .subject("Picture")
                  .mediaUrls(List.of("https://example.com/image.jpg"))
                  .build();

              MessageSendResponse response = client.messages().send(params);
              System.out.println(response);
          }
      }
      ```

      ```csharp .NET theme={null}
      using Telnyx;

      TelnyxConfiguration.SetApiKey(Environment.GetEnvironmentVariable("TELNYX_API_KEY"));

      var service = new MessageService();
      var response = await service.SendAsync(new MessageSendOptions
      {
          From = "+15551234567",
          To = "+15559876543",
          Text = "Check out this image!",
          Subject = "Picture",
          MediaUrls = new[] { "https://example.com/image.jpg" }
      });

      Console.WriteLine(response.Data);
      ```

      ```php
      <?php
      require_once 'vendor/autoload.php';

      \Telnyx\Telnyx::setApiKey(getenv('TELNYX_API_KEY'));

      $response = \Telnyx\Message::Create([
          'from' => '+15551234567',
          'to' => '+15559876543',
          'text' => 'Check out this image!',
          'subject' => 'Picture',
          'media_urls' => ['https://example.com/image.jpg']
      ]);

      print_r($response);
      ```

    <Callout type="info">
      Media URLs must be publicly accessible.

Replace the placeholder values:

* `YOUR_API_KEY`: Your API key from step 3
* `from`: Your first Telnyx number (the sender)
* `to`: Your second Telnyx number (the recipient)

<Callout type="info">
  **E.164 format is required.** Always include the `+` prefix, country code, and full number with no spaces or punctuation.

**International number format examples**

  | Country   | Format                              | Example          |
  | --------- | ----------------------------------- | ---------------- |
  | US/Canada | +1 + 10 digits                      | `+15551234567`   |
  | UK        | +44 + 10-11 digits (drop leading 0) | `+447911123456`  |
  | Germany   | +49 + 10-11 digits (drop leading 0) | `+4915123456789` |
  | Australia | +61 + 9 digits (drop leading 0)     | `+61412345678`   |
  | Brazil    | +55 + 10-11 digits                  | `+5511987654321` |
  | India     | +91 + 10 digits                     | `+919876543210`  |

  **Common mistakes:**

  * ❌ `15551234567` (missing `+`)
  * ❌ `+1 (555) 123-4567` (contains spaces and punctuation)
  * ❌ `+1-555-123-4567` (contains dashes)
  * ✅ `+15551234567`

---

<Callout type="warning">
  **Sending to non-Telnyx numbers?** Off-net messaging to external carriers typically requires sender registration (10DLC, toll-free verification, etc.). See [Next steps](#next-steps) for registration guides.

### Response

A successful response looks like this:

```json theme={null}
{
  "data": {
    "record_type": "message",
    "direction": "outbound",
    "id": "b0c7e8cb-6227-4c74-9f32-c7f80c30934b",
    "type": "SMS",
    "messaging_profile_id": "16fd2706-8baf-433b-82eb-8c7fada847da",
    "from": {
      "phone_number": "+15551234567",
      "carrier": "Telnyx",
      "line_type": "Wireless"
    },
    "to": [
      {
        "phone_number": "+15559876543",
        "status": "queued",
        "carrier": "CARRIER",
        "line_type": "Wireless"
      }
    ],
    "text": "Hello, world!",
    "encoding": "GSM-7",
    "parts": 1,
    "cost": {
      "amount": 0.0051,
      "currency": "USD"
    }
  }
}
```

The `status: "queued"` means your message is on its way. Save the `id` to track delivery status.

## Error handling

API errors return structured JSON responses with an error code, title, and detail message. Handle these in your application to provide clear feedback and enable automatic recovery.

### Error response format

```json theme={null}
{
  "errors": [
    {
      "code": "40300",
      "title": "Forbidden",
      "detail": "The from number +15551234567 is not assigned to a messaging profile.",
      "meta": {
        "url": "https://developers.telnyx.com/docs/messaging/messages/error-codes"
      }
    }
  ]
}
```

### SDK error handling examples

  ```javascript
  import Telnyx from 'telnyx';

  const client = new Telnyx({
    apiKey: process.env['TELNYX_API_KEY'],
  });

  try {
    const response = await client.messages.send({
      from: '+15551234567',
      to: '+15559876543',
      text: 'Hello, world!'
    });
    console.log('Message sent:', response.data.id);
  } catch (error) {
    switch (error.status) {
      case 400:
        console.error('Bad request:', error.message);
        // Malformed JSON, missing required fields
        break;
      case 401:
        console.error('Authentication failed. Check your API key.');
        break;
      case 403:
        console.error('Forbidden:', error.message);
        // Number not assigned to profile, or registration required
        break;
      case 422:
        console.error('Validation error:', error.message);
        // Invalid phone number format, text too long, etc.
        break;
      case 429:
        // Rate limited — extract retry-after header
        const retryAfter = error.headers?.['retry-after'] || 1;
        console.warn(`Rate limited. Retrying after ${retryAfter}s...`);
        await new Promise(r => setTimeout(r, retryAfter * 1000));
        // Retry the request
        break;
      default:
        console.error(`Error (${error.status}):`, error.message);
    }
  }
  ```

  ```python
  import os
  import time
  from telnyx import Telnyx
  from telnyx import APIError, AuthenticationError, RateLimitError

  client = Telnyx(
      api_key=os.environ.get("TELNYX_API_KEY"),
  )

  def send_with_retry(from_number, to_number, text, max_retries=3):
      for attempt in range(max_retries):
          try:
              response = client.messages.send(
                  from_=from_number,
                  to=to_number,
                  text=text,
              )
              print(f"Message sent: {response.data.id}")
              return response
          except AuthenticationError:
              print("Authentication failed. Check your API key.")
              raise  # Don't retry auth errors
          except RateLimitError as e:
              retry_after = int(e.headers.get("retry-after", 1))
              print(f"Rate limited. Retrying in {retry_after}s (attempt {attempt + 1})")
              time.sleep(retry_after)
          except APIError as e:
              if e.status_code == 422:
                  print(f"Validation error: {e.message}")
                  raise  # Don't retry validation errors
              elif e.status_code == 403:
                  print(f"Forbidden: {e.message}")
                  raise  # Don't retry permission errors
              elif e.status_code >= 500:
                  wait = 2 ** attempt
                  print(f"Server error ({e.status_code}). Retrying in {wait}s...")
                  time.sleep(wait)
              else:
                  raise
      raise Exception("Max retries exceeded")

  send_with_retry("+15551234567", "+15559876543", "Hello, world!")
  ```

  ```ruby
  require "telnyx"

  client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

  begin
    response = client.messages.send_(
      from: "+15551234567",
      to: "+15559876543",
      text: "Hello, world!"
    )
    puts "Message sent: #{response.id}"
  rescue Telnyx::AuthenticationError
    puts "Authentication failed. Check your API key."
  rescue Telnyx::RateLimitError => e
    retry_after = e.http_headers["retry-after"]&.to_i || 1
    puts "Rate limited. Retry after #{retry_after}s"
    sleep(retry_after)
    retry
  rescue Telnyx::InvalidRequestError => e
    puts "Validation error: #{e.message}"
  rescue Telnyx::APIError => e
    puts "API error (#{e.http_status}): #{e.message}"
  end
  ```

  ```go
  package main

  import (
    "context"
    "errors"
    "fmt"
    "os"
    "time"

    "github.com/team-telnyx/telnyx-go"
    "github.com/team-telnyx/telnyx-go/option"
  )

  func sendWithRetry(client *telnyx.Client, params telnyx.MessageSendParams, maxRetries int) error {
    for attempt := 0; attempt < maxRetries; attempt++ {
      response, err := client.Messages.Send(context.TODO(), params)
      if err == nil {
        fmt.Printf("Message sent: %s\n", response.Data.ID)
        return nil
      }

      var apiErr *telnyx.Error
      if errors.As(err, &apiErr) {
        switch apiErr.StatusCode {
        case 401:
          return fmt.Errorf("authentication failed: %s", apiErr.Message)
        case 403:
          return fmt.Errorf("forbidden: %s", apiErr.Message)
        case 422:
          return fmt.Errorf("validation error: %s", apiErr.Message)
        case 429:
          wait := time.Duration(1<<attempt) * time.Second
          fmt.Printf("Rate limited. Retrying in %v...\n", wait)
          time.Sleep(wait)
          continue
        default:
          if apiErr.StatusCode >= 500 {
            wait := time.Duration(1<<attempt) * time.Second
            fmt.Printf("Server error (%d). Retrying in %v...\n", apiErr.StatusCode, wait)
            time.Sleep(wait)
            continue
          }
          return fmt.Errorf("API error (%d): %s", apiErr.StatusCode, apiErr.Message)
        }
      }
      return err
    }
    return fmt.Errorf("max retries exceeded")
  }

  func main() {
    client := telnyx.NewClient(option.WithAPIKey(os.Getenv("TELNYX_API_KEY")))
    err := sendWithRetry(client, telnyx.MessageSendParams{
      From: "+15551234567",
      To:   "+15559876543",
      Text: "Hello, world!",
    }, 3)
    if err != nil {
      fmt.Println("Error:", err)
    }
  }
  ```

  ```java
  package com.telnyx.example;

  import com.telnyx.sdk.client.TelnyxClient;
  import com.telnyx.sdk.client.okhttp.TelnyxOkHttpClient;
  import com.telnyx.sdk.models.messages.MessageSendParams;
  import com.telnyx.sdk.models.messages.MessageSendResponse;
  import com.telnyx.sdk.exceptions.TelnyxException;
  import com.telnyx.sdk.exceptions.RateLimitException;
  import com.telnyx.sdk.exceptions.AuthenticationException;
  import com.telnyx.sdk.exceptions.InvalidRequestException;

  public final class Main {
      public static void main(String[] args) throws Exception {
          TelnyxClient client = TelnyxOkHttpClient.fromEnv();

          MessageSendParams params = MessageSendParams.builder()
              .from("+15551234567")
              .to("+15559876543")
              .text("Hello, world!")
              .build();

          int maxRetries = 3;
          for (int attempt = 0; attempt < maxRetries; attempt++) {
              try {
                  MessageSendResponse response = client.messages().send(params);
                  System.out.println("Message sent: " + response.getId());
                  return;
              } catch (AuthenticationException e) {
                  System.err.println("Authentication failed. Check your API key.");
                  throw e;
              } catch (InvalidRequestException e) {
                  System.err.println("Validation error: " + e.getMessage());
                  throw e; // Don't retry validation errors
              } catch (RateLimitException e) {
                  long waitMs = (long) Math.pow(2, attempt) * 1000;
                  System.out.printf("Rate limited. Retrying in %dms...%n", waitMs);
                  Thread.sleep(waitMs);
              } catch (TelnyxException e) {
                  if (e.getStatusCode() >= 500) {
                      long waitMs = (long) Math.pow(2, attempt) * 1000;
                      System.out.printf("Server error (%d). Retrying in %dms...%n", e.getStatusCode(), waitMs);
                      Thread.sleep(waitMs);
                  } else {
                      throw e;
                  }
              }
          }
          throw new Exception("Max retries exceeded");
      }
  }
  ```

  ```csharp .NET theme={null}
  using Telnyx;

  TelnyxConfiguration.SetApiKey(Environment.GetEnvironmentVariable("TELNYX_API_KEY"));

  var service = new MessageService();
  var options = new MessageSendOptions
  {
      From = "+15551234567",
      To = "+15559876543",
      Text = "Hello, world!"
  };

  int maxRetries = 3;
  for (int attempt = 0; attempt < maxRetries; attempt++)
  {
      try
      {
          var response = await service.SendAsync(options);
          Console.WriteLine($"Message sent: {response.Data.Id}");
          break;
      }
      catch (TelnyxException e) when (e.HttpStatusCode == 429)
      {
          var wait = (int)Math.Pow(2, attempt) * 1000;
          Console.WriteLine($"Rate limited. Retrying in {wait}ms...");
          await Task.Delay(wait);
      }
      catch (TelnyxException e) when (e.HttpStatusCode == 401)
      {
          Console.Error.WriteLine("Authentication failed. Check your API key.");
          throw;
      }
      catch (TelnyxException e) when (e.HttpStatusCode == 422)
      {
          Console.Error.WriteLine($"Validation error: {e.Message}");
          throw; // Don't retry validation errors
      }
      catch (TelnyxException e) when (e.HttpStatusCode >= 500)
      {
          var wait = (int)Math.Pow(2, attempt) * 1000;
          Console.WriteLine($"Server error ({e.HttpStatusCode}). Retrying in {wait}ms...");
          await Task.Delay(wait);
      }
  }
  ```

  ```php
  <?php
  require_once 'vendor/autoload.php';

  \Telnyx\Telnyx::setApiKey(getenv('TELNYX_API_KEY'));

  function sendWithRetry($params, $maxRetries = 3) {
      for ($attempt = 0; $attempt < $maxRetries; $attempt++) {
          try {
              $response = \Telnyx\Message::Create($params);
              echo "Message sent: " . $response->id . "\n";
              return $response;
          } catch (\Telnyx\Exception\AuthenticationException $e) {
              echo "Authentication failed. Check your API key.\n";
              throw $e;
          } catch (\Telnyx\Exception\InvalidRequestException $e) {
              echo "Validation error: " . $e->getMessage() . "\n";
              throw $e; // Don't retry validation errors
          } catch (\Telnyx\Exception\RateLimitException $e) {
              $wait = pow(2, $attempt);
              echo "Rate limited. Retrying in {$wait}s...\n";
              sleep($wait);
          } catch (\Telnyx\Exception\ApiException $e) {
              if ($e->getHttpStatus() >= 500) {
                  $wait = pow(2, $attempt);
                  echo "Server error ({$e->getHttpStatus()}). Retrying in {$wait}s...\n";
                  sleep($wait);
              } else {
                  throw $e;
              }
          }
      }
      throw new \Exception("Max retries exceeded");
  }

  sendWithRetry([
      'from' => '+15551234567',
      'to' => '+15559876543',
      'text' => 'Hello, world!'
  ]);
  ```

### HTTP error codes

| HTTP Status | Meaning               | Retryable | Action                                                                       |
| ----------- | --------------------- | --------- | ---------------------------------------------------------------------------- |
| `400`       | Bad Request           | No        | Fix the request body — malformed JSON or missing required fields             |
| `401`       | Unauthorized          | No        | Check your API key is correct and active                                     |
| `402`       | Payment Required      | No        | Add funds to your [account balance](https://portal.telnyx.com/#/app/billing) |
| `403`       | Forbidden             | No        | Number not assigned to a messaging profile, or sender registration required  |
| `404`       | Not Found             | No        | The resource (message ID, profile ID) does not exist                         |
| `422`       | Unprocessable Entity  | No        | Validation failed — see error detail for the specific field                  |
| `429`       | Too Many Requests     | **Yes**   | Rate limited — wait for the `retry-after` header value, then retry           |
| `500`       | Internal Server Error | **Yes**   | Telnyx server error — retry with exponential backoff                         |
| `503`       | Service Unavailable   | **Yes**   | Temporary outage — retry with exponential backoff                            |

### Messaging-specific error codes

These codes appear in the `errors[].code` field and provide more specific detail than HTTP status codes alone:

| Code    | Description                              | Resolution                                                                                                                                             |
| ------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `40001` | Phone number not in E.164 format         | Format as `+[country code][number]` with no spaces or punctuation                                                                                      |
| `40002` | Missing required field                   | Include all required fields: `from`, `to`, and `text` (or `media_urls`)                                                                                |
| `40300` | Number not assigned to messaging profile | Go to [My Numbers](https://portal.telnyx.com/#/app/numbers/my-numbers) and assign a messaging profile                                                  |
| `40301` | Sender registration required             | Register for [10DLC](../tutorial/getting-started-with-10dlc.md), [toll-free verification](toll-free-verification-with-business-registration-fields.md), or another sender type |
| `40302` | Messaging profile disabled               | Re-enable the profile in the [portal](https://portal.telnyx.com/#/app/messaging)                                                                       |
| `42200` | Invalid `from` number                    | Verify the number belongs to your account and supports messaging                                                                                       |
| `42201` | Invalid `to` number                      | Verify the destination is a valid, active phone number                                                                                                 |
| `42202` | Message body too long                    | SMS max: 1,600 characters (concatenated). Reduce content or split into multiple messages                                                               |
| `42203` | Invalid media URL                        | Ensure `media_urls` are publicly accessible HTTPS URLs                                                                                                 |
| `42204` | Too many media attachments               | MMS supports up to 10 media URLs per message                                                                                                           |
| `42205` | Media file too large                     | Individual media files must be under 1 MB; total under 2 MB                                                                                            |

<Callout type="tip">
  For a complete error code reference including delivery failure codes, see the [Messaging Error Codes](messaging-error-code-reference.md) guide.

### Rate limiting

The Telnyx Messaging API enforces rate limits to ensure platform stability. When you exceed the limit, the API returns `429 Too Many Requests` with a `retry-after` header.

**Rate limit headers:**

| Header                  | Description                                               |
| ----------------------- | --------------------------------------------------------- |
| `x-ratelimit-limit`     | Maximum requests allowed in the current window            |
| `x-ratelimit-remaining` | Requests remaining in the current window                  |
| `x-ratelimit-reset`     | Unix timestamp when the window resets                     |
| `retry-after`           | Seconds to wait before retrying (only on `429` responses) |

**Best practices for high-volume sending:**

* Implement exponential backoff: wait `2^attempt` seconds between retries (1s, 2s, 4s, 8s...)
* Add jitter to prevent thundering herd: `wait = base_wait * (0.5 + random())`
* Set a maximum retry count (3–5 attempts) to avoid infinite loops
* Use a message queue (Redis, RabbitMQ, SQS) to buffer outbound messages and control throughput
* Monitor `x-ratelimit-remaining` and slow down before hitting the limit

### Troubleshooting checklist

If your message fails to send, work through this checklist:

7. **Verify API key**

    Confirm your API key is active at [API Keys](https://portal.telnyx.com/#/app/api-keys). Revoked or expired keys return `401`.

8. **Check number assignment**

    Verify your `from` number is assigned to a messaging profile at [My Numbers](https://portal.telnyx.com/#/app/numbers/my-numbers). Unassigned numbers return `403`.

9. **Confirm E.164 format**

    Both `from` and `to` must be in E.164 format: `+15551234567`. No spaces, dashes, or parentheses.

10. **Check sender registration**

    Sending to US carriers off-net requires registration. Check your registration status:

    * **10DLC:** [10DLC Registration](https://portal.telnyx.com/#/app/messaging/10dlc)
    * **Toll-free:** [Toll-Free Verification](https://portal.telnyx.com/#/app/messaging/toll-free-verification)
    * **Short code:** [Short Codes](https://portal.telnyx.com/#/app/messaging/short-codes)

11. **Verify account balance**

    Insufficient balance returns `402`. Check and top up at [Billing](https://portal.telnyx.com/#/app/billing).

12. **Check message content**

    * SMS body must not exceed 1,600 characters
    * MMS media URLs must be publicly accessible HTTPS URLs
    * Content must comply with carrier guidelines (no SHAFT content without proper registration)

13. **Review webhook events**

    If the API returns `200` but the message doesn't arrive, check `message.finalized` webhook events for delivery failure details. See [Webhooks and delivery tracking](#webhooks-and-delivery-tracking).

<Callout type="info">
  **Still stuck?** Check the [Telnyx Status Page](https://status.telnyx.com) for platform issues, or contact [support](https://support.telnyx.com) with your message ID from the API response.

## Webhooks and delivery tracking

After sending a message, Telnyx delivers real-time status updates via webhooks. Configure a webhook URL on your [Messaging Profile](https://portal.telnyx.com/#/app/messaging) to receive these events automatically.

### Message lifecycle events

Messages progress through these statuses:

| Event               | Status                 | Description                                        |
| ------------------- | ---------------------- | -------------------------------------------------- |
| `message.sent`      | `sent`                 | Message accepted and sent to the carrier           |
| `message.finalized` | `delivered`            | Carrier confirmed delivery to the handset          |
| `message.finalized` | `delivery_failed`      | Carrier could not deliver the message              |
| `message.finalized` | `delivery_unconfirmed` | No delivery confirmation received from the carrier |

<Callout type="info">
  Not all carriers return delivery receipts. Some messages may remain in `sent` status without a finalized event. US carriers generally support delivery receipts for SMS; international coverage varies.

### Webhook payload example

```json theme={null}
{
  "data": {
    "event_type": "message.finalized",
    "id": "e6e3e550-4e3f-4b3a-9e10-1c2d3e4f5a6b",
    "occurred_at": "2026-03-05T18:30:00.000+00:00",
    "payload": {
      "id": "b0c7e8cb-6227-4c74-9f32-c7f80c30934b",
      "record_type": "message",
      "direction": "outbound",
      "type": "SMS",
      "from": { "phone_number": "+15551234567" },
      "to": [
        {
          "phone_number": "+15559876543",
          "status": "delivered"
        }
      ],
      "text": "Hello, world!",
      "parts": 1,
      "cost": { "amount": "0.0051", "currency": "USD" },
      "errors": [],
      "completed_at": "2026-03-05T18:30:00.000+00:00"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/webhooks"
  }
}
```

### Processing webhooks

Set up an endpoint to receive webhook `POST` requests and return a `200` response. Telnyx retries failed deliveries with exponential backoff.

  ```javascript
  import express from 'express';

  const app = express();
  app.use(express.json());

  app.post('/webhooks/messaging', (req, res) => {
    const event = req.body.data;

    switch (event.event_type) {
      case 'message.sent':
        console.log(`Message ${event.payload.id} sent`);
        break;
      case 'message.finalized': {
        const status = event.payload.to[0].status;
        if (status === 'delivered') {
          console.log(`Message ${event.payload.id} delivered`);
        } else if (status === 'delivery_failed') {
          console.error(`Message ${event.payload.id} failed:`, event.payload.errors);
        }
        break;
      }
    }

    res.sendStatus(200);
  });

  app.listen(3000, () => console.log('Webhook server listening on port 3000'));
  ```

  ```python
  from flask import Flask, request, jsonify

  app = Flask(__name__)

  @app.route("/webhooks/messaging", methods=["POST"])
  def handle_webhook():
      event = request.json["data"]

      if event["event_type"] == "message.sent":
          print(f"Message {event['payload']['id']} sent")
      elif event["event_type"] == "message.finalized":
          status = event["payload"]["to"][0]["status"]
          if status == "delivered":
              print(f"Message {event['payload']['id']} delivered")
          elif status == "delivery_failed":
              print(f"Message {event['payload']['id']} failed:", event["payload"]["errors"])

      return jsonify(success=True), 200

  if __name__ == "__main__":
      app.run(port=3000)
  ```

  ```ruby
  require "sinatra"
  require "json"

  post "/webhooks/messaging" do
    event = JSON.parse(request.body.read)["data"]

    case event["event_type"]
    when "message.sent"
      puts "Message #{event['payload']['id']} sent"
    when "message.finalized"
      status = event["payload"]["to"][0]["status"]
      if status == "delivered"
        puts "Message #{event['payload']['id']} delivered"
      elsif status == "delivery_failed"
        puts "Message #{event['payload']['id']} failed: #{event['payload']['errors']}"
      end
    end

    status 200
    json success: true
  end
  ```

  ```go
  package main

  import (
  	"encoding/json"
  	"fmt"
  	"log"
  	"net/http"
  )

  type WebhookEvent struct {
  	Data struct {
  		EventType string `json:"event_type"`
  		Payload   struct {
  			ID   string `json:"id"`
  			To   []struct {
  				Status string `json:"status"`
  			} `json:"to"`
  			Errors []map[string]interface{} `json:"errors"`
  		} `json:"payload"`
  	} `json:"data"`
  }

  func handleWebhook(w http.ResponseWriter, r *http.Request) {
  	var event WebhookEvent
  	if err := json.NewDecoder(r.Body).Decode(&event); err != nil {
  		http.Error(w, "Bad request", 400)
  		return
  	}

  	switch event.Data.EventType {
  	case "message.sent":
  		fmt.Printf("Message %s sent\n", event.Data.Payload.ID)
  	case "message.finalized":
  		if len(event.Data.Payload.To) > 0 {
  			status := event.Data.Payload.To[0].Status
  			if status == "delivered" {
  				fmt.Printf("Message %s delivered\n", event.Data.Payload.ID)
  			} else if status == "delivery_failed" {
  				fmt.Printf("Message %s failed: %v\n", event.Data.Payload.ID, event.Data.Payload.Errors)
  			}
  		}
  	}

  	w.WriteHeader(http.StatusOK)
  	json.NewEncoder(w).Encode(map[string]bool{"success": true})
  }

  func main() {
  	http.HandleFunc("/webhooks/messaging", handleWebhook)
  	log.Println("Webhook server listening on port 3000")
  	log.Fatal(http.ListenAndServe(":3000", nil))
  }
  ```

  ```java
  package com.telnyx.example;

  import com.sun.net.httpserver.HttpServer;
  import com.sun.net.httpserver.HttpExchange;
  import com.fasterxml.jackson.databind.JsonNode;
  import com.fasterxml.jackson.databind.ObjectMapper;

  import java.io.IOException;
  import java.io.OutputStream;
  import java.net.InetSocketAddress;

  public class WebhookServer {
      private static final ObjectMapper mapper = new ObjectMapper();

      public static void main(String[] args) throws IOException {
          HttpServer server = HttpServer.create(new InetSocketAddress(3000), 0);
          server.createContext("/webhooks/messaging", WebhookServer::handleWebhook);
          System.out.println("Webhook server listening on port 3000");
          server.start();
      }

      private static void handleWebhook(HttpExchange exchange) throws IOException {
          JsonNode body = mapper.readTree(exchange.getRequestBody());
          JsonNode data = body.get("data");
          String eventType = data.get("event_type").asText();
          String messageId = data.get("payload").get("id").asText();

          if ("message.sent".equals(eventType)) {
              System.out.printf("Message %s sent%n", messageId);
          } else if ("message.finalized".equals(eventType)) {
              String status = data.get("payload").get("to").get(0).get("status").asText();
              if ("delivered".equals(status)) {
                  System.out.printf("Message %s delivered%n", messageId);
              } else if ("delivery_failed".equals(status)) {
                  System.out.printf("Message %s failed: %s%n", messageId, data.get("payload").get("errors"));
              }
          }

          String response = "{\"success\":true}";
          exchange.sendResponseHeaders(200, response.length());
          try (OutputStream os = exchange.getResponseBody()) {
              os.write(response.getBytes());
          }
      }
  }
  ```

  ```csharp .NET theme={null}
  using Microsoft.AspNetCore.Builder;
  using Microsoft.AspNetCore.Http;
  using System.Text.Json;

  var builder = WebApplication.CreateBuilder(args);
  var app = builder.Build();

  app.MapPost("/webhooks/messaging", async (HttpContext context) =>
  {
      using var doc = await JsonDocument.ParseAsync(context.Request.Body);
      var data = doc.RootElement.GetProperty("data");
      var eventType = data.GetProperty("event_type").GetString();
      var messageId = data.GetProperty("payload").GetProperty("id").GetString();

      if (eventType == "message.sent")
      {
          Console.WriteLine($"Message {messageId} sent");
      }
      else if (eventType == "message.finalized")
      {
          var status = data.GetProperty("payload").GetProperty("to")[0].GetProperty("status").GetString();
          if (status == "delivered")
              Console.WriteLine($"Message {messageId} delivered");
          else if (status == "delivery_failed")
              Console.WriteLine($"Message {messageId} failed: {data.GetProperty("payload").GetProperty("errors")}");
      }

      return Results.Ok(new { success = true });
  });

  app.Run("http://localhost:3000");
  ```

  ```php
  <?php
  $payload = json_decode(file_get_contents('php://input'), true);
  $event = $payload['data'];

  switch ($event['event_type']) {
      case 'message.sent':
          error_log("Message {$event['payload']['id']} sent");
          break;
      case 'message.finalized':
          $status = $event['payload']['to'][0]['status'];
          if ($status === 'delivered') {
              error_log("Message {$event['payload']['id']} delivered");
          } elseif ($status === 'delivery_failed') {
              error_log("Message {$event['payload']['id']} failed: " . json_encode($event['payload']['errors']));
          }
          break;
  }

  http_response_code(200);
  echo json_encode(['success' => true]);
  ```

### Retrieve message status via API

You can also check a message's current status by its ID:

  ```bash
  curl -X GET "https://api.telnyx.com/v2/messages/b0c7e8cb-6227-4c74-9f32-c7f80c30934b" \
    -H "Authorization: Bearer YOUR_API_KEY"
  ```

  ```javascript
  const message = await client.messages.retrieve('b0c7e8cb-6227-4c74-9f32-c7f80c30934b');
  console.log(message.data.to[0].status); // "delivered"
  ```

  ```python
  message = client.messages.retrieve("b0c7e8cb-6227-4c74-9f32-c7f80c30934b")
  print(message.data.to[0].status)  # "delivered"
  ```

### Delivery failure error codes

When a message fails delivery, the `errors` array in the webhook payload contains error codes:

| Code    | Description                   | Action                                           |
| ------- | ----------------------------- | ------------------------------------------------ |
| `30003` | Unreachable destination       | Verify the number is active and can receive SMS  |
| `30004` | Message blocked by carrier    | Check content compliance and sender registration |
| `30005` | Unknown destination           | Number may be disconnected or invalid            |
| `30006` | Landline or unreachable       | Number cannot receive SMS (landline, VoIP)       |
| `30007` | Carrier violation             | Message rejected due to content filtering        |
| `30008` | Destination capacity exceeded | Retry after a delay                              |

<Callout type="tip">
  For a complete error code reference, see the [Messaging Error Codes](messaging-error-code-reference.md) guide.

### Webhook security

Validate incoming webhooks to ensure they're from Telnyx:

1. **IP allowlisting** — Telnyx sends webhooks from `192.76.120.192/27`
2. **HTTPS endpoints** — Always use HTTPS for your webhook URL
3. **Respond quickly** — Return `200` within 5 seconds to prevent retries

<Callout type="warning">
  If your endpoint consistently fails to respond, Telnyx will retry with exponential backoff and eventually disable the webhook. Monitor your endpoint health to avoid missing delivery events.

## Next steps

  - [Receive Messages](receive-sms-and-mms-messages.md) — Set up webhooks to receive incoming SMS

  - [Choose a Sender Type](../tutorial/choosing-a-sender-type.md) — Learn about long codes, toll-free, and short codes

  - [10DLC Registration](../tutorial/getting-started-with-10dlc.md) — Register your brand for US messaging compliance

  - [API Reference](https://developers.telnyx.com/api-reference/messages/send-a-message) — Explore all messaging parameters


## Related Pages

- [Send RCS Messages](../runbooks/send-rcs-messages.md)
- [Send WhatsApp Messages](../runbooks/send-whatsapp-messages.md)
