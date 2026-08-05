---
title: Telnyx Number Management and E911 Configuration
summary: This page consolidates Telnyx Mission Control guidance for managing phone
  numbers, configuring E911 emergency services, registering emergency addresses, testing
  emergency calling, and using bulk edit tools for voice, messaging, tags, and emergency
  settings.
sources:
- url: https://support.telnyx.com/en/articles/1130647-register-e911-addresses
- url: https://support.telnyx.com/en/articles/1130683-e911-setup-guide
- url: https://support.telnyx.com/en/articles/1130709-how-do-i-test-e911-service
- url: https://support.telnyx.com/en/articles/12580667-configure-repeat-call-guard-on-outbound-voice-profiles-beta
- url: https://support.telnyx.com/en/articles/2807846-bulk-edit-numbers-voice-settings
- url: https://support.telnyx.com/en/articles/2807910-bulk-edit-numbers-assigning-tags
- url: https://support.telnyx.com/en/articles/2819213-bulk-edit-numbers-emergency-services
- url: https://support.telnyx.com/en/articles/2819236-bulk-edit-numbers-delete-numbers
- url: https://support.telnyx.com/en/articles/2819238-bulk-edit-numbers-messaging-profile
- url: https://support.telnyx.com/en/articles/4294429-addresses-overview
- url: https://support.telnyx.com/en/articles/4349113-my-numbers-page
- url: https://support.telnyx.com/en/articles/4366901-your-number-lookup-guide
- url: https://support.telnyx.com/en/articles/4640720-what-is-an-exhausted-npa
updated_at: 2026-08-05T13:30:13Z
---

# Telnyx Number Management and E911 Configuration

*Part 3 of 4 — see also: [Part 1](telnyx-number-management-and-e911-configuration--part-1.md), [Part 2](telnyx-number-management-and-e911-configuration--part-2.md), [Part 4](telnyx-number-management-and-e911-configuration--part-4.md)*

This page consolidates Telnyx Mission Control guidance for managing phone numbers, configuring E911 emergency services, registering emergency addresses, testing emergency calling, and using bulk edit tools for voice, messaging, tags, and emergency settings.

## Bulk Editing Numbers

The [My Numbers Page](my-numbers-page.md) supports bulk actions on up to 100 numbers at a time. Select numbers using the checkboxes (or the top checkbox to select all on the page), expand the row count to 10–100 numbers, then open the **Bulk Actions** dropdown. Available bulk actions include voice settings, tags, emergency settings, messaging profile, and delete numbers.

### Bulk Edit Voice Settings

The [Bulk Edit Numbers - Voice Settings](bulk-edit-numbers-voice-settings.md) workflow opens a **Bulk Edit Voice Settings** window with tabs for **Routing/Billing**, **HD Voice Feature**, **CNAM**, **Forwarding**, **Recording**, **Voicemail**, and **Expert Config**.

- **SIP Connections / Applications:** Select a SIP Trunk Connection to apply to all selected numbers, or choose **No Connection** to bulk-remove a SIP connection.
- **Billing Group:** Associate or de-associate numbers with a billing profile.
- **Voice Billing Method:** Switch numbers between [Channel Billing](https://support.telnyx.com/en/articles/1130678-channel-billing-and-how-to-use-it) and [Pay-per-minute Billing](https://support.telnyx.com/en/articles/1130659-billing-increments).
- **CNAM Listing:** Enable or disable CNAM listing for the selected numbers.
- **CNAM Caller ID Lookup:** Enable or disable caller ID lookup for inbound calls on the selected numbers.
- **Forwarding:** Set call forwarding (Always or On-Failure) for the selected numbers.
- **Recording:** Configure call recording for the selected numbers.
- **Voice Mail:** Toggle voicemail and set a PIN for the selected numbers.
- **Expert Config:** Enable Translated Number, Tech Prefix, T.38 FAX gateway, Accept any RTP Packets, and RTP Auto Adjust settings.

### Bulk Edit Tags

The [Bulk Edit Numbers - Assigning tags](bulk-edit-numbers-assigning-tags.md) workflow lets you apply or remove tags across many numbers. After selecting numbers and choosing **Edit Tags** from the Bulk Actions dropdown, you can select an existing tag or create a new one (for example, `test-tag`) and save. To remove tags in bulk, follow the same path and enter the tag name to remove.

### Bulk Edit Emergency Services

The [Bulk Edit Numbers - Emergency Services](bulk-edit-numbers-emergency-services.md) workflow lets you assign an emergency address to many numbers at once. After selecting numbers and choosing **Edit Emergency Settings**, you can **Enable All**, **Disable All**, or leave settings **Unchanged**. With **Enable All**, you can pick an existing saved address or click **New Address** to add one. Saving applies the address and enables emergency service for all selected numbers.

> **NOTE:** Failure to register an address and enable emergency services on numbers that make emergency calls is considered unregistered and incurs a $100 penalty.

### Bulk Edit Messaging Profile

The [Bulk Edit Numbers - Messaging Profile](bulk-edit-numbers-messaging-profile.md) workflow assigns a messaging profile to many numbers. After selecting numbers and choosing **Edit Messaging Profile**, pick a profile from the dropdown, accept the MRC charge prompt, and save. The chosen messaging profile is then applied to all selected numbers.

### Bulk Delete Numbers

The [Bulk Edit Numbers - Delete Numbers](bulk-edit-numbers-delete-numbers.md) workflow permanently deletes selected numbers. After selecting numbers and choosing **Delete Numbers**, confirm the list and click the red **Delete Numbers** button. This action is irreversible; deleted numbers can be repurchased within 15 days from the deletion date. After 15 days, the numbers enter an ageing state and are eventually released back to the number pool.

## Repeat Call Guard on Outbound Voice Profiles

The [Configure Repeat Call Guard on Outbound Voice Profiles (BETA)](configure-repeat-call-guard-on-outbound-voice-profiles-beta.md) feature controls how many times a destination number can be called within a specific time window, protecting against over-dialing and supporting compliance with customer contact policies. It applies only to calls made through SIP connections and is configured per Outbound Voice Profile.

### Standard behavior

Outbound calls can be made to the same destination number without restriction, and call frequency limits depend only on the user's dialing logic.

### New behavior with Repeat Call Guard enabled

1. Users define active calling hours (start and end times).
2. Users set a maximum number of allowed call attempts per destination number (CLD).
3. Once the limit is reached, additional calls to that number are automatically blocked until the next day.
4. Counters reset daily based on the configured time window.

### Pre-requisites

- Access to the Telnyx Customer Portal.
- An existing Outbound Voice Profile.
- A valid Telnyx API key.

### Configure Repeat Call Guard

1. Log in to the Telnyx Customer Portal.
2. Go to **Voice → Outbound Voice Profiles**.
3. Select an existing profile or create a new one.
4. Locate the **Repeat Call Guard** section below the Audio File Channel Type field.
5. Enable the toggle and configure:
   - **Start Time:** When call restrictions start in UTC (for example, `08:00`).
   - **End Time:** When the restriction window ends in UTC (for example, `18:00`).
   - **Calls per CLD:** How many times a single destination number can be called on a 24-hour rolling basis within the window.
6. Click **Save** to apply the configuration.

Repeat Call Guard uses a rolling reset for the call counter within daily active window hours. After hitting the maximum limit, the counter resets the next rolling 24 hours just after the time of the previous day's first allowed call, allowing a fresh slot from that point onward within the window.

**Example:** On Day 1, you make 3 calls starting at 14:00 (first at 14:00, then 14:30 and 15:10) — limit hit, blocking further calls in that window. On Day 2, the counter resets at 14:01, so you can make up to 3 new calls starting from 14:01 within the window (for example, at 14:01, 14:40, 16:00). Calls before 14:01 on Day 2 are still blocked.

### Configure via API

You can configure Repeat Call Guard directly through the Telnyx API:

```
curl -L -X PATCH 'https://api.telnyx.com/v2/outbound_voice_profiles/{profileID}' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer KEYxxxxxxxxxxxxxxxxxxxxxxx' \
  -d '{
    "name": "time",
    "calling_window": {
      "start_time": "02:01",
      "end_time": "22:01",
      "calls_per_cld": 4
    }
  }'
```

Replace `{profileID}` and the `Authorization` key with your actual values.

### Verify the configuration

Once saved, verify that:

- The toggle shows **Enabled**.
- The correct **Start Time**, **End Time**, and **Calls per CLD** values appear.
- Calls exceeding the defined limit during the window are automatically blocked. A message `Daily calling restriction to Destination Number +11234567890 exceeded D66 (code 403)` will be sent by Telnyx.

### Tips for success

- Configure the timezone correctly. Times are saved in UTC, so convert from the target location's local time to UTC.
- Remember that the call limit resets daily at midnight.
- Disable the feature temporarily if you need unrestricted outbound dialing.
