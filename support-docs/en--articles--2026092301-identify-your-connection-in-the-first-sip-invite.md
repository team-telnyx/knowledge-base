---
source_url: "https://support.telnyx.com/en/articles/2026092301-identify-your-connection-in-the-first-sip-invite"
title: "Identify Your Connection in the First SIP INVITE"
description: "How to identify a credential-based SIP connection early enough for correct authentication and AnchorSite® routing"
updated_at: "2026-09-29T22:25:13Z"
modified_at: "2026-09-29T22:25:13Z"
collection_path: "2484718-everything-sip"
content_hash: "0dc0bb51c07cd5252ae7a3891100a74e9d6682b7a3fac7559212e9319066cb24"
---

# Identify Your Connection in the First SIP INVITE

How to identify a credential-based SIP connection early enough for correct authentication and AnchorSite® routing

## Overview

For a credential-based SIP connection, include the connection’s SIP username in the very first INVITE sent to Telnyx. This allows Telnyx to identify the intended connection before initial call routing and apply the connection’s configuration, including its AnchorSite® preference.

## Why the first INVITE matters

SIP digest authentication commonly involves an initial INVITE, an authentication challenge, and a subsequent INVITE containing the digest response. Some SIP devices and applications omit the username from the first INVITE and provide it only in the later authentication request.

When the username is missing from the initial INVITE, Telnyx may need to identify the connection using other information, such as the source IP address. This can lead to two issues:

1. **The INVITE may be associated with the wrong connection.** If another Telnyx customer has a SIP connection associated with the same source IP address, Telnyx may identify the initial INVITE as belonging to that other customer. Telnyx may then skip the expected digest challenge for the intended credential-based connection and process the call using the other connection’s configuration. This is especially relevant when using hosted PBX, SBC, or communications platforms that share public IP addresses across customers.
2. **The connection’s AnchorSite® preference may not be honored.** Without the username, Telnyx may not be able to identify the intended connection when the first INVITE arrives. By the time the authenticated INVITE is received, the SIP transaction is already associated with the B2BUA instance that handled the initial INVITE. Telnyx must keep the subsequent request on that same instance, so it may be too late to apply the intended connection’s AnchorSite® routing preference.

## How to include the SIP username

There are two supported ways to provide the connection username in the first INVITE. Use whichever method your SIP device or provider supports; you do not need to include both.

### Option 1: Contact header user part (recommended when supported)

Set the user part of the SIP URI in the Contact header to the exact SIP username configured on your Telnyx connection. This is a common approach supported by most SIP devices and applications.

```text
Contact: <sip:YOUR_SIP_USERNAME@192.0.2.10:5060>
```

### Option 2: X-Telnyx-Username custom header

If your SIP device or provider cannot set the username in the Contact header user part, include it in the custom X-Telnyx-Username header. Telnyx recognizes this header for connection identification. This can be useful with platforms such as LiveKit, where the Contact header user part may not be configurable.

```text
X-Telnyx-Username: YOUR_SIP_USERNAME
```

## Example first INVITE (abbreviated)

```text
INVITE sip:+1XXXXXXXXXX@sip.telnyx.com SIP/2.0
Via: SIP/2.0/TLS 192.0.2.10:5061;branch=z9hG4bK...
From: <sip:+1XXXXXXXXXX@192.0.2.10:5061>;tag=...
To: <sip:+1XXXXXXXXXX@sip.telnyx.com>
Contact: <sip:YOUR_SIP_USERNAME@192.0.2.10:5061;transport=tls>
```

Alternatively, when the Contact header user part cannot carry the username, the initial INVITE can include:

```text
X-Telnyx-Username: YOUR_SIP_USERNAME
```

Replace YOUR_SIP_USERNAME with the exact username of the intended Telnyx credential-based connection. The examples are abbreviated; retain the other SIP headers and parameters required by your environment.

## Important

> The username must be present in the first INVITE—not only in the authenticated retry. Adding it only after receiving a digest challenge does not resolve the initial connection-identification or AnchorSite® routing issue.

## Troubleshooting

If calls are being associated with an unexpected connection or the expected AnchorSite® preference is not taking effect, inspect the first outbound INVITE as it leaves your device or provider. Confirm that either the Contact header user part or the X-Telnyx-Username header contains the intended connection username.
