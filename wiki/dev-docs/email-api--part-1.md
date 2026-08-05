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

*Part 1 of 3 — see also: [Part 2](email-api--part-2.md), [Part 3](email-api--part-3.md)*

Telnyx email API reference covering reusable Liquid-based email templates (create, manage, render, and send), unsubscribe groups for category-level opt-outs, and pre-send email validation (single and batch) with five structured checks.

## Email Templates

Email templates store reusable subject and body content so you can send the same message to many recipients without re-sending the content on every request. Templates use [Liquid](https://shopify.github.io/liquid/) variables — `{{first_name}}` — so each send renders recipient-specific content from variables you supply at send time.

Templates are useful when you:

- Send the same message repeatedly — onboarding sequences, receipts, password resets.
- Separate content from code — let designers edit email copy in a template while your application only passes variables.
- Build agent workflows — an AI agent generates variable values, the template governs structure, and you render to validate the result before sending.

All requests use the base URL `https://api.telnyx.com/v2` and an `Authorization: Bearer ***` header.

### Create a template

Create a template with `POST /email_templates`. Only `name` is required; `subject`, `html_body`, and `text_body` are optional Liquid template strings.

```
curl -X POST https://api.telnyx.com/v2/email_templates \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ***" \
  -d '{
    "name": "Welcome Email",
    "subject": "Welcome to Telnyx, {{first_name}}!",
    "html_body": "<h1>Hi {{first_name}},</h1><p>Thanks for signing up.</p>",
    "text_body": "Hi {{first_name}}, thanks for signing up."
  }'
```

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `name` | string | yes | Letters, numbers, spaces, hyphens, and underscores only (`^[A-Za-z0-9 _-]+$`). Unique per account. |
| `subject` | string | no | Liquid template subject. |
| `html_body` | string | no | Liquid template HTML body. |
| `text_body` | string | no | Liquid template text body. |
| `variables` | array of strings | no | Variable names the template uses. **Auto-extracted** from `subject`, `html_body`, and `text_body` when you omit it. The extractor is deliberately narrow (see Auto-extraction limits) — supply it explicitly when your template uses filters or other complex Liquid. |

A successful create returns `201 Created` with the template in `data`:

```
{
  "data": {
    "record_type": "email_template",
    "id": "7a7c1a2b-1111-4c72-8c21-2bbf3d40c123",
    "name": "Welcome Email",
    "subject": "Welcome to Telnyx, {{first_name}}!",
    "html_body": "<h1>Hi {{first_name}},</h1><p>Thanks for signing up.</p>",
    "text_body": "Hi {{first_name}}, thanks for signing up.",
    "variables": ["first_name"],
    "created_at": "2026-07-06T12:00:00.000000Z",
    "updated_at": "2026-07-06T12:00:00.000000Z"
  }
}
```

The `variables` array is stored on the template and returned on every read. Save the `id` — you'll use it to render, send with, update, and delete the template.

The `variables` field is descriptive metadata, not a constraint. Passing `template_variables` with keys that aren't listed here is not an error — only the Liquid tags actually present in your template's content are substituted. Use `variables` to document what a caller should supply.

### Manage templates

#### List templates

List templates for your account with `GET /email_templates`. Pagination is cursor-based: `page_size` (default 25, clamped 1–100) and `page_cursor`.

```
curl https://api.telnyx.com/v2/email_templates?page_size=10 \
  -H "Authorization: Bearer ***"
```

```
{
  "data": [
    {
      "record_type": "email_template",
      "id": "7a7c1a2b-1111-4c72-8c21-2bbf3d40c123",
      "name": "Welcome Email",
      "subject": "Welcome to Telnyx, {{first_name}}!",
      "html_body": "<h1>Hi {{first_name}},</h1>",
      "text_body": "Hi {{first_name}}",
      "variables": ["first_name"],
      "created_at": "2026-07-06T12:00:00.000000Z",
      "updated_at": "2026-07-06T12:00:00.000000Z"
    }
  ],
  "meta": {
    "page_size": 10,
    "page_cursor": "MjAyNi0wNy0wNlQxMjowMDowMHw3YTdjMW..."
  }
}
```

`page_cursor` in `meta` is the opaque cursor for the next page. It is **omitted** (not `null`) when there is no next page. Pass it back as the `page_cursor` query parameter to fetch the next page.

#### Get a template

Fetch a single template by id with `GET /email_templates/{id}`:

```
curl https://api.telnyx.com/v2/email_templates/7a7c1a2b-1111-4c72-8c21-2bbf3d40c123 \
  -H "Authorization: Bearer ***"
```

Returns `200` with the template in `data`, or `404` if the template doesn't exist or belongs to another account.

#### Update a template

Update a template with `PATCH /email_templates/{id}` or `PUT /email_templates/{id}`. Both verbs are served by the same partial-update handler, accept the same `UpdateEmailTemplateRequest` body, and return `200` with the updated template.

```
curl -X PATCH https://api.telnyx.com/v2/email_templates/7a7c1a2b-1111-4c72-8c21-2bbf3d40c123 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ***" \
  -d '{
    "subject": "Welcome aboard, {{first_name}}!"
  }'
```

Updatable fields: `name`, `subject`, `html_body`, `text_body`, `variables`. When you change `subject` or a body and don't supply `variables`, the variable list is auto-extracted again from the new content.

`PUT` is **not** a full replacement. `PUT` and `PATCH` are routed to the same handler, and both update only the fields you send — omitted fields are left unchanged on either verb. Sending `PUT` with a partial body will not clear the fields you left out. To clear a field, send it explicitly as `null`.

#### Delete a template

Delete a template with `DELETE /email_templates/{id}`:

```
curl -X DELETE https://api.telnyx.com/v2/email_templates/7a7c1a2b-1111-4c72-8c21-2bbf3d40c123 \
  -H "Authorization: Bearer ***"
```

Returns `204 No Content` with an empty body. Deleting a template does not affect messages already sent from it; it only prevents future sends and renders that reference the `template_id`.

### Variables

Template content uses [Liquid](https://shopify.github.io/liquid/) syntax. The renderer is the [Solid](https://hexdocs.pm/solid) Liquid engine.

#### What's substitutable

Variable substitution applies to **all three content fields** — `subject`, `html_body`, and `text_body`. Each is rendered independently from the same `template_variables` map.

#### Syntax

| Construct | Example | Result |
| --- | --- | --- |
| Output a variable | `{{first_name}}` | The value of `first_name`. |
| Dot-notation access | `{{user.name}}` | The `name` field of a `user` object. |
| For loop | `{% for item in items %}{{item.title}}{% endfor %}` | Iterates the `items` collection. |
| Assign a local | `{% assign greeting = "Hi" %}{{greeting}}` | Creates a local for use in the rest of the template. |

#### Missing-variable behavior

**A variable you don't supply renders as an empty string — it does not raise an error.** If your template contains `{{first_name}}` and you send `template_variables: {}` (or omit the key entirely), the rendered output has an empty string in place of `{{first_name}}`. The render or send succeeds.

This is by design: templates degrade gracefully so a partial variable set never blocks a send. If you need to enforce that a variable is present, validate the rendered output with the render endpoint before sending, or check your `template_variables` map in application code.

#### Auto-extraction limits

When you omit `variables`, Telnyx extracts the list from your template content with a small set of regexes. It recognizes exactly three shapes:

- Unfiltered output tags — `{{first_name}}` → `first_name`
- Dot-notation roots in unfiltered output tags — `{{user.name}}` → `user`
- For-loop collections — `{% for item in items %}` → `items` (the loop variable `item` is extracted only when separately referenced in an unfiltered output tag such as `{{item.title}}`)

`{% assign %}` targets are excluded, since the template creates them rather than receiving them.

Anything else is **not** extracted. Most importantly, an output tag containing a filter is skipped entirely:

| Template content | Extracted |
| --- | --- |
| `Hi {{first_name}}` | `["first_name"]` |
| `{{ user.name }}` | `["user"]` |
| `{% for item in items %}{{item.title}}{% endfor %}` | `["item", "items"]` |
| `{{user_input | escape}}` | `[]` |
| `{{ price | round: 2 }}` | `[]` |
| `{% if admin %}{{name}}{% endif %}` | `["name"]` (the `if` condition `admin` is missed) |

A filtered expression like `{{user_input | escape}}` renders correctly at send time but is **not** auto-extracted, so `variables` comes back empty for it. Because `variables` is descriptive metadata only, this never breaks a send — but it does make the template under-report what a caller must supply. Pass `variables` explicitly whenever your template uses filters, `if`/`unless` conditions, or other complex Liquid expressions.

#### Escaping and HTML safety

The renderer substitutes values as-is — it does **not** HTML-escape variables. If a variable value can contain untrusted content (for example, user-generated display names), escape it in your application before passing it in `template_variables`, or use Liquid's [`escape` filter](https://shopify.github.io/liquid/filters/escape/) in the template: `{{user_input | escape}}`.

### Render and preview

`POST /email_templates/{id}/render` renders a template with a set of variables and returns the Liquid-rendered, **pre-send** content — without sending anything. This is the key capability that makes templates safe for automated and agent-driven workflows: you can inspect the rendered output, run assertions against it, and catch malformed variables before a single message goes out.

The render output is the Liquid-rendered template. The send pipeline subsequently applies CSS inlining (when `inline_css: true`), click-link rewriting, and open-tracking pixel injection. Final recipient HTML may therefore differ from the preview. Use render to validate template structure and variable substitution, not as a byte-identical preview of the delivered message.

#### Request

Supply `template_variables` in the body. The body itself is optional — if you omit it, the template renders with an empty variable set.

```
curl -X POST https://api.telnyx.com/v2/email_templates/7a7c1a2b-1111-4c72-8c21-2bbf3d40c123/render \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ***" \
  -d '{
    "template_variables": {
      "first_name": "Ada"
    }
  }'
```

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `template_variables` | object | no | Variable values for Liquid rendering. Defaults to `{}`. Non-object values are silently coerced to an empty map — this coercion is **specific to the render endpoint**; the same value on `POST /email_messages` returns `422 Validation Failed`. |

#### Response

A successful render returns `200` with the full template object **plus** the rendered `subject`, `html_body`, and `text_body` replacing the template-string versions:

```
{
  "data": {
    "record_type": "email_template",
    "id": "7a7c1a2b-1111-4c72-8c21-2bbf3d40c123",
    "name": "Welcome Email",
    "subject": "Welcome to Telnyx, Ada!",
    "html_body": "<h1>Hi Ada,</h1><p>Thanks for signing up.</p>",
    "text_body": "Hi Ada, thanks for signing up.",
    "variables": ["first_name"],
    "created_at": "2026-07-06T12:00:00.000000Z",
    "updated_at": "2026-07-06T12:00:00.000000Z"
  }
}
```

The response merges the stored template (record type, id, name, variables, timestamps) with the rendered output. Compare the rendered `subject`/`html_body`/`text_body` against the stored Liquid versions to confirm substitution worked.

#### Errors

| HTTP | Code | When |
| --- | --- | --- |
| 404 | `10001` | The template id doesn't exist or belongs to another account. |
| 422 | `10015` | Liquid parsing or rendering failed (malformed Liquid syntax or a filter error). The standard `detail` field carries the engine's error detail. |

A 422 response from the standalone render endpoint uses the standard error envelope:

```
{
  "errors": [
    {
      "code": "10015",
      "title": "Template Render Failed",
      "detail": "Liquid parse error: ..."
    }
  ]
}
```

Note that **missing variables are not an error** — they render as empty strings. A `422` from the standalone render endpoint means the Liquid itself is syntactically broken or a filter threw; it uses the `10015` standard error envelope shown above.

#### Use cases

1. **Preview UIs** — Build a preview pane in any email composer by calling render with draft variables. Because the response is plain JSON, you can render server-side and drop the HTML straight into an `<iframe>` or your preview component — no client-side Liquid engine needed. The Liquid-rendered output matches the send path's variable substitution; note that the send pipeline may further modify HTML (CSS inlining, tracking pixel) before final delivery.
2. **Agent content validation** — When an AI agent generates variable values, render the template before sending to confirm the output is well-formed — that names aren't blank, that loop bodies populated, that no stray Liquid tags leaked into the rendered text. Treat the render call as a gate: only send once the rendered subject and body pass your assertions.
3. **CI checks on template changes** — Call render in a test or CI step against a fixture variable set whenever a template changes. A non-empty `errors` array, or a rendered body that diverges from a recorded snapshot, fails the check before the template reaches production.

### Send with a template

Send using a stored template with `POST /email_messages`. Pass `template_id` and `template_variables`; the API renders the template server-side and sends the result. You only supply the addressing — `from`, `to`, and any send options like `scheduled_at` or `inline_css`. For safe retries, pass an `Idempotency-Key` HTTP header rather than a request-body field.

```
curl -X POST https://api.telnyx.com/v2/email_messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ***" \
  -H "Idempotency-Key: d7888471-1951-4ec1-9eef-bf69fe804ab4" \
  -d '{
    "from": "sender@example.com",
    "to": ["recipient@example.com"],
    "template_id": "7a7c1a2b-1111-4c72-8c21-2bbf3d40c123",
    "template_variables": {
      "first_name": "Ada"
    }
  }'
```

| Field | Type | Notes |
| --- | --- | --- |
| `template_id` | string (UUID) | The stored template to render. Must belong to your account. |
| `template_variables` | object | Variables for Liquid rendering. Defaults to `{}`. Must be an object — non-object values return `422 Validation Failed` on send; only the standalone render endpoint coerces them to `{}`. |

When you send with `template_id`, `subject` is optional — the template's rendered subject is used. If the template has no `subject` or it renders to an empty string, the request returns `400`.

#### Precedence: template content and inline content are mutually exclusive

You **cannot** mix a template with inline content. If the request contains `template_id` **and** any of `subject`, `html_body`, or `text_body`, the API returns `400` with:

```
{
  "errors": [
    {
      "code": "10015",
      "title": "Bad Request",
      "detail": "template_id cannot be used with subject, html_body, or text_body"
    }
  ]
}
```

There is no merge or override — the presence of `template_id` means the template fully governs `subject`, `html_body`, and `text_body`. Other top-level fields (`from`, `to`, `cc`, `bcc`, `reply_to`, `attachments`, `headers`, `tags`, `metadata`, `scheduled_at`, `inline_css`) combine with the template normally.

Use `scheduled_at` to schedule a templated send. `send_at` is a deprecated alias kept for backward compatibility — when both are supplied, `scheduled_at` wins, and responses always report the field as `scheduled_at`.

Want to preview before sending? Call `POST /email_templates/{id}/render` with the same `template_variables`, inspect the output, then send. The render and send paths use the same Liquid engine and the same template, so the variable substitution matches. Note that the send pipeline may apply additional transformations (CSS inlining, click-link rewriting, open-tracking pixel) before final delivery.

#### Render errors at send time

If the template's Liquid fails to render at send time, the request returns `422` with the send endpoint's non-standard `{code: "render_error", message: "..."}` error shape. This differs from the standalone render endpoint, which returns `10015` with `title` and `detail`. A template that renders with missing variables as empty strings will still send — only a genuine Liquid parse or filter failure blocks the send.

#### `inline_css` with templates

`inline_css` is a send-time option on `POST /email_messages`, not a template property. When you set `inline_css: true` on a send that uses a template, the rendered HTML body has its `<style>` blocks inlined into element `style` attributes before the message is sent. This works the same way whether you send inline HTML or via a template.
