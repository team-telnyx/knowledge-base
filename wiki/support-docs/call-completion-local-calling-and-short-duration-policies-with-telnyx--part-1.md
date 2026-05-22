---
title: Call Completion, Local Calling, and Short Duration Policies with Telnyx
summary: A practical guide to understanding how Telnyx routes calls, why calls sometimes
  fail or delay, how Local Calling improves completion, how Short Duration Calls are
  handled, and the fastest ways to troubleshoot and report issues.
sources:
- url: https://support.telnyx.com/en/articles/1130707-what-are-short-duration-calls
- url: https://support.telnyx.com/en/articles/4096828-us-rural-call-completion
- url: https://support.telnyx.com/en/articles/4378813-us-local-call-completion
- url: https://support.telnyx.com/en/articles/4453840-post-dial-delay-pdd
- url: https://support.telnyx.com/en/articles/5025298-troubleshooting-call-completion
- url: https://support.telnyx.com/en/articles/6622229-pstn-replacement-local-calling-with-telnyx
- url: https://support.telnyx.com/en/articles/1130664-countries-that-telnyx-offers-termination-in
- url: https://support.telnyx.com/en/articles/7885470-chiro8000-and-telnyx-integration
updated_at: 2026-05-20T15:41:50Z
---

# Call Completion, Local Calling, and Short Duration Policies with Telnyx

*Part 1 of 2 — see also: [Part 2](call-completion-local-calling-and-short-duration-policies-with-telnyx--part-2.md)*

A practical guide to understanding how Telnyx routes calls, why calls sometimes fail or delay, how Local Calling improves completion, how Short Duration Calls are handled, and the fastest ways to troubleshoot and report issues.

## Understanding call routing and completion
Successful call delivery depends on industry routing data and multiple carrier handoffs. In typical US local scenarios the path is: Originating Carrier → Downstream Tandem → LEC → Upstream Tandem → Destination Carrier (Telnyx). Routing relies on LERG, LATA, LRN, LNP, NPA, and Rate Center information. Telnyx assigns LRNs to number blocks and broadcasts them via NPAC so other carriers can update translations and route to Telnyx. Translation or tandem loading delays (especially after new number launches or ports) are common causes of initial local reachability issues, similar to challenges described in [US Local Call Completion](us-local-call-completion.md).

## Key symptoms, thresholds, and definitions
- Post Dial Delay (PDD): Time from final digit or SIP INVITE to the first ringing response (e.g., 180 Ringing). PDD under 7 seconds is generally considered acceptable; investigate if consistently above 7 seconds. See details in [Post Dial Delay (PDD)](post-dial-delay-pdd.md).
- Short Duration Calls (SDCs): Outbound calls 6 seconds or less. Telnyx allows up to 15% of your connected outbound traffic to be SDCs per calendar month (UTC). If your month-end SDC rate exceeds 15%, penalties apply to all SDCs that month, not just the portion above 15%. As of Jan 1, 2024, international SDCs incur $0.01 per call when your SDC rate is above 15%. Calculation: short_duration_connected_calls / total_connected_calls. Example: 200/1000 = 20%.

## Common causes of failed or poor-quality calls
- Local and rural US completion: Least-cost routing, stale translations after ports, or tandem mis-mappings can produce intercepts, dead air, or prolonged ringing. Wireless endpoints with weak signal can also increase PDD. See [US Rural Call Completion](us-rural-call-completion.md) and [US Local Call Completion](us-local-call-completion.md).
- International “local-looking” calls: Many countries block calls that present a local CLI when entering via international exchanges, resulting in 503 errors and failed completion. 
- Configuration issues: Invalid caller ID format, missing international whitelisting, authentication problems, SRTP/codec mismatches, firewall/NAT blocking SIP/RTP, or negative account balance.

## Telnyx features that improve completion
- Local Calling (PSTN Replacement): Telnyx routes through Tier‑1 in-country partners, bypassing international exchanges so the callee sees a local CLI and calls complete more reliably. Benefits include higher completion, correct local caller ID delivery, and built-in enablement on eligible Telnyx numbers. To use it, purchase a number with the Local Calling feature in the Portal and present it as CLI on outbound calls. If you cannot use Local Calling, avoid matching the destination’s country for CLI; otherwise calls are more likely to be blocked. Note: call forwarding can interfere when the forwarded destination matches the caller’s CLI. See [PSTN Replacement / Local Calling with Telnyx](pstn-replacement-local-calling-with-telnyx.md).
- Seasoned LRNs and redundancy: Telnyx maintains seasoned LRNs and redundant coverage across most LATAs, aiding consistent local completion. 
- Global termination: Telnyx offers termination in every country; view international termination pricing in the Portal (https://portal.telnyx.com/#/pricing/voice).

## Step-by-step troubleshooting
Outbound
- Validate caller ID: Must be in +E.164. If missing/invalid you may see 403 “Caller Origination Number is Invalid D35.” Use Caller ID Override on your SIP Connection if your device cannot set it.
- Check destination permissions: By default, Outbound Voice Profiles allow US/CA only. For other regions, whitelist them in the Outbound Voice Profile and complete any required Level 2 verification (https://portal.telnyx.com/#/app/account/verifications).
- 403 Forbidden: Beyond auth failures, other causes include negative balance, missing Outbound Voice Profile, token/tech prefix mismatches, or using a caller ID that belongs to another Telnyx account.
- 503 Service Unavailable/No routes found: Often a downstream routing condition. Contact support with a call example.

Inbound
- Registration (credentials auth): Ensure your device is REGISTERing and that Telnyx IPs/subnets are whitelisted so calls reach your endpoint.
- IP/FQDN auth: Confirm the advertised IP/port and your PBX’s listening IP/port match; configure firewall/NAT and port forwarding for SIP and RTP.

## Interpreting common SIP hangup reasons
- NORMAL_CLEARING (16): Expected hangup; no error.
- USER_BUSY (17): Callee is on another call.
- INCOMPATIBLE_DESTINATION (88): SDP/codec/encryption mismatch (e.g., SRTP enabled on the SIP Connection but not on the device, or unsupported codec set).
- MANAGER_REQUEST (16): Telnyx system ended the call (fraud controls or negative balance).
Inbound-focused
- RECOVERY_ON_TIMER_EXPIRE (102): No timely response to INVITEs (often firewall/NAT or unwhitelisted Telnyx IPs).
- MANDATORY_IE_MISSING (96): Required signaling element missing; can occur if a device expects proxy auth from unknown IPs.
- UNALLOCATED_NUMBER (1): DID not assigned to a SIP Connection, registration down, or not matched by device dial-plan/format. See [Number Formats](number-formats.md).
- PROGRESS_TIMEOUT (16): No 180/183 from customer side within default 5s. Adjust No Ringback Timeout in [SIP Connection: Inbound & Outbound Settings](sip-connection-inbound-outbound-settings.md).
- ALLOTTED_TIMEOUT (602): Answer timeout exceeded on your SIP Connection or in Call Control app settings.
Outbound examples
- CALL_REJECTED (21): Usually 4xx from Telnyx (e.g., invalid CLI, destination not whitelisted). See [Telnyx SIP Response Codes](telnyx-sip-response-codes.md).
- NORMAL_TEMPORARY_FAILURE (41): Often a 5xx from Telnyx due to downstream routing; contact support.

## Tools that speed up diagnosis
Use the Portal Debugging tool to inspect SIP logs, call flow, and test with the Web Dialer. See [Debugging Tools](debugging-tools.md). For a complete list of Telnyx SIP responses, see [Telnyx SIP Response Codes](telnyx-sip-response-codes.md).

## How to report issues effectively
Provide recent, reproducible examples within 48 hours when possible, including:
- Description of the symptom (intercepts, dead air, prolonged ringing, etc.)
- From and To numbers
- Date/time with timezone
- Any error messages heard or observed
- Any testing already completed with local/rural carriers and relevant contacts
Contact: support@telnyx.com or +1 888 980 9750.

## Managing and reducing short duration calls
Telnyx does not support use cases that require high volumes of Short Duration Calls. To locate SDC sources in your traffic:
- Download an outbound-only detail report from the Portal (https://portal.telnyx.com/#/app/reporting/detail-requests).
- Sort by call duration; remove 0‑second calls.
- Count calls ≤ 6 seconds and identify the SIP Connection names that appear most frequently.
If your monthly SDC rate exceeds 15%, penalties apply to all SDCs that month; for international SDCs above 15%, a $0.01 per‑call fee applies.

## Notes on messaging, compliance, and example integration
If you send SMS (e.g., appointment reminders) from software like Chiro8000, Telnyx offers prepaid, low-cost messaging with numbers typically $1/month + $1 setup. US local number messaging requires 10DLC registration; Toll‑Free also has a verification process but is generally simpler. Useful account controls include low-balance notifications, auto-recharge, 2FA, and daily spend limits on outbound profiles. For 10DLC questions: 10DLCquestions@telnyx.com. Pricing: https://portal.telnyx.com/#/app/pricing.
