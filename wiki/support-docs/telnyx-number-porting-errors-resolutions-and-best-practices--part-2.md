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

*Part 2 of 2 — see also: [Part 1](telnyx-number-porting-errors-resolutions-and-best-practices--part-1.md)*

A consolidated guide to Telnyx number porting that explains common rejection reasons, how to resolve them, key documents and identifiers (LOA, CSR, BTN/ATN), day‑of‑port readiness, port request statuses, and how to manage port‑outs from Telnyx.

## Port request lifecycle and statuses
- draft: Order created, not yet submitted to Telnyx. Drafts older than 30 calendar days are auto‑deleted.
- in‑process: Submitted to Telnyx and pending submission to the losing carrier.
- submitted: Delivered to the losing carrier; awaiting their response (updates typically within ~36–48 business hours after carrier reply).
- exception: Losing carrier rejected the request (mismatch or other error). Correct data per the rejection reason list and resubmit.
- foc‑date‑confirmed: Losing carrier confirmed the activation date/time.
- activation‑in‑progress (V2 API): The FOC window has arrived and activation/port cutover is underway.
- ported: Activation confirmed; calls should now route via Telnyx.
- cancel‑pending: Telnyx received your cancellation; awaiting losing‑carrier confirmation (can take up to 48 hours depending on carrier).
- cancelled: Losing carrier confirmed cancellation; the port will not occur.

## When a carrier resists or delays your port
- Verify everything against the CSR: Most rejections trace back to simple mismatches. Correcting data up front saves weeks.
- Call instead of only emailing: Many carriers provide faster updates over the phone for porting cases.
- Know your rights: The FCC provides detailed guidance on number portability; understanding it can help resolve disputes. See https://www.fcc.gov/consumers/guides/porting-keeping-your-phone-number-when-you-change-providers

## Managing port‑outs from Telnyx
- Information to give your new (gaining) carrier:
  - End‑user name: Business or residential name.
  - Address: Any valid address within the TN’s country (for US numbers, any US address).
  - BTN / Account number: Telnyx doesn’t use separate account numbers—use one of the TNs being ported as the BTN/account number.
  - Request a Full Port: Telnyx will not cancel or disconnect other services based solely on a gaining‑carrier port request.
- CSR note: Telnyx does not hold or provide CSR data. If the new carrier requires CSR info, they must proceed without it or the end user must provide alternate proof.
- Exporting your numbers: In the portal under My Numbers, you can export your DIDs to CSV for reference.
- Notifications and timing:
  - Telnyx creates a Port‑Out request upon receipt from the gaining carrier and notifies the account owner by email (webhooks available). You can adjust notification recipients/permissions in the portal.
  - Please acknowledge within 24–48 hours. If you approve, status moves to Authorized and Telnyx notifies the gaining carrier. If you reject, you must provide a valid reason; withholding numbers for non‑regulatory reasons (e.g., billing disputes) is not allowed. Invalid rejections may be overridden and FOC provided.
  - No acknowledgment auto‑approves the port‑out.
  - FOC changes from the gaining carrier trigger a webhook. The gaining carrier has a 10‑day grace window after the listed FOC date to complete the port‑out.
- Completion and fees:
  - Once port‑out is confirmed, numbers are removed from your account immediately.
  - Port‑out fees apply as per your pricing; see your account’s Pricing section or contact sales if you have questions.

## Support and escalation
- Telnyx Porting team: porting@telnyx.com
- Telnyx LNP (port‑out inquiries): lnp@telnyx.com
- Use your Mission Control Portal to: create/track port‑ins, assign connections, monitor port‑outs, manage permissions for who can view/act on porting requests.
