---
title: Zapier Integration
summary: Connect Telnyx SMS to 7,000+ apps with Zapier.
sources:
  - url: https://developers.telnyx.com/docs/messaging/messages/zapier-integration/index
    content_hash: a4d09fb2112e3732286f4c24821ebc65236936068fecadbd1f1dc780db94ac72
updated_at: 2026-04-10T00:00:00Z
---

# Zapier Integration

Connect Telnyx SMS to 7,000+ apps with Zapier. Automate messaging workflows without code — send alerts, forward messages, and create auto-responders.

Connect Telnyx SMS messaging to 7,000+ apps using [Zapier](https://zapier.com/apps/telnyx/integrations) — no code required. Build automated workflows that send messages, forward inbound SMS, and respond to triggers from other services.

> **Note:** **When to use Zapier vs. the API:** Zapier is ideal for simple automations, prototyping, and connecting to third-party services without code. For high-volume messaging, complex logic, or production-critical workflows, use the [Telnyx Messaging API](send-your-first-message.md) directly.

## Prerequisites

* A [Telnyx account](https://portal.telnyx.com) with a messaging-enabled phone number
* A [Messaging Profile](../concepts/messaging-profiles-overview.md) configured with a webhook URL
* A [Zapier account](https://zapier.com/) (free tier available)
* Your Telnyx [v2 API Key](https://portal.telnyx.com/#/app/auth/v2)

***

## Connect Telnyx to Zapier

1. **Find the Telnyx integration**

    Go to the [Telnyx Zapier integration page](https://zapier.com/apps/telnyx/integrations) and click **Connect**.

2. **Authenticate**

    Enter your Telnyx v2 API key when prompted. This gives Zapier permission to send and receive messages on your behalf.

3. **Select a sender number**

    After authenticating, Zapier displays all phone numbers on your Telnyx account. Select the number you want to use for sending.

    > **Note:** Zapier does not support selecting a messaging profile directly — it lists individual numbers from your account. The number you choose must be assigned to a messaging profile with a webhook URL configured for inbound triggers to work.

***

## Available triggers and actions

| Type        | Name              | Description                                             |
| ----------- | ----------------- | ------------------------------------------------------- |
| **Trigger** | Receive a Message | Fires when an SMS/MMS is received on your Telnyx number |
| **Action**  | Send SMS          | Sends an SMS message from your Telnyx number            |

***

## Example workflows

### SMS Notifications

    ### Send SMS alerts from any app

    Connect any Zapier trigger to Telnyx SMS to send notifications:

    **Popular combinations:**

    * **Google Sheets** → new row → send SMS (e.g., new lead notification)
    * **Shopify** → new order → send SMS confirmation
    * **Google Calendar** → event starting → send SMS reminder
    * **Stripe** → payment received → send SMS receipt
    * **Typeform** → new response → send SMS follow-up

    **Setup:**

    1. Create a new Zap and select your trigger app (e.g., Google Sheets)
    2. Configure the trigger event (e.g., "New Spreadsheet Row")
    3. Add **Telnyx** as the action and select **Send SMS**
    4. Map fields from the trigger into the message:
       * **Source Number:** Select a Telnyx number from the dropdown — this is a fixed number from your account, not a mapped field from the trigger
       * **Destination Number:** Use a field from the trigger (e.g., a phone number column from Google Sheets) or enter a fixed number
       * **Message Content:** Compose your message using trigger data
    5. Test and turn on the Zap

### SMS Forwarding

    ### Forward inbound SMS to your phone

    Route messages received on your Telnyx number to your personal phone — useful for monitoring business numbers.

    **Setup:**

    1. Create a new Zap with **Telnyx → Receive a Message** as the trigger
    2. Add **Telnyx → Send SMS** as the action
    3. Configure the action:
       * **Source Number:** Your Telnyx number
       * **Destination Number:** Your personal number
       * **Message Content:** Use trigger fields:
         ```
         FWD FROM: {{From Phone Number}}
         BODY: {{Text}}
         ```
    4. Test and turn on the Zap

    > **Note:** You can also forward to email, Slack, or any other Zapier-supported app instead of (or in addition to) SMS.

### Auto-Responder

    ### Automatically reply to inbound messages

    Set up automatic replies for inbound messages — useful for business hours notices, keyword responses, or acknowledgments.

    **Setup:**

    1. Create a new Zap with **Telnyx → Receive a Message** as the trigger
    2. (Optional) Add a **Filter by Zapier** step to only reply to certain messages — for example, filter where `{{Text}}` contains "HOURS" or "INFO". Note: filtering requires a [Zapier paid plan](https://zapier.com/pricing) (Professional or higher)
    3. Add **Telnyx → Send SMS** as the action
    4. Configure the action:
       * **Source Number:** Your Telnyx number
       * **Destination Number:** Use `{{From Phone Number}}` from the trigger (replies to sender)
       * **Message Content:** Your auto-reply message
    5. Test and turn on the Zap

    > **Warning:** Be careful with auto-responders — they can create infinite loops if two Telnyx numbers with auto-responders message each other. Use filters to prevent this.

***

## Limitations

**Zapier polling delay**

    Zapier checks for new triggers on a schedule based on your plan:

    | Zapier Plan    | Polling Interval |
    | -------------- | ---------------- |
    | Free           | Every 15 minutes |
    | Starter        | Every 15 minutes |
    | Professional   | Every 2 minutes  |
    | Team / Company | Every 1 minute   |

    This means inbound messages may not trigger actions immediately. For real-time processing, use the [Telnyx Messaging API](send-your-first-message.md) with [webhooks](receiving-webhooks-for-messaging.md) directly.

---

**No MMS media support**

    The Telnyx Zapier integration supports **SMS only**. MMS media attachments are not included in the trigger data, and the Send SMS action does not support `media_urls`.

    For MMS, use the [Messaging API](send-your-first-message.md) directly.

---

**One sender number per action step**

    Each Telnyx **Send SMS** action step uses a single sender number selected from your account. To send from different numbers in the same Zap, add multiple Telnyx action steps — each with a different sender number.

---

**No message status tracking**

    The Zapier integration does not provide delivery status (sent, delivered, failed). For delivery tracking, use the API with [webhooks](receiving-webhooks-for-messaging.md) or [Message Detail Records](message-detail-records.md).

---

**Rate limits apply**

    Standard Telnyx [rate limits](rate-limiting.md) apply to messages sent via Zapier. If your Zap sends messages faster than your sender type allows, messages will be queued or rejected.

---

***

## Troubleshooting

**Test fails with 'invalid number format'**

    Ensure phone numbers include the country code with `+` prefix:

    * ✅ `+15551234567`
    * ❌ `5551234567`
    * ❌ `(555) 123-4567`

---

**Messages not being received by Zapier**

    1. Verify your Telnyx number is assigned to the correct messaging profile
    2. Check that the messaging profile has a webhook URL configured
    3. Ensure the Zap is turned **on** (not paused)
    4. Check Zapier's [task history](https://zapier.com/app/history) for errors
    5. On free plans, polling may take up to 15 minutes

---

**Authentication error when connecting**

    1. Verify your API key is a **v2 key** from the [Telnyx Portal](https://portal.telnyx.com/#/app/auth/v2)
    2. Ensure the key has not been revoked or expired
    3. Try removing the Telnyx connection in Zapier and re-adding it

---

**Zap triggers but message fails to send**

    Check the error in Zapier's task history. Common causes:

    * **40333:** Spend limit reached — increase your [daily spend limit](configurable-spend-limits.md)
    * **40318:** Queue full — you're sending too fast for your sender type
    * **40300:** Invalid `from` number — ensure the source number is assigned to a messaging profile in the Telnyx Portal

---

**Auto-responder creating infinite loop**

    If two numbers with auto-responders message each other, they create an infinite loop. Fix by:

    1. Adding a Zapier **Filter** step that checks if the sender is your own number
    2. Using a **delay** step to rate-limit responses
    3. Checking for duplicate messages within a time window

---

***

## Related resources

  - [Send Your First Message](send-your-first-message.md) — Use the Telnyx API directly for full messaging control.

  - [Webhooks](receiving-webhooks-for-messaging.md) — Real-time message delivery via webhooks (no polling delay).

  - [Telnyx on Zapier](https://zapier.com/apps/telnyx/integrations) — Browse all Telnyx Zapier integrations and templates.

  - [Messaging Profiles](../concepts/messaging-profiles-overview.md) — Configure the messaging profile used by your Zapier integration.


## Related Pages

- [LlamaIndex Integration](../runbooks/llamaindex-integration.md)
- [Langchain Integration](../runbooks/langchain-integration.md)
