---
title: Phone Numbers and Porting
summary: This page consolidates Telnyx developer documentation covering phone number
  search, ordering, reservations, bulk and advanced orders, regulatory requirements,
  requirement groups, documents, port-in and port-out workflows, and the notifications
  and events that track them. It provides an end-to-end reference for purchasing numbers,
  fulfilling regulatory requirements, transferring numbers in and out of Telnyx, and
  monitoring the lifecycle of those operations via webhooks and events.
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
- url: https://developers.telnyx.com/docs/numbers/porting/allowed-foc-dates
- url: https://developers.telnyx.com/docs/numbers/porting/bundles-porting
- url: https://developers.telnyx.com/docs/numbers/porting/cancel-port-order
- url: https://developers.telnyx.com/docs/numbers/porting/extensions
- url: https://developers.telnyx.com/docs/numbers/porting/getting-started/index
- url: https://developers.telnyx.com/docs/numbers/porting/messaging-porting
- url: https://developers.telnyx.com/docs/numbers/porting/on-demand-activations
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-blocks
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-events
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-notifications
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-requirements
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-events
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-notifications
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-quickstart/index
- url: https://developers.telnyx.com/docs/numbers/porting/porting-additional-steps/index
updated_at: 2026-07-17T09:16:33Z
---

# Phone Numbers and Porting

*Part 6 of 11 — see also: [Part 1](phone-numbers-and-porting--part-1.md), [Part 2](phone-numbers-and-porting--part-2.md), [Part 3](phone-numbers-and-porting--part-3.md), [Part 4](phone-numbers-and-porting--part-4.md), [Part 5](phone-numbers-and-porting--part-5.md), [Part 7](phone-numbers-and-porting--part-7.md), [Part 8](phone-numbers-and-porting--part-8.md), [Part 9](phone-numbers-and-porting--part-9.md), [Part 10](phone-numbers-and-porting--part-10.md), [Part 11](phone-numbers-and-porting--part-11.md)*

This page consolidates Telnyx developer documentation covering phone number search, ordering, reservations, bulk and advanced orders, regulatory requirements, requirement groups, documents, port-in and port-out workflows, and the notifications and events that track them. It provides an end-to-end reference for purchasing numbers, fulfilling regulatory requirements, transferring numbers in and out of Telnyx, and monitoring the lifecycle of those operations via webhooks and events.

## Documents

The Documents API allows you to upload and manage files that are required for regulatory compliance, identity verification, and other services on your Telnyx account. Documents are commonly used when ordering phone numbers in countries that require proof of identity, proof of address, or other supporting documentation. Once uploaded, documents must be linked to a service (such as a number order or regulatory requirement) within 30 minutes, or they will be automatically deleted.

### Constraints

- Maximum file size is 20 MB.
- Maximum filename length is 512 characters.
- Filenames must contain only printable Unicode characters. Non-printable characters (control characters) are not allowed.
- Spaces in filenames are automatically removed.
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

When a document is attached to a service on your account, a document link is automatically created. You do not need to create these links manually. Use the [GET /document_links endpoint](https://developers.telnyx.com/api-reference/documents/list-all-document-links) to view which services a document is currently associated with. You can filter results by `document_id`, `linked_record_type`, or `linked_resource_id`.

## Port-in Orders

Port-in orders allow you to transfer existing phone numbers from another carrier to Telnyx. The porting process involves creating a draft order, providing required information and documents, and submitting the order for processing with the losing carrier. Port orders are processed asynchronously through coordination between Telnyx and the losing carrier. Processing times vary based on carrier, country, and phone number type—ranging from same-day for FastPort-eligible numbers to several weeks for international ports.

### Constraints

- Phone numbers must pass a portability check before creating a port order. Non-portable numbers will result in API errors.
- Port orders may be automatically split into multiple orders based on country, number type, SPID (for US/CA), and FastPort eligibility.
- Each split order must be updated and submitted independently.
- A Letter of Authorization (LOA) and recent invoice are required for most port orders.
- Requested FOC dates are not guaranteed—the losing carrier determines the actual activation date.

### Order Splitting

When you create a port order with multiple phone numbers, the API may split them into separate orders. Numbers are grouped based on:

- **Country**: Numbers from different countries are split into separate orders.
- **Number type**: Local, toll-free, and mobile numbers are processed separately.
- **SPID**: For US and CA numbers, numbers with different Service Provider IDs are split.
- **FastPort eligibility**: FastPort-eligible numbers are separated from standard port orders.

If your order is split, the API returns multiple port order IDs. You must complete and submit each order individually.

### How It Works

**Step 1: Check portability.** Use the [Portability check endpoint](https://developers.telnyx.com/api-reference/phone-number-porting/run-a-portability-check) to verify your numbers can be ported to Telnyx before creating an order. Phone numbers must be submitted in E.164 format. The response indicates whether each number is `portable` and includes additional details like `fast_portable` eligibility and `messaging_capable` status.

**Step 2: Create a draft port order.** Use the [Create porting order endpoint](https://developers.telnyx.com/api-reference/porting-orders/create-a-porting-order) to create a draft order with your phone numbers. The API validates the numbers and may split them into multiple orders. Each order is created in `draft` status.

**Step 3: Fulfill the porting order.** Use the [Edit porting order endpoint](https://developers.telnyx.com/api-reference/porting-orders/edit-a-porting-order) to provide the required information:

- **End user information**: The name and account details of the current account holder with the losing carrier.
- **Service address**: The address associated with the phone numbers being ported.
- **Regulatory requirements**: Documents and information required for the port, such as a Letter of Authorization (LOA) and recent invoice.
- **Phone number configuration**: Optionally assign a `connection_id`, `messaging_profile_id`, or `emergency_address_id` to apply settings to all ported numbers.
- **FOC date**: Select your requested firm order commitment (FOC) date.

**Step 4: Submit the port order.** Use the [Submit porting order endpoint](https://developers.telnyx.com/api-reference/porting-orders/submit-a-porting-order) to submit your order. The order transitions from `draft` to `in-process` status.

**Step 5: Monitor order progress.** Track your order status using the [Retrieve porting order endpoint](https://developers.telnyx.com/api-reference/porting-orders/retrieve-a-porting-order) or configure webhooks to receive status change notifications. If the order enters `exception` status, check the order comments for details about the rejection.
