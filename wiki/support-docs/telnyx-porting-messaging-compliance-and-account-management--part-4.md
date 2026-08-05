---
title: Telnyx Porting, Messaging Compliance, and Account Management
summary: This page consolidates Telnyx guidance on porting numbers from Skype and
  VoIP resellers, resolving Canadian reseller porting errors, cancelling accounts,
  configuring Skype for Business SIP trunks, toll-free messaging verification and
  opt-in workflows, SMS opt-out keywords, WhatsApp conversation windows, and handling
  toll-free carrier rejections.
sources:
- url: https://support.telnyx.com/en/articles/10715399-porting-away-from-skype
- url: https://support.telnyx.com/en/articles/1130619-invalid-reseller-error
- url: https://support.telnyx.com/en/articles/1130689-how-do-i-cancel-my-account
- url: https://support.telnyx.com/en/articles/1130698-skype-set-up-skype-for-biz-sip-trunk
- url: https://support.telnyx.com/en/articles/11898569-toll-free-opt-in-workflow-description
- url: https://support.telnyx.com/en/articles/1270091-sms-opt-out-keywords-and-stop-words
- url: https://support.telnyx.com/en/articles/13986482-whatsapp-24-hour-conversation-window
- url: https://support.telnyx.com/en/articles/14708130-porting-numbers-away-from-resellers-aircall-intercom-ringcentral-vonage-etc
- url: https://support.telnyx.com/en/articles/15138019-toll-free-carrier-rejections
- url: https://support.telnyx.com/en/articles/5353868-toll-free-messaging
- url: https://support.telnyx.com/en/articles/6989758-toll-free-opt-out-words
updated_at: 2026-08-05T13:26:16Z
---

# Telnyx Porting, Messaging Compliance, and Account Management

*Part 4 of 5 — see also: [Part 1](telnyx-porting-messaging-compliance-and-account-management--part-1.md), [Part 2](telnyx-porting-messaging-compliance-and-account-management--part-2.md), [Part 3](telnyx-porting-messaging-compliance-and-account-management--part-3.md), [Part 5](telnyx-porting-messaging-compliance-and-account-management--part-5.md)*

This page consolidates Telnyx guidance on porting numbers from Skype and VoIP resellers, resolving Canadian reseller porting errors, cancelling accounts, configuring Skype for Business SIP trunks, toll-free messaging verification and opt-in workflows, SMS opt-out keywords, WhatsApp conversation windows, and handling toll-free carrier rejections.

## SMS Opt-Out Keywords and Stop Words

Telnyx automatically processes incoming messages and recognises English-language stop words. When a stop word is identified, the person's phone number is added to the opt-out list and no further messages can be sent to that number.

### Opt-Outs at the Messaging Profile Level

This is default behaviour when creating an account. Any further messages from numbers on the same messaging profile sent to a number on the opt-out list will not be processed. For example, if Messaging Profile X has numbers 1-222-222-2222 and 1-333-333-3333 assigned, and 1-222-222-2222 sends a text to 1-999-999-9999 who opts out by responding with STOP, then both 1-222-222-2222 and 1-333-333-3333 (and any other number associated with Messaging Profile X) will not be able to text 1-999-999-9999 further. The number 1-444-444-4444 on Messaging Profile Y can still text 1-999-999-9999.

### Recognised Stop Words

Telnyx recognises the following English-language stop words:

- stop
- stopall
- stop all
- unsubscribe
- cancel
- end
- quit

Stop words are only recognised if they are the only words in the message. For example, "stop all" is recognised but "please stop all messages" would not be.

### Opt-In Keywords

To opt in again, the number that opted out must send any of the following opt-in keywords to the exact same number they opted out from:

- start
- unstop

When using the number pool feature, the end user must send opt-in keywords to the exact same number they opted out from. The opt-out SMS can be found in MDRs by filtering for the number that opted out to determine where the opt-in needs to be sent.

### Auto Responses

By default, Telnyx handles the auto response. When a user opts out via a stop word, Telnyx automatically sends a generic unsubscribed message from the number that received the opt-out message:

- "You have successfully been unsubscribed, you will not receive any more messages from this number. Reply START to re-subscribe."
- "You have successfully been re-subscribed to this number. Reply STOP to unsubscribe. Msg&Data Rates May Apply."

Custom block rules and auto responses can be configured on a per messaging profile basis — contact sales@telnyx.com to discuss.

### Keyword Management

Telnyx offers the ability to add custom keywords for opt-in/out and help messages along with specifying auto responses. This feature is accessible via the Keywords Management section of the portal. To set up custom keywords, select the desired messaging profile from the keywords management menu, then add keywords globally (Country: Global) or click "Add keywords in other languages based on country selected" to create a new rule set for a specified country. A maximum of 20 keywords can be added.

## Toll-Free Opt-Out Words

Telnyx handles opt-outs and opt-ins differently for toll-free numbers compared to 10-digit long code numbers. The only keyword recognised for opting out of communications with a Telnyx toll-free number is "stop". The only keywords recognised for opting in are "start" and "unstop".

When someone opts out of a Telnyx toll-free number, the following auto response is sent:

> "NETWORK MSG: You replied with the word \"stop\" which blocks all texts sent from this number. Text back \"unstop\" to receive messages again."

When someone opts in, the following auto response is sent:

> "NETWORK MSG: You have replied \"unstop\" and will begin receiving messages again from this number."

On opt-out, further communications from the toll-free number to the opted-out number are blocked; on opt-in, messaging is allowed again.

Because opt-out logic and auto responses for toll-free numbers are handled outside of Telnyx, it is not possible to change the opt-out or opt-in keywords or the content of the auto responses specifically for toll-free numbers. If custom block rules and auto responses have been set for a messaging profile, separate toll-free numbers from that profile to avoid unintended behaviour.

## WhatsApp 24-Hour Conversation Window

WhatsApp uses a 24-hour conversation window to control when businesses can send free-form messages. The window opens when a customer messages you and lasts for 24 hours from the customer's last message.

### What Opens the Window

- A customer sends you a message (text, image, button reply, etc.)
- A customer taps a call-to-action button in a previous message
- A customer replies to a template message

Each new message from the customer resets the 24-hour timer.

### During the Window (Open)

While the window is open, you can send:

- Free-form messages (text, media, location, contacts, interactive)
- Template messages (these still work within the window)

Free-form messages within the window create Service conversations, which are typically the lowest-cost conversation category.

### After the Window Closes (Expired)

Once 24 hours have passed since the customer's last message:

- Free-form messages will fail
- You must use an approved template message to re-initiate contact
- The template message opens a new conversation (billed at the template's category rate)

### Conversation Billing

Each conversation is billed once when it opens. The conversation type determines the rate:

- **Service** — Customer messages you, you reply with free-form. Duration: 24 hours from window open.
- **Marketing** — You send a Marketing template. Duration: 24 hours from template send.
- **Utility** — You send a Utility template. Duration: 24 hours from template send.
- **Authentication** — You send an Authentication template. Duration: 24 hours from template send.

### Tips

- Respond promptly — The 24-hour window starts from the customer's message, not your reply. Delays eat into your free-form messaging time.
- Use templates strategically — If you need to follow up after the window closes, have relevant templates pre-approved and ready.
- Monitor via webhooks — Use delivery status webhooks to track whether messages succeeded or failed due to window expiration.
