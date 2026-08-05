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

*Part 6 of 8 — see also: [Part 1](branded-calling--part-1.md), [Part 2](branded-calling--part-2.md), [Part 3](branded-calling--part-3.md), [Part 4](branded-calling--part-4.md), [Part 5](branded-calling--part-5.md), [Part 7](branded-calling--part-7.md), [Part 8](branded-calling--part-8.md)*

Branded Calling is a Telnyx product (currently in beta, US-only) that displays a verified business identity — display name, logo, and call reason — on outbound calls instead of a bare number or "Spam Likely". The feature is built on a CTIA-managed industry registry and uses SHAKEN PASSporT tokens to deliver rich call data to supported carriers and devices. This page covers the full lifecycle: registering an Enterprise, accepting the Branded Calling Terms of Service, activating the product, creating and vetting a Display Identity Record (DIR), attaching phone numbers in batches, configuring call reasons, handling infringement claims, and pricing.

## Infringement Claims

If a third party believes your DIR's display name, logo, or content infringes on a protected right (trademark, copyright, etc.), they can file an **infringement claim** through Telnyx. Claims are filed and adjudicated by Telnyx; you cannot create a claim through this API, but you can read and contest claims filed against your own DIRs.

For infringement issues, please mail [brand-infringement@telnyx.com](mailto:brand-infringement@telnyx.com).

While a claim is `pending` or `contested`:

- The DIR is moved to `suspended`.
- Branded calling pauses for the affected DIR.
- You **cannot add phone numbers** to the DIR (returns `400`).
- You **cannot delete** the DIR (returns `409`, blocked by the `no_active_claims` precondition).
- You **cannot re-submit** the DIR with `POST /submit` (returns `409` with the open claim IDs, blocked by the `no_active_claims` precondition).
- To revise content while the claim is open, call `PUT /v2/dir/{dir_id}/infringement_update` on the `suspended` DIR (see "Fix-and-resubmit" below). This is the only way to re-vet during an open claim.

### Claim lifecycle

```
pending ──► contested  (you submit a contest)
        ──► resolved   (Telnyx admin adjudicates)

resolved.resolution = upheld   ──► your DIR moves to permanently_rejected (terminal); the live registration and phone-number registrations are torn down. The DIR cannot be recovered; create a new DIR with corrected content.
resolved.resolution = rejected ──► claim is dismissed; if your DIR was suspended for the claim, it is restored to verified and branded calling resumes.
resolved.resolution = modified ──► partial outcome; DIR status is unchanged by the resolve, see resolution_notes for required follow-up.
```

### API endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/v2/dir/{dir_id}/infringement_claims` | List claims against a DIR |
| `GET` | `/v2/infringement_claims/{claim_id}` | Get a single claim |
| `POST` | `/v2/infringement_claims/{claim_id}/contest` | File a contest |

### List claims on a DIR

```
curl -g "https://api.telnyx.com/v2/dir/{dir_id}/infringement_claims?page[size]=20" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Get a single claim

```
curl https://api.telnyx.com/v2/infringement_claims/{claim_id} \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Contest a claim

You can submit a contest more than once — the first submission moves the claim from `pending` to `contested`; later submissions append additional notes and documents to the same claim without changing status.

```
curl -X POST https://api.telnyx.com/v2/infringement_claims/{claim_id}/contest \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contest_notes": "Acme Plumbing LLC has been operating under this name since 2008, predating the cited trademark filing. Attached: trademark search results and our state business registration.",
    "documents": [
      {
        "document_id": "d1e2f3a4-573d-446d-b3ce-aff9117272a6",
        "document_type": "trademark_registration",
        "description": "Our 2008 state trademark registration."
      }
    ]
  }'
```

| Field | Required | Description |
| --- | --- | --- |
| `contest_notes` | yes | 10-2000 characters. Explain why the claim is invalid or how you've addressed it. |
| `documents` | no | Up to 20 supporting documents per submission. Each must reference a `document_id` from the [Telnyx Documents API](/api-reference/documents/upload-a-document) and include a `document_type`. Duplicate `document_id`s within one submission are rejected. |

Contesting a `resolved` claim returns `400`.

### Fix-and-resubmit a suspended DIR

While an infringement claim is open (`pending` or `contested`), Telnyx may pre-emptively move your DIR to `suspended` to halt branded calling. To recover **without waiting for the claim to be resolved**, use the dedicated `PUT /v2/dir/{dir_id}/infringement_update` endpoint to atomically apply your content fix and re-submit for vetting in one call. This endpoint requires an active (unresolved) claim and a `suspended` DIR.

```
curl -X PUT https://api.telnyx.com/v2/dir/{dir_id}/infringement_update \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "display_name": "Acme Local Plumbing",
    "logo_url": "https://acmeplumbing.example.com/logo-v2-256.bmp",
    "certify_no_infringement": true,
    "certify_brand_is_accurate": true,
    "certify_no_shaft_content": true,
    "certify_ip_ownership": true,
    "infringement_resolution_notes": "Renamed to Acme Local Plumbing and replaced the logo so the new display identity no longer reads on the cited trademark.",
    "documents": [
      {
        "document_id": "550e8400-e29b-41d4-a716-446655440000",
        "document_type": "trademark_registration",
        "description": "Registration proving we own the revised name."
      }
    ]
  }'
```

Requirements:

- The DIR must have an active (unresolved) infringement claim.
- The DIR must be in `suspended` status.
- All four certifications (`certify_no_infringement`, `certify_brand_is_accurate`, `certify_no_shaft_content`, `certify_ip_ownership`) must be supplied as `true`.
- `infringement_resolution_notes` is required (10-500 chars); explain how the edits resolve the claim.

The content fields (`display_name`, `logo_url`, `call_reasons`) are all optional; send only the ones you're changing. You can also attach supporting `documents` (up to 20, append-only) as proof that backs your fix, for example authorization or licensing paperwork. Each entry references a `document_id` from the [Telnyx Documents API](/api-reference/documents/upload-a-document) plus a `document_type`, and re-attaching a document already on the DIR is rejected.

After the update, the DIR moves to `submitted` and goes through vetting again, even though the claim is still open. If the new content passes vetting, the DIR returns to `verified` and the claim can be resolved. If vetting rejects the changes, the DIR returns to `suspended` and you can update again. You can submit `infringement_update` multiple times while the claim is open.

> **Why the standard `PATCH` + `POST /submit` flow doesn't work here:** `POST /submit` is gated by the FSM's `no_active_claims` precondition and returns `409` while a claim is still `pending` or `contested`. `PUT /infringement_update` is the only customer-callable endpoint that can move a `suspended`-with-open-claim DIR back into vetting; it bypasses the `no_active_claims` gate by design. Use `PATCH` + `POST /submit` only after Telnyx has marked the claim `resolved` with `resolution = modified`. `resolution = rejected` auto-restores the DIR and `resolution = upheld` is terminal; neither requires a customer `PATCH` + `/submit`.

### After the claim resolves

- **`resolution = rejected`**: your DIR is automatically restored to `verified`; no action required. Branded calling resumes.
- **`resolution = upheld`**: your DIR is `permanently_rejected` and cannot be reused. To continue branded calling, create a **new** DIR with corrected content; you may reuse the same enterprise.
- **`resolution = modified`**: read `resolution_notes` for the required content edits, then `PATCH` the DIR and `POST /submit` (the `no_active_claims` gate is now open because the claim is `resolved`).
