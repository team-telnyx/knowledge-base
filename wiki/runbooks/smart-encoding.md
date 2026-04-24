---
title: Smart Encoding
summary: Automatically substitute Unicode characters with GSM-7 equivalents to reduce SMS segment counts and costs.
sources:
  - url: https://developers.telnyx.com/docs/messaging/messages/smart-encoding/index
    content_hash: a9a7fcc012bff4491926abe1dcc7ea511a25181e02fe02f2f45e42dff6c2bf9d
updated_at: 2026-04-10T00:00:00Z
---

# Smart Encoding

Automatically substitute Unicode characters with GSM-7 equivalents to reduce SMS segment counts and costs.

Smart encoding automatically replaces Unicode characters with visually similar GSM-7 characters. This keeps your messages in the more efficient GSM-7 encoding, reducing segment counts and costs.

> **Note:** Smart encoding applies to SMS only. MMS and RCS messages use UTF-8 encoding by default and are not affected.

## Why use smart encoding

SMS messages using GSM-7 encoding fit **160 characters per segment**. When a message contains even one Unicode character outside GSM-7, the entire message switches to UTF-16 encoding, which only fits **70 characters per segment**.

A single smart quote (`"`) or em dash (`—`) can more than double your messaging costs.

**Example:**

| Message                                                 | Encoding | Segments | Cost impact |
| ------------------------------------------------------- | -------- | -------- | ----------- |
| `Hello, how are you?` (150 chars)                       | GSM-7    | 1        | Base cost   |
| `Hello, how are you?` (150 chars with `"smart quotes"`) | UTF-16   | 3        | 3× cost     |
| `Hello, how are you?` (same, smart encoding ON)         | GSM-7    | 1        | Base cost   |

Smart encoding is especially valuable when your message text originates from word processors, CMS platforms, or mobile keyboards that silently insert Unicode characters like curly quotes, em dashes, or non-breaking spaces.

## How it works

When smart encoding is enabled:

1. Your message text is scanned for Unicode characters that have GSM-7 equivalents.
2. Matching characters are automatically replaced (e.g., `"` → `"`, `—` → `-`, `…` → `...`).
3. The final encoding (GSM-7 or UTF-16) is determined **after** all substitutions.
4. The segment count is recalculated based on the transformed text.
5. The API response includes metadata about the transformation.

<Callout type="info">
  **Webhooks return the original text.** The `text` field in delivery webhooks contains your original message, not the smart-encoded version. This ensures your application's message tracking stays consistent.

## Enable smart encoding

You can enable smart encoding at two levels: on a **messaging profile** (applies to all messages) or on a **per-request** basis.

### On a messaging profile

Enable smart encoding as a default for all messages sent through a profile.

### API

      ```bash
      curl -X PATCH https://api.telnyx.com/v2/messaging_profiles/{profile_id} \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -d '{
          "smart_encoding": true
        }'
      ```

      ```javascript
      import Telnyx from 'telnyx';

      const client = new Telnyx({
        apiKey: process.env['TELNYX_API_KEY'],
      });

      const response = await client.messagingProfiles.update(
        'your_messaging_profile_id',
        { smart_encoding: true }
      );

      console.log(response.data);
      ```

      ```python
      import os
      from telnyx import Telnyx

      client = Telnyx(
          api_key=os.environ.get("TELNYX_API_KEY"),
      )

      response = client.messaging_profiles.update(
          "your_messaging_profile_id",
          smart_encoding=True,
      )

      print(response.data)
      ```

      ```ruby
      require "telnyx"

      client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

      response = client.messaging_profiles.update(
        "your_messaging_profile_id",
        smart_encoding: true
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
        response, err := client.MessagingProfiles.Update(
          context.TODO(),
          "your_messaging_profile_id",
          telnyx.MessagingProfileUpdateParams{
            SmartEncoding: telnyx.Bool(true),
          },
        )
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
      import com.telnyx.sdk.models.messagingprofiles.MessagingProfileUpdateParams;
      import com.telnyx.sdk.models.messagingprofiles.MessagingProfileUpdateResponse;

      public final class Main {
          public static void main(String[] args) {
              TelnyxClient client = TelnyxOkHttpClient.fromEnv();

              MessagingProfileUpdateParams params = MessagingProfileUpdateParams.builder()
                  .smartEncoding(true)
                  .build();

              MessagingProfileUpdateResponse response = client
                  .messagingProfiles()
                  .update("your_messaging_profile_id", params);

              System.out.println(response);
          }
      }
      ```

      ```csharp .NET theme={null}
      using Telnyx;

      TelnyxConfiguration.SetApiKey(Environment.GetEnvironmentVariable("TELNYX_API_KEY"));

      var service = new MessagingProfileService();
      var response = await service.UpdateAsync(
          "your_messaging_profile_id",
          new MessagingProfileUpdateOptions
          {
              SmartEncoding = true
          }
      );

      Console.WriteLine(response.Data);
      ```

      ```php
      <?php
      require_once 'vendor/autoload.php';

      \Telnyx\Telnyx::setApiKey(getenv('TELNYX_API_KEY'));

      $response = \Telnyx\MessagingProfile::Update(
          'your_messaging_profile_id',
          ['smart_encoding' => true]
      );

      print_r($response);
      ```

### Portal

1. **Go to Messaging**

        Navigate to [Messaging > Messaging Profiles](https://portal.telnyx.com/#/app/messaging) in the portal.

2. **Select your profile**

        Click on the messaging profile you want to update.

3. **Enable Smart Encoding**

        Toggle **Smart Encoding** to enabled.

4. **Save**

        Click **Save** to apply the change.

### Per-request control

Override the profile setting on individual messages using the `encoding` parameter:

| Value  | Behavior                                                                                                                                           |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `auto` | Follow the profile's `smart_encoding` setting (default).                                                                                           |
| `gsm7` | Force GSM-7 encoding. Smart encoding is applied. Returns `400` if the message contains characters that cannot be converted to GSM-7 (e.g., emoji). |
| `ucs2` | Force UCS-2 encoding. **Skips smart encoding entirely.**                                                                                           |

<Callout type="warning">
  The request-level `encoding` parameter **takes precedence** over the messaging profile's `smart_encoding` setting.

  ```bash
  curl -X POST https://api.telnyx.com/v2/messages \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -d '{
      "from": "+15551234567",
      "to": "+15559876543",
      "text": "Don\u2019t miss our \u201cflash sale\u201d \u2014 50% off!",
      "encoding": "auto"
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
    text: 'Don\u2019t miss our \u201cflash sale\u201d \u2014 50% off!',
    encoding: 'auto',
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
      text="Don\u2019t miss our \u201cflash sale\u201d \u2014 50% off!",
      encoding="auto",
  )

  print(response.data)
  ```

  ```ruby
  require "telnyx"

  client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

  response = client.messages.send_(
    from: "+15551234567",
    to: "+15559876543",
    text: "Don\u2019t miss our \u201cflash sale\u201d \u2014 50% off!",
    encoding: "auto"
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
      From:     "+15551234567",
      To:       "+15559876543",
      Text:     "Don\u2019t miss our \u201cflash sale\u201d \u2014 50% off!",
      Encoding: telnyx.String("auto"),
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
              .text("Don\u2019t miss our \u201cflash sale\u201d \u2014 50% off!")
              .encoding("auto")
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
      Text = "Don\u2019t miss our \u201cflash sale\u201d \u2014 50% off!",
      Encoding = "auto"
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
      'text' => "Don\u{2019}t miss our \u{201c}flash sale\u{201d} \u{2014} 50% off!",
      'encoding' => 'auto'
  ]);

  print_r($response);
  ```

## Response metadata

When smart encoding is applied, the API response includes detailed metadata:

```json theme={null}
{
  "data": {
    "id": "8a0c35c0-5eed-4c0e-b1f0-abc123456789",
    "type": "SMS",
    "encoding": "GSM-7",
    "parts": 1,
    "smart_encoding": {
      "smart_encoding_applied": true,
      "final_encoding": "gsm7",
      "segment_count": 1,
      "character_count": 155,
      "replaced_character_count": 3,
      "length_change": 2
    }
  }
}
```

| Field                      | Description                                                            |
| -------------------------- | ---------------------------------------------------------------------- |
| `smart_encoding_applied`   | Whether any characters were replaced.                                  |
| `final_encoding`           | The encoding used after transformation (`gsm7` or `ucs2`).             |
| `segment_count`            | Number of segments after smart encoding.                               |
| `character_count`          | Message length after transformation.                                   |
| `replaced_character_count` | Number of unique characters that were substituted.                     |
| `length_change`            | Difference in length (positive means message grew, e.g., `…` → `...`). |

> **Note:** The `parts` field in the top-level response reflects the segment count **after** smart encoding, so you always see the actual billing impact.

### Checking the response

  ```bash
  # Send and inspect the smart_encoding metadata
  curl -s -X POST https://api.telnyx.com/v2/messages \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -d '{
      "from": "+15551234567",
      "to": "+15559876543",
      "text": "Don\u2019t miss our \u201cflash sale\u201d \u2014 50% off!"
    }' | jq '.data.smart_encoding'
  ```

  ```javascript
  import Telnyx from 'telnyx';

  const client = new Telnyx({
    apiKey: process.env['TELNYX_API_KEY'],
  });

  const response = await client.messages.send({
    from: '+15551234567',
    to: '+15559876543',
    text: 'Don\u2019t miss our \u201cflash sale\u201d \u2014 50% off!',
  });

  if (response.data.smart_encoding?.smart_encoding_applied) {
    console.log('Smart encoding applied!');
    console.log(`Encoding: ${response.data.smart_encoding.final_encoding}`);
    console.log(`Segments: ${response.data.smart_encoding.segment_count}`);
    console.log(`Characters replaced: ${response.data.smart_encoding.replaced_character_count}`);
  }
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
      text="Don\u2019t miss our \u201cflash sale\u201d \u2014 50% off!",
  )

  smart = response.data.smart_encoding
  if smart and smart.smart_encoding_applied:
      print(f"Encoding: {smart.final_encoding}")
      print(f"Segments: {smart.segment_count}")
      print(f"Characters replaced: {smart.replaced_character_count}")
  ```

  ```ruby
  require "telnyx"

  client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

  response = client.messages.send_(
    from: "+15551234567",
    to: "+15559876543",
    text: "Don\u2019t miss our \u201cflash sale\u201d \u2014 50% off!"
  )

  smart = response.data.smart_encoding
  if smart&.smart_encoding_applied
    puts "Encoding: #{smart.final_encoding}"
    puts "Segments: #{smart.segment_count}"
    puts "Characters replaced: #{smart.replaced_character_count}"
  end
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
      Text: "Don\u2019t miss our \u201cflash sale\u201d \u2014 50% off!",
    })
    if err != nil {
      panic(err.Error())
    }
    if response.Data.SmartEncoding != nil && response.Data.SmartEncoding.SmartEncodingApplied {
      fmt.Printf("Encoding: %s\n", response.Data.SmartEncoding.FinalEncoding)
      fmt.Printf("Segments: %d\n", response.Data.SmartEncoding.SegmentCount)
      fmt.Printf("Replaced: %d\n", response.Data.SmartEncoding.ReplacedCharacterCount)
    }
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
              .text("Don\u2019t miss our \u201cflash sale\u201d \u2014 50% off!")
              .build();

          MessageSendResponse response = client.messages().send(params);

          var smart = response.data().smartEncoding();
          if (smart != null && smart.smartEncodingApplied()) {
              System.out.println("Encoding: " + smart.finalEncoding());
              System.out.println("Segments: " + smart.segmentCount());
              System.out.println("Replaced: " + smart.replacedCharacterCount());
          }
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
      Text = "Don\u2019t miss our \u201cflash sale\u201d \u2014 50% off!"
  });

  var smart = response.Data.SmartEncoding;
  if (smart?.SmartEncodingApplied == true)
  {
      Console.WriteLine($"Encoding: {smart.FinalEncoding}");
      Console.WriteLine($"Segments: {smart.SegmentCount}");
      Console.WriteLine($"Replaced: {smart.ReplacedCharacterCount}");
  }
  ```

  ```php
  <?php
  require_once 'vendor/autoload.php';

  \Telnyx\Telnyx::setApiKey(getenv('TELNYX_API_KEY'));

  $response = \Telnyx\Message::Create([
      'from' => '+15551234567',
      'to' => '+15559876543',
      'text' => "Don\u{2019}t miss our \u{201c}flash sale\u{201d} \u{2014} 50% off!"
  ]);

  $smart = $response->smart_encoding;
  if ($smart && $smart->smart_encoding_applied) {
      echo "Encoding: " . $smart->final_encoding . "\n";
      echo "Segments: " . $smart->segment_count . "\n";
      echo "Replaced: " . $smart->replaced_character_count . "\n";
  }
  ```

## Precedence rules

Smart encoding behavior is determined by a combination of your messaging profile setting and the per-request `encoding` parameter:

| Profile `smart_encoding` | Request `encoding` | Behavior                                                          |
| ------------------------ | ------------------ | ----------------------------------------------------------------- |
| `true`                   | *(not set)*        | Smart encoding **applied**                                        |
| `false`                  | *(not set)*        | Smart encoding **not applied**                                    |
| `true`                   | `auto`             | Smart encoding **applied**                                        |
| `false`                  | `auto`             | Smart encoding **not applied**                                    |
| `true` or `false`        | `gsm7`             | Smart encoding **applied**, must result in GSM-7 or returns `400` |
| `true` or `false`        | `ucs2`             | Smart encoding **skipped**, forced UCS-2                          |

<Callout type="info">
  The request-level `encoding` parameter always takes precedence over the messaging profile setting.

## Character substitutions

Smart encoding replaces 200+ Unicode characters with GSM-7 equivalents. The tables below show all supported substitutions grouped by category.

**Quotation marks**

  | Unicode | Glyph | Description                                       | Replacement |
  | ------- | ----- | ------------------------------------------------- | ----------- |
  | U+00AB  | «     | Left-pointing double angle quotation mark         | "           |
  | U+00BB  | »     | Right-pointing double angle quotation mark        | "           |
  | U+201C  | "     | Left double quotation mark                        | "           |
  | U+201D  | "     | Right double quotation mark                       | "           |
  | U+02BA  | ʺ     | Modifier letter double prime                      | "           |
  | U+02EE  | ˮ     | Modifier letter double apostrophe                 | "           |
  | U+201F  | ‟     | Double high-reversed-9 quotation mark             | "           |
  | U+275D  | ❝     | Heavy double turned comma quotation mark ornament | "           |
  | U+275E  | ❞     | Heavy double comma quotation mark ornament        | "           |
  | U+301D  | 〝     | Reversed double prime quotation mark              | "           |
  | U+301E  | 〞     | Double prime quotation mark                       | "           |
  | U+FF02  | ＂     | Fullwidth quotation mark                          | "           |
  | U+201E  | „     | Double low quotation mark                         | "           |

---

**Apostrophes and single quotes**

  | Unicode | Glyph | Description                                       | Replacement |
  | ------- | ----- | ------------------------------------------------- | ----------- |
  | U+2018  | '     | Left single quotation mark                        | '           |
  | U+2019  | '     | Right single quotation mark                       | '           |
  | U+02BB  | ʻ     | Modifier letter turned comma                      | '           |
  | U+02C8  | ˈ     | Modifier letter vertical line                     | '           |
  | U+02BC  | ʼ     | Modifier letter apostrophe                        | '           |
  | U+02BD  | ʽ     | Modifier letter reversed comma                    | '           |
  | U+02B9  | ʹ     | Modifier letter prime                             | '           |
  | U+201B  | ‛     | Single high-reversed-9 quotation mark             | '           |
  | U+FF07  | ＇     | Fullwidth apostrophe                              | '           |
  | U+00B4  | ´     | Acute accent                                      | '           |
  | U+02CA  | ˊ     | Modifier letter acute accent                      | '           |
  | U+0060  | \`    | Grave accent                                      | '           |
  | U+02CB  | ˋ     | Modifier letter grave accent                      | '           |
  | U+275B  | ❛     | Heavy single turned comma quotation mark ornament | '           |
  | U+275C  | ❜     | Heavy single comma quotation mark ornament        | '           |
  | U+0313  | ̓     | Combining comma above                             | '           |
  | U+0314  | ̔     | Combining reversed comma above                    | '           |
  | U+FE10  | ︐     | Presentation form for vertical comma              | '           |
  | U+FE11  | ︑     | Presentation form for vertical ideographic comma  | '           |

---

**Dashes and hyphens**

  | Unicode | Glyph | Description            | Replacement |
  | ------- | ----- | ---------------------- | ----------- |
  | U+2014  | —     | Em dash                | -           |
  | U+2013  | –     | En dash                | -           |
  | U+23BC  | ⎼     | Horizontal scan line-7 | -           |
  | U+23BD  | ⎽     | Horizontal scan line-9 | -           |
  | U+2015  | ―     | Horizontal bar         | -           |
  | U+FE63  | ﹣     | Small hyphen-minus     | -           |
  | U+FF0D  | －     | Fullwidth hyphen-minus | -           |
  | U+2010  | ‐     | Hyphen                 | -           |
  | U+2022  | •     | Bullet                 | -           |
  | U+2043  | ⁃     | Hyphen bullet          | -           |

---

**Slashes and division**

  | Unicode | Glyph | Description                     | Replacement |
  | ------- | ----- | ------------------------------- | ----------- |
  | U+00F7  | ÷     | Division sign                   | /           |
  | U+00BC  | ¼     | Vulgar fraction one quarter     | 1/4         |
  | U+00BD  | ½     | Vulgar fraction one half        | 1/2         |
  | U+00BE  | ¾     | Vulgar fraction three quarters  | 3/4         |
  | U+29F8  | ⧸     | Big solidus                     | /           |
  | U+0337  | ̷     | Combining short solidus overlay | /           |
  | U+0338  | ̸     | Combining long solidus overlay  | /           |
  | U+2044  | ⁄     | Fraction slash                  | /           |
  | U+2215  | ∕     | Division slash                  | /           |
  | U+FF0F  | ／     | Fullwidth solidus               | /           |

---

**Backslashes**

  | Unicode | Glyph | Description                       | Replacement |
  | ------- | ----- | --------------------------------- | ----------- |
  | U+29F9  | ⧹     | Big reverse solidus               | \\          |
  | U+29F5  | ⧵     | Reverse solidus operator          | \\          |
  | U+20E5  |       | Combining reverse solidus overlay | \\          |
  | U+FE68  | ﹨     | Small reverse solidus             | \\          |
  | U+FF3C  | ＼     | Fullwidth reverse solidus         | \\          |

---

**Underscores and vertical lines**

  | Unicode | Glyph | Description                           | Replacement |
  | ------- | ----- | ------------------------------------- | ----------- |
  | U+0332  | ̲     | Combining low line                    | \_          |
  | U+FF3F  | ＿     | Fullwidth low line                    | \_          |
  | U+2017  | ‗     | Double low line                       | \_          |
  | U+20D2  | ⃒     | Combining long vertical line overlay  | \|          |
  | U+20D3  | ⃓     | Combining short vertical line overlay | \|          |
  | U+2223  | ∣     | Divides                               | \|          |
  | U+FF5C  | ｜     | Fullwidth vertical line               | \|          |
  | U+23B8  | ⎸     | Left vertical box line                | \|          |
  | U+23B9  | ⎹     | Right vertical box line               | \|          |
  | U+23D0  | ⏐     | Vertical line extension               | \|          |
  | U+239C  | ⎜     | Left parenthesis extension            | \|          |
  | U+239F  | ⎟     | Right parenthesis extension           | \|          |

---

**Symbols and punctuation**

  | Unicode | Glyph | Description                                     | Replacement |
  | ------- | ----- | ----------------------------------------------- | ----------- |
  | U+FE6B  | ﹫     | Small commercial at sign                        | @           |
  | U+FF20  | ＠     | Fullwidth commercial at sign                    | @           |
  | U+FE69  | ﹩     | Small dollar sign                               | \$          |
  | U+FF04  | ＄     | Fullwidth dollar sign                           | \$          |
  | U+01C3  | ǃ     | Latin letter retroflex click                    | !           |
  | U+FE15  | ︕     | Presentation form for vertical exclamation mark | !           |
  | U+FE57  | ﹗     | Small exclamation mark                          | !           |
  | U+FF01  | ！     | Fullwidth exclamation mark                      | !           |
  | U+203C  | ‼     | Double exclamation mark                         | !!          |
  | U+FE5F  | ﹟     | Small number sign                               | #           |
  | U+FF03  | ＃     | Fullwidth number sign                           | #           |
  | U+FE6A  | ﹪     | Small percent sign                              | %           |
  | U+FF05  | ％     | Fullwidth percent sign                          | %           |
  | U+FE60  | ﹠     | Small ampersand                                 | &           |
  | U+FF06  | ＆     | Fullwidth ampersand                             | &           |
  | U+2026  | …     | Horizontal ellipsis                             | ...         |

---

**Commas**

  | Unicode | Glyph | Description                 | Replacement |
  | ------- | ----- | --------------------------- | ----------- |
  | U+201A  | ‚     | Single low-9 quotation mark | ,           |
  | U+0326  | ̦     | Combining comma below       | ,           |
  | U+FE50  | ﹐     | Small comma                 | ,           |
  | U+3001  | 、     | Ideographic comma           | ,           |
  | U+FE51  | ﹑     | Small ideographic comma     | ,           |
  | U+FF0C  | ，     | Fullwidth comma             | ,           |
  | U+FF64  | ､     | Halfwidth ideographic comma | ,           |

---

**Parentheses and brackets**

  | Unicode | Glyph | Description                                 | Replacement |
  | ------- | ----- | ------------------------------------------- | ----------- |
  | U+2768  | ❨     | Medium left parenthesis ornament            | (           |
  | U+276A  | ❪     | Medium flattened left parenthesis ornament  | (           |
  | U+FE59  | ﹙     | Small left parenthesis                      | (           |
  | U+FF08  | （     | Fullwidth left parenthesis                  | (           |
  | U+27EE  | ⟮     | Mathematical left flattened parenthesis     | (           |
  | U+2985  | ⦅     | Left white parenthesis                      | (           |
  | U+2769  | ❩     | Medium right parenthesis ornament           | )           |
  | U+276B  | ❫     | Medium flattened right parenthesis ornament | )           |
  | U+FE5A  | ﹚     | Small right parenthesis                     | )           |
  | U+FF09  | ）     | Fullwidth right parenthesis                 | )           |
  | U+27EF  | ⟯     | Mathematical right flattened parenthesis    | )           |
  | U+2986  | ⦆     | Right white parenthesis                     | )           |
  | U+2774  | ❴     | Medium left curly bracket ornament          | \{          |
  | U+FE5B  | ﹛     | Small left curly bracket                    | \{          |
  | U+FF5B  | ｛     | Fullwidth left curly bracket                | \{          |
  | U+2775  | ❵     | Medium right curly bracket ornament         | }           |
  | U+FE5C  | ﹜     | Small right curly bracket                   | }           |
  | U+FF5D  | ｝     | Fullwidth right curly bracket               | }           |
  | U+FF3B  | ［     | Fullwidth left square bracket               | \[          |
  | U+FF3D  | ］     | Fullwidth right square bracket              | ]           |

---

**Asterisks**

  | Unicode | Glyph | Description                                    | Replacement |
  | ------- | ----- | ---------------------------------------------- | ----------- |
  | U+204E  | ⁎     | Low asterisk                                   | \*          |
  | U+2217  | ∗     | Asterisk operator                              | \*          |
  | U+229B  | ⊛     | Circled asterisk operator                      | \*          |
  | U+2722  | ✢     | Four teardrop-spoked asterisk                  | \*          |
  | U+2723  | ✣     | Four balloon-spoked asterisk                   | \*          |
  | U+2724  | ✤     | Heavy four balloon-spoked asterisk             | \*          |
  | U+2725  | ✥     | Four club-spoked asterisk                      | \*          |
  | U+2731  | ✱     | Heavy asterisk                                 | \*          |
  | U+2732  | ✲     | Open center asterisk                           | \*          |
  | U+2733  | ✳     | Eight spoked asterisk                          | \*          |
  | U+273A  | ✺     | Sixteen pointed asterisk                       | \*          |
  | U+273B  | ✻     | Teardrop-spoked asterisk                       | \*          |
  | U+273C  | ✼     | Open center teardrop-spoked asterisk           | \*          |
  | U+273D  | ✽     | Heavy teardrop-spoked asterisk                 | \*          |
  | U+2743  | ❃     | Heavy teardrop-spoked pinwheel asterisk        | \*          |
  | U+2749  | ❉     | Balloon-spoked asterisk                        | \*          |
  | U+274A  | ❊     | Eight teardrop-spoked propeller asterisk       | \*          |
  | U+274B  | ❋     | Heavy eight teardrop-spoked propeller asterisk | \*          |
  | U+29C6  | ⧆     | Squared asterisk                               | \*          |
  | U+FE61  | ﹡     | Small asterisk                                 | \*          |
  | U+FF0A  | ＊     | Fullwidth asterisk                             | \*          |

---

**Math, comparison, periods, and colons**

  | Unicode | Glyph | Description                                  | Replacement |
  | ------- | ----- | -------------------------------------------- | ----------- |
  | U+02D6  | ˖     | Modifier letter plus sign                    | +           |
  | U+FE62  | ﹢     | Small plus sign                              | +           |
  | U+FF0B  | ＋     | Fullwidth plus sign                          | +           |
  | U+FE64  | ﹤     | Small less-than sign                         | `<`         |
  | U+FF1C  | ＜     | Fullwidth less-than sign                     | `<`         |
  | U+0347  | ͇     | Combining equals sign below                  | =           |
  | U+A78A  | ꞊     | Modifier letter short equals sign            | =           |
  | U+FE66  | ﹦     | Small equals sign                            | =           |
  | U+FF1D  | ＝     | Fullwidth equals sign                        | =           |
  | U+FE65  | ﹥     | Small greater-than sign                      | `>`         |
  | U+FF1E  | ＞     | Fullwidth greater-than sign                  | `>`         |
  | U+2039  | ‹     | Single left-pointing angle quotation mark    | `<`         |
  | U+203A  | ›     | Single right-pointing angle quotation mark   | `>`         |
  | U+3002  | 。     | Ideographic full stop                        | .           |
  | U+FE52  | ﹒     | Small full stop                              | .           |
  | U+FF0E  | ．     | Fullwidth full stop                          | .           |
  | U+FF61  | ｡     | Halfwidth ideographic full stop              | .           |
  | U+02D0  | ː     | Modifier letter triangular colon             | :           |
  | U+02F8  | ˸     | Modifier letter raised colon                 | :           |
  | U+2982  | ⦂     | Z notation type colon                        | :           |
  | U+A789  | ꞉     | Modifier letter colon                        | :           |
  | U+FE13  | ︓     | Presentation form for vertical colon         | :           |
  | U+FF1A  | ：     | Fullwidth colon                              | :           |
  | U+204F  | ⁏     | Reversed semicolon                           | ;           |
  | U+FE14  | ︔     | Presentation form for vertical semicolon     | ;           |
  | U+FE54  | ﹔     | Small semicolon                              | ;           |
  | U+FF1B  | ；     | Fullwidth semicolon                          | ;           |
  | U+FE16  | ︖     | Presentation form for vertical question mark | ?           |
  | U+FE56  | ﹖     | Small question mark                          | ?           |
  | U+FF1F  | ？     | Fullwidth question mark                      | ?           |

---

**Fullwidth digits**

  | Unicode | Glyph | Description           | Replacement |
  | ------- | ----- | --------------------- | ----------- |
  | U+FF10  | ０     | Fullwidth digit zero  | 0           |
  | U+FF11  | １     | Fullwidth digit one   | 1           |
  | U+FF12  | ２     | Fullwidth digit two   | 2           |
  | U+FF13  | ３     | Fullwidth digit three | 3           |
  | U+FF14  | ４     | Fullwidth digit four  | 4           |
  | U+FF15  | ５     | Fullwidth digit five  | 5           |
  | U+FF16  | ６     | Fullwidth digit six   | 6           |
  | U+FF17  | ７     | Fullwidth digit seven | 7           |
  | U+FF18  | ８     | Fullwidth digit eight | 8           |
  | U+FF19  | ９     | Fullwidth digit nine  | 9           |

---

**Fullwidth and small capital letters**

  **Fullwidth uppercase (U+FF21–U+FF3A)** → A–Z

  **Fullwidth lowercase (U+FF41–U+FF5A)** → a–z

  **Small capital letters:**

  | Unicode | Glyph | Description                  | Replacement |
  | ------- | ----- | ---------------------------- | ----------- |
  | U+1D00  | ᴀ     | Latin letter small capital A | A           |
  | U+0299  | ʙ     | Latin letter small capital B | B           |
  | U+1D04  | ᴄ     | Latin letter small capital C | C           |
  | U+1D05  | ᴅ     | Latin letter small capital D | D           |
  | U+1D07  | ᴇ     | Latin letter small capital E | E           |
  | U+A730  | ꜰ     | Latin letter small capital F | F           |
  | U+0262  | ɢ     | Latin letter small capital G | G           |
  | U+029C  | ʜ     | Latin letter small capital H | H           |
  | U+026A  | ɪ     | Latin letter small capital I | I           |
  | U+1D0A  | ᴊ     | Latin letter small capital J | J           |
  | U+1D0B  | ᴋ     | Latin letter small capital K | K           |
  | U+029F  | ʟ     | Latin letter small capital L | L           |
  | U+1D0D  | ᴍ     | Latin letter small capital M | M           |
  | U+0274  | ɴ     | Latin letter small capital N | N           |
  | U+1D0F  | ᴏ     | Latin letter small capital O | O           |
  | U+1D18  | ᴘ     | Latin letter small capital P | P           |
  | U+0280  | ʀ     | Latin letter small capital R | R           |
  | U+A731  | ꜱ     | Latin letter small capital S | S           |
  | U+1D1B  | ᴛ     | Latin letter small capital T | T           |
  | U+1D1C  | ᴜ     | Latin letter small capital U | U           |
  | U+1D20  | ᴠ     | Latin letter small capital V | V           |
  | U+1D21  | ᴡ     | Latin letter small capital W | W           |
  | U+028F  | ʏ     | Latin letter small capital Y | Y           |
  | U+1D22  | ᴢ     | Latin letter small capital Z | Z           |

---

**Greek letters**

  Greek capital letters that visually resemble Latin letters are substituted:

  | Unicode | Glyph | Description                  | Replacement |
  | ------- | ----- | ---------------------------- | ----------- |
  | U+0391  | Α     | Greek capital letter Alpha   | A           |
  | U+0392  | Β     | Greek capital letter Beta    | B           |
  | U+0395  | Ε     | Greek capital letter Epsilon | E           |
  | U+0397  | Η     | Greek capital letter Eta     | H           |
  | U+0399  | Ι     | Greek capital letter Iota    | I           |
  | U+039A  | Κ     | Greek capital letter Kappa   | K           |
  | U+039C  | Μ     | Greek capital letter Mu      | M           |
  | U+039D  | Ν     | Greek capital letter Nu      | N           |
  | U+039F  | Ο     | Greek capital letter Omicron | O           |
  | U+03A1  | Ρ     | Greek capital letter Rho     | P           |
  | U+03A4  | Τ     | Greek capital letter Tau     | T           |
  | U+03A7  | Χ     | Greek capital letter Chi     | X           |
  | U+03A5  | Υ     | Greek capital letter Upsilon | Y           |
  | U+0396  | Ζ     | Greek capital letter Zeta    | Z           |

---

**Tildes and circumflex**

  | Unicode | Glyph | Description                       | Replacement |
  | ------- | ----- | --------------------------------- | ----------- |
  | U+02C6  | ˆ     | Modifier letter circumflex accent | ^           |
  | U+0302  | ̂     | Combining circumflex accent       | ^           |
  | U+FF3E  | ＾     | Fullwidth circumflex accent       | ^           |
  | U+1DCD  | ᷍     | Combining double circumflex above | ^           |
  | U+02DC  | ˜     | Small tilde                       | \~          |
  | U+02F7  | ˷     | Modifier letter low tilde         | \~          |
  | U+0303  | ̃     | Combining tilde                   | \~          |
  | U+0330  | ̰     | Combining tilde below             | \~          |
  | U+0334  | ̴     | Combining tilde overlay           | \~          |
  | U+223C  | ∼     | Tilde operator                    | \~          |
  | U+FF5E  | ～     | Fullwidth tilde                   | \~          |

---

**Whitespace characters**

  These characters are replaced with a standard space or removed:

  | Unicode | Description               | Replacement |
  | ------- | ------------------------- | ----------- |
  | U+00A0  | No-break space            | (space)     |
  | U+2000  | En quad                   | (space)     |
  | U+2001  | Em quad                   | (space)     |
  | U+2002  | En space                  | (space)     |
  | U+2003  | Em space                  | (space)     |
  | U+2004  | Three-per-em space        | (space)     |
  | U+2005  | Four-per-em space         | (space)     |
  | U+2006  | Six-per-em space          | (space)     |
  | U+2007  | Figure space              | (space)     |
  | U+2008  | Punctuation space         | (space)     |
  | U+2009  | Thin space                | (space)     |
  | U+200A  | Hair space                | (space)     |
  | U+200B  | Zero width space          | (removed)   |
  | U+202F  | Narrow no-break space     | (space)     |
  | U+205F  | Medium mathematical space | (space)     |
  | U+3000  | Ideographic space         | (space)     |
  | U+FEFF  | Zero width no-break space | (removed)   |
  | U+2028  | Line separator            | (removed)   |
  | U+2029  | Paragraph separator       | (removed)   |
  | U+2060  | Word joiner               | (removed)   |

---

**Control characters**

  These control characters are removed or transformed:

  | Unicode | Description                 | Replacement |
  | ------- | --------------------------- | ----------- |
  | U+0009  | Tab                         | 7 spaces    |
  | U+0000  | Null                        | (removed)   |
  | U+0003  | End of text                 | (removed)   |
  | U+0004  | End of transmission         | (removed)   |
  | U+0010  | Escape                      | (removed)   |
  | U+0011  | Device control one          | (removed)   |
  | U+0012  | Device control two          | (removed)   |
  | U+0013  | Device control three        | (removed)   |
  | U+0014  | Device control four         | (removed)   |
  | U+0017  | End of transmission block   | (removed)   |
  | U+0019  | End of medium               | (removed)   |
  | U+0080  | C1 control codes            | (removed)   |
  | U+008D  | Reverse line feed           | (removed)   |
  | U+0090  | Device control string       | (removed)   |
  | U+009B  | Control sequence introducer | (removed)   |
  | U+009F  | Application program command | (removed)   |

  > **Warning:** Tab characters (U+0009) are converted to 7 spaces, which can significantly increase message length and affect segment count.

---

## Edge cases

**Message length increases**

  Some substitutions increase message length. For example:

  * Horizontal ellipsis (`…`) becomes three periods (`...`) — adds 2 characters
  * Tab (U+0009) becomes 7 spaces — adds 6 characters
  * Vulgar fractions like `½` become `1/2` — adds 2 characters

  The segment count is calculated **after** these replacements, so a message near the 160-character limit may become multi-part after transformation.

---

**Mixed replaceable and non-replaceable characters**

  If your message contains both replaceable Unicode characters and non-replaceable ones (like emojis), smart encoding still applies all possible substitutions. However, the non-replaceable characters will keep the message in UTF-16 encoding.

  This is still beneficial — fewer Unicode characters means a shorter UTF-16 message and potentially fewer segments.

---

**Extended GSM-7 characters**

  The characters `~`, `^`, `|`, `\`, `{`, `}`, `[`, `]` are part of the GSM-7 extended set and count as **2 characters** each when calculating segment length. Smart encoding accounts for this when determining the final segment count.

---

**Zero-width characters and empty messages**

  Zero-width characters (like U+200B zero-width space) are removed entirely. If your message consists entirely of zero-width or control characters that all get removed, the API returns a `400` error — messages cannot be empty after transformation.

---

**encoding=gsm7 with non-convertible characters**

  If you set `encoding=gsm7` on a request but the message contains characters that cannot be represented in GSM-7 (e.g., emoji), the API returns a `400` error rather than silently dropping characters.

---

## Limitations

* **SMS only** — MMS and RCS use UTF-8 encoding by default and are not affected by smart encoding.
* **Not all characters convert** — Emojis and non-Latin scripts (e.g., Chinese, Arabic, Cyrillic) have no GSM-7 equivalents and will still trigger UTF-16 encoding.
* **Visual differences** — Substitutions may slightly alter the appearance of your message. Review the character tables above to understand what changes will occur.
* **Length may increase** — Some substitutions produce longer output (e.g., `…` → `...`). Always check the response metadata for the actual segment count.

## Related resources

  - [Message Encoding](message-encoding.md) — Learn about GSM-7, UTF-16, and segment calculations.

  - [Send Your First Message](send-your-first-message.md) — Get started with the Telnyx Messaging API.

  - [Messaging Profiles API](https://developers.telnyx.com/api-reference/messaging-profiles/update-a-messaging-profile) — API reference for updating messaging profile settings.

  - [Messages API](https://developers.telnyx.com/api-reference/messages/send-a-message) — API reference for sending messages with encoding options.


## Related Pages

- [Message Encoding](../runbooks/message-encoding.md)
