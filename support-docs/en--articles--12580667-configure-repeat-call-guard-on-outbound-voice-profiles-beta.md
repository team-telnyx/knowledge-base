---
source_url: https://support.telnyx.com/en/articles/12580667-configure-repeat-call-guard-on-outbound-voice-profiles-beta
scraped: 2026-07-08
content_hash: fb43cf98394528f486f9c1c354bcdb7bc67058815891be0c1a9d9e142aedade4
---

Configure Repeat Call Guard on Outbound Voice Profiles (BETA) | Telnyx Help Center

[Skip to main content](#main-content)

# Configure Repeat Call Guard on Outbound Voice Profiles (BETA)

Control how many times a destination number can be called within a specific time window.

Written by Telnyx Engineering

October 24, 2025

Table of contents

## Background

The **Repeat Call Guard** feature lets users manage call frequency to prevent repeated outbound calls to the same number within a day. This protects against over-dialing and ensures compliance with customer contact policies.

## Standard Behavior

1. Outbound calls can be made to the same destination number without restriction.
2. Call frequency limits depend only on the user’s dialing logic.

## New Behavior (with Repeat Call Guard Enabled)

1. Users define active calling hours (start and end times).
2. Users set a maximum number of allowed call attempts per destination number (CLD).
3. Once the limit is reached, additional calls to that number are automatically blocked until the next day.
4. Counters reset daily based on the configured time window.

**Note:** This feature only applies to **calls made through SIP connections** and is **configured per Outbound Voice Profile**, meaning limits are tracked independently for each profile.

---

## Pre-requisites

Before you begin, make sure you have:

* Access to the **Telnyx Customer Portal**
* An existing **Outbound Voice Profile**
* A valid **Telnyx API key**

---

## Step 1: Navigate to Outbound Voice Profiles

1. Log in to the **Telnyx Customer Portal**.
2. Go to **Voice → Outbound Voice Profiles**.
3. Select an existing profile or create a new one.

---

## Step 2: Locate the Repeat Call Guard Section

You’ll find the **Repeat Call Guard** section **below the Audio File Channel Type field** on the profile configuration page at the bottom.

---

## Step 3: Configure Repeat Call Guard

Enable the toggle to activate **Repeat Call Guard**.

* **Start Time:** Define when call restrictions start in UTC.  
  Example: `08:00`
* **End Time:** Define when the restriction window ends in UTC.   
  Example: `18:00`
* **Calls per CLD:** Set how many times a single destination number can be called on a 24 hour rolling basis within the window.  
  ​

**Note on Rolling Reset:** Repeat Call Guard uses a rolling reset for the call counter within daily active window hours (e.g., 8:00–18:00 UTC). After hitting the max limit (e.g., 3 calls), the counter resets the next rolling 24 hours just after the time of the previous day's *first* allowed call, allowing a fresh slot from that point onward within the window.

**Example:** On Day 1, you make 3 calls starting at 14:00 (first at 14:00, then 14:30 and 15:10)—limit hit, blocking further calls in that window. On Day 2, the counter resets at 14:01, so you can make up to 1 new call of 3 starting from 14:01 within the window (e.g., at 14:01, 14:40, 16:00). The other 2 open up when their 24 hr mark hits. Calls before 14:01 on Day 2 are still blocked.

---

## Step 4: Save Your Settings

Click **Save** to apply the configuration.  
Your outbound profile will now enforce the set call limits within the defined time window.

---

## Configure via API (Optional)

You can configure Repeat Call Guard directly through the Telnyx API.

**Curl example:**

```
curl -L -X PATCH 'https://api.telnyx.com/v2/outbound_voice_profiles/{profileID}' \ -H 'Content-Type: application/json' \ -H 'Accept: application/json' \ -H 'Authorization: Bearer KEYxxxxxxxxxxxxxxxxxxxxxxx' \ -d '{   "name": "time",   "calling_window": {     "start_time": "02:01",     "end_time": "22:01",     "calls_per_cld": 4   } }'
```

Replace `{profileID}` and the `Authorization` key with your actual values.

---

## Step 5: Verify the Configuration

Once saved, verify that:

* The toggle shows **Enabled**.
* The correct **Start Time**, **End Time**, and **Calls per CLD** values appear.
* Calls exceeding the defined limit during the window are automatically blocked. A message "`Daily calling restriction to Destination Number +11234567890 exceeded D66 (code 403)`" will be sent by Telnyx.

---

## Tips for Success

* Configure the timezone correctly. Times are saved in UTC, so you will have to ensure the time entered is converted from that target location's local time to UTC equivalent.
* Remember that the call limit resets daily at midnight.
* Disable the feature temporarily if you need unrestricted outbound dialing.

---

## References

* [Telnyx Portal - Outbound Voice Profiles](https://portal.telnyx.com/#/outbound-profiles)
* [Telnyx API Reference – Outbound Voice Profiles](https://developers.telnyx.com/)

---

Related Articles

[Configuring a Cisco CME Credentials Trunk](https://support.telnyx.com/en/articles/1130668-configuring-a-cisco-cme-credentials-trunk)[Distinguish your outbound profiles & DIDs](https://support.telnyx.com/en/articles/1130721-distinguish-your-outbound-profiles-dids)[More About Outbound Voice Profiles](https://support.telnyx.com/en/articles/4320411-more-about-outbound-voice-profiles)[Configuring Call Control/TeXML Applications - Voice API](https://support.telnyx.com/en/articles/4374050-configuring-call-control-texml-applications-voice-api)[HD Voice - Number Feature](https://support.telnyx.com/en/articles/8394071-hd-voice-number-feature)

Did this answer your question?

😞😐😃

Table of contents
