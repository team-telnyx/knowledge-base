---
title: 'Phone Number Ordering: Search, Reserve, Order, and Compliance'
summary: A consolidated guide to finding, reserving, and purchasing Telnyx phone numbers,
  including regulatory requirements, requirement groups, action-based verifications,
  documents, advanced orders, bulk ordering, statuses, deadlines, notifications, and
  post-activation steps.
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
updated_at: 2026-05-20T09:21:49Z
---

# Phone Number Ordering: Search, Reserve, Order, and Compliance

*Part 2 of 2 — see also: [Part 1](phone-number-ordering-search-reserve-order-and-compliance--part-1.md)*

A consolidated guide to finding, reserving, and purchasing Telnyx phone numbers, including regulatory requirements, requirement groups, action-based verifications, documents, advanced orders, bulk ordering, statuses, deadlines, notifications, and post-activation steps.

## Documents API for Compliance

Use Documents to upload files required for regulatory proofs.

Constraints
- Max file size 20 MB; filename up to 512 characters; printable Unicode only.
- Spaces are removed from filenames; file extensions appended based on MIME type.
- Must link the uploaded document to a service within 30 minutes or it’s deleted.
- Linked documents cannot be deleted until unlinked.
- All uploads are malware-scanned; infected files are denied.

Accepted types
- PDF, PNG, JPEG, CSV, TXT, JSON, DOCX, DOC, XLSX, XLS.

Upload methods (POST /documents)
- Base64 body with filename, or multipart/form-data. Optional customer_reference for your tracking.

Antivirus scan statuses
- pending_scan, scanned, infected, not_scanned.

Document links
- Links are created automatically when attaching to services (e.g., orders/requirements). Use GET /document_links to see associations.

References
- Guide: https://developers.telnyx.com/docs/numbers/phone-numbers/documents
- Upload API: https://developers.telnyx.com/api-reference/documents/upload-a-document

## Advanced Orders (When No Inventory Matches)

Use Advanced Orders when Telnyx has coverage but no numbers match your search.

Constraints
- Not for US/CA toll-free.
- Not for unique/vanity pattern requests.
- Best-effort; procurement not guaranteed.

Statuses
- pending, processing, exception, hold, ordered, failed.

Process
- If searches return no results, create an advanced order: POST v2/advanced_orders (use the same criteria you searched).
- Provide regulatory requirements via a matching requirement group: PATCH v2/advanced_orders/{id}/requirement_group.
- When status is ordered, check the orders array for created number orders, then manage them as standard orders (retrieve details, fulfill any remaining requirements).

Collaboration and notifications
- Comments with comment_record_type=advanced_number_order.
- Configure email/webhook notifications for status updates.
- Webhooks include advanced_order.status_update transitions and advanced_order.new_comment.

References
- Guide: https://developers.telnyx.com/docs/numbers/phone-numbers/advanced-orders
- Create API: https://developers.telnyx.com/api-reference/advanced-number-orders/create-advanced-order

## Bulk Number Orders (US/CA)

Bulk (inexplicit) orders let you specify criteria and quantity; Telnyx searches, reserves, and orders asynchronously.

Constraints
- US and CA only.
- Up to 10,000 numbers per bulk order.
- Procures what’s available at processing time; availability not guaranteed (use inventory coverage beforehand when supported).

Ordering groups and statuses
- One bulk order can contain multiple ordering groups with independent filters and progress.
- Group statuses: pending, processing, success, partial_success, failed.

Process
- Create: POST v2/inexplicit_number_orders with one or more ordering_groups (country_iso, count_requested, phone_number_type). Optional filters. Strategy: always (default) or never when inventory is insufficient. Optional connection_id, messaging_profile_id, billing_group_id, customer_reference to auto-apply settings.
- Monitor: GET v2/inexplicit_number_orders and GET v2/inexplicit_number_orders/{id}. Track status and compare count_allocated vs count_requested per group.
- Access created orders: the orders array lists number_order_id and sub_number_order_ids. Manage them using standard order APIs.

Notifications
- Configure notifications. Webhooks are emitted by the underlying number orders created by the bulk order (not by the bulk order object itself).

References
- Guide: https://developers.telnyx.com/docs/numbers/phone-numbers/bulk-ordering

## Ordering via Mission Control Portal

- Portal path: Real-Time Communication > Numbers > Buy Numbers.
- Choose country, features (SMS, Voice, Fax), number type, region, and area code; search and add to cart; place order.

Reference
- https://developers.telnyx.com/docs/numbers/phone-numbers/buy-phone-number

## Order and Phone Number Statuses, Deadlines, and Cancellations

Order/sub-order statuses
- pending: created and processing; numbers not yet active.
- success: completed; numbers activated.
- failure: issue with the order.
- cancelled: cancelled by you or Telnyx.
- deleted: numbers deleted from the account.

While an order is pending, individual phone numbers can be:
- requirement-info-pending: missing requirement values.
- requirement-info-under-review: values supplied; awaiting review.
- requirement-info-exception: one/more requirements rejected.
- approved: all requirements approved.
- deleted: numbers removed from the account.

Deadlines and auto-cancellation
- Each order has a deadline to provide all requirements. Missing the deadline auto-cancels the order.
- If requirements are rejected, a new deadline is set. Deadlines can be extended upon request via order comments.

## Notifications and Comments

- Configure email and webhook notifications for number orders, requirement groups, advanced orders, and (indirectly) bulk orders.
- Use the Comments API to collaborate with Telnyx:
  - For advanced orders: filter comment_record_type=advanced_number_order and set comment_record_id to the advanced order ID.
  - For requirement groups: comment_record_type=requirement_group and comment_record_id to the group ID.
  - For number orders: standard comments endpoints are available.

References
- Notification settings: https://support.telnyx.com/en/articles/4277896-notification-settings
- Comments API: https://developers.telnyx.com/api-reference/phone-number-orders/retrieve-all-comments

## Next Steps After Activation

- Voice: assign the number to a SIP Connection or Voice API Application.
- Messaging: assign a Messaging Profile.
- Fax: configure the Fax Application settings.

Reference
- https://developers.telnyx.com/docs/numbers/phone-numbers/buy-phone-number
