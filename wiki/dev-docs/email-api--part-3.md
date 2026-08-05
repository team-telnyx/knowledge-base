---
title: Email API
summary: Telnyx email API reference covering reusable Liquid-based email templates
  (create, manage, render, and send), unsubscribe groups for category-level opt-outs,
  and pre-send email validation (single and batch) with five structured checks.
sources:
- url: https://developers.telnyx.com/docs/messaging/email/templates/index
- url: https://developers.telnyx.com/docs/messaging/email/unsubscribe-groups
- url: https://developers.telnyx.com/docs/messaging/email/validation
updated_at: 2026-08-05T13:52:12Z
---

# Email API

*Part 3 of 3 — see also: [Part 1](email-api--part-1.md), [Part 2](email-api--part-2.md)*

Telnyx email API reference covering reusable Liquid-based email templates (create, manage, render, and send), unsubscribe groups for category-level opt-outs, and pre-send email validation (single and batch) with five structured checks.

## Email Validation

Validate email addresses before you send to reduce bounces, keep your sender reputation healthy, and avoid suppressing recipients unnecessarily. Telnyx runs five checks per address and returns a structured result you can act on.

Typical uses:

- **Pre-send hygiene** — check an address a user just typed in before you send to it, and offer a correction if they mistyped their provider.
- **List cleaning before import** — run a batch over a list you're about to import so you don't seed suppressions with addresses that can't deliver.
- **Reducing bounces** — a high hard-bounce rate hurts your domain reputation and can trigger suppression of otherwise-good recipients; validating first lets you drop the ones that fail.

All requests use the base URL `https://api.telnyx.com/v2` and an `Authorization: Bearer ***` header.

### What's checked

Every address is run through five checks. A failed syntax check short-circuits the rest (no DNS lookup is performed), and those checks return `pass: false` with a `details` note that they were skipped.

| Check | What it does | `checks` key |
| --- | --- | --- |
| **Syntax** | Practical email syntax validation — an RFC 5322-inspired ASCII subset, not the full grammar. Regex match for `local@domain.tld` (local part allows `A–Z a–z 0–9 . _ % + -`; TLD ≥ 2 letters) plus a 254-byte length cap. Plus-addressing (`user+tag@…`) is accepted; Unicode internationalized domains must be supplied as Punycode (`xn--…`). Quoted local parts, comments, and other exotic RFC 5322 forms are rejected. | `syntax` |
| **MX / deliverability signal** | DNS lookup for MX records on the address's domain. Falls back to an A record (RFC 5321). Treats RFC 7505 null-MX records and self-referencing wildcard-DNS MX records as "no records found." | `mx` |
| **Disposable domain** | Checks the domain against a community-maintained blocklist (5,000+ domains, refreshed periodically), including subdomain matching (`sub.mailinator.com` matches `mailinator.com`). | `disposable` |
| **Role-based address** | Checks the local part against a curated list of role prefixes (e.g. `admin`, `noreply`, `postmaster`, `support`). Informational — not a hard fail. | `role_based` |
| **Typo suggestion** | Compares the domain against 21 popular provider domains using Damerau-Levenshtein distance of 1 (handles insertions, deletions, substitutions, and adjacent transpositions). Returns a `suggestion` when close. | `typo` |

A result is `valid: true` only when `syntax`, `mx`, and `disposable` all pass. `role_based` and `typo` never flip `valid` to `false` — they're signals you choose how to act on.

### Validate one address

`POST /email_validations` validates a single address and returns synchronously. Any non-empty string is accepted; invalid syntax returns `valid: false` rather than a request error.

```
curl -X POST https://api.telnyx.com/v2/email_validations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ***" \
  -d '{
    "email": "user@gmai.com"
  }'
```

Response (`200`):

```
{
  "data": {
    "record_type": "email_validation",
    "email": "user@gmai.com",
    "valid": true,
    "risk_score": 0.1,
    "did_you_mean": "user@gmail.com",
    "checks": {
      "syntax": { "pass": true },
      "mx": { "pass": true, "details": "1 MX record found" },
      "disposable": { "pass": true },
      "role_based": { "pass": true },
      "typo": { "pass": false, "details": "Possible typo in domain", "suggestion": "gmail.com" }
    }
  }
}
```

This is the classic "likely typo" result: the address is technically deliverable (`valid: true`, syntax and MX pass), but the domain is one edit away from `gmail.com`, so the typo check fails and contributes `0.1` to `risk_score`. Prompt the user to confirm `did_you_mean` before sending.

A typo domain is not automatically a *valid* domain. Some common misspellings — `gmial.com` among them — are on the disposable blocklist, which makes `disposable.pass: false` and flips the whole result to `valid: false` with `risk_score: 0.7` (0.6 disposable + 0.1 typo). Always read `valid` and the individual `checks` rather than assuming a typo suggestion implies an otherwise-good address.

#### Result fields

| Field | Type | Notes |
| --- | --- | --- |
| `record_type` | string | Always `"email_validation"`. |
| `email` | string | The address as validated (leading/trailing whitespace trimmed). |
| `valid` | boolean | `true` only when `syntax`, `mx`, and `disposable` all pass. |
| `risk_score` | number | 0–1 weighted score. Higher is riskier: syntax fail contributes 1.0, mx fail 0.8, disposable 0.6, role-based 0.2, typo 0.1 — capped at 1.0. |
| `did_you_mean` | string | A full corrected address (`local@suggested-domain`) when the typo check found a suggestion. **Omitted entirely** (not `null`) when there is none. |
| `checks.syntax` | object | `{pass, details?}`. `details` present only when the check fails. |
| `checks.mx` | object | `{pass, details?}`. `details` reports MX record count, the A-record fallback, null-MX, wildcard-DNS, or a DNS lookup failure. |
| `checks.disposable` | object | `{pass, details?}`. `details: "Disposable email domain"` when the domain is on the blocklist. |
| `checks.role_based` | object | `{pass, details?}`. `details: "Role-based email address"` when the local part matches a role prefix. |
| `checks.typo` | object | `{pass, details?, suggestion?}`. `suggestion` holds the suggested domain when a close popular-domain match is found; omitted when nil. |

When syntax fails, the remaining checks are skipped and return `pass: false` with `details: "Skipped: syntax failed"`. `risk_score` is `1.0` in that case.

### Validate in batch

`POST /email_validations/batch` creates an asynchronous job for up to 1,000 addresses. The request returns immediately (`202`) with a batch ID you poll for results. Optionally pass a `webhook_url` to receive a POST when the batch completes.

```
curl -X POST https://api.telnyx.com/v2/email_validations/batch \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ***" \
  -d '{
    "emails": [
      "user@gmail.com",
      " admin@yahoo.com ",
      "user@gmail.com",
      "admin@yahoo.com"
    ],
    "webhook_url": "https://example.com/webhooks/email-validation"
  }'
```

Response (`202`):

```
{
  "data": {
    "record_type": "email_validation_batch",
    "id": "3f0c1b2a-4d5e-6f70-8190-2a3b4c5d6e7f",
    "status": "pending",
    "total": 2,
    "duplicates_removed": 2,
    "webhook_url": "https://example.com/webhooks/email-validation"
  }
}
```

#### Batch input rules

- **Max size:** 1,000 emails. Requests with more (before or after dedup) return `400`.
- **Deduplication:** emails are trimmed, blank strings are dropped, and the remainder is deduplicated case-insensitively (so `"User@Example.com"` and `"user@example.com"` count as one). `duplicates_removed` is the number of duplicates plus blanks discarded.
- **All-blank input:** returns `400` (`emails array must contain at least one email address`).
- **`webhook_url`:** optional HTTP(S) URL, max 2048 characters. Empty string is treated as omitted. SSRF-protected — private/reserved IPs and internal hostnames are rejected at creation and re-checked at delivery time. `webhook_url` is **omitted from both responses entirely** (not `null`) when unset.

#### Poll for results

`GET /email_validations/batch/{id}` returns the batch status and, once completed, a `results` map keyed by email address.

```
curl https://api.telnyx.com/v2/email_validations/batch/3f0c1b2a-4d5e-6f70-8190-2a3b4c5d6e7f \
  -H "Authorization: Bearer ***"
```

While processing (`status: "pending"` or `"processing"`):

```
{
  "data": {
    "record_type": "email_validation_batch",
    "id": "3f0c1b2a-4d5e-6f70-8190-2a3b4c5d6e7f",
    "status": "processing",
    "total": 2
  }
}
```

When complete (`status: "completed"`), `results` and `completed_at` appear:

```
{
  "data": {
    "record_type": "email_validation_batch",
    "id": "3f0c1b2a-4d5e-6f70-8190-2a3b4c5d6e7f",
    "status": "completed",
    "total": 2,
    "completed_at": "2026-07-06T12:00:05Z",
    "results": {
      "user@gmail.com": {
        "email": "user@gmail.com",
        "valid": true,
        "risk_score": 0.0,
        "checks": {
          "syntax": { "pass": true },
          "mx": { "pass": true, "details": "5 MX records found" },
          "disposable": { "pass": true },
          "role_based": { "pass": true },
          "typo": { "pass": true }
        }
      },
      "admin@yahoo.com": {
        "email": "admin@yahoo.com",
        "valid": true,
        "risk_score": 0.2,
        "checks": {
          "syntax": { "pass": true },
          "mx": { "pass": true, "details": "3 MX records found" },
          "disposable": { "pass": true },
          "role_based": { "pass": false, "details": "Role-based email address" },
          "typo": { "pass": true }
        }
      }
    }
  }
}
```

Batch status values: `pending`, `processing`, `completed`, `failed`. If the worker exhausts its retries, the batch is marked `failed`; a `failed` batch has no `results` map. Each result object has the same `email`, `valid`, `risk_score`, `did_you_mean?`, and `checks` shape as the single-address response. Note that the GET response does **not** include `duplicates_removed` (that's only on the create response).

#### Completion webhook

When you provide a `webhook_url`, the worker sends a `POST` to it once the batch finishes processing. The payload is a summary — the full per-address results come from polling the GET endpoint:

```
{
  "batch_id": "3f0c1b2a-4d5e-6f70-8190-2a3b4c5d6e7f",
  "total": 2,
  "valid": 2,
  "invalid": 0,
  "completed_at": "2026-07-06T12:00:05Z",
  "status": "completed"
}
```

Webhook delivery is best-effort: a non-2xx response or a network failure is logged but doesn't fail the batch. The webhook is sent **before** the batch record is marked `completed`, so a worker crash during delivery can cause Oban to retry and resend the webhook.

### Interpreting results

Use the checks to decide what to do with an address — validation is a strong signal, not a delivery guarantee.

| Outcome | Suggested action |
| --- | --- |
| `valid: true`, all checks pass | Safe to send. |
| `valid: true`, `role_based: false` | It's a shared mailbox (e.g. `support@`). Fine to send, but engagement is usually lower than for a personal address. |
| `valid: true`, `typo.pass: false` with `did_you_mean` | The user likely mistyped their provider, but the domain they typed does resolve. Prompt them to confirm `did_you_mean`, or use it directly for low-risk signups. A failing typo check never flips `valid` on its own. |
| `valid: false`, `mx.pass: false` | The domain has no mail exchanger (including RFC 7505 null-MX domains like `example.com`). Don't send — this will bounce. |
| `valid: false`, `disposable.pass: false` | The domain is a known throwaway provider. Decide whether to allow it for your signup flow; it won't deliver reliably long-term. Note some typo domains are also blocklisted, so you can see `typo.pass: false` and `disposable.pass: false` together. |
| `valid: false`, `syntax.pass: false` | The string isn't a valid address. Reject it; no other checks ran. |

Validation checks DNS records and known blocklists at validation time. It does **not** verify that a mailbox exists or that a message will be accepted by the receiving server. A `valid: true` address can still bounce if the mailbox is full, disabled, or behind a greylisting/accept-all policy. Treat validation as pre-send hygiene, not a delivery guarantee.
