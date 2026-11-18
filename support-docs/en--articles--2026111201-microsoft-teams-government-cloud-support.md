---
source_url: "https://support.telnyx.com/en/articles/2026111201-microsoft-teams-government-cloud-support"
title: "Telnyx Support for Microsoft Teams Government Clouds"
description: "Check Telnyx Operator Connect and Direct Routing availability for Microsoft Teams government cloud tenants."
collection_path: "3421382-microsoft-teams"
updated_at: "2026-11-12"
modified_at: "2026-11-12"
---

# Telnyx Support for Microsoft Teams Government Clouds

**Telnyx does not support Microsoft Teams calling through Operator Connect or Direct Routing for GCC High or Department of Defense (DoD) tenants.**

Telnyx Operator Connect is also unavailable for Government Community Cloud (GCC) tenants.

If your organization has both commercial and government tenants, check which tenant hosts the Teams Phone users you plan to enable. Use the setup guides below for eligible commercial tenants.

## Calling options for commercial tenants

Both options connect Teams Phone to the public telephone network through Telnyx. Choose based on how you want to manage phone numbers and calling routes.

### Operator Connect for simpler administration

Telnyx manages the calling infrastructure. Enable Telnyx as an operator and assign phone numbers to users in the Teams admin center. You can add new Telnyx numbers or port eligible existing numbers. Your team can provision calling without setting up a session border controller (SBC) or configuring voice routes in Teams. [Set up Telnyx Operator Connect](https://support.telnyx.com/en/articles/7260976-operator-connect-guide-microsoft-teams)

### Direct Routing for control over call routing

Connect Teams Phone to Telnyx SIP trunking through the Telnyx Teams SBC. Your Teams administrator configures dial plans, voice routes, and calling policies. This gives your team control over which routes users can use and which destinations they can dial. [Set up Telnyx Direct Routing](https://support.telnyx.com/en/articles/5253876-configuring-telnyx-with-microsoft-teams-direct-routing)

## Before you deploy

1. Confirm that users have Teams Phone licensing and that an administrator can manage Teams voice settings.
2. Check number availability and porting eligibility for the countries where your users need calling. Decide which numbers to keep and which to purchase.
3. Plan emergency calling for each location where users will make calls. For address and location handling, see the [Telnyx Teams emergency call routing guide](https://support.telnyx.com/en/articles/9718403-microsoft-teams-emergency-call-routing).
