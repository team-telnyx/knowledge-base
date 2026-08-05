---
title: Telnyx SIP Connection Configuration Guide
summary: This page consolidates Telnyx guidance on configuring SIP connections, including
  IP and credentials-based authentication, failover and retry behavior, multi-device
  registration, tech prefixes, X-Telnyx-Token authentication, P-Charge-Info headers,
  and PBX-specific setup examples for FreePBX, FreeSWITCH, and FusionPBX.
sources:
- url: https://support.telnyx.com/en/articles/1130715-register-multiple-devices-on-one-connection
- url: https://support.telnyx.com/en/articles/1176364-sip-connection-failover-guide-ip-fqdn-based
- url: https://support.telnyx.com/en/articles/12580765-configure-p-charge-info-for-private-pbx-example-freepbx
- url: https://support.telnyx.com/en/articles/12580952-configure-token-authentication-header-x-telnyx-token-in-freepbx
- url: https://support.telnyx.com/en/articles/1616935-freeswitch-ip-trunk-setup
- url: https://support.telnyx.com/en/articles/1618801-freeswitch-credentials-trunk
- url: https://support.telnyx.com/en/articles/2602782-ip-authentication-with-tech-prefix
- url: https://support.telnyx.com/en/articles/3220393-fusionpbx-telnyx-credentials
- url: https://support.telnyx.com/en/articles/4305158-api-keys-and-how-to-use-them
- url: https://support.telnyx.com/en/articles/4320364-sip-connection-fail-over-and-retries
- url: https://support.telnyx.com/en/articles/4860170-ip-authentication-with-x-telnyx-token
updated_at: 2026-08-05T13:32:19Z
---

# Telnyx SIP Connection Configuration Guide

*Part 2 of 5 — see also: [Part 1](telnyx-sip-connection-configuration-guide--part-1.md), [Part 3](telnyx-sip-connection-configuration-guide--part-3.md), [Part 4](telnyx-sip-connection-configuration-guide--part-4.md), [Part 5](telnyx-sip-connection-configuration-guide--part-5.md)*

This page consolidates Telnyx guidance on configuring SIP connections, including IP and credentials-based authentication, failover and retry behavior, multi-device registration, tech prefixes, X-Telnyx-Token authentication, P-Charge-Info headers, and PBX-specific setup examples for FreePBX, FreeSWITCH, and FusionPBX.

## IP Authentication with X-Telnyx-Token

The token setting is found under the **Settings** tab of your [SIP Connections](https://portal.telnyx.com/#/voice/connections) Authentication & Routing Configuration section.

![X-Telnyx-Token setting](_images/8e3293ffa56227f7.png)

When managing numerous clients through a unified IP phone system, Telnyx enables the creation of multiple IP connections that operate under a single IP. Introducing a token requires your SIP INVITEs to carry the specified token within a custom header named **X-Telnyx-Token**. INVITEs must be sent from an IP address associated with the connection for which the token has been configured.

An X-Telnyx-Token is a string of characters configured as the token in the expert settings of your IP authentication connection. When you select the Token option, the portal suggests a token randomly generated using the connection's name (for example, a connection named "Chicago" might suggest **Chicagoqwhowg6ze2d7o**). You can use a custom string instead, but it must:

- Contain only alphanumeric characters and dashes ("-")
- Be between 12 and 48 characters
- Be globally unique

## P-Charge-Info Header for Private PBX (FreePBX Example)

Some carriers and services, including Telnyx, use the **P-Charge-Info** SIP header to identify the billing number associated with a call. When using a private PBX like FreePBX, you can manually configure this header so that calls sent through your SIP trunk include the correct DID (billing number) in the SIP INVITE.

By default, calls sent from your PBX to Telnyx via SIP trunk do not include a P-Charge-Info header. With the header configured, the PBX injects a P-Charge-Info header into SIP INVITE messages containing a specific DID from the Telnyx connection, and Telnyx uses this DID for call identification.

This configuration applies only when your PBX sends calls via IP-based SIP trunks. If multiple IP trunks are configured, apply the rule only to the relevant one.

### Pre-requisites

- A Telnyx SIP Connection configured for outbound calling
- Access to your FreePBX Admin interface and the underlying server filesystem
- The DID number (E.164 format) that should appear in the P-Charge-Info header
- Root or admin privileges to edit FreePBX configuration files

### Configuration Steps

1. **Locate the custom extension configuration file** at `/etc/asterisk/extensions_custom.conf`. This file extends default dial plan behavior safely without affecting future system updates.
2. **Add the P-Charge-Info configuration block** at the bottom of the file:

   ```
   [macro-dialout-trunk-predial-hook] exten => s,1,NoOp(Entering user defined context [macro-dialout-trunk-predial-hook] in extensions_custom.conf) same => n,GoSub(func-set-sipheader,s,1(P-Charge-Info,+1541234567)) same => n,Verbose(2,Added P-Charge-Info: +1541234567) same => n,MacroExit()
   ```

   Replace `+1541234567` with your actual DID number from the Telnyx connection. This macro ensures every outbound call includes the P-Charge-Info header in the SIP INVITE.
3. **Apply and reload configuration** by running `fwconsole reload` from **Admin → CLI** in FreePBX or via SSH. This reloads the Asterisk configuration without requiring a full restart.
4. **Verify the header** by enabling SIP debug on the Asterisk console with `asterisk -rvv sip set debug on`, placing an outbound call through the configured trunk, and checking the INVITE message for `P-Charge-Info: +1541234567`.

### Tips

- This assumes one IP-based trunk; the macro applies to all IP trunks by default. Update to target a specific trunk if required.
- Ensure the DID matches the number assigned to your Telnyx connection.
- If calls fail after applying the macro, comment out the new lines and reload to troubleshoot.
- Always back up `extensions_custom.conf` before editing.

## X-Telnyx-Token Header in FreePBX

When sending calls from a private PBX to Telnyx via IP-based SIP trunks, you can authenticate those calls using a connection token by adding a custom SIP header — **X-Telnyx-Token** — to each outbound SIP INVITE. Telnyx validates this token against the configured SIP connection in your account.

By default, calls are authenticated using IP for setups explicitly using IP Auth, and no token is included in SIP INVITEs. With the token header configured, FreePBX injects an X-Telnyx-Token header in every outbound INVITE, and Telnyx verifies the token and authorizes the call. This setup assumes there is only one IP-based trunk; if multiple IP trunks exist, the header will be added to all unless scoped to the target connection in the macro.

### Pre-requisites

- A Telnyx SIP Connection set up for outbound calls
- Your Telnyx Connection Token from the [Telnyx Mission Control Portal](https://portal.telnyx.com/)
- Admin or root access to your FreePBX system
- Permission to edit Asterisk configuration files

### Configuration Steps

1. **Locate the custom extensions config file** at `/etc/asterisk/extensions_custom.conf`.
2. **Add the token authentication macro** by appending the following to the file:

   ```
   [macro-dialout-trunk-predial-hook]
   exten => s,1,NoOp(Entering user defined context [macro-dialout-trunk-predial-hook] in extensions_custom.conf)
   same => n,GoSub(func-set-sipheader,s,1(X-Telnyx-Token,TOKENFROMPORTAL)) same => n,Verbose(2,Added X-Telnyx-Token universally)
   same => n,MacroExit()
   ```

   Replace `TOKENFROMPORTAL` with your actual token from the Telnyx Portal.
3. **Apply and reload configuration** by running `fwconsole reload`.
4. **Verify the header** by accessing the Asterisk console with `asterisk -rvv`, enabling SIP debugging with `sip set debug on`, placing an outbound call, and looking for `X-Telnyx-Token: TOKENFROMPORTAL` in the INVITE request.

### Tips

- Validate the token in the Telnyx Portal before applying.
- Scope logic carefully if multiple IP trunks exist.
- Back up `extensions_custom.conf` before editing.
