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

*Part 2 of 8 — see also: [Part 1](10dlc-campaign-use-cases-and-event-notifications--part-1.md), [Part 3](10dlc-campaign-use-cases-and-event-notifications--part-3.md), [Part 4](10dlc-campaign-use-cases-and-event-notifications--part-4.md), [Part 5](10dlc-campaign-use-cases-and-event-notifications--part-5.md), [Part 6](10dlc-campaign-use-cases-and-event-notifications--part-6.md), [Part 7](10dlc-campaign-use-cases-and-event-notifications--part-7.md), [Part 8](10dlc-campaign-use-cases-and-event-notifications--part-8.md)*

Comprehensive guide to Telnyx 10DLC campaign use cases, sample messages, opt-in/opt-out requirements, and webhook event notifications for brands, campaigns, and phone numbers. Includes SDK examples, retry policies, and campaign appeal mechanisms.

## Standard Use Cases

### 2FA / Two-Factor Authentication

The simplest use case — short, transactional, no marketing content.

**Sample messages (3 required):**

```
Your Acme verification code is 847291. This code expires in 10 minutes. If you didn't request this, ignore this message.
```

```
Your login code for Acme is 523016. Don't share this code with anyone. Reply STOP to opt out.
```

```
Acme security code: 194738. Enter this code to complete your password reset. This code expires in 5 minutes.
```

**Opt-in language:**

```
By entering your phone number, you agree to receive one-time verification
codes from [Brand] via SMS. Message frequency varies. Message and data rates
may apply. Reply STOP to opt out.
```

**Tips for approval:**

- Keep messages under 160 characters
- Include the code prominently
- Add an expiry time
- Don't include marketing content or links
- Brand name should appear in the message

### Customer Care

Support conversations, ticket updates, and service messages.

**Sample messages (3 required):**

```
Hi [Name], your support ticket #4521 has been updated. Our team has responded — view details at support.acme.com/tickets/4521. Reply STOP to opt out.
```

```
Acme Support: Your return request for order #8834 has been approved. A prepaid label has been sent to your email. Questions? Reply HELP.
```

```
Your appointment with Acme Support is confirmed for March 15 at 2:00 PM EST. Reply YES to confirm or RESCHEDULE to change. Reply STOP to unsubscribe.
```

**Opt-in language:**

```
By providing your phone number, you consent to receive customer service
messages from [Brand] via SMS, including support ticket updates, appointment
reminders, and service notifications. Message frequency varies. Msg & data
rates may apply. Reply HELP for help, STOP to cancel.
```

**Tips for approval:**

- Messages should be reactive (responding to customer actions)
- Include ticket/order numbers for context
- Don't mix in promotional content
- Keep a helpful, service-oriented tone
- Include brand name in every message

### Delivery Notifications

Order confirmations, shipping updates, and delivery status.

**Sample messages (3 required):**

```
Acme: Your order #99281 has shipped! Tracking: 1Z999AA10123456784. Estimated delivery: March 18. Track at acme.com/track. Reply STOP to opt out.
```

```
Your Acme delivery is out for delivery and will arrive today between 2-6 PM. A photo confirmation will be sent upon delivery. Reply STOP to unsubscribe.
```

```
Acme: Your package was delivered at 3:42 PM and left at front door. View delivery photo at acme.com/orders/99281. Reply STOP to opt out.
```

**Opt-in language:**

```
By placing an order, you agree to receive shipping and delivery updates from
[Brand] via SMS. Message frequency varies based on order activity. Msg & data
rates may apply. Reply STOP to cancel, HELP for help.
```

**Tips for approval:**

- Include order/tracking numbers
- Messages should follow the order lifecycle
- Include delivery estimates when available
- Don't add promotional upsells in delivery messages

### Account Notifications

Password changes, billing alerts, account activity.

**Sample messages (3 required):**

```
Acme: Your password was successfully changed on March 4, 2026. If you didn't make this change, contact support immediately at 1-800-555-0199. Reply STOP to opt out.
```

```
Acme billing alert: Your payment of $49.99 was processed successfully. Your next billing date is April 4, 2026. View invoice at acme.com/billing. Reply STOP to unsubscribe.
```

```
Acme: Your subscription plan was upgraded to Pro. Your new monthly rate is $79.99, effective immediately. Questions? Reply HELP. Reply STOP to opt out.
```

**Opt-in language:**

```
By creating an account, you consent to receive account-related notifications
from [Brand] via SMS, including billing alerts, password changes, and account
updates. Msg frequency varies. Msg & data rates apply. Reply STOP to cancel.
```

**Tips for approval:**

- Focus on account changes the user initiated
- Include specific details (amounts, dates)
- Provide a way to verify or dispute changes
- Never include marketing in account notifications

### Marketing

Promotions, sales, product announcements, and brand content. Marketing campaigns receive the most scrutiny. Opt-in must be explicit and separate from terms of service.

**Sample messages (3 required):**

```
Acme Summer Sale! 🎉 Get 30% off all items this weekend only. Use code SUMMER30 at checkout. Shop now: acme.com/sale. Reply STOP to opt out.
```

```
New at Acme: Our spring collection just dropped! Be the first to shop 50+ new styles starting at $19.99. Browse: acme.com/new. Txt STOP to unsubscribe.
```

```
Acme: Thanks for being a loyal customer! Here's an exclusive 20% off coupon just for you. Use code VIP20 by March 31. Shop: acme.com. Reply STOP to cancel.
```

**Opt-in language:**

```
By checking this box, you agree to receive recurring marketing messages from
[Brand] via SMS, including promotions, sales, and product updates. Consent is
not a condition of purchase. Message frequency varies (up to 8 msgs/month).
Msg & data rates may apply. Reply HELP for help, STOP to unsubscribe.
View our Privacy Policy at [link] and Terms at [link].
```

**Tips for approval:**

- Opt-in MUST be separate from ToS (not buried in fine print)
- Include message frequency estimate
- State "consent is not a condition of purchase"
- Link to privacy policy and terms
- Every message must include opt-out language
- Don't use ALL CAPS excessively
- Include brand name in every message

### Security Alerts

Login alerts, fraud detection, and security notifications.

**Sample messages (3 required):**

```
Acme security alert: New login detected from Chrome on Windows in New York, NY at 3:42 PM EST. If this wasn't you, secure your account: acme.com/security. Reply STOP to opt out.
```

```
Acme: Unusual activity detected on your account. A purchase of $299.99 was attempted. If this wasn't you, reply BLOCK or call 1-800-555-0199. Reply STOP to unsubscribe.
```

```
Acme: Your account recovery email was changed. If you made this change, no action needed. If not, contact security immediately at 1-800-555-0199. Reply STOP to opt out.
```

**Opt-in language:**

```
By enabling security alerts, you agree to receive security notifications from
[Brand] via SMS, including login alerts, fraud detection, and account security
updates. Message frequency varies based on account activity. Msg & data rates
may apply. Reply STOP to cancel.
```

**Tips for approval:**

- Include specific details (device, location, time)
- Always provide a way to take action
- Keep urgency appropriate — don't create false panic
- These are high-priority; carriers are lenient but still review

### Polling & Voting

Surveys, feedback requests, and interactive polls.

**Sample messages (3 required):**

```
Acme: How was your recent purchase? Rate your experience 1-5 (1=poor, 5=excellent). Your feedback helps us improve! Reply STOP to opt out.
```

```
Acme customer survey: Would you recommend us to a friend? Reply YES or NO. As a thank you, get 10% off your next order. Reply STOP to unsubscribe.
```

```
Acme: Quick poll — which new feature matters most to you? Reply A) Faster shipping B) More colors C) Lower prices. Reply STOP to opt out.
```

**Opt-in language:**

```
By opting in, you agree to receive occasional survey and feedback requests
from [Brand] via SMS. Message frequency: up to 2 msgs/month. Msg & data
rates may apply. Reply STOP to opt out, HELP for help.
```

**Tips for approval:**

- Keep surveys short (1-2 questions per message)
- Make responses simple (numbers, YES/NO, letters)
- Don't disguise marketing as surveys
- Include clear opt-out in every message

### Charity / Nonprofit

Fundraising, awareness campaigns, and donation acknowledgments.

**Sample messages (3 required):**

```
Habitat for Hope: Thanks to donors like you, we built 12 homes this month! See the impact at habitatforhope.org/impact. Reply STOP to opt out.
```

```
Habitat for Hope: Our spring fundraiser starts March 15! Your $25 donation provides building materials for a family in need. Donate: habitatforhope.org/give. Reply STOP to unsubscribe.
```

```
Thank you for your $50 donation to Habitat for Hope! Your tax receipt has been emailed. Together we're building stronger communities. Reply STOP to opt out.
```

**Opt-in language:**

```
By texting JOIN to [number], you agree to receive updates from [Nonprofit]
via SMS, including impact updates, fundraising campaigns, and donation
receipts. Msg frequency varies (up to 4 msgs/month). Msg & data rates apply.
Reply STOP to cancel, HELP for help.
```

**Tips for approval:**

- Clearly identify your nonprofit in every message
- Show impact, not just ask for money
- Include donation receipts/acknowledgments
- Link to your organization's website

### Mixed (Most Common)

Multiple message types from a single campaign. This is the most frequently used use case.

**Sample messages (3 required — show variety):**

```
Acme: Your order #77412 has shipped and will arrive by March 18. Track at acme.com/track. Reply STOP to opt out.
```

```
Acme Support: Your ticket #2291 has been resolved. If you need further help, reply to this message or visit support.acme.com. Reply STOP to unsubscribe.
```

```
Acme: Spring sale starts tomorrow! Get early access with code SPRING25 for 25% off. Shop: acme.com/sale. Reply STOP to opt out.
```

**Opt-in language:**

```
By providing your phone number, you consent to receive messages from [Brand]
via SMS, including order updates, customer support notifications, and
promotional offers. Message frequency varies. Msg & data rates may apply.
Consent is not required for purchase. Reply HELP for help, STOP to cancel.
View our Privacy Policy at [link].
```

**Tips for approval:**

- Each sample should demonstrate a DIFFERENT message type
- Opt-in must mention ALL types of messages (transactional + marketing)
- If you include marketing, follow marketing opt-in rules
- Description should list all message categories
- This is the safest choice if you're unsure which use case to pick
