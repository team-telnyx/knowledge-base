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

*Part 2 of 3 — see also: [Part 1](telnyx-microsoft-teams-integration--part-1.md), [Part 3](telnyx-microsoft-teams-integration--part-3.md)*

Telnyx offers three methods to connect Microsoft Teams to the PSTN: Direct Routing via the Telnyx MS Teams SBC, the Call2Teams third-party add-on, and the Microsoft Operator Connect program. This page covers the setup procedures for each method, including prerequisites, step-by-step configuration, and troubleshooting for TLS and SIP Options warnings.

## Call2Teams Setup

Call2Teams is a third-party add-on that connects Microsoft Teams to any PBX or SIP trunk. It requires a Call2Teams subscription, a Windows PC, a spare Microsoft 365 user license, and Global admin access to your tenant.

### Prerequisites

- A correctly configured Telnyx portal account with SIP credentials.
- Available DIDs to assign.
- Global admin access to your Microsoft 365 tenant.
- A Call2Teams subscription.

### Step 1 — Set Up the Office 365 Tenant

1. After creating a Call2Teams subscription, accept the email invitation and log in with your Office 365 account (associated with the target organisation and with global-level access).
2. Give Call2Teams permission to connect to your 365 account. **You must check the "Connect on behalf of your organization" checkbox.**
3. Click **Accept**.

### Step 2 — Connect to Telnyx and Create a SIP Trunk

1. In the Call2Teams admin portal, click the **Service** tab, then the **Trunk** tab, and click **Add New Trunk**.
2. Select **Custom** from the provider drop-down (Telnyx is not yet on the pre-configured list). Click **Proceed with Unsupported Configuration**.
3. Enter the following details:

   | Field | Value |
   |---|---|
   | Service Name | Telnyx Trunk 1 (or your preference) |
   | Country / State | Your country and state |
   | Range Start / Range End | Your Telnyx DIDs (include `+` and country code; add non-sequential DIDs individually with **+ Add Additional Range**) |
   | SIP Domain | `sip.telnyx.com` |
   | Authenticate Type | Registration |
   | Username / Auth Username | Your Telnyx account or sub-account username |
   | Password | Your Telnyx account or sub-account password |
   | Expiry (seconds) | `300` (or leave blank) |
   | Protocol | UDP or TCP |
   | Encrypt Media | No |
   | Propagate Refer | Yes (if you have call centre users; otherwise No for better consultative transfers) |
   | Outside Line Prefix | Leave blank |
   | E164 Number Format | Localized |
   | From Header | SIP Identifier |
   | P-Asserted-Identity Header | Passthrough Caller ID or Trunk User Number |
   | Outbound International Prefix | `011` |
   | Outbound National Prefix | Leave blank |
   | Inbound International Prefix | As appropriate for your region |
   | Inbound National Prefix | Leave blank |

4. Click **Add Trunk**. You can monitor the trunk's health from the Trunk tab.

### Step 3 — Associate a Number with a Team Member

1. Click the **Users** tab, then **Add New User**.
2. Select the user, the trunk you created, and the DID intended for that user.
3. Click **Add**, then click **Sync Now** in the upper right.

---

## Operator Connect Setup

Operator Connect allows Telnyx to appear as a listed operator within the Microsoft Teams admin center.

### Prerequisites

- A Telnyx portal account.
- An active Microsoft 365 subscription with Global Administrator privileges.
- At minimum, a Microsoft 365 E5 license assigned.
- Access to the Microsoft Teams admin portal.
- At least one user with a Microsoft Teams Phone license.

### Step 1 — Log In and Navigate to Microsoft Teams

1. Log into the [Telnyx Mission Control Portal](https://portal.telnyx.com/).
2. Log into your [Microsoft Teams admin account](https://admin.teams.microsoft.com/) with a valid admin account. Note the email associated with your Telnyx account.
3. In the Telnyx portal, navigate to the **Microsoft Teams** tab on the left-hand menu.
4. If you have not already configured Operator Connect, click **Get Started** in the setup wizard.

### Step 2 — Verify Your Email Address

1. In the Microsoft Teams admin center, navigate to **Voice → Operator Connect**.
2. Verify that **Telnyx** is listed among available operators.
3. Ensure the contact email in the Operator Setting page matches the email associated with your Telnyx portal account.
4. In the Telnyx portal setup wizard, select **Yes** to confirm the emails match. This starts a synchronisation of your Telnyx and Microsoft Teams accounts.
5. If accounts do not immediately sync, wait up to 24 hours and check again.

### Step 3 — Assign Numbers

1. In the Telnyx portal's Microsoft Teams section, click the edit button (pencil icon) on your connection and go to the **Numbers** tab.
2. Click **Add Numbers**, select the agent type (Human or Voice App) and country, then click **Next**.
3. If numbers are already purchased, they will appear in the list. Otherwise, click **Buy Numbers** to search and purchase.
4. Add numbers to the Operator Connect setup, select an emergency address from the drop-down, and click **Submit**.
5. Confirm charges. Numbers will appear in the **Number History** tab — orange indicates not yet ready, green indicates ready to use. Use the refresh button to check status.

### Step 4 — Assign a Number to a User in Teams

1. Go to the [Phone Numbers](https://admin.teams.microsoft.com/phone-numbers) page in the Teams admin center.
2. Select a number, click **Edit**, search for a user to assign it to, and click **Apply**.
3. Test by calling from the Teams client — the assigned number will appear below the dial pad.

### Emergency Address Considerations

When setting emergency addresses for Teams, ensure:
- Emergency calling policy is set and assigned to users.
- Dynamic emergency calling is enabled so the actual address is sent when an emergency call is placed.
- A static emergency address in Teams settings is correctly configured as a fallback.

### Pricing

Pricing for Operator Connect bundles is available on the [Bundles Pricing Page](https://portal.telnyx.com/#/bundles/order) in the Telnyx portal.

---
