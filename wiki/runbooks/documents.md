---
title: Documents
summary: Upload and manage documents used for regulatory requirements and identity verification.
sources:
  - url: https://developers.telnyx.com/docs/numbers/phone-numbers/documents/index
    content_hash: 886bdc93da271da3b6a8aae05cdbbc9d661de18ea7359b36d8102c8158107a06
updated_at: 2026-04-10T00:00:00Z
---

# Documents

Upload and manage documents used for regulatory requirements and identity verification

## Overview

The Documents API allows you to upload and manage files that are required for regulatory compliance, identity verification, and other services on your Telnyx account. Documents are commonly used when ordering phone numbers in countries that require proof of identity, proof of address, or other supporting documentation.

Once uploaded, documents must be linked to a service (such as a number order or regulatory requirement) within 30 minutes, or they will be automatically deleted. This ensures that only actively used documents are retained on your account.

You can upload documents by sending base64-encoded file content or by uploading the file directly via multipart form data.

## Constraints

* Maximum file size is **20 MB**.
* Maximum filename length is **512 characters**.
* Filenames must contain only **printable Unicode characters**. Non-printable characters (control characters) are not allowed.
* Spaces in filenames are **automatically removed**. For example, `my document.pdf` becomes `mydocument.pdf`.
* The file extension is **automatically appended** based on the detected MIME type, even if omitted from the filename.
* Uploaded documents must be **linked to a service within 30 minutes** or they will be automatically deleted.
* Documents that are linked to a service **cannot be deleted** until they are unlinked.
* All uploaded documents are scanned for malware. Documents flagged as infected will be denied.

## Accepted file types

The following file types are accepted for upload:

| File type     | MIME type                                                                 |
| :------------ | :------------------------------------------------------------------------ |
| PDF           | `application/pdf`                                                         |
| PNG           | `image/png`                                                               |
| JPEG          | `image/jpeg`                                                              |
| CSV           | `text/csv`, `application/csv`                                             |
| Plain text    | `text/plain`                                                              |
| JSON          | `application/json`                                                        |
| Word (.docx)  | `application/vnd.openxmlformats-officedocument.wordprocessingml.document` |
| Word (.doc)   | `application/msword`                                                      |
| Excel (.xlsx) | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`       |
| Excel (.xls)  | `application/vnd.ms-excel`                                                |

## Upload methods

Documents can be uploaded using any of three methods through the [POST /documents endpoint](https://developers.telnyx.com/api-reference/documents/upload-a-document):

* **Base64**: Provide the file content as a base64-encoded string in the `file` field, along with a `filename`.
* **Multipart form data**: Upload the file directly as binary data using `multipart/form-data`.

You can optionally include a `customer_reference` with any upload method to associate your own tracking identifier with the document.

## Antivirus scan statuses

All uploaded documents are scanned for malware. The `av_scan_status` field indicates the scan result:

| Status         | Description                                             |
| :------------- | :------------------------------------------------------ |
| `pending_scan` | The document is queued for scanning.                    |
| `scanned`      | The scan completed and no threats were detected.        |
| `infected`     | The scan detected malware. The document will be denied. |
| `not_scanned`  | The document has not yet been scanned.                  |

## Document links

When a document is attached to a service on your account (such as a number order or regulatory requirement), a document link is automatically created. You do not need to create these links manually — they are managed by the services that use the document.

You can use the [GET /document\_links endpoint](https://developers.telnyx.com/api-reference/documents/list-all-document-links) to view which services a document is currently associated with. You can filter results by `document_id`, `linked_record_type`, or `linked_resource_id`.
