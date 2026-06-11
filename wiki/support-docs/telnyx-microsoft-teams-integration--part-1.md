---
title: Telnyx Microsoft Teams Integration
summary: 'Telnyx offers three methods to connect Microsoft Teams to the PSTN: Direct
  Routing via the Telnyx MS Teams SBC, the Call2Teams third-party add-on, and the
  Microsoft Operator Connect program. This page covers the setup procedures for each
  method, including prerequisites, step-by-step configuration, and troubleshooting
  for TLS and SIP Options warnings.'
sources:
- url: https://support.telnyx.com/en/articles/5253876-configuring-telnyx-with-microsoft-teams-direct-routing
- url: https://support.telnyx.com/en/articles/6133589-ms-teams-call2teams-telnyx
- url: https://support.telnyx.com/en/articles/7260976-operator-connect-guide-microsoft-teams
- url: https://support.telnyx.com/en/articles/7048813-tls-sip-warnings-for-teams
updated_at: 2026-06-11T11:39:52Z
---

# Telnyx Microsoft Teams Integration

*Part 1 of 3 — see also: [Part 2](telnyx-microsoft-teams-integration--part-2.md), [Part 3](telnyx-microsoft-teams-integration--part-3.md)*

Telnyx offers three methods to connect Microsoft Teams to the PSTN: Direct Routing via the Telnyx MS Teams SBC, the Call2Teams third-party add-on, and the Microsoft Operator Connect program. This page covers the setup procedures for each method, including prerequisites, step-by-step configuration, and troubleshooting for TLS and SIP Options warnings.

## Integration Methods Overview

Telnyx supports three distinct approaches for integrating with Microsoft Teams:

| Method | Description | Key Requirement |
|---|---|---|
| **Direct Routing** | Uses the Telnyx MS Teams SBC (`mstsbc.telnyx.tech`) to interconnect Teams with the Telnyx telephony platform. Customers connect via an auto-generated subdomain and token authentication. | Microsoft Teams E5 license or Phone System add-on |
| **Call2Teams** | A third-party add-on that connects Teams to any PBX or SIP trunk, including Telnyx. | Call2Teams subscription + Global admin access |
| **Operator Connect** | A Microsoft-managed program where Telnyx is listed as an operator in the Teams admin center. Synchronisation between Telnyx and Microsoft accounts is required. | Microsoft 365 E5 license + Microsoft Teams Phone license |

---

## Direct Routing Prerequisites

Before configuring Direct Routing, ensure you have:

- A Telnyx account with at least one purchased number. See the [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) for account setup.
- A Microsoft Teams **E5** license assigned to each user who will make and receive PSTN calls (or an equivalent base plan with the required add-on).
- Global Administrator access to the Microsoft 365 admin center. Verify your role at **Users → Active Users → [Your User] → Account → Roles → Manage roles**.

### Microsoft Licensing for Direct Routing

| Base Plan | Add-On Required for Direct Routing |
|---|---|
| Microsoft Business Basic / Standard / Premium | Microsoft 365 Business Voice without Calling Plan |
| Microsoft Office 365 Enterprise E1 / E3 / F3 / A1 / A3 | Phone System |
| Microsoft Office 365 Enterprise E5 | No add-on required |

---

## Direct Routing Setup

### Step 1 — Create the SIP Connection in Telnyx

1. In the [Telnyx Mission Control Portal](https://portal.telnyx.com/), navigate to the **SIP Connections** page.
2. Click **Create SIP Connection** and choose a name.
3. Select the connection type **MS Teams Direct Routing SBC**.
4. **Important:** Note the auto-generated subdomain — it is required in later steps.
5. Click **Next** and configure **Authentication and Routing**, then **Configuration** details.
6. Click **Next**.

### Step 2 — Configure Inbound and Outbound Details

Set the inbound options to your preference. For outbound settings, ensure the assigned Outbound Voice Profile is appropriate (review it under **Voice → Settings → Outbound Profiles**). Click **Next**.

### Step 3 — Assign a Number to the SBC Connection

1. Purchase a number from Telnyx if you have not already done so.
2. Navigate to the **Numbers** section and assign the number to your MS Teams connection (or navigate to the Numbers page and assign the MS Teams connection to the desired DID).
3. Click **Complete**.

### Step 4 — Add the Subdomain in Microsoft 365

1. In the Microsoft 365 admin center, search for **Domains**.
2. Click **Add Domain** and enter the auto-generated subdomain from Step 1 (e.g. `yyyy.mstsbc.telnyx.tech`).
3. Click **Use This Domain**, then verify the domain by selecting **Add a TXT record instead**.
4. Click **Next** and note the TXT value displayed.
5. Return to your SIP Connection settings in the Telnyx portal and navigate to the **Domain Validation** header (top right). Paste the TXT value into the **TXT Value** text box.
   - The TXT Name and TTL fields are auto-populated and cannot be edited.
   - Do **not** include the `.mstsbc.telnyx.tech` suffix in the `txt_name` field — use only the identifier portion (e.g. `1234abc` instead of `1234abc.mstsbc.telnyx.tech`).
6. Click **Save All Changes** in the Telnyx portal.
7. Return to the Microsoft 365 admin center and click **Verify**.
8. Select **More Options → Skip and do this later**, then click **Next**. Domain setup will be confirmed.

### Step 5 — Activate the Subdomain

1. In the Microsoft 365 admin center, go to **Users → Active Users → Add a user**.
2. Fill in the user details:
   - **Domain:** Select the Telnyx subdomain (`yyyy.mstsbc.telnyx.tech`).
   - Assign an E5 license under **Product Licenses**.
3. Click **Add**.
   - You can remove the E5 license from this user once the domain has been added to Direct Routing.

### Step 6 — Add the Telnyx SBC in Direct Routing

> Changes in the Microsoft Teams admin portal may take up to 24 hours to take effect.

1. In the Microsoft Teams admin center, navigate to **Voice → Direct Routing**.
2. Click the **SBCs** tab, then click **Add**.
3. Enter the auto-generated subdomain from Step 1.
4. Provide the following settings:
   - **Enabled:** On
   - **SIP Signaling port:** `5061`
   - **Send SIP options:** On
   - **Forward P-Asserted-Identity (PAI) header:** On (if you want anonymous calls to connect)
5. Click **Save**.

### Step 7 — Create Voice Routes

1. Navigate to **Voice → Direct Routing → Voice routes** tab.
2. Click **Add** and enter a name and description.
3. Set the priority and dialed number pattern:
   - **US numbers:** prepend `1`, match pattern `NXXNXXXXXX`; or prepend blank, match pattern `1NXXNXXXXXX`
   - **International numbers:** prepend the country dialing prefix, match pattern `NXXNXXXXXX`; or prepend blank, match pattern `(country prefix)NXXNXXXXXX`

### Step 8 — Enroll the SBC

1. From the **Direct Routing** page, navigate to **SBCs enrolled**.
2. Click **Add SBCs**, select the desired SBCs, and click **Apply**.

### Step 9 — Add PSTN Usage Records

1. Navigate to **Voice → Direct Routing** and find the **PSTN usage records** section.
2. Click **Add PSTN usage** and select the desired records. (The pattern `^(.*)$` allows dialling any destination; use a more restrictive pattern if needed.)
3. Click **Apply**.
4. Under **Voice → Voice Routing Policies**, in the **PSTN usage records** section, click **Add PSTN usage** and select **Telnyx**.
5. Click **Save**.

### Step 10 — Configure Voice Routing Policies

1. Navigate to **Voice → Voice Routing Policies**.
2. Click **Add**.
3. Name the policy **TELNYX** and add a description.
4. Add the PSTN usage record created in the previous step.
5. Save the policy.

### Step 11 — Assign Dial Plan and Voice Routing Policies

1. Navigate to **Users** and click the **Policies** tab.
2. Select **Edit** and assign:
   - **Dial Plan:** Telnyx
   - **Voice Routing Policy:** Telnyx
3. Click **Apply**.

### Step 12 — Assign a Telnyx DID to On-Premises PSTN Connectivity

1. Go to [admin.teams.microsoft.com](https://admin.teams.microsoft.com/) → **Manage Users** and click the intended user.
2. Under **Account**:
   - Enable the **Enterprise Voice** toggle.
   - Click **Assign a primary phone number**.
3. In the side panel, add the phone number and click **Apply**.

---
