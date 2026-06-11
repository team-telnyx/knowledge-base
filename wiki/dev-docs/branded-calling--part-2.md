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

*Part 2 of 6 — see also: [Part 1](branded-calling--part-1.md), [Part 3](branded-calling--part-3.md), [Part 4](branded-calling--part-4.md), [Part 5](branded-calling--part-5.md), [Part 6](branded-calling--part-6.md)*

Branded Calling displays your verified business identity (name, logo, call reason) on recipients' phones before they answer, increasing answer rates and building trust. The product suite also includes Number Reputation, a standalone monitoring tool that reports spam risk scores for your outbound numbers.

## Display Identity Records

A DIR defines what recipients see: display name, optional logo, and 1–10 call reasons. DIRs must be vetted and approved by Telnyx before becoming active.

### API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/v2/enterprises/{enterprise_id}/dir` | Create a DIR under an enterprise |
| `GET` | `/v2/dir` | List DIRs across the account |
| `GET` | `/v2/enterprises/{enterprise_id}/dir` | List DIRs under one enterprise |
| `GET` | `/v2/dir/{dir_id}` | Get a DIR |
| `PATCH` | `/v2/dir/{dir_id}` | Update a DIR |
| `DELETE` | `/v2/dir/{dir_id}` | Delete a DIR |
| `POST` | `/v2/dir/{dir_id}/submit` | Submit for vetting |

### Required Fields

| Field | Description |
|-------|-------------|
| `display_name` | Shown to recipients. 1–35 chars, no emoji, not whitespace-only. |
| `authorizer_name` | Authorizer point-of-contact name. Max 255 chars. |
| `authorizer_email` | Authorizer point-of-contact email. |
| `certify_brand_is_accurate` | Must be `true`. |
| `certify_no_shaft_content` | Must be `true`. (SHAFT = Sex, Hate, Alcohol, Firearms, Tobacco.) |
| `certify_ip_ownership` | Must be `true`. |
| `call_reasons` | Array of 1–10 strings, each 1–64 characters. |

### Optional Fields

| Field | Description |
|-------|-------------|
| `logo_url` | HTTPS URL (max 128 chars) to a 256×256 BMP image (≤1 MB, ≤32-bit color depth). Telnyx downloads and validates on every create/PATCH. PNG, JPEG, and other formats are rejected with `400`. |
| `documents` | Up to 20 entries of `{document_id, document_type, description?}`. Each `document_id` must come from a prior upload to the Telnyx Documents API. Documents are append-only — existing documents are never removed by a PATCH. |
| `reselling` | Boolean. `true` if you resell calling services on behalf of others. Defaults to `false`. |

### Document Types

Each document entry's `document_type` must be one of: `letter_of_authorization`, `business_registration`, `articles_of_incorporation`, `tax_document`, `ein_letter`, `trademark_registration`, `website_ownership`, `business_license`, `professional_license`, `government_id`, `utility_bill`, `bank_statement`, `other`.

### DIR Statuses

| Status | Meaning |
|--------|---------|
| `draft` | Initial state. Editable. |
| `submitted` | Vetting requested. Editing, deleting, and re-submitting are blocked. |
| `in_review` | Telnyx is actively reviewing. Same restrictions as `submitted`. |
| `verified` | Approved. Phone numbers can be attached. Editable, but a non-trivial PATCH moves the DIR back to `draft` and tears down the live registration. |
| `rejected` | Vetting failed for fixable reasons. Edit and re-submit. |
| `unsuccessful` | Vetting failed for a system reason. Edit and re-submit. |
| `suspended` | DIR has an attached infringement claim (Telnyx may pre-emptively suspend while a claim is `pending` or `contested`). `PATCH` is allowed but `POST /submit` is blocked with `409` while the claim is open. Use `PUT /v2/dir/{dir_id}/infringement_update` instead. |
| `expired` | The one-year verification window has closed. Re-submit to renew. |
| `infringement_claimed` | Legacy status. New claims move the DIR to `suspended`. |
| `permanently_rejected` | Terminal. Cannot be re-submitted. The only exit is `DELETE`. |

### Updating a DIR

`PATCH` is allowed in `draft`, `rejected`, `unsuccessful`, `suspended`, and `verified`.

- **`draft` / `rejected` / `unsuccessful`**: `PATCH` is a pure edit; status doesn't change. Call `POST /submit` to re-vet when ready.
- **`suspended`**: `PATCH` is allowed and leaves status unchanged, but `POST /submit` is blocked with `409` while an infringement claim is `pending` or `contested`. Use `PUT /v2/dir/{dir_id}/infringement_update` instead.
- **`verified`**: A `PATCH` that actually changes a field flips the DIR back to `draft` and tears down the live registration. The DIR stops serving branded identity until you `POST /submit` and are re-approved.
- If you provide `logo_url`, it is re-downloaded and re-validated on every `PATCH`.
- `documents` are append-only; existing documents are never removed by a `PATCH`.

### Resubmitting After Rejection

When a DIR is `rejected` or `unsuccessful`, check `rejection_reasons` on the DIR and the reviewer notes on the comments thread (`GET /v2/dir/{dir_id}/comments`). Fix with `PATCH`, then:

```
curl -X POST https://api.telnyx.com/v2/dir/{dir_id}/submit \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Deleting a DIR

```
curl -X DELETE https://api.telnyx.com/v2/dir/{dir_id} \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Allowed in: `draft`, `rejected`, `unsuccessful`, `verified`, `suspended`, `expired`, `infringement_claimed`, and `permanently_rejected`. The mid-vetting statuses `submitted` and `in_review` return `400`. The DIR must have **no phone numbers still attached** — remove them with `DELETE /v2/dir/{dir_id}/phone_numbers` first. Returns `409` if the DIR has a `pending` or `contested` infringement claim.

## Call Reasons

A call reason is a short string explaining why your business is calling (e.g. "Appointment Reminder", "Delivery Update"). Call reasons are set at the DIR level as a list of 1–10 strings (each up to 64 characters).

Telnyx maintains a list of **pre-approved** call reasons. When a DIR's call reasons are *all* pre-approved, the call-reason vetting check passes automatically (the DIR still goes through full vetting; pre-approved reasons are not auto-approval). If any reason is custom, that check is reviewed by a human, which can take longer.

### API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/v2/call_reasons` | List pre-approved call reasons. Default `page[size]` is 100 (max 250). |
| `POST` | `/v2/call_reasons/validate` | Check whether a list of reasons is fully pre-approved. |

### Validate Call Reasons

```
curl -X POST https://api.telnyx.com/v2/call_reasons/validate \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '["Appointment Reminder", "Follow-Up Calls"]'
```

The body is a **bare JSON array of strings** — do not wrap it in `{ "call_reasons": [...] }`. The result is returned under `data` with three fields: `all_pre_approved` (true when every reason is pre-approved), `requires_manual_vetting` (true when at least one is not), and `non_approved_reasons` (the list of non-pre-approved reasons).

### Constraints

| Limit | Value |
|-------|-------|
| Min call reasons per DIR | 1 |
| Max call reasons per DIR | 10 |
| Max characters per reason | 64 |
