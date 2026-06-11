---
title: Branded Calling
summary: Branded Calling displays your verified business identity (name, logo, call
  reason) on recipients' phones before they answer, increasing answer rates and building
  trust. The product suite also includes Number Reputation, a standalone monitoring
  tool that reports spam risk scores for your outbound numbers.
sources:
- url: https://developers.telnyx.com/docs/branded-calling/bc-phone-numbers/index
- url: https://developers.telnyx.com/docs/branded-calling/brands/index
- url: https://developers.telnyx.com/docs/branded-calling/call-reasons/index
- url: https://developers.telnyx.com/docs/branded-calling/enterprises/index
- url: https://developers.telnyx.com/docs/branded-calling/infringement-claims/index
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/index
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/loa
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/phone-numbers
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/quickstart
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/remediation
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/settings
- url: https://developers.telnyx.com/docs/branded-calling/overview
- url: https://developers.telnyx.com/docs/branded-calling/quickstart
- url: https://developers.telnyx.com/docs/branded-calling/terms-of-service/index
updated_at: 2026-06-11T10:26:56Z
---

# Branded Calling

*Part 4 of 6 — see also: [Part 1](branded-calling--part-1.md), [Part 2](branded-calling--part-2.md), [Part 3](branded-calling--part-3.md), [Part 5](branded-calling--part-5.md), [Part 6](branded-calling--part-6.md)*

Branded Calling displays your verified business identity (name, logo, call reason) on recipients' phones before they answer, increasing answer rates and building trust. The product suite also includes Number Reputation, a standalone monitoring tool that reports spam risk scores for your outbound numbers.

## Infringement Claims

If a third party believes your DIR's display name, logo, or content infringes on a protected right, they can file an infringement claim through Telnyx. You cannot create claims through the API, but you can read and contest claims filed against your DIRs.

While a claim is `pending` or `contested`:
- The DIR is moved to `suspended` and branded calling pauses.
- You **cannot add phone numbers** (returns `400`).
- You **cannot delete** the DIR (returns `409`).
- You **cannot re-submit** with `POST /submit` (returns `409`, blocked by the `no_active_claims` gate).
- To revise content during an open claim, use `PUT /v2/dir/{dir_id}/infringement_update`.

### Claim Lifecycle

```
pending ──► contested  (you submit a contest)
        ──► resolved   (Telnyx admin adjudicates)

resolved.resolution = upheld    → DIR moves to permanently_rejected (terminal)
resolved.resolution = rejected  → claim dismissed; DIR restored to verified
resolved.resolution = modified  → partial outcome; DIR status unchanged, read resolution_notes
```

### API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/v2/dir/{dir_id}/infringement_claims` | List claims against a DIR |
| `GET` | `/v2/infringement_claims/{claim_id}` | Get a single claim |
| `POST` | `/v2/infringement_claims/{claim_id}/contest` | File a contest |

### Contesting a Claim

```
curl -X POST https://api.telnyx.com/v2/infringement_claims/{claim_id}/contest \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contest_notes": "Acme Plumbing LLC has been operating under this name since 2008.",
    "documents": [
      {
        "document_id": "d1e2f3a4-573d-446d-b3ce-aff9117272a6",
        "document_type": "trademark_registration",
        "description": "Our 2008 state trademark registration."
      }
    ]
  }'
```

- `contest_notes`: required, 10–2000 characters.
- `documents`: optional, up to 20 per submission. Duplicate `document_id`s within one submission are rejected.
- The first submission moves the claim from `pending` to `contested`; later submissions append additional notes and documents without changing status.
- Contesting a `resolved` claim returns `400`.

### Fix-and-Resubmit a Suspended DIR

Use `PUT /v2/dir/{dir_id}/infringement_update` to atomically apply a content fix and re-submit for vetting in one call, **without waiting for the claim to be resolved**:

```
curl -X PUT https://api.telnyx.com/v2/dir/{dir_id}/infringement_update \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "display_name": "Acme Local Plumbing",
    "logo_url": "https://acmeplumbing.example.com/logo-v2-256.bmp",
    "certify_no_infringement": true,
    "certify_brand_is_accurate": true,
    "certify_no_shaft_content": true,
    "certify_ip_ownership": true,
    "infringement_resolution_notes": "Renamed to Acme Local Plumbing and replaced the logo."
  }'
```

Requirements:
- The DIR must have an active (unresolved) claim and be in `suspended` status.
- All four certifications must be `true`.
- `infringement_resolution_notes` is required (10–500 chars).
- Content fields (`display_name`, `logo_url`, `call_reasons`) are all optional; send only the ones you're changing.

After the update, the DIR moves to `submitted` and goes through vetting again, even though the claim is still open. If vetting passes, the DIR returns to `verified`. If it fails, the DIR returns to `suspended` and you can update again. You can submit `infringement_update` multiple times.

This endpoint bypasses the `no_active_claims` gate by design. The standard `PATCH` + `POST /submit` flow only works after the claim is `resolved` with `resolution = modified`.

### After the Claim Resolves

- **`resolution = rejected`**: DIR is automatically restored to `verified`. No action required.
- **`resolution = upheld`**: DIR is `permanently_rejected` (terminal). Create a new DIR with corrected content; you may reuse the same enterprise.
- **`resolution = modified`**: Read `resolution_notes` for required edits, then `PATCH` the DIR and `POST /submit`.

## Number Reputation

Number Reputation is a **standalone monitoring product** that lets you query the spam reputation of your outbound calling phone numbers. It reports spam risk and scores but does not change how calls are placed. Reputation data is sourced from the major call-analytics networks used by US carriers.

Each number returns:

| Field | Values | Meaning |
|-------|--------|----------|
| `spam_risk` | `low` / `medium` / `high` / `null` | Overall spam likelihood. `high` = likely flagged as spam. |
| `maturity_score` | 0–100 or `null` | Maturity metric. |
| `connection_score` | 0–100 or `null` | Connection metric. |
| `engagement_score` | 0–100 or `null` | Engagement metric. |
| `sentiment_score` | 0–100 or `null` | Sentiment metric. |
| `spam_category` | string or `null` | Category label if flagged. Opaque string; set may grow. `null` = not flagged. |
| `last_refreshed_at` | ISO 8601 or `null` | When data was last updated. `null` = no check performed yet. |

A `null` score means there isn't enough data. The `reputation_data` object as a whole is `null` until the first refresh is collected.

### Number Reputation Workflow

1. Register your business as an [Enterprise](enterprises.md).
2. Render, sign, and upload an LOA to get a `loa_document_id`.
3. Enable Number Reputation with that `loa_document_id` (billable).
4. Wait for both approval gates: `status` **and** `loa_status` must each be `approved`.
5. Associate phone numbers for monitoring (up to 100 per request, US numbers, E.164, billable).
6. Query reputation scores (cached = free, fresh = billed).
7. Automatic monitoring re-checks on a configurable schedule.

### Constraints

| Constraint | Limit |
|------------|-------|
| Phone number format | E.164 (`+1NPANXXXXXX`), US numbers only |
| Numbers per add request | 100 (atomic — all-or-nothing) |
| Score range | 0–100 (`null` = insufficient data) |
| Account access | Verified and enterprise-level accounts only |
| Approval gates | Both `status` and `loa_status` must be `approved` |
