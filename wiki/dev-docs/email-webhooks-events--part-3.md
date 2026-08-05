---
title: Email Webhooks & Events
summary: Telnyx email events flow through three consumption surfaces — recipient-scoped
  webhooks, the Events API for polling, and per-message lookups — covering the full
  lifecycle from queued through delivered, bounced, and engagement signals, plus domain
  lifecycle events. This page documents the event model, webhook payload envelope,
  signature verification, polling endpoints, and how to combine both surfaces in production.
sources:
- url: https://developers.telnyx.com/docs/messaging/email/webhooks-events/index
updated_at: 2026-08-05T13:53:18Z
---

# Email Webhooks & Events

*Part 3 of 5 — see also: [Part 1](email-webhooks-events--part-1.md), [Part 2](email-webhooks-events--part-2.md), [Part 4](email-webhooks-events--part-4.md), [Part 5](email-webhooks-events--part-5.md)*

Telnyx email events flow through three consumption surfaces — recipient-scoped webhooks, the Events API for polling, and per-message lookups — covering the full lifecycle from queued through delivered, bounced, and engagement signals, plus domain lifecycle events. This page documents the event model, webhook payload envelope, signature verification, polling endpoints, and how to combine both surfaces in production.

## Consume via webhooks

Webhooks push events to your HTTPS endpoint in real time. Email webhooks are **scoped to a domain**: you create a subscription on a specific email domain, and it fires only for the event types you allowlist on that subscription.

### Webhook payload envelope

**Delivery webhooks are recipient-scoped, not message-scoped.** One recipient produces one webhook event carrying one status and one address. The payload never contains arrays of `to`/`cc`/`bcc`. A message sent to three recipients produces three separate `email.delivered` callbacks, each with its own `recipient_id` and its own outcome. This differs from the Events API, which returns stored events with mixed cardinality (message-scoped admission events plus per-recipient delivery transitions) — see [#Event schemas by surface](event-schemas-by-surface.md). In rare cases where a callback carries no durable recipient ID (for example, an ownership mismatch or a pre-recipient-ID legacy message), the webhook falls back to a message-scoped payload without `recipient_id`. Treat `recipient_id` as present in the normal case but do not crash on its absence.

Every webhook delivery is an HTTP `POST` with a JSON body in this shape:

```json
{
  "data": {
    "event_type": "email.delivered",
    "id": "f3a2c1d0-1234-4abc-9def-67890abcdef0",
    "occurred_at": "2026-07-06T18:24:00.000Z",
    "payload": {
      "id": "b0c7e8cb-6227-4c74-9f32-c7f80c30934b",
      "recipient_id": "7c1e9a44-2f60-4d1b-9a0e-3c7b5e8d1f22",
      "status": "delivered",
      "occurred_at": "2026-07-06T18:24:00.000Z",
      "from": { "email": "sender@example.com", "name": "Telnyx" },
      "to": { "email": "recipient@example.com", "name": null, "kind": "to" },
      "subject": "Welcome"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1
  }
}
```

| Field | Description |
| --- | --- |
| `data.event_type` | One of the 18 published webhook event types above (`email.sending` is accepted but never delivered). |
| `data.id` | Unique identifier for this event delivery. Recipient-scoped lifecycle events derive a stable per-recipient id, so each recipient’s callback has its own `data.id`. |
| `data.occurred_at` | ISO 8601 timestamp of when the event occurred. |
| `data.payload` | Recipient-scoped event data. See the field table below. |
| `data.record_type` | Always `"event"`. |
| `meta.attempt` | Delivery attempt number (starts at 1). |

#### Recipient lifecycle payload fields

| Field | Type | Description |
| --- | --- | --- |
| `id` | UUID | The email **message** id. Use this to correlate all recipients of one send, and to query the Events API. |
| `recipient_id` | UUID | The per-recipient row id. Unique per recipient per message — this is what makes each callback distinct. |
| `status` | string | The webhook event slug for this transition: `queued`, `scheduled`, `sent`, `delivered`, `deferred`, `bounced`, `failed`, `opened`, `clicked`, `unsubscribed`, `complained`, `received`, or `sandbox`. This is the event type name, not the authoritative recipient status — for `email.bounced` the status is always `bounced` even when the recipient row is `expired` or `failed`. Use `error_evidence.code` (the 30xxx taxonomy) to distinguish failure subtypes. The authoritative recipient status is available via `recipient_statuses` on the message or the recipient endpoints. |
| `occurred_at` | ISO 8601 | When this recipient’s transition occurred. |
| `from` | object | `{email, name}` of the sender. |
| `to` / `cc` / `bcc` | object | **Exactly one** of these keys is present, matching this recipient’s kind. The value is a single object `{email, name, kind}` — never an array. |
| `subject` | string | The message subject. |
| `error_evidence` | object (absent on success) | Normalized error contract. Present only on error statuses. See below. |
| `errors` | array (absent on success) | Array form of the same normalized error. Present only on error statuses. See below. |
| `smtp_code` | integer (absent on success) | Raw SMTP status from the remote MX, preserved additively for ops triage. |
| `smtp_response` | string (absent on success) | Raw SMTP response text, preserved additively. |

**BCC addresses are redacted.** A webhook for a BCC recipient carries a `bcc` key whose `email` is an HMAC-SHA256 sentinel of the form `redacted+sha256:<16-hex>@bcc.invalid`, with `name: null`. The sentinel is stable for the same address, so support tooling can correlate records without the plaintext address ever leaving Telnyx. You cannot recover the original BCC address from a webhook.

#### Error evidence on failure events

Error statuses (`bounced`, `failed`, `deferred`, `expired`, `suppressed`, `gw_reject`) carry a normalized error contract in **two equivalent shapes**. Prefer `error_evidence` for programmatic branching; `errors[]` mirrors the platform-wide Telnyx error array convention.

```json
{
  "error_evidence": {
    "code": "30001",
    "message": "550 5.1.1 <user@example.com>: Recipient address rejected",
    "enhanced_code": "5.1.1",
    "source": "smtp",
    "smtp_status": 550,
    "retryable": false
  },
  "errors": [
    {
      "code": "30001",
      "title": "Hard bounce",
      "detail": "550 5.1.1 <user@example.com>: Recipient address rejected",
      "source": "smtp",
      "smtp_status": 550,
      "enhanced_code": "5.1.1",
      "retryable": false
    }
  ]
}
```

| Field | Description |
| --- | --- |
| `code` | The **normalized 30xxx delivery error code** — never a raw SMTP status. See [Asynchronous delivery errors](/docs/messaging/email/error-codes#asynchronous-delivery-errors-30xxx) for the full taxonomy. |
| `message` (`detail` in `errors[]`) | The raw SMTP response text, when the failure reached SMTP. |
| `enhanced_code` | The DSN enhanced status code (e.g. `5.1.1`), when the remote supplied one. |
| `source` | Where the failure was observed: `smtp`, `mta`, or `api`. |
| `smtp_status` | The raw SMTP status as an integer, or `null` for failures that never reached SMTP (queue expiry, suppression, gateway rejection). |
| `retryable` | Whether resubmitting the same message could succeed. Only `30002` (Deferred) is retryable. |

**`bounce_category` is an internal classification field.** It does not appear in normal recipient-scoped webhook payloads and is not part of the public webhook contract. In the normal callback path it never reaches the stored event row (the correlation map does not include it). A legacy message-scoped fallback path may persist it in stored events, but the Events API sanitizer does not explicitly strip it. Do not build consumer logic that reads `bounce_category` from any public surface. Use `error_evidence.code` (the 30xxx taxonomy) to distinguish failure types programmatically — for example `30001` for a hard bounce versus `30005` for a queue expiry.

### Event schemas by surface

The three consumption surfaces do **not** share a schema. They differ in cardinality (one event per recipient for webhooks versus mixed cardinality for the Events API) and in field set. Do not write a single parser that assumes all three are interchangeable.

| Surface | Cardinality | Shape | Carries `error_evidence` |
| --- | --- | --- | --- |
| Recipient lifecycle webhook | One event **per recipient** per transition | `data.payload` with `recipient_id` and a single `to`/`cc`/`bcc` object | Yes, on error statuses |
| Events API (`GET /email_events`) | Mixed cardinality: message-scoped admission events and **per-recipient** delivery/engagement transitions | `{id, type, occurred_at, email_id, email, payload}` where `email` is a message summary with recipient **arrays**. Recipient transitions produce multiple rows per message even though the response does not expose `recipient_id`. | No — internal fields are stripped before the response |

The Events API strips observability-only and internal fields from the stored event payload before returning it. Fields you see in a webhook — including `error_evidence` — are not guaranteed to be present in the Events API response. Treat the webhook as the source of delivery-failure detail.

### Subscribe to events (webhook CRUD)

**Webhook configuration is owned by the email-domains service**, not the Email API. The `/email_domains/{domain_id}/webhooks` CRUD routes are served by the Telnyx email-domains service; the Email API only *resolves* a sending domain’s webhook list at publish time to decide where to fan out. Because the two services version independently, treat the email-domains API reference as authoritative for these routes’ request/response schemas and error codes. See [Domains & DKIM](domains-dkim.md) for domain setup.

Email webhooks live under the domains surface at `/email_domains/{domain_id}/webhooks`. A subscription requires a `url` and an `events` allowlist (at least one event type) — there is no default-to-all.

#### Create a webhook

```bash
curl -X POST https://api.telnyx.com/v2/email_domains/123e4567-e89b-12d3-a456-426614174000/webhooks \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ***" \
  -d '{
    "url": "https://example.com/webhooks/email",
    "events": ["email.sent", "email.delivered", "email.bounced"]
  }'
```

Response `201 Created`:

```json
{
  "data": {
    "id": "123e4567-e89b-12d3-a456-426614174003",
    "record_type": "email_webhook",
    "url": "https://example.com/webhooks/email",
    "events": ["email.sent", "email.delivered", "email.bounced"],
    "domain_id": "123e4567-e89b-12d3-a456-426614174000",
    "created_at": "2026-06-18T12:00:00Z",
    "updated_at": "2026-06-18T12:00:00Z"
  }
}
```

A domain can have multiple webhooks. Each event is delivered to every webhook on that domain whose `events` allowlist includes the event type — so you can route different event types to different endpoints by creating separate subscriptions.

#### List webhooks for a domain

```bash
curl https://api.telnyx.com/v2/email_domains/123e4567-e89b-12d3-a456-426614174000/webhooks \
  -H "Authorization: Bearer ***"
```

List responses use offset pagination (`page[number]`, `page[size]`) with a `meta` block of `{ page_number, page_size, total_pages, total_results }`.

#### Retrieve, update, and delete

| Operation | Method & path | Notes |
| --- | --- | --- |
| Retrieve one | `GET /email_domains/{domain_id}/webhooks/{id}` | Returns the full `EmailWebhook` object. |
| Update | `PATCH /email_domains/{domain_id}/webhooks/{id}` | `url` and/or `events` (optional; `domain_id` is not mutable). `events` must still have ≥1 item. |
| Delete | `DELETE /email_domains/{domain_id}/webhooks/{id}` | Returns `204 No Content`. |

All four operations return `404` if the domain or webhook is not found; create/update return `422` on validation failure.

### Event filtering per subscription

The `events` array on each webhook is an **allowlist** — Telnyx only delivers events whose type appears in that list to that webhook’s URL. To receive every event type, list all 18 published types (19 are accepted, but `email.sending` is never delivered). To receive only delivery confirmations and failures:

```json
{ "events": ["email.delivered", "email.bounced", "email.failed"] }
```

Filtering happens before delivery: an event whose type isn’t on the allowlist is never sent to that endpoint. You can update the allowlist at any time with `PATCH`.

### Signature verification

Telnyx signs every webhook delivery with **Ed25519 public-key cryptography** so you can verify that a request genuinely came from Telnyx. **This is strongly recommended for production.**

Each webhook request includes two headers:

| Header | Description |
| --- | --- |
| `telnyx-signature-ed25519` | Base64-encoded Ed25519 signature. |
| `telnyx-timestamp` | Unix timestamp of when the request was signed. |

The signature is computed over the string `{timestamp}|{raw_json_body}`. This is the standard Telnyx webhook signing scheme — email events are delivered by the same central delivery service that signs all Telnyx webhooks.

Outbound message events are published to RabbitMQ by the email API, `email.received` by the inbound pipeline, and domain lifecycle events by the email-domains service. Telnyx’s central **event_dispatcher** service signs payloads (Ed25519 / `TelnyxSigner`), performs HTTP delivery with retries, and tracks delivery status. The signing and retry logic is shared across all Telnyx webhook products — email uses the identical scheme as messaging webhooks.

#### Get your public key

Find your public key in the [Mission Control Portal](https://portal.telnyx.com/#/app/api-keys) under **Keys & Credentials → Public Key**.

#### Verification examples

**Node**

```javascript
import express from 'express';
import Telnyx from 'telnyx';

const app = express();
const telnyx = new Telnyx({ apiKey: process.env.TELNYX_API_KEY });

// Use express.raw to get the exact request body — the signature is
// computed over the raw JSON bytes, not a re-serialized object.
app.post('/webhooks', express.raw({ type: 'application/json' }), (req, res) => {
  const signature = req.headers['telnyx-signature-ed25519'];
  const timestamp = req.headers['telnyx-timestamp'];
  const payload = req.body.toString('utf8');

  try {
    const event = telnyx.webhooks.constructEvent(
      payload,
      signature,
      timestamp,
      process.env.TELNYX_PUBLIC_KEY
    );
    console.log('Verified email event:', event.data.event_type);
    res.sendStatus(200);
  } catch (err) {
    console.error('Signature verification failed:', err.message);
    res.sendStatus(403);
  }
});

app.listen(5000, () => console.log('Server running on port 5000'));
```

**Python**

```python
from flask import Flask, request
import telnyx

app = Flask(__name__)
telnyx.api_key = "YOUR_API_KEY"
telnyx.public_key = "YOUR_PUBLIC_KEY"

@app.route('/webhooks', methods=['POST'])
def webhooks():
    payload = request.data  # raw bytes
    signature = request.headers.get('telnyx-signature-ed25519')
    timestamp = request.headers.get('telnyx-timestamp')

    try:
        event = telnyx.Webhook.construct_event(payload, signature, timestamp)
        print(f"Verified email event: {event['data']['event_type']}")
        return '', 200
    except telnyx.error.SignatureVerificationError:
        return 'Invalid signature', 403
```

**Go**

```go
package main

import (
	"crypto/ed25519"
	"encoding/base64"
	"fmt"
	"io"
	"net/http"
	"os"
)

func verifySignature(payload, signature, timestamp string, publicKey ed25519.PublicKey) bool {
	signedPayload := timestamp + "|" + payload
	sigBytes, err := base64.StdEncoding.DecodeString(signature)
	if err != nil {
		return false
	}
	return ed25519.Verify(publicKey, []byte(signedPayload), sigBytes)
}

func webhookHandler(w http.ResponseWriter, r *http.Request) {
	body, _ := io.ReadAll(r.Body)
	signature := r.Header.Get("telnyx-signature-ed25519")
	timestamp := r.Header.Get("telnyx-timestamp")

	pubKeyBytes, _ := base64.StdEncoding.DecodeString(os.Getenv("TELNYX_PUBLIC_KEY"))
	publicKey := ed25519.PublicKey(pubKeyBytes)

	if !verifySignature(string(body), signature, timestamp, publicKey) {
		http.Error(w, "Invalid signature", http.StatusForbidden)
		return
	}

	fmt.Println("Webhook verified")
	w.WriteHeader(http.StatusOK)
}

func main() {
	http.HandleFunc("/webhooks", webhookHandler)
	http.ListenAndServe(":5000", nil)
}
```

**Verify the raw body.** The signature is computed over the exact bytes Telnyx sent. Re-serializing a parsed JSON object (e.g. `JSON.stringify(req.body)` after body-parser) can reorder keys and break verification. Read the raw request body, as shown above.

**Replay protection.** Reject webhooks where `telnyx-timestamp` is more than 5 minutes outside your server’s clock to prevent replay attacks.

### Delivery and retries

1. **An event occurs** — A message changes state or a recipient interacts, and Telnyx emits an event.
2. **Telnyx sends a POST** — The event_dispatcher service signs the payload and sends an HTTP `POST` to every webhook URL on the matching domain whose `events` allowlist includes the event type.
3. **Your server responds** — Return a `2xx` status code to acknowledge receipt.
4. **Retries on failure** — If your endpoint doesn’t return `2xx`, Telnyx retries the delivery. Delivery uses the standard Telnyx webhook retry behavior with backoff.

Retries, URL health checking, and delivery-status tracking are handled by the central event_dispatcher service shared across all Telnyx webhook products. Email webhooks inherit the same delivery guarantees as messaging webhooks.
