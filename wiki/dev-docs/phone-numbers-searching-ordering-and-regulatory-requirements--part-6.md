---
title: 'Phone Numbers: Searching, Ordering, and Regulatory Requirements'
summary: This page covers the end-to-end workflow for purchasing phone numbers on
  Telnyx, including searching inventory, reserving numbers, placing standard, bulk,
  and advanced orders, fulfilling regulatory requirements (textual, address, document,
  and action types), uploading supporting documents, and configuring webhook notifications.
sources:
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/action-ordering-requirement
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/advanced-orders
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/bulk-ordering
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/buy-phone-number
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/documents/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/getting-started
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-orders
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-reservations/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-search/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/regulatory-requirements
updated_at: 2026-08-05T14:00:16Z
---

# Phone Numbers: Searching, Ordering, and Regulatory Requirements

*Part 6 of 6 — see also: [Part 1](phone-numbers-searching-ordering-and-regulatory-requirements--part-1.md), [Part 2](phone-numbers-searching-ordering-and-regulatory-requirements--part-2.md), [Part 3](phone-numbers-searching-ordering-and-regulatory-requirements--part-3.md), [Part 4](phone-numbers-searching-ordering-and-regulatory-requirements--part-4.md), [Part 5](phone-numbers-searching-ordering-and-regulatory-requirements--part-5.md)*

This page covers the end-to-end workflow for purchasing phone numbers on Telnyx, including searching inventory, reserving numbers, placing standard, bulk, and advanced orders, fulfilling regulatory requirements (textual, address, document, and action types), uploading supporting documents, and configuring webhook notifications.

## Documents

The Documents API allows you to upload and manage files that are required for regulatory compliance, identity verification, and other services on your Telnyx account. Documents are commonly used when ordering phone numbers in countries that require proof of identity, proof of address, or other supporting documentation. Once uploaded, documents must be linked to a service (such as a number order or regulatory requirement) within 30 minutes, or they will be automatically deleted.

### Constraints

- Maximum file size is **20 MB**.
- Maximum filename length is **512 characters**.
- Filenames must contain only printable Unicode characters. Non-printable characters (control characters) are not allowed.
- Spaces in filenames are automatically removed (e.g., `my document.pdf` becomes `mydocument.pdf`).
- The file extension is automatically appended based on the detected MIME type, even if omitted from the filename.
- Uploaded documents must be linked to a service within 30 minutes or they will be automatically deleted.
- Documents that are linked to a service cannot be deleted until they are unlinked.
- All uploaded documents are scanned for malware. Documents flagged as infected will be denied.

### Accepted File Types

| File type | MIME type |
| --- | --- |
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

Documents can be uploaded using any of three methods through the [POST /documents endpoint](https://developers.telnyx.com/api-reference/documents/upload-a-document):

- **Base64**: Provide the file content as a base64-encoded string in the `file` field, along with a `filename`.
- **Multipart form data**: Upload the file directly as binary data using `multipart/form-data`.

You can optionally include a `customer_reference` with any upload method to associate your own tracking identifier with the document.

### Antivirus Scan Statuses

All uploaded documents are scanned for malware. The `av_scan_status` field indicates the scan result:

| Status | Description |
| --- | --- |
| `pending_scan` | The document is queued for scanning. |
| `scanned` | The scan completed and no threats were detected. |
| `infected` | The scan detected malware. The document will be denied. |
| `not_scanned` | The document has not yet been scanned. |

### Document Links

When a document is attached to a service on your account (such as a number order or regulatory requirement), a document link is automatically created. You do not need to create these links manually — they are managed by the services that use the document. Use the [GET /document_links endpoint](https://developers.telnyx.com/api-reference/documents/list-all-document-links) to view which services a document is currently associated with. You can filter results by `document_id`, `linked_record_type`, or `linked_resource_id`.

## Webhook Notifications

You can configure webhook notifications to receive updates about your orders. [Follow this support article](https://support.telnyx.com/en/articles/4277896-notification-settings) to set up webhook notifications. Select the "Number Order Notifications" notification setting to receive webhooks for all number order events. Note that webhook events for bulk orders are generated by the underlying number orders created by the bulk order, not by the bulk order itself.

For Advanced Orders, the following webhook events are emitted:

- `advanced_order.status_update`: Emitted on status transitions (e.g., `pending` → `processing`, `processing` → `hold`, `hold` → `exception`, `processing` → `ordered`, `processing` → `failed`).
- `advanced_order.new_comment`: Emitted when a new comment is added to the Advanced Order.

Example payload for `advanced_order.status_update`:

```
{
  "data": {
    "event_type": "advanced_order.status_update",
    "id": "83996511-474b-4cbe-afc3-14c9c0144404",
    "occurred_at": "2025-09-23T20:18:04.789361Z",
    "payload": {
      "new_status": "pending",
      "old_status": "created",
      "order_id": "a6d6633e-824b-4042-a2b7-5ac0cccd799b"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://webhook.site/a61372df-394b-4c61-a601-79b35421824a"
  }
}
```

Example payload for `advanced_order.new_comment`:

```
{
  "data": {
    "event_type": "advanced_order.new_comment",
    "id": "236a47ea-ac71-4df0-aa3e-55f249c72818",
    "occurred_at": "2025-09-23T20:38:07.990291Z",
    "payload": {
      "advanced_order_id": "a6d6633e-824b-4042-a2b7-5ac0cccd799b",
      "comment": "This is an admin comment"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://webhook.site/a61372df-394b-4c61-a601-79b35421824a"
  }
}
```
