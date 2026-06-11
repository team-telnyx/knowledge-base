---
title: Phone Number Ordering
summary: 'Covers the full lifecycle of purchasing phone numbers on Telnyx: searching
  available inventory, reserving numbers, placing standard and bulk orders, submitting
  advanced orders for unavailable inventory, and fulfilling regulatory requirements
  including document uploads, address verification, and action-based requirements.'
sources:
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/action-ordering-requirement
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/advanced-orders
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/bulk-ordering
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/buy-phone-number
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/documents/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/getting-started/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-orders
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-reservations/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-search/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/regulatory-requirements/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/requirement-groups
updated_at: 2026-06-11T10:39:50Z
---

# Phone Number Ordering

*Part 3 of 3 — see also: [Part 1](phone-number-ordering--part-1.md), [Part 2](phone-number-ordering--part-2.md)*

Covers the full lifecycle of purchasing phone numbers on Telnyx: searching available inventory, reserving numbers, placing standard and bulk orders, submitting advanced orders for unavailable inventory, and fulfilling regulatory requirements including document uploads, address verification, and action-based requirements.

## Requirement Groups

Requirement groups let you pre-fill regulatory requirement values for a specific combination of `country_code`, `phone_number_type`, and `action`, then reuse that group across multiple orders.

### Requirement Group Constraints

- Optional in most countries; you can fulfill requirements individually instead.
- **Mandatory** in CH (Switzerland), DK (Denmark), IT (Italy), NO (Norway), PT (Portugal), and SE (Sweden).
- A requirement group must be **fulfilled** (every requirement has a value) to be used in mandatory countries.
- Groups can only be associated with orders matching their `country_code`, `phone_number_type`, and `action`.
- Number orders do not automatically synchronize with requirement group changes; you must make another API request to apply updates.

### Requirement Group Statuses

| Status | Description |
|---|---|
| unapproved | Default after creation. Orders using this group go through standard review. |
| pending-approval | Submitted and under review. Orders go through standard review. |
| approved | Passed review. Orders activate automatically within minutes. |
| declined | Requirements rejected during pre-approval. Orders go through standard review. |
| expired | Requirements exceeded validity window. Orders go through standard review. |
| no-longer-eligible | Regulatory requirements changed; cannot be used for orders. Create a new group. |

### Pre-Approval

Pre-approval is optional. Once a requirement group is pre-approved, orders using it can activate automatically within minutes, bypassing manual review.

**When to use pre-approval**: You will reuse the same group for multiple orders AND need quick activation.

**When to skip**: Only a few orders or you don't need immediate activation.

**Limitations**:
- Not supported in all countries (e.g., Italy does not support pre-approval).
- If the group has an address requirement, ordered numbers must comply with that address (e.g., matching the DID area code). Ordering a mismatched number causes the order to undergo standard review.

### Requirement Group Flow

1. **Create a requirement group**: `POST /v2/requirement_groups` with `country_code`, `phone_number_type`, and `action`.
2. **View the requirement group**: `GET /v2/requirement_groups` (list) or `GET /v2/requirement_groups/:id` (retrieve). The `regulatory_requirements` array lists each requirement with its `requirement_id`.
3. **Fulfill the requirement group**: `PATCH /v2/requirement_groups/:id` with each `requirement_id` and its associated value.
4. **Associate with an order**:
   - **New number orders**: Include `requirement_group_id` in each `phone_number` object of the `POST /v2/number_orders` request.
   - **Existing pending sub number orders**: `POST /v2/sub_number_orders/:id/requirement_group` with the `requirement_group_id`.
   - **Porting orders**: `PATCH /v2/porting_orders/:id` with the `requirement_group_id`.
5. **Submit for pre-approval (optional)**: `POST /v2/requirement_groups/:id/submit_for_approval`. The group transitions to `pending-approval`. If approved, the status becomes `approved`; if rejected, `declined`. Feedback is communicated via comments (`comment_record_type=requirement_group`).

## Action Requirements

Action requirements are a special type of regulatory requirement that cannot be fulfilled by submitting documents or text information. Instead, the end user must complete an external action such as identity verification through a third-party service.

### Australia Mobile ID Verification

Australia mobile number orders require end-user identity verification. Telnyx partners with [Onfido](https://onfido.com/) for this process.

- **Requirement ID**: `b7c72fb8-fa08-4529-aaf6-b9117d3f3698`

**Verification process**:

1. Generate a verification link by making a `POST /v2/external_requirements/sub_number_orders/` request with the end user's `first_name` and `last_name`.
2. The API returns a URL in the `requirement_action.value` field. Share this URL with the end user.
3. The end user visits the URL and completes identity verification via the Onfido portal.
4. Upon approval, the requirement is automatically marked as completed on the order.
5. The order's `requirements_met` field updates to `true`, allowing the order to proceed.

## Documents

The Documents API lets you upload and manage files required for regulatory compliance, identity verification, and other services.

### Document Constraints

- Maximum file size: **20 MB**.
- Maximum filename length: **512 characters**.
- Filenames must contain only printable Unicode characters; control characters are not allowed.
- Spaces in filenames are automatically removed.
- File extensions are automatically appended based on detected MIME type.
- Documents must be linked to a service within **30 minutes** or they are automatically deleted.
- Documents linked to a service cannot be deleted until unlinked.
- All uploads are scanned for malware; infected documents are denied.

### Accepted File Types

| File type | MIME type |
|---|---|
| PDF | `application/pdf` |
| PNG | `image/png` |
| JPEG | `image/jpeg` |
| CSV | `text/csv`, `application/csv` |
| Plain text | `text/plain` |
| JSON | `application/json` |
| Word (.docx) | `application/vnd.openxmlformats-officedocument.wordprocessingml.document` |
| Word (.doc) | `application/msword` |
| Excel (.xlsx) | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` |
| Excel (.xls) | `application/vnd.ms-excel` |

### Upload Methods

Upload via `POST /v2/documents` using:
- **Base64**: Provide base64-encoded content in the `file` field with a `filename`.
- **Multipart form data**: Upload binary data using `multipart/form-data`.

Optionally include a `customer_reference` for tracking.

### Antivirus Scan Statuses

| Status | Description |
|---|---|
| `pending_scan` | Queued for scanning. |
| `scanned` | Scan completed; no threats detected. |
| `infected` | Malware detected; document denied. |
| `not_scanned` | Not yet scanned. |

### Document Links

When a document is attached to a service, a document link is created automatically. Use `GET /v2/document_links` to view associations, filtered by `document_id`, `linked_record_type`, or `linked_resource_id`.

## Webhook Notifications

Configure webhook notifications for order events via the [notification settings guide](https://support.telnyx.com/en/articles/4277896-notification-settings).

- **Standard and bulk orders**: Select "Number Order Notifications" to receive webhooks for all number order events.
- **Advanced orders**: Advanced order webhooks include `advanced_order.status_update` (status transitions) and `advanced_order.new_comment` (new comments).
- **Requirement groups**: Select "Requirement Group Status Change" to receive webhooks when a requirement group transitions between statuses.
