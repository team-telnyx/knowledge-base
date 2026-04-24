---
title: 10DLC Troubleshooting Guide
summary: Diagnose and resolve common 10DLC brand registration, campaign approval, phone number assignment, and messaging delivery issues.
sources:
  - url: https://developers.telnyx.com/docs/messaging/10dlc/troubleshooting/index
    content_hash: f1a94884f745844427b4021cfc13b778b7e13a8d4cf87c8050b362d39c18d1af
updated_at: 2026-04-10T00:00:00Z
---

# 10DLC Troubleshooting Guide

Diagnose and resolve common 10DLC brand registration, campaign approval, phone number assignment, and messaging delivery issues.

This guide covers the most common 10DLC failures across brand registration, campaign approval, phone number assignment, and message delivery — with specific error codes, root causes, and fixes.

  **Quick links:** [Brand issues](#brand-registration-failures) · [Campaign issues](#campaign-rejection-reasons) · [Number assignment issues](#phone-number-assignment-failures) · [Delivery issues](#message-delivery-failures) · [Carrier-specific issues](#carrier-specific-issues)

***

## Brand registration failures

Brand registration fails when TCR cannot verify your business identity. The `identityStatus` field on your brand object indicates the result.

| Status            | Meaning                                 |
| ----------------- | --------------------------------------- |
| `VERIFIED`        | Brand identity confirmed                |
| `UNVERIFIED`      | Verification failed — action required   |
| `VETTED_VERIFIED` | External vetting completed successfully |
| `SELF_DECLARED`   | Sole proprietor — limited verification  |

### Common brand failures and fixes

**EIN mismatch — company name doesn't match IRS records**

    **Error:** Brand identity verification failed — company name mismatch.

    **Root cause:** The `companyName` you submitted doesn't match what the IRS has on file for that EIN.

    **Fix:**

    1. Look up your exact legal name on the [IRS Tax Exempt Organization Search](https://apps.irs.gov/app/eos/) or your incorporation documents
    2. Update your brand with the exact legal name (including suffixes like "Inc.", "LLC")
    3. Re-submit for vetting

    ```bash
    curl -X PATCH https://api.telnyx.com/v2/10dlc/brand/{brandId} \
      -H "Authorization: Bearer $TELNYX_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{"companyName": "Exact Legal Name Inc."}'
    ```

---

**Address validation failure**

    **Error:** Brand address could not be verified.

    **Root cause:** The address doesn't match USPS records, or uses an incomplete format (e.g., missing suite number).

    **Fix:**

    1. Verify your address via [USPS Address Lookup](https://tools.usps.com/zip-code-lookup.htm)
    2. Use the exact USPS-standardized format
    3. Include suite/unit numbers if applicable
    4. Update the brand and re-submit

    > **Warning:** PO Boxes are generally not accepted. Use a physical business address.

---

**Website URL unreachable or doesn't match**

    **Error:** Brand website could not be verified.

    **Root cause:** TCR checks that the website is live and relates to the registered business. Common issues:

    * Website is down or returns errors
    * URL redirects to a different domain
    * Website content doesn't match the business name

    **Fix:**

    1. Ensure your website is live and loads without errors
    2. Use the root domain (e.g., `https://example.com`, not a deep link)
    3. Verify the website clearly identifies your business name
    4. Don't use placeholder/under-construction pages

---

**Duplicate brand — already registered**

    **Error:** A brand with this EIN already exists.

    **Root cause:** Your business was already registered with TCR, either by you or another Telnyx account (or through another CSP).

    **Fix:**

    1. Check your existing brands: `GET /v2/10dlc/brand`
    2. If registered under another account, contact [Telnyx support](https://support.telnyx.com) to transfer ownership
    3. If registered through another CSP, you can still create campaigns through Telnyx as a secondary CSP

---

**Low vetting score**

    **Error:** Brand vetting score too low for desired throughput.

    **Root cause:** The third-party vetting partner (Campaign Verify) scored your brand below the threshold for your desired messaging volume.

    **Fix:**

    1. Review your brand profile for accuracy — incomplete or inconsistent data lowers scores
    2. Ensure your website, social media, and public records align with your brand information
    3. Request a re-vet after updating information (each vetting attempt has a fee)
    4. See [10DLC Rate Limits](10dlc-rate-limits-throughput.md) for score-to-throughput mapping

      **Vetting score ranges:** 0–24 (low), 25–49 (medium-low), 50–74 (medium), 75–100 (high). Each tier unlocks higher throughput per carrier.

---

**Sole proprietor OTP verification failure**

    **Error:** OTP verification timed out or failed.

    **Root cause:** The one-time password sent to your registered phone number wasn't confirmed in time, or the phone number can't receive SMS.

    **Fix:**

    1. Ensure the phone number on file can receive SMS
    2. Request a new OTP and complete verification within the time window
    3. Check that the phone number matches your identity documents
    4. See the [Sole Proprietor guide](sole-proprietor-10dlc-registration.md) for detailed steps

---

### Check brand status via API

  ```python
  import telnyx

  telnyx.api_key = "YOUR_API_KEY"

  brand = telnyx.TenDlcBrand.retrieve("BRAND_ID")
  print(f"Status: {brand.identityStatus}")
  print(f"Entity Type: {brand.entityType}")

  if brand.identityStatus == "UNVERIFIED":
      print("⚠ Brand verification failed. Check rejection reason and update brand info.")
  ```

  ```javascript
  const telnyx = require("telnyx")("YOUR_API_KEY");

  const brand = await telnyx.tenDlcBrands.retrieve("BRAND_ID");
  console.log(`Status: ${brand.data.identityStatus}`);

  if (brand.data.identityStatus === "UNVERIFIED") {
    console.log("⚠ Brand verification failed. Check rejection reason and update brand info.");
  }
  ```

  ```bash
  curl -s https://api.telnyx.com/v2/10dlc/brand/BRAND_ID \
    -H "Authorization: Bearer $TELNYX_API_KEY" | python3 -m json.tool
  ```

***

## Campaign rejection reasons

Campaign rejections happen during carrier review. The rejection reason is delivered via [10DLC Event Notifications](10dlc-event-notifications.md) webhooks.

| Rejection Reason                  | Common Cause                                                      | Fix                                                                                                               |
| --------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Samples don't match use case**  | Sample messages describe a different use case than declared       | Rewrite samples to match the exact declared use case                                                              |
| **Missing opt-out language**      | No STOP/unsubscribe instructions in samples                       | Add "Reply STOP to unsubscribe" to every sample                                                                   |
| **Inadequate opt-in description** | Opt-in workflow is vague or missing                               | Describe the exact opt-in mechanism (web form URL, keyword, etc.)                                                 |
| **Prohibited content**            | SHAFT content (sex, hate, alcohol, firearms, tobacco) or cannabis | Remove prohibited content or apply for special use case approval                                                  |
| **Brand not vetted**              | Campaign submitted before brand vetting completed                 | Complete [brand vetting](10dlc-brand-registration.md#step-3-submit-for-external-vetting) first |
| **Duplicate campaign**            | Similar campaign already registered for this brand                | Use the existing campaign or differentiate the use case                                                           |
| **Insufficient sample messages**  | Not enough variety in sample messages                             | Provide 2–5 diverse samples showing different message types                                                       |

### Writing samples that pass review

1. **Match your declared use case exactly**

    If you registered as "Customer Care," every sample should be a customer service message:

    > ✅ "Hi Jane, your support ticket #4521 has been resolved. Reply HELP for assistance or STOP to opt out."

    > ❌ "Flash sale! 50% off today only!" (this is marketing, not customer care)

2. **Include opt-out in every sample**

    Every sample message should include opt-out instructions:

    > ✅ "Your order #1234 has shipped. Track: [https://example.com/track](https://example.com/track). Reply STOP to unsubscribe."

3. **Use realistic content — no placeholders**

    Carriers reject generic or placeholder text:

    > ❌ "This is a test message"
    >
    > ❌ "Hello , this is "

    > ✅ "Hi Sarah, your appointment at Downtown Clinic is confirmed for March 5 at 2:00 PM. Reply C to confirm or R to reschedule. Reply STOP to opt out."

4. **Show variety in your samples**

    Provide 2–5 samples that demonstrate different message types within your use case:

    * Confirmation messages
    * Follow-up messages
    * Status update messages
    * Opt-in confirmation messages

### Resubmitting after rejection

You cannot edit a rejected campaign. Create a new one with corrected information:

```python
import telnyx

telnyx.api_key = "YOUR_API_KEY"


## Related Pages

- [Troubleshooting](../reference/troubleshooting.md)
- [Troubleshooting](../reference/troubleshooting-2.md)
- [Android Push Troubleshooting](../reference/android-push-troubleshooting.md)
- [Flutter Push Troubleshooting](../reference/flutter-push-troubleshooting.md)
