---
title: Send and Receive Messages with the Telnyx Messaging API
summary: Walks through sending your first SMS and MMS with the Telnyx Messaging API,
  including setup, code samples in multiple languages, error handling, rate limiting,
  webhook-based delivery tracking, and inbound MMS processing.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/send-message/index
- url: https://developers.telnyx.com/docs/messaging/messages/send-receive-mms/index
updated_at: 2026-08-05T13:58:28Z
---

# Send and Receive Messages with the Telnyx Messaging API

*Part 4 of 6 — see also: [Part 1](send-and-receive-messages-with-the-telnyx-messaging-api--part-1.md), [Part 2](send-and-receive-messages-with-the-telnyx-messaging-api--part-2.md), [Part 3](send-and-receive-messages-with-the-telnyx-messaging-api--part-3.md), [Part 5](send-and-receive-messages-with-the-telnyx-messaging-api--part-5.md), [Part 6](send-and-receive-messages-with-the-telnyx-messaging-api--part-6.md)*

Walks through sending your first SMS and MMS with the Telnyx Messaging API, including setup, code samples in multiple languages, error handling, rate limiting, webhook-based delivery tracking, and inbound MMS processing.

## Error Handling

API errors return structured JSON responses with an error code, title, and detail message. Handle these in your application to provide clear feedback and enable automatic recovery.

### Error Response Format

```
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

### SDK Error Handling Examples

#### Node

```
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

#### Python

```
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

#### Ruby

```
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

#### Go

```
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

#### Java

```
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

#### .NET

```
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

#### PHP

```
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

### HTTP Error Codes

| HTTP Status | Meaning | Retryable | Action |
| --- | --- | --- | --- |
| `400` | Bad Request | No | Fix the request body — malformed JSON or missing required fields |
| `401` | Unauthorized | No | Check your API key is correct and active |
| `402` | Payment Required | No | Add funds to your [account balance](https://portal.telnyx.com/#/app/billing) |
| `403` | Forbidden | No | Number not assigned to a messaging profile, or sender registration required |
| `404` | Not Found | No | The resource (message ID, profile ID) does not exist |
| `422` | Unprocessable Entity | No | Validation failed — see error detail for the specific field |
| `429` | Too Many Requests | **Yes** | Rate limited — wait for the `retry-after` header value, then retry |
| `500` | Internal Server Error | **Yes** | Telnyx server error — retry with exponential backoff |
| `503` | Service Unavailable | **Yes** | Temporary outage — retry with exponential backoff |

### Messaging-Specific Error Codes

These codes appear in the `errors[].code` field and provide more specific detail than HTTP status codes alone:

| Code | Description | Resolution |
| --- | --- | --- |
| `40001` | Phone number not in E.164 format | Format as `+[country code][number]` with no spaces or punctuation |
| `40002` | Missing required field | Include all required fields: `from`, `to`, and `text` (or `media_urls`) |
| `40300` | Number not assigned to messaging profile | Go to [My Numbers](https://portal.telnyx.com/#/app/numbers/my-numbers) and assign a messaging profile |
| `40301` | Sender registration required | Register for [10DLC](/docs/messaging/10dlc/quickstart/index), [toll-free verification](/docs/messaging/toll-free-verification), or another sender type |
| `40302` | Messaging profile disabled | Re-enable the profile in the [portal](https://portal.telnyx.com/#/app/messaging) |
| `42200` | Invalid `from` number | Verify the number belongs to your account and supports messaging |
| `42201` | Invalid `to` number | Verify the destination is a valid, active phone number |
| `42202` | Message body too long | SMS max: 1,600 characters (concatenated). Reduce content or split into multiple messages |
| `42203` | Invalid media URL | Ensure `media_urls` are publicly accessible HTTPS URLs |
| `42204` | Too many media attachments | MMS supports up to 10 media URLs per message |
| `42205` | Media file too large | Individual media files must be under 1 MB; total under 2 MB |

For a complete error code reference including delivery failure codes, see the [Messaging Error Codes](/docs/messaging/messages/error-codes) guide.

### Rate Limiting

The Telnyx Messaging API enforces rate limits to ensure platform stability. When you exceed the limit, the API returns `429 Too Many Requests` with a `retry-after` header.

Rate limit headers:

| Header | Description |
| --- | --- |
| `x-ratelimit-limit` | Maximum requests allowed in the current window |
| `x-ratelimit-remaining` | Requests remaining in the current window |
| `x-ratelimit-reset` | Unix timestamp when the window resets |
| `retry-after` | Seconds to wait before retrying (only on `429` responses) |

Best practices for high-volume sending:

- Implement exponential backoff: wait `2^attempt` seconds between retries (1s, 2s, 4s, 8s…)
- Add jitter to prevent thundering herd: `wait = base_wait * (0.5 + random())`
- Set a maximum retry count (3–5 attempts) to avoid infinite loops
- Use a message queue (Redis, RabbitMQ, SQS) to buffer outbound messages and control throughput
- Monitor `x-ratelimit-remaining` and slow down before hitting the limit

### Troubleshooting Checklist

If your message fails to send, work through this checklist:

1. **Verify API key** — Confirm your API key is active at [API Keys](https://portal.telnyx.com/#/app/api-keys). Revoked or expired keys return `401`.
2. **Check number assignment** — Verify your `from` number is assigned to a messaging profile at [My Numbers](https://portal.telnyx.com/#/app/numbers/my-numbers). Unassigned numbers return `403`.
3. **Confirm E.164 format** — Both `from` and `to` must be in E.164 format: `+15551234567`. No spaces, dashes, or parentheses.
4. **Check sender registration** — Sending to US carriers off-net requires registration. Check your registration status:
   - **10DLC:** [10DLC Registration](https://portal.telnyx.com/#/app/messaging/10dlc)
   - **Toll-free:** [Toll-Free Verification](https://portal.telnyx.com/#/app/messaging/toll-free-verification)
   - **Short code:** [Short Codes](https://portal.telnyx.com/#/app/messaging/short-codes)
5. **Verify account balance** — Insufficient balance returns `402`. Check and top up at [Billing](https://portal.telnyx.com/#/app/billing).
6. **Check message content** —
   - SMS body must not exceed 1,600 characters
   - MMS media URLs must be publicly accessible HTTPS URLs
   - Content must comply with carrier guidelines (no SHAFT content without proper registration)
7. **Review webhook events** — If the API returns `200` but the message doesn't arrive, check `message.finalized` webhook events for delivery failure details. See [Webhooks and Delivery Tracking](webhooks-and-delivery-tracking.md).

**Still stuck?** Check the [Telnyx Status Page](https://status.telnyx.com) for platform issues, or contact [support](https://support.telnyx.com) with your message ID from the API response.

### MMS Troubleshooting

- **MMS sent but recipient receives SMS only** — The media URL was unreachable, or the recipient's carrier doesn't support MMS. Verify the media URL is publicly accessible (no auth required), check [message detail records](/docs/messaging/messages/message-detail-records/index) for error details, and confirm the recipient's number supports MMS.
- **Media too large — message rejected** — Total media payload exceeds carrier limits. Compress images before sending (aim for < 600 KB each), enable automatic transcoding (on by default), and see [carrier size limits](/docs/messaging/messages/mms-transcoding/index#carrier-size-limits).
- **Inbound media URL returns 404** — Telnyx media URLs are temporary. Download media immediately in your webhook handler and store in your own S3/GCS bucket.
- **MMS not supported on my number** — Some number types (e.g., alphanumeric sender IDs) don't support MMS. Use a US/Canada long code, toll-free, or short code with MMS enabled in your [messaging profile](https://portal.telnyx.com/#/app/messaging).
