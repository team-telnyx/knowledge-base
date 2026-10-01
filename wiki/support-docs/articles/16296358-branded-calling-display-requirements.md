---
title: "Branded Calling display requirements"
summary: "Telnyx applies approved Branded Calling information to eligible outbound SIP trunking calls from approved phone numbers."
sources:
- url: "https://support.telnyx.com/en/articles/16296358-branded-calling-display-requirements"
updated_at: 2026-09-15T00:00:00Z
tags: [support-docs]
source_path: "support-docs/16296358-branded-calling-display-requirements.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/16296358-branded-calling-display-requirements.md -->

# Branded Calling display requirements

Telnyx applies approved Branded Calling information to eligible outbound SIP trunking calls from approved phone numbers. Whether that information appears on the recipient's screen depends on the receiving carrier, device model, operating system, dialer or call-screening app, and the network path used to complete the call.

This article explains the main factors that affect Branded Calling display.

## **What must be configured in Telnyx**

Before Branded Calling information can be sent with your calls, make sure:

- Your Telnyx account has access to Branded Calling.
- Your Enterprise profile is created and approved where required.
- Your Display Identity Record, or DIR, is approved.
- The phone number used as outbound caller ID is added to the approved DIR.
- The phone number status is approved, active, or otherwise ready for Branded Calling in Mission Control Portal.
- You place the outbound call through your Telnyx SIP connection using the approved phone number as caller ID.

Approval means Telnyx can include your approved branded information in eligible call signaling. It does not guarantee that every receiving carrier or device will display it.

## **What affects display on the recipient's phone**

After Telnyx sends approved Branded Calling information, the display depends on the receiving side of the call. The most common factors are:

- **Receiving carrier support**: The recipient's carrier must support Branded Calling display for that call scenario. Branded Calling display support is available for supported Verizon and T-Mobile receiving scenarios, subject to the device, operating system, line type, provisioning, and call path constraints described below.
- **Destination number type**: Branded Calling display is intended for supported US mobile destinations. Landlines, international destinations, and unsupported number types may not display branded information.
- **Device model**: some phones can display business name, logo, and call reason; others may display only the name, or no branded information.
- **Operating system version**: supported behavior can depend on Android or iOS version. Keep recipient devices updated to current carrier-supported OS versions when possible.
- **Device provisioning**: carrier-purchased, carrier-provisioned, unlocked, bring-your-own-device, and MVNO devices may behave differently.
- **Dialer or call-screening app**: the app that displays incoming calls may affect whether branded information appears.
- **Network path**: the route a call takes through the telecom network can vary from call to call. Not every route carries or renders the full set of branded information. This is normal telecom routing behavior, not necessarily a Telnyx configuration problem.
- **Provisioning status and propagation**: newly approved brands or numbers may take time to become visible across supported networks. Use the status shown in Mission Control Portal as the source of truth, and contact Support if a status remains unchanged longer than expected.

## **What information may appear**

Depending on the carrier and device, a recipient may see one or more of the following:

- **Display name**: your approved business or brand name.
- **Logo**: your approved brand logo, where supported by the carrier and device.
- **Call reason**: a short approved reason for the call, where supported.

Not every supported device displays all branded elements. Some devices or lines may show only the business name.

## **How branded data is carried**

At a high level, Telnyx applies approved Branded Calling information to eligible outbound calls using industry-standard telecom signaling, including STIR/SHAKEN and Rich Call Data (RCD). The receiving carrier and recipient device decide whether to display the name, logo, call reason, some combination of those fields, or standard caller ID only.

## **Internal carrier and device display matrix**

Carrier and device support changes over time. Use the tables below as current display guidance for representative supported receiving-side scenarios, and confirm with Telnyx Support/Product if you are troubleshooting a specific destination device or carrier account type.

## **Device, OS, and provisioning display guidance**

Display support varies by recipient device family, operating system version, device provisioning, line type, and receiving network behavior. The guidance below combines representative supported scenarios from carrier-provided display eligibility materials.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Recipient device or service scenario** | **Name** | **Logo** | **Call reason** | **Requirements or notes** |
| Samsung Android devices | Yes | Yes | Yes | Android U / Android 14 or newer. |
| Motorola Android devices | Yes | Yes | Yes | Android U / Android 14 or newer. |
| TCL Android devices | Yes | Yes | Yes | Android U / Android 14 or newer. |
| Apple iPhone XS and newer | Yes | Yes | No | iOS 18.5 or newer. Call reason may not be supported in all iOS receiving scenarios. |
| Android Samsung or Motorola devices purchased from or provisioned for the receiving network | Yes | Yes | Yes | Rich Call Data display still depends on device capability, software version, and line behavior. |
| iOS devices purchased for or provisioned for the receiving network | Yes | Yes | No | Name and logo may display where supported by the device and software version. |
| Other Android devices, other iOS devices, bring-your-own devices, unlocked devices, and MVNO/reseller services | Yes | No | No | Name-only behavior is expected in many of these scenarios, even when richer display is supported on other devices. |
| MVNO/reseller destinations | Yes | No | No | Name-only behavior is common. Logo and call reason support may be limited or unavailable. |

## Additional display notes:

- Devices purchased directly from or provisioned for the receiving network generally have the most predictable branded display behavior.
- Devices purchased unlocked directly from a device manufacturer, non-stock devices, bring-your-own devices, and MVNO/reseller devices may show reduced branded display.
- Devices originally locked to another network and later unlocked may behave differently after a compatible SIM is activated.
- For Apple devices, logo assets must be 32-bit BMP with an alpha channel for transparency, 256 × 256 pixels.
- Logo display on Apple iPhone XS and newer may require iOS 18.5 or later. Apple iPhone XS and newer devices on iOS 18.4 or older may be ineligible for logo display.
- Keep iPhones updated to the latest supported iOS version. Older iOS 18 builds and early iOS 26 builds may have intermittent logo delivery behavior.
- Some line types may receive name only, even when the device itself can support richer branded display.
- Some receiving scenarios do not support the Name + Call Reason use case. Only name, or name and logo, may be delivered.
- A receiving network may receive Rich Call Data but still decide final display based on device capability, software version, line behavior, and call path.

## **Quick diagnostic: why did the logo or call reason not display?**

Use this checklist before escalating a Branded Calling display issue:

1. **Is Branded Calling approved in Telnyx?** Confirm the Enterprise/DIR is approved and the calling number is associated with the approved DIR.
2. **Is the destination an eligible US mobile destination?** Landline, international, unsupported mobile, or non-participating carrier scenarios may show standard caller ID only.
3. **Which receiving network is involved?** Check the internal device, OS, and provisioning guidance above for supported elements.
4. **Does the recipient device support the requested element?** Some devices support name only; some support name + logo; fewer support name + logo + call reason.
5. **Is the device carrier-purchased/provisioned?** Unlocked, BYOD, non-stock, or MVNO devices may show reduced branding even when the same carrier supports richer display on stock devices.
6. **Is the recipient OS current enough?** Confirm whether the recipient device meets the OS guidance above, such as Android U / Android 14 or newer for supported Android devices, or iOS 18.5 or newer for Apple iPhone XS and newer logo display. Older eligible platforms may also have intermittent behavior.
7. **Could the line type reduce display?** Some line types may receive name only, even where richer branded display is supported elsewhere.
8. **Has provisioning had time to propagate?** Newly approved brands, numbers, or updates may take time before downstream display behavior stabilizes.
9. **Is the behavior inconsistent on the same destination?** Network path, dialer/call-screening app, and carrier/device handling can cause occasional differences. Collect examples before escalating.

If the issue remains after these checks, collect the details in **What to send Telnyx Support** below.

## **Why branding may appear on one phone but not another**

It is normal for two recipients to see different results from the same approved calling number. For example:

- One recipient may see your business name and logo.
- Another may see only your business name.
- Another may see standard caller ID only.
- Another may see branding on one device but not after changing phones, SIMs, OS versions, or dialer apps.

This does not necessarily mean your Telnyx Branded Calling setup is incorrect. It usually means the receiving carrier, device, OS, line type, or call path handled the branded information differently.

## **Troubleshooting display issues**

If Branded Calling is approved but not visible, check the following:

1. Confirm the DIR is approved.
2. Confirm the calling number is added to the approved DIR.
3. Confirm the phone number status is active or ready for Branded Calling.
4. Confirm the outbound call uses the approved number as caller ID.
5. Confirm the call is to an eligible US mobile destination.
6. Ask whether the recipient is on a supported carrier and supported device.
7. Ask whether the recipient's device is updated to a current carrier-supported OS version.
8. Ask whether the recipient uses a carrier-provided device, unlocked device, BYOD device, MVNO service, or third-party dialer/call-screening app.
9. Allow for provisioning and downstream propagation time after approval or number changes.

## **What to send Telnyx Support**

If your Branded Calling setup is approved and you still need help, send Telnyx Support:

- Your Enterprise name.
- Your Display Identity Record name.
- The approved calling number.
- The destination number.
- The call date and time, including timezone.
- The receiving carrier, if known.
- The recipient device model, if known.
- The recipient operating system version, if known.
- Whether the recipient device is carrier-purchased, unlocked, BYOD, or on an MVNO.
- What the recipient saw on the incoming call screen.
- A screenshot from the recipient's device, if available.

## **FAQ**

## **Does Branded Calling display on every call?**

No. Telnyx applies approved Branded Calling information to eligible calls, but display depends on receiving carrier, device, operating system, dialer app, line type, and network path.

## **Why does one recipient see my logo while another only sees my name?**

Different devices and carriers support different branded elements. Some scenarios support name, logo, and call reason; others may support name only.

## **Can unlocked or bring-your-own devices display Branded Calling?**

Sometimes, but behavior varies. Carrier-provisioned devices generally have the most predictable branded display behavior. Unlocked, bring-your-own, and MVNO devices may show reduced branding or no branding depending on their provisioning and software support.

## **Does updating the recipient's phone help?**

It can. Some branded display behavior depends on the recipient's operating system version and dialer support. Keeping the device on a supported, current OS version may improve display behavior.

## **Does Telnyx control whether the recipient's phone displays the brand?**

Telnyx controls whether approved branded information is applied to eligible outbound calls from your approved numbers. The final display is controlled by the receiving carrier, recipient device, operating system, and call-screening or dialer behavior.

---

Related Articles

- [Troubleshooting Call Completion](https://support.telnyx.com/en/articles/5025298-troubleshooting-call-completion)
- [Google Verified Calls FAQ](https://support.telnyx.com/en/articles/5941652-google-verified-calls-faq)
- [Inbound Call Screening](https://support.telnyx.com/en/articles/8037040-inbound-call-screening)
- [Calls Per Second (CPS) Limits](https://support.telnyx.com/en/articles/15668484-calls-per-second-cps-limits)
