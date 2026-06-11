---
title: 10DLC Messaging
summary: 10DLC (10-Digit Long Code) is the industry standard for application-to-person
  (A2P) messaging on US long code numbers. Registering your brand and campaigns with
  The Campaign Registry (TCR) through Telnyx provides higher throughput, better deliverability,
  and reduced carrier filtering. Your brand's vetting score directly determines your
  messaging throughput limits across AT&T, T-Mobile, and other carriers.
sources:
- url: https://developers.telnyx.com/docs/messaging/10dlc/10dlc-rate-limits/index
  content_hash: 9943ccfddd1c957dfe7878e5b4986f8fa9835d971ebd1b91e66f6da6a1a2712d
- url: https://developers.telnyx.com/docs/messaging/10dlc/brand-registration/index
  content_hash: 669ecf4a319d95ef7d8118e55118d4f6fa117267b9d14ddf62f6cae43aa0a8c6
- url: https://developers.telnyx.com/docs/messaging/10dlc/campaign-registration/index
  content_hash: d844d00c269f33c0327211f2c101598026d3bbb2c11f93b00d4ea81d113bf3ee
- url: https://developers.telnyx.com/docs/messaging/10dlc/campaign-use-cases
  content_hash: c73f74bb5dc7965cc6dd20978b78cf8e20385f1e182e850388d958c0d69700c4
- url: https://developers.telnyx.com/docs/messaging/10dlc/event-notifications/index
  content_hash: aef723a2d6f3c487373aa6d0158ed211985e6ec1ee5015195bc074b22a4dda5a
- url: https://developers.telnyx.com/docs/messaging/10dlc/isv-reseller-onboarding
  content_hash: af3fbd26d75cd780f923a80eb807b01a62035c2e6b93f238fd8c5906deb3a793
- url: https://developers.telnyx.com/docs/messaging/10dlc/phone-number-assignment
  content_hash: e7abb4216aadda176b528fc5534f03401c3920a1f26bb71b96f9c5467da1bbe3
- url: https://developers.telnyx.com/docs/messaging/10dlc/quickstart/index
  content_hash: d6e1b878528e10807fceeb1eac0dd13795f0fb71164c24bde7c30e4f0fced486
- url: https://developers.telnyx.com/docs/messaging/10dlc/sole-proprietor/index
  content_hash: 3a06ac956d054b870c43e88ec1bca52a6e8e6aa911aba3859735a40813023013
- url: https://developers.telnyx.com/docs/messaging/10dlc/troubleshooting/index
  content_hash: 216718dde2f7d3ed58832aeb8b1249d7b3d20bdccc6a4a0588225f99cb48a3ef
- url: https://developers.telnyx.com/docs/messaging/getting-started/choosing-your-sender-type/index
  content_hash: 754e129874cf330ed7df6e6c4f06b5f1ef44d65a1ed1774f6b453188cdba8a22
updated_at: 2026-06-11T10:36:45Z
---

# 10DLC Messaging

*Part 5 of 5 — see also: [Part 1](10dlc-messaging--part-1.md), [Part 2](10dlc-messaging--part-2.md), [Part 3](10dlc-messaging--part-3.md), [Part 4](10dlc-messaging--part-4.md)*

10DLC (10-Digit Long Code) is the industry standard for application-to-person (A2P) messaging on US long code numbers. Registering your brand and campaigns with The Campaign Registry (TCR) through Telnyx provides higher throughput, better deliverability, and reduced carrier filtering. Your brand's vetting score directly determines your messaging throughput limits across AT&T, T-Mobile, and other carriers.

## Compliance Checklist

Carriers can reduce throughput or reject campaigns that don't follow these guidelines:

| Requirement | Details |
| --- | --- |
| ✅ Website domain = email domain | `admin@acme.com` + `acme.com` |
| ✅ Company name matches website | Consistent branding across registration |
| ✅ Clear opt-in on website | SMS consent checkbox visible near submit button |
| ✅ Detailed campaign description | Specific, not vague or generic |
| ✅ Sample messages match use case | Realistic and representative |
| ✅ No disallowed content | No SHAFT, cannabis, payday lending, sweepstakes |
| ✅ Opt-out language in messages | Include "Reply STOP to unsubscribe" |
| ✅ Honor opt-outs immediately | Process STOP requests within seconds |
| ✅ Keep consent records | Maintain proof of opt-in (timestamp, source, phone number) for at least 4 years |

### Disallowed Use Cases

The following will be rejected or result in very low throughput:

- Unsolicited messaging (cold outreach, lead generation spam)
- Non-direct lending (3rd party auto loans, payday loans)
- Indirect debt collection
- Cannabis or CBD marketing
- Gambling (unless licensed)
- SHAFT content (Sex, Hate, Alcohol, Firearms, Tobacco)
- Sweepstakes and "free giveaway" campaigns

## Troubleshooting

### Brand Registration Failures

| Issue | Cause | Fix |
| --- | --- | --- |
| **EIN mismatch** | `companyName` doesn't match IRS records | Use exact legal name from EIN confirmation letter (CP 575) |
| **Invalid EIN format** | Must be `XX-XXXXXXX` | Double-check format; no spaces or extra characters |
| **Website not accessible** | Vetting partner couldn't access website | Ensure website is live, publicly accessible, and matches business |
| **Phone number not valid** | Not a valid, reachable US/CA number | Provide working business phone in E.164 format |
| **Address verification failed** | Address doesn't match USPS records | Verify via [USPS Address Lookup](https://tools.usps.com/zip-code-lookup.htm); use physical address, not PO Box |
| **Duplicate brand** | EIN already registered | One brand per EIN; contact support to transfer if registered elsewhere |
| **Duplicate vetting (error 10012)** | Same `evpId` + `vettingClass` already exists | Retrieve existing vettings; use different class or provider |
| **Low vetting score** | Incomplete or inconsistent data | Update brand info, ensure website/social media align, request re-vet or enhanced vetting |

### Campaign Rejection Reasons

| Rejection Reason | Fix |
| --- | --- |
| Samples don't match use case | Rewrite samples to match declared use case exactly |
| Missing opt-out language | Add "Reply STOP to unsubscribe" to every sample |
| Vague message flow | Describe exact opt-in mechanism (website form URL, keyword, etc.) |
| Prohibited content | Remove restricted content (cannabis, gambling, etc.) |
| Brand not vetted | Complete brand vetting before resubmitting |
| Insufficient sample variety | Provide 2–5 diverse samples showing different message types |
| URL shorteners used | Use full branded URLs, not bit.ly/tinyurl |

You cannot edit a rejected campaign. Create a new one with corrected information. Each submission incurs a TCR registration fee.

### Phone Number Assignment Failures

| Issue | Fix |
| --- | --- |
| Number not eligible for 10DLC | Verify it's a standard long code, not toll-free or short code |
| Number not on messaging profile | Assign number to a messaging profile first via `PATCH /v2/phone_numbers/{id}` |
| Campaign not active | Wait for carrier approval; check status via API |
| Number already assigned to another campaign | Remove from current campaign first, then reassign |
| AT&T registration timeout | Wait up to 7 business days; AT&T processes in batches |
| Messages still filtered after assignment | Wait 24–72 hours for carrier propagation; verify content matches campaign |

### Message Delivery Errors

| Error Code | Description | Fix |
| --- | --- | --- |
| `40300` | Number not registered for 10DLC | Assign sending number to an approved campaign |
| `40301` | Campaign suspended | Check campaign status; contact support |
| `40302` | Brand suspended | Resolve brand compliance issues |
| `40310` | Rate limit exceeded | Reduce sending rate; see rate limits |
| `40311` | Daily message limit reached | Wait for daily reset or increase vetting score |
| `40320` | Content flagged by carrier | Review message content for SHAFT violations |
| `40321` | URL blocked by carrier | Remove or replace flagged URLs; use branded short links |

### Carrier-Specific Behaviors

**AT&T:** 3–7 business days for number registration; aggressive URL filtering (avoid URL shorteners); lowest per-campaign limits with vetting score having the largest impact; will suspend campaigns with spam complaints without warning.

**T-Mobile:** Blocks messages with prohibited content patterns; requires 24h cooldown when moving numbers between campaigns; enforces strict daily per-number limits; automatically blocks messages to numbers that texted STOP.

**Verizon:** Generally fastest registration processing; less aggressive filtering than AT&T/T-Mobile; more generous throughput at all vetting tiers.

### Diagnostic Checklist

1. Verify brand status: `GET /v2/10dlc/brand/{brandId}` — confirm `identityStatus` is `VERIFIED` or `VETTED_VERIFIED`
2. Verify campaign status: `GET /v2/10dlc/campaign/{campaignId}` — confirm `campaignStatus` is `ACTIVE`
3. Verify number assignment: `GET /v2/10dlc/phoneNumberCampaign?phoneNumber={number}`
4. Check event notifications for rejection, suspension, or status change events
5. Review Message Detail Records for specific error codes on failed messages
6. Compare sending rate against your campaign throughput limits
