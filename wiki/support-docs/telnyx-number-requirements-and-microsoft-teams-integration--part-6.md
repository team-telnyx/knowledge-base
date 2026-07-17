---
title: Telnyx Number Requirements and Microsoft Teams Integration
summary: This page consolidates Telnyx documentation covering DID number requirements
  for Reunion, Australia, and New Zealand, Australian emergency services and IPND,
  and Microsoft Teams integration guides including Direct Routing, Call2Teams, TLS/SIP
  warnings, Operator Connect, and emergency call routing.
sources:
- url: https://support.telnyx.com/en/articles/13720024-reunion-did-requirements
- url: https://support.telnyx.com/en/articles/3505912-australia-did-requirements
- url: https://support.telnyx.com/en/articles/5253876-configuring-telnyx-with-microsoft-teams-direct-routing
- url: https://support.telnyx.com/en/articles/5466823-new-zealand-did-requirements
- url: https://support.telnyx.com/en/articles/6133589-ms-teams-call2teams-telnyx
- url: https://support.telnyx.com/en/articles/7048813-tls-sip-warnings-for-teams
- url: https://support.telnyx.com/en/articles/7260976-operator-connect-guide-microsoft-teams
- url: https://support.telnyx.com/en/articles/9039036-emergency-services-and-ipnd-in-australia
- url: https://support.telnyx.com/en/articles/9718403-microsoft-teams-emergency-call-routing
updated_at: 2026-07-17T09:09:12Z
---

# Telnyx Number Requirements and Microsoft Teams Integration

*Part 6 of 6 — see also: [Part 1](telnyx-number-requirements-and-microsoft-teams-integration--part-1.md), [Part 2](telnyx-number-requirements-and-microsoft-teams-integration--part-2.md), [Part 3](telnyx-number-requirements-and-microsoft-teams-integration--part-3.md), [Part 4](telnyx-number-requirements-and-microsoft-teams-integration--part-4.md), [Part 5](telnyx-number-requirements-and-microsoft-teams-integration--part-5.md)*

This page consolidates Telnyx documentation covering DID number requirements for Reunion, Australia, and New Zealand, Australian emergency services and IPND, and Microsoft Teams integration guides including Direct Routing, Call2Teams, TLS/SIP warnings, Operator Connect, and emergency call routing.

## Operator Connect Guide - Microsoft Teams

Use Telnyx Operator Connect to connect Microsoft Teams Phone users to PSTN calling through Telnyx.

Operator Connect lets you enable Telnyx as an operator in the Microsoft Teams admin center, synchronize your Microsoft tenant with Telnyx, add or port phone numbers, and assign those numbers to Teams users.

Unlike Direct Routing, Operator Connect does not require you to configure or manage your own SBC, voice routes, or PSTN usage records in Microsoft Teams. Telnyx provides the operator-managed PSTN connectivity.

### Minimum Requirements

Before you begin, make sure you have:

- A Telnyx portal account.
- Access to the Telnyx Microsoft Teams or Operator Connect setup flow.
- Microsoft 365 administrator access with permission to manage Teams voice settings.
- Access to the Microsoft Teams admin center.
- Users who are licensed for Teams Phone.
- At least one Telnyx number available for Operator Connect, or a porting plan for numbers you want to move to Telnyx.
- Emergency address information for numbers that require emergency-service configuration.

Microsoft 365 E5 or Office 365 E5 is not the minimum requirement for Operator Connect. E5 is sufficient because it includes Teams Phone, but Operator Connect users only need the required Microsoft Teams and Teams Phone entitlements for their plan.

### Step 1: Log in to Telnyx and the Microsoft Teams admin portals

- Log into the Mission Control Portal
- Log into your Microsoft Teams account with a valid admin account and note the email associated with your Telnyx account. This will be needed when setting up the integration between Telnyx and Microsoft.

### Step 2: Navigate to the Microsoft Teams section

- On the left hand menu, navigate to the Microsoft Teams tab.
- Check if you have already configured Operator Connect in your environment. If not, follow the setup wizard in the Admin Dashboard by clicking "Get Started".

### Step 3: Verify your email address

- In the Microsoft Teams Admin, navigate to the Operator Connect tab under the Voice section on the left-hand menu. Verify that **Telnyx** is listed among your available operators.
- Ensure the contact email in the Operator Setting page in the Microsoft Teams Admin Portal matches the email address associated with your Telnyx portal account.
- When you have confirmed the email address in both systems, select 'Yes' in the set up Wizard in the Mission Control Portal. This will start a synchronization of your Telnyx and Microsoft Teams account.
- If your accounts don't immediately sync, wait 24 hours and check again before reaching out to support.

### Assigning A Number

Now that you have your Operator Connect set up, let us add some numbers which will be used in your Teams.

In your connections on the Teams Page, click the edit button (Pencil Icon), it will open the on the settings tab, Select the Next "Numbers" tab.

If you don't have some numbers already added, select the "**Add Numbers**" button.

Select which Agent will be using the app, (Human or Voice App), and select the country your number will be used from and hit **Next**.

If you have already purchased your numbers they will show up in the list of numbers. Otherwise select the "Buy Numbers" button which will redirect you to the Buy Numbers Page. There you can Search and purchase numbers.

Move back to the "Add numbers to this connection" under Teams and add numbers to your Operator Connect setup. Add an Emergency address from the drop-down and hit **Submit**.

Confirm Charges and on the next page your numbers will appear in the **Number History** tab list with the Status of the connection. Orange - Not yet ready, Green - Ready to use. Use the refresh button on the right to check status updates.

You can find your available numbers in the **Numbers** Tab.

Now that you have your numbers connected, go to the Phone Numbers page on the Teams Admin and assign a number to a User. Select Number, Click Edit then search for a user to assign and click **Apply.**

Now Finally, you can test your App by calling from Teams and back. Your Assigned number will show up below the dial pad.

### Tips - Emergency Address in shared calling policies in Teams

When setting emergency addresses for MSFT teams, make sure these steps are followed to ensure they are properly routed when users call emergency services are called or when users are called back.

- Ensure emergency calling policy is set and assigned to users.
- Dynamic emergency calling is set to on. This will ensure the actual address is always sent when the emergency call is placed.
- Static Emergency address in Teams settings is correctly set, as Microsoft will fall back to it if the dynamic address is not available.

### Pricing

Customers can find pricing for our Operator Connect bundles on the Bundles Pricing Page in the portal.

## Microsoft Teams Emergency Call Routing

In today's fast-paced digital world, ensuring that emergency calls are routed accurately and efficiently is more critical than ever. Whether you're managing a large enterprise or a small business, having a reliable system that directs emergency calls to the correct Public Safety Answering Point (PSAP) can make all the difference in critical situations.

Microsoft Teams integrates advanced technologies to support emergency services, ensuring that when a call is made to emergency numbers, it is quickly and correctly routed. One key component in this process is the use of [Dynamic Location Routing](https://learn.microsoft.com/en-us/microsoftteams/configure-dynamic-emergency-calling). This feature ensures that emergency calls made through Microsoft Teams are directed to the right location, taking into account the caller's current position.

### Microsoft Teams Operator Connect and Direct Routing Dynamic Location Routing: Technical Overview

**PIDF-LO** (Presence Information Data Format Location Object) is a standardized protocol crucial for enhancing the effectiveness of emergency calls by embedding precise location data. This information is essential for VoIP providers, enabling them to route calls accurately to the appropriate Emergency Public Safety Answering Point (PSAP).

Given the critical importance of emergency services, PIDF-LO supports multiple implementations. Currently, Telnyx leverages Microsoft's **Dynamic Location Routing** to ensure rapid and accurate routing of emergency calls.

In this implementation, Microsoft Teams includes emergency address details within the SIP INVITE MIME part. Telnyx then processes this information to route the call accurately to the appropriate emergency PSAP.

The current methods for PIDF-LO supported are LIS or ASSIST. This XML data is processed by Telnyx to determine the correct PSAP for routing the emergency call.

By leveraging this sophisticated technology, Microsoft Teams and Telnyx ensure that every emergency call is handled with the utmost accuracy, providing peace of mind for users who rely on these services in critical moments.
