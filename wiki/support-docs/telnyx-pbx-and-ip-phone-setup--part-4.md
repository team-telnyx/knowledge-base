---
title: Telnyx PBX and IP Phone Setup
summary: Consolidated Telnyx setup guides for Yeastar P-Series, Yeastar S-Series,
  Vodia Multi-Tenant PBX, Epygi QX IP PBX, Positron IP PBX, ScopTEL IP PBX, and Positron
  IP phones, plus a reference table of Cisco/Linksys star codes. Each section covers
  prerequisites, trunk creation, outbound routing, and inbound routing so the device
  can place and receive calls using Telnyx as the SIP provider.
sources:
- url: https://support.telnyx.com/en/articles/13375115-how-to-configure-yeastar-p-series
- url: https://support.telnyx.com/en/articles/3185933-vodia-multi-tenant-pbx-setup
- url: https://support.telnyx.com/en/articles/5724344-cisco-linksys-star-codes
- url: https://support.telnyx.com/en/articles/5728748-epygi-ip-pbx-telnyx-setup
- url: https://support.telnyx.com/en/articles/5748952-yeastar-s-series-telnyx-sip
- url: https://support.telnyx.com/en/articles/5790910-positron-ip-pbx
- url: https://support.telnyx.com/en/articles/5803103-scoptel-ip-pbx
- url: https://support.telnyx.com/en/articles/5811761-positron-ip-phone
updated_at: 2026-07-17T09:08:57Z
---

# Telnyx PBX and IP Phone Setup

*Part 4 of 4 — see also: [Part 1](telnyx-pbx-and-ip-phone-setup--part-1.md), [Part 2](telnyx-pbx-and-ip-phone-setup--part-2.md), [Part 3](telnyx-pbx-and-ip-phone-setup--part-3.md)*

Consolidated Telnyx setup guides for Yeastar P-Series, Yeastar S-Series, Vodia Multi-Tenant PBX, Epygi QX IP PBX, Positron IP PBX, ScopTEL IP PBX, and Positron IP phones, plus a reference table of Cisco/Linksys star codes. Each section covers prerequisites, trunk creation, outbound routing, and inbound routing so the device can place and receive calls using Telnyx as the SIP provider.

## Cisco/Linksys Star Codes

Cisco and Linksys ATAs expose a set of star codes for call control features. The table below summarizes the most common codes.

| Star Code | Name | Action |
| --- | --- | --- |
| \*69 | Call Return Code | Calls the last incoming caller. |
| \*07 | Call Redial Code | Redials the last outgoing call number. (Not in pap2t) |
| \*98 | Blind Transfer Code | Begins a blind transfer of the current call to the extension specified after the activation code. |
| \*66 | Call Back Act Code | Calls a busy line over and over automatically for 30 minutes. When the line becomes free, the caller's phone will notify with a distinctive ring. |
| \*86 | Call Back Deact Code | Cancels a callback. |
| \*05 | Call Back Busy Act Code | Starts a callback when the last outbound call is busy. (Not in pap2t) |
| \*72 | Cfwd All Act Code | Forwards all calls to the extension specified after the activation code, if an extension is specified. |
| \*73 | Cfwd All Deact Code | Cancels call forwarding for all incoming calls. |
| \*90 | Cfwd Busy Act Code | Forwards all calls to a specified extension when your line is busy. |
| \*91 | Cfwd Busy Deact Code | Cancels call forwarding for calls incoming when your line is busy. |
| \*92 | Cfwd No Ans Act Code | Forwards unanswered calls to an extension specified. |
| \*93 | Cfwd No Ans Deact Code | Cancels call forwarding of unanswered calls. |
| \*63 | Cfwd Last Act Code | Forwards the last inbound or outbound calls to the extension specified after the activation code. |
| \*83 | Cfwd Last Deact Code | Cancels call forwarding of the last inbound or outbound calls. |
| \*60 | Block Last Act Code | Blocks the last inbound call. |
| \*80 | Block Last Deact Code | Unblocks the last inbound call. |
| \*64 | Accept Last Act Code | Allows the last inbound call to ring through when do not disturb or call forwarding of all calls are enabled. |
| \*84 | Accept Last Deact Code | Cancels the code to accept the last outbound call. |
| \*56 | CW Act Code | Enables call waiting on all calls. |
| \*57 | CW Deact Code | Disables call waiting on all calls. |
| \*71 | CW Per Call Act Code | Enables call waiting for the next call. |
| \*70 | CW Per Call Deact Code | Disables call waiting for the next call. |
| \*67 | Block CID Act Code | Blocks caller ID on all outbound calls. |
| \*68 | Block CID Deact Code | Removes caller ID blocking on all outbound calls. |
| \*81 | Block CID Per Call Act Code | Blocks caller ID on the next outbound call. |
| \*82 | Block CID Per Call Deact Code | Removes caller ID blocking on the next inbound call. |
| \*77 | Block ANC Act Code | Blocks all anonymous calls. |
| \*87 | Block ANC Deact Code | Removes blocking of all anonymous calls. |
| \*78 | DND Act Code | Enables the do not disturb feature. |
| \*79 | DND Deact Code | Disables the do not disturb feature. |
| \*65 | CID Act Code | Enables caller ID generation. |
| \*85 | CID Deact Code | Disables caller ID generation. |
| \*25 | CWCID Act Code | Enables call waiting, caller ID generation. |
| \*45 | CWCID Deact Code | Disables call waiting, caller ID generation. |
| \*26 | Dist Ring Act Code | Enables the distinctive ringing feature. |
| \*46 | Dist Ring Deact Code | Enables the distinctive ringing feature. The default is \*46. |
| \*74 | Speed Dial Act Code | Assigns a speed dial number. |
| \*16 | Secure All Call Act Code | Makes all outbound calls secure. |
| \*17 | Secure No Call Act Code | Removes security on all outbound calls. |
| \*18 | Secure One Call Act Code | Makes the next outbound call secure. (Redundant if all outbound calls are secure by default.) |
| \*19 | Secure One Call Deact Code | Makes the next outbound call not secure. (Redundant if all outbound calls are not secure by default.) |

Common questions:

- **\*69 (Call Return):** Calls the last incoming caller.
- **\*07 (Call Redial):** Redials the last outgoing call number. Not available in pap2t.
- **\*98 (Blind Transfer):** Begins a blind transfer of the current call to the extension specified after activating the code.
