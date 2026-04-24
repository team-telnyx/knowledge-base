---
title: Number Reputation Settings
summary: Enable, configure, and manage Number Reputation monitoring for your enterprise.
sources:
  - url: https://developers.telnyx.com/docs/branded-calling/number-reputation/settings
    content_hash: 566dacf4011ada22c1408826de41d420de2c2653c34a6c4ebedfa2b956402166
updated_at: 2026-04-10T00:00:00Z
---

# Number Reputation Settings

Enable, configure, and manage Number Reputation monitoring for your enterprise.

## Overview

Number Reputation Settings control the monitoring lifecycle for your enterprise. You enable reputation monitoring, configure how often numbers are checked, and manage the vetting status.

## Prerequisites

Before enabling Number Reputation, you need:

1. An [Enterprise](https://developers.telnyx.com/docs/branded-calling/enterprises/overview) registered on your account
2. A signed **Letter of Authorization (LOA)** uploaded via the Documents API — this authorizes Telnyx to register your numbers with third-party analytics providers

## Enable Number Reputation

Submit your LOA document ID to enable reputation monitoring:

```bash theme={null}
curl -X POST https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "loa_document_id": "YOUR_DOCUMENT_ID"
  }'
```

Your enterprise details are sent to Hiya for automated vetting. This typically takes **minutes**.

## Vetting lifecycle

```
pending ──► approved    (you can now register numbers and query reputation)
pending ──► rejected    (check rejection_reasons in the response)
approved ──► deleted    (reputation disabled via DELETE)
```

Check your current status:

```bash theme={null}
curl https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation \
  -H "Authorization: Bearer YOUR_API_KEY"
```

The response includes:

| Field               | Description                                     |
| :------------------ | :---------------------------------------------- |
| `status`            | `pending`, `approved`, `rejected`, or `deleted` |
| `check_frequency`   | Current auto-refresh schedule                   |
| `loa_document_id`   | Your uploaded LOA reference                     |
| `rejection_reasons` | Array of reasons if status is `rejected`        |

## Auto-refresh schedules

Telnyx automatically runs fresh reputation queries on all your registered numbers based on the configured `check_frequency`:

| Frequency        | Schedule                                        |
| :--------------- | :---------------------------------------------- |
| `business_daily` | Mon–Fri **(default)**                           |
| `daily`          | Every day including weekends                    |
| `weekly`         | Once per week                                   |
| `biweekly`       | Every 2 weeks                                   |
| `monthly`        | Once per month                                  |
| `never`          | Manual only — use `?fresh=true` or bulk refresh |

### Change the schedule

```bash theme={null}
curl -X PATCH https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/frequency \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"check_frequency": "daily"}'
```

Choose a frequency that balances data freshness with cost. Each auto-refresh counts as a billed query per number.

## Disable Number Reputation

To stop monitoring entirely and remove the enterprise from reputation tracking:

```bash theme={null}
curl -X DELETE https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation \
  -H "Authorization: Bearer YOUR_API_KEY"
```

This de-registers your numbers from analytics providers. The status changes to `deleted`.

## Terms of Service

You must accept the Number Reputation Terms of Service before enabling monitoring:

```bash theme={null}
curl -X POST https://api.telnyx.com/v2/terms_of_service/number_reputation/agree \
  -H "Authorization: Bearer YOUR_API_KEY"
```

This is a one-time step per account.


## Related Pages

- [Number Reputation](../runbooks/number-reputation.md)
- [Number Reputation Quickstart](../tutorial/number-reputation-quickstart.md)
- [Phone Number Reputation](../runbooks/phone-number-reputation.md)
- [Transcription Settings](../runbooks/transcription-settings.md)
- [Number Reservations](../runbooks/number-reservations.md)
