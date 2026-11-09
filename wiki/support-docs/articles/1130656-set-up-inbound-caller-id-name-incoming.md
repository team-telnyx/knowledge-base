---
title: "Set up Inbound Caller ID Name (incoming)"
summary: "Inbound caller name lookup uses the caller’s number to look up their name on incoming calls anchored in the US or Canada. When Telnyx finds a name, it includes it in the SIP INVITE to your connection."
sources:
- url: "https://support.telnyx.com/en/articles/1130656-set-up-inbound-caller-id-name-incoming"
updated_at: 2026-07-08T00:00:00Z
tags: [support-docs]
source_path: "support-docs/en--articles--1130656-set-up-inbound-caller-id-name-incoming.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/en--articles--1130656-set-up-inbound-caller-id-name-incoming.md -->

# Set up Inbound Caller ID Name (incoming)

Inbound caller name lookup uses the caller’s number to look up their name on incoming calls anchored in the US or Canada. When Telnyx finds a name, it includes it in the SIP INVITE to your connection. Outbound CNAM Listing is a separate setting for the name associated with your own number.

## Guide to Configuring Inbound Caller ID Name

1. Open [My Numbers](https://portal.telnyx.com/#/numbers/my-numbers) in Mission Control and edit the number you want to configure.
2. Open the **Voice** tab and find **Inbound caller name lookup** under **Services**.
3. Choose a lookup option.

   ![Inbound caller name lookup menu showing Off, Standard, and Enhanced at $1.50 per month.](_images/1130656-inbound-cnam-options.png)

   | Option | Lookup and monthly charge |
   | --- | --- |
   | **Off** | Disables lookup. No inbound CNAM monthly charge. |
   | **Standard** | Uses standard caller name lookup at your existing rate. |
   | **Enhanced** | Uses enhanced caller name lookup for $1.50 per month per enabled number. This replaces the Standard monthly charge. |

4. Select **Save Changes**. To switch tiers or turn lookup off later, return to the same setting, select the option you want, and save.

   ![Inbound caller name lookup with Enhanced selected and the monthly price displayed.](_images/1130656-inbound-cnam-enhanced.png)

If your account still shows **Enable CNAM Caller ID lookup**, use that checkbox to turn Standard lookup on or off.

For API configuration, see [Update a phone number with voice settings](https://developers.telnyx.com/api-reference/phone-number-configurations/update-a-phone-number-with-voice-settings).
