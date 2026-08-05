---
title: Email API
summary: Telnyx email API reference covering reusable Liquid-based email templates
  (create, manage, render, and send), unsubscribe groups for category-level opt-outs,
  and pre-send email validation (single and batch) with five structured checks.
sources:
- url: https://developers.telnyx.com/docs/messaging/email/templates/index
- url: https://developers.telnyx.com/docs/messaging/email/unsubscribe-groups
- url: https://developers.telnyx.com/docs/messaging/email/validation
updated_at: 2026-08-05T13:52:12Z
---

# Email API

*Part 2 of 3 — see also: [Part 1](email-api--part-1.md), [Part 3](email-api--part-3.md)*

Telnyx email API reference covering reusable Liquid-based email templates (create, manage, render, and send), unsubscribe groups for category-level opt-outs, and pre-send email validation (single and batch) with five structured checks.

## Unsubscribe Groups

Unsubscribe groups let recipients opt out of specific categories of email without unsubscribing from all your messages. For example, a recipient can unsubscribe from your marketing newsletter but still receive transactional receipts.

### How it works

1. **Create a group** — each group represents a category of email (e.g., "Marketing", "Product Updates", "Billing")
2. **Send with a group** — include `group_id` in your send request
3. **Recipients unsubscribe** — clicking the unsubscribe link in the email immediately opts the recipient out of the group associated with that message, then shows a generic confirmation page
4. **Suppression is automatic** — future sends to that recipient with the same group are blocked

### Create an unsubscribe group

```
curl -X POST https://api.telnyx.com/v2/email_unsubscribe_groups \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "name": "Marketing Newsletter",
    "description": "Weekly product updates and promotions"
  }'
```

### Send with a group

Include the `group_id` field when sending a message to associate it with an unsubscribe group:

```
curl -X POST https://api.telnyx.com/v2/email_messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "from": {"email": "marketing@yourdomain.com"},
    "to": [{"email": "user@example.com"}],
    "subject": "Weekly product roundup",
    "html_body": "<p>Here is what is new this week...</p>",
    "group_id": "{group_id}"
  }'
```

When a recipient clicks the unsubscribe link, they are opted out of that specific group only. If `group_id` is omitted, the unsubscribe becomes global — the recipient is suppressed from all future sends.

### List group suppressions

View which recipients have unsubscribed from a specific group:

```
curl -X GET https://api.telnyx.com/v2/email_unsubscribe_groups/{id}/suppressions \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Add a suppression manually

Add a single recipient to a group's suppression list (e.g., via a support request):

```
curl -X POST https://api.telnyx.com/v2/email_unsubscribe_groups/{id}/suppressions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"to": "user@example.com"}'
```

### Remove a suppression

Remove a suppression to allow sending again:

```
curl -X DELETE https://api.telnyx.com/v2/email_unsubscribe_groups/{id}/suppressions/{email} \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Best practices

- **Use groups for every marketing send** — transactional emails can use a group too, but recipients should rarely want to unsubscribe from those
- **Keep group names clear** — group names are for your internal organization
- **Don't create too many** — 3-5 groups is typical; more creates unnecessary complexity
- **Monitor suppression counts** — high unsubscribe rates signal content or frequency issues
- **Always include `group_id` for marketing** — without it, unsubscribes become global and block all future sends to that recipient
