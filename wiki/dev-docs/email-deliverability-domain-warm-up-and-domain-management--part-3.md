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

*Part 3 of 7 — see also: [Part 1](email-deliverability-domain-warm-up-and-domain-management--part-1.md), [Part 2](email-deliverability-domain-warm-up-and-domain-management--part-2.md), [Part 4](email-deliverability-domain-warm-up-and-domain-management--part-4.md), [Part 5](email-deliverability-domain-warm-up-and-domain-management--part-5.md), [Part 6](email-deliverability-domain-warm-up-and-domain-management--part-6.md), [Part 7](email-deliverability-domain-warm-up-and-domain-management--part-7.md)*

How mailbox providers evaluate mail, how to authenticate and warm up a sending domain with Telnyx, how to read delivery events and error codes, and how to register, verify, and manage email domains.

## Register and manage a domain

Register a custom sending domain with `POST /email_domains`. Only `domain` is required; the optional fields configure inbound routing, your DMARC policy, and tracking:

```
curl -X POST https://api.telnyx.com/v2/email_domains \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ***" \
  -d '{
    "domain": "example.com",
    "inbound_enabled": false,
    "dmarc_policy": { "p": "none", "rua": "mailto:dmarc@telnyx.com" },
    "tracking": {
      "open_tracking": true,
      "click_tracking": true,
      "unsubscribe_tracking": true
    }
  }'
```

| Field | Type | Default | Notes |
| --- | --- | --- | --- |
| `domain` | string | — | Required. Must be a domain you control; public email providers, disposable domains, IP addresses, and single-label hostnames are rejected. |
| `inbound_enabled` | boolean | `false` | Enable inbound routing. When `true`, the MX record becomes required for verification. |
| `dmarc_policy` | object | null | Your DMARC policy. Omit or `null` for the advisory default. |
| `tracking` | object | see below | Open, click, and unsubscribe tracking toggles. Stored on the account's sending profile. |

A new domain starts with `status: "pending"` and `usable_for_sending: false`. Telnyx generates a DKIM key and the five DNS records at create time, and a background verification worker runs shortly after — but you'll still need to publish the records first.

The effective tracking defaults for a new domain are `open_tracking: false`, `click_tracking: false`, and `unsubscribe_tracking: true`. Open and click tracking are opt-in; one-click unsubscribe (RFC 8058) is on by default because Gmail and Yahoo bulk-sender rules require it.

**Tracking is scoped to the sending profile, not to the domain.** Tracking settings are stored on your account's default sending profile, which every domain on the account shares. Supplying `tracking` at registration therefore only succeeds for the **first** domain on an account — once a default profile exists, `POST /email_domains` with `tracking` is rejected with a validation error telling you to use `PATCH /email_domains/{id}` instead.

### DNS records

Every domain gets five DNS records. Fetch them with `GET /email_domains/{domain_id}/dns_records` and publish them at your DNS provider:

```
curl https://api.telnyx.com/v2/email_domains/{domain_id}/dns_records \
  -H "Authorization: Bearer ***"
```

Each record in the response has `host`, `value` (what to publish), `actual_value` (what Telnyx last observed in DNS), `record_type`, `priority`, `required`, and `status`.

| # | Purpose | Type | Host | Value | Priority | Required |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Ownership | TXT | `<domain>` | `telnyx-domain-verification=<domain_id>` | — | ✅ yes |
| 2 | SPF | TXT | `<domain>` | `v=spf1 include:spf.telnyx.com ~all` | — | recommended |
| 3 | DKIM | TXT | `<selector>._domainkey.<domain>` | `v=DKIM1; k=rsa; p=<base64 public key>` | — | ✅ yes |
| 4 | MX | MX | `<domain>` | `mx.telnyx.com` | 10 | when inbound enabled |
| 5 | DMARC | TXT | `_dmarc.<domain>` | `v=DMARC1; p=none; rua=mailto:dmarc@telnyx.com` | — | recommended |

The required records are **ownership** and **DKIM** — plus **MX** when `inbound_enabled` is true (`mx` shows `not_required` when inbound is off). **SPF** and **DMARC** are recommended (marked `required: false`) but strongly advised for deliverability — omitting them won't block verification, but recipient providers will treat your mail less favorably.

**What each record does:**

- **Ownership** — proves you control the domain. The value contains the domain's `id`.
- **SPF** — authorizes Telnyx's mail servers to send on your domain's behalf. If you send through multiple providers, add the `include:spf.telnyx.com` directive to your existing SPF record rather than creating a second one (multiple SPF records invalidate each other).
- **DKIM** — publishes the public key that corresponds to Telnyx's DKIM signing key. The host uses the DKIM selector (default `telnyx1`).
- **MX** — directs inbound mail to Telnyx. Required only when `inbound_enabled` is `true`; shows `not_required` in the health check when inbound is off.
- **DMARC** — the advisory default is `p=none` (monitor only) with aggregate reports sent to `mailto:dmarc@telnyx.com`. You can publish a stronger policy (`p=quarantine` or `p=reject`) — Telnyx verifies any valid `v=DMARC1` record, not just its own recommended value.

### Verify and the status lifecycle

Once you've published the DNS records, trigger verification:

```
curl -X POST https://api.telnyx.com/v2/email_domains/{domain_id}/verify \
  -H "Authorization: Bearer ***"
```

The response returns the updated domain. A `200` does not by itself mean success — the same `200` can report `verified`, `pending` (records not yet observed), or `failed` (a required record is missing or wrong). Only `"status": "verified"` means all required records passed and the domain is usable for sending.

A domain's `status` field can be one of:

| Status | Meaning | Can send? | Can receive (inbound)? |
| --- | --- | --- | --- |
| `pending` | Records not yet verified (or some still propagating). | No | No |
| `verified` | All required records pass; DKIM signing material is available. | Yes | Yes, if `inbound_enabled` and MX verified |
| `failed` | A required record (ownership or DKIM — and MX if inbound-enabled) is missing or wrong. | No | No |
| `degraded` | Was verified, but a required record has since failed. | No | Only if `usable_for_inbound` remains `true` |
| `suspended` | Blocked by Telnyx (e.g. for policy or abuse reasons). Admin-only — no public API sets this. | No | No |

`verifying` is a reserved value in the status enum but is never assigned by any production code path. Verification is synchronous: `POST /verify` returns the domain already resolved to `verified`, `failed`, or `pending`. Don't write client logic that waits for `verifying`.

**`degraded` is a soft failure.** A degraded domain was once verified but a **required** record has since failed — Telnyx's drift monitor re-checks verified domains periodically and transitions them to `degraded` when a previously-passing required record now fails. Only ownership and DKIM (plus MX when inbound is enabled) are marked required, so only those can degrade a domain; drift on the optional SPF or DMARC records is a deliverability warning that does not by itself affect sendability. A degraded domain **cannot send**. It can receive inbound mail only when inbound is enabled and the response still reports `usable_for_inbound: true`. Fix the DNS records and re-verify to return to `verified`.

The drift monitor only re-checks domains in `verified` or `degraded` status. When a degraded domain's records recover, it's automatically transitioned back to `verified`. The lifecycle events `email_domain.verified`, `email_domain.degraded`, and `email_domain.suspended` are emitted to configured webhooks on each transition.

### Domain health

For a compact, health-focused view, use `GET /email_domains/{id}/health`:

```
curl https://api.telnyx.com/v2/email_domains/{id}/health \
  -H "Authorization: Bearer ***"
```

```
{
  "data": {
    "id": "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
    "record_type": "email_domain_health",
    "status": "verified",
    "usable_for_sending": true,
    "usable_for_inbound": false,
    "verification": {
      "ownership": "verified",
      "spf": "verified",
      "dkim": "verified",
      "dmarc": "missing_optional",
      "mx": "not_required"
    },
    "checked_at": "2026-05-31T12:00:00Z"
  }
}
```

The `verification` object shows the per-record status: `verified`, `failed`, `pending`, `not_required` (e.g. MX when inbound is off), or `missing_optional` (SPF/DMARC when the optional record is absent).

Use `GET /health` for dashboards and monitoring — it's lighter than the full domain object (no nested `dns_records` or `dkim` detail). Use `GET /email_domains/{id}` when you need the actual DNS record values to publish or the DKIM selector.

### DKIM

DKIM (DomainKeys Identified Mail) lets receivers verify that a message wasn't altered after it was sent. Telnyx signs every outgoing message with the domain's active DKIM private key; the recipient looks up the corresponding public key in your DNS at `<selector>._domainkey.<domain>`.

- **Algorithm:** `rsa-sha256`
- **Key length:** 2048-bit RSA
- **Selector:** `telnyx1` (the default; appears in the DKIM record's host)
- **DNS record value:** `v=DKIM1; k=rsa; p=<base64-encoded DER public key>`

The active key is reflected on the domain object in `dkim`:

```
"dkim": {
  "selector": "telnyx1",
  "algorithm": "rsa-sha256",
  "key_length": 2048,
  "active": true,
  "rotated_at": null
}
```

**Key management:** DKIM keys are generated and managed **server-side by Telnyx**. A 2048-bit RSA key pair is created when you register the domain, the private key never leaves Telnyx, and the matching public key is published in the DKIM DNS record you copy to your provider. There is no customer-facing key rotation endpoint — the public API exposes no route to rotate, revoke, or replace a DKIM key. The `dkim.rotated_at` field reflects the active key's revocation timestamp and is `null` for a normal active key. If you need a key replaced, contact Telnyx support.

### Domain settings

Update mutable settings with `PATCH /email_domains/{id}`:

```
curl -X PATCH https://api.telnyx.com/v2/email_domains/{domain_id} \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ***" \
  -d '{
    "inbound_enabled": true,
    "dmarc_policy": { "p": "reject", "rua": "mailto:dmarc@example.com" },
    "tracking": {
      "open_tracking": false,
      "unsubscribe_tracking": true
    }
  }'
```

| Field | Notes |
| --- | --- |
| `inbound_enabled` | Toggles inbound routing. Enabling it makes the MX record required for verification. |
| `dmarc_policy` | Updates the recommended `_dmarc` TXT record value and resets its verification to `pending` — republish the record and re-verify. Omit/`null` for the advisory default. |
| `tracking` | Open, click, and unsubscribe tracking. Explicit values — including `false` — always override the defaults. **Scoped to the sending profile:** the setting is stored on the account's default profile, so a change made through one domain applies to every domain sharing that profile. |

The `domain` itself, `status`, `account_id`, and `profile_id` are not settable via `PATCH`. Reputation fields are also rejected on the public API — they're computed internally.

**Delete a domain:**

```
curl -X DELETE "https://api.telnyx.com/v2/email_domains/{domain_id}?force=true" \
  -H "Authorization: Bearer ***"
```

Verified or degraded domains require `force=true`; pending or failed domains can be deleted without it. A `suspended` domain can be deleted without `force`. A successful deletion returns `204 No Content`; no domain body is returned. Deleting a shared domain you don't own returns `403` (code `10008`).

### Reputation

Each domain response includes a `reputation` object computed by Telnyx from your sending behavior:

```
"reputation": {
  "band": "good",
  "breakdown": {},
  "computed_at": "2026-07-05T00:00:00Z"
}
```

| Field | Description |
| --- | --- |
| `band` | Reputation band — e.g. `excellent`, `good`, `warn`, `poor`, or `insufficient_data` (for senders below the volume floor). |
| `breakdown` | Component scores contributing to the band. |
| `computed_at` | When the reputation was last calculated. `null` if not yet computed. |

Reputation is read-only on the public API — it's updated internally via a daily computation job, not via `PATCH`. A domain in the `poor` band will have sending suspended with a `reputation_suspended` (429) error.
