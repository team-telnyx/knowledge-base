---
title: Toll-Free Verification and Messaging
summary: Toll-Free numbers on Telnyx require verification before sending outbound
  messages. This page covers the full verification process, form requirements, use
  case selection, opt-in workflows, prohibited content, carrier rejections, and related
  topics such as opt-out handling, webhook notifications, and number porting.
sources:
- url: https://support.telnyx.com/en/articles/10729979-toll-free-verification-request-guide
- url: https://support.telnyx.com/en/articles/11898569-toll-free-opt-in-workflow-description
- url: https://support.telnyx.com/en/articles/12650709-how-to-pick-a-toll-free-use-case
- url: https://support.telnyx.com/en/articles/13765655-compliance-catch-up-why-toll-free-verification-now-mirrors-10dlc
- url: https://support.telnyx.com/en/articles/14286763-forbidden-messaging-use-cases-in-the-us-and-canada-10dlc-toll-free-and-short-code
- url: https://support.telnyx.com/en/articles/15138019-toll-free-carrier-rejections
- url: https://support.telnyx.com/en/articles/5353868-toll-free-messaging
- url: https://support.telnyx.com/en/articles/6989758-toll-free-opt-out-words
- url: https://support.telnyx.com/en/articles/8269305-appeal-level-2-verification-status
- url: https://support.telnyx.com/en/articles/8673249-us-ca-toll-free-number-porting
updated_at: 2026-06-11T11:12:33Z
---

# Toll-Free Verification and Messaging

*Part 4 of 4 — see also: [Part 1](toll-free-verification-and-messaging--part-1.md), [Part 2](toll-free-verification-and-messaging--part-2.md), [Part 3](toll-free-verification-and-messaging--part-3.md)*

Toll-Free numbers on Telnyx require verification before sending outbound messages. This page covers the full verification process, form requirements, use case selection, opt-in workflows, prohibited content, carrier rejections, and related topics such as opt-out handling, webhook notifications, and number porting.

## Webhook Notifications

Telnyx provides real-time status updates via webhooks when a verification request status changes. The `verification_status` field in the payload reflects one of: `Rejected`, `Waiting For Vendor`, `Waiting For Customer`, or `Verified`. Each event includes context such as the affected phone number(s), business name, and reason for the current status.

To receive notifications, provide a webhook URL during submission. In the Telnyx Portal, you can also input a webhook URL on the Toll-Free Verification page to receive updates.

## Toll-Free Number Porting

Toll-free (8YY) number porting — covering 800, 844, 855, 866, 877, and 888 exchanges — uses a centralized portal and typically completes faster than standard local number porting. The process takes approximately 2 business days, though it can range from 1 to 7 business days.

**Required documentation:**
1. Letter of Authorization (LOA) — [download the template](https://portal.telnyx.com/downloads/other/Telnyx-LOA.pdf)
2. Latest invoice

Submit port requests at least two weeks before the desired activation date. Toll-free numbers risk disconnection if not activated within 1–2 weeks after release by the RespOrg.

**SMS porting best practice:** Telnyx cannot guarantee SMS will migrate at the same time as voice. To minimize downtime:
1. Create a hosted SMS request for the numbers at least 5 business days before the desired FOC date.
2. Create a porting order for the same numbers with an FOC date at least 5 business days out.
3. After 3–4 business days, the hosted SMS request should complete — SMS migrates to Telnyx while voice still routes through the losing carrier.
4. When the FOC date arrives, voice ports in and both voice and SMS route through Telnyx with no downtime.

For more details, see the [LOA & Documentation Policy](https://support.telnyx.com/en/articles/2034326-how-to-fill-out-an-loa) and [Hosted SMS Messaging Process](https://support.telnyx.com/en/articles/5336668-hosted-sms-messaging-process).

## Best Practices

- **Obtain clear consent:** Have a clear call-to-action that informs recipients of the program description, originating number, sender identity, opt-in language, associated fees, and how to opt out.
- **Use compliant language:** Avoid misleading claims and include required disclaimers.
- **Brand your messages:** Clearly identify your business in each message.
- **Provide transparent opt-out mechanisms:** Include "Reply STOP to opt out" in messages and honor opt-outs within 24 hours.
- **Use branded domains:** Avoid public URL shorteners; use HTTPS and recognizable domains.
- **Register campaigns where required:** Ensure all messaging aligns with registered use cases.
- **Avoid high-frequency messaging:** Do not exceed 10 messages to a recipient in 24 hours unless the recipient has engaged in two-way communication or explicitly opted in.
- **Do not spoof:** Never represent yourself as another individual or business.
- **Separate toll-free numbers from custom messaging profiles:** If you have custom block rules or auto-responses configured, keep toll-free numbers on a separate messaging profile to avoid unintended behavior.
