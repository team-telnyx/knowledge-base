---
title: AI Assistant Configuration
summary: Telnyx AI assistants can be extended with enterprise integrations, tuned
  interruption behavior, persistent memory across conversations, and multi-participant
  call capabilities. This page covers the available integration catalog and connection
  workflow, interruption settings for turn-taking and non turn-taking transcription
  models, memory configuration via the dynamic variables webhook, and the Invite and
  Skip Turn tools used to coordinate multi-participant voice calls.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/integrations
- url: https://developers.telnyx.com/docs/inference/ai-assistants/interruption-settings
- url: https://developers.telnyx.com/docs/inference/ai-assistants/memory
- url: https://developers.telnyx.com/docs/inference/ai-assistants/multi-participant-calls
updated_at: 2026-08-05T13:44:48Z
---

# AI Assistant Configuration

*Part 2 of 6 — see also: [Part 1](ai-assistant-configuration--part-1.md), [Part 3](ai-assistant-configuration--part-3.md), [Part 4](ai-assistant-configuration--part-4.md), [Part 5](ai-assistant-configuration--part-5.md), [Part 6](ai-assistant-configuration--part-6.md)*

Telnyx AI assistants can be extended with enterprise integrations, tuned interruption behavior, persistent memory across conversations, and multi-participant call capabilities. This page covers the available integration catalog and connection workflow, interruption settings for turn-taking and non turn-taking transcription models, memory configuration via the dynamic variables webhook, and the Invite and Skip Turn tools used to coordinate multi-participant voice calls.

## Integrations

Telnyx AI assistants can integrate with leading enterprise platforms to access customer data, create tickets, update records, and automate workflows directly during conversations. The Integrations tab in the assistant builder offers a growing catalog of enterprise connectors, organized by category. Use the category filter chips at the top of the **Add Integration** section to narrow the list.

### Available integrations

**Sales & CRM**

- **Salesforce** — Manage leads, contacts, accounts, opportunities, tasks, and cases.
- **HubSpot** — Manage contacts, companies, deals, tickets, and custom objects.
- **Pipedrive** — Manage deals, contacts, organizations, activities, and pipelines.
- **Zoho CRM** — Manage leads, contacts, accounts, deals, tasks, and notes.
- **Gong** — Revenue intelligence: call analysis, deal insights, and user management.

**Customer Support**

- **Zendesk** — Manage tickets, users, organizations, and support operations.
- **Intercom** — Manage contacts, companies, conversations, and help center articles.
- **ServiceNow** — Enterprise ITSM: incidents, change requests, problems, and service catalog.
- **Jira** — Issue tracking, comments, transitions, and project management.
- **Jira Service Management** — Service desks, customer management, and request lifecycle.

**Engineering & Product**

- **GitHub** — Repository, issue, and pull request management.
- **Jira** — Issue tracking, comments, transitions, and project management.
- **Linear** — Project management: issues, projects, and team workflows.

**IT Operations**

- **ServiceNow** — Enterprise ITSM: incidents, change requests, problems, and service catalog.
- **Jira Service Management** — Service desks, customer management, and request lifecycle.
- **Microsoft Teams** — Manage teams, channels, messages, members, and file operations.

**Work Management**

- **Asana** — Manage tasks, projects, teams, workspaces, and custom fields.
- **Airtable** — Manage bases, tables, records, fields, comments, and attachments.
- **Notion** — Manage databases, pages, blocks, users, and content.

**Knowledge & Documentation**

- **Confluence** — Manage pages, spaces, content, and attachments.
- **Notion** — Manage databases, pages, blocks, users, and content.
- **SharePoint** — Manage sites, document libraries, lists, and content.
- **GitHub** — Repository, issue, and pull request management.

**Communication & Collaboration**

- **Microsoft Teams** — Manage teams, channels, messages, members, and file operations.
- **Outlook** — Manage email, calendar events, contacts, and mailbox organization.

**File Storage & Productivity**

- **OneDrive** — Manage files, folders, sharing, and metadata.
- **Outlook** — Manage email, calendar events, contacts, and mailbox organization.
- **SharePoint** — Manage sites, document libraries, lists, and content.

**HR & Recruiting**

- **Greenhouse** — ATS: candidates, jobs, applications, scorecards, and recruiting workflows.
- **SAP SuccessFactors** — Manage employees, time off, performance goals, positions, and recruiting.

**Scheduling**

- **Calendly** — Manage scheduling, events, invitees, event types, and organization operations.

**Design & UX**

- **Figma** — Manage files, projects, teams, comments, components, styles, and dev resources.

**Accounting & Finance**

- **QuickBooks Online** — Accounting: customers, invoices, payments, bills, and financial reporting.

**E-commerce & Payments**

- **Shopify** — Manage products, orders, customers, inventory, and store operations.
- **Stripe** — Payment processing: customers, charges, refunds, subscriptions, and invoices.

**Testing & Evaluation**

- **Coval** — Simulation and evaluation for voice and chat agents — automated testing, regression detection, and production monitoring.

The integration catalog is expanding regularly. The **Add Integration** section in the assistant builder always reflects the current, complete list — if you see a platform there that isn't documented, it works the same way: connect it, enter the required credentials, and enable the tools you need.

### Connection workflow

Before connecting an integration, make sure you have:

1. **Platform account** — Active access with the right permissions on the target platform.
2. **API credentials** — Platform-specific keys or tokens required by the integration.
3. **Telnyx AI assistant** — A configured assistant ready to connect the integration.

To connect an integration:

1. Open your assistant in [AI Assistants](https://portal.telnyx.com/#/ai/assistants) or create a new one.
2. Go to the **Integrations** tab.
3. In the **Add Integration** section, optionally filter by category, pick a provider, and enter the required credentials.
4. Enable the tools you need, adjust defaults, and save the assistant.

![Mission Control Portal showing the Add Integration section with category filter chips and a grid of available integration platforms](https://mintcdn.com/telnyx/33ANQJ-HKUTIlR5u/img/ai-integration-dropdown-full.jpeg?fit=max&auto=format&n=33ANQJ-HKUTIlR5u&q=85&s=7176434b10aaf4661cc5bc0d1a8118ed)

### Platform-specific setup

**GitHub** — Connect for code hosting, version control, and development workflows. Provide a Personal Access Token generated at <https://github.com/settings/tokens> with scopes such as `repo`, `read:user`, and `read:org`. After connecting, the assistant can create issues, search repositories, manage pull requests, access code, and manage labels.

![GitHub integration credentials dialog showing Personal Access Token input field](https://mintcdn.com/telnyx/4tBNWGoUCO9azKQ0/img/github-integration-credentials.png?fit=max&auto=format&n=4tBNWGoUCO9azKQ0&q=85&s=b0f75f53aeede000a3c9ddfa42330adb)

**Greenhouse** — Connect for applicant tracking and recruiting workflows. Provide a Harvest API key from **Dev Center → API Credential Management**. After connecting, the assistant can look up candidates, coordinate interview scheduling, manage applications, view job postings, and review scorecards.

![Greenhouse integration credentials dialog showing API Key input field](https://mintcdn.com/telnyx/4tBNWGoUCO9azKQ0/img/greenhouse-integration-credentials.png?fit=max&auto=format&n=4tBNWGoUCO9azKQ0&q=85&s=e576b348e0ab3c47bc1c88b366ae4b0d)

**HubSpot** — Connect for marketing, sales, and customer service workflows. Provide a private app access token from **Settings → Integrations → Private Apps**. After connecting, the assistant can manage contacts, track deals, manage tickets, update company records, and log engagements.

![HubSpot integration credentials dialog showing Private app token input field](https://mintcdn.com/telnyx/tKcWw-YZ6CuwkRsC/img/hubspot-integration-credentials.png?fit=max&auto=format&n=tKcWw-YZ6CuwkRsC&q=85&s=8024927ea21619f4ad4cef37136dfb2c)

**Intercom** — Connect for customer messaging and support workflows. Provide an access token from a private app created in **Settings → Developers → Developer Hub → Your Apps → New App**. After connecting, the assistant can access conversation history, create notes, update customer attributes, search users, and manage tags.

![Intercom integration credentials dialog showing Access Token input field](https://mintcdn.com/telnyx/JbAKfH7SbyeZcDpH/img/intercom-integration-credentials.png?fit=max&auto=format&n=JbAKfH7SbyeZcDpH&q=85&s=95c38b50b1f90b7f467354dcf736ffe9)

**Jira** — Connect for project management, issue tracking, and software development workflows. Provide the account email, an API token from <https://id.atlassian.com/manage-profile/security/api-tokens>, and the site URL (for example `yourcompany.atlassian.net`) without the `https://` prefix. After connecting, the assistant can create issues, update issues, search issues, add comments, and transition issues.

![Jira integration credentials dialog showing Email, API token, and Site URL input fields](https://mintcdn.com/telnyx/JbAKfH7SbyeZcDpH/img/jira-integration-credentials.png?fit=max&auto=format&n=JbAKfH7SbyeZcDpH&q=85&s=bf3fa74adbf94d690daa7e18df5900fe)

**Salesforce** — Connect to access customer records, create cases, and update opportunities. Provide the instance domain (for example `acme.my.salesforce.com`), username, password, security token (from Personal Settings → Reset My Security Token), and Organization ID (from Setup → Company Settings → Company Information). After connecting, the assistant can search records, create records, update records, and run SOQL queries.

![Salesforce integration credentials dialog showing Instance domain, Username, Password, Security token, and Organization ID input fields](https://mintcdn.com/telnyx/piPv--L_2q5NFR4U/img/salesforce-integration-credentials.png?fit=max&auto=format&n=piPv--L_2q5NFR4U&q=85&s=0ff6a06b4c09afe50c3c3020eaced2d7)

**ServiceNow** — Connect for IT service management, incident tracking, and workflow automation. Provide the instance URL (for example `acme.service-now.com`), username, and password. After connecting, the assistant can create incidents, update tickets, search the knowledge base, and query records.

![ServiceNow integration credentials dialog showing Instance URL, Username, and Password input fields](https://mintcdn.com/telnyx/piPv--L_2q5NFR4U/img/servicenow-integration-credentials.png?fit=max&auto=format&n=piPv--L_2q5NFR4U&q=85&s=516ed46fe8754e406f373f2e4a51e5fa)

**Zendesk** — Connect for customer service and support workflows. Provide the subdomain (for example `company` if your portal is `company.zendesk.com`), the email of the account that owns the API token, and an API token generated in **Admin Center → Apps and integrations → APIs → Zendesk API**. After connecting, the assistant can create tickets, search customer history, update ticket status, and access the knowledge base.

![Zendesk integration credentials dialog showing Subdomain, Email, and API token input fields](https://mintcdn.com/telnyx/Bg7y6_RQhPe1fn_1/img/zendesk-integration-credentials.png?fit=max&auto=format&n=Bg7y6_RQhPe1fn_1&q=85&s=0a45d7798601cf7464a07eecd243bb48)

**Coval** — Connect to [Coval](https://www.coval.dev/) for automated simulation, evaluation, and production monitoring of voice and chat agents. Coval is a testing and evaluation tool — unlike the other integrations, it does not add tools your assistant uses during conversations. Instead, it tests and monitors the assistant itself. Provide a Coval API key from your workspace settings. After connecting, you can run automated scenario simulation, CI/CD regression testing, production monitoring, and built-in evaluation metrics (latency, accuracy, tool-call effectiveness, instruction compliance).

### Managing integrations

To view connected integrations, open the assistant in the Mission Control Portal, select the **Integrations** tab, and review the **Connected Integrations** section.

![Integrations section displaying Jira under Connected Integrations with description and unassign button](https://mintcdn.com/telnyx/d2AUJO5qdne_WnZI/img/connected-integration-view.png?fit=max&auto=format&n=d2AUJO5qdne_WnZI&q=85&s=da05d2e45c00e8b67aaf3f9e0cf27ed7)

To disconnect an integration from an assistant, open the **Integrations** tab, locate the integration under **Connected Integrations**, click the chain-link **unassign** button, and confirm. After disconnecting, the integration is removed from this assistant, all associated tools are disabled, and the integration moves to **Available Integrations** where it can be reconnected later. Disconnecting only removes the integration from the current assistant — it remains in your account and can be connected to other assistants.

![Jira integration card in Connected Integrations showing unassign button (chain link icon)](https://mintcdn.com/telnyx/JbAKfH7SbyeZcDpH/img/jira-connected-integration-unassign.png?fit=max&auto=format&n=JbAKfH7SbyeZcDpH&q=85&s=e88ef24a3c6a8831b57ceeb1c582ebb7)

To permanently delete an integration from your account, open the **Integrations** tab, find the integration under **Available Integrations**, click the trash icon, and confirm. Deleting permanently removes the integration and all stored credentials — you will need to set it up again from scratch to use it in the future.

![Jira integration card in Available Integrations showing connect button and delete button (trash icon)](https://mintcdn.com/telnyx/JbAKfH7SbyeZcDpH/img/jira-available-integrations-actions.png?fit=max&auto=format&n=JbAKfH7SbyeZcDpH&q=85&s=f75887f9279b1ca6c811cbca269024dd)

### Best practices

**Security**

- Use dedicated service accounts with only the permissions the workflow needs.
- Rotate credentials regularly.
- Monitor usage through platform audit logs.
- Limit permissions to the scopes required for each use case.
- Use sandbox environments to test and validate integrations first.

**Configuration**

- Start with read-only tools, then gradually introduce write actions.
- Provide clear descriptions of when and how each tool should be used.
- Test thoroughly across multiple conversation scenarios.
- Use tool parameters to configure sensible defaults and reduce user input errors.
- Handle errors gracefully with defined fallback behavior.

**Performance**

- Minimize API calls and avoid duplicate searches.
- Cache frequently accessed data (for example, via dynamic variables) for the duration of a session.
- Set appropriate timeouts that balance responsiveness with reliability.
- Monitor rate limits and design workflows to stay within allocation.

### Troubleshooting

- **Connection failures** — Verify credentials are correct and not expired, check that the user account has API access, ensure security tokens or API keys are current, include the security token for Salesforce, and verify instance URL format (no `https://` or trailing `/`) for cloud platforms.
- **Tools not appearing** — Refresh the page, verify the integration account has required permissions, check that the platform subscription includes API access, and try disconnecting and reconnecting.
- **Authentication errors during calls** — Regenerate API tokens or security tokens, update stored credentials, verify the account has not been locked or suspended, and check IP allowlists if applicable.
- **Missing data or records** — Verify the integration account can access the records, check record permissions and sharing settings, confirm records exist in the platform, and verify search parameters and filters.
- **Rate limiting** — Reduce call frequency, implement caching, contact platform support to increase limits, and distribute calls across multiple service accounts.
