---
title: Porting Numbers to Telnyx
summary: A consolidated reference for porting numbers to Telnyx from Skype, Twilio,
  Microsoft Teams, and VoIP resellers (Aircall, Intercom, RingCentral, Vonage, Grasshopper),
  including carrier-specific credentials, common porting errors (TN Not Portable,
  Invalid Reseller, Authorized Name Mismatch), and related voice features such as
  Repeat Call Guard, Branded Calling, and Inbound Call Screening.
sources:
- url: https://support.telnyx.com/en/articles/10715399-porting-away-from-skype
- url: https://support.telnyx.com/en/articles/1130616-number-not-portable-tn-not-portable-error
- url: https://support.telnyx.com/en/articles/1130619-invalid-reseller-error
- url: https://support.telnyx.com/en/articles/1130623-authorized-name-mismatch-error
- url: https://support.telnyx.com/en/articles/12580667-configure-repeat-call-guard-on-outbound-voice-profiles-beta
- url: https://support.telnyx.com/en/articles/14708128-porting-numbers-away-from-aircall-to-telnyx
- url: https://support.telnyx.com/en/articles/14708129-porting-numbers-away-from-intercom-to-telnyx
- url: https://support.telnyx.com/en/articles/14708130-porting-numbers-away-from-resellers-aircall-intercom-ringcentral-vonage-etc
- url: https://support.telnyx.com/en/articles/15138152-making-calls-with-branded-calling
- url: https://support.telnyx.com/en/articles/3947850-porting-away-from-twilio
- url: https://support.telnyx.com/en/articles/5104103-port-your-microsoft-ms-teams-numbers
- url: https://support.telnyx.com/en/articles/8037040-inbound-call-screening
updated_at: 2026-07-17T09:01:08Z
---

# Porting Numbers to Telnyx

*Part 3 of 5 — see also: [Part 1](porting-numbers-to-telnyx--part-1.md), [Part 2](porting-numbers-to-telnyx--part-2.md), [Part 4](porting-numbers-to-telnyx--part-4.md), [Part 5](porting-numbers-to-telnyx--part-5.md)*

A consolidated reference for porting numbers to Telnyx from Skype, Twilio, Microsoft Teams, and VoIP resellers (Aircall, Intercom, RingCentral, Vonage, Grasshopper), including carrier-specific credentials, common porting errors (TN Not Portable, Invalid Reseller, Authorized Name Mismatch), and related voice features such as Repeat Call Guard, Branded Calling, and Inbound Call Screening.

## Repeat Call Guard (Outbound Voice Profiles)

Repeat Call Guard lets you manage call frequency to prevent repeated outbound calls to the same number within a day, protecting against over-dialing and supporting compliance with customer contact policies.

By default, outbound calls to the same destination number are unrestricted. With Repeat Call Guard enabled, you define active calling hours (start and end times in UTC) and a maximum number of allowed call attempts per destination number (CLD). Once the limit is reached, additional calls to that number are automatically blocked until the next day. Counters reset daily based on the configured time window.

This feature only applies to calls made through SIP connections and is configured per Outbound Voice Profile, meaning limits are tracked independently for each profile.

### Configuration

1. Log in to the Telnyx Customer Portal and go to **Voice → Outbound Voice Profiles**.
2. Select an existing profile or create a new one.
3. Find the **Repeat Call Guard** section below the Audio File Channel Type field.
4. Enable the toggle and configure:
   - **Start Time:** When call restrictions start in UTC (e.g., `08:00`)
   - **End Time:** When the restriction window ends in UTC (e.g., `18:00`)
   - **Calls per CLD:** How many times a single destination number can be called on a 24-hour rolling basis within the window
5. Click **Save**.

Repeat Call Guard uses a rolling reset within the daily active window. After hitting the max limit (e.g., 3 calls), the counter resets the next rolling 24 hours just after the time of the previous day's first allowed call, allowing a fresh slot from that point onward within the window.

**Example:** On Day 1, you make 3 calls starting at 14:00 (first at 14:00, then 14:30 and 15:10) — limit hit, blocking further calls in that window. On Day 2, the counter resets at 14:01, so you can make up to 3 new calls starting from 14:01 within the window. Calls before 14:01 on Day 2 are still blocked.

### API Configuration

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

When the limit is exceeded, Telnyx sends the message: `Daily calling restriction to Destination Number +11234567890 exceeded D66 (code 403)`.
