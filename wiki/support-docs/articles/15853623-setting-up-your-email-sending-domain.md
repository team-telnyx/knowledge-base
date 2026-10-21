---
title: "Setting up your email sending domain"
summary: "Before Telnyx can send email for you, you need to prove you own the domain you send from and configure it so inbox providers trust your mail. You do that by adding a few DNS records."
sources:
- url: "https://support.telnyx.com/en/articles/15853623-setting-up-your-email-sending-domain"
updated_at: 2026-09-21T00:00:00Z
tags: [support-docs]
source_path: "support-docs/15853623-setting-up-your-email-sending-domain.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/15853623-setting-up-your-email-sending-domain.md -->

# Setting up your email sending domain

Before Telnyx can send email for you, you need to prove you own the domain you send from and configure it so inbox providers trust your mail. You do that by adding a few DNS records. This guide shows you how to add a sending domain, fetch its records, publish them at your DNS provider, verify the domain, and understand what each record does.

**Email is currently managed through the Telnyx API**, so this guide uses `curl`. You will also need access to your DNS provider (usually your domain registrar or web host) to add records.

---

## Step 1: Add your domain

Most senders use a subdomain such as `mail.yourcompany.com` rather than the root domain. A subdomain keeps your sending reputation separate from your regular corporate mail and is the recommended approach. Add it:

```
curl -X POST https://api.telnyx.com/v2/email_domains \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": "mail.yourcompany.com"}'
```

The response contains the domain `id` and a `status` of `pending`. Note the `id` — you use it in the next steps.

---

## Step 2: Fetch your DNS records

Ask Telnyx for the records to publish:

```
curl https://api.telnyx.com/v2/email_domains/{domain_id}/dns_records \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Each record in the response has three things you care about:

- **Host** (also called name or record name) — where the record goes, for example `mail.yourcompany.com` or `telnyx1._domainkey.mail.yourcompany.com`.
- **Value** — the exact content to paste in.
- **Required** — whether the record is mandatory for verification.

You will receive several record types. For a send-only domain, ownership and DKIM are required for verification. MX is required only when inbound email is enabled for the domain. SPF and DMARC are optional but strongly recommended for good deliverability. Check the per-record results from the verify response to see which requirements apply.

---

## Step 3: Add the records at your DNS provider

Sign in to wherever your domain's DNS is managed and add each record exactly as Telnyx provided it. The general process is the same everywhere:

- Choose the record **type** (TXT or MX) shown by Telnyx.
- Paste the **host** into the name field.
- Paste the **value** into the value/content field.
- For MX records, set the **priority** if your provider asks for one.
- Save.

**Notes for common providers:**

|  |  |
| --- | --- |
| **Provider** | **What to watch for** |
| **GoDaddy** | Enter only the subdomain part in the Host field (for example `mail`, not the full `mail.yourcompany.com`). GoDaddy appends your domain automatically. |
| **Cloudflare** | Set TXT and MX records to **DNS only** (grey cloud), not proxied. Proxying does not apply to mail records. |
| **Namecheap** | Use the Advanced DNS tab. Enter the host without the domain suffix, and use `@` for the root. |
| **Route 53 / Google Domains** | Enter the fully-qualified host. If the console splits long TXT values into quoted chunks, that is fine — just do not add extra spaces. |

**The single most common mistake** is adding the domain twice, which produces a host like `mail.yourcompany.com.yourcompany.com`. Some providers want just the subdomain (`mail`) and add the rest for you; others want the full host. When in doubt, add the record and then look up what actually got published before verifying.

---

## Step 4: Verify your domain

Once the records are saved, ask Telnyx to check them:

```
curl -X POST https://api.telnyx.com/v2/email_domains/{domain_id}/verify \
  -H "Authorization: Bearer YOUR_API_KEY"
```

If everything matches, the domain `status` becomes `verified` and you can send. If it does not pass yet, the response shows the status of each individual record so you can see which one still needs attention. DNS changes are not instant — if a record was just added, wait a little and run verify again. See **Troubleshooting email domain verification** if it keeps failing.

---

## What each record does

You do not need to be a DNS expert, but a little context helps you set things up correctly and troubleshoot later.

|  |  |  |
| --- | --- | --- |
| **Record** | **Type** | **What it does** |
| **Ownership** | TXT | A unique verification string that proves to Telnyx you control the domain. Required. |
| **SPF** | TXT | Sender Policy Framework. Lists which servers are allowed to send mail for your domain, so receivers can reject forgeries. Recommended. |
| **DKIM** | TXT | DomainKeys Identified Mail. Publishes a public key so receivers can confirm each message was cryptographically signed by you and not altered in transit. Required. |
| **DMARC** | TXT | Tells receivers what to do with mail that fails SPF or DKIM, and where to send reports. Increasingly expected by Gmail and Yahoo. Recommended. |
| **MX** | MX | Mail Exchange. Routes inbound mail to Telnyx when inbound email is enabled. Required only for an inbound-enabled domain; it is not required for a send-only domain. |

Together, SPF, DKIM, and DMARC are how modern inbox providers decide whether to trust your mail. Publishing all of them — and keeping them in place — is the single biggest thing you can do for deliverability.

---

## Rotate your DKIM key

Rotate an account-owned custom domain with:

```sh
curl -X POST "https://api.telnyx.com/v2/email_domains/{domain_id}/rotate_dkim" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

A successful rotation returns `201` with the new DKIM key information and replacement `dns_records`. Shared domains are Telnyx-managed and return `403`; a concurrent rotation conflict returns retryable `409`.

**Be ready to update DNS immediately.** Rotation immediately switches signing to the new key, retires the previous signing key, and resets DKIM verification to `pending`. It uses the same fixed selector: replace the existing DKIM TXT value with the returned value at the same host. There is no dual-signing selector overlap; `old_selector_retained` is `false`. Cached old TXT values can cause temporary DKIM failures during propagation.

After replacing the TXT value, check public DNS against the returned record and run `POST /v2/email_domains/{domain_id}/verify` again. Telnyx publishes `email_domain.dkim_rotated` for subscribed webhooks. See [Troubleshooting email domain verification](https://support.telnyx.com/en/articles/15853624-troubleshooting-email-domain-verification) if verification stays pending.

DKIM signing failures are fail-closed for shared and custom domains over both HTTP and SMTP: sending does not fall back to unsigned mail.

---

## Keep your records in place

Verification is not a one-time event. Telnyx periodically checks required DNS records. If ownership or DKIM later stops matching — or MX stops matching while inbound email is enabled — the domain can become degraded, and sending is rejected until the required records are restored. SPF or DMARC drift does not degrade the domain or block sending, although incorrect optional records can hurt deliverability. If a domain that used to work suddenly stops, check its required records first.

---

Related Articles

- [Getting started with Telnyx Email](https://support.telnyx.com/en/articles/15853622-getting-started-with-telnyx-email)
- [Troubleshooting email domain verification](https://support.telnyx.com/en/articles/15853624-troubleshooting-email-domain-verification)
- [Why didn't my email arrive?](https://support.telnyx.com/en/articles/15853625-why-didn-t-my-email-arrive)
