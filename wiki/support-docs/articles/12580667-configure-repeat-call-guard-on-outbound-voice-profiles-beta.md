---
title: "Configure Repeat Call Guard on Outbound Voice Profiles (BETA)"
summary: "Control how many times a destination number can be called within a specific time window. See Telnyx guidance and requirements."
sources:
- url: "https://support.telnyx.com/en/articles/12580667-configure-repeat-call-guard-on-outbound-voice-profiles-beta"
updated_at: 2026-09-25T00:00:00Z
tags: [support-docs]
source_path: "support-docs/en--articles--12580667-configure-repeat-call-guard-on-outbound-voice-profiles-beta.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/en--articles--12580667-configure-repeat-call-guard-on-outbound-voice-profiles-beta.md -->

# Configure Repeat Call Guard on Outbound Voice Profiles (BETA)

Control how many times a destination number can be called within a specific time window. See Telnyx guidance and requirements.

## Background

The **Repeat Call Guard** feature lets users manage call frequency to prevent repeated outbound calls to the same number within a configured calling window. This protects against over-dialing and ensures compliance with customer contact policies.

## Standard Behavior

1. Outbound calls can be made to the same destination number without restriction.
2. Call frequency limits depend only on the user's dialing logic.

## Behavior with Repeat Call Guard Enabled

1. Users define active calling hours (start and end times in UTC).
2. Users set a maximum number of allowed call attempts per destination number (CLD).
3. Once the limit is reached, additional calls to that number are automatically blocked until the counter resets at the start of the next calling window.
4. The counter resets at the configured **start time** each day, not on a rolling 24-hour basis. A midnight UTC reset applies only when the configured start time is midnight.

**Note:** This feature only applies to **calls made through SIP connections** and is **configured per Outbound Voice Profile**, meaning limits are tracked independently for each profile.

---

## How the Calling Window Works

Repeat Call Guard counts calls within **fixed daily UTC windows**. The counter starts fresh at the configured start time each day.

- If the **end time is later than the start time** (e.g., `08:00`–`18:00`), the window runs within a single UTC day.
- If the **end time is earlier than the start time** (e.g., `14:00`–`02:00`), the window **crosses midnight UTC** and continues into the following UTC day. Calls on both sides of UTC midnight belong to the same counter window.

Repeat Call Guard is **not a rolling 24-hour counter**. It does not reopen individual call slots 24 hours after each call. The entire counter resets at the next configured start time.

### Example: Window crossing midnight UTC

A customer in Nicaragua (UTC−6) wants to cover business hours 08:00–20:00 local time:

- **Start time:** `14:00` UTC (08:00 Nicaragua)
- **End time:** `02:00` UTC (20:00 Nicaragua)
- **Calls per CLD:** 3

Because the end time (`02:00`) is earlier than the start time (`14:00`), the system treats this as one overnight window:

- **Thursday 14:00 UTC** through **Friday 02:00 UTC** = one window
- **Friday 14:00 UTC** through **Saturday 02:00 UTC** = next window

The counter resets at 14:00 UTC each day (08:00 Nicaragua local time), not at 00:00 UTC.

---

## Pre-requisites

Before you begin, make sure you have:

- Access to the **Telnyx Customer Portal**
- An existing **Outbound Voice Profile**
- A valid **Telnyx API key**

---

## Step 1: Navigate to Outbound Voice Profiles

1. Log in to the **Telnyx Customer Portal**.
2. Go to **Voice → Outbound Voice Profiles**.
3. Select an existing profile or create a new one.

---

## Step 2: Locate the Repeat Call Guard Section

You'll find the **Repeat Call Guard** section **below the Audio File Channel Type field** on the profile configuration page at the bottom.

---

## Step 3: Configure Repeat Call Guard

Enable the toggle to activate **Repeat Call Guard**.

- **Start Time:** Define when the calling window starts in UTC.
  Example: `08:00`
- **End Time:** Define when the calling window ends in UTC.
  Example: `18:00`
- **Calls per CLD:** Set the maximum number of call attempts allowed to a single destination number within each daily calling window.

The counter resets at the configured **start time** each day. If the end time is earlier than the start time, the window crosses midnight UTC as described above.

---

## Step 4: Save Your Settings

Click **Save** to apply the configuration.
Your outbound profile will now enforce the set call limits within the defined time window.

---

## Configure via API (Optional)

You can configure Repeat Call Guard directly through the Telnyx API.

**Curl example:**

```
curl -L -X PATCH 'https://api.telnyx.com/v2/outbound_voice_profiles/{profileID}' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer KEYxxxxxxxxxxxxxxxxxxxxxxx' \
  -d '{
    "name": "time",
    "calling_window": {
      "start_time": "14:00",
      "end_time": "02:00",
      "calls_per_cld": 3
    }
  }'
```

Replace `{profileID}` and the `Authorization` key with your actual values.

The example above configures an overnight window from 14:00 UTC to 02:00 UTC with a limit of 3 calls per destination number per window.

---

## Step 5: Verify the Configuration

Once saved, verify that:

- The toggle shows **Enabled**.
- The correct **Start Time**, **End Time**, and **Calls per CLD** values appear.
- Calls exceeding the defined limit during the window are automatically blocked. A message "`Daily calling restriction to Destination Number +11234567890 exceeded D66 (code 403)`" will be sent by Telnyx.

---

## Tips for Success

- **Convert local time to UTC.** Times are saved in UTC. Ensure you convert from the target location's local time to the UTC equivalent. For example, 08:00 Nicaragua (UTC−6) = 14:00 UTC.
- **Counter resets at the configured start time.** The call limit resets at the start of each daily calling window and not 24 hours after the first call. It resets at midnight UTC only if that is the configured start time.
- **Windows can cross midnight UTC.** If your configured end time is earlier than the start time, the window spans into the following UTC day. This is expected behavior.
- **Enforce business hours separately.** To prevent calls outside your business hours, also configure operating hours in your dialing application.
- **Disable temporarily if needed.** Toggle the feature off if you need unrestricted outbound dialing.

---

## References

- [Telnyx Portal - Outbound Voice Profiles](https://portal.telnyx.com/#/outbound-profiles)
- [Telnyx API Reference – Outbound Voice Profiles](https://developers.telnyx.com/)
