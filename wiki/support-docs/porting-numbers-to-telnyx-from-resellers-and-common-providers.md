---
title: Porting Numbers to Telnyx from Resellers and Common Providers
summary: A consolidated guide to moving phone numbers into Telnyx when your current
  service is a reseller (Aircall, Intercom, RingCentral, Vonage, Grasshopper, voip.ms)
  or a carrier (Twilio, Bandwidth), including what credentials you need, provider-specific
  PIN/account rules, timelines, LOA options, toll-free nuances, automation via API,
  and how to avoid common rejections.
sources:
- url: https://support.telnyx.com/en/articles/14708128-porting-numbers-away-from-aircall-to-telnyx
- url: https://support.telnyx.com/en/articles/14708129-porting-numbers-away-from-intercom-to-telnyx
- url: https://support.telnyx.com/en/articles/14708130-porting-numbers-away-from-resellers-aircall-intercom-ringcentral-vonage-etc
- url: https://support.telnyx.com/en/articles/3947850-porting-away-from-twilio
- url: https://support.telnyx.com/en/articles/3947875-porting-away-from-bandwidth
- url: https://support.telnyx.com/en/articles/5595770-port-away-from-voip-ms
- url: https://support.telnyx.com/en/articles/14790558-how-to-find-your-porting-pin-or-passcode
- url: https://support.telnyx.com/en/articles/5386351-automating-ports-with-programmatic-api
- url: https://support.telnyx.com/en/articles/8006189-port-out-pin-protection
- url: https://support.telnyx.com/en/articles/8268276-loa-template-download
- url: https://support.telnyx.com/en/articles/8588086-auto-generated-letter-of-authorization-loa
- url: https://support.telnyx.com/en/articles/8673249-us-ca-toll-free-number-porting
- url: https://support.telnyx.com/en/articles/8709331-porting-bundles
updated_at: 2026-05-20T15:45:59Z
---

# Porting Numbers to Telnyx from Resellers and Common Providers

A consolidated guide to moving phone numbers into Telnyx when your current service is a reseller (Aircall, Intercom, RingCentral, Vonage, Grasshopper, voip.ms) or a carrier (Twilio, Bandwidth), including what credentials you need, provider-specific PIN/account rules, timelines, LOA options, toll-free nuances, automation via API, and how to avoid common rejections.

## Understand resellers vs carriers
Many business voice platforms are resellers: they present phone numbers in their app, but the numbers actually live on an underlying carrier (e.g., Twilio, Bandwidth, Inteliquent). For any port, the losing carrier’s records are the source of truth. That means the account number, PIN/passcode, authorized name, and service address must match the underlying carrier’s records—not just what you see in the reseller portal.

Key implications:
- Always ask your current provider to identify the underlying carrier and supply the carrier-level account number and port-out PIN.
- The losing carrier decides if a PIN is required and its format.
- Keep your current service active until the port completes.

## What to gather before you submit a port
Collect these carrier-level details from your current provider (reseller or carrier):
- Underlying carrier name (Twilio, Bandwidth, etc.)
- Account number on carrier records (may differ from your app/customer ID)
- Port-out PIN/passcode (not your login password)
- Authorized name (exact legal name on the carrier account)
- Service address (as recorded by the carrier)

Tip: If your provider won’t share this, note that most are obligated to provide it. Contact porting@telnyx.com for help escalating.

## Provider-specific instructions
Use the exact fields and formats below when filling your Telnyx port request.

- Twilio
  - Account Number: Twilio Account SID (AC…); for sub-accounts, use the sub-account SID.
  - PIN: Twilio auth token or a port-out passcode (if configured in Console > Phone Numbers > Port Out Settings).
  - Notes: Twilio’s PIN rules have changed over time; if you see PIN rejections, confirm the current passcode/token. For toll-free, Twilio doesn’t use BTNs/account numbers—use any one of the numbers being ported as both BTN and Account Number.

- Bandwidth
  - Account Number/BTN: Bandwidth doesn’t use BTNs/account numbers—use any one of the numbers you’re porting as both BTN and Account Number.
  - Notes: If you don’t use Bandwidth’s port-out validation, they often grant automatic FOC; otherwise request a CSR from Bandwidth.

- Aircall (reseller; often Twilio-backed)
  - Account Number: Provided by Aircall support (not your Aircall portal ID).
  - PIN: Carrier-level passcode from Aircall support.
  - Use the name and address on the Aircall carrier account. Contact Aircall first to retrieve credentials.

- Intercom (reseller; often Twilio-backed)
  - Account Number: Carrier account number via Intercom support; if Twilio, use the Twilio Account SID.
  - PIN: Carrier-level PIN; if Twilio, use auth token or the port-out passcode.

- Vonage (incl. Vonage Business)
  - Account Number: On invoices.
  - PIN: Set in the Vonage portal (Account > Security > Port-Out PIN).
  - Notes: Attach an LOA.

- RingCentral
  - Account Number: In Admin Portal > Account Details.
  - PIN: Set in Admin Portal (must be set before starting a port).

- Grasshopper (often Bandwidth/Inteliquent-backed)
  - Account Number: Your Grasshopper account number.
  - PIN: Obtain from Grasshopper support.

- voip.ms
  - Account Information: May vary if you use sub-accounts (you may need separate port orders per sub-account).
  - PIN: If previously enabled (Account Settings > Security). If no PIN is enabled, a PIN may not be required.
  - Account Number: Not on invoices; visible in portal. Generally not required if PIN not enabled.

## Toll-free (US/CA) specifics
Toll-free (8YY) porting operates through a centralized industry process and typically completes faster than local ports when clean. Plan carefully:
- Submit 1–2 weeks before desired activation; numbers risk disconnection if not activated within 1–2 weeks after RespOrg release.
- Required docs: Signed LOA and a recent invoice.
- Timeline: Often ~2 business days; industry variance can run 1–7 business days.
- SMS best practice: Migrate SMS first via hosted SMS 3–5 business days before voice FOC to avoid downtime; when voice ports at FOC, both services consolidate on Telnyx.

## Typical timelines and expedites
Actual timing depends on the losing carrier and data accuracy.
- Small/simple local ports (US/CA): ~3–7 business days after acceptance.
- Larger/complex ports: ~5–15 business days after acceptance.
- Example expedite windows seen in practice:
  - US local: As little as same-day (≈6 business hours) when the losing carrier supports it.
  - CA local: Typically ~3 days; same-day may be possible with a fee per order.
  - Toll-free: ~1–2 days; same-day sometimes available.
To request an expedite, submit your order and contact Telnyx porting via live chat in the Portal. Expedites are not guaranteed and fees may apply even if same-day isn’t achieved.

## LOA and documentation options
- Telnyx requires a signed Letter of Authorization (LOA) and a recent invoice from your current provider for validation.
- Auto-generated LOA in Portal: For eligible US/CA local ports, Telnyx can prefill an LOA from your order details. You can:
  - Download it, attach it to the order, or
  - Share a time-limited link with an authorized signer who can sign and attach it without a Telnyx login.
  - Customize LOA branding with your company logo and details; manage multiple templates and select per order.
- Programmatic LOA template download: Via API, download an LOA template PDF for a given porting order and incorporate into automated flows.

## Automate porting with the API
Streamline high-volume or embedded workflows using the Porting and Documents APIs:
- Run a portability check (developers.telnyx.com API docs) before creating an order.
- Create a porting order (v2/porting_orders) with end user info, activation settings (FOC date), and number configuration.
- Upload required documents via the Documents API; pass returned document UUIDs on the port order.
- Confirm the port order and monitor status via webhooks; see the Porting Quickstart on developers.telnyx.com.

## Pre-configure Bundles on your port order
- In the Portal, open your port order and use Pre-configure Bundles to associate eligible bundles with specific numbers before they arrive.
- Notes:
  - You can pre-configure at any time before completion; bundles actually apply after the numbers port in.
  - Ensure bundle geography matches your numbers (e.g., US bundle for US numbers).
  - You can also integrate pre-configuration via the Porting API (see developers guide).

## Common rejection reasons and how to fix
- PASSCODE_PIN_INVALID: The PIN/passcode doesn’t match. Obtain the carrier-level PIN from your provider; don’t guess or reuse stale codes.
- ACCOUNT_NUMBER_MISMATCH: You used a reseller portal ID or the wrong account number. Ask for the carrier account number.
- BUSINESS_NAME_MISMATCH: Legal name mismatch. Use the exact name on the carrier account.
- SERVICE_ADDRESS_MISMATCH: Address mismatch. Use the carrier’s service address, not billing or mailing if they differ.
Each rejection typically delays progress 3–5 business days while revalidating—verify credentials before submitting.

## Best practices and escalation
- Don’t cancel your current service until the port completes and you’ve tested inbound/outbound and (if applicable) SMS.
- Gather carrier credentials up front; PIN and account number issues are the top causes of delays.
- For Twilio/Bandwidth CSR data, request it directly from their porting support if needed.
- If a reseller is unresponsive or obstructive, contact porting@telnyx.com; we can help identify the underlying carrier and escalate.
- For Telnyx customers safeguarding numbers from unauthorized port-outs, see [Port Out PIN Protection](port-out-pin-protection.md) to enable PIN validation on outbound ports of your on-net US numbers.
