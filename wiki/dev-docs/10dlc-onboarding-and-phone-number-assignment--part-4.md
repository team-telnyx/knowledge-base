---
title: 10DLC Onboarding and Phone Number Assignment
summary: Comprehensive guide to registering brands, vetting, creating campaigns, and
  assigning phone numbers for 10DLC A2P messaging on Telnyx — covering both direct
  customer and ISV/reseller architectures, plus bulk operations, webhooks, appeals,
  and troubleshooting.
sources:
- url: https://developers.telnyx.com/docs/messaging/10dlc/isv-reseller-onboarding
- url: https://developers.telnyx.com/docs/messaging/10dlc/phone-number-assignment
- url: https://developers.telnyx.com/docs/messaging/10dlc/quickstart/index
updated_at: 2026-08-05T13:48:57Z
---

# 10DLC Onboarding and Phone Number Assignment

*Part 4 of 5 — see also: [Part 1](10dlc-onboarding-and-phone-number-assignment--part-1.md), [Part 2](10dlc-onboarding-and-phone-number-assignment--part-2.md), [Part 3](10dlc-onboarding-and-phone-number-assignment--part-3.md), [Part 5](10dlc-onboarding-and-phone-number-assignment--part-5.md)*

Comprehensive guide to registering brands, vetting, creating campaigns, and assigning phone numbers for 10DLC A2P messaging on Telnyx — covering both direct customer and ISV/reseller architectures, plus bulk operations, webhooks, appeals, and troubleshooting.

## Managing customers at scale

### Multi-tenant architecture patterns

**Pattern 1: One brand + campaign per customer (recommended)** — Best for agencies and resellers managing distinct businesses. Each customer gets their own brand and campaign, providing isolated throughput per customer, independent compliance status, and clear separation for TCR. Trade-off: more registration overhead, but better isolation.

```
Your Platform Account
├── Customer A → Brand A → Campaign A → Numbers [+1xxx, +1yyy]
├── Customer B → Brand B → Campaign B → Numbers [+1zzz]
└── Customer C → Brand C → Campaign C → Numbers [+1www, +1vvv]
```

**Pattern 2: Shared campaign across customers** — Best for SaaS platforms where all customers send similar message types. One brand (yours) with shared campaigns. All customers' traffic flows through the same campaign. Trade-off: simpler setup, but throughput is shared and one customer's violations affect all.

```
Your Platform Account
└── Your Brand → Shared Campaign → Numbers [+1xxx, +1yyy, +1zzz]
    ├── Customer A traffic
    ├── Customer B traffic
    └── Customer C traffic
```

**Pattern 3: Hybrid (recommended for growth)** — Best for platforms with a mix of high-volume and low-volume customers. High-volume customers get dedicated brands + campaigns; low-volume customers share a platform campaign. Migrate customers to dedicated as they grow.

```
Your Platform Account
├── Platform Brand → Shared Campaign → [low-volume customers]
├── Big Customer A → Brand A → Campaign A → [dedicated numbers]
└── Big Customer B → Brand B → Campaign B → [dedicated numbers]
```

### Bulk brand registration

For platforms onboarding many customers, automate brand registration:

```python
import telnyx
import os
import time

telnyx.api_key = os.environ["TELNYX_API_KEY"]

customers = [
    {
        "company_name": "Acme Corp LLC",
        "ein": "12-3456789",
        "email": "admin@acme.com",
        "website": "https://acme.com",
        "phone": "+12025550001",
    },
    {
        "company_name": "Widget Inc",
        "ein": "98-7654321",
        "email": "admin@widget.com",
        "website": "https://widget.com",
        "phone": "+12025550002",
    },
]

results = []
for customer in customers:
    try:
        brand = telnyx.Brand.create(
            entity_type="PRIVATE_PROFIT",
            company_name=customer["company_name"],
            ein=customer["ein"],
            ein_issuing_country="US",
            phone=customer["phone"],
            street="123 Main St",
            city="New York",
            state="NY",
            postal_code="10001",
            country="US",
            email=customer["email"],
            website=customer["website"],
            vertical="TECHNOLOGY",
            display_name=customer["company_name"].split()[0],
        )
        results.append({"customer": customer["company_name"], "brand_id": brand.id, "status": "created"})
        print(f"✓ {customer['company_name']}: Brand {brand.id}")
        time.sleep(0.5)  # Rate limit courtesy
    except Exception as e:
        results.append({"customer": customer["company_name"], "error": str(e)})
        print(f"✗ {customer['company_name']}: {e}")

print(f"\nRegistered {sum(1 for r in results if 'brand_id' in r)}/{len(customers)} brands")
```

### Webhook monitoring for partner campaigns

Set up webhooks to track campaign status changes across all your customers:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhooks/10dlc", methods=["POST"])
def handle_10dlc_webhook(self):
    event = request.json
    event_type = event.get("data", {}).get("event_type", "")

    if event_type == "campaign.status_update":
        campaign_id = event["data"]["payload"]["campaignId"]
        new_status = event["data"]["payload"]["campaignStatus"]
        print(f"Campaign {campaign_id} → {new_status}")

        if new_status == "ACTIVE":
            # Campaign approved — notify customer, assign numbers
            activate_customer_messaging(campaign_id)
        elif new_status == "REJECTED":
            # Campaign rejected — notify customer with reason
            reason = event["data"]["payload"].get("rejectionReason", "Unknown")
            notify_customer_rejection(campaign_id, reason)

    elif event_type == "brand.status_update":
        brand_id = event["data"]["payload"]["brandId"]
        identity_status = event["data"]["payload"]["identityStatus"]
        print(f"Brand {brand_id} → {identity_status}")

    return jsonify({"status": "ok"}), 200
```

## Partner campaign appeals

When a shared campaign is rejected, the appeal process differs from native campaigns. Partner campaigns use a **CSP nudge mechanism**:

1. **Review the rejection reason** — Check the campaign status and rejection details via your upstream CSP.
2. **Fix the issue** — Update the campaign details (description, samples, message flow) at your upstream CSP based on the rejection reason.
3. **Trigger a CSP nudge** — Your upstream CSP sends a `CAMPAIGN_NUDGE` event to TCR, which triggers a re-review. The nudge mechanism is **only available for partner campaigns**. Native campaigns use the direct appeal API. See [10DLC Event Notifications](10dlc-event-notifications.md) for details.
4. **Monitor for approval** — Set up webhooks to receive campaign status updates automatically.

## Compliance checklist for ISVs

ISVs have **additional compliance responsibilities** because you are sending on behalf of customers. TCR and carriers hold you accountable for your customers' messaging practices.

- **Customer vetting** — Verify your customers' business legitimacy before registration.
- **Content monitoring** — Monitor message content for compliance with campaign use case.
- **Opt-in verification** — Ensure customers collect proper consent from end users.
- **Opt-out processing** — STOP/HELP keywords must work across all customer traffic.
- **Volume management** — Don't exceed throughput limits for your campaign's vetting score.
- **Incident response** — Have a process to quickly disable a customer's messaging if they violate policies.
- **Record retention** — Keep opt-in records for at least 4 years per CTIA guidelines.
- **Sample message accuracy** — Registered samples must match actual production messages.
