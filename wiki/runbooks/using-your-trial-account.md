---
title: Using Your Trial Account
summary: Recommended process to get the most value from Telnyx trial credits.
sources:
  - url: https://developers.telnyx.com/docs/account-setup/using-trial-account
    content_hash: 9164b1d2b92322fb830ce5838ee6f4ee2ddd45aaeb1bdcabcb3e2747c9d36f8a
updated_at: 2026-04-10T00:00:00Z
---

# Using Your Trial Account

Recommended process to get the most value from Telnyx trial credits.

Follow this process to make the most of your trial credit and stay within trial limitations.

1. **Verify a phone number**

    A [verified number](https://portal.telnyx.com/#/numbers/verified-numbers) is essential to test Voice and Messaging. Use a mobile phone number that you control.

    Keep in mind that trial accounts have limits on delivery attempts and the number of changes allowed. Once the allowance is depleted, [upgrade your account](account-upgrade.md).

2. **Search for and purchase a phone number**

    Search results show only local (to the signup origin) numbers in full +E164; other results appear partially redacted.

    A successful purchase depends on inventory availability, sufficient account balance, and local jurisdiction [documentation rules](https://portal.telnyx.com/#/numbers/requirements). Only **one** phone number order is allowed during the trial, regardless of the outcome.

3. **Test calling workflows**

    Use one of the following tutorials to place calls:

    * [SIP Trunking](https://developers.telnyx.com/docs/voice/sip-trunking/get-started)
    * [Programmable Voice](https://developers.telnyx.com/docs/voice/programmable-voice/get-started)
    * [TeXML](https://developers.telnyx.com/docs/voice/programmable-voice/texml-setup)

    Regardless of how the call is created, the destination is limited to the verified phone number from Step 1, and inbound calls must also originate from that number. Check [trial voice limits](trial-account-privileges-limitations.md).

4. **Test messaging workflows**

    Use the [Send Message](https://developers.telnyx.com/docs/messaging/messages/send-message) tutorial to send SMS.

    Outbound messages must target the verified phone number you configured, and inbound messages must also originate from that number. Check [trial messaging limits](trial-account-privileges-limitations.md).


## Related Pages

- [Create Your Telnyx Account](../runbooks/create-your-telnyx-account.md)
