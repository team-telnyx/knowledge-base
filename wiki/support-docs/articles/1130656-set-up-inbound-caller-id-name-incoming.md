---
title: "Set up Inbound Caller ID Name (incoming)"
summary: "Inbound caller name lookup can add a caller’s name to calls you receive on a Telnyx number. The setting applies to eligible calls anchored in the US or Canada. Use Outbound CNAM Listing to manage the name associated with your own number on outgoing calls."
sources:
- url: "https://support.telnyx.com/en/articles/1130656-set-up-inbound-caller-id-name-incoming"
updated_at: 2026-07-08T00:00:00Z
tags: [support-docs]
source_path: "support-docs/en--articles--1130656-set-up-inbound-caller-id-name-incoming.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/en--articles--1130656-set-up-inbound-caller-id-name-incoming.md -->

# Set up Inbound Caller ID Name (incoming)

Inbound caller name lookup can add a caller’s name to calls you receive on a Telnyx number. The setting applies to eligible calls anchored in the US or Canada. Use **Outbound CNAM Listing** to manage the name associated with your own number on outgoing calls.

## Standard vs. Enhanced

| Option | What you get | Monthly charge |
| --- | --- | --- |
| **Off** | Telnyx skips the caller name lookup for this number. | No inbound CNAM charge. |
| **Standard** | Telnyx uses traditional CNAM databases to look up the name listed for the caller’s number. | Your existing rate. |
| **Enhanced** | Telnyx uses a separate data source that can return a person or business name for more US caller numbers. Names can use mixed case and exceed the traditional 15-character limit. | $1.50 per enabled number. This replaces the Standard charge. |

## How Telnyx handles incoming calls

1. If the call already has a caller name that Telnyx can use, Telnyx uses that name first.
2. When lookup is enabled and a name is needed, Telnyx looks up the **calling number** using the tier configured on the **Telnyx number that received the call**.
3. If the lookup returns a name, Telnyx includes it as the caller’s display name in the SIP INVITE to your connection. If the lookup finds no name or is unavailable, the call continues with the usual caller ID information. For an Enhanced lookup, only the Enhanced data source is queried.

## Guide to Configuring Inbound Caller ID Name

1. Open [My Numbers](https://portal.telnyx.com/#/numbers/my-numbers) in Mission Control and edit the number you want to configure.
2. Open the **Voice** tab and find **Inbound caller name lookup** under **Services**.
3. Choose a lookup option.

   ![Inbound caller name lookup menu showing Off, Standard, and Enhanced at $1.50 per month.](_images/1130656-inbound-cnam-options.png)

4. Select **Save Changes**. To switch tiers or turn lookup off later, return to the same setting, select the option you want, and save.

   ![Inbound caller name lookup with Enhanced selected and the monthly price displayed.](_images/1130656-inbound-cnam-enhanced.png)

If your account still shows **Enable CNAM Caller ID lookup**, use that checkbox to turn Standard lookup on or off.

For API configuration, see [Update a phone number with voice settings](https://developers.telnyx.com/api-reference/phone-number-configurations/update-a-phone-number-with-voice-settings).
