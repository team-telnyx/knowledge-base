---
title: Number Reputation
summary: Number Reputation is a Telnyx product that monitors the spam reputation of
  US outbound calling numbers by querying the major call-analytics networks used by
  US carriers. It exposes per-number spam risk, granular scores, and category labels,
  and supports batch remediation requests to re-evaluate flagged numbers. The product
  is governed by its own Terms of Service and is currently US-only.
sources:
- url: https://developers.telnyx.com/docs/number-reputation/loa
- url: https://developers.telnyx.com/docs/number-reputation/overview
- url: https://developers.telnyx.com/docs/number-reputation/phone-numbers
- url: https://developers.telnyx.com/docs/number-reputation/pricing
- url: https://developers.telnyx.com/docs/number-reputation/quickstart
- url: https://developers.telnyx.com/docs/number-reputation/remediation
- url: https://developers.telnyx.com/docs/number-reputation/settings
updated_at: 2026-08-05T14:00:24Z
---

# Number Reputation

*Part 5 of 5 — see also: [Part 1](number-reputation--part-1.md), [Part 2](number-reputation--part-2.md), [Part 3](number-reputation--part-3.md), [Part 4](number-reputation--part-4.md)*

Number Reputation is a Telnyx product that monitors the spam reputation of US outbound calling numbers by querying the major call-analytics networks used by US carriers. It exposes per-number spam risk, granular scores, and category labels, and supports batch remediation requests to re-evaluate flagged numbers. The product is governed by its own Terms of Service and is currently US-only.

## Pricing

Number Reputation pricing has three components:

| Component | Cost | Description |
| --- | --- | --- |
| **Reputation monitoring** | $100/month per Enterprise | Recurring monthly fee to enable reputation monitoring on an enterprise. |
| **Reputation check** | $0.10 per check | Charged per reputation query. Cached reads are free; fresh (live) queries and auto-refreshes are billed. |
| **Remediation check** | $1.00 per check | Charged per number submitted for reputation remediation (re-evaluation). |

Rendering the LOA is **not billable**. You only pay once you enable reputation monitoring and add numbers.

For the full pricing details, see the [Telnyx Numbers pricing page](https://telnyx.com/pricing/numbers).

### How billing works

| Action | Billed? |
| --- | --- |
| Render LOA PDF | No |
| Enable reputation monitoring | Yes ($100 MRC) |
| Add phone numbers | Yes ($0.10 per number per check) |
| Cached reputation query | No (free once data exists) |
| Fresh reputation query (`?fresh=true`) | Yes ($0.10 per check) |
| Forced refresh | Yes ($0.10 per check) |
| Auto-refresh (scheduled) | Yes ($0.10 per check per number) |
| Submit remediation request | Yes ($1.00 per number) |

Enterprise registration is free. An Enterprise can serve Number Reputation, Branded Calling, or both.

## Simplified endpoints

If your account has only one enterprise, you can skip the `enterprise_id` path parameter:

| Method | Simplified path |
| --- | --- |
| GET | `/v2/reputation/numbers` |
| GET | `/v2/reputation/numbers/{phone_number}` |
| DELETE | `/v2/reputation/numbers/{phone_number}` |

Remember to URL-encode the `+` as `%2B` in the `{phone_number}` path:

```
# List all monitored numbers (simplified)
curl https://api.telnyx.com/v2/reputation/numbers \
  -H "Authorization: Bearer YOUR_API_KEY"

# Get reputation for a specific number (simplified)
curl https://api.telnyx.com/v2/reputation/numbers/%2B12025551234 \
  -H "Authorization: Bearer YOUR_API_KEY"

# Remove a specific number (simplified)
curl -X DELETE https://api.telnyx.com/v2/reputation/numbers/%2B12025551234 \
  -H "Authorization: Bearer YOUR_API_KEY"
```

## Portal setup

You can also set up Number Reputation from the [Telnyx Portal](https://portal.telnyx.com) — the full workflow (accept ToS, create enterprise, render LOA, enable monitoring, add numbers, query scores) is available in the UI. The API and Portal are fully interchangeable.

## Next steps

- [Number Reputation Settings](number-reputation-settings.md) — vetting lifecycle, auto-refresh schedules, and configuration
- [Letter of Authorization (LOA)](letter-of-authorization-loa.md) — render, sign, upload, and replace a rejected LOA
- [Phone Number Reputation](phone-number-reputation.md) — reputation data model, scores, and querying in depth
- [Reputation Remediation](reputation-remediation.md) — submit flagged numbers for re-evaluation
- [Number Reputation Pricing](number-reputation-pricing.md) — Number Reputation pricing details
