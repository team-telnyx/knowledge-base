---
title: Toll-Free Verification
summary: Telnyx toll-free verification requires Business Registration Number (BRN)
  fields for all new submissions starting February 17, 2026. This page covers the
  required and optional fields, API usage for creating, retrieving, and updating verification
  requests, common rejection reasons, the resubmission process, delivery troubleshooting,
  and guidance on choosing between toll-free and 10DLC messaging.
sources:
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/index
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/troubleshooting
updated_at: 2026-08-05T13:58:33Z
---

# Toll-Free Verification

*Part 5 of 6 — see also: [Part 1](toll-free-verification--part-1.md), [Part 2](toll-free-verification--part-2.md), [Part 3](toll-free-verification--part-3.md), [Part 4](toll-free-verification--part-4.md), [Part 6](toll-free-verification--part-6.md)*

Telnyx toll-free verification requires Business Registration Number (BRN) fields for all new submissions starting February 17, 2026. This page covers the required and optional fields, API usage for creating, retrieving, and updating verification requests, common rejection reasons, the resubmission process, delivery troubleshooting, and guidance on choosing between toll-free and 10DLC messaging.

## Resubmission Process

After a rejection, you can fix the issues and resubmit. There's no limit on resubmission attempts.

1. **Read the rejection reason carefully**

   Check your verification status via API or the [Telnyx portal](https://portal.telnyx.com/#/app/messaging/toll-free-verification). The rejection reason tells you exactly what to fix.

   ```
   curl -s https://api.telnyx.com/v2/tollFreeVerification/requests/{requestId} \
     -H "Authorization: Bearer $TELNYX_API_KEY" | python3 -m json.tool
   ```

2. **Fix the identified issues**

   Update only the fields that caused the rejection. Use PATCH to update specific fields:

   ```
   curl -X PATCH https://api.telnyx.com/v2/tollFreeVerification/requests/{requestId} \
     -H "Authorization: Bearer $TELNYX_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{
     "businessName": "Corrected Legal Name LLC",
     "messageVolume": "10000",
     "useCaseSummary": "Updated description of our messaging use case...",
     "sampleMessage1": "Updated sample with opt-out. Reply STOP to unsubscribe.",
     "sampleMessage2": "Another realistic sample. Reply STOP to opt out."
   }'
   ```

3. **Resubmit for review**

   After updating, the verification automatically enters the review queue again. No separate "submit" action is needed — the PATCH triggers re-review.

4. **Monitor status via webhooks**

   Set up webhooks to get notified when the review completes:

   ```
   from flask import Flask, request, jsonify

   app = Flask(__name__)

   @app.route("/webhooks/toll-free", methods=["POST"])
   def handle_toll_free_webhook():
       event = request.json
       event_type = event.get("data", {}).get("event_type", "")

       if event_type == "toll_free_verification.status_update":
           payload = event["data"]["payload"]
           status = payload["status"]
           request_id = payload["id"]

           if status == "verified":
               print(f"✅ Verification {request_id} approved!")
               # Enable full messaging for this number
           elif status == "rejected":
               reason = payload.get("rejectionReason", "No reason provided")
               print(f"❌ Verification {request_id} rejected: {reason}")
               # Alert team, prepare resubmission

       return jsonify({"status": "ok"}), 200
   ```

### Resubmission Tips

| Do | Don't |
| --- | --- |
| Fix **only** the cited rejection reason | Change everything at once |
| Use exact legal business name | Use informal names or abbreviations |
| Provide realistic sample messages | Use generic placeholder text |
| Include opt-out in every sample | Assume opt-out is implied |
| Wait for the full review cycle | Submit multiple times in rapid succession |

## Delivery Issues After Verification

Even after successful verification, you may experience delivery problems.

### Throughput Limitations

| Verification status | Throughput | Notes |
| --- | --- | --- |
| **Unverified** | ~0.25 MPS | Heavy carrier filtering, low reliability |
| **Pending review** | ~1 MPS | Some filtering may apply |
| **Verified** | Up to 20 MPS | Full throughput, minimal filtering |

Sending above your throughput tier results in message queuing and eventual `40014` (Expired in queue) errors. If you need more than 20 MPS from toll-free numbers, consider using short codes or 10DLC with number pools.

### Common Delivery Errors

**40002 — Blocked as spam (even after verification)**

- **Cause**: Message content triggered carrier-level content filters, independent of verification status.
- **Fix**:
  1. Review message content for spam trigger words (FREE, WINNER, ACT NOW)
  2. Avoid URL shorteners (bit.ly, tinyurl) — use full URLs or Telnyx URL shortening
  3. Don't send identical messages to many recipients in rapid succession
  4. Check if recipient has previously opted out
  5. Review the error code reference for specific guidance

**40005 — Destination number unreachable**

- **Cause**: The recipient number is invalid, deactivated, or not SMS-capable.
- **Fix**:
  1. Validate numbers before sending (use Number Lookup API)
  2. Remove landlines and VoIP numbers that don't support SMS
  3. Check for typos in the recipient number

**40011 — Rate limit exceeded**

- **Cause**: Sending faster than your verified throughput allows.
- **Fix**:
  1. Implement client-side rate limiting
  2. Spread traffic across multiple toll-free numbers if needed
  3. Use a messaging profile with number pooling for high-volume use cases

**40014 — Message expired in queue**

- **Cause**: Message sat in the queue too long, usually due to throughput congestion.
- **Fix**:
  1. Reduce sending rate to stay within throughput limits
  2. Check if a carrier outage is causing delivery backlog
  3. For time-sensitive messages, set a shorter validity period

**Messages delivering but not received by all carriers**

- **Cause**: Some carriers may still filter your toll-free traffic even after verification, especially for:
  - New verifications (carrier trust builds over time)
  - Content that resembles spam patterns
  - High complaint rates from recipients
- **Fix**:
  1. Start with lower volumes and ramp up gradually over 1–2 weeks
  2. Monitor delivery rates per carrier using MDRs
  3. Ensure opt-out is working properly (high complaint rates trigger filtering)
  4. Contact Telnyx support if specific carriers consistently filter your traffic

## Checking Verification Status

### Via API

```
# Get status of a specific verification
curl -s https://api.telnyx.com/v2/tollFreeVerification/requests/{requestId} \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  | python3 -c "
import sys, json
data = json.load(sys.stdin)['data']
print(f\"Status: {data['status']}\")
print(f\"Phone numbers: {', '.join(data.get('phoneNumbers', []))}\")
if data.get('rejectionReason'):
    print(f\"Rejection reason: {data['rejectionReason']}\")
"

# List all verifications
curl -s "https://api.telnyx.com/v2/tollFreeVerification/requests?page[size]=25" \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  | python3 -c "
import sys, json
data = json.load(sys.stdin)['data']
for req in data:
    numbers = ', '.join(req.get('phoneNumbers', []))
    print(f\"{req['id']} | {req['status']:12} | {numbers}\")
"
```

### Via Portal

1. Log in to the [Telnyx Portal](https://portal.telnyx.com)
2. Navigate to **Messaging** → **Toll-Free Verification**
3. View status, rejection reasons, and submission details for each verification

### Status Reference

| Status | Meaning | Action needed |
| --- | --- | --- |
| `draft` | Created but not yet submitted | Complete required fields and submit |
| `pending` | Under carrier review | Wait (1–2 weeks typical) |
| `verified` | Approved ✅ | None — full throughput unlocked |
| `rejected` | Carrier rejected ❌ | Fix issues and resubmit |
