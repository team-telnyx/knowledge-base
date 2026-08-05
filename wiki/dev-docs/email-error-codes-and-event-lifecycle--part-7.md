---
title: Email Error Codes and Event Lifecycle
summary: Reference for the Telnyx Email API's two error families — synchronous HTTP
  errors (10xxx) returned on the API request itself, and asynchronous delivery errors
  (30xxx) reported later via webhooks and Email Detail Records — together with the
  per-recipient event lifecycle that drives them.
sources:
- url: https://developers.telnyx.com/docs/messaging/email/error-codes
- url: https://developers.telnyx.com/docs/messaging/email/event-lifecycle
updated_at: 2026-08-05T13:54:42Z
---

# Email Error Codes and Event Lifecycle

*Part 7 of 9 — see also: [Part 1](email-error-codes-and-event-lifecycle--part-1.md), [Part 2](email-error-codes-and-event-lifecycle--part-2.md), [Part 3](email-error-codes-and-event-lifecycle--part-3.md), [Part 4](email-error-codes-and-event-lifecycle--part-4.md), [Part 5](email-error-codes-and-event-lifecycle--part-5.md), [Part 6](email-error-codes-and-event-lifecycle--part-6.md), [Part 8](email-error-codes-and-event-lifecycle--part-8.md), [Part 9](email-error-codes-and-event-lifecycle--part-9.md)*

Reference for the Telnyx Email API's two error families — synchronous HTTP errors (10xxx) returned on the API request itself, and asynchronous delivery errors (30xxx) reported later via webhooks and Email Detail Records — together with the per-recipient event lifecycle that drives them.

## The Email Detail Record (EDR)

The **Email Detail Record** is the durable, per-recipient record of what happened. Where webhooks are a real-time notification you might miss, the EDR is the system of record used for billing, support, and reconciliation. **One recipient = one EDR identity.** The recipient's UUID is the stable EDR UUID, so a message to five people produces five EDR identities.

### What produces an EDR — and what doesn't

EDRs are published at three points, not on every event:

- **Sandbox acceptance** — a provisional record per recipient (`billable` forced false); sandbox never enters the send pipeline, so this is its only publication point.
- **Injection outcomes** — a provisional record for each recipient the MTA accepted, and a final record for each recipient it refused (`gw_reject`).
- **Applicable callback transitions** — a `Reception`, `Delivery`, `TransientFailure`, `Bounce`, `OOB`, `AdminBounce`, or `Expiration` that actually moves the recipient forward.

Nothing else publishes one:

- **Engagement events** (`email.opened`, `email.clicked`, `email.unsubscribed`) create stored events and webhooks but never invoke the EDR publisher.
- **Complaints on an already-`delivered` or `bounced` recipient** are state-machine no-ops, so they produce no new record.
- **Ambiguous injection timeouts** explicitly get no EDR — the outcome is unknown. If a late `Reception` reconciles the recipient to `sent`, that transition publishes the provisional record.
- **Pre-dispatch system failures** write stored events and update recipient rows directly; they do not publish an EDR.

### Provisional and final records

For a recipient **accepted by the MTA**, the first record is **provisional** — a unique-per-recipient rating intent, so a pipeline replay cannot create a second one. Every subsequent lifecycle transition (deferred, delivered, OOB, bounce, expiry) publishes an **append-only final** record: a new row that carries the same recipient UUID as its stable EDR identity. Records are never rewritten in place.

**A refused recipient starts final, not provisional.** When the MTA refuses injection, the recipient goes straight to `gw_reject` and a single **final** EDR is published for it — there is no provisional record first, because there was never a rating intent to reserve. Do not assume every EDR identity begins with a provisional row.

### Lifecycle fields

| Field | Meaning |
| --- | --- |
| `status` | Current lifecycle state — the field you want. One of `queued`, `sending`, `sent`, `deferred`, `delivered`, `bounced`, `failed`, `expired`, `suppressed`, `cancelled`, `gw_reject` |
| `created_at` | API acceptance time |
| `sent_at` | Queue acceptance by the MTA |
| `delivered_at` | Remote MX accepted |
| `deferred_at` | **First** transient failure |
| `bounced_at` | Permanent rejection |
| `failed_at` | System/operator non-delivery |
| `expired_at` | MTA retry window expired |
| `suppressed_at` | Recipient was suppressed before sending |
| `completed_at` | First terminal outcome |
| `attempt_count` | Delivery attempts made |
| `expired` / `suppressed` | Booleans mirroring the terminal condition |
| `billable` | Whether this recipient counts toward usage |

Every lifecycle timestamp is **set-once**: it locks on first acceptance, and a later record that tries to overwrite a stamped value is rejected. That is why `deferred_at` is the first deferral rather than the most recent one — a retry never rewrites it, and it never rewrites `sent_at` either.

**`delivery_status` is not the lifecycle state.** Despite the name, the EDR's `delivery_status` field is a fixed platform-level field currently emitted as `"not_configured"`. Read **`status`** for the delivery outcome. Filtering or branching on `delivery_status` will not do what you expect.

### Error fields

Two structured fields carry failure detail, and both use the **normalized 30xxx error taxonomy** — not raw SMTP codes. Raw SMTP codes vary per remote MX, collide across unrelated failure modes, and are absent entirely for failures that never reached SMTP (queue expiry, suppression, gateway rejection). The EDR therefore carries a product-level code and preserves the raw SMTP status alongside it as `smtp_status`.

#### The 30xxx taxonomy

| Code | Title | `source` | `retryable` | Raised when |
| --- | --- | --- | --- | --- |
| `30001` | Hard bounce | `smtp` | `false` | `bounced` with a 5xx code, or a bounce with no usable code |
| `30002` | Deferred | `smtp` | `true` | `deferred`, or `bounced` carrying a 4xx code |
| `30003` | Injection failure | `mta` | `false` | `failed` **with** an SMTP status — the MTA refused the injection |
| `30004` | Suppressed recipient | `api` | `false` | `suppressed` — the address was on the suppression list |
| `30005` | Queue expiry | `mta` | `false` | `expired` — the retry window elapsed |
| `30006` | Gateway rejection | `api` | `false` | `gw_reject` — refused at the HTTP injection boundary |
| `30099` | Internal error | `api` | `false` | `failed` **without** an SMTP status — nothing reached the MTA |

#### `error_evidence`

Six fields. Required on every error status: `bounced`, `failed`, `deferred`, `expired`, `suppressed`, `gw_reject`. Omitted entirely on success statuses.

```
{
  "error_evidence": {
    "code": "30001",
    "message": "5.1.1 The email account that you tried to reach does not exist",
    "enhanced_code": "5.1.1",
    "source": "smtp",
    "smtp_status": 550,
    "retryable": false
  }
}
```

| Key | Type | Meaning |
| --- | --- | --- |
| `code` | string | Normalized 30xxx taxonomy code. **Never** a raw SMTP code — a record carrying `"550"` here is rejected before publication |
| `message` | string | null | Diagnostic text from the receiving server. Required when `source` is `smtp`; null for failures that never reached a remote host |
| `enhanced_code` | string | null | RFC 3463 enhanced status code in `X.Y.Z` form (`"5.1.1"`) |
| `source` | string | Where the failure originated: `smtp`, `mta`, `api`, `dns`, `dkim`, or `spam` |
| `smtp_status` | integer | null | The raw SMTP status code, preserved for ops triage (`550`, `421`) |
| `retryable` | boolean | Whether retrying this address could succeed |

#### `errors[]`

Seven fields per entry. Non-empty for every error status, empty for success statuses.

```
{
  "errors": [
    {
      "code": "30001",
      "title": "Hard bounce",
      "detail": "5.1.1 The email account that you tried to reach does not exist",
      "source": "smtp",
      "smtp_status": 550,
      "enhanced_code": "5.1.1",
      "retryable": false
    }
  ]
}
```

| Key | Type | Meaning |
| --- | --- | --- |
| `code` | string | Normalized 30xxx code — structurally required |
| `title` | string | Human-readable taxonomy title (`"Hard bounce"`, `"Queue expiry"`) — structurally required |
| `detail` | string | null | Diagnostic text. **This field is named `detail`, not `message`** |
| `source` | string | `smtp`, `mta`, `api`, `dns`, `dkim`, or `spam` — structurally required |
| `smtp_status` | integer | null | Raw SMTP status code when one exists |
| `enhanced_code` | string | null | Enhanced status code when one exists |
| `retryable` | boolean | Structurally required |

`code`, `title`, `source`, and `retryable` are present on every entry. `detail`, `smtp_status`, and `enhanced_code` legitimately stay null for failures that never reached SMTP — fabricating a response string would be worse than leaving it empty.

### Webhook payloads

Webhook payloads are **not** a projection of the full EDR. They are built from a compact recipient-scoped shape:

```
{
  "id": "8f2b1c34-...",
  "recipient_id": "6c0a9d51-...",
  "status": "bounced",
  "occurred_at": "2026-07-24T12:00:00.000000Z",
  "from": { "email": "you@yourdomain.com", "name": "Your App" },
  "subject": "Your receipt",
  "to": { "email": "user@example.com", "name": null, "kind": "to" }
}
```

| Field | Meaning |
| --- | --- |
| `id` | The message ID |
| `recipient_id` | The durable recipient row UUID — your join key |
| `status` | The **event type** (`queued`, `sent`, `delivered`, `bounced`, `deferred`, `failed`, `injection_timeout`, …), not the recipient's internal status |
| `occurred_at` | When the event occurred |
| `from` | Sender address and display name |
| `subject` | Message subject |
| `to` / `cc` / `bcc` | Exactly one recipient projection — `{email, name, kind}`. The key names which envelope field this recipient came from. BCC addresses are redacted to a stable HMAC sentinel |

On error events (`bounced`, `failed`, `deferred`, `expired`, `suppressed`, `gw_reject` recipient statuses) the payload additionally carries `error_evidence` and `errors[]`. Scheduled sends add `send_at`; ambiguous-injection events add `ambiguous_timeout: true`.

**The raw `smtp_code` / `smtp_response` compatibility fields are conditional.** They are present only when the failure carries callback-driven SMTP evidence — a `Bounce`, `TransientFailure`, `OOB`, `AdminBounce`, or `Expiration` record from KumoMTA that actually reached the wire. Failures raised before SMTP was ever spoken carry **no** `smtp_code` or `smtp_response` at all. Injection refusals (`gw_reject`, code `30006`) build their payload from the normalized error contract only: `error_evidence` and `errors[]`, with `smtp_status` and `message` explicitly `null`. Treat `error_evidence` as the field you branch on, and both raw SMTP fields as optional extras that may be absent entirely.

**What a webhook payload does not contain.** Billing fields (`billable`, `sandbox`), EDR lifecycle timestamps (`sent_at`, `delivered_at`, `bounced_at`, `expired_at`, …), SMTP-host evidence (`sending_ip`, `mx_hostname`, `mx_ip`), tags, and `bounce_category` are **not** forwarded into the published webhook. These fields are not uniformly recoverable elsewhere. Billing fields, lifecycle timestamps, and SMTP-host evidence live on the **EDR**. `bounce_category` is internal: it is not on the webhook, and it is not written into the recipient-scoped event row that `GET /v2/email_events` returns. The stored event returned by that endpoint carries a **sanitized** payload — internal correlation fields are stripped before it is returned — so it is not a full EDR replacement. Null values are **not** stripped — `"name": null` is sent as an explicit null. Handle nulls rather than assuming key absence. If you need the full record, use the authoritative per-recipient status endpoint or the EDR — not a `recipient_id` join against `GET /v2/email_events`, whose public payload omits the internal recipient identifiers.
