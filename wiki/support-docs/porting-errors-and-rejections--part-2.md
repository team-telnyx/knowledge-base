---
title: Porting Errors and Rejections
summary: A comprehensive guide to the error messages, rejection reasons, and resolution
  steps that can arise when porting telephone numbers to or from Telnyx—including
  BTN/ATN mismatches, authorized-name errors, reseller issues, port-out notifications,
  and PIN protection settings.
sources:
- url: https://support.telnyx.com/en/articles/1130610-btn-or-atn-mismatch-error
- url: https://support.telnyx.com/en/articles/1130616-number-not-portable-tn-not-portable-error
- url: https://support.telnyx.com/en/articles/1130619-invalid-reseller-error
- url: https://support.telnyx.com/en/articles/1130623-authorized-name-mismatch-error
- url: https://support.telnyx.com/en/articles/1618776-porting-error-messages
- url: https://support.telnyx.com/en/articles/1782930-port-request-rejected
- url: https://support.telnyx.com/en/articles/2030667-i-received-a-port-out-notification
- url: https://support.telnyx.com/en/articles/2047076-carrier-refusing-to-port-your-number
- url: https://support.telnyx.com/en/articles/8006189-port-out-pin-protection
updated_at: 2026-06-11T11:12:13Z
---

# Porting Errors and Rejections

*Part 2 of 2 — see also: [Part 1](porting-errors-and-rejections--part-1.md)*

A comprehensive guide to the error messages, rejection reasons, and resolution steps that can arise when porting telephone numbers to or from Telnyx—including BTN/ATN mismatches, authorized-name errors, reseller issues, port-out notifications, and PIN protection settings.

## Why Port Requests Get Rejected

The most common reason for rejection is that the information submitted on the port request is incorrect. Carriers must verify that numbers are being ported out legitimately and with the consent of the account holder.

**Best practice:** Request a CSR (Customer Service Record) from the losing carrier *upfront* when submitting port requests. A CSR provides your full account information. Comparing the CSR to the information on your LOA before submission will help avoid rejections. If a rejection does occur, the CSR can be used to dispute it with the losing carrier.

For a complete list of rejection-related error messages, see the table in the Common Porting Error Messages section above.

If you have questions about a specific port request, comment on your [Port Request within the Portal](https://portal.telnyx.com/#/app/numbers/port-numbers?status=both) or email the Telnyx porting team at [porting@telnyx.com](mailto:porting@telnyx.com).

## When a Carrier Refuses to Port Your Number

Porting a number away from a provider means loss of business for them, which can make the process difficult. Telnyx works with carriers and verifies information in real-time, but does not have relationships with every carrier. Steps you can take:

1. **Make sure your porting request information is correct.** Incorrect information is the most common reason for rejection and can take weeks to resolve. If you are unsure of your account details, request a CSR from your carrier.
2. **Call your provider.** Emailing a support team can mean waiting days for each response. Calling often results in a quicker—if not instant—update on your porting request.
3. **Know the FCC regulations.** The [FCC has detailed guidelines on number portability](https://www.fcc.gov/consumers/guides/porting-keeping-your-phone-number-when-you-change-providers). Familiarizing yourself with them is important if you frequently encounter porting issues.

## Receiving a Port-Out Notification

When a carrier receives a port-in request, it sends the current carrier a port-out notification to inform them that a number is being ported out (usually with the end-user's authorization).

Telnyx automatically creates a port-out request and sends a notification via email/webhook, depending on your notification settings. By default, email notifications go to the main account owner's email address.

**Action required:** Telnyx typically asks that you respond to port-out notifications within 24–48 hours via email.

- If you **do not wish** the numbers to be ported out, notify Telnyx as soon as possible. Reject the request and inform Telnyx that you decline along with a valid reason. Provided you decline within the timeframe and give a valid reason, the numbers will not be ported out. See [Port Out Tracking](port-out-tracking.md) for details.
- If you are a **service provider or reseller**, check whether the end-user (your customer) has submitted a port request with a new carrier. It is your responsibility to ensure port-out requests are actioned and responded to correctly.

For questions about a port-out or port-out notification, contact [lnp@telnyx.com](mailto:lnp@telnyx.com).

## Port Out PIN Protection

Port Out PIN protection allows you to validate PINs on incoming port-out requests. When enabled, the PIN provided by the losing carrier is checked against your account settings. If it matches, the order is created and sent to you for review. If it does not match (or is not provided), the order is automatically rejected. Auto-rejected orders are visible on the [Port Out Requests](https://portal.telnyx.com/#/app/numbers/port-outs) page in the Mission Control Portal.

By default, PIN protection is **off** for all accounts. If left off, no PIN validation occurs.

**Important:** Port Out PIN protection is available for on-net US numbers only. Customers using PIN protection must adhere to all Telnyx and FCC rules, including the requirement to provide the PIN to end users/resellers so that legitimate port-outs are not blocked. Telnyx may immediately revoke PIN protection if these rules are violated or if the process is abused to prevent legitimate port-outs. By using PIN protection, you accept all liability for any claims of rule or law violations.

### Enabling PIN Protection and Setting a Default PIN

1. In the [Telnyx Portal](https://portal.telnyx.com/#/app/home), select your profile (top right) and choose **Account Settings**.
2. Select the **Security** tab.
3. Scroll to the Security section and configure:
   - **Enable Port out Pins** — toggle on or off.
   - **Default PIN for Phone Numbers** — the account-level port-out PIN. If no individual PIN is set for a number, this default is used for validation.

### Individual PIN Settings

You can set unique Port Out PINs for individual phone numbers:

1. Go to the [My Numbers](https://portal.telnyx.com/#/app/numbers/my-numbers-beta) page.
2. Click the **Edit** icon for the desired number.
3. On the **Settings** tab, scroll to the **Porting** section.
4. Enter the PIN in the **PIN** field and click **Save Changes**.

If no individual PIN is set, the account-level default PIN applies.

### Eligible vs. Non-Eligible Port Out Orders

On the Port Out Requests page, a **PIN Validation** column shows either **Eligible** or **Non-Eligible**. PIN validation only occurs on Eligible requests. Because PIN protection is limited to on-net US numbers, non-US or off-net numbers will appear as Non-Eligible.
