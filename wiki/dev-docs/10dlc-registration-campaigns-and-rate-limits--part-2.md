---
title: 10DLC Registration, Campaigns, and Rate Limits
summary: A consolidated reference for registering a 10DLC brand and campaign with
  The Campaign Registry (TCR) through Telnyx, submitting for external vetting, and
  understanding how the resulting vetting score controls carrier throughput on AT&T,
  T-Mobile, and Verizon.
sources:
- url: https://developers.telnyx.com/docs/messaging/10dlc/10dlc-rate-limits/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/brand-registration/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/campaign-registration/index
updated_at: 2026-08-05T13:48:40Z
---

# 10DLC Registration, Campaigns, and Rate Limits

*Part 2 of 4 — see also: [Part 1](10dlc-registration-campaigns-and-rate-limits--part-1.md), [Part 3](10dlc-registration-campaigns-and-rate-limits--part-3.md), [Part 4](10dlc-registration-campaigns-and-rate-limits--part-4.md)*

A consolidated reference for registering a 10DLC brand and campaign with The Campaign Registry (TCR) through Telnyx, submitting for external vetting, and understanding how the resulting vetting score controls carrier throughput on AT&T, T-Mobile, and Verizon.

## Common rejection reasons and fixes

**EIN mismatch — company name doesn't match IRS records**

- **Cause:** The `companyName` field doesn't match what the IRS has on file for that EIN.
- **Fix:** Use your exact legal name as registered with the IRS. Check your EIN confirmation letter (CP 575) or search the [IRS tax-exempt organization database](https://www.irs.gov/charities-non-profits/tax-exempt-organization-search) for non-profits.

**Invalid EIN format**

- **Cause:** EIN must be in `XX-XXXXXXX` format (9 digits with a hyphen after the first 2).
- **Fix:** Double-check your EIN. It should look like `12-3456789`. Don't include spaces or extra characters.

**Website not accessible or doesn't match business**

- **Cause:** The vetting partner couldn't access your website, or the website content doesn't match the registered business.
- **Fix:** Ensure your website is live, publicly accessible (no authentication required), and has content that clearly identifies your business. The domain should ideally match your business email domain.

**Phone number not valid or not reachable**

- **Cause:** The business phone number provided is not a valid, reachable US/CA number.
- **Fix:** Provide a working business phone number in E.164 format (e.g., `+15551234567`). The number should be answerable during business hours.

**Address verification failed**

- **Cause:** The provided address doesn't match USPS records or can't be verified.
- **Fix:** Use your exact business address as registered. Verify it through [USPS address lookup](https://tools.usps.com/zip-code-lookup.htm).

**Duplicate brand — EIN already registered**

- **Cause:** A brand with this EIN is already registered (possibly by another CSP or a previous registration).
- **Fix:** You can only have one brand per EIN. If you previously registered through another provider, you may need to import or transfer the brand. Contact [Telnyx support](https://support.telnyx.com/) for assistance.

## Appeal process

If your brand is rejected or receives a low vetting score, you can appeal:

1. **Review the rejection reason** — Check the brand's `identityStatus` and any associated error messages via the API or [Mission Control Portal](https://portal.telnyx.com/#/app/messaging/10dlc/brands).
2. **Fix the identified issues** — Update your brand information to address the specific rejection reason using the update brand API.
3. **Re-submit for vetting** — After updating your brand, submit a new external vetting request. Each vetting submission incurs a fee.
4. **Contact support if needed** — For complex cases (EIN transfers, duplicate brands, identity disputes), contact [Telnyx support](https://support.telnyx.com/) with your `brandId` and details.

Re-vetting after fixing issues often results in a higher score. The most common improvement is ensuring your website, company name, and EIN all align.

## Campaign use case types

A 10DLC campaign defines your messaging use case — what you're sending, who you're sending to, and how recipients opted in. Every campaign must be registered with TCR and approved by mobile carriers before you can send messages at scale.

### Standard use cases

| Use Case | Description | Example |
| --- | --- | --- |
| `CUSTOMER_CARE` | Support and service messages | "Your ticket #4521 has been updated. View details at…" |
| `DELIVERY_NOTIFICATION` | Order and shipping updates | "Your package shipped! Tracking: 1Z999…" |
| `ACCOUNT_NOTIFICATION` | Account alerts and changes | "Your password was changed. If this wasn't you, call…" |
| `MARKETING` | Promotional content | "Summer sale! 30% off all items this weekend…" |
| `2FA` | Two-factor authentication codes | "Your verification code is 847291. Expires in 10 min." |
| `SECURITY_ALERT` | Security-related notifications | "New login detected from Chrome on Windows…" |
| `POLLING_VOTING` | Surveys and polls | "How was your experience? Reply 1-5." |
| `CHARITY` | Nonprofit fundraising and awareness | "Thanks for supporting Habitat! Text DONATE for…" |
| `POLITICAL` | Political campaigns and advocacy | "Reminder: Vote on Nov 5th. Find your polling place…" |
| `MIXED` | Multiple message types (most common) | Combination of the above |

### Special use cases

| Use Case | Description | Requirements |
| --- | --- | --- |
| `LOW_VOLUME` | Under 6,000 messages/month | Simplified registration |
| `SOLE_PROPRIETOR` | Individual/small business without EIN | See [Sole Proprietor](sole-proprietor.md) guide |
| `EMERGENCY` | Life-threatening alerts | Must demonstrate emergency nature |
| `AGENTS_FRANCHISES` | ISVs sending on behalf of clients | Additional compliance requirements |
| `SWEEPSTAKES` | Contests and giveaways | Must include rules and terms |

**Choose carefully.** Changing a campaign's use case after registration requires creating a new campaign. Carriers reject campaigns where sample messages don't match the declared use case.

## Create a campaign

You need an approved brand before creating campaigns. Your brand's vetting score affects campaign throughput — see [#Rate limits and throughput](rate-limits-and-throughput.md).

### Required fields

| Field | Type | Description |
| --- | --- | --- |
| `brandId` | string | Your registered brand ID |
| `usecase` | string | Use case type (see table above) |
| `description` | string | What your campaign does (2-4 sentences) |
| `sample1` | string | First sample message |
| `sample2` | string | Second sample message |
| `messageFlow` | string | How users opt in to receive messages |
| `helpMessage` | string | Response to HELP keyword |
| `optinKeywords` | string | Comma-separated opt-in keywords |
| `optoutKeywords` | string | Comma-separated opt-out keywords |
| `helpKeywords` | string | Comma-separated help keywords |

### Optional fields

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `embeddedLink` | boolean | `false` | Messages contain URLs |
| `embeddedPhone` | boolean | `false` | Messages contain phone numbers |
| `numberPool` | boolean | `false` | Using number pool for sending |
| `ageGated` | boolean | `false` | Content requires age verification |
| `directLending` | boolean | `false` | Related to direct lending |
| `subscriberOptin` | boolean | `true` | Subscribers have opted in |
| `subscriberOptout` | boolean | `true` | Subscribers can opt out |
| `subscriberHelp` | boolean | `true` | Help keyword is supported |
| `sample3` | string | — | Third sample message (recommended) |
| `sample4` | string | — | Fourth sample message |
| `sample5` | string | — | Fifth sample message |

```bash
curl -X POST https://api.telnyx.com/v2/10dlc/campaignBuilder \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "brandId": "BRAND_ID",
    "usecase": "DELIVERY_NOTIFICATION",
    "description": "Order confirmation and delivery status updates for e-commerce customers who purchase through our website.",
    "sample1": "Hi {{name}}, your order #{{orderId}} has been confirmed! Estimated delivery: {{date}}. Track at https://acme.com/track/{{orderId}} Reply STOP to opt out.",
    "sample2": "Great news! Your package is out for delivery and should arrive by 5 PM today. Driver: {{driverName}}. Reply STOP to unsubscribe.",
    "sample3": "Your order #{{orderId}} has been delivered to your front door. Rate your experience: https://acme.com/review/{{orderId}}",
    "messageFlow": "Customers opt in at checkout by checking a consent box that reads: I agree to receive order updates via SMS. Frequency varies. Msg & data rates may apply.",
    "helpMessage": "Acme Corp order updates. For help, visit https://acme.com/support or call +15551234567. Reply STOP to cancel.",
    "optinKeywords": "START, YES, SUBSCRIBE",
    "optoutKeywords": "STOP, UNSUBSCRIBE, CANCEL, QUIT",
    "helpKeywords": "HELP, INFO",
    "embeddedLink": true,
    "numberPool": false,
    "ageGated": false
  }'
```
