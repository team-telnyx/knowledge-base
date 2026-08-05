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

*Part 2 of 7 — see also: [Part 1](email-deliverability-domain-warm-up-and-domain-management--part-1.md), [Part 3](email-deliverability-domain-warm-up-and-domain-management--part-3.md), [Part 4](email-deliverability-domain-warm-up-and-domain-management--part-4.md), [Part 5](email-deliverability-domain-warm-up-and-domain-management--part-5.md), [Part 6](email-deliverability-domain-warm-up-and-domain-management--part-6.md), [Part 7](email-deliverability-domain-warm-up-and-domain-management--part-7.md)*

How mailbox providers evaluate mail, how to authenticate and warm up a sending domain with Telnyx, how to read delivery events and error codes, and how to register, verify, and manage email domains.

## Verify your sending domain

The single most important deliverability step is domain verification. Recipient providers (Gmail, Outlook, Yahoo) check SPF, DKIM, and DMARC records before accepting mail.

1. **Register your domain** via `POST /v2/email_domains`.
2. **Publish the DNS records** Telnyx generates for you — ownership (TXT) and DKIM (TXT on `<selector>._domainkey.<domain>`) are required — plus MX when `inbound_enabled` is true; SPF and DMARC are strongly recommended. Fetch the exact values from `GET /v2/email_domains/{domain_id}/dns_records` and publish them as-is.
3. **Verify** with `POST /v2/email_domains/{domain_id}/verify` after DNS propagates (usually 5–15 minutes; can take up to 48 hours).
4. **Use a shared domain** for a controlled onboarding test — it needs no DNS setup, but requires `onboarding@<shared-domain>` as the sender and the account owner's verified email address as every recipient.

Two separate background workers watch your DNS, on different schedules. Initial verification retries every **30 minutes** after registration, so a domain whose records propagate late will verify on its own without another API call. Once verified, a distinct **drift monitor** re-checks the published records every **6 hours** and transitions the domain to `degraded` if they stop matching. A record you delete or change after verification is therefore detected within hours, not immediately. You can always force an immediate check with `POST /v2/email_domains/{domain_id}/verify`.

Unverified domains cannot send. A send from an unverified domain returns `403` with error code `10007` and a domain-not-verified detail — verify the domain first.

### Custom vs shared domains

Telnyx provides two kinds of sending domains:

|  | Custom domain | Shared domain |
| --- | --- | --- |
| Owned by | Your account (BYOD) | Telnyx (system account) |
| DNS setup | Required — you publish the 5 records | None — Telnyx publishes them |
| Visible in `GET /email_domains` | Your domains only | Yes, visible to **all** accounts (`"type": "shared"`) |
| Readable by any account | No — only the owner | Yes |
| Mutable (PATCH/DELETE/verify) | Yes — by the owning account | No — read-only for non-owners |
| From address | Any local-part on your domain | `onboarding@<shared-domain>` only |
| Recipients | Any valid recipient (trial accounts: account owner's verified email only) | Account owner's verified email address only |

Shared domains are a restricted zero-setup onboarding resource: they're verified at provisioning time and need no DNS setup, but the `from` address must be `onboarding@<shared-domain>` and every recipient must match the account owner's verified email address. Use a custom domain for arbitrary recipients, your own `from` address, and control over sender authentication and domain reputation.

**Trial accounts** are restricted to the account owner's verified email address as the recipient regardless of domain type — registering and verifying a custom domain does not lift the restriction. Sends to any other recipient are rejected with `403` and code `10007`. Upgrade the account to send to arbitrary recipients.

Shared domains are **read-only** for accounts that don't own them. A `PATCH`, `DELETE`, or `POST …/verify` on a shared domain you don't own returns `403` with error code `10008`.

### DKIM signing

Telnyx attempts to DKIM-sign every outbound message using the key generated for your domain at registration time. DKIM signatures let receiving servers verify the message wasn't tampered with in transit.

**DKIM signing is best-effort for custom domains, not guaranteed.** The outbound MTA fails *open* for custom sending domains: if no key is available or the signing operation errors, the message is still sent — unsigned — rather than being rejected. A verified custom domain with a correctly published DKIM record signs reliably, but you should not assume every delivered message carried a valid DKIM signature.

The shared sending domain `mail.telnyx.com` **requires** successful DKIM signing. If signing fails for a shared-domain send, the message is rejected rather than sent unsigned. This does not affect custom domains.

Verify real-world signing with a seed test to a mailbox you control and inspect the received headers, or monitor DMARC aggregate reports.

- **Dynamic DKIM**: Telnyx generates a DKIM keypair automatically during domain registration. No manual key generation is needed.
- **Key rotation**: Keys are generated **at provisioning time**. There is no automatic rotation schedule and no customer-facing rotation endpoint in the current service. Key storage is append-only — creating a new key retires the previous one to a `retiring` state — but that path is operator-initiated, not scheduled. If a key is ever rotated, the DKIM DNS record's `value` changes and you must republish it; the drift monitor will transition the domain to `degraded` until the published record matches. See [Domains & DKIM](domains-dkim.md) for details.

### SPF

Publish the SPF record Telnyx generates exactly as specified:

```
yourdomain.com  TXT  "v=spf1 include:spf.telnyx.com ~all"
```

If you send through multiple providers, add the `include:spf.telnyx.com` directive to your existing SPF record rather than creating a second one — multiple SPF records invalidate each other.

### DMARC

DMARC tells receiving servers what to do when SPF and/or DKIM fail. DMARC is **advisory** — it is not required for verification — but publishing it is strongly recommended.

Telnyx generates a recommended DMARC record for your domain, and it is returned alongside your other records by `GET /v2/email_domains/{domain_id}/dns_records`. The service default is:

```
_dmarc.yourdomain.com  TXT  "v=DMARC1; p=none; rua=mailto:dmarc@telnyx.com"
```

The default aggregate-report address is `dmarc@telnyx.com`, which routes reports to Telnyx. Publish the generated value as-is if you want Telnyx to receive them. If you'd rather collect reports yourself, point `rua` at your own mailbox instead — for example `rua=mailto:dmarc@yourdomain.com`, or list both addresses comma-separated. Always publish the record returned by the API rather than hand-authoring one, so the policy tags stay aligned with what Telnyx expects.

- `p=none` is a monitoring-only policy — collect reports without affecting delivery.
- Move to `p=quarantine` or `p=reject` only after reports show alignment is high.
