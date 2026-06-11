---
title: Telnyx Messaging Features
summary: Covers Telnyx messaging capabilities including MMS SMIL templates, Sticky
  Sender, URL Shortening, Zapier integration, toll-free verification, and the full
  WhatsApp Business messaging workflow from embedded signup through template management
  and message sending.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/smil-template
  content_hash: d29aa01a72d9457e2c15bca36d1a114fad0d8a8fd2d7b721484dbeb7d7ea9663
- url: https://developers.telnyx.com/docs/messaging/messages/sticky-sender/index
  content_hash: b60693e817349ec8df4be29ac868e8661434934e8c3047b7acc28151d7d666ae
- url: https://developers.telnyx.com/docs/messaging/messages/url-shortening/index
  content_hash: 4c488d1b1e1c401b24857bbee9b2dc380feeb3307e7bce07ecaa412fe56d304f
- url: https://developers.telnyx.com/docs/messaging/messages/zapier-integration
  content_hash: aad83743cb42ebbc89f6978b6f626af75781bd0d86f1dc76eec2c92463a1daa1
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/index
  content_hash: 4252b4aba3308d22e312c4bfc31ff2bf8b9dad3363bc6fa0d6dd8cc1765f4379
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/troubleshooting
  content_hash: 73f55d4531a2ff98fb6c9a7234dfb34e6b4429f9a1fdbc66b6c62d286cb29463
- url: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup
  content_hash: 2ed927e07af5e37713ddd6b340998cd8842b6303ef28e2428218537475463b8c
- url: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup/tech-provider
  content_hash: bb93e5d911b134f7064cd7997b82d901cca70eae5ee880c925434e16bb05f284
- url: https://developers.telnyx.com/docs/messaging/whatsapp/manage-templates
  content_hash: ed0efe6efb4a082f13f54662244ee901249886ad4eed11780a77d535efca8e89
- url: https://developers.telnyx.com/docs/messaging/whatsapp/quickstart/index
  content_hash: abd0f4264c0b578171e98a4800bc241b283f1640a411eb55d283297c41637ae9
- url: https://developers.telnyx.com/docs/messaging/whatsapp/send-messages/index
  content_hash: 6c916c387118b87a1258ad874d5461c0bf493edb141be63764cac4cb36a2cdcb
updated_at: 2026-06-11T10:38:44Z
---

# Telnyx Messaging Features

*Part 1 of 5 — see also: [Part 2](telnyx-messaging-features--part-2.md), [Part 3](telnyx-messaging-features--part-3.md), [Part 4](telnyx-messaging-features--part-4.md), [Part 5](telnyx-messaging-features--part-5.md)*

Covers Telnyx messaging capabilities including MMS SMIL templates, Sticky Sender, URL Shortening, Zapier integration, toll-free verification, and the full WhatsApp Business messaging workflow from embedded signup through template management and message sending.

## SMIL Templates for MMS Layout

SMIL (Synchronized Multimedia Integration Language) specifies how MMS media files are laid out. Telnyx generates SMIL automatically based on the `media_urls` and `text` fields in an MMS request. Advanced users can provide a custom `smil_template` parameter to control layout.

Template parameters are enclosed in double braces `{{ }}`. During SMIL construction, `{{ text }}` is replaced with the text content location, and `{{ 0 }}`, `{{ 1 }}`, etc. are replaced with the locations of the first, second, etc. URLs in the `media_urls` list.

Example template:

```xml
<smil>
  <head>
    <region id="Text" top="70%" left="0%" height="30%" width="100%" fit="scroll"/>
    <region id="Image" top="0%" left="0%" height="70%" width="100%" fit="meet"/>
  </head>
  <body>
    <par dur="10s">
      <text src="{{ text }}" region="Text" />
      <img src="{{ 0 }}" region="Image" />
    </par>
  </body>
</smil>
```

The template must be set in the `smil_template` parameter of the MMS request and properly JSON-escaped:

```json
{
  "from": "+13125551234",
  "to": "+18655551234",
  "text": "Hello from Telnyx",
  "media_urls": ["https://example.com/media.jpg"],
  "smil_template": "<smil>\n\t<head>\n\t\t<region id=\"Text\" top=\"70%\"..."
}
```

Many modern handsets (most notably iPhones) ignore SMIL and use their own layout algorithm.

## Sticky Sender

Sticky Sender ensures the same phone number is used every time your application messages a particular recipient, building familiarity and trust. It is part of Number Pool settings—you must have Number Pool enabled to use it.

### How It Works

1. **First message**: Telnyx selects a number from the pool (using weights, geomatch, or availability)
2. **Mapping created**: The recipient-to-sender pairing is stored
3. **Future messages**: The same sender is automatically reused for that recipient
4. **Mapping expires**: After 8 days of no messages, the mapping resets

| Scenario | Behavior |
|---|---|
| Message sent within 8 days | Same sender reused, timer resets |
| No messages for 8+ days | Mapping expires, new sender assigned |
| Sticky Sender disabled | All mappings cleared immediately |
| Number removed from profile | Mappings to that number cleared |
| Sticky number unavailable | New number selected, new mapping created |

### Configuration

Enable via API by patching your Messaging Profile:

```bash
curl -X PATCH "https://api.telnyx.com/v2/messaging_profiles/YOUR_PROFILE_ID" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "number_pool_settings": {
      "sticky_sender": true
    }
  }'
```

In the Portal, go to **Messaging**, edit your profile, toggle on **Number Pool**, check **Sticky Sender**, and save.

To disable, set `sticky_sender` to `false`. This immediately clears all mappings—previous mappings are not restored if you re-enable.

### Priority Order for Number Selection

1. **Sticky Sender** (if enabled and mapping exists)
2. **Geomatch** (if enabled and matching area code available)
3. **Weight distribution** (long code vs. toll-free preference)
4. **Skip unhealthy** (exclude poor-performing numbers)

When Sticky Sender and Geomatch are both enabled, Geomatch selects a number matching the recipient's area code on the first message, and Sticky Sender reuses that number thereafter. If a sticky number becomes unhealthy, the mapping is preserved and messages still route through that number (skip_unhealthy does not override sticky mappings). To force re-selection, temporarily disable and re-enable Sticky Sender.

## URL Shortening

Telnyx provides a URL Shortening service with custom links to improve brand awareness and bypass spam filters that block popular shortening sites. This feature requires activation by the Telnyx Sales Team.

### How It Works

When enabled, any message containing URLs with supported domains is converted to a custom shortened URL. For example, `https://bit.ly/78ejf9n` becomes `http://scdlchg.cc/b20`.

### Supported Domains

By default, only these domains are shortened:

- bit.do, bit.ly, carebank.site, drvline.site, eatngage.com, goo.gl, healthsettle.pw, ht.ly, is.gd, ow.ly, rebrand.ly, t.co, tiny.cc, tinyurl.com, x.co

To shorten all domains (not just the above), disable the `replace_blacklist_only` setting.

### Configuration

URL Shortening is enabled per Messaging Profile via the `url_shortener_settings` field:

```bash
curl -X PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --data '{"url_shortener_settings":
    {"domain": "arv.fyi",
     "prefix":"custom_prefix",
     "replace_blacklist_only": false,
     "send_webhooks": true}}' \
  "https://api.telnyx.com/v2/messaging_profiles/{YOUR_MESSAGING_PROFILE_ID}"
```

Key settings:

- **domain**: Your custom short domain
- **prefix**: Identifying prefix for shortened URLs
- **replace_blacklist_only**: Set `false` to shorten all URLs, not just supported domains
- **send_webhooks**: Receive webhooks when shortened links are clicked

To set up a custom domain, contact customer support with your customer ID, custom domains (which need AAA records), and the profile IDs to assign.

### Engagement Reports

View link click data via the Message Engagement Report in the Portal. Select a date range, choose messaging profiles, and generate the report. You can also download detailed click data.

## Zapier Integration

Connect Telnyx SMS to 7,000+ apps via [Zapier](https://zapier.com/apps/telnyx/integrations) without code. Zapier is ideal for simple automations and prototyping; for high-volume or production-critical workflows, use the Telnyx Messaging API directly.

### Prerequisites

- A Telnyx account with a messaging-enabled phone number
- A Messaging Profile configured with a webhook URL
- A Zapier account
- Your Telnyx v2 API Key

### Available Triggers and Actions

| Type | Name | Description |
|---|---|---|
| **Trigger** | Receive a Message | Fires when SMS/MMS is received on your Telnyx number |
| **Action** | Send SMS | Sends an SMS message from your Telnyx number |

### Example Workflows

**SMS alerts from any app**: Connect a trigger (e.g., Google Sheets new row, Shopify new order, Stripe payment) to the Telnyx Send SMS action.

**Forward inbound SMS**: Use Telnyx → Receive a Message as the trigger, then Telnyx → Send SMS as the action, forwarding to your personal number.

**Auto-responder**: Trigger on Receive a Message, optionally add a Filter step (requires Zapier paid plan), then Send SMS as the action replying with `{{From Phone Number}}` as the destination. Be cautious of infinite loops between two auto-responders.

### Limitations

- **Polling delay**: Free/Starter plans poll every 15 minutes; Professional every 2 minutes; Team/Company every 1 minute
- **SMS only**: No MMS media support in triggers or actions
- **One sender per action step**: Add multiple action steps to send from different numbers
- **No delivery status tracking**: Use the API with webhooks or MDRs instead
- **Rate limits apply**: Standard Telnyx rate limits apply to messages sent via Zapier

### Troubleshooting

- **Invalid number format**: Use `+15551234567` format with country code and `+` prefix
- **Messages not received**: Verify the number is assigned to the correct profile with a webhook URL; ensure the Zap is on
- **Authentication error**: Ensure you're using a v2 API key from the Telnyx Portal
- **Message fails to send**: Check Zapier task history for errors like 40333 (spend limit), 40318 (queue full), or 40300 (invalid from number)
