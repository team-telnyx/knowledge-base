---
title: Toll-Free Verification with Business Registration Fields
summary: Telnyx toll-free verification now includes mandatory Business Registration
  Number (BRN) fields starting February 17, 2026, to improve carrier compliance, speed
  reviews, and reduce fraud. This guide explains required/optional fields, API usage,
  validation and error handling, migration steps, and includes troubleshooting guidance
  for rejections and post-verification delivery issues.
sources:
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/index
  content_hash: eed1b0b21c0a803b0fbca66cf8a40e345216fe5ba857d02c1240881aa87a82e1
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/troubleshooting
  content_hash: ed027a01b9954dab62c82dda4c5e476109f5031e7ffe3faf78596cba08639df6
updated_at: 2026-05-20T09:12:49Z
---

# Toll-Free Verification with Business Registration Fields

*Part 2 of 2 — see also: [Part 1](toll-free-verification-with-business-registration-fields--part-1.md)*

Telnyx toll-free verification now includes mandatory Business Registration Number (BRN) fields starting February 17, 2026, to improve carrier compliance, speed reviews, and reduce fraud. This guide explains required/optional fields, API usage, validation and error handling, migration steps, and includes troubleshooting guidance for rejections and post-verification delivery issues.

## Rejection reasons and fixes
Business information
- Business name mismatch: Ensure businessName exactly matches government records (include Inc./LLC/Corp. suffixes). Use legal name, not DBA.
- BRN cannot be verified: Ensure the number exists, matches the name, type matches the number format (e.g., EIN), and issuing country is correct. For US sole proprietors using SSN, legal name must match.
- Website unreachable/doesn’t match: Publicly accessible, shows company name, content aligns to use case, preferably HTTPS; avoid parked/under-construction pages.
- Contact info invalid: Use a reachable phone and a business-domain email tied to the company; contact must be authorized.
- Entity type mismatch: Choose the value that matches your registration (SOLE_PROPRIETOR, PRIVATE_PROFIT, PUBLIC_PROFIT, NON_PROFIT, GOVERNMENT).

Messaging use case
- Samples don’t match use case: Provide realistic samples that clearly reflect the declared use case.
- Missing opt-out language: Include opt-out text (e.g., “Reply STOP to unsubscribe”) in every sample.
- Volume inconsistent: Align messageVolume with your use case; justify higher volumes when applicable.
- Opt-in mechanism unclear: Describe the full consent flow (where, exact consent language, single/double opt-in, record-keeping).
- Prohibited/restricted content: Remove prohibited content (e.g., cannabis/CBD, adult). For regulated industries, include relevant licensing; contact Telnyx Support if unsure.

## Resubmission workflow
- Read the rejection reason via API or the Telnyx Portal and identify exact issues.
- PATCH only the fields that need correction (businessName, BRN fields, useCaseSummary, sample messages, etc.).
- No separate submit step: updated requests are re-queued automatically.
- Monitor results via webhooks (event type like toll_free_verification.status_update) and alert your team on approval/rejection.
Do’s and don’ts
- Do correct only the cited issue; use exact legal names; provide realistic samples with opt-out.
- Don’t shotgun-change everything or resubmit repeatedly in quick succession.

## Post-verification delivery issues
Throughput tiers (typical)
- Unverified: ~0.25 MPS; heavy filtering.
- Pending review: ~1 MPS.
- Verified: up to 20 MPS with minimal filtering.

Common delivery errors
- 40002 Blocked as spam: Avoid spammy content/phrasing, stay away from public URL shorteners, stagger sends, ensure recipients haven’t opted out.
- 40005 Destination unreachable: Validate numbers (e.g., Number Lookup) and remove non-SMS-capable lines.
- 40011 Rate limit exceeded: Implement client-side rate limiting; consider number pooling for scale.
- 40014 Message expired in queue: Reduce send rate, watch for carrier backlogs, set shorter validity for time-sensitive traffic.

Best practices
- Ramp volumes gradually after approval; monitor per-carrier delivery using [Message Detail Records](message-detail-records.md).
- Keep opt-out processing healthy; high complaint rates trigger filtering.
- Consider [Short Codes](short-codes.md) or [10DLC Registration](10dlc-registration.md) for higher sustained throughput needs.

## Status tracking
Via API
- Get a specific request by ID with GET /public/api/v2/requests/{id} and inspect verification status, phoneNumbers, and any rejection reason.
- List requests with pagination to audit all submissions.

Via Portal
- Telnyx Portal → Messaging → Toll-Free Verification: view status, reasons, and submission details.

Status reference
- draft: Created but incomplete — add required fields and submit.
- pending: Under carrier review — expect 1–2 weeks.
- verified: Approved — full throughput unlocked.
- rejected: Fix issues and resubmit via PATCH.

## Diagnostic checklist
Before submitting
- Legal name matches official records (include suffixes like Inc./LLC).
- BRN is valid and matches the legal name and type; country code is correct.
- Website is live, public, and shows the business name; content aligns to use case.
- Contact phone/email are valid and business-associated.
- entityType matches registration.
- useCaseSummary is clear; sample messages are realistic and include opt-out text.
- Opt-in workflow describes where/how consent is captured and stored.
- messageVolume is reasonable for the use case.

After rejection
- Read the full reason; cross-reference this guide.
- Fix only the cited issue; verify against official records.
- Resubmit via PATCH; set webhooks to track the outcome.

After verification (delivery)
- Confirm the number is on an active messaging profile.
- Stay within throughput; implement rate limiting.
- Review content for spam triggers; ensure opt-out processing works.
- Monitor MDRs and error codes for patterns.

## Toll-free vs. 10DLC: choosing the right channel
- Setup time: Toll-free ~1–2 weeks; 10DLC typically days (brand + campaign).
- Throughput: Toll-free up to ~20 MPS; 10DLC varies by vetting (can exceed with enhanced tiers and pooling).
- Cost: Toll-free per-message; 10DLC per-message plus campaign fees.
- Number presentation: Toll-free is national; 10DLC offers local presence.
- Many businesses use both: toll-free for support/national reach; 10DLC for local presence and some high-volume transactional/marketing with number pools.

## Related resources
- [Toll-Free Verification API](toll-free-verification-api.md)
- [Messaging API](messaging-api.md)
- [10DLC Registration](10dlc-registration.md)
- [Advanced Opt-In/Out](advanced-opt-in-out.md)
- [Number Pool](number-pool.md)
- [Rate Limiting](rate-limiting.md)
- [Error Code Reference](error-code-reference.md)
- [Message Detail Records](message-detail-records.md)

## Support
- Support Portal: https://support.telnyx.com
- Email: support@telnyx.com
- Developer community: share questions and learn from peers
