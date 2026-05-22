---
title: '10DLC: Registration, Throughput, and Operations'
summary: 'A practical, end-to-end guide to US 10DLC messaging with Telnyx: how to
  register brands and campaigns, understand throughput by carrier, assign numbers,
  set up webhooks, support ISV/partner architectures, complete Sole Proprietor flows,
  and troubleshoot common issues.'
sources:
- url: https://developers.telnyx.com/docs/messaging/10dlc/10dlc-rate-limits/index
  content_hash: 778f91edfc3b519d1fa78264b75d243101835bcccd1c70887dfcdb3d50a9c44f
- url: https://developers.telnyx.com/docs/messaging/10dlc/brand-registration/index
  content_hash: 39994ba318e4e3a7c75131a82eb25a5d5c2bd96f09d80f7cac667f9839b761b8
- url: https://developers.telnyx.com/docs/messaging/10dlc/campaign-registration/index
  content_hash: a6fc32def70955fd17e93a7cb8caa7589bb18c2316d95ed430a6aa7fed716bef
- url: https://developers.telnyx.com/docs/messaging/10dlc/campaign-use-cases
  content_hash: b729b07db7aa6e397bc369537b41919329ecd85382829a651396f419a6cda9a1
- url: https://developers.telnyx.com/docs/messaging/10dlc/event-notifications/index
  content_hash: 13ffe17f5284335d505b05bee75dacfea349d0f56c9ec36eed38140093157fc9
- url: https://developers.telnyx.com/docs/messaging/10dlc/isv-reseller-onboarding
  content_hash: 9cfed36e574cb16f51643a2ea50a1bde4185ce070c60ab2984454476d4b00aa9
- url: https://developers.telnyx.com/docs/messaging/10dlc/phone-number-assignment
  content_hash: 8451069b16cf46a423a7cbaa6d754d641aaaca2c7c00d241847e8ac67d9f4189
- url: https://developers.telnyx.com/docs/messaging/10dlc/quickstart/index
  content_hash: d55fc696fae83f278f2ab9783caac528414f28745237054dde41ec1aaa37eda8
- url: https://developers.telnyx.com/docs/messaging/10dlc/sole-proprietor/index
  content_hash: ff779403c2902d0a478596637a911a878e4ee0451119d869cfdf96f08e95307d
- url: https://developers.telnyx.com/docs/messaging/10dlc/troubleshooting/index
  content_hash: 4676e2401045f5dd8e34238444dc85c6f3b9a77f3dd30e488f17116abce7d015
updated_at: 2026-05-20T08:58:06Z
---

# 10DLC: Registration, Throughput, and Operations

*Part 1 of 2 — see also: [Part 2](10dlc-registration-throughput-and-operations--part-2.md)*

A practical, end-to-end guide to US 10DLC messaging with Telnyx: how to register brands and campaigns, understand throughput by carrier, assign numbers, set up webhooks, support ISV/partner architectures, complete Sole Proprietor flows, and troubleshoot common issues.

## What 10DLC is and why register
10DLC (10‑Digit Long Code) is the standard for A2P messaging over US long codes. Registering your brand and campaigns with The Campaign Registry (TCR) via Telnyx improves deliverability, unlocks higher throughput, and reduces carrier filtering. See [Getting Started with 10DLC](getting-started-with-10dlc.md).

## End‑to‑end registration flow
- Create Brand: Register your business identity with TCR (instant)
- Vet Brand: Third‑party vetting assigns a 0–100 trust score (typically 1–7 business days)
- Create Campaign: Register your messaging use case; carriers review (varies; see timeline below)
- Assign Numbers: Link US long code numbers to the approved campaign (instant after approval)
Tip: Vetting is critical; your score drives throughput. See [10DLC Rate Limits & Throughput](10dlc-rate-limits-throughput.md).

## Throughput and rate limits by carrier
Throughput depends on brand vetting score and campaign type; carriers apply different controls.

- AT&T (per‑campaign, TPM = messages/min):
  - Standard classes (score‑based):
    - A/B (75–100): 4,500 SMS TPM; 2,400 MMS TPM
    - C/D (50–74): 2,400 SMS TPM; 1,200 MMS TPM
    - E/F (1–49): 240 SMS TPM; 150 MMS TPM
    - T (Low Volume Mixed): 75 SMS TPM; 50 MMS TPM
    - W (Sole Proprietor): 15 SMS TPM; 50 MMS TPM
  - Special use cases (fixed):
    - Political K: 4,500 SMS TPM; 2,400 MMS TPM
    - Charity/Nonprofit P: 2,400 SMS TPM; 1,200 MMS TPM
    - Social S: 9,000 SMS TPM; 2,400 MMS TPM
    - Emergency X: 4,500 SMS TPM; 2,400 MMS TPM
    - Proxy G (per number): 60 SMS TPM; 50 MMS TPM
    - Agents & Franchises N (per number): 60 SMS TPM; 50 MMS TPM
  - Conversion: 4,500 TPM ≈ 75 MPS.

- T‑Mobile (brand‑level daily caps shared across all campaigns):
  - Top (75–100): 200,000/day
  - High (50–74): 40,000/day
  - Medium (25–49): 10,000/day
  - Basic (1–24 or unvetted): 2,000/day
  - Sole Proprietor: 1,000/day

- Verizon: No published numeric caps; relies on content compliance with registered use case.

Vetting score guidance (brand level):
- 75–100: Highest throughput; ideal for production
- 50–74: Good for moderate volume
- 25–49: Limited; consider enhanced vetting
- 1–24 or Unvetted: Very limited; improve score and get vetted

## Brand registration essentials
A brand is your business identity at TCR. Register via Telnyx API/Portal. See [10DLC Brand Registration](10dlc-brand-registration.md).

- Entity types: PRIVATE_PROFIT, PUBLIC_PROFIT, NON_PROFIT, GOVERNMENT, SOLE_PROPRIETOR
- Key fields: displayName, companyName (exact IRS legal name), EIN, phone, address, email, website, vertical
- Statuses: SELF_DECLARED, VERIFIED, VETTED_VERIFIED, UNVERIFIED
- External vetting: STANDARD (~$4) or ENHANCED (~$40). Idempotency prevents duplicate active vettings for the same provider/class.
- Common rejection reasons (and fixes): EIN/name mismatch, invalid EIN format, website unreachable or mismatched, invalid phone, address mismatch, duplicate brand (EIN already registered)
- Appeals: Review reason, correct data, re‑vet; contact support for complex cases.
- Webhooks: Receive brand lifecycle updates via [10DLC Event Notifications](10dlc-event-notifications.md).

## Campaign registration essentials
A campaign declares your use case (what you send, who receives it, how they opted in). See [10DLC Campaign Registration](10dlc-campaign-registration.md).

- Common use cases: MIXED, MARKETING, CUSTOMER_CARE, DELIVERY_NOTIFICATION, ACCOUNT_NOTIFICATION, 2FA, SECURITY_ALERT, POLLING_VOTING, CHARITY, POLITICAL
- Special use cases: LOW_VOLUME, SOLE_PROPRIETOR, EMERGENCY, AGENTS_FRANCHISES, SWEEPSTAKES
- Required fields: brandId, usecase, description, sample1/2 (2–5 recommended), messageFlow, helpMessage, opt‑in/opt‑out/help keywords
- Provisioning timeline per carrier (typical): T‑Mobile instant–24h; AT&T 1–3 business days; Verizon 1–3 business days; US Cellular 3–5 business days
- Statuses: ACTIVE, EXPIRED, SUSPENDED; detailed lifecycle states arrive via webhooks
- Rejections: You cannot edit a rejected campaign—create a new one with corrected details

## Writing samples that pass review
See templates and patterns in [Campaign Use Case Examples & Sample Messages](campaign-use-case-examples-sample-messages.md). Essentials:
- Always include opt‑out text (“Reply STOP to unsubscribe”) in samples
- Make samples realistic, specific, and brand‑named; avoid placeholders
- Ensure samples match the declared use case exactly (no marketing in non‑marketing use cases)
- Use branded, full URLs; avoid public URL shorteners
- Describe opt‑in flow clearly (where/how consent is captured, confirmation, message types)

## Phone number assignment and number pools
Assign US long codes to an approved campaign before sending. See [10DLC Phone Number Assignment](10dlc-phone-number-assignment.md).

- Requirements: US 10DLC number; assigned to a messaging profile; campaign must be ACTIVE; a number can belong to only one campaign at a time
- Number Pools: If using number pools, every pool number must be assigned to the same campaign; otherwise delivery will be inconsistent
- Propagation: Some carrier provisioning can take 24–72 hours after assignment
- Troubleshooting: Ensure number is on your account and messaging‑enabled, in E.164 format, not already assigned, and that the campaign is active

## Webhooks and event notifications
Configure brand/campaign webhookURL (and optional webhookFailoverURL) to receive JSON event posts. See [10DLC Event Notifications](10dlc-event-notifications.md).

- Event types: 10dlc.brand.update, 10dlc.campaign.update, 10dlc.phone_number.update
- Brand payload types: REGISTRATION, ORDER_EXTERNAL_VETTING, REVET, TCR_BRAND_UPDATE
- Campaign payload types: REGISTRATION, TELNYX_REVIEW, NUMBER_POOL_PROVISIONED/DEPROVISIONED, TCR_EVENT, MNO_REVIEW, TELNYX_EVENT, VERIFIED
- Phone number payload types: ASSIGNMENT, DELETION, STATUS_UPDATE
- Appeals & nudging: Native campaigns can be appealed via API; partner campaigns use CAMPAIGN_NUDGE from the CSP
- Delivery: Retry policy with multiple attempts; return HTTP 2xx quickly, deduplicate by event id; use HTTPS and consider signature verification; test with tools like ngrok/Cloudflare Tunnel

## ISV and reseller architectures
If you message on behalf of customers, use partner (shared) campaign architecture. See [ISV & Reseller 10DLC Onboarding](isv-reseller-10dlc-onboarding.md).

- Concepts: Upstream CSP (where you register), Downstream CSP (Telnyx for delivery), Partner/Shared Campaigns, Campaign Sharing (must be accepted)
- Patterns:
  - One brand + campaign per customer (best isolation, recommended)
  - Shared platform campaign (simpler, shared limits/risks)
  - Hybrid: shared for low‑volume; dedicated for high‑volume
- Steps: Register each customer’s brand; submit ENHANCED vetting if volume warrants; create AGENTS_FRANCHISES campaigns; share to Telnyx; Telnyx accepts; assign numbers; send
- Appeals: Partner campaigns re‑enter review via CSP CAMPAIGN_NUDGE (native uses direct appeal)
- ISV compliance: Customer vetting, content monitoring, opt‑in/out enforcement, volume management, quick incident response, record retention, samples matching production

## Sole Proprietor specifics
For individuals without an EIN. See [Sole Proprietor 10DLC Registration](sole-proprietor-10dlc-registration.md).

- Constraints: 1 campaign per brand; 1 number per campaign; low throughput; mobile phone reuse limited (up to 3 SP brands per mobile)
- OTP flow: Create SOLE_PROPRIETOR brand → trigger SMS OTP (pinSms includes @OTP_PIN@) → verify PIN → brand becomes VERIFIED → create SOLE_PROPRIETOR campaign → assign one number
- Typical fees and auto‑approval: SP campaigns often activate quickly once OTP is verified
