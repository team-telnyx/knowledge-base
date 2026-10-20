---
title: "Why didn't my email arrive?"
summary: "An email that did not arrive almost always leaves a trail. Telnyx records request progress separately from each recipient's delivery outcome, so the fastest way to troubleshoot is to inspect both the message and its events."
sources:
- url: "https://support.telnyx.com/en/articles/15853625-why-didn-t-my-email-arrive"
updated_at: 2026-09-21T00:00:00Z
tags: [support-docs]
source_path: "support-docs/15853625-why-didn-t-my-email-arrive.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/15853625-why-didn-t-my-email-arrive.md -->

# Why didn't my email arrive?

An email that did not arrive almost always leaves a trail. Telnyx records request progress separately from each recipient's delivery outcome, so the fastest way to troubleshoot is to inspect both the message and its events.

**Email is currently managed through the Telnyx API**, so the checks below use `curl`.

---

## **Step 1: Check the message and recipient events**

Start with the parent message. If you saved the message `id` returned when you sent it, look it up:

```
curl https://api.telnyx.com/v2/email_messages/{message_id} \
  -H "Authorization: Bearer YOUR_API_KEY"
```

The parent message `status` describes request processing, not delivery to every recipient. Its lifecycle is `scheduled`, `queued`, `processing`, `completed`, `cancelled`, or `sandbox`. A parent status of `completed` means processing finished; it does not mean every recipient's mailbox provider accepted the message.

Next, request the recipient-scoped event history:

```
curl "https://api.telnyx.com/v2/email_messages/{message_id}/events?page_size=25" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

The default event page contains up to 25 records. If the response includes `meta.page_cursor`, request the next page and repeat until no cursor is returned:

```
curl "https://api.telnyx.com/v2/email_messages/{message_id}/events?page_size=25&page_cursor={page_cursor}" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Interpret recipient events and statuses independently from the parent message:

|  |  |
| --- | --- |
| **You see...** | **It means** |
| `queued` / `sending` | Telnyx is still processing or injecting that recipient. Check again shortly. |
| `sent` | The Telnyx MTA accepted the recipient into its delivery queue. This is not confirmation that the remote mailbox provider accepted it. |
| `delivered` | The remote recipient mail server accepted the message. This does not guarantee inbox placement; it may still be filtered into spam or junk. |
| `deferred` | The remote server returned a temporary failure. Telnyx may retry while the message remains in the queue. |
| `bounced`, `expired`, or `failed` | Delivery ended without remote acceptance. Read the event detail to distinguish a recipient rejection, queue expiration, or system failure. |

For a single send, inspect the `202` acceptance response or the immediate `errors` array. For a batch, inspect its `207` per-item results; see [Sending email in batches: limits, results, and safe retries](https://support.telnyx.com/en/articles/16823821-sending-email-in-batches-limits-results-and-safe-retries). Email sends allow up to **1 MB for `html_body` plus `text_body`** and **25 MB total** for the body plus attachments. Attachment sizes are counted after base64 decoding. Exceeding either Email API limit returns `422`.

---

## **Step 2: Understand bounces, deferrals, and queue expiry**

A remote mail server may reject a message permanently or temporarily:

|  |  |
| --- | --- |
| **Outcome** | **What it means and what to do** |
| **Permanent bounce** | The remote server returned a permanent failure, such as a nonexistent mailbox. Do not retry without correcting the address or cause. |
| **Temporary deferral** | The server is temporarily unavailable, the mailbox is full, or the message was greylisted. Telnyx may retry. Repeated temporary failures can eventually be escalated into a suppression. |
| **Queue expiry** | Telnyx exhausted the delivery window after retries. Delivery ended without remote acceptance. |

Do not interpret a suppression reason of `hard_bounce` as proof of one permanent SMTP rejection. Telnyx also uses that suppression reason when a queue expires and when repeated soft bounces reach the escalation threshold. Use the delivery event detail to identify the original outcome.

---

## **Distinguish pre-queue failures**

Event polling and webhooks expose `canonical_event_type` alongside the compatibility `event_type`. Gateway rejection is `email.gw_reject` under `email.failed`; queue expiry is `email.expired` under `email.bounced`; an ambiguous timeout is `email.injection_timeout`. Read the canonical field and `error_evidence` rather than inferring the outcome from a generic name.

A refusal before the MTA accepts a recipient is classified using its structured refusal, origin, and reason. Retryable platform/configuration/transport refusals use a durable background retry worker rather than immediately becoming terminal `gw_reject`. Permanent recipient-policy refusals remain terminal. Exhausting the platform retry budget produces a stable terminal failure with bounded error evidence.

Do not retry every `email.failed` blindly. Record the message, recipient, and event IDs, inspect the canonical outcome and evidence, and resolve the cause before sending again. For the separate scheduled queue-publication exhaustion case, see [Scheduling and cancelling an email send](https://support.telnyx.com/en/articles/16099894-scheduling-and-cancelling-an-email-send).

---

## **Step 3: Check whether the recipient is suppressed**

Telnyx may suppress an address after eligible delivery failures, repeated soft-bounce escalation, queue expiry, an invalid-address determination, a spam complaint, an unsubscribe, or a manual block. When some recipients are suppressed, the accepted send response lists skipped addresses in `suppressed`; if all recipients are suppressed, the request returns `422` with `recipient_suppressed`.

List suppression records and inspect their `to` values. The list endpoint does not support `filter[to]`; use supported filters such as reason, domain, or creation date, and page through the results when necessary:

```
curl "https://api.telnyx.com/v2/email_blocks?page[size]=100&page[number]=1" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Every suppression can be removed by ID, regardless of its reason:

```
curl -X DELETE https://api.telnyx.com/v2/email_blocks/{block_id} \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Deletion and send-time override are different. `ignore_suppression: true` can override only `unsubscribe` and `manual_block`. It cannot override `hard_bounce`, `invalid`, or `spam_complaint`. Remove any suppression only when you have a lawful, verified reason to resume sending; a future qualifying event may recreate it.

---

## **Step 4: Check the sending domain**

A degraded sending domain is a domain problem, not a recipient problem. The public send response is `403 Forbidden` with `errors[0].code` `10007` and detail explaining that the domain is degraded. Sending remains blocked until the required DNS records are restored.

Fetch the expected records:

```
curl https://api.telnyx.com/v2/email_domains/{domain_id}/dns_records \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Restore records that are missing or changed, wait for DNS propagation, and then re-run verification:

```
curl -X POST https://api.telnyx.com/v2/email_domains/{domain_id}/verify \
  -H "Authorization: Bearer YOUR_API_KEY"
```

See **Troubleshooting email domain verification** for a detailed walkthrough.

---

## **Step 5: It was accepted by the remote server but is not in the inbox**

If the recipient event is `delivered`, the remote server accepted the message, but it can still place it in spam, junk, quarantine, or another tab or folder.

- **Authentication alignment.** Make sure SPF, DKIM, and DMARC are published and passing for your sending domain.
- **Content.** Avoid misleading subject lines, all-caps, excessive links, link shorteners, and large image-only messages. Include a plain-text alternative alongside HTML.
- **Reputation.** Send to clean, engaged recipients, increase volume gradually, and keep bounce and complaint rates low.
- **Unsubscribe handling.** Keep one-click unsubscribe enabled for eligible mail so recipients can opt out instead of marking messages as spam.

---

## **Triage summary**

- Check the parent message for request progress, then inspect every page of recipient events for delivery outcomes.
- `sent` means accepted into the Telnyx MTA queue; `delivered` means accepted by the remote mail server.
- Treat event details as the cause. A `hard_bounce` suppression can also result from queue expiry or soft-bounce escalation.
- Any suppression can be deleted, but `ignore_suppression` overrides only unsubscribe and manual blocks.
- A degraded domain produces public error code `10007`.
- Respect the 1 MB body and 25 MB total decoded-message limits.

---

Related Articles

- [Getting started with Telnyx Email](https://support.telnyx.com/en/articles/15853622-getting-started-with-telnyx-email)
- [Managing email suppressions and unsubscribes](https://support.telnyx.com/en/articles/15853626-managing-email-suppressions-and-unsubscribes)
- [Setting up and troubleshooting Telnyx Email webhooks](https://support.telnyx.com/en/articles/16099889-setting-up-and-troubleshooting-telnyx-email-webhooks)
- [Understanding Telnyx Email errors and message size limits](https://support.telnyx.com/en/articles/16099890-understanding-telnyx-email-errors-and-message-size-limits)
- [Scheduling and cancelling an email send](https://support.telnyx.com/en/articles/16099894-scheduling-and-cancelling-an-email-send)
