---
title: Telnyx Messaging
summary: A consolidated reference for Telnyx programmable messaging covering messaging
  profiles, opt-in/opt-out keywords and auto responses, 10DLC and toll-free verification,
  hosted SMS, SMPP setup, and third-party integrations.
sources:
- url: https://support.telnyx.com/en/articles/10645338-10dlc-keywords-and-confirmation-messages
- url: https://support.telnyx.com/en/articles/12650709-how-to-pick-a-toll-free-use-case
- url: https://support.telnyx.com/en/articles/1270091-sms-opt-out-keywords-and-stop-words
- url: https://support.telnyx.com/en/articles/15138019-toll-free-carrier-rejections
- url: https://support.telnyx.com/en/articles/1667062-short-message-peer-to-peer-set-up-guide
- url: https://support.telnyx.com/en/articles/3562059-setting-up-a-messaging-profile
- url: https://support.telnyx.com/en/articles/4348981-receiving-sms-on-your-telnyx-number
- url: https://support.telnyx.com/en/articles/5336668-hosted-sms-messaging-process
- url: https://support.telnyx.com/en/articles/5353868-toll-free-messaging
- url: https://support.telnyx.com/en/articles/6986625-easy-text-marketing-and-telnyx-integration
- url: https://support.telnyx.com/en/articles/6989758-toll-free-opt-out-words
updated_at: 2026-07-17T09:00:31Z
---

# Telnyx Messaging

*Part 4 of 4 — see also: [Part 1](telnyx-messaging--part-1.md), [Part 2](telnyx-messaging--part-2.md), [Part 3](telnyx-messaging--part-3.md)*

A consolidated reference for Telnyx programmable messaging covering messaging profiles, opt-in/opt-out keywords and auto responses, 10DLC and toll-free verification, hosted SMS, SMPP setup, and third-party integrations.

## Easy Text Marketing Integration

Easy Text Marketing (formerly Rockstar SMS) integrates with Telnyx as a BYOC carrier. The setup process:

1. Create a Telnyx account at [telnyx.com/sign-up](https://telnyx.com/sign-up).
2. Add funds via the [billing portal](https://portal.telnyx.com/#/billing/payment); $25 is typically sufficient to start. Standard phone number cost is $1 activation and $1/month.
3. Configure auto-recharge settings after the first payment.
4. Copy the API Key (not the public key) from the [Mission Control home](https://portal.telnyx.com/#/home).
5. Sign in or create an account at [rockstarsms.app](http://rockstarsms.app).
6. In the Easy Text Marketing profile, select Telnyx as the SMS Gateway and paste the API Key at [rockstarsms.app/users/edit](https://rockstarsms.app/users/edit).
7. In the Easy Text Marketing dashboard, click **Get a Number** at [rockstarsms.app/users/profile](https://rockstarsms.app/users/profile), which automatically creates a Telnyx messaging profile.
8. Back in Telnyx, assign the Easy Text Marketing messaging profile (likely listed as "Text Marketing Made Easy") to the new number at [My Numbers](https://portal.telnyx.com/#/voice/my-numbers).

For Telnyx support, contact [klane@telnyx.com](mailto:klane@telnyx.com). For sub-accounts (Managed Accounts), also contact [klane@telnyx.com](mailto:klane@telnyx.com). For Easy Text Marketing support, visit [rockstarsms.app/helpdesk/](https://rockstarsms.app/helpdesk/).
