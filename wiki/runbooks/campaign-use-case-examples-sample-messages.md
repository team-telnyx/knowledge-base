---
title: Campaign Use Case Examples & Sample Messages
summary: Compliant sample messages, opt-in language, and content patterns for every 10DLC campaign use case type — ready to use in your TCR registration.
sources:
  - url: https://developers.telnyx.com/docs/messaging/10dlc/campaign-use-cases/index
    content_hash: 0928af2277fc9a751e5b5df07df69f841dc8ba4802f65a31c4a695fe90bc9170
updated_at: 2026-04-10T00:00:00Z
---

# Campaign Use Case Examples & Sample Messages

Compliant sample messages, opt-in language, and content patterns for every 10DLC campaign use case type — ready to use in your TCR registration.

Writing good sample messages is the #1 factor in getting your 10DLC campaign approved. Carriers reject campaigns when sample messages don't match the declared use case, lack opt-out language, or look like spam.

This guide provides ready-to-use sample messages, compliant opt-in language, and content patterns for every campaign use case type.

  **How carriers review sample messages:**

  * Must match the declared use case type
  * Must include opt-out language (STOP to opt out)
  * Must represent actual messages you'll send
  * Vague or generic samples get rejected

***

## Standard use cases

### 2FA / Two-Factor Authentication

The simplest use case — short, transactional, no marketing content.

**Sample messages (3 required)**

    **Sample 1:**

    ```
    Your Acme verification code is 847291. This code expires in 10 minutes. If you didn't request this, ignore this message.
    ```

    **Sample 2:**

    ```
    Your login code for Acme is 523016. Don't share this code with anyone. Reply STOP to opt out.
    ```

    **Sample 3:**

    ```
    Acme security code: 194738. Enter this code to complete your password reset. This code expires in 5 minutes.
    ```

---

**Opt-in language**

    ```
    By entering your phone number, you agree to receive one-time verification
    codes from [Brand] via SMS. Message frequency varies. Message and data rates
    may apply. Reply STOP to opt out.
    ```

---

**Tips for approval**

    * Keep messages under 160 characters
    * Include the code prominently
    * Add an expiry time
    * Don't include marketing content or links
    * Brand name should appear in the message

---

**API example — registering a 2FA campaign:**

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

  ```javascript Node.js theme={null}
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

  ```csharp .NET theme={null}
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

***

### Customer Care

Support conversations, ticket updates, and service messages.

**Sample messages (3 required)**

    **Sample 1:**

    ```
    Hi [Name], your support ticket #4521 has been updated. Our team has responded — view details at support.acme.com/tickets/4521. Reply STOP to opt out.
    ```

    **Sample 2:**

    ```
    Acme Support: Your return request for order #8834 has been approved. A prepaid label has been sent to your email. Questions? Reply HELP.
    ```

    **Sample 3:**

    ```
    Your appointment with Acme Support is confirmed for March 15 at 2:00 PM EST. Reply YES to confirm or RESCHEDULE to change. Reply STOP to unsubscribe.
    ```

---

**Opt-in language**

    ```
    By providing your phone number, you consent to receive customer service
    messages from [Brand] via SMS, including support ticket updates, appointment
    reminders, and service notifications. Message frequency varies. Msg & data
    rates may apply. Reply HELP for help, STOP to cancel.
    ```

---

**Tips for approval**

    * Messages should be reactive (responding to customer actions)
    * Include ticket/order numbers for context
    * Don't mix in promotional content
    * Keep a helpful, service-oriented tone
    * Include brand name in every message

---

***

### Delivery Notifications

Order confirmations, shipping updates, and delivery status.

**Sample messages (3 required)**

    **Sample 1:**

    ```
    Acme: Your order #99281 has shipped! Tracking: 1Z999AA10123456784. Estimated delivery: March 18. Track at acme.com/track. Reply STOP to opt out.
    ```

    **Sample 2:**

    ```
    Your Acme delivery is out for delivery and will arrive today between 2-6 PM. A photo confirmation will be sent upon delivery. Reply STOP to unsubscribe.
    ```

    **Sample 3:**

    ```
    Acme: Your package was delivered at 3:42 PM and left at front door. View delivery photo at acme.com/orders/99281. Reply STOP to opt out.
    ```

---

**Opt-in language**

    ```
    By placing an order, you agree to receive shipping and delivery updates from
    [Brand] via SMS. Message frequency varies based on order activity. Msg & data
    rates may apply. Reply STOP to cancel, HELP for help.
    ```

---

**Tips for approval**

    * Include order/tracking numbers
    * Messages should follow the order lifecycle
    * Include delivery estimates when available
    * Don't add promotional upsells in delivery messages

---

***

### Account Notifications

Password changes, billing alerts, account activity.

**Sample messages (3 required)**

    **Sample 1:**

    ```
    Acme: Your password was successfully changed on March 4, 2026. If you didn't make this change, contact support immediately at 1-800-555-0199. Reply STOP to opt out.
    ```

    **Sample 2:**

    ```
    Acme billing alert: Your payment of $49.99 was processed successfully. Your next billing date is April 4, 2026. View invoice at acme.com/billing. Reply STOP to unsubscribe.
    ```

    **Sample 3:**

    ```
    Acme: Your subscription plan was upgraded to Pro. Your new monthly rate is $79.99, effective immediately. Questions? Reply HELP. Reply STOP to opt out.
    ```

---

**Opt-in language**

    ```
    By creating an account, you consent to receive account-related notifications
    from [Brand] via SMS, including billing alerts, password changes, and account
    updates. Msg frequency varies. Msg & data rates apply. Reply STOP to cancel.
    ```

---

**Tips for approval**

    * Focus on account changes the user initiated
    * Include specific details (amounts, dates)
    * Provide a way to verify or dispute changes
    * Never include marketing in account notifications

---

***

### Marketing

Promotions, sales, product announcements, and brand content.

> **Warning:** Marketing campaigns receive the most scrutiny. Opt-in must be explicit and separate from terms of service.

**Sample messages (3 required)**

    **Sample 1:**

    ```
    Acme Summer Sale! 🎉 Get 30% off all items this weekend only. Use code SUMMER30 at checkout. Shop now: acme.com/sale. Reply STOP to opt out.
    ```

    **Sample 2:**

    ```
    New at Acme: Our spring collection just dropped! Be the first to shop 50+ new styles starting at $19.99. Browse: acme.com/new. Txt STOP to unsubscribe.
    ```

    **Sample 3:**

    ```
    Acme: Thanks for being a loyal customer! Here's an exclusive 20% off coupon just for you. Use code VIP20 by March 31. Shop: acme.com. Reply STOP to cancel.
    ```

---

**Opt-in language**

    ```
    By checking this box, you agree to receive recurring marketing messages from
    [Brand] via SMS, including promotions, sales, and product updates. Consent is
    not a condition of purchase. Message frequency varies (up to 8 msgs/month).
    Msg & data rates may apply. Reply HELP for help, STOP to unsubscribe.
    View our Privacy Policy at [link] and Terms at [link].
    ```

---

**Tips for approval**

    * Opt-in MUST be separate from ToS (not buried in fine print)
    * Include message frequency estimate
    * State "consent is not a condition of purchase"
    * Link to privacy policy and terms
    * Every message must include opt-out language
    * Don't use ALL CAPS excessively
    * Include brand name in every message

---

***

### Security Alerts

Login alerts, fraud detection, and security notifications.

**Sample messages (3 required)**

    **Sample 1:**

    ```
    Acme security alert: New login detected from Chrome on Windows in New York, NY at 3:42 PM EST. If this wasn't you, secure your account: acme.com/security. Reply STOP to opt out.
    ```

    **Sample 2:**

    ```
    Acme: Unusual activity detected on your account. A purchase of $299.99 was attempted. If this wasn't you, reply BLOCK or call 1-800-555-0199. Reply STOP to unsubscribe.
    ```

    **Sample 3:**

    ```
    Acme: Your account recovery email was changed. If you made this change, no action needed. If not, contact security immediately at 1-800-555-0199. Reply STOP to opt out.
    ```

---

**Opt-in language**

    ```
    By enabling security alerts, you agree to receive security notifications from
    [Brand] via SMS, including login alerts, fraud detection, and account security
    updates. Message frequency varies based on account activity. Msg & data rates
    may apply. Reply STOP to cancel.
    ```

---

**Tips for approval**

    * Include specific details (device, location, time)
    * Always provide a way to take action
    * Keep urgency appropriate — don't create false panic
    * These are high-priority; carriers are lenient but still review

---

***

### Polling & Voting

Surveys, feedback requests, and interactive polls.

**Sample messages (3 required)**

    **Sample 1:**

    ```
    Acme: How was your recent purchase? Rate your experience 1-5 (1=poor, 5=excellent). Your feedback helps us improve! Reply STOP to opt out.
    ```

    **Sample 2:**

    ```
    Acme customer survey: Would you recommend us to a friend? Reply YES or NO. As a thank you, get 10% off your next order. Reply STOP to unsubscribe.
    ```

    **Sample 3:**

    ```
    Acme: Quick poll — which new feature matters most to you? Reply A) Faster shipping B) More colors C) Lower prices. Reply STOP to opt out.
    ```

---

**Opt-in language**

    ```
    By opting in, you agree to receive occasional survey and feedback requests
    from [Brand] via SMS. Message frequency: up to 2 msgs/month. Msg & data
    rates may apply. Reply STOP to opt out, HELP for help.
    ```

---

**Tips for approval**

    * Keep surveys short (1-2 questions per message)
    * Make responses simple (numbers, YES/NO, letters)
    * Don't disguise marketing as surveys
    * Include clear opt-out in every message

---

***

### Charity / Nonprofit

Fundraising, awareness campaigns, and donation acknowledgments.

**Sample messages (3 required)**

    **Sample 1:**

    ```
    Habitat for Hope: Thanks to donors like you, we built 12 homes this month! See the impact at habitatforhope.org/impact. Reply STOP to opt out.
    ```

    **Sample 2:**

    ```
    Habitat for Hope: Our spring fundraiser starts March 15! Your $25 donation provides building materials for a family in need. Donate: habitatforhope.org/give. Reply STOP to unsubscribe.
    ```

    **Sample 3:**

    ```
    Thank you for your $50 donation to Habitat for Hope! Your tax receipt has been emailed. Together we're building stronger communities. Reply STOP to opt out.
    ```

---

**Opt-in language**

    ```
    By texting JOIN to [number], you agree to receive updates from [Nonprofit]
    via SMS, including impact updates, fundraising campaigns, and donation
    receipts. Msg frequency varies (up to 4 msgs/month). Msg & data rates apply.
    Reply STOP to cancel, HELP for help.
    ```

---

**Tips for approval**

    * Clearly identify your nonprofit in every message
    * Show impact, not just ask for money
    * Include donation receipts/acknowledgments
    * Link to your organization's website

---

***

### Mixed (Most Common)

Multiple message types from a single campaign. This is the most frequently used use case.

**Sample messages (3 required — show variety)**

    **Sample 1 (transactional):**

    ```
    Acme: Your order #77412 has shipped and will arrive by March 18. Track at acme.com/track. Reply STOP to opt out.
    ```

    **Sample 2 (support):**

    ```
    Acme Support: Your ticket #2291 has been resolved. If you need further help, reply to this message or visit support.acme.com. Reply STOP to unsubscribe.
    ```

    **Sample 3 (promotional):**

    ```
    Acme: Spring sale starts tomorrow! Get early access with code SPRING25 for 25% off. Shop: acme.com/sale. Reply STOP to opt out.
    ```

---

**Opt-in language**

    ```
    By providing your phone number, you consent to receive messages from [Brand]
    via SMS, including order updates, customer support notifications, and
    promotional offers. Message frequency varies. Msg & data rates may apply.
    Consent is not required for purchase. Reply HELP for help, STOP to cancel.
    View our Privacy Policy at [link].
    ```

---

**Tips for approval**

    * Each sample should demonstrate a DIFFERENT message type
    * Opt-in must mention ALL types of messages (transactional + marketing)
    * If you include marketing, follow marketing opt-in rules
    * Description should list all message categories
    * This is the safest choice if you're unsure which use case to pick

---

***

## Special use cases

### Low Volume

For brands sending fewer than 6,000 messages per month. Simplified registration with reduced documentation.

**Sample messages**

    Same as whatever your primary use case is — low volume is about throughput, not content type. Use samples from the relevant standard use case above.

---

**Tips for approval**

    * Best for small businesses with limited messaging needs
    * Lower throughput limits (75 messages/minute on T-Mobile)
    * Cannot be upgraded to standard — must create a new campaign
    * Still requires compliant opt-in and opt-out

---

### Sole Proprietor

For individuals or small businesses without an EIN. See the full [Sole Proprietor guide](sole-proprietor-10dlc-registration.md).

### Emergency

For life-safety alerts. Requires demonstrating genuine emergency nature.

**Sample messages**

    **Sample 1:**

    ```
    EMERGENCY ALERT: Severe weather warning for your area. Tornado watch until 8 PM. Seek shelter immediately. Details: alerts.example.com. Reply STOP to opt out.
    ```

    **Sample 2:**

    ```
    SafeAlert: Building evacuation in progress at 123 Main St. Exit via stairwell B. Do NOT use elevators. All clear will be sent when safe. Reply STOP to opt out.
    ```

---

**Tips for approval**

    * Must be genuinely life-safety related
    * Carriers may grant higher throughput
    * Don't abuse this category — misuse leads to suspension

---

***

## Writing compliant sample messages

### Do's and don'ts

  - [✅ Do](#) — * Include your brand name in every message
    * Add opt-out language (STOP to opt out)
    * Use specific, realistic content
    * Match samples to your declared use case
    * Show the actual format you'll send
    * Include 3 distinct sample messages

  - [❌ Don't](#) — * Use generic placeholder text ("Hello, this is a test")
    * Mix marketing into transactional use cases
    * Use ALL CAPS for entire messages
    * Include URL shorteners (bit.ly, tinyurl)
    * Copy samples from other brands
    * Submit identical or near-identical samples

### Opt-out language requirements

Every campaign must support these keywords:

| Keyword            | Required Response                                                                                                                     |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| `STOP`             | "You have been unsubscribed from \[Brand] messages. No more messages will be sent. Reply START to resubscribe."                       |
| `HELP`             | "\[Brand] support: For help, visit \[url] or call \[number]. Msg & data rates may apply. Msg frequency varies. Reply STOP to cancel." |
| `START` / `UNSTOP` | "You have been resubscribed to \[Brand] messages. Reply STOP to opt out, HELP for help."                                              |

  Telnyx handles STOP/START/HELP keyword processing automatically when [Advanced Opt-Out](https://developers.telnyx.com/docs/messaging/messages/opt-out-opt-in/index) is enabled on your messaging profile.

### Message flow description

Your campaign's `message_flow` field should clearly describe how users opt in. Carriers look for:

1. **Entry point**

    How does the user first provide their phone number? (Website form, checkout, text-to-join keyword, etc.)

2. **Consent mechanism**

    How is consent captured? (Checkbox, keyword reply, verbal confirmation, etc.)

3. **Confirmation**

    What happens after opt-in? (Welcome message, double opt-in confirmation, etc.)

4. **Message types**

    What kinds of messages will the user receive?

**Example message flow:**

```
Customers opt in by checking a consent checkbox during online checkout at
acme.com/checkout. After opting in, they receive a welcome message confirming
their subscription. They then receive order confirmations, shipping updates,
and delivery notifications related to their purchases. Customers can opt out
at any time by replying STOP.
```

***

## Common rejection reasons

| Rejection Reason                            | Fix                                                           |
| ------------------------------------------- | ------------------------------------------------------------- |
| Sample messages don't match use case        | Rewrite samples to clearly demonstrate your declared use case |
| Missing opt-out language                    | Add "Reply STOP to opt out" to every sample                   |
| Vague or generic samples                    | Use specific, realistic content with your brand name          |
| Inadequate opt-in description               | Detail the exact opt-in flow (where, how, what users see)     |
| URL shorteners used                         | Use full branded URLs (acme.com/track, not bit.ly/abc)        |
| Samples too similar                         | Make each sample distinctly different                         |
| Marketing content in non-marketing use case | Remove promotional language or switch to MIXED use case       |

  For detailed troubleshooting of campaign rejections, see the [10DLC Troubleshooting Guide](10dlc-troubleshooting-guide.md).

***

## Related resources

  - [Campaign Registration](10dlc-campaign-registration.md) — Register your campaign via API or Portal

  - [Brand Registration](10dlc-brand-registration.md) — Register your brand with TCR first

  - [10DLC Troubleshooting](10dlc-troubleshooting-guide.md) — Fix registration and delivery issues
