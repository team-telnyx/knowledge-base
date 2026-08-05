---
title: Sole Proprietor 10DLC Registration
summary: Sole Proprietor registration enables individuals and small businesses without
  a federal Tax ID (EIN) to register for 10DLC messaging. This page covers the API
  workflow for creating Sole Proprietor brands, completing OTP verification, and managing
  campaigns programmatically, along with troubleshooting guidance for common failures.
sources:
- url: https://developers.telnyx.com/docs/messaging/10dlc/sole-proprietor/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/troubleshooting/index
updated_at: 2026-08-05T13:49:22Z
---

# Sole Proprietor 10DLC Registration

*Part 6 of 7 — see also: [Part 1](sole-proprietor-10dlc-registration--part-1.md), [Part 2](sole-proprietor-10dlc-registration--part-2.md), [Part 3](sole-proprietor-10dlc-registration--part-3.md), [Part 4](sole-proprietor-10dlc-registration--part-4.md), [Part 5](sole-proprietor-10dlc-registration--part-5.md), [Part 7](sole-proprietor-10dlc-registration--part-7.md)*

Sole Proprietor registration enables individuals and small businesses without a federal Tax ID (EIN) to register for 10DLC messaging. This page covers the API workflow for creating Sole Proprietor brands, completing OTP verification, and managing campaigns programmatically, along with troubleshooting guidance for common failures.

## Troubleshooting

### Sole Proprietor OTP Verification Failure

**Error:** OTP verification timed out or failed.
**Root cause:** The one-time password sent to your registered phone number wasn't confirmed in time, or the phone number can't receive SMS.
**Fix:**

1. Ensure the phone number on file can receive SMS
2. Request a new OTP and complete verification within the time window
3. Check that the phone number matches your identity documents

### Brand Status Reference

The `identityStatus` field on a brand object indicates the verification result. For Sole Proprietor brands, the relevant status is `SELF_DECLARED` (limited verification) once the OTP flow completes.

| Status | Meaning |
| --- | --- |
| `VERIFIED` | Brand identity confirmed |
| `UNVERIFIED` | Verification failed — action required |
| `VETTED_VERIFIED` | External vetting completed successfully |
| `SELF_DECLARED` | Sole proprietor — limited verification |

### Check Brand Status via API

```
import telnyx

telnyx.api_key = "YOUR_API_KEY"

brand = telnyx.TenDlcBrand.retrieve("BRAND_ID")
print(f"Status: {brand.identityStatus}")
print(f"Entity Type: {brand.entityType}")

if brand.identityStatus == "UNVERIFIED":
    print("⚠ Brand verification failed. Check rejection reason and update brand info.")
```

```
const telnyx = require("telnyx")("YOUR_API_KEY");

const brand = await telnyx.tenDlcBrands.retrieve("BRAND_ID");
console.log(`Status: ${brand.data.identityStatus}`);

if (brand.data.identityStatus === "UNVERIFIED") {
  console.log("⚠ Brand verification failed. Check rejection reason and update brand info.");
}
```

```
curl -s https://api.telnyx.com/v2/10dlc/brand/BRAND_ID \
  -H "Authorization: Bearer $TELNYX_API_KEY" | python3 -m json.tool
```

### Campaign Rejection Reasons

Campaign rejections happen during carrier review. The rejection reason is delivered via [10DLC Event Notifications](10dlc-event-notifications.md) webhooks.

| Rejection Reason | Common Cause | Fix |
| --- | --- | --- |
| **Samples don't match use case** | Sample messages describe a different use case than declared | Rewrite samples to match the exact declared use case |
| **Missing opt-out language** | No STOP/unsubscribe instructions in samples | Add "Reply STOP to unsubscribe" to every sample |
| **Inadequate opt-in description** | Opt-in workflow is vague or missing | Describe the exact opt-in mechanism (web form URL, keyword, etc.) |
| **Prohibited content** | SHAFT content (sex, hate, alcohol, firearms, tobacco) or cannabis | Remove prohibited content or apply for special use case approval |
| **Brand not vetted** | Campaign submitted before brand vetting completed | Complete brand vetting first |
| **Duplicate campaign** | Similar campaign already registered for this brand | Use the existing campaign or differentiate the use case |
| **Insufficient sample messages** | Not enough variety in sample messages | Provide 2–5 diverse samples showing different message types |

### Writing Samples That Pass Review

1. **Match your declared use case exactly.** If you registered as "Customer Care," every sample should be a customer service message.
2. **Include opt-out in every sample.** Every sample message should include opt-out instructions.
3. **Use realistic content — no placeholders.** Carriers reject generic or placeholder text.
4. **Show variety in your samples.** Provide 2–5 samples that demonstrate different message types within your use case (confirmations, follow-ups, status updates, opt-in confirmations).

### Resubmitting After Rejection

You cannot edit a rejected campaign. Create a new one with corrected information:

```
import telnyx

telnyx.api_key = "YOUR_API_KEY"

# Create a new campaign with corrected samples
campaign = telnyx.TenDlcCampaign.create(
    brandId="BRAND_ID",
    usecase="CUSTOMER_CARE",
    description="Customer support notifications for order updates and ticket resolution",
    sample1="Hi Jane, your support ticket #4521 has been resolved. Let us know if you need anything else. Reply STOP to opt out.",
    sample2="Your order #8876 is out for delivery and should arrive by 3 PM today. Reply STOP to unsubscribe.",
    messageFlow="Customers opt in via checkbox on our website checkout page at https://example.com/checkout. They can opt out at any time by replying STOP.",
    helpMessage="Reply HELP for support options or visit https://example.com/help",
    optoutMessage="You have been unsubscribed and will no longer receive messages from us."
)

print(f"New campaign ID: {campaign.id}")
print(f"Status: {campaign.campaignStatus}")
```

Each campaign submission incurs a TCR registration fee ($15 standard / $4 low-volume). Review samples carefully before submitting to avoid repeated fees.

### Phone Number Assignment Failures

**Number not eligible for 10DLC.** The number may be a toll-free number (use toll-free verification instead), a short code, not provisioned for messaging, or already assigned to another campaign. Verify the number type with `GET /v2/phone_numbers/{id}`, ensure it's a standard long code (10-digit US number), enable messaging on the number if not already configured, and unassign from any existing campaign before reassigning.

**AT&T registration timeout.** AT&T's 10DLC registration system can be slow, especially during high-volume periods. Registration can take up to 7 business days. Wait 7 business days before escalating, check the number's registration status via webhooks or API, and contact Telnyx support if still pending after 7 days. AT&T processes 10DLC number registrations in batches; delays of 3–5 business days are normal.

**T-Mobile number rejection.** T-Mobile applies additional scrutiny to numbers with low-score brands or campaigns flagged for review. Ensure your brand vetting score is sufficient, verify the campaign isn't flagged or suspended, try reassigning the number after the campaign is fully approved, and contact Telnyx support if the issue persists.

### Message Delivery Failures

| Error Code | Description | Fix |
| --- | --- | --- |
| `40300` | Number not registered for 10DLC | Assign the sending number to an approved campaign |
| `40301` | Campaign suspended | Check campaign status; contact support if unexpected |
| `40302` | Brand suspended | Review brand status and resolve compliance issues |
| `40310` | Rate limit exceeded | Reduce sending rate; see [10DLC Rate Limits](10dlc-rate-limits.md) |
| `40311` | Daily message limit reached | Wait for daily reset or request higher throughput via vetting |
| `40320` | Content flagged by carrier | Review message content for SHAFT violations |
| `40321` | URL blocked by carrier | Remove or replace flagged URLs; use branded short links |

### Debugging Delivery Issues

```
import telnyx
import json

telnyx.api_key = "YOUR_API_KEY"

# Check message detail record for error info
mdr = telnyx.MessageDetailRecord.list(
    direction="outbound",
    phone_number="+12125551234",
    start_date="2026-03-01T00:00:00Z",
    end_date="2026-03-02T00:00:00Z"
)

for record in mdr.data:
    if record.status != "delivered":
        print(f"Message {record.id}")
        print(f"  Status: {record.status}")
        print(f"  Error: {record.errors}")
        print(f"  To: {record.to}")
        print(f"  Sent at: {record.created_at}")
```

```
const telnyx = require("telnyx")("YOUR_API_KEY");

const mdrs = await telnyx.messageDetailRecords.list({
  direction: "outbound",
  phone_number: "+12125551234",
  start_date: "2026-03-01T00:00:00Z",
  end_date: "2026-03-02T00:00:00Z",
});

for (const record of mdrs.data) {
  if (record.status !== "delivered") {
    console.log(`Message ${record.id}`);
    console.log(`  Status: ${record.status}`);
    console.log(`  Error: ${JSON.stringify(record.errors)}`);
  }
}
```

```
curl -s "https://api.telnyx.com/v2/message_detail_records?direction=outbound&phone_number=%2B12125551234&start_date=2026-03-01T00%3A00%3A00Z&end_date=2026-03-02T00%3A00%3A00Z" \
  -H "Authorization: Bearer $TELNYX_API_KEY" | python3 -m json.tool
```

### Carrier-Specific Issues

**AT&T**

- Registration delay: 3–7 business days for number registration
- Content filtering: Aggressive URL filtering; avoid URL shorteners (bit.ly, tinyurl)
- Rate limits: Lowest per-campaign limits; vetting score has largest impact
- Suspension: Will suspend campaigns with spam complaints without warning

**T-Mobile**

- Content filtering: Blocks messages with prohibited content patterns
- Number reassignment: Requires 24h cooldown when moving numbers between campaigns
- Daily limits: Enforces strict daily per-number limits
- Opt-out enforcement: Automatically blocks messages to numbers that texted STOP

**Verizon**

- Registration: Generally fastest registration processing
- Content: Less aggressive filtering than AT&T/T-Mobile
- Rate limits: More generous throughput at all vetting tiers

### Diagnostic Checklist

1. **Verify brand status.** `GET /v2/10dlc/brand/{brandId}` — confirm `identityStatus` is `VERIFIED` or `VETTED_VERIFIED`.
2. **Verify campaign status.** `GET /v2/10dlc/campaign/{campaignId}` — confirm `campaignStatus` is `ACTIVE`.
3. **Verify number assignment.** `GET /v2/10dlc/phoneNumberCampaign?phoneNumber={number}` — confirm the sending number is assigned to the active campaign.
4. **Check event notifications.** Review [10DLC Event Notifications](10dlc-event-notifications.md) webhooks for rejection, suspension, or status change events.
5. **Review message detail records.** Check MDRs for specific error codes on failed messages.
6. **Check rate limits.** Compare your sending rate against your campaign throughput limits. Vetting score determines your ceiling.
