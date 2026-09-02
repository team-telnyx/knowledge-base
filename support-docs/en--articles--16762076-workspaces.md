---
source_url: https://support.telnyx.com/en/articles/16762076-workspaces
title: "Workspaces"
description: "Access multiple Telnyx organizations from a single login — switch between organizations, accept invitations, and migrate legacy sub-users."
scraped: 2026-08-31
content_hash: 2519d9edb7bca0436985a4f6ee35bb00411d7b778a7c7ef137d74a6deecaa6fd
---

# Workspaces

Access multiple Telnyx organizations from a single login — switch between organizations, accept invitations, and migrate legacy sub-users.

## Overview

Workspaces let you belong to and switch between multiple Telnyx organizations using a single login. Each workspace represents a membership in a different organization, with its own billing, resources, API keys, and configuration.

Workspaces is a supplementary upgrade to the legacy sub-user model. Instead of a sub-user being limited to a single organization with no path to become a primary account owner, with Workspaces you sign in once with your real email address and use the workspace switcher in the Mission Control Portal to operate in different organizational contexts.

## How it works

| Concept | Description |
| --- | --- |
| **Primary account** | Your real identity. Owns billing, resources, and API keys. Can have multiple workspace memberships. |
| **Tenant user** | A sub-user record created inside the target organization. Has its own permissions, audit trail, and API keys within that org. |
| **Workspace** | A link between your primary account and a tenant user in another organization. |

When you switch into a workspace, you receive a session token scoped to that organization's tenant user. You can then use all of that organization's resources as if you were a member of it. Switching back to your primary account returns you to your own organization's context.

## Using the workspace switcher

**1. Open the workspace switcher**

In the [Mission Control Portal](https://portal.telnyx.com), click the organization selector in the top navigation bar. A dropdown shows your current organization and all available workspaces.

**2. Switch into a workspace**

Click a workspace name in the dropdown to switch into it. The portal reloads in the context of that organization. A banner indicates which workspace you're currently in.

**3. Return to your primary account**

Click the workspace switcher again and select your primary account (listed as "Individual" or your organization name) to return to your own organization context.

> **Note:** The switch token is valid for 6 hours. If it expires, you will be returned to your primary account and can switch again.

## Workspace invitations

Organization owners can invite users to join their organization as a workspace member. Invitations are sent by email and also appear as in-app notifications in the Mission Control Portal.

### Accepting an invitation

When you receive a workspace invitation email:

1. Click the **Take action** button in the email.
2. You'll be taken to the Mission Control Portal.
3. Review the organization name and click **Accept** to join the organization.

Once accepted, a tenant user is created inside the inviting organization, and the workspace appears in your workspace switcher.

### Rejecting an invitation

To decline an invitation, click the **Take action** button in the email and select **Reject**. No workspace will be created.

> **Note:** You can only accept invitations addressed to the email associated with your Telnyx account. If you have multiple accounts, make sure you're signed in with the correct one.

## Migrating a legacy sub-user

If you're currently a sub-user in an organization (not a primary account owner), you can migrate your account to the Workspaces model. Migration creates a primary account with your real email and converts your existing sub-user record into a workspace tenant.

**1. Check eligibility**

You're eligible if you're a confirmed sub-user, not blocked or suspended, not an account manager or managed account, and don't already have a workspace membership.

**2. Start migration**

When eligible, the Mission Control Portal shows a migration prompt. Click **Create my workspace login** to begin.

**3. Confirm migration**

Review the confirmation screen. Your current organization access stays the same and becomes your first workspace. Nothing about billing, resources, or permissions changes.

After migration:

- You sign in with your existing email address as a primary account.
- Your original organization appears as a workspace in the switcher.
- You can be invited to additional organizations in the future.

## Security

### Tenant user sign-in

Workspace tenant users cannot sign in directly. Access to a workspace is only possible through the workspace owner's primary account via the workspace switcher. This ensures the workspace owner always controls access to their tenant contexts.

### Two-factor authentication

When you belong to one or more workspaces, sign-in enforces mandatory 2FA setup if **any** of your workspaces' organization owners have two-factor authentication required.

## Legacy sub-user model

Before Workspaces, a sub-user belonged to exactly one organization and had no path to become a primary account owner. Existing sub-users continue to work as-is until they opt into migration. There is no forced disruption.
