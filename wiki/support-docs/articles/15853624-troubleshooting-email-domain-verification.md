---
title: "Troubleshooting email domain verification"
summary: "If POST /v2/emaildomains/{domainid}/verify is not returning a verified status, the cause is almost always in the DNS records — either they have not finished propagating, or one of them does not exactly match what Telnyx expects."
sources:
- url: "https://support.telnyx.com/en/articles/15853624-troubleshooting-email-domain-verification"
updated_at: 2026-09-21T00:00:00Z
tags: [support-docs]
source_path: "support-docs/15853624-troubleshooting-email-domain-verification.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/15853624-troubleshooting-email-domain-verification.md -->

# Troubleshooting email domain verification

If `POST /v2/email_domains/{domain_id}/verify` is not returning a `verified` status, the cause is almost always in the DNS records — either they have not finished propagating, or one of them does not exactly match what Telnyx expects. This guide walks through the real, common causes in order, so you can find the one that applies to you.

**Start here every time:** run verify and read the per-record status in the response. The verify response tells you which records passed and which did not, so you can go straight to the one that needs fixing instead of guessing.

```
curl -X POST https://api.telnyx.com/v2/email_domains/{domain_id}/verify \
  -H "Authorization: Bearer YOUR_API_KEY"
```

---

## 1. A record was not added, or was added with a typo

The most common cause. A required ownership or DKIM record is missing, or its host or value contains a small mistake — an extra space, a missing character, or a transposed value. MX is also required when inbound email is enabled, but not for a send-only domain.

- Re-fetch the expected records with `GET /v2/email_domains/{domain_id}/dns_records`.
- Compare each expected **host** and **value** character-for-character against what is published at your DNS provider.
- Copy and paste values rather than typing them by hand — DKIM and ownership values are long and easy to mistype.

Even a single wrong character in a DKIM or ownership value will cause verification to fail, so this is always worth double-checking first.

---

## 2. DNS has not propagated yet

DNS changes are not instant. After you add or edit a record, it can take anywhere from a few minutes to a few hours (occasionally up to 24–48 hours, depending on your provider's TTL settings) before Telnyx can see it.

- If you just added the records, wait a bit and run verify again.
- You can check whether a record is visible publicly using any DNS lookup tool for the specific host Telnyx gave you.
- Lowering the record's TTL before you make changes can make future updates propagate faster, but this only helps going forward.

If a record looks correct and simply is not being seen yet, propagation delay is the likely reason — patience and a retry usually resolve it.

---

## 3. The DKIM value was truncated or split

DKIM values are long — often longer than a single DNS TXT string allows. Some registrar interfaces silently cut off a long value, or split it into multiple quoted chunks and then reassemble it incorrectly.

- Confirm the entire DKIM value was saved. Compare the length of what is published against the value from Telnyx.
- If your provider requires long TXT records to be split into 255-character chunks, make sure the chunks are entered in order with no extra spaces or characters between them.
- Do not add line breaks in the middle of the value.

A DKIM record that is even slightly truncated will not validate, so this is the first thing to check when the ownership record and any applicable MX record pass but DKIM does not.

---

## 4. The host is wrong (double-domain concatenation)

Different DNS providers expect the host field in different formats, and mixing them up produces an invalid host. The classic mistake is the domain appearing twice:

|  |  |
| --- | --- |
| **What got published (wrong)** | **What it should be** |
| `telnyx1._domainkey.mail.yourcompany.com.yourcompany.com` | `telnyx1._domainkey.mail.yourcompany.com` |

This happens when a provider automatically appends your domain to whatever you type, but you entered the full host anyway. To fix it:

- If your provider appends the domain for you (common with GoDaddy and Namecheap), enter only the part **before** your domain — for example `telnyx1._domainkey.mail`.
- If your provider expects the full host, enter it exactly as Telnyx shows it.
- After saving, look up the record to confirm the final host is exactly what Telnyx expects, with no duplicated domain.

---

## 5. SPF include conflicts

SPF is designed so a domain has **one** SPF record. If you already send mail through another provider, you may already have an SPF record — and adding a second one, or leaving two in place, breaks SPF entirely.

- Check whether your domain already has a TXT record starting with `v=spf1`.
- If it does, do not add a second one. Instead, merge the Telnyx mechanism `include:spf.telnyx.com` into your existing SPF record alongside your other senders.
- Keep the record to a single `v=spf1 ... all` statement with all your `include:` mechanisms in it.
- Watch the SPF lookup limit: SPF allows at most 10 DNS lookups. Too many `include:` entries can cause SPF to fail even when each one is valid.

For example, an existing Google Workspace SPF record could become `v=spf1 include:_spf.google.com include:spf.telnyx.com ~all`. SPF is recommended rather than strictly required for verification, but getting it wrong hurts deliverability, so it is worth fixing properly.

---

## 6. A previously-verified domain stopped working (drift)

Verification is not permanent. If a previously verified domain has required DNS drift, Telnyx can mark it degraded. Sends then fail with public error code `10007` and the detail `Domain is in a degraded state.` The service uses `domain_degraded` internally, but that is not the public error code. Telnyx periodically re-checks verified domains.

Common triggers:

- A required ownership or DKIM record was edited, removed, or overwritten — sometimes by a migration to a new DNS provider or a bulk change.
- The MX record changed while inbound email was enabled for the domain.
- A DNS provider change reset records to defaults.

To recover, re-fetch the expected records with `GET /v2/email_domains/{domain_id}/dns_records`. Restore required ownership and DKIM records and, when inbound email is enabled, MX. Wait for propagation, then run verify again. Once the required records match, the domain returns to `verified` and sending resumes. Repair SPF or DMARC problems for deliverability, but changes to those optional records alone do not degrade the domain or block sending.

---

## Quick checklist

- Run verify and read the per-record status first.
- Re-fetch expected records and compare host and value exactly.
- Give DNS time to propagate, then retry.
- Confirm the DKIM value was saved in full, not truncated.
- Make sure no host has the domain duplicated.
- Keep a single, merged SPF record.
- For a domain that used to work, restore changed ownership and DKIM records, plus MX when inbound email is enabled; repair SPF and DMARC separately for deliverability.

---

## After a DKIM rotation

Rotation replaces the TXT value at the existing fixed-selector host and immediately switches the signing key. Compare the new DKIM record returned by the rotation endpoint (or `GET /v2/email_domains/{domain_id}/dns_records`) with live DNS. Replace the old TXT value rather than adding a second selector.

DKIM verification returns to `pending` until the replacement is verified. Resolvers holding the old TXT value can temporarily fail to verify signatures made by the new key; there is no dual-signing overlap. Wait for propagation and run verification again. Signing failures are fail-closed, so do not expect unsigned fallback. Follow the [DKIM rotation steps](https://support.telnyx.com/en/articles/15853623-setting-up-your-email-sending-domain) to check the cutover.

---

Related Articles

- [Getting started with Telnyx Email](https://support.telnyx.com/en/articles/15853622-getting-started-with-telnyx-email)
- [Setting up your email sending domain](https://support.telnyx.com/en/articles/15853623-setting-up-your-email-sending-domain)
- [Why didn't my email arrive?](https://support.telnyx.com/en/articles/15853625-why-didn-t-my-email-arrive)
- [Setting up and troubleshooting Telnyx Email webhooks](https://support.telnyx.com/en/articles/16099889-setting-up-and-troubleshooting-telnyx-email-webhooks)
