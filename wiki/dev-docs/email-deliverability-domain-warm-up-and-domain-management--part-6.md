---
title: Email Deliverability, Domain Warm-up, and Domain Management
summary: How mailbox providers evaluate mail, how to authenticate and warm up a sending
  domain with Telnyx, how to read delivery events and error codes, and how to register,
  verify, and manage email domains.
sources:
- url: https://developers.telnyx.com/docs/messaging/email/deliverability-best-practices
- url: https://developers.telnyx.com/docs/messaging/email/deliverability/index
- url: https://developers.telnyx.com/docs/messaging/email/domains/index
updated_at: 2026-08-05T13:54:17Z
---

# Email Deliverability, Domain Warm-up, and Domain Management

*Part 6 of 7 — see also: [Part 1](email-deliverability-domain-warm-up-and-domain-management--part-1.md), [Part 2](email-deliverability-domain-warm-up-and-domain-management--part-2.md), [Part 3](email-deliverability-domain-warm-up-and-domain-management--part-3.md), [Part 4](email-deliverability-domain-warm-up-and-domain-management--part-4.md), [Part 5](email-deliverability-domain-warm-up-and-domain-management--part-5.md), [Part 7](email-deliverability-domain-warm-up-and-domain-management--part-7.md)*

How mailbox providers evaluate mail, how to authenticate and warm up a sending domain with Telnyx, how to read delivery events and error codes, and how to register, verify, and manage email domains.

## Understanding delivery error codes

Telnyx reports failures at two distinct levels. Confusing them sends you looking in the wrong place.

### API-level errors (10xxx)

These occur **before** a message exists — your request was rejected. They are about your API call, not about deliverability.

| Code | Meaning | Deliverability relevance |
| --- | --- | --- |
| `10015` | Validation failed / bad request | Malformed fields; nothing was sent |
| `10007` | Forbidden | The Email API's generic Forbidden code. Covers domain not verified, suspended, degraded, missing an active DKIM key, a `from` address outside the domain's sending profile, trial-account recipient restrictions, and insufficient authorization scope. Read `detail` to find out which |
| `10008` | Forbidden (shared domain) | Returned by the email **domains** service when you try to modify, verify, or delete a Telnyx-managed shared domain. Shared domains are usable for sending by every account but read-only for non-owners |
| `10027` | Idempotency conflict | Same `Idempotency-Key` reused with a different body. Enforced at the API gateway, not by the Email service |
| `10036` | Still processing | Same key, same body — the original request is in flight. Also gateway-enforced |
| `reputation_suspended` | Sending suspended | The domain's reputation band dropped to `poor` |

`10007` is a service-wide code, not a domain-authentication signal. Several unrelated policy failures share it, so branching on the code alone will mislead you — always inspect the `detail` string (and, where present, `source`) to identify the actual cause before acting on it.

`10007` and `reputation_suspended` are the two that most often carry genuine deliverability meaning: the first frequently indicates your domain isn't verified or your `from` address isn't authorized, the second says your reputation has already degraded far enough that Telnyx stopped sending. See [Error Codes](error-codes.md) for the complete reference.

### Delivery-level errors

These occur **after** the message was accepted — the send happened and delivery failed.

**`bounce_category`** appears on `email.bounced` events and identifies *why* the bounce occurred:

| Value | Origin | Meaning |
| --- | --- | --- |
| `permanent` | KumoMTA `Bounce` record | The MTA classified the failure as a permanent bounce. This is the record category, **not** proof that the address is invalid |
| `transient` | Retries exhausted | Repeated 4xx responses; the MTA gave up |
| `admin` | Operator-initiated | Cancelled in flight — not a recipient-side signal |
| `oob` | Out-of-band report | The remote MTA accepted, then asynchronously rejected |

`permanent` is the default category assigned to any `Bounce` record — it is derived from the record type, not from the SMTP code. A `permanent` bounce is therefore *not* the same thing as a confirmed invalid address, and it does not by itself mean the recipient was suppressed. Suppression is decided separately, by narrower enhanced-code rules, and it happens asynchronously. `transient` as a bounce category is likewise not the same as an `email.deferred` event. A deferral is still being retried. A `transient` bounce means retrying already happened and failed — the message is permanently undelivered even though every individual failure was temporary.

**`error_evidence`** is the structured error field on the Email Detail Record (EDR). It is populated for every error status — `bounced`, `failed`, `deferred`, `expired`, `suppressed`, and `gw_reject` — and is null for successful ones:

| Field | Contents |
| --- | --- |
| `code` | The **normalized Telnyx delivery error code** (`30001`–`30099`), as a string |
| `message` | The callback/MTA delivery detail text, when available. Usually the remote server's response, but operator-initiated failures carry Telnyx-generated text |
| `enhanced_code` | The enhanced SMTP status code in `X.Y.Z` form, when the remote server supplied one |
| `source` | Which layer produced the error: `smtp`, `mta`, `api`, `dns`, `dkim`, or `spam` |
| `smtp_status` | The **raw SMTP response code** as an integer (for example `550`, `421`), when the failure reached SMTP |
| `retryable` | Whether Telnyx will retry this failure automatically |

`error_evidence.code` is always a normalized `30xxx` code — never a raw SMTP code. The raw SMTP response lives in `smtp_status`. If your integration matches on `code == "550"` it will never fire; match on `code == "30001"` and read `smtp_status` when you need the remote server's exact response.

#### Normalized delivery error codes (30xxx)

Raw SMTP codes are a poor integration surface: they vary per remote MX, they collide across unrelated failure modes, and they are absent entirely for failures that never reached SMTP (queue expiry, suppression, gateway rejection). Telnyx therefore normalizes every delivery failure into a small product-level taxonomy.

| Code | Title | Source | Retryable | What it means |
| --- | --- | --- | --- | --- |
| `30001` | Hard bounce | `smtp` | No | The remote MX permanently rejected the recipient (5xx), or bounced without a usable code |
| `30002` | Deferred | `smtp` | Yes | A transient rejection (4xx). Telnyx is still retrying |
| `30003` | Injection failure | `mta` | No | The outbound MTA refused the injection |
| `30004` | Suppressed recipient | `api` | No | The recipient was on a suppression list |
| `30005` | Queue expiry | `mta` | No | Retries were exhausted and the MTA gave up |
| `30006` | Gateway rejection | `api` | No | The message was refused before entering the queue |
| `30099` | Internal error | `api` | No | The send failed before anything reached the MTA |

The status is the primary axis of classification; the SMTP code only disambiguates where one status covers both a permanent and a transient failure. A `bounced` recipient carrying a 4xx response is classified `30002` (retryable) rather than `30001`, because the remote server's own code says the rejection was temporary.

The `message` field is the most diagnostically useful and the least structured. It carries whatever delivery detail the callback supplied, and its provenance depends on who generated the failure: an SMTP rejection carries the receiving provider's own free text — frequently a URL explaining a block, or a specific reason the numeric code cannot convey — while an operator-initiated failure such as an admin bounce carries Telnyx-generated text instead. Do not assume the string came from the remote host. Failures that never produced a callback at all — suppression and gateway rejection — have no delivery detail to carry, so `message` is null there rather than fabricated.

**Enhanced codes drive suppression.** Telnyx uses the `X.Y.Z` class — not the `30xxx` code — to decide whether a bounce reflects a bad address or a policy decision. Codes in the `5.1.x` (bad destination address) and `5.2.x` (mailbox status — disabled, full) ranges indicate a recipient-side problem and qualify for auto-suppression. Codes in the `5.7.x` range are security and policy rejections and are *not* suppressed, because the address may be perfectly valid while your sending configuration is not. A bounce with no enhanced code at all falls back to the raw SMTP code: 5xx qualifies for suppression, anything else does not.

That distinction matters when you are diagnosing a spike in bounces. A wave of `5.1.1` responses means your list has decayed. A wave of `5.7.x` responses means the receiver is rejecting your mail on security or policy grounds and the recipients themselves are probably fine.

### Record status values

The EDR carries a `status` field describing the recipient's delivery outcome. For outbound mail the possible values are `queued`, `sending`, `sent`, `deferred`, `delivered`, `bounced`, `failed`, `expired`, `suppressed`, `cancelled`, and `gw_reject`. Inbound records use `received` and `delivered`.

Three values are easy to misread. `failed` means a sender-side or operator-side non-delivery — the remote MX never rejected the recipient — which is why an admin bounce maps to `failed` rather than `bounced`. `expired` is its own terminal status, not a flavor of `failed`: it means the MTA exhausted its retries and gave up (`30005`). `gw_reject` means the message was refused before entering the queue, and is never billable.

#### `injection_timeout`: a recipient state with no detail record

`injection_timeout` is a recipient and webhook state, **not** an EDR status. It occurs when the injection request to the MTA times out ambiguously — the MTA may or may not have accepted the recipient, and Telnyx cannot tell which. Retrying would risk a duplicate send, so the recipient is parked in this terminal state instead.

Because the outcome is genuinely unknown, **no detail record is emitted**. The recipient enters a terminal `injection_timeout` state. Note: `injection_timeout` is not currently available as a subscribable webhook event type. If the MTA did in fact accept the message, its later Reception callback reconciles the recipient to `sent` and a detail record is published then. If no callback ever arrives, the recipient stays in `injection_timeout` and no EDR is ever produced.

Reconcile on the webhook, not on the absence of a record. An `injection_timeout` webhook with no corresponding EDR does not mean the message failed — it means the outcome is not yet known. Treat the delivery outcome as unknown and do not retry — a later `sent` transition may reconcile the state, but if no callback arrives, `injection_timeout` remains terminal and no definitive delivery outcome is available.
