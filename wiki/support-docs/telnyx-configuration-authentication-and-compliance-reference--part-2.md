---
title: Telnyx Configuration, Authentication, and Compliance Reference
summary: This page consolidates Telnyx support guidance on whitelisting SIP signaling,
  media, and webhook IP addresses; IP authentication methods (tech prefix, X-Telnyx-Token,
  P-Charge-Info) including FreePBX configuration; multi-device registration limits;
  AI Assistant configuration with tools, handoffs, transfers, and MCP servers; UK
  TPS compliance for marketing calls; and the public Knowledge Agent bot-to-bot support
  API.
sources:
- url: https://support.telnyx.com/en/articles/10007243-whitelisting-telnyx-media-ip-addresses
- url: https://support.telnyx.com/en/articles/1130687-whitelisting-telnyx-ip-addresses
- url: https://support.telnyx.com/en/articles/1130715-register-multiple-devices-on-one-connection
- url: https://support.telnyx.com/en/articles/12232444-comprehensive-ai-assistants-configuration-walk-through
- url: https://support.telnyx.com/en/articles/12580765-configure-p-charge-info-for-private-pbx-example-freepbx
- url: https://support.telnyx.com/en/articles/12580952-configure-token-authentication-header-x-telnyx-token-in-freepbx
- url: https://support.telnyx.com/en/articles/15455646-bot-to-bot-support-api-ask-telnyx-knowledge-agent
- url: https://support.telnyx.com/en/articles/2602782-ip-authentication-with-tech-prefix
- url: https://support.telnyx.com/en/articles/4860170-ip-authentication-with-x-telnyx-token
- url: https://support.telnyx.com/en/articles/6136385-uk-tps-register-guidelines
- url: https://support.telnyx.com/en/collections/133094-general-telnyx-portal-account
- url: https://support.telnyx.com/en/collections/19623087-ai-assistant
updated_at: 2026-07-17T08:59:35Z
---

# Telnyx Configuration, Authentication, and Compliance Reference

*Part 2 of 4 — see also: [Part 1](telnyx-configuration-authentication-and-compliance-reference--part-1.md), [Part 3](telnyx-configuration-authentication-and-compliance-reference--part-3.md), [Part 4](telnyx-configuration-authentication-and-compliance-reference--part-4.md)*

This page consolidates Telnyx support guidance on whitelisting SIP signaling, media, and webhook IP addresses; IP authentication methods (tech prefix, X-Telnyx-Token, P-Charge-Info) including FreePBX configuration; multi-device registration limits; AI Assistant configuration with tools, handoffs, transfers, and MCP servers; UK TPS compliance for marketing calls; and the public Knowledge Agent bot-to-bot support API.

## IP Authentication Methods

When multiple connections share a single public IP, Telnyx offers three methods to uniquely identify each connection: tech prefix, X-Telnyx-Token, and P-Charge-Info.

### IP Authentication with Tech Prefix

The tech prefix setting is found under the Settings tab of your SIP Connections, in the Authentication & Routing Configuration section.

![Authentication & Routing Configuration section](_images/beb6baa7d1d09998.png)

A tech prefix is a 4-digit number prefixed to the dialed number. For example, with a tech prefix of "1234" and a destination of "18005678912", you would dial "123418005678912". Your phone system's outbound settings can be configured to automatically prepend the tech prefix to all calls.

If the tech prefix is not included on outbound calls sent to Telnyx, the call will not be recognized, leading to a SIP 407 Proxy Authentication response and call rejection.

Tech prefixes can also be applied at the number level for more granular control of call routing and identification.

#### Termination Endpoint Error

While connections can share the same IP address, they must be uniquely identified to avoid the "Termination Endpoint" error. This error occurs when another connection with the same IP address is already assigned to an outbound voice profile. To prevent this, ensure each connection has a unique combination, achieved through a tech prefix, token, or P-Charge-Info.

### IP Authentication with X-Telnyx-Token

The token setting is found under the Settings tab of your SIP Connections, in the Authentication & Routing Configuration section.

![](_images/8e3293ffa56227f7.png)

An X-Telnyx-Token is a string of characters configured as the Token in the expert settings of your IP authentication connection. When you select the Token option, the portal suggests a token randomly generated from the connection's name (for example, `Chicagoqwhowg6ze2d7o` for a connection named Chicago).

You may use a custom string instead, but it must:

- Contain only alphanumeric characters and dashes ("-")
- Be between 12 and 48 characters
- Be globally unique

When using a token, your SIP INVITEs must carry the specified token within a custom header named `X-Telnyx-Token`. INVITEs must also be sent from an IP address associated with the connection for which the token has been configured.

### Configuring X-Telnyx-Token in FreePBX

When sending calls from a private PBX to Telnyx via IP-based SIP trunks, you can authenticate calls using a connection token by adding a custom `X-Telnyx-Token` header to each outbound SIP INVITE. Telnyx validates this token against the configured SIP connection.

**Pre-requisites:**

- A Telnyx SIP Connection set up for outbound calls
- Your Telnyx Connection Token from the [Telnyx Mission Control Portal](https://portal.telnyx.com/)
- Admin or root access to your FreePBX system
- Permission to edit Asterisk configuration files

**Step 1 — Locate the custom extensions config file:**

FreePBX stores custom user-defined contexts in `/etc/asterisk/extensions_custom.conf`, which allows you to extend dialplan behavior safely without affecting system updates.

**Step 2 — Add the token authentication macro:**

Append the following to `/etc/asterisk/extensions_custom.conf`:

```
[macro-dialout-trunk-predial-hook]   
exten => s,1,NoOp(Entering user defined context [macro-dialout-trunk-predial-hook] in extensions_custom.conf)   
same => n,GoSub(func-set-sipheader,s,1(X-Telnyx-Token,TOKENFROMPORTAL)) same => n,Verbose(2,Added X-Telnyx-Token universally)   
same => n,MacroExit()
```

Replace `TOKENFROMPORTAL` with your actual token from the Telnyx Portal.

**Step 3 — Apply and reload configuration:**

```
fwconsole reload
```

**Step 4 — Verify the header:**

1. Access the Asterisk console: `asterisk -rvv`
2. Enable SIP debugging: `sip set debug on`
3. Place an outbound call and look for `X-Telnyx-Token: TOKENFROMPORTAL` in the INVITE request.

**Tips:**

- Validate the token in the Telnyx Portal before applying
- Scope logic carefully if multiple IP trunks exist
- Backup `extensions_custom.conf` before editing

### Configuring P-Charge-Info in FreePBX

Some carriers and services, including Telnyx, use the P-Charge-Info SIP header to identify the billing number associated with a call. When using a private PBX like FreePBX, you can manually configure this header so that calls sent through your SIP trunk include the correct DID (billing number) in the SIP INVITE.

**Pre-requisites:**

- A Telnyx SIP Connection configured for outbound calling
- Access to your FreePBX Admin interface and the underlying server filesystem
- The DID number (E.164 format) that should appear in the P-Charge-Info header
- Root or admin privileges to edit FreePBX configuration files

**Step 1 — Locate the custom extension configuration file:**

FreePBX allows custom dial plan extensions in `/etc/asterisk/extensions_custom.conf`.

**Step 2 — Add the P-Charge-Info configuration block:**

```
[macro-dialout-trunk-predial-hook] exten => s,1,NoOp(Entering user defined context [macro-dialout-trunk-predial-hook] in extensions_custom.conf) same => n,GoSub(func-set-sipheader,s,1(P-Charge-Info,+1541234567)) same => n,Verbose(2,Added P-Charge-Info: +1541234567) same => n,MacroExit()
```

Replace `+1541234567` with your actual DID number from the Telnyx connection.

**Step 3 — Apply and reload configuration:**

```
fwconsole reload
```

**Step 4 — Verify the header in SIP messages:**

1. Enable SIP debug: `asterisk -rvv sip set debug on`
2. Place an outbound call through the configured trunk
3. Check the INVITE message for `P-Charge-Info: +1541234567`

**Tips:**

- This assumes one IP-based trunk; the macro applies to all IP trunks by default
- Ensure the DID matches the number assigned to your Telnyx connection
- If calls fail after applying the macro, comment out the new lines and reload to troubleshoot
- Always back up `extensions_custom.conf` before editing

## Registering Multiple Devices on One Connection

Telnyx Mission Control is designed for multi-tenant environments. You can create as many connections as needed to support all your customers and end-users.

If you create a credentials-based connection, you can register it to any device, but only one device can be actively registered at any one time. For example, if you register your connection to an IP phone in your office and then register it to a softphone application while on the go, calls will only come and go from the softphone and not to the IP phone, which becomes an unregistered device.
