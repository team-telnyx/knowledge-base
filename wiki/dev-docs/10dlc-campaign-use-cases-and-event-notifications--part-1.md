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

*Part 1 of 8 — see also: [Part 2](10dlc-campaign-use-cases-and-event-notifications--part-2.md), [Part 3](10dlc-campaign-use-cases-and-event-notifications--part-3.md), [Part 4](10dlc-campaign-use-cases-and-event-notifications--part-4.md), [Part 5](10dlc-campaign-use-cases-and-event-notifications--part-5.md), [Part 6](10dlc-campaign-use-cases-and-event-notifications--part-6.md), [Part 7](10dlc-campaign-use-cases-and-event-notifications--part-7.md), [Part 8](10dlc-campaign-use-cases-and-event-notifications--part-8.md)*

Comprehensive guide to Telnyx 10DLC campaign use cases, sample messages, opt-in/opt-out requirements, and webhook event notifications for brands, campaigns, and phone numbers. Includes SDK examples, retry policies, and campaign appeal mechanisms.

## Overview

Writing good sample messages is the #1 factor in getting your 10DLC campaign approved. Carriers reject campaigns when sample messages don't match the declared use case, lack opt-out language, or look like spam. This page covers both the campaign use case requirements and the webhook event notifications you can configure to track registration, review, and provisioning status in real time.

**How carriers review sample messages:**

- Must match the declared use case type
- Must include opt-out language (STOP to opt out)
- Must represent actual messages you'll send
- Vague or generic samples get rejected
