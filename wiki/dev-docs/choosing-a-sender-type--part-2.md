---
title: Choosing a Sender Type
summary: A guide to selecting the right Telnyx messaging sender type — 10DLC long
  code, toll-free, short code, RCS, or alphanumeric sender ID — based on use case,
  region, throughput, and registration requirements, with a quick-start example for
  sending your first message.
sources:
- url: https://developers.telnyx.com/docs/messaging/getting-started/choosing-your-sender-type/index
updated_at: 2026-08-05T13:53:35Z
---

# Choosing a Sender Type

*Part 2 of 2 — see also: [Part 1](choosing-a-sender-type--part-1.md)*

A guide to selecting the right Telnyx messaging sender type — 10DLC long code, toll-free, short code, RCS, or alphanumeric sender ID — based on use case, region, throughput, and registration requirements, with a quick-start example for sending your first message.

## Quick Start: Send Your First Message

Once you've chosen your sender type, sending a message uses the same API regardless of sender:

```bash
curl -X POST https://api.telnyx.com/v2/messages \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "from": "+15551234567",
    "to": "+15559876543",
    "text": "Hello from Telnyx!"
  }'
```

```python
import telnyx

telnyx.api_key = "YOUR_API_KEY"

message = telnyx.Message.create(
    from_="+15551234567",
    to="+15559876543",
    text="Hello from Telnyx!"
)
print(message.id)
```

```javascript
const telnyx = require('telnyx')('YOUR_API_KEY');

const message = await telnyx.messages.create({
  from: '+15551234567',
  to: '+15559876543',
  text: 'Hello from Telnyx!'
});
console.log(message.data.id);
```

```ruby
require 'telnyx'

Telnyx.api_key = 'YOUR_API_KEY'

message = Telnyx::Message.create(
  from: '+15551234567',
  to: '+15559876543',
  text: 'Hello from Telnyx!'
)
puts message.id
```

```java
import com.telnyx.sdk.*;
import com.telnyx.sdk.api.MessagesApi;
import com.telnyx.sdk.model.CreateMessageRequest;

ApiClient client = Configuration.getDefaultApiClient();
client.setApiKey("YOUR_API_KEY");

MessagesApi api = new MessagesApi(client);
CreateMessageRequest request = new CreateMessageRequest()
    .from("+15551234567")
    .to("+15559876543")
    .text("Hello from Telnyx!");

api.createMessage(request);
```

```csharp
using Telnyx;

TelnyxConfiguration.SetApiKey("YOUR_API_KEY");

var service = new MessagingSenderIdService();
var message = service.CreateMessage(new NewMessage
{
    From = "+15551234567",
    To = "+15559876543",
    Text = "Hello from Telnyx!"
});
Console.WriteLine(message.Id);
```

```php
require 'vendor/autoload.php';

$telnyx = new \Telnyx\TelnyxClient('YOUR_API_KEY');

$message = $telnyx->messages->create([
    'from' => '+15551234567',
    'to' => '+15559876543',
    'text' => 'Hello from Telnyx!'
]);
echo $message->id;
```

```go
package main

import (
    "context"
    "fmt"
    telnyx "github.com/telnyx/telnyx-go"
)

func main() {
    client := telnyx.NewClient("YOUR_API_KEY")

    message, err := client.Messages.Create(context.Background(),
        &telnyx.MessageParams{
            From: "+15551234567",
            To:   "+15559876543",
            Text: "Hello from Telnyx!",
        },
    )
    if err != nil {
        panic(err)
    }
    fmt.Println(message.ID)
}
```

The `from` field determines your sender type automatically:

- **Phone number** (`+15551234567`) → Long code or toll-free
- **Short code** (`12345`) → Short code
- **Alphanumeric** (`"MyBrand"`) → Alphanumeric sender ID

You can also use a [Messaging Profile](messaging-profile.md) to let Telnyx select the best sender from your number pool.

## Next Steps

- [Send a Message](send-a-message.md) — Complete guide to sending your first SMS/MMS.
- [Messaging Profiles](messaging-profiles--part-1.md) — Configure number pools, webhooks, and features.
- [10DLC Rate Limits](10dlc-rate-limits.md) — Understand throughput tiers and daily caps.
- [10DLC Registration](10dlc-registration.md) — Register your brand and campaign for US A2P messaging.
- [Toll-Free Verification](toll-free-verification--part-1.md) — Verify your toll-free number for higher throughput.
- [Short Code Setup](short-code-setup.md) — Apply for a dedicated short code.
- [RCS Getting Started](rcs-getting-started--part-1.md) — Set up RCS business messaging with rich media.
- [Alphanumeric Sender ID](alphanumeric-sender-id.md) — Send branded one-way messages internationally.
- [Hosted SMS](hosted-sms.md) — Bring your existing numbers to Telnyx messaging.
