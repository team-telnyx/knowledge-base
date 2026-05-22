---
title: 'Telnyx Number Porting: Errors, Resolutions, and Best Practices'
summary: A consolidated guide to Telnyx number porting that explains common rejection
  reasons, how to resolve them, key documents and identifiers (LOA, CSR, BTN/ATN),
  day‑of‑port readiness, port request statuses, and how to manage port‑outs from Telnyx.
sources:
- url: https://support.telnyx.com/en/articles/1130610-btn-or-atn-mismatch-error
  content_hash: e55cbc854a0a61a7e57307c6d359ed4c592fb45b6ff14e28a0d8e766c51f8ca9
- url: https://support.telnyx.com/en/articles/1130616-number-not-portable-tn-not-portable-error
  content_hash: 5082c391c4aee79c97f8a3aaa525750ef6b88b3814b0751e33ed6d69533d163a
- url: https://support.telnyx.com/en/articles/1130619-invalid-reseller-error
  content_hash: 98d357e00ca44c332d96fbfa08393e2b2c465aaaa73bde392c1024cc4624be1b
- url: https://support.telnyx.com/en/articles/1130623-authorized-name-mismatch-error
  content_hash: c4d75c0c79b83cc18e1f5a236c1a1359d4636352ea340723ffc4e33a0cd818d1
- url: https://support.telnyx.com/en/articles/1618776-porting-error-messages
  content_hash: b9d67ad26ba3f21eb422134ca7aa78068f3d0bf91258d982b1fd69e278e0e274
- url: https://support.telnyx.com/en/articles/1782930-port-request-rejected
  content_hash: ecb23dd5050ef0482613ba7e2cf645dd0d465d089e965f3de5e6d9c69e3e2c36
- url: https://support.telnyx.com/en/articles/2042977-porting-in-day-of-port-foc
  content_hash: 9cbecc41d0cf092075b724885585de016fb4ae7907b2581fec55cc6e97eb176c
- url: https://support.telnyx.com/en/articles/2030667-i-received-a-port-out-notification
  content_hash: e70a362e315b1bd24ec2a4150f4c3ca44bc1b6f2ec99a0dac7ae4c4d44efea85
- url: https://support.telnyx.com/en/articles/2030770-port-in-best-practices
  content_hash: c2c1dbbb098132064899b005e326f38caaa439f891bdcb047a6e5aeab134dea0
- url: https://support.telnyx.com/en/articles/2033789-port-numbers-away-from-telnyx
  content_hash: d68c7d80ea15adee4bd3939261ce51da8187a56e3252db19d5f86d488c71cc40
- url: https://support.telnyx.com/en/articles/2047076-carrier-refusing-to-port-your-number
  content_hash: ba790faf8b1864cf144bbb376d86b02637b8fa20f00333bf8053fcc790ace8d7
- url: https://support.telnyx.com/en/articles/2906030-port-out-tracking
  content_hash: b2544abeff555b81b8c2b4920db364a27a697ff83b416a5fbaf56a2fd14c4adb
- url: https://support.telnyx.com/en/articles/3284588-port-request-statuses
  content_hash: 77c24e8db7d012139d570157ddcfd930f324b808fc259f50f33c5cd360ec572c
- url: https://support.telnyx.com/en/articles/2034326-how-to-fill-out-an-loa
  content_hash: dc91c1d39e9c2410f20864f52940eecf7ef555366b222f3c130f369c9659ca09
updated_at: 2026-05-20T15:45:05Z
---

# Telnyx Number Porting: Errors, Resolutions, and Best Practices

*Part 1 of 2 — see also: [Part 2](telnyx-number-porting-errors-resolutions-and-best-practices--part-2.md)*

A consolidated guide to Telnyx number porting that explains common rejection reasons, how to resolve them, key documents and identifiers (LOA, CSR, BTN/ATN), day‑of‑port readiness, port request statuses, and how to manage port‑outs from Telnyx.

## Key identifiers and documents you’ll need
- Billing Telephone Number (BTN) / Account Telephone Number (ATN): The primary number on an account used by many carriers to validate a port. It often isn’t visible on invoices (common exceptions: wireless and toll‑free). If you have multiple accounts with your current carrier, each may have a different BTN/ATN.
- Customer Service Record (CSR): The authoritative record at the losing carrier that lists service address, BTN/ATN, authorized contacts, and sometimes features. Use it to ensure your LOA data matches what’s on file.
- Letter of Authorization/Agency (LOA): Grants Telnyx permission to port numbers on the end user’s behalf. Must be complete and legibly signed by an authorized person on the account. Include service address (not just billing), current carrier name, BTN, and all TNs in NPA‑NXX‑XXXX format. For US/CA toll‑free, include “Port to RespOrg QIT02.” If unsure of required values, request a CSR first.
- Proof of ownership: Typically a recent invoice listing the TNs. If the invoice doesn’t show numbers, use a CSR or a current carrier portal screenshot.
- Passcode/PIN: Some carriers require a port‑out PIN/passcode; ensure it matches the carrier’s records.

## Common rejection reasons and how to fix them
Below are frequent errors you may see during validation or after submission to the losing carrier, with concise remediation steps:
- ACCOUNT_NUMBER_MISMATCH / ACCOUNT_NUMBER_REQUIRED: The account number is wrong or missing. Some carriers use the BTN as the account number. Verify via CSR.
- AUTH_NAME_MISMATCH: Authorized user name doesn’t match. Call the losing carrier or use the CSR to obtain the exact authorized name. For multi‑site businesses, the authorized user might be a current/former store manager.
- BTN_ATN_MISMATCH: BTN/ATN doesn’t match what’s on the CSR. Re‑check the CSR or ask the carrier; in large ports, some TNs may belong to a different account with a different BTN/ATN.
- BUSINESS_NAME_MISMATCH: End‑user or business name differs from carrier records. Match the CSR exactly.
- DIFFERENT_ACCOUNTS: The TN list spans multiple losing‑carrier accounts. Split the order by account.
- DIFFERENT_RATE_CENTERS: TNs span multiple rate centers and must be split accordingly. Telnyx often corrects this automatically.
- FOC_REJECTED: Requested activation time/date not accepted. Propose an alternative; avoid last‑minute changes when possible.
- ILLEGIBLE_LOA: Provide a clear, legible LOA with proper signature.
- INVALID_RESELLER (Canada): The reseller name in your request doesn’t match what the carrier has. Obtain the reseller’s exact legal name as filed with the carrier (it may differ from branding on invoices).
- LOSING_CARRIER_NO_RESPONSE: Telnyx will typically re‑engage the losing carrier; no action usually required from you.
- OTHER: Unspecified carrier‑side error; Telnyx will advise next steps.
- PASSCODE_PIN_INVALID: Correct the passcode/PIN with the losing carrier.
- PENDING_ORDER: Another change (port or service update) is already in progress. Ask the losing carrier to complete/cancel it before re‑submitting.
- PORTING_MAIN_BTN: You marked a partial port but included the account’s BTN; that would strand remaining TNs. Either full‑port the account or designate a new BTN with the losing carrier before re‑submitting.
- REQUEST_INCORRECT: The request type (full vs partial) was wrong. Correct and resubmit.
- SERVICE_ADDRESS_MISMATCH / ZIP_POSTAL_CODE_MISMATCH: Ensure the LOA service address matches the CSR exactly (street, city, state/province, ZIP/postal code).
- TN_HAS_SPECIAL_FEATURE: A TN has features (e.g., DSL, signal ring, or bundled offers) that must be removed or adjusted before porting.
- TN_MISMATCH: A TN in the order isn’t on the losing‑carrier account specified. Reconcile the TN list against the CSR.
- TN_NOT_PORTABLE: Catch‑all for non‑portability (inactive numbers, pending changes, special features/plans, recent account changes). Call the losing carrier to identify the specific blocker; reactivate inactive TNs before porting.
- UNSUPPORTED_RATE_CENTER: Telnyx cannot port TNs in certain rural/unsupported rate centers.

## BTN/ATN mismatch: why it happens and how to correct it
- Why it appears: The BTN/ATN you supplied doesn’t match the losing carrier’s CSR. In large orders, some TNs may reside on different accounts (and thus have different BTNs/ATNs). Losing carriers usually won’t identify which subset is mismatched.
- How to fix:
  - Check the latest invoice header for BTN/ATN (may not be shown for many services).
  - If you work through a reseller/VOIP provider, note that their BTN/ATN with the underlying carrier may differ from what appears on your reseller invoice.
  - If not readily available, request the CSR directly from the losing carrier; align your LOA and order data to the CSR.
  - For reseller scenarios, do not submit the end customer’s number/address when the BTN and service address actually belong to the reseller’s account.

## Authorized and reseller name pitfalls
- Authorized user vs bill recipient: The authorized name on file can differ from the person who receives invoices. Always confirm the authorized user via the CSR or by calling the losing carrier.
- Multi‑location businesses: The authorized user can be a local manager (current or former) rather than corporate.
- Canada‑specific reseller rule: Canadian ports often require the reseller’s exact legal name as filed with the carrier. Obtain the precise spelling from the reseller; it may not match their marketing or invoice brand.

## Preventing rejections: Port‑in best practices
- Lock in FOC dates: Avoid changing the FOC date/time. Many rejections or service hiccups occur when dates change late; some carriers may still drop lines on the original date.
- Avoid last‑minute changes: FOC changes within 48 hours are best‑effort only; risk of losing‑carrier misalignment increases.
- Provide full documentation: Submit a complete LOA and recent invoice; add a CSR when available to pre‑validate data or to dispute rejections quickly.
- Assign a Telnyx connection up front: Map incoming TNs to a SIP connection in the portal so calls route correctly the moment activation completes.
- Confirm with the losing carrier: Some carriers call the end user to confirm—respond promptly to accelerate the process.
- Engage Telnyx early if issues arise before/after FOC: The Porting team can help isolate whether a problem is on the losing side, in transit, or during activation.

## Day‑of‑port (FOC) checklist
- Confirm routing: Ensure every TN is assigned to the correct Telnyx connection in your account before the FOC window.
- Prepare systems: Have PBXs, SBCs, IPs, firewalls, and translations ready to accept traffic at the FOC time.
- Expect minor delays: During high‑volume windows, some variance around the exact FOC minute can occur; Telnyx works to minimize this.
- SMS capability note: US numbers may show “Not SMS Capable” while pending; this updates when activation completes.
- Tight activation requirement: If you need near‑exact FOC execution, notify the Porting team a few days in advance. If eligible, consider FastPort®.
