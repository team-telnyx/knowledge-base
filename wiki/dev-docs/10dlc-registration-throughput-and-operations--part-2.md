---
title: '10DLC: Registration, Throughput, and Operations'
summary: 'A practical, end-to-end guide to US 10DLC messaging with Telnyx: how to
  register brands and campaigns, understand throughput by carrier, assign numbers,
  set up webhooks, support ISV/partner architectures, complete Sole Proprietor flows,
  and troubleshoot common issues.'
sources:
- url: https://developers.telnyx.com/docs/messaging/10dlc/10dlc-rate-limits/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/brand-registration/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/campaign-registration/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/campaign-use-cases
- url: https://developers.telnyx.com/docs/messaging/10dlc/event-notifications/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/isv-reseller-onboarding
- url: https://developers.telnyx.com/docs/messaging/10dlc/phone-number-assignment
- url: https://developers.telnyx.com/docs/messaging/10dlc/quickstart/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/sole-proprietor/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/troubleshooting/index
updated_at: 2026-05-20T08:58:06Z
---

# 10DLC: Registration, Throughput, and Operations

*Part 2 of 2 — see also: [Part 1](10dlc-registration-throughput-and-operations--part-1.md)*

A practical, end-to-end guide to US 10DLC messaging with Telnyx: how to register brands and campaigns, understand throughput by carrier, assign numbers, set up webhooks, support ISV/partner architectures, complete Sole Proprietor flows, and troubleshoot common issues.

## Monitoring, troubleshooting, and common errors
See full guidance in [10DLC Troubleshooting Guide](10dlc-troubleshooting-guide.md). Highlights:

- Brand failures: EIN/company name mismatch; invalid address; unreachable/mismatched website; duplicate brand; duplicate or pending vetting; low vetting score; SP OTP failures
- Campaign rejections: Samples mismatch use case; missing opt‑out; vague opt‑in; prohibited content; brand not vetted; duplicate campaign; insufficient/too‑similar samples
- Number assignment issues: Ineligible number (toll‑free/short code/not messaging‑enabled/already assigned); campaign not active; AT&T registration delays (batching); T‑Mobile number rejections
- Delivery failures (common codes):
  - 40300 number not registered → assign to approved campaign
  - 40301/40302 campaign/brand suspended → check status/events
  - 40310 rate limit exceeded → slow down per carrier limits
  - 40311 daily cap reached → wait for reset or improve vetting
  - 40320 content flagged; 40321 URL blocked → adjust content/links
- Carrier nuances:
  - AT&T: 3–7 day registration delays possible; stricter URL filtering; lowest per‑campaign limits
  - T‑Mobile: strict daily caps and opt‑out enforcement; cooldown when moving numbers
  - Verizon: faster processing; relies more on content compliance
- Diagnostics checklist:
  1) Brand status VERIFIED/VETTED_VERIFIED
  2) Campaign status ACTIVE/MNO_PROVISIONED
  3) Number assigned to that campaign
  4) Review 10DLC webhooks for rejections/suspensions
  5) Inspect Message Detail Records
  6) Compare send rate vs. your limits (see [10DLC Rate Limits & Throughput](10dlc-rate-limits-throughput.md))

## Compliance checklist and disallowed content
Carriers can throttle or reject if you miss fundamentals:
- Website domain and email domain align; company name consistent
- Clear opt‑in on website; detailed campaign description
- Samples match use case and include opt‑out language
- Disallowed or restricted: unsolicited spam; indirect/debt collection; cannabis/CBD; gambling (unless licensed); payday/non‑direct lending; SHAFT (Sex, Hate, Alcohol, Firearms, Tobacco); sweepstakes/free giveaways
- Honor STOP/HELP/START keywords; see Opt‑In/Out best practices in [Campaign Use Case Examples & Sample Messages](campaign-use-case-examples-sample-messages.md) and [10DLC Campaign Registration](10dlc-campaign-registration.md)

## API quick references (minimal)
- Brands: POST /v2/10dlc/brand; GET /v2/10dlc/brand/{brandId}; PUT/PATCH to update; POST /v2/10dlc/brand/{brandId}/externalVetting (or /vetting); list with pagination
- Campaigns: POST /v2/10dlc/campaignBuilder (or /campaign per API evolution); GET /v2/10dlc/campaignBuilder/{campaignId}; list campaigns; appeal/update per campaign type
- Phone numbers: POST /v2/10dlc/phoneNumberCampaign to assign; DELETE to remove; list assignments with filters
- Webhooks: Set brand/campaign webhookURL and optional webhookFailoverURL; events: 10dlc.brand.update, 10dlc.campaign.update, 10dlc.phone_number.update
For end‑to‑end examples and payloads, see [10DLC Event Notifications](10dlc-event-notifications.md).

## Related resources
- [Getting Started with 10DLC](getting-started-with-10dlc.md)
- [10DLC Brand Registration](10dlc-brand-registration.md)
- [10DLC Campaign Registration](10dlc-campaign-registration.md)
- [Campaign Use Case Examples & Sample Messages](campaign-use-case-examples-sample-messages.md)
- [10DLC Phone Number Assignment](10dlc-phone-number-assignment.md)
- [10DLC Event Notifications](10dlc-event-notifications.md)
- [ISV & Reseller 10DLC Onboarding](isv-reseller-10dlc-onboarding.md)
- [Sole Proprietor 10DLC Registration](sole-proprietor-10dlc-registration.md)
- [10DLC Troubleshooting Guide](10dlc-troubleshooting-guide.md)
- [10DLC Rate Limits & Throughput](10dlc-rate-limits-throughput.md)
- [Message Detail Records](message-detail-records.md)

Note: Brand and campaign registration occurs with The Campaign Registry (TCR). Learn more at https://www.campaignregistry.com/.
