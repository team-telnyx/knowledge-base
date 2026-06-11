---
source_url: https://support.telnyx.com/en/articles/12580765-configure-p-charge-info-for-private-pbx-example-freepbx
scraped: 2026-06-11
---

Configure P-Charge-Info for Private PBX (Example: FreePBX) | Telnyx Help Center

[Skip to main content](#main-content)

# Configure P-Charge-Info for Private PBX (Example: FreePBX)

Learn how to add a P-Charge-Info SIP header for calls made through your private PBX (using FreePBX as an example).

Written by Telnyx Engineering

October 14, 2025

Table of contents

## Background

Some carriers and services, including Telnyx, use the **P-Charge-Info** SIP header to identify the billing number associated with a call.  
When using a **private PBX** like FreePBX, you can manually configure this header so that calls sent through your SIP trunk include the correct DID (billing number) in the SIP INVITE.

## Standard Behavior

1. Calls are sent from your PBX to Telnyx via SIP trunk.
2. No **P-Charge-Info** header is included by default.

## New Behavior (With P-Charge-Info)

1. PBX injects a **P-Charge-Info** header into SIP INVITE messages.
2. The header includes a specific DID from the Telnyx connection.
3. Telnyx uses this DID call identification.

**Note:** This configuration applies only when your PBX sends calls via IP-based SIP trunks. If multiple IP trunks are configured, apply the rule only to the relevant one.

---

## Pre-requisites

Before you begin, make sure you have:

* A **Telnyx SIP Connection** configured for outbound calling.
* Access to your **FreePBX Admin interface** and the underlying server filesystem.
* The **DID number** (E.164 format) that should appear in the P-Charge-Info header.
* Root or admin privileges to edit FreePBX configuration files.

---

## Step 1: Locate the Custom Extension Configuration File

FreePBX allows for custom dial plan extensions in:

```
/etc/asterisk/extensions_custom.conf
```

This file is used to extend default dial plan behavior safely, without affecting future system updates.

---

## Step 2: Add the P-Charge-Info Configuration Block

Open the `extensions_custom.conf` file and add the following section at the bottom:

```
[macro-dialout-trunk-predial-hook] exten => s,1,NoOp(Entering user defined context [macro-dialout-trunk-predial-hook] in extensions_custom.conf) same => n,GoSub(func-set-sipheader,s,1(P-Charge-Info,+1541234567)) same => n,Verbose(2,Added P-Charge-Info: +1541234567) same => n,MacroExit()
```

Replace **`+1541234567`** with your actual DID number from the Telnyx connection.

**Tip:** This macro ensures that every outbound call includes the P-Charge-Info header in the SIP INVITE.

---

## Step 3: Apply and Reload Configuration

After saving your changes:

1. In FreePBX, go to **Admin → CLI** or SSH into your PBX.
2. Run the following command:

```
fwconsole reload
```

This reloads the Asterisk configuration without requiring a full restart.

---

## Step 4: Verify the Header in SIP Messages

You can confirm that the **P-Charge-Info** header is being sent:

1. Enable SIP debug on the Asterisk console:

   ```
   asterisk -rvv sip set debug on
   ```
2. Place an outbound call through the configured trunk.
3. Check the INVITE message for:

   ```
   P-Charge-Info: +1541234567
   ```

---

## Tips for Success

* This assumes **one IP-based trunk** configured in the setup — the macro applies to all IP trunks by default. Update to target specific trunk if required.
* Ensure the DID matches the number assigned to your Telnyx connection.
* If calls fail after applying the macro, comment out the new lines and reload to troubleshoot.
* Always back up `extensions_custom.conf` before editing.

---

## References

* [Telnyx SIP Connection Setup Guide](https://support.telnyx.com/en/articles/2602782-ip-authentication-with-tech-prefix)
* [Telnyx Trunk with FreePBX V15 Configuration](https://support.telnyx.com/en/articles/5619595-freepbx-v15-ip-trunk-pjsip)

---

Related Articles

[Configuring a FreePBX V13 Credentials Trunk](https://support.telnyx.com/en/articles/1130648-configuring-a-freepbx-v13-credentials-trunk)[FreePBX V14: IP Trunk - ChanSIP](https://support.telnyx.com/en/articles/3284736-freepbx-v14-ip-trunk-chansip)[FreePBX V14: Credentials - ChanSIP](https://support.telnyx.com/en/articles/3284752-freepbx-v14-credentials-chansip)[FreePBX V15: IP Trunk - PJSIP](https://support.telnyx.com/en/articles/5619595-freepbx-v15-ip-trunk-pjsip)[Configure Token Authentication Header (X-Telnyx-Token) in FreePBX](https://support.telnyx.com/en/articles/12580952-configure-token-authentication-header-x-telnyx-token-in-freepbx)

Did this answer your question?

😞😐😃

Table of contents
