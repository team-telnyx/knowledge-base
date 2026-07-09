---
source_url: https://support.telnyx.com/en/articles/12580952-configure-token-authentication-header-x-telnyx-token-in-freepbx
scraped: 2026-07-08
content_hash: f3c47f34626edf3edcdeadadd3caf0bea970e047cd00857c49527519aaabc3d3
---

Configure Token Authentication Header (X-Telnyx-Token) in FreePBX | Telnyx Help Center

[Skip to main content](#main-content)

# Configure Token Authentication Header (X-Telnyx-Token) in FreePBX

Add a Telnyx token-based authentication header to outbound SIP calls from your FreePBX PBX system.

Written by Telnyx Engineering

October 15, 2025

Table of contents

## Background

When sending calls from a **private PBX** to Telnyx via IP-based SIP trunks, you can authenticate those calls using a **connection token**.

This is done by adding a custom SIP header — **`X-Telnyx-Token`** — to each outbound SIP INVITE.  
Telnyx validates this token against the configured SIP connection in your account.

## Standard Behavior

1. Calls are authenticated using IP for setups explicitly using IP Auth.
2. No token is included in SIP INVITEs by default.

## New Behavior (With Token Header)

1. FreePBX injects an **`X-Telnyx-Token`** header in every outbound INVITE.
2. Telnyx verifies the token and authorizes the call.

**Note:** This setup assumes there’s **only one IP-based trunk**. If multiple IP trunks exist, the header will be added to all unless scoped to the target connection in the macro.

---

## Pre-requisites

Before starting, ensure you have:

* A **Telnyx SIP Connection** set up for outbound calls.
* Your **Telnyx Connection Token** (from the [Telnyx Mission Control Portal](https://portal.telnyx.com/)).
* Admin or root access to your **FreePBX** system.
* Permission to edit Asterisk configuration files.

---

## Step 1: Locate the Custom Extensions config File

FreePBX stores custom user-defined contexts in:

```
/etc/asterisk/extensions_custom.conf
```

This file allows you to extend dialplan behavior safely without affecting system updates.

---

## Step 2: Add the Token Authentication Macro

Open `/etc/asterisk/extensions_custom.conf` in a text editor and append the following:

```
[macro-dialout-trunk-predial-hook]   
exten => s,1,NoOp(Entering user defined context [macro-dialout-trunk-predial-hook] in extensions_custom.conf)   
same => n,GoSub(func-set-sipheader,s,1(X-Telnyx-Token,TOKENFROMPORTAL)) same => n,Verbose(2,Added X-Telnyx-Token universally)   
same => n,MacroExit()
```

Replace `TOKENFROMPORTAL` with your actual token from the Telnyx Portal.

---

## Step 3: Apply and Reload Configuration

After saving changes, apply them with:

```
fwconsole reload
```

This reloads the Asterisk dialplan without restarting services.

---

## Step 4: Verify the Header

To confirm the header is applied correctly:

1. Access the Asterisk console:

   ```
   asterisk -rvv
   ```
2. Enable SIP debugging:

   ```
   sip set debug on
   ```
3. Place an outbound call.
4. In the INVITE request, look for:

   ```
   X-Telnyx-Token: TOKENFROMPORTAL
   ```

---

## Tips for Success

* **Validate the token** in the Telnyx Portal before applying.
* **Scope logic carefully** if multiple IP trunks exist.
* Backup `extensions_custom.conf` before editing.

---

## References

* [Telnyx SIP Connection Setup Guide](https://support.telnyx.com/en/articles/2602782-ip-authentication-with-tech-prefix)
* [Telnyx Trunk with FreePBX V15 Configuration](https://support.telnyx.com/en/articles/5619595-freepbx-v15-ip-trunk-pjsip)

---

Related Articles

[Configuring a FreePBX V13 Credentials Trunk](https://support.telnyx.com/en/articles/1130648-configuring-a-freepbx-v13-credentials-trunk)[FreePBX V14: Credentials - ChanSIP](https://support.telnyx.com/en/articles/3284752-freepbx-v14-credentials-chansip)[Setting Up FreePBX V15 with Telnyx API](https://support.telnyx.com/en/articles/5464056-setting-up-freepbx-v15-with-telnyx-api)[FreePBX V15: IP Trunk - PJSIP](https://support.telnyx.com/en/articles/5619595-freepbx-v15-ip-trunk-pjsip)[Configure P-Charge-Info for Private PBX (Example: FreePBX)](https://support.telnyx.com/en/articles/12580765-configure-p-charge-info-for-private-pbx-example-freepbx)

Did this answer your question?

😞😐😃

Table of contents
