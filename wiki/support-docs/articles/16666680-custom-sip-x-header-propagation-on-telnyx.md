---
title: "Custom SIP X-Header Propagation on Telnyx"
summary: "Custom SIP X-headers are used by many PBX systems and applications to pass metadata along with call signaling, trace IDs, session context, application-specific identifiers, and more."
sources:
- url: "https://support.telnyx.com/en/articles/16666680-custom-sip-x-header-propagation-on-telnyx"
updated_at: 2026-09-15T00:00:00Z
tags: [support-docs]
source_path: "support-docs/16666680-custom-sip-x-header-propagation-on-telnyx.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/16666680-custom-sip-x-header-propagation-on-telnyx.md -->

# Custom SIP X-Header Propagation on Telnyx

Custom SIP X-headers are used by many PBX systems and applications to pass metadata along with call signaling, trace IDs, session context, application-specific identifiers, and more.

This article describes how custom X-headers behave across the different call paths in the Telnyx SIP Trunking and Programmable Voice ecosystem.

**Terminology:** In this article, **on-net** refers to calls that originate and terminate within the Telnyx network (e.g., Telnyx SIP Trunk to Telnyx SIP Trunk).

**Off-net** refers to calls that terminate to the PSTN or an external carrier outside the Telnyx network.

## **Summary of Behavior**

|  |  |  |
| --- | --- | --- |
| **Call Path** | **Custom X-Headers Preserved?** | **Notes** |
| **SIP Trunk → SIP Trunk (on-net, same account)** | ✅ Yes | Headers pass end-to-end through the Telnyx network |
| **SIP Trunk → SIP Trunk (on-net, cross-account)** | ❌ No | Headers are stripped when routing between trunks on different Telnyx accounts |
| **SIP Trunk → Programmable Voice** | ✅ Yes (with caveat) | Headers appear in webhook custom\_headers; X-Telnyx prefix is reserved and stripped |
| **Programmable Voice → SIP (inbound leg)** | ✅ Yes | Headers injected via Programmable Voice custom\_headers parameter appear on the SIP INVITE leg |
| **Programmable Voice → SIP (same account, on-net)** | ✅ Yes | Headers preserved when routing to a SIP trunk within the same account |
| **Programmable Voice → SIP (different account)** | ❌ No | Headers are stripped when routing to a SIP trunk on a different account |
| **Programmable Voice → PSTN** | ❌ No | Headers are stripped at the Telnyx network boundary before the carrier leg |
| **SIP Trunk → PSTN/Carrier (off-net)** | ❌ No | Headers are stripped at the Telnyx network boundary before the carrier leg |

## **SIP Trunk to SIP Trunk (On-Net, Same Account)**

When a call originates from one Telnyx SIP Trunk and terminates to another Telnyx SIP Trunk **within the same account**, custom X-headers are **preserved end-to-end**. The headers travel through the Telnyx network to the receiving trunk endpoint without modification.

**What you need to know:**

- Any custom X-header (e.g., X-Trace-Id, X-Custom-Header, X-Session-Info) set on the outbound INVITE from your PBX will arrive intact at the receiving PBX.
- Telnyx strips its own internal routing and session headers before delivering the INVITE to the receiving trunk. These are platform-internal and not customer-visible.
- This applies to both credential-based and IP-based SIP trunk connections.

**Example:**

Sending side (Asterisk PJSIP):

```
PJSIP_HEADER(add,X-Trace-Id)=my-trace-12345
PJSIP_HEADER(add,X-Custom-Header)=my-value
```

Receiving side — both headers will be present in the inbound INVITE.

## **SIP Trunk to SIP Trunk (On-Net, Cross-Account)**

When a call routes between two Telnyx SIP Trunks on **different accounts**, custom X-headers are **not preserved**.

The platform strips custom headers when routing across account boundaries.

**What this means:**

- If you are routing calls between trunks that belong to different Telnyx accounts, do not rely on custom X-headers reaching the receiving endpoint.

**Recommendation:** If you need metadata to accompany a cross-account call, use out-of-band mechanisms (webhooks, API callbacks, or your own application-layer signaling) rather than SIP X-headers.

## **SIP Trunk to Programmable Voice**

When a call arrives on a SIP Trunk and is routed to a Programmable Voice application, custom X-headers **are propagated to the Programmable Voice layer** and appear in the custom\_headers array of webhook events (call.initiated, call.hangup, etc.).

**Reserved namespace:** Headers prefixed with `X-Telnyx` are treated as internal/reserved and are **stripped** from the webhook `custom_headers` payload.

This filter is case-insensitive and does not require a dash after `X-Telnyx` — for example, `X-Telnyx-Foo`, `X-TelnyxABC`, and `x-telnyx-lower` are all stripped.\
Do not use the `X-Telnyx` prefix for your custom application headers.

**Example webhook payload (`call.initiated`):**

```
{
  "event_type": "call.initiated",
  "custom_headers": [
    {"name": "X-Trace-Id", "value": "my-trace-12345"},
    {"name": "X-Custom-Header", "value": "my-value"}
  ]
}
```

**Recommendation:** Use prefixes like `X-Custom-*`, `X-Trace-*,` `X-App-*,` or any other non-reserved prefix for your custom headers.

## **Programmable Voice to SIP (Inbound Leg)**

When your application uses Programmable Voice to place an outbound call to a SIP endpoint, you can inject custom X-headers into the SIP INVITE that Telnyx delivers to the destination trunk or endpoint. Programmable Voice accepts a `custom_headers` array in the dial request — these headers are added to the generated SIP INVITE and sent to the receiving party.

This provides a mechanism for one-way header injection from your application into SIP signaling. Common use cases include passing trace IDs for call correlation, application-specific metadata for the receiving PBX, or priority indicators for call routing logic on the receiving side.

**Example (Programmable Voice):**

```
{
  "custom_headers": [
    {"name": "X-App-Trace-Id", "value": "abc-123"},
    {"name": "X-Priority", "value": "high"}
  ]
}
```

These headers will appear in the SIP INVITE delivered to the SIP trunk endpoint.

## **Programmable Voice to SIP (Same Account, On-Net)**

When Programmable Voice routes a call to a SIP trunk endpoint **within the same account**, custom X-headers are **preserved**. The headers injected via the `custom_headers` parameter in the dial request are delivered intact to the receiving SIP trunk endpoint.

This is pure on-net routing — the call never leaves the Telnyx network, so headers pass through without being stripped, mirroring the behavior of same-account SIP Trunk → SIP Trunk calls.

## **Programmable Voice to SIP (Different Account)**

When Programmable Voice routes a call to a SIP trunk endpoint on a **different account**, custom X-headers are **not preserved**.

The platform strips custom headers when routing across account boundaries, consistent with cross-account SIP Trunk → SIP Trunk behavior.

**Recommendation:** If you need metadata to reach a SIP endpoint on a different account, use out-of-band mechanisms (webhooks, API callbacks, or your own application-layer signaling) rather than relying on SIP X-headers.

## **Programmable Voice to PSTN**

When Programmable Voice places a call that terminates to the PSTN or an external carrier, custom X-headers are **not propagated** to the carrier leg. Telnyx generates a fresh INVITE for the outbound carrier leg containing only standard, RFC-compliant SIP headers.

This is by design — Telnyx terminates the application dialog and creates a new outbound dialog for the carrier leg, ensuring SIP compliance and avoiding interoperability issues with carrier equipment.

## **SIP Trunk to PSTN / External Carrier (Off-Net)**

When a call terminates to the PSTN or an external carrier, custom X-headers are **not propagated** to the carrier leg. Telnyx generates a fresh INVITE for the outbound carrier leg containing only standard, RFC-compliant SIP headers.

**Why this happens:** This is by design. Telnyx terminates the inbound dialog and creates a new outbound dialog for the carrier leg. Custom headers are not forwarded to external carriers to ensure SIP compliance and avoid interoperability issues with carrier equipment.

**What you can do instead:**

- Use standard SIP headers for caller information (`P-Asserted-Identity`, `Remote-Party-ID`).
- Use the Diversion header for call forwarding context.
- For application metadata that needs to reach the called party, use out-of-band mechanisms (webhooks, API callbacks, or your own application-layer signaling).

## **Best Practices**

1. **Avoid the X-Telnyx prefix** for custom headers. This namespace is reserved by the platform and headers using it will be stripped from webhook events. The filter is case-insensitive (e.g., `x-telnyx-foo` is also stripped) and does not require a dash separator (e.g., `X-TelnyxABC` is also stripped).
2. **Use descriptive, non-conflicting header names** (e.g., `X-App-Trace-Id,` `X-Session-Context`).
3. Avoid header names that conflict with standard SIP headers (e.g., From, To, Via, `Contact`, `Call-ID`). Custom X-headers should use the `X-` prefix convention and avoid names that SIP proxies may interpret as standard headers.
4. **For trunk-to-trunk calls within the same account**, X-headers are a reliable metadata channel — use them freely.
5. **For calls to the PSTN**, do not rely on custom X-headers reaching the far end. Use out-of-band signaling for metadata that must accompany the call.
6. **For SIP Trunk → Programmable Voice**, X-headers in webhook `custom_headers` provide a bridge between SIP-layer metadata and application-layer logic.
7. **Do not include sensitive data in custom X-headers** without encryption. SIP headers are transmitted in plaintext (unless TLS transport is used) and may be logged by intermediate network elements.

---

Related Articles

- [Configuring a Cisco CUBE/CUCM SIP Trunk](https://support.telnyx.com/en/articles/1130673-configuring-a-cisco-cube-cucm-sip-trunk)
- [Grandstream UCM6xxx: SIP Trunks](https://support.telnyx.com/en/articles/5748258-grandstream-ucm6xxx-sip-trunks)
- [How to Configure a SIP Trunk](https://support.telnyx.com/en/articles/8096455-how-to-configure-a-sip-trunk)
- [BYOC: Telnyx & Genesys](https://support.telnyx.com/en/articles/8268122-byoc-telnyx-genesys)
- [Configure Token Authentication Header (X-Telnyx-Token) in FreePBX](https://support.telnyx.com/en/articles/12580952-configure-token-authentication-header-x-telnyx-token-in-freepbx)
