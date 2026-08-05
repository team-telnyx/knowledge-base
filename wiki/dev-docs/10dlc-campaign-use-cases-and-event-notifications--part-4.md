---
title: 10DLC Campaign Use Cases and Event Notifications
summary: Comprehensive guide to Telnyx 10DLC campaign use cases, sample messages,
  opt-in/opt-out requirements, and webhook event notifications for brands, campaigns,
  and phone numbers. Includes SDK examples, retry policies, and campaign appeal mechanisms.
sources:
- url: https://developers.telnyx.com/docs/messaging/10dlc/campaign-use-cases
- url: https://developers.telnyx.com/docs/messaging/10dlc/event-notifications/index
updated_at: 2026-08-05T13:49:31Z
---

# 10DLC Campaign Use Cases and Event Notifications

*Part 4 of 8 — see also: [Part 1](10dlc-campaign-use-cases-and-event-notifications--part-1.md), [Part 2](10dlc-campaign-use-cases-and-event-notifications--part-2.md), [Part 3](10dlc-campaign-use-cases-and-event-notifications--part-3.md), [Part 5](10dlc-campaign-use-cases-and-event-notifications--part-5.md), [Part 6](10dlc-campaign-use-cases-and-event-notifications--part-6.md), [Part 7](10dlc-campaign-use-cases-and-event-notifications--part-7.md), [Part 8](10dlc-campaign-use-cases-and-event-notifications--part-8.md)*

Comprehensive guide to Telnyx 10DLC campaign use cases, sample messages, opt-in/opt-out requirements, and webhook event notifications for brands, campaigns, and phone numbers. Includes SDK examples, retry policies, and campaign appeal mechanisms.

## API Example: Registering a 2FA Campaign

**Python:**

```python
import telnyx

telnyx.api_key = "YOUR_API_KEY"

campaign = telnyx.TenDLCCampaign.create(
    brand_id="B000001",
    usecase="2FA",
    description="One-time verification codes for user login and password reset",
    sample1="Your Acme verification code is 847291. This code expires in 10 minutes.",
    sample2="Your login code for Acme is 523016. Don't share this code with anyone. Reply STOP to opt out.",
    sample3="Acme security code: 194738. Enter this code to complete your password reset.",
    message_flow="Users enter their phone number during login or password reset. A one-time code is sent via SMS. Users enter the code to authenticate.",
    help_message="Reply HELP for support or contact support@acme.com",
    optin_message="By entering your phone number, you agree to receive verification codes from Acme via SMS. Reply STOP to opt out.",
)
print(campaign.campaign_id)
```

**Node.js:**

```javascript
const telnyx = require('telnyx')('YOUR_API_KEY');

const campaign = await telnyx.tenDlcCampaigns.create({
  brand_id: 'B000001',
  usecase: '2FA',
  description: 'One-time verification codes for user login and password reset',
  sample1: 'Your Acme verification code is 847291. This code expires in 10 minutes.',
  sample2: "Your login code for Acme is 523016. Don't share this code with anyone. Reply STOP to opt out.",
  sample3: 'Acme security code: 194738. Enter this code to complete your password reset.',
  message_flow: 'Users enter their phone number during login or password reset. A one-time code is sent via SMS.',
  help_message: 'Reply HELP for support or contact support@acme.com',
  optin_message: 'By entering your phone number, you agree to receive verification codes from Acme via SMS. Reply STOP to opt out.',
});
console.log(campaign.data.campaign_id);
```

**Ruby:**

```ruby
require 'telnyx'

Telnyx.api_key = 'YOUR_API_KEY'

campaign = Telnyx::TenDlcCampaign.create(
  brand_id: 'B000001',
  usecase: '2FA',
  description: 'One-time verification codes for user login and password reset',
  sample1: 'Your Acme verification code is 847291. This code expires in 10 minutes.',
  sample2: "Your login code for Acme is 523016. Don't share this code with anyone. Reply STOP to opt out.",
  sample3: 'Acme security code: 194738. Enter this code to complete your password reset.',
  message_flow: 'Users enter their phone number during login or password reset.',
  help_message: 'Reply HELP for support or contact support@acme.com',
  optin_message: 'By entering your phone number, you agree to receive verification codes from Acme via SMS. Reply STOP to opt out.',
)
puts campaign.campaign_id
```

**Java:**

```java
import com.telnyx.sdk.ApiClient;
import com.telnyx.sdk.api.TenDlcApi;
import com.telnyx.sdk.model.CreateTenDlcCampaignRequest;

ApiClient client = new ApiClient();
client.setApiKey("YOUR_API_KEY");
TenDlcApi api = new TenDlcApi(client);

CreateTenDlcCampaignRequest request = new CreateTenDlcCampaignRequest()
    .brandId("B000001")
    .usecase("2FA")
    .description("One-time verification codes for user login and password reset")
    .sample1("Your Acme verification code is 847291. This code expires in 10 minutes.")
    .sample2("Your login code for Acme is 523016. Don't share this code with anyone. Reply STOP to opt out.")
    .sample3("Acme security code: 194738. Enter this code to complete your password reset.")
    .messageFlow("Users enter their phone number during login or password reset.")
    .helpMessage("Reply HELP for support or contact support@acme.com")
    .optinMessage("By entering your phone number, you agree to receive verification codes from Acme via SMS. Reply STOP to opt out.");

var campaign = api.createTenDlcCampaign(request);
System.out.println(campaign.getData().getCampaignId());
```

**.NET:**

```csharp
using Telnyx.net;

TelnyxConfiguration.SetApiKey("YOUR_API_KEY");

var service = new TenDlcCampaignService();
var campaign = service.Create(new TenDlcCampaignCreateOptions
{
    BrandId = "B000001",
    Usecase = "2FA",
    Description = "One-time verification codes for user login and password reset",
    Sample1 = "Your Acme verification code is 847291. This code expires in 10 minutes.",
    Sample2 = "Your login code for Acme is 523016. Don't share this code with anyone. Reply STOP to opt out.",
    Sample3 = "Acme security code: 194738. Enter this code to complete your password reset.",
    MessageFlow = "Users enter their phone number during login or password reset.",
    HelpMessage = "Reply HELP for support or contact support@acme.com",
    OptinMessage = "By entering your phone number, you agree to receive verification codes from Acme via SMS. Reply STOP to opt out.",
});
Console.WriteLine(campaign.CampaignId);
```

**PHP:**

```php
$telnyx = new \Telnyx\Telnyx('YOUR_API_KEY');

$campaign = \Telnyx\TenDlcCampaign::create([
    'brand_id' => 'B000001',
    'usecase' => '2FA',
    'description' => 'One-time verification codes for user login and password reset',
    'sample1' => 'Your Acme verification code is 847291. This code expires in 10 minutes.',
    'sample2' => "Your login code for Acme is 523016. Don't share this code with anyone. Reply STOP to opt out.",
    'sample3' => 'Acme security code: 194738. Enter this code to complete your password reset.',
    'message_flow' => 'Users enter their phone number during login or password reset.',
    'help_message' => 'Reply HELP for support or contact support@acme.com',
    'optin_message' => 'By entering your phone number, you agree to receive verification codes from Acme via SMS. Reply STOP to opt out.',
]);
echo $campaign->campaign_id;
```

**Go:**

```go
package main

import (
    "fmt"
    telnyx "github.com/telnyx/telnyx-go"
)

func main() {
    client := telnyx.NewClient("YOUR_API_KEY")

    campaign, err := client.TenDlc.Campaigns.Create(&telnyx.TenDlcCampaignParams{
        BrandID:     "B000001",
        Usecase:     "2FA",
        Description: "One-time verification codes for user login and password reset",
        Sample1:     "Your Acme verification code is 847291. This code expires in 10 minutes.",
        Sample2:     "Your login code for Acme is 523016. Don't share this code with anyone. Reply STOP to opt out.",
        Sample3:     "Acme security code: 194738. Enter this code to complete your password reset.",
        MessageFlow: "Users enter their phone number during login or password reset.",
        HelpMessage: "Reply HELP for support or contact support@acme.com",
        OptinMessage: "By entering your phone number, you agree to receive verification codes from Acme via SMS. Reply STOP to opt out.",
    })
    if err != nil {
        panic(err)
    }
    fmt.Println(campaign.CampaignID)
}
```
