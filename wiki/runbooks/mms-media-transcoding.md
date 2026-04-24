---
title: MMS Media & Transcoding
summary: Send MMS messages with media attachments.
sources:
  - url: https://developers.telnyx.com/docs/messaging/messages/mms-transcoding/index
    content_hash: 7ca0c41e45e34883e7f50bf97dfff595461ef479e925ead59562663704a628b7
updated_at: 2026-04-10T00:00:00Z
---

# MMS Media & Transcoding

Send MMS messages with media attachments. Understand carrier size limits, supported formats, and automatic transcoding.

MMS messages let you send images, videos, and other media files alongside text. This guide covers supported media types, carrier size limits, and how to use Telnyx's automatic transcoding to ensure delivery.

> **Note:** MMS is supported on Long Code, Toll-Free, and Short Code numbers in the US and Canada. International MMS support varies by carrier.

## Send an MMS message

Include one or more `media_urls` in your message request to send an MMS:

  ```bash
  curl -X POST https://api.telnyx.com/v2/messages \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -d '{
      "from": "+15551234567",
      "to": "+15559876543",
      "text": "Check out this image!",
      "media_urls": ["https://example.com/image.jpg"]
    }'
  ```

  ```python
  import os
  from telnyx import Telnyx

  client = Telnyx(api_key=os.environ.get("TELNYX_API_KEY"))

  response = client.messages.send(
      from_="+15551234567",
      to="+15559876543",
      text="Check out this image!",
      media_urls=["https://example.com/image.jpg"],
  )

  print(response.data)
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
    media_urls: ['https://example.com/image.jpg'],
  });

  console.log(response.data);
  ```

  ```ruby
  require "telnyx"

  client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

  response = client.messages.send_(
    from: "+15551234567",
    to: "+15559876543",
    text: "Check out this image!",
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

  import java.util.List;

  public final class Main {
      public static void main(String[] args) {
          TelnyxClient client = TelnyxOkHttpClient.fromEnv();

          var params = MessageSendParams.builder()
              .from("+15551234567")
              .to("+15559876543")
              .text("Check out this image!")
              .mediaUrls(List.of("https://example.com/image.jpg"))
              .build();

          var response = client.messages().send(params);
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
      MediaUrls = new List<string> { "https://example.com/image.jpg" }
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
      'media_urls' => ['https://example.com/image.jpg']
  ]);

  print_r($response);
  ```

> **Note:** You can include up to **10 media URLs** per MMS message. Each URL must be publicly accessible — Telnyx fetches the media at send time.

***

## Supported media types

| Category  | Formats                         | Notes                                 |
| --------- | ------------------------------- | ------------------------------------- |
| Images    | JPEG, PNG, GIF, BMP, TIFF, WebP | Most widely supported across carriers |
| Video     | MP4, 3GP, MOV                   | H.264 codec recommended               |
| Audio     | MP3, WAV, AMR, OGG              | Limited carrier support               |
| Documents | PDF, vCard (.vcf), iCal (.ics)  | Limited carrier support               |

> **Warning:** **Animated GIFs** are not supported for transcoding. If you send animated GIFs, ensure they are under the carrier size limit — they will not be resized.

***

## Carrier size limits

Each US carrier imposes different maximum MMS message sizes based on the sender type. Messages exceeding these limits will be rejected by the carrier.

| Carrier  | Long Code | Toll-Free | Short Code |
| -------- | --------- | --------- | ---------- |
| AT\&T    | 1 MB      | 600 KB    | 600 KB     |
| T-Mobile | 1.5 MB    | 600 KB    | 1 MB       |
| Verizon  | 1 MB      | 600 KB    | 1.2 MB     |

> **Warning:** The **safe maximum** across all carriers and sender types is **600 KB**. To guarantee delivery to all recipients regardless of carrier, keep your total media under this limit — or enable transcoding.

***

## Automatic transcoding

Telnyx can automatically resize media to comply with carrier size limits. When enabled, oversized images and videos are resized before delivery.

### How transcoding works

1. You send an MMS with media that exceeds the destination carrier's size limit
2. Telnyx detects the destination carrier and its size restriction
3. Media is resized to fit within the limit:
   * **Images** → converted to JPEG
   * **Videos** → converted to H.264 MP4
4. The resized media is delivered to the recipient

> **Note:** Transcoding reduces media quality to meet size constraints. For best results, optimize your media before sending.

### Enable transcoding

Enable `mms_transcoding` on your messaging profile to apply it to all MMS sent through that profile.

### API

      ```bash
      curl -X PATCH https://api.telnyx.com/v2/messaging_profiles/{profile_id} \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -d '{
          "mms_transcoding": true
        }'
      ```

      ```python
      import os
      from telnyx import Telnyx

      client = Telnyx(api_key=os.environ.get("TELNYX_API_KEY"))

      response = client.messaging_profiles.update(
          "your_messaging_profile_id",
          mms_transcoding=True,
      )

      print(response.data)
      ```

      ```javascript
      import Telnyx from 'telnyx';

      const client = new Telnyx({
        apiKey: process.env['TELNYX_API_KEY'],
      });

      const response = await client.messagingProfiles.update(
        'your_messaging_profile_id',
        { mms_transcoding: true }
      );

      console.log(response.data);
      ```

      ```ruby
      require "telnyx"

      client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

      response = client.messaging_profiles.update(
        "your_messaging_profile_id",
        mms_transcoding: true
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
            MMSTranscoding: telnyx.Bool(true),
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

      public final class Main {
          public static void main(String[] args) {
              TelnyxClient client = TelnyxOkHttpClient.fromEnv();

              var params = MessagingProfileUpdateParams.builder()
                  .mmsTranscoding(true)
                  .build();

              var response = client.messagingProfiles()
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
              MmsTranscoding = true
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
          ['mms_transcoding' => true]
      );

      print_r($response);
      ```

### Portal

1. **Go to Messaging Profiles**

        Navigate to [Messaging > Messaging Profiles](https://portal.telnyx.com/#/app/messaging) in the portal.

2. **Select your profile**

        Click on the messaging profile you want to update.

3. **Enable MMS Transcoding**

        Toggle **MMS Transcoding** to enabled.

4. **Save**

        Click **Save** to apply.

***

## Best practices

**Optimize media before sending**

    Pre-optimize your media for the best balance of quality and deliverability:

    * **Images:** Resize to 640×480 or smaller, use JPEG at 80% quality
    * **Videos:** Compress to H.264, keep under 30 seconds, target 480p
    * **Target size:** Stay under 600 KB for universal carrier compatibility

    This gives you control over quality rather than relying on automatic transcoding.

---

**Use publicly accessible URLs**

    Media URLs must be publicly accessible — Telnyx fetches them at send time. Ensure:

    * URLs don't require authentication
    * URLs respond quickly (timeouts cause delivery failures)
    * URLs return the correct `Content-Type` header
    * URLs use HTTPS for security

---

**Handle inbound MMS media**

    Inbound MMS media URLs in webhooks are **ephemeral** — they expire after a short period. Always download and store important media to your own storage (e.g., AWS S3) immediately upon receiving the webhook.

    See the [Send & Receive MMS](send-receive-mms.md) tutorial for a complete implementation.

---

**Consider SMS for text-only messages**

    If your message doesn't include media, send it as SMS instead of MMS. SMS is:

    * **Cheaper** — MMS messages cost more than SMS
    * **Faster** — No media download/processing overhead
    * **More reliable** — Fewer points of failure

    Only use MMS when you actually need to include media content.

---

***

## Related resources

  - [Send & Receive MMS Tutorial](send-receive-mms.md) — Full tutorial for building an MMS application with media storage.

  - [SMIL Templates](modifying-mms-smil-template.md) — Customize the layout of your MMS media with SMIL templates.

  - [Send Your First Message](send-your-first-message.md) — Get started with the Telnyx Messaging API.

  - [Messages API Reference](https://developers.telnyx.com/api-reference/messages/send-a-message) — API reference for sending messages with media.
