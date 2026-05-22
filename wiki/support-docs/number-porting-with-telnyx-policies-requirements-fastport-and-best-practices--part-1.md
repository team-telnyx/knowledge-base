---
title: 'Number Porting with Telnyx: Policies, Requirements, FastPort, and Best Practices'
summary: A single, end-to-end guide to porting phone numbers with Telnyx, covering
  prerequisites, portal and API submission, automated validation, FastPort activation,
  timelines and holidays, status tracking and communications, international and toll-free
  nuances, port-outs, and escalation paths.
sources:
- url: https://support.telnyx.com/en/articles/1130614-obtaining-a-csr-from-your-carrier
  content_hash: 42eb06b15e89d83ddbc309a327b5f7cf3369b90817f9aeb4e4934c41ff48a7f3
- url: https://support.telnyx.com/en/articles/1130626-international-number-porting-required-documents
  content_hash: 1fa1ac56b2ed10ffa5950fcc7ac4736c21063f7d645762ed265ffc78626ec145
- url: https://support.telnyx.com/en/articles/1130630-porting-policy-procedure
  content_hash: abaf4c5ff065d1d62cd651098255865bbc70ce926949d0d21984ac4117b8d099
- url: https://support.telnyx.com/en/articles/1130633-checking-a-port-request-status
  content_hash: 501c1cd03ba354735d38b2d656269b06f70abfb0b85c78741c78cead1aef7767
- url: https://support.telnyx.com/en/articles/1130634-port-numbers-to-telnyx
  content_hash: 2cbf84a59c40a180bd800d99667188f4e56f4856d30afab18967638f5dd07a56
- url: https://support.telnyx.com/en/articles/1130635-can-i-port-out-my-telnyx-number
  content_hash: 5a24af60e7d9b53d4030ba64c7fc182babf36c4fc4d3111cf71b468c7d7763ea
- url: https://support.telnyx.com/en/articles/1516776-automated-port-request-validation
  content_hash: c2700d0b896d1091a76949f1a88b6bed826e34b4154a12cd7d227785cda953f2
- url: https://support.telnyx.com/en/articles/2021334-your-guide-to-fastport
  content_hash: ee82b4c249b661a5f927f0390f6e90c01c336d82f3dd7c84b6b4e7518f813089
- url: https://support.telnyx.com/en/articles/2054704-fastport-faqs
  content_hash: 433d1fdefb00235b7aa5d90cfed1b5a495cabc3e178da759bd89f1dfc1154a9c
- url: https://support.telnyx.com/en/articles/2086149-number-porting-rules-and-guidelines
  content_hash: 08fd678016e2b41554832815702a254ae574d6ac8f1ec52a8b1d89d1a770a9ee
- url: https://support.telnyx.com/en/articles/3561993-using-telnyx-fastport
  content_hash: 3e1f6b4cfa93d88fc2975e2fb0bf2ec8e493ba6a458e847809c6e97af27ba63f
- url: https://support.telnyx.com/en/articles/5469551-international-numbers-required-documents
  content_hash: d415934f287642c4f88e502a5c35de1eef50ee68e941a9410e9075965ccd973a
- url: https://support.telnyx.com/en/articles/6460777-porting-requirements
  content_hash: d924cbb514302638a7330664c831c6b7dfe36480fef0b45b211c2ed9488ccd82
- url: https://support.telnyx.com/en/articles/5820338-best-practices-for-contacting-porting
  content_hash: 2d13a855c50f2c47e9eac0458a47be8fe38c195d8e89cb362b0b06d17723b364
updated_at: 2026-05-20T15:43:52Z
---

# Number Porting with Telnyx: Policies, Requirements, FastPort, and Best Practices

*Part 1 of 2 — see also: [Part 2](number-porting-with-telnyx-policies-requirements-fastport-and-best-practices--part-2.md)*

A single, end-to-end guide to porting phone numbers with Telnyx, covering prerequisites, portal and API submission, automated validation, FastPort activation, timelines and holidays, status tracking and communications, international and toll-free nuances, port-outs, and escalation paths.

## Overview
Number porting lets you move existing phone numbers from a current (losing) carrier to Telnyx. You can submit and manage ports in the Mission Control Portal or via API, take advantage of automated validation and FastPort activation, and track progress in real time. This page consolidates what to prepare, how to submit, typical timelines, common pitfalls, special cases (resellers, international, toll-free), and how to contact and escalate with the Telnyx Porting team.

## What to Prepare (Documents and Data)
Have these ready before you submit:
- Letter of Authorization (LOA)
  - Signed within the last 90 days
  - Wet or valid e-signature (DocuSign/Adobe Sign)
  - Signed by the authorized person on the losing carrier account
  - Lists all numbers being ported and includes end-customer name and service address
  - Toll-free: include the line “Port to RespOrg QIT02”
  - Template: How to fill out an LOA (external): https://support.telnyx.com/en/articles/2034326-how-to-fill-out-an-loa
- Recent invoice or bill
  - From your current (losing) carrier
  - Dated within the last 30 days
  - Ideally shows the numbers; if not, provide one of: portal screenshot from your current carrier, CSR, or contact porting@telnyx.com to discuss alternatives
- CSR (Customer Service Record) — highly recommended but not required
  - Confirms the exact account holder name, service address, BTN/ATN, and number list used to validate your port
  - US-focused; carriers are not obligated to release CSRs to other carriers, and Canadian carriers commonly won’t. Best obtained directly from your current carrier. Upload to your port request when available.
- Account details and validation data
  - Account number and BTN/ATN
  - Service address on file with the losing carrier (often different from the billing address)
  - Authorized person’s name
  - Wireless-specific items (if applicable): account PIN; some carriers may request last 4 of SSN

## Submitting a Port-In (Portal and API)
- Portal navigation
  - Mission Control: Real-Time Communications → Numbers → Port Numbers → New Port Request
  - Choose whether you’re porting your own numbers or acting as a reseller for customers
  - Select the country (create separate requests per country)
- Enter numbers
  - Paste or type, separated by commas or line breaks
  - Supported formats: NPANXXYYYY, 1NPANXXYYYY, NPA-NXX-YYYY, 1-NPA-NXX-YYYY
  - Click Check Portability; remove any non-portable numbers or contact porting@telnyx.com if an international number appears ineligible
  - Telnyx groups numbers into Sub-Requests by underlying carrier to speed processing
- Provide account information
  - Use the service address on file with the losing carrier (not the billing address)
  - Enter the authorized person’s name from the losing carrier’s records
- Upload documents
  - Upload LOA and invoice (and CSR if available). Portal will display any extra, country-specific requirements after portability is checked.
- Choose a default Connection for activation
- Request a desired FOC date (not guaranteed; each carrier has its own rules)
- Expedites are case-by-case and require Telnyx approval
- API option: You can also port via the Mission Control API (external): https://support.telnyx.com/en/articles/1130736-mission-control-api-porting

## Automated Validation and FastPort
- Automated Port Request Validation
  - When supported by the losing carrier (e.g., Level 3, AT&T, CenturyLink), Telnyx automatically requests a CSR using your BTN/account/name/service address and compares it to your submission (allow up to ~30 minutes)
  - If data matches, Telnyx proceeds to final submission; mismatches place the request in Exception status. Update the request via comments and Telnyx will re-validate.
  - For privacy reasons, Telnyx cannot reveal corrected data—only whether it matched.
- FastPort
  - Real-time checks help catch data errors early, avoiding days of back-and-forth
  - After FOC is confirmed, choose activation:
    - On Demand: you click Activate within the activation window
    - Schedule: you pick a time within the window; numbers auto-activate then
  - If you don’t activate during the window, numbers auto-activate at window end
  - You can reschedule within the activation window; changing the FOC date itself requires contacting the Porting team at least 72 hours before FOC
  - No Telnyx port-in fees for US/CA numbers; FastPort eligibility varies by losing carrier

## FOC, Activation Windows, and Scheduling
- Telnyx notifies you when the losing carrier approves the request (FOC)
- Activation occurs on the assigned FOC date/time
- Most US activations support 24/5 (Mon–Fri). In rare cases Telnyx must activate manually during business hours
- With FastPort, use On Demand or Schedule within the activation window shown on the request

## Timelines, SLAs, and Processing Hours
- Simple ports (FCC definition: single line account, no unbundled elements, no complex translations, no reseller; typically under 20 numbers)
  - Submission to losing carrier: within 2 business days
  - Estimated completion: ~7 business days
- Non-simple ports (e.g., >20 numbers, multi-line, complex services)
  - Submission to losing carrier: within 4 business days
  - Estimated completion: ~15 business days or more; may require project management
- Submission availability and processing
  - You can submit requests 24/7/365 via Portal; Telnyx processes and submits Mon–Fri, 9:00 AM–5:00 PM CT

## Tracking Status and Communicating with Telnyx
- Real-time status in Mission Control: Port Numbers page; color-coded statuses; View Details shows sub-requests, FOC dates, comments, and per-number status
- Use the comments section on the port request for all updates and document uploads so everything stays on-record
- Automated emails provide key status updates
- Contacting Porting (support hours vs. order processing)
  - Porting team support hours: Mon–Fri, 9:00 AM–7:00 PM CT
  - Best channels: in-portal chat or phone (+1 888 980 9750) for quick status checks; use a support ticket when you need to request an expedite or provide broader context; always mirror requests/changes in the specific order’s comments
  - You can also email porting@telnyx.com for questions

## Common Exceptions and How to Avoid Them
- Data mismatches
  - Account name spelling differs from carrier records
  - Service address mismatch (use the service—not billing—address on file)
  - Missing or wrong account number/BTN/ATN
  - Grouping numbers from multiple end-customers into one request
  - Inactive numbers in the request
- Document issues
  - Unsigned LOA, signer not authorized, signature older than 90 days
  - LOA does not list all numbers to be ported
  - Missing recent (≤30 days) invoice or acceptable alternative proof
- Prevention tips
  - Obtain and reference a CSR; validate service address and BTN; ensure the authorized signer matches the losing carrier’s records

## Resellers and Special Cases
- If you’re acting on behalf of end-customers and your company is not on the CSR:
  - Use end-customer information on the LOA and have them sign it
  - Be prepared to provide your MSA or proof of authorization upon request
  - Submit separate port requests per end-customer and per service address

## International Porting Nuances
- Submit international ports via the Portal with LOA and invoice; Telnyx will confirm portability with coverage/carrier and advise any country-specific documents
- Requirements vary widely (e.g., local/company IDs, tax/VAT numbers, local address, proof of address, local representative details). The Portal surfaces what’s needed once you check portability
- Notes
  - Some countries or number types may be unavailable (N/A)
  - For Canadian accounts, carriers generally do not share CSRs with other carriers—obtain data from your provider directly
