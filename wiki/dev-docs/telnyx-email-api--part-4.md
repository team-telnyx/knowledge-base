---
title: Telnyx Email API
summary: The Telnyx Email API is a full email platform combining transactional sending,
  bi-directional inboxes, deliverability tooling, and event tracking on the same infrastructure
  that powers Telnyx's global messaging network. This page covers the API's capabilities,
  architecture, getting-started paths, inboxes, migration from other ESPs, and rate
  limits and quotas.
sources:
- url: https://developers.telnyx.com/docs/messaging/email/inboxes/index
- url: https://developers.telnyx.com/docs/messaging/email/migrate-to-telnyx
- url: https://developers.telnyx.com/docs/messaging/email/overview
- url: https://developers.telnyx.com/docs/messaging/email/quickstart
- url: https://developers.telnyx.com/docs/messaging/email/rate-limits
updated_at: 2026-08-05T13:51:25Z
---

# Telnyx Email API

*Part 4 of 5 — see also: [Part 1](telnyx-email-api--part-1.md), [Part 2](telnyx-email-api--part-2.md), [Part 3](telnyx-email-api--part-3.md), [Part 5](telnyx-email-api--part-5.md)*

The Telnyx Email API is a full email platform combining transactional sending, bi-directional inboxes, deliverability tooling, and event tracking on the same infrastructure that powers Telnyx's global messaging network. This page covers the API's capabilities, architecture, getting-started paths, inboxes, migration from other ESPs, and rate limits and quotas.

## Migrate to Telnyx Email

Move your email sending from an existing provider — SendGrid, Mailgun, Amazon SES, Postmark, or any other ESP — to Telnyx Email. This guide maps the concepts you already use to their Telnyx equivalents, then walks the migration end to end.

All requests use the production base URL `https://api.telnyx.com/v2` and an `Authorization` header with the Bearer authentication scheme.

### Concept mapping

Every ESP exposes the same core primitives under different names. Here's how they map to Telnyx:

| What you're doing | Typical ESP surface | Telnyx equivalent |
| --- | --- | --- |
| Authenticating | API key in a header (or SMTP credentials) | `Authorization: Bearer YOUR_API_KEY` on every request |
| Sending one email | `POST /mail/send`, `POST /messages`, `SendEmail` | `POST /v2/email_messages` |
| Sending many at once | Personalizations, recipient variables, bulk templated send | `POST /v2/email_messages/batch` (up to 50 messages per request) |
| Looking up a message | Message/activity lookup | `GET /v2/email_messages/{id}` |
| Storing reusable content | Dynamic/handlebars templates | `POST /v2/email_templates` + `template_id` / `template_variables` on send |
| Previewing a template | Template preview | `POST /v2/email_templates/{id}/render` |
| Receiving events | Event webhook / notification topic | Webhooks on `POST /v2/email_domains/{domain_id}/webhooks` |
| Polling events | Activity/messages/events API | `GET /v2/email_events` |
| Aggregate stats | Stats endpoint | `GET /v2/email_events/stats` |
| Suppression list | Bounces, blocks, spam reports, unsubscribes | `POST /v2/email_blocks` (plus CSV import at `POST /v2/email_blocks/import`) |
| Unsubscribe groups | ASM groups / subscription topics | `POST /v2/email_unsubscribe_groups` |
| Domain authentication | Domain auth / verified identity | `POST /v2/email_domains` + `GET /v2/email_domains/{domain_id}/dns_records` + `POST /v2/email_domains/{domain_id}/verify` |
| Scheduling | `send_at` / scheduled send | `scheduled_at` (preferred) or `send_at` on the send payload |

There is no `POST /v2/suppressions` endpoint on Telnyx. Suppressions live under **email blocks** — `POST /v2/email_blocks` for a single manual block, and `POST /v2/email_blocks/import` for a bulk CSV migration from your old provider. See [Suppressions & Unsubscribes](suppressions-unsubscribes.md).

### Event-type mapping

Telnyx publishes an event for each delivery-lifecycle transition. If you already handle ESP events, this is the mapping you need:

| What happened | Telnyx event type |
| --- | --- |
| Accepted by the API and queued | `email.queued` |
| Handed to the outbound MTA and accepted for delivery | `email.sent` |
| Accepted by the receiving server | `email.delivered` |
| Temporary failure — Telnyx will retry | `email.deferred` |
| Permanent failure (bounce, expiration, admin bounce, or out-of-band bounce) | `email.bounced` |
| Recipient reported the message as spam (ARF feedback) | `email.complained` |
| Sender-side failure after the message was accepted and persisted | `email.failed` |
| Recipient opened the message | `email.opened` |
| Recipient clicked a tracked link | `email.clicked` |
| Recipient unsubscribed | `email.unsubscribed` |

Several Telnyx behaviors differ from most ESPs and are worth handling explicitly:

- **`email.queued` and `email.sent` are separate stages.** `email.queued` fires when the API accepts and persists the message; `email.sent` fires later, when the message is successfully injected into the outbound MTA. Most ESPs don't split these. SendGrid, for example, has **no** event equivalent to `email.sent` — its earliest delivery event is `processed` ("accepted and can deliver the message"), which is closer to Telnyx's `email.queued` (acceptance) than to `email.sent` (MTA injection). Treat `email.queued` as acceptance only: a message can sit in `queued` and still fail before it is ever sent.
- **`email.failed` only applies to an accepted message.** A request that fails validation is rejected synchronously with `422` and never creates a message, so it produces **no** lifecycle webhook at all. Handle input errors from the HTTP response; use `email.failed` only for failures after acceptance.
- **`email.bounced` covers four underlying causes.** Hard bounces, retry expiration, administrative bounces, and out-of-band bounces all surface as `email.bounced`, distinguished by a `bounce_category` of `permanent`, `transient`, `admin`, or `oob`. If your current code branches on separate bounce and drop events, collapse that logic onto `email.bounced` + `bounce_category`.
- **`email.deferred` is not terminal.** A deferred message is still in flight and will retry. Don't treat it as a failure or trigger a resend.

If you're coming from SendGrid specifically, the event names map like this:

| SendGrid event | Telnyx event |
| --- | --- |
| `processed` | `email.queued` (approximate — both mean "accepted") |
| *(no equivalent)* | `email.sent` — fires on outbound MTA injection, a stage SendGrid does not report |
| `delivered` | `email.delivered` |
| `deferred` | `email.deferred` |
| `bounce`, `dropped` | `email.bounced` (check `bounce_category`) |
| `spamreport` | `email.complained` |
| `open` | `email.opened` |
| `click` | `email.clicked` |
| `unsubscribe`, `group_unsubscribe` | `email.unsubscribed` |

If your SendGrid integration keys off `processed` as "we sent it," note that the equivalent Telnyx signal is `email.queued`, not `email.sent`. Subscribe to `email.sent` as well if you want to know when the message actually reached the outbound MTA — SendGrid gives you no such event today.

Telnyx additionally has an `injection_timeout` recipient status for the ambiguous case where the MTA handoff timed out and Telnyx cannot yet tell whether the message was accepted. **Do not resend on this status** — retrying risks a duplicate. If the MTA did accept the message, a later callback reconciles the recipient from `injection_timeout` to `sent`.

The polling API (`GET /v2/email_events`) uses **bare** event names — `delivered`, `bounced`, `opened` — while webhook subscriptions use the `email.`-prefixed types above. Filter accordingly: `?event_type=delivered,bounced`.

### Migrating from SendGrid

SendGrid has the largest install base, so here it is in detail. Notes for Mailgun, SES, and Postmark follow each section.

**API concepts:**

| SendGrid | Telnyx |
| --- | --- |
| `POST /v3/mail/send` | `POST /v2/email_messages` |
| `personalizations[]` | One message per recipient group, batched via `POST /v2/email_messages/batch` |
| `content[{type, value}]` | `html_body` and `text_body` as separate top-level fields |
| `dynamic_template_data` | `template_variables` |
| Handlebars template syntax | Liquid template syntax |
| `POST /v3/templates` | `POST /v2/email_templates` |
| Event Webhook (account-wide) | Webhooks per domain — `POST /v2/email_domains/{domain_id}/webhooks` |
| `GET /v3/suppression/bounces` | `GET /v2/email_blocks` |
| ASM unsubscribe groups | `POST /v2/email_unsubscribe_groups` |
| Domain authentication | `POST /v2/email_domains` + `verify` |
| `send_at` (Unix timestamp) | `scheduled_at` (ISO 8601) |

**Sending a single email.** SendGrid nests recipients under `personalizations` and bodies under `content`. Telnyx flattens both:

SendGrid:

```bash
curl -X POST https://api.sendgrid.com/v3/mail/send \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ***" \
  -d '{
    "personalizations": [
      { "to": [{ "email": "recipient@example.com" }] }
    ],
    "from": { "email": "sender@example.com" },
    "subject": "Welcome",
    "content": [
      { "type": "text/plain", "value": "Welcome aboard." },
      { "type": "text/html", "value": "<h1>Welcome aboard.</h1>" }
    ]
  }'
```

Telnyx:

```bash
curl -X POST https://api.telnyx.com/v2/email_messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ***" \
  -d '{
    "from": { "email": "sender@example.com", "name": "Example" },
    "to": [{ "email": "recipient@example.com" }],
    "subject": "Welcome",
    "text_body": "Welcome aboard.",
    "html_body": "<h1>Welcome aboard.</h1>"
  }'
```

Key differences:

- `to`, `cc`, and `bcc` are top-level arrays. Each item is either a plain email string or an `{email, name}` object — both forms work.
- `from` accepts a plain string or `{email, name}`.
- Bodies are `html_body` and `text_body`, not a `content` array.
- A successful send returns **`202 Accepted`** with `"status": "queued"` — not `200`. Update any response-code assertions.
- `html_body`, `text_body`, `headers`, `tags`, and `metadata` are **write-only** — they are not echoed back in responses.

**Mailgun:** replace the multipart `from`/`to`/`html`/`text` form fields with the JSON payload above; `o:tag` becomes `tags`, and `v:my-var` custom variables become `metadata`.
**Amazon SES:** `Destination.ToAddresses` → `to`, `Message.Body.Html.Data` → `html_body`, `Message.Body.Text.Data` → `text_body`.
**Postmark:** `From`/`To`/`HtmlBody`/`TextBody` map almost one to one; lowercase the field names and wrap `to` in an array.

**Idempotent retries.** Telnyx supports optional idempotency on send via an `Idempotency-Key` HTTP header, so a retried request doesn't produce a duplicate email:

```bash
curl -X POST https://api.telnyx.com/v2/email_messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ***" \
  -H "Idempotency-Key: 8e03978e-40d5-43e8-bc93-6894a57f9326" \
  -d '{
    "from": "sender@example.com",
    "to": ["recipient@example.com"],
    "subject": "Order confirmation",
    "text_body": "Order #12345 confirmed."
  }'
```

- Generate a unique **UUID v4** per logical request and reuse it only when retrying that same operation with the same body.
- Keys are retained for **24 hours**, and **only successful responses are replayed**. A replayed response carries the `Idempotent-Replayed: true` header; the header is omitted for first-time requests and for error responses.
- Reusing a key with a **different** request body returns `422` with code `10027`.
- Sending the same key while the original request is **still processing** returns `409` with code `10036`.
- An empty, duplicate, malformed, or overlong key returns `400` with code `10015`.
- Idempotency is enforced at the Telnyx Edge and **fails closed** — if that protection is unavailable for a keyed request, you get `503` with code `10016`. Retry with the same key.

`idempotency_key` is **not** a request-body field. A body field by that name is ignored — only the `Idempotency-Key` HTTP header takes effect. A request sent **without** the header is not deduplicated, so an unkeyed retry after a timeout or a 5xx can produce a duplicate email.

Full details, including the batch behavior, are in [Send Email](send-email.md) and [Error Codes](error-codes.md).

**Batch sending.** SendGrid's `personalizations` array sends one request with many recipient blocks. Telnyx uses an explicit `messages` array where each item is a complete send payload:

SendGrid:

```bash
curl -X POST https://api.sendgrid.com/v3/mail/send \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ***" \
  -d '{
    "personalizations": [
      { "to": [{ "email": "one@example.com" }], "dynamic_template_data": { "first_name": "Ada" } },
      { "to": [{ "email": "two@example.com" }], "dynamic_template_data": { "first_name": "Grace" } }
    ],
    "from": { "email": "sender@example.com" },
    "template_id": "d-abc123"
  }'
```

Telnyx:

```bash
curl -X POST https://api.telnyx.com/v2/email_messages/batch \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ***" \
  -d '{
    "messages": [
      {
        "from": "sender@example.com",
        "to": ["one@example.com"],
        "template_id": "7a7c1a2b-1111-4c72-8c21-2bbf3d40c123",
        "template_variables": { "first_name": "Ada" }
      },
      {
        "from": "sender@example.com",
        "to": ["two@example.com"],
        "template_id": "7a7c1a2b-1111-4c72-8c21-2bbf3d40c123",
        "template_variables": { "first_name": "Grace" }
      }
    ]
  }'
```

- The batch limit is **50 messages per request**. An empty array or more than 50 items returns `400`. If you currently send 1,000-recipient personalization blocks, chunk them into groups of 50.
- **`207`** is always returned for batch responses. When all messages succeed, `errors` is empty. When one or more fail, the response carries a `data` array of successes and an `errors` array of failures.
- Batch item errors use a different shape from single-send errors: each entry has `index` (zero-based position in your request array), `code`, and `message` — note `message`, not `detail`. Match failures back to inputs by `index`.
- An `Idempotency-Key` header applies to the **whole batch request**, not to individual messages — there are no per-message keys inside `messages`. Reuse the key only when retrying the identical batch body. On a partial (`207`) result, do **not** replay the original batch: build a new request containing only the failed `index` entries, with a new key.

**Webhooks.** The biggest structural difference: SendGrid's Event Webhook is configured once per account, and Telnyx webhooks are **scoped to a sending domain**. If you send from three domains and want events from all three, create three subscriptions.

```bash
curl -X POST https://api.telnyx.com/v2/email_domains/{domain_id}/webhooks \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ***" \
  -d '{
    "url": "https://example.com/webhooks/email",
    "events": ["email.sent", "email.delivered", "email.bounced", "email.complained"]
  }'
```

- `events` is a required **allowlist** with at least one entry — there is no subscribe-to-everything default. Events whose type isn't listed are never delivered to that URL.
- Telnyx signs deliveries with **Ed25519**, not the HMAC scheme SendGrid uses. Verify the `telnyx-signature-ed25519` and `telnyx-timestamp` headers against the raw request body. Your existing SendGrid verification code will not carry over — see [Webhooks & Events](webhooks-events.md) for verified examples in Node, Python, and Go.
- SendGrid posts a JSON **array** of events per request. Telnyx posts a **single event** per request under `data`, with the event type at `data.event_type` and the message snapshot at `data.payload`.

If you don't have a public HTTPS endpoint, skip webhooks entirely and poll instead:

```bash
curl "https://api.telnyx.com/v2/email_events?page_size=50&event_type=delivered,bounced&from=2026-07-01T00:00:00Z" \
  -H "Authorization: Bearer ***"
```

Polling is cursor-based: read `meta.page_cursor` and pass it as `page_cursor` on the next request. The field is **omitted entirely** — not `null` — once you reach the end of the results.

**Templates.** SendGrid uses Handlebars (`{{name}}` with `{{#if}}` blocks); Telnyx uses **Liquid**. Simple variable interpolation looks identical, but conditionals, loops, and filters need rewriting.

SendGrid:

```bash
curl -X POST https://api.sendgrid.com/v3/templates \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ***" \
  -d '{
    "name": "Welcome",
    "generation": "dynamic"
  }'
```

Telnyx:

```bash
curl -X POST https://api.telnyx.com/v2/email_templates \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ***" \
  -d '{
    "name": "Welcome",
    "subject": "Welcome, {{first_name}}",
    "html_body": "<h1>Welcome, {{first_name}}!</h1>",
    "text_body": "Welcome, {{first_name}}!"
  }'
```

Telnyx creates the template and its content in **one** request — there's no separate template/version step. Fields are `name`, `subject`, `html_body`, `text_body`, and an optional `variables` array; when you omit `variables`, Telnyx extracts them from the subject and bodies automatically. Creation returns `201`.

Liquid syntax is validated at create time, so a malformed template fails immediately with `422` rather than at send time.

Preview a template without sending:

```bash
curl -X POST https://api.telnyx.com/v2/email_templates/{id}/render \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ***" \
  -d '{ "template_variables": { "first_name": "Ada" } }'
```

Then send with it by passing `template_id` and `template_variables`. When you use a template, `subject` on the send is optional — the template's subject renders instead.

Three different fields are easy to confuse when porting templates. They are not interchangeable:

| Field | Where it's used | Type | Behavior |
| --- | --- | --- | --- |
| `variables` | `POST /v2/email_templates` (create/update) | Array of variable **name** strings | Declares the names used by the template. Omit it and Telnyx extracts the names from the subject and bodies automatically. |
| `template_variables` | `POST /v2/email_templates/{id}/render` | Object of name → value | Supplies the values for a preview render. A missing or non-object value is treated as `{}`, so the template renders with empty substitutions rather than erroring. |
| `template_variables` | `POST /v2/email_messages` (send) | Object of name → value | Supplies the values for the actual send. **Must be an object.** A non-object value (string, array, number) is rejected with `422` — the send does not happen. Omitting the field entirely is fine; it defaults to `{}`. |

The render and send paths do **not** behave the same way for a malformed value. `POST /v2/email_templates/{id}/render` tolerates a non-object and previews with `{}`; `POST /v2/email_messages` **rejects** it with `422`. A mis-serialized value — for example sending `"{\"first_name\":\"Ada\"}"` as a JSON string rather than an object — will preview fine but fail at send time. Send an object, not a stringified object.

**Mailgun:** Mailgun templates also use Handlebars — the same rewrite to Liquid applies. **Postmark:** Mustachio templates map cleanly to Liquid for basic interpolation.

**Suppressions.** Migrate your existing list in bulk rather than replaying it address by address. `POST /v2/email_blocks/import` accepts a CSV and **auto-detects the provider from the header row** — SendGrid, Mailgun, and Amazon SES exports are recognized natively:

```bash
curl -X POST https://api.telnyx.com/v2/email_blocks/import \
  -H "Authorization: Bearer ***" \
  -F "file=@sendgrid_bounces.csv" \
  -F "block_ttl_days=30"
```

Export each SendGrid suppression list (bounces, blocks, spam reports, unsubscribes, invalid emails) and import them as-is. The importer maps SendGrid's `type` column onto the Telnyx reason taxonomy: `bounces` → `hard_bounce`, `spam_reports` → `spam_complaint`, `unsubscribes` → `unsubscribe`, `invalid_emails` → `invalid`, and `blocks` → `manual_block`.

The endpoint returns `202` with an async job; poll `GET /v2/email_blocks/import/{id}` until `status` is `completed` or `failed`. Limits: 25 MiB decoded and 250,000 rows.

Import your suppression list **before** your first production send. Sending to addresses that bounced or complained at your previous ESP is the fastest way to damage a new domain's reputation.

### Migration checklist

1. **Get a Telnyx API key.** Create a key in the [Mission Control Portal](https://portal.telnyx.com/#/app/api-keys) under **Auth → API Keys**. Send it as `Authorization: Bearer YOUR_API_KEY` on every request. If you plan to bypass overridable suppressions with `ignore_suppression`, the key needs the `email:override` scope (granted by `full_access` or `email:admin`).

2. **Register and verify your sending domain.**

   ```bash
   curl -X POST https://api.telnyx.com/v2/email_domains \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer ***" \
     -d '{ "domain": "example.com" }'
   ```

   Save the returned `id`, fetch the generated records with `GET /v2/email_domains/{domain_id}/dns_records`, publish them at your DNS provider, then trigger validation:

   ```bash
   curl -X POST https://api.telnyx.com/v2/email_domains/{domain_id}/verify \
     -H "Authorization: Bearer ***"
   ```

   Telnyx generates its own DKIM keypair, so you'll publish a **new** DKIM record alongside your existing ESP's. Both can coexist during the migration — keep the old records live until you've fully cut over. See [Email Domains & DKIM](email-domains-dkim.md).

3. **Import your suppression list.** Import your ESP's bounce, complaint, and unsubscribe exports via `POST /v2/email_blocks/import` before sending anything. If you use subscription groups, recreate them with `POST /v2/email_unsubscribe_groups` and add members with `POST /v2/email_unsubscribe_groups/{id}/suppressions`, then pass the matching `group_id` on sends.

4. **Send a test email.**

   ```bash
   curl -X POST https://api.telnyx.com/v2/email_messages \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer ***" \
     -d '{
       "from": "sender@example.com",
       "to": ["you@example.com"],
       "subject": "Migration test",
       "text_body": "Hello from Telnyx."
     }'
   ```

   Expect `202` with `"status": "queued"`. Save the `id` and confirm the timeline with `GET /v2/email_messages/{id}/events`.

5. **Set up event tracking.** Create a webhook per sending domain with an explicit `events` allowlist, and implement Ed25519 signature verification against the raw request body. Or skip webhooks and poll `GET /v2/email_events`. Use `GET /v2/email_events/stats` for the aggregate counts and rates that replace your ESP's stats dashboard.

6. **Port your templates.** Recreate each template with `POST /v2/email_templates`, rewriting Handlebars or Mustachio syntax to Liquid. Verify the output with `POST /v2/email_templates/{id}/render` before switching production traffic, then map your old template IDs to the new Telnyx UUIDs in your application config.

7. **Cut over batch sending.** Chunk any bulk sends into batches of 50 or fewer, switch to the `messages` array shape, and handle `207` partial-success responses by matching the `errors[].index` back to your input array.

8. **Warm up and ramp.** A new sending domain has no reputation history at the mailbox providers, even if your old one did. Ramp volume gradually rather than moving 100% of traffic on day one, and watch bounce and complaint rates via `GET /v2/email_events/stats`. See [Deliverability and Domain Warm-up](deliverability-and-domain-warm-up.md).

### Differences to plan for

| Behavior | What to expect on Telnyx |
| --- | --- |
| Success status code | `202 Accepted` on send, not `200`. |
| Batch size | Hard cap of 50 messages per `POST /v2/email_messages/batch` request. |
| Partial batch failure | `207` with per-item `errors[]` carrying `index`, `code`, and `message`. |
| Suppressed recipients | Never silently dropped — a `202` includes a top-level `suppressed[]` array; if *all* recipients are suppressed you get `422` with code `recipient_suppressed`. |
| Bounce granularity | One `email.bounced` type with a `bounce_category` discriminator. |
| Webhook scope | Per sending domain, not per account. |
| Webhook signing | Ed25519 over `{timestamp}|{raw_body}`, verified with your public key. |
| Template language | Liquid, not Handlebars or Mustachio. |
| Idempotency | Optional, via the `Idempotency-Key` HTTP header (enforced at Edge, 24-hour retention, successful responses replayed with `Idempotent-Replayed: true`). The body field `idempotency_key` is ignored. |
| Write-only fields | `html_body`, `text_body`, `headers`, `tags`, and `metadata` are not returned in responses. |
| Reputation enforcement | Sending is suspended with `429` and code `reputation_suspended` if the domain's reputation band falls to `poor`. |

Running both providers in parallel during cutover is the safest path: keep your old ESP's DNS records published, route a small percentage of traffic to Telnyx, compare delivery and bounce rates via `GET /v2/email_events/stats`, then ramp. Full endpoint details are in the [API reference](/api-reference), and error codes are catalogued in [Error Codes](error-codes.md).
