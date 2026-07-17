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

*Part 4 of 6 — see also: [Part 1](telnyx-number-requirements-and-microsoft-teams-integration--part-1.md), [Part 2](telnyx-number-requirements-and-microsoft-teams-integration--part-2.md), [Part 3](telnyx-number-requirements-and-microsoft-teams-integration--part-3.md), [Part 5](telnyx-number-requirements-and-microsoft-teams-integration--part-5.md), [Part 6](telnyx-number-requirements-and-microsoft-teams-integration--part-6.md)*

This page consolidates Telnyx documentation covering DID number requirements for Reunion, Australia, and New Zealand, Australian emergency services and IPND, and Microsoft Teams integration guides including Direct Routing, Call2Teams, TLS/SIP warnings, Operator Connect, and emergency call routing.

## MS Teams: Call2Teams & Telnyx

[Microsoft Call2Teams](https://www.call2teams.com/) is an add-on for Office 365 that connects Microsoft Teams to any PBX or SIP Trunk, allowing you to make and receive calls on any device using the Microsoft Teams App.

### Pre-requisites

- Your Telnyx Portal must be correctly set up and configured for use
- Have your SIP Credentials (The username/password for your main SIP account or SIP sub-account)
- Have DIDs available to assign
- A PC running a Windows OS
- Create a temporary spare user license on Microsoft 365
- Global admin access to your Microsoft 365 tenant
- Create a Call2Teams subscription

### 1. Set up the Office 365 tenant

1. Once you've created your subscription to Call2Teams, you'll receive an email inviting you to the portal. When you click Accept Invitation, you'll need to use your Office 365 account to log in. Make sure this account is associated with the organization you're configuring Call2Teams for and that you have global-level access.
2. Give Call2Teams permission to connect to your 365 account. You MUST check the **Connect on behalf of your organization** checkbox.
3. Click **Accept**.

### 2. Connect to Telnyx and Create a SIP trunk

1. From the Call2Teams admin portal, click on the "Service" tab in the top navigation.
2. From here, find the "Trunk" tab. Click on this, then click "Add New Trunk".
3. Here you will see a drop-down menu where you can select from a list of verified providers with pre-configured profiles that will set your trunk up for you. As of the time of writing, Telnyx is not yet on this list, so you'll need to select **Custom** from this list. You'll get a message telling you that any Telnyx-specific support can't be handled by Microsoft at this time. Click the **Proceed with Unsupported Configuration** button.
4. You'll now be able to enter your Telnyx account information. Provide the following:
   - **Service Name**: *Telnyx Trunk 1*
   - **Country**: Your Country
   - **State/Province**: Your State/Province
   - **Range Start/Range End**: You'll use your Telnyx DIDs. Ensure that you add + plus your country code before entering your DID. If you have more than one DID that you would like to add and they are not sequential, add each of these DIDs on both the **START Range** and the **Range END** fields. You will need to add each DID separately by adding a new range by clicking on **+ Add Additional Range.**
   - **SIP Domain**: *sip.telnyx.com*
   - **Authenticate Type**: *Registration*
   - **Username**: Your Telnyx account/sub-account username
   - **Auth Username**: Your Telnyx account/sub-account username
   - **Password**: Your Telnyx account/sub-account password
   - **Expiry (seconds)**: If you want, click on the padlock, and enter *300*. You can also leave this blank.
   - **Protocol**: *UDP* or *TCP*.
   - **Encrypt Media**: *No*
   - **Propagate Refer:** *Yes*

> **Note:** Select *Yes* to propagate received SIP REFER messages from Microsoft upstream to this service. If set to *No* then transfers are bridged out as new calls. On the 2nd Gen OneClick Teams connector you should select *Yes* if you have users in a Call Center, but otherwise select *No* as this will allow consultative transfers to work better.

   - **Outside Line Prefix**: Leave this option blank
   - **E164 Number Format**: *Localized*
   - **From Header**: *SIP Identifier*
   - **P-Asserted-Identity Header**: This will be the outbound caller ID Name. You can choose *Passthrough Caller Id* (the caller ID given by the far end, e.g. Teams user extension name) or *Trunk User Number* (to display the phone number assigned to the user in the portal).
   - **E164 Number Translation** (The incoming number needs to be converted to E164 format):
     - **Outbound International Prefix**: *011*
     - **Outbound National Prefix**: Leave blank
     - **Inbound International Prefix**: Indicate
     - **Inbound National Prefix**: Leave blank

5. Click the "Add Trunk" button.
6. You'll now see your new trunk in your list. Click on the Trunk tab to see your list at any time. You can also monitor the health of your Trunk and ensure it's still up and running from this list.

### 3. Associate a number with a team member

1. Click on the **Users** tab in the top navigation.
2. From this tab, click **Add New User** and provide the following information:
   - **Select a User:** Select the user intended for the number.
   - **PBX/Trunk:** Select a trunk you've created
   - **Select a Trunk Number:** Select the DID intended for this user.
3. Click the **Add** button, followed by the **Sync Now** button in the upper right.
