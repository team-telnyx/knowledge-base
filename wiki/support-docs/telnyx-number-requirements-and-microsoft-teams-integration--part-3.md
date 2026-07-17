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

*Part 3 of 6 — see also: [Part 1](telnyx-number-requirements-and-microsoft-teams-integration--part-1.md), [Part 2](telnyx-number-requirements-and-microsoft-teams-integration--part-2.md), [Part 4](telnyx-number-requirements-and-microsoft-teams-integration--part-4.md), [Part 5](telnyx-number-requirements-and-microsoft-teams-integration--part-5.md), [Part 6](telnyx-number-requirements-and-microsoft-teams-integration--part-6.md)*

This page consolidates Telnyx documentation covering DID number requirements for Reunion, Australia, and New Zealand, Australian emergency services and IPND, and Microsoft Teams integration guides including Direct Routing, Call2Teams, TLS/SIP warnings, Operator Connect, and emergency call routing.

## Configuring Telnyx with Microsoft Teams Direct Routing

[Direct Routing](https://learn.microsoft.com/en-us/microsoftteams/direct-routing-plan) with [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software) allows businesses to connect external phone lines to Microsoft Teams and use Teams as an office phone system instead of a legacy PBX system. This means you can maintain your existing SIP trunks and PSTN connectivity -- retaining control over your numbers and realizing cost savings over the MS Teams Calling Plans.

This article will guide you on how to use Telnyx as a PSTN provider for Microsoft Teams Direct Routing. Once set up is complete, Telnyx customers will be able to use numbers purchased from Telnyx to send and receive calls via the PSTN from the same Teams account.

> **Note:** This integration is carried out via the Telnyx MS Teams SBC, which interconnects Microsoft Teams with the Telnyx telephony platform. Telnyx SBC uses the base domain mstsbc.telnyx.tech, and Telnyx customers will be able to interconnect using a subdomain of mstsbc.telnyx.tech and a token for authentication.

### Pre-requisites

- You'll need a Telnyx account with a purchased number.
- Assign a **Microsoft Teams E5** license to each user who will be making and receiving calls to the PSTN
- Make sure you can sign in to the Microsoft 365 admin center as a Global Administrator.
- Procure a Microsoft license. You'll need one of these base plans and an add-on if necessary:

| BASE PLAN | ADD ON REQUIRED FOR DIRECT ROUTING |
| --- | --- |
| Microsoft Business Basic / Standard / Premium | Microsoft 365 Business Voice without Calling Plan |
| Microsoft Office 365 Enterprise E1 / E3 / F3 / A1 / A3 | Phone System |
| Microsoft Office 365 Enterprise E5 | No add on required |

### 1. Add a SIP connection in Telnyx

Once you have set up your Telnyx account, you will have to set up a new connection for the Telnyx SBC on the SIP Connections page.

1. Click on the **Create SIP Connection** button and choose a name for your connection. You should see options that will allow you to choose a SIP Connection Type on the next page. For this connection, we must choose **MS Teams Direct Routing SBC.**
2. You will want to take note of the auto-generated subdomain that appears as it will be needed at different stages of the setup.
3. Click **Next** and follow the guide to set up your **Authentication and Routing** details on the following page, followed by your **Configuration** details.
4. Scroll down and Click **Next**.

### 2. Set up Inbound and Outbound details

Now, you will set up **Inbound** and **Outbound** details for the SIP Connection. You will also be able to assign it an Outbound Voice Profile.

For the Inbound settings, there are a variety of options you may configure to your preference and for the Outbound settings, it is critical to keep in mind the details of the Outbound profile being assigned. You can see these from the Voice > Settings > Outbound profiles page.

Click **Next.**

### 3. Assign a number to the Telnyx SBC Connection

You are now required to assign a Number to the MS Teams connection you just created.

1. If you have not done so already as part of your pre-requisite activities, you'll need to purchase a number from Telnyx.
2. Once you have a number, navigate to the Numbers section and assign the number to your connection.

Alternatively, navigate to the Numbers page in the Telnyx Mission Control Portal and assign your MS Teams connection to the desired DID.

Click **Complete.**

### 4. Add a subdomain to the customer tenant in Microsoft

Now that your Mission Control Portal is set up and ready to go, you'll need to add a subdomain in the Microsoft admin portal before setting up Direct Routing in Microsoft Teams.

1. Perform a search for *Domains* within the Microsoft 365 admin center search bar at the top of your screen.
2. Click the **Add Domain** option at the top left and add the auto generated subdomain that corresponds to the SIP Connection we created in Section 1.
3. Click **Use This Domain** and verify the domain on the following page. Select the **Add a TXT record instead** option.
4. Click **Next** and take note of the TXT value displayed.
5. Navigate back to your MS Teams SBC SIP Connection settings in your Telnyx Mission Control Portal.
6. Navigate to the **Domain Validation** header in the top right corner of the window and paste the TXT Value from MS Teams into the **TXT Value** text box.

> **Note:** The TXT Name and TLL fields should match the fields shown in the MS 365 admin center, hence why they cannot be edited. Any user who tries to set the `txt_name` on a MS DR connection to `*.mstsbc.telnyx.tech` will get an error that says `txt_name should not include the '.mstsbc.telnyx.tech' suffix. Use only the identifier portion (e.g. '1234abc' instead of '1234abc.mstsbc.telnyx.tech')`.

7. Click **Save All Changes**.
8. Once you have saved your changes, navigate back to Microsoft 365 admin center and click on the **Verify** button at the bottom.
9. On the next page, select **More Options**.
10. Select **Skip and do this later** and click **Next**.
11. After this you will be prompted that setup has been complete.

### 5. Activate the subdomain

After you have registered a domain name, you'll need to activate it by adding at least one user and assigning the domain that matches the subdomain that was automatically generated when the SIP Connection was created in Section 1.

1. From Microsoft 365 Admin Center, navigate to **Users → Active Users → Add a user**.
2. Next, fill in the User details:
   - **Domain:** Select the Telnyx subdomain (i.e. *yyyy.mstsbc.telnyx.tech*)
   - Assign E5 license under "Product Licenses".
3. Click **Add.**

> **Note:** You can remove the E5 license from this user once you're able to add this domain to Direct Routing.

### 6. Add the Telnyx SBC in Direct Routing

Next, we'll need to set up the Telnyx SBC subdomain in the Microsoft Teams admin center. To do this, you'll have to have a Microsoft Teams E5 license assigned to each user who will be making and receiving calls to the PSTN. Keep in mind that the changes on the MS Teams admin portal may take up to 24 hours to take effect.

1. In the left tab of the Microsoft Teams admin center, navigate to **Voice → Direct Routing**.
2. Click the **SBCs** tab.
3. Click **Add** and enter the subdomain that was automatically generated in your SIP Connection from Section 4.
4. Provide the following information:
   - **Enabled:** Toggle on
   - **SIP Signaling port:** *5061*
   - **Send SIP options:** Toggle on
   - **Forward P-Asserted-Identity (PAI) header:** Toggle on if you would like anonymous calls to connect.
5. Click **Save**.

### 7. Create voice routes

Now you'll need to create a pass-through voice route.

1. In the left-hand navigation of your 365 admin portal, navigate to **Voice → Direct Routing**.
2. When on the Directing Routing page, select the **Voice routes** tab.
3. Click **Add,** and enter a name and description for your voice route.
4. Set the priority and specify the dialed number pattern as per Telnyx's number plan.

**For US numbers:**

- prepend: *1*; match pattern: *NXXNXXXXXX*
- prepend: blank; match pattern: *1NXXNXXXXXX*

**For International numbers:**

- prepend: Country Dialing prefix; match pattern: *NXXNXXXXXX*
- prepend: blank; match pattern: (Country Dialing prefix)*NXXNXXXXXX*

### 8. Enroll the SBC

In this section, we will enroll the SBC with the voice route.

1. From the **Direct Routing** page, navigate to **SBCs enrolled**.
2. Click **Add SBCs**.
3. Select the SBCs you want to enroll.
4. Click **Apply**.

### 9. Add the PSTN usage records

In this section, you will add Public Switched Telephone Network (PSTN) usage records, which specify a class of call (such as internal, local, or long distance) that can be made by a user or group of users in an organization.

1. From your Microsoft 365 admin portal, use the left-hand navigation to navigate to **Voice → Direct Routing** and find the **PSTN usage records** section.
2. Click **Add PSTN usage**.
3. Select the PSTN records you want to add.

> **Note:** This example includes "^(.*)$", which allows you to dial any destination. We recommend using a different pattern if you want to include restrictions.

4. Click **Apply**.
5. From the left-hand navigation, under **Voice**, click **Voice Routing Policies.**
6. In the **PSTN usage records** section, click **Add PSTN** usage.
7. Select *Telnyx*.
8. Click **Save**.

### 10. Configure voice routing policies

1. From the left-hand navigation of the 365 admin portal, under **Voice**, click **Voice Routing Policies.**
2. Click **Add**.
3. Type **TELNYX** as the name and add a description.

### 11. Assign Dialplan and Voice routing policies

1. From the left-hand navigation of the 365 admin portal, click **Users**.
2. Click the **Policies** tab.
3. Select **Edit** and assign the following:
   - **Dial Plan:** *Telnyx*
   - **Voice Routing Policy:** *Telnyx*
4. Click **Apply**.

### 12. Assign Telnyx DID to on-premises PSTN connectivity

Finally, provision a user with an on-premises phone number. Go to [admin.teams.microsoft.com](http://admin.teams.microsoft.com/) > **Manage Users**. Click on the intended user.

Under Account:

- Enable the toggle `Enterprise Voice`
- Click on `Assign a primary phone number`

A new prompt will open to the side. Add the phone number and click on Apply.

### 13. Make some test calls with Microsoft Teams

Your setup for Microsoft Teams Direct Routing should now be complete. The last step is to make both inbound & outbound test calls from Microsoft Teams to verify the service has been set up correctly.

1. Call a PSTN number from the Microsoft Teams client. You'll want to confirm that the call connects through Telnyx and that there is two-way audio.
2. Call a Telnyx DID that is assigned to both your new Microsoft Teams SIP Connection and one of your Microsoft Teams users from the PSTN (i.e. a cell phone). Confirm that the call is received in Microsoft Teams and that two-way audio is functioning correctly.
3. Check the CDRs from the **Reporting** section of your Telnyx Mission Control Portal to validate that both calls went through correctly.

If you encounter any issues during these tests, please contact us at [support@telnyx.com](mailto:support@telnyx.com) with a note of the number dialled and the date/time.
