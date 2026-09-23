---
source_url: https://support.telnyx.com/en/articles/importance-of-x-telnyx-username-in-first-invite
title: "Importance of X-Telnyx-Username in the First INVITE"
description: "Why sending X-Telnyx-Username in the first SIP INVITE matters for credential-based connections, and what happens when IP auth takes precedence without it. See Telnyx guidance and requirements."
scraped: 2026-09-23
---

# Importance of X-Telnyx-Username in the First INVITE

Why sending X-Telnyx-Username in the first SIP INVITE matters for credential-based connections, and what happens when IP auth takes precedence without it. See Telnyx guidance and requirements.

When your PBX or SBC sends a SIP INVITE to Telnyx using a **credential-based connection**, including the `X-Telnyx-Username` header in the **first** INVITE is critical for correct call routing. Without it, Telnyx cannot identify your connection from credentials alone in the initial message, and the system may match your call to a different account using IP authentication — causing call failures with a **D51** rejection.

---

## Why X-Telnyx-Username matters

Telnyx identifies incoming SIP traffic using one of several authentication methods depending on your connection type:

* **Credential-based connections** authenticate using a SIP username and password.
* **IP-based connections** authenticate using the source IP address of the SIP signaling.
* **FQDN-based connections** authenticate using a Fully Qualified Domain Name.

For credential-based connections, Telnyx needs to know which connection a call belongs to **before** it can apply connection-specific settings such as [AnchorSite®](https://support.telnyx.com/en/articles/5271423-guide-to-sip-anchorsite-settings), inbound routing rules, or number ownership checks.

When the `X-Telnyx-Username` header is present in the first INVITE, Telnyx immediately identifies the correct connection and account. When it is absent, Telnyx must fall back to other identification methods — and this is where problems can arise.

---

## What happens when X-Telnyx-Username is missing

If your SIP INVITE arrives without `X-Telnyx-Username` in the first message:

1. **AnchorSite® is not honored** — the routing logic cannot determine the correct account or connection from credentials alone in the initial message, so the AnchorSite® setting on your connection is not applied.

2. **IP authentication takes precedence** — if the source IP address of the SIP INVITE matches an IP-authenticated connection on **any** Telnyx account, that IP auth match takes precedence over credential-based authentication. The call is routed to whichever account owns the matching IP-auth connection, not necessarily the account that owns the credential-based connection you intended to use.

This is not a bug — it is the expected behavior when no username is provided in the initial INVITE. The system must identify the call somehow, and IP matching is the fallback mechanism.

---

## The D51 error

When IP auth precedence causes a call to be routed to the wrong account, the receiving account typically does not own the destination number. The call is rejected with a **403 Forbidden** response containing the code **D51**.

D51 indicates that the call was rejected because the destination number is not found on the account that the call was routed to. This happens because:

* The SIP INVITE was sent without `X-Telnyx-Username`.
* The source IP matched an IP-auth connection on a different account.
* That account does not own the number being dialed.
* The call is rejected with 403 D51.

### Example scenario

A customer using credential-based authentication sends calls from a shared SBC IP address. Another Telnyx account adds that same IP to their IP-auth connection. When the first customer sends an INVITE without `X-Telnyx-Username`:

* The system matches the source IP to the other account's IP-auth connection.
* The call is routed to the wrong account.
* The wrong account does not own the destination number.
* The call fails with 403 D51.

This can happen with **shared SBC IPs**, **elastic/cloud IPs**, or any scenario where the same public IP is used by multiple Telnyx accounts.

---

## How to include X-Telnyx-Username in the first INVITE

Add the `X-Telnyx-Username` header to the first SIP INVITE your PBX or SBC sends to Telnyx. The value is the **username** of your credential-based SIP Connection.

### Finding your SIP Connection username

1. Navigate to **Voice → SIP Trunking → SIP Connections** in the Mission Control Portal.
2. Select your credential-based connection.
3. Go to the **Authentication & Routing Configuration** section.
4. Copy the **Username** value.

### Example SIP INVITE with X-Telnyx-Username

```text
INVITE sip:+1800XXXXXXX@sip.telnyx.com SIP/2.0
Via: SIP/2.0/TLS 54.77.38.86:5061;branch=z9hG4bK...
From: <sip:+1800XXXXXXX@54.77.38.86:5061>;tag=...
To: <sip:+1800XXXXXXX@sip.telnyx.com>
Contact: <sip:sbc@54.77.38.86:5061;transport=tls>
X-Telnyx-Username: 3e2d6b71-96fc-4be5-9662-99b638005c1a
```

The `X-Telnyx-Username` value is the connection's username — a UUID-format string like `3e2d6b71-96fc-4be5-9662-99b638005c1a`.

### Configuration examples

**Asterisk (pjsip.conf):**

```ini
[transport-tls]
type=transport
protocol=tls
bind=0.0.0.0:5061

[my-telnyx-auth]
type=auth
auth_type=userpass
username=3e2d6b71-96fc-4be5-9662-99b638005c1a
password=your_password
```

In your dialplan, add the header to outbound calls:

```text
exten => _X.,1,Set(PJSIP_HEADER(add,X-Telnyx-Username)=3e2d6b71-96fc-4be5-9662-99b638005c1a)
```

**FreePBX:**

In your outbound trunk settings, add a custom header under **Advanced Settings → Custom SIP Headers**:

```text
X-Telnyx-Username: 3e2d6b71-96fc-4be5-9662-99b638005c1a
```

**Generic SBC:**

Most SBCs allow you to add custom SIP headers to outbound INVITEs. Consult your SBC documentation for instructions on adding a custom header to the initial INVITE message.

---

## Best practices for shared IPs

If your deployment uses shared or elastic IP addresses (for example, a cloud SBC that serves multiple tenants), follow these recommendations:

* **Always send `X-Telnyx-Username` in the first INVITE** for credential-based connections. This is the most reliable way to ensure correct routing.

* **Use IP + Token or IP + Tech Prefix** for IP-based connections when the IP is shared. These provide unique identification beyond the IP address alone. See:
  * [IP Authentication with X-Telnyx-Token](https://support.telnyx.com/en/articles/4860170-ip-authentication-with-x-telnyx-token)
  * [IP Authentication with Tech Prefix](https://support.telnyx.com/en/articles/2602782-ip-authentication-with-tech-prefix)

* **Avoid adding shared IPs to IP-auth connections** on multiple accounts. If the same public IP is configured as IP-auth on two different Telnyx accounts, calls from that IP without a username or token will match the first account the system finds — which may not be the one you intend.

* **Coordinate with your SBC provider** if you share SBC infrastructure with other Telnyx customers. Ensure each tenant sends a unique identifier (username, token, or tech prefix) so Telnyx can route calls correctly.

---

## AnchorSite® and X-Telnyx-Username

For credential-based connections, the [AnchorSite®](https://support.telnyx.com/en/articles/5271423-guide-to-sip-anchorsite-settings) setting — which determines which Telnyx media server handles your call — requires the connection to be identified in the first INVITE. Without `X-Telnyx-Username`, AnchorSite® cannot be applied and calls may be anchored on a suboptimal media server.

This is documented in the [Guide to SIP AnchorSite® Settings](https://support.telnyx.com/en/articles/5271423-guide-to-sip-anchorsite-settings): credential-based connections must include the SIP Connection's username in the Contact header or as the `X-Telnyx-Username` header in the first SIP INVITE for AnchorSite® to work.

---

## Troubleshooting

### Calls fail with 403 D51

* Check whether your PBX/SBC is sending `X-Telnyx-Username` in the **first** INVITE (not in a subsequent message or re-INVITE).
* Verify the username value matches your SIP Connection's username in the Mission Control Portal.
* Check whether the source IP is also configured as an IP-auth connection on another Telnyx account. If so, IP auth may be taking precedence.
* If you control both accounts, remove the overlapping IP-auth configuration from the account that should not own it.
* If you do not control the other account, contact Telnyx support — the IP may need to be added to [Shared IP Protection](https://support.telnyx.com/en/articles/noc-274-shared-ip-protection).

### AnchorSite® not working

* Confirm `X-Telnyx-Username` is present in the first INVITE.
* Check that the username matches your credential-based SIP Connection.
* Verify your firewall allows ICMP ping from Telnyx media IPs (needed for latency-based AnchorSite®).

### Calls work intermittently

* If calls sometimes succeed and sometimes fail with D51, another account may have intermittently added your IP to their IP-auth configuration.
* Sending `X-Telnyx-Username` on every call eliminates this variability.

---

## Key takeaway

**Always send `X-Telnyx-Username` in the first SIP INVITE for credential-based connections.** This ensures Telnyx identifies your connection correctly, honors your AnchorSite® setting, and routes your calls to the right account — regardless of what other IP-auth configurations exist on the platform.

---

Related Articles

[SIP Connection: Types](https://support.telnyx.com/en/articles/4245868-sip-connection-types)[Guide to SIP AnchorSite® Settings](https://support.telnyx.com/en/articles/5271423-guide-to-sip-anchorsite-settings)[IP Authentication with X-Telnyx-Token](https://support.telnyx.com/en/articles/4860170-ip-authentication-with-x-telnyx-token)[IP Authentication with Tech Prefix](https://support.telnyx.com/en/articles/2602782-ip-authentication-with-tech-prefix)[SIP Connection: Settings](https://support.telnyx.com/en/articles/4351104-sip-connection-settings)

Did this answer your question?

😞😐😃
