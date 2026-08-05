---
title: Branded Calling
summary: 'Branded Calling is a Telnyx product (currently in beta, US-only) that displays
  a verified business identity — display name, logo, and call reason — on outbound
  calls instead of a bare number or "Spam Likely". The feature is built on a CTIA-managed
  industry registry and uses SHAKEN PASSporT tokens to deliver rich call data to supported
  carriers and devices. This page covers the full lifecycle: registering an Enterprise,
  accepting the Branded Calling Terms of Service, activating the product, creating
  and vetting a Display Identity Record (DIR), attaching phone numbers in batches,
  configuring call reasons, handling infringement claims, and pricing.'
sources:
- url: https://developers.telnyx.com/docs/branded-calling/bc-phone-numbers/index
- url: https://developers.telnyx.com/docs/branded-calling/brands/index
- url: https://developers.telnyx.com/docs/branded-calling/call-reasons/index
- url: https://developers.telnyx.com/docs/branded-calling/enterprises/index
- url: https://developers.telnyx.com/docs/branded-calling/infringement-claims/index
- url: https://developers.telnyx.com/docs/branded-calling/overview
- url: https://developers.telnyx.com/docs/branded-calling/pricing
- url: https://developers.telnyx.com/docs/branded-calling/quickstart
- url: https://developers.telnyx.com/docs/branded-calling/terms-of-service/index
updated_at: 2026-08-05T13:39:22Z
---

# Branded Calling

*Part 4 of 8 — see also: [Part 1](branded-calling--part-1.md), [Part 2](branded-calling--part-2.md), [Part 3](branded-calling--part-3.md), [Part 5](branded-calling--part-5.md), [Part 6](branded-calling--part-6.md), [Part 7](branded-calling--part-7.md), [Part 8](branded-calling--part-8.md)*

Branded Calling is a Telnyx product (currently in beta, US-only) that displays a verified business identity — display name, logo, and call reason — on outbound calls instead of a bare number or "Spam Likely". The feature is built on a CTIA-managed industry registry and uses SHAKEN PASSporT tokens to deliver rich call data to supported carriers and devices. This page covers the full lifecycle: registering an Enterprise, accepting the Branded Calling Terms of Service, activating the product, creating and vetting a Display Identity Record (DIR), attaching phone numbers in batches, configuring call reasons, handling infringement claims, and pricing.

## Call Reasons

A **call reason** is a short string explaining why your business is calling, for example, "Appointment Reminder" or "Delivery Update". Call reasons are set at the **DIR level** as a list of 1-10 strings (each up to 64 characters) at DIR-create time.

Telnyx maintains a list of **pre-approved call reasons**. When a DIR's `call_reasons` are *all* pre-approved, the call-reason vetting check passes automatically, which can help speed up review. If any reason is custom (not pre-approved), that check is reviewed by a human instead. Either way the DIR still goes through full vetting; pre-approved reasons are not auto-approved.

### API endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/v2/call_reasons` | List pre-approved call reasons. |
| `POST` | `/v2/call_reasons/validate` | Check whether a list of reasons is fully pre-approved. |

### List pre-approved call reasons

Default `page[size]` is `100` (max `250`).

```
curl -g "https://api.telnyx.com/v2/call_reasons?page[size]=100" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Use the returned `reason` strings verbatim in your DIR's `call_reasons` array to help speed up the call-reason check during vetting.

### Validate a list of call reasons

Before creating a DIR, check whether the reasons you plan to use are pre-approved:

```
curl -X POST https://api.telnyx.com/v2/call_reasons/validate \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '["Appointment Reminder", "Follow-Up Calls"]'
```

> The body is a **bare JSON array of strings**: do **not** wrap it in `{ "call_reasons": [...] }`. This is unusual for Telnyx APIs; copy the example verbatim.

The result is returned under a top-level `data` object with three fields:
`all_pre_approved` (true when *every* reason is pre-approved and enabled),
`requires_manual_vetting` (true when at least one reason is not pre-approved),
and `non_approved_reasons` (the list of reasons that are not pre-approved).

### Constraints

| Limit | Value |
| --- | --- |
| Min call reasons per DIR | 1 |
| Max call reasons per DIR | 10 |
| Max characters per reason | 64 |
