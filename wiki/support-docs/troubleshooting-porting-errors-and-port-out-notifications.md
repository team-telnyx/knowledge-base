---
title: Troubleshooting Porting Errors and Port-Out Notifications
summary: How to interpret common Telnyx number porting errors, prevent rejections,
  resolve BTN/ATN, reseller, and authorization mismatches, and manage port-out notifications
  and responses.
sources:
- url: https://support.telnyx.com/en/articles/1130610-btn-or-atn-mismatch-error
  content_hash: e55cbc854a0a61a7e57307c6d359ed4c592fb45b6ff14e28a0d8e766c51f8ca9
- url: https://support.telnyx.com/en/articles/1130616-number-not-portable-tn-not-portable-error
  content_hash: d3549cdfa65a105c5969b7a57c08b66e36113b7bdc042bc71f8cd56979f812b0
- url: https://support.telnyx.com/en/articles/1130619-invalid-reseller-error
  content_hash: 98d357e00ca44c332d96fbfa08393e2b2c465aaaa73bde392c1024cc4624be1b
- url: https://support.telnyx.com/en/articles/1130623-authorized-name-mismatch-error
  content_hash: c4d75c0c79b83cc18e1f5a236c1a1359d4636352ea340723ffc4e33a0cd818d1
- url: https://support.telnyx.com/en/articles/1618776-porting-error-messages
  content_hash: b9d67ad26ba3f21eb422134ca7aa78068f3d0bf91258d982b1fd69e278e0e274
- url: https://support.telnyx.com/en/articles/1782930-port-request-rejected
  content_hash: 910801379e53a43652dc27cd351fa6f1023ba369f8b4dd6469b078a3bc9c8e73
- url: https://support.telnyx.com/en/articles/2030667-i-received-a-port-out-notification
  content_hash: e70a362e315b1bd24ec2a4150f4c3ca44bc1b6f2ec99a0dac7ae4c4d44efea85
updated_at: 2026-05-14T11:32:27Z
---

# Troubleshooting Porting Errors and Port-Out Notifications

How to interpret common Telnyx number porting errors, prevent rejections, resolve BTN/ATN, reseller, and authorization mismatches, and manage port-out notifications and responses.

## Key terms you’ll see during porting
- BTN/ATN: Billing/Account Telephone Number that identifies an account with the losing carrier. It’s often not printed on invoices and may be one of the TNs on the account.
- CSR: Customer Service Record from the losing carrier showing the definitive account data (authorized name, service address, BTN/ATN, account number, etc.).
- LOA: Letter of Authorization/Agency used to authorize the port. Details on the LOA must match the CSR.
- FOC date: The firm order commitment date accepted by the losing carrier for the port to complete.
- TN: Telephone Number.

## Why port requests get rejected
Carriers verify that the requester is the legitimate account holder by matching submitted data to what’s on file. If any required field doesn’t match (or a TN can’t be ported), the losing carrier rejects the request. Requesting a CSR up front and mirroring it exactly on your LOA and port submission is the single best way to avoid rejections. If a rejection occurs, a CSR enables Telnyx to dispute it with the losing carrier.

## Common errors and how to resolve them
- Account number mismatch/required
  - Meaning: The account number is missing or doesn’t match. Some carriers use the BTN as the account number.
  - Fix: Obtain the CSR and use the exact account number shown.

- Authorized name mismatch (Auth Name, Authorized User, Name Mismatch)
  - Meaning: The authorized user on file differs from what you submitted; this isn’t always the billing contact.
  - Fix: Call the current carrier to confirm the authorized user; Telnyx may be able to request a CSR to identify it. For retailers/banks/chains, the authorized user may be a current/former store manager rather than corporate.

- BTN/ATN mismatch (Wrong BTN/ATN)
  - Meaning: Submitted BTN/ATN doesn’t match the losing carrier’s CSR. Large ports often mix TNs from multiple accounts with different BTNs.
  - Fix: Check if a BTN/ATN shows on the latest bill; if not, request the CSR. If serviced through a reseller, the reseller’s BTN/ATN on the underlying carrier may differ from what appears on your invoice. Split the request by account when needed.
  - Reseller note: End customers sometimes submit the reseller’s number or their own info incorrectly. Use the reseller’s BTN and service address when required.

- Invalid reseller (Canada only)
  - Meaning: The reseller name you submitted doesn’t exactly match the name on file with the losing carrier.
  - Fix: Ask your reseller for the exact legal spelling they have with the carrier; it may differ from branding on invoices/marketing.

- TN not portable / Number not portable (catch‑all)
  - Meaning: The carrier is intentionally unspecific. Common reasons include inactive TNs, pending orders/changes, special features (e.g., DSL, signal ring), bundled/special rate plans, or recent informational updates.
  - Fix: Call the current carrier to identify impacted TNs; remove features/bundles, clear pending orders, or reactivate inactive TNs before porting.

- Other frequent error categories you may see
  - Business name mismatch: Use the exact business/end-user name from the CSR.
  - Service address or ZIP/postal mismatch: Match CSR address/ZIP exactly (no abbreviations unless shown that way).
  - TN mismatch: A listed TN isn’t on the specified account—split or correct the request.
  - Different accounts: Your list includes TNs from multiple accounts—submit separate requests per account.
  - Different rate centers: Some carriers require splitting by rate center—Telnyx often corrects this automatically.
  - Passcode/PIN invalid: Provide the exact port-out PIN/passcode if the losing carrier requires one.
  - Pending order: Another change or port is already in progress—wait until it completes or cancel it.
  - TN has special feature: Remove DSL/feature/bundle before porting.
  - Porting main BTN (partial port): You attempted a partial port that includes the account’s BTN, which would strand TNs—reassign the BTN with the losing carrier or convert to a full port.
  - Request incorrect (partial vs full): Ensure the request type matches your intent and the account’s structure.
  - FOC rejected: Propose a new date acceptable to the losing carrier.
  - Illegible LOA: Resubmit a clear, readable LOA.
  - Losing carrier no response / Other: Telnyx will typically follow up; no action may be needed from you initially.
  - Unsupported rate center: Some rural rate centers can’t be ported to Telnyx.

## Best practices to prevent rejections
- Always request a CSR from the losing carrier before submitting a port.
- Mirror the CSR precisely on the LOA and in your port request (names, address, BTN/ATN, account number, ZIP/postal, authorized user).
- Confirm whether numbers are via a reseller; for Canada, use the reseller’s exact legal name. Use the reseller’s BTN/service address when required.
- Group TNs by account and, where necessary, by rate center; avoid mixing.
- Ensure TNs are active and free of special features/bundles; clear any pending orders.
- Provide any required passcode/PIN and choose an acceptable FOC date.
- Submit a legible LOA and clean documentation.

## What to do after a rejection
- Compare the CSR to your submitted data, correct mismatches, and resubmit.
- If you have a CSR, Telnyx can use it to dispute the rejection with the losing carrier.
- For questions or assistance, comment directly on your Port Request in the Telnyx Portal (https://portal.telnyx.com/#/app/numbers/port-numbers?status=both) or email porting@telnyx.com.

## Understanding Telnyx port‑out notifications
- When another carrier submits a port‑in, Telnyx (as current carrier) creates a port‑out request and sends you a notification via email and/or webhook by your notification settings. By default, emails go to the main account owner; you can adjust recipients via account/user permissions settings.
- Please reply within 24–48 hours. If you do not wish the numbers to port out, reject the request within the timeframe and include a valid reason. Use your Port Out Tracking workflow to action the response.
- If you are a service provider/reseller, verify with your end user whether they initiated the port; it’s your responsibility to respond correctly and on time.
- For port‑out questions, contact lnp@telnyx.com.

## Notes for large and partial ports
- Large requests often include TNs from multiple accounts—split by account (and rate center where required) to avoid DIFFERENT_ACCOUNTS/DIFFERENT_RATE_CENTERS errors.
- For partial ports, do not include the account’s BTN unless you first reassign the BTN with the losing carrier or convert to a full port to avoid PORTING_MAIN_BTN.
