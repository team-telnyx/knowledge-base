---
title: AI assistant integrations
summary: Connect your Telnyx AI assistants with enterprise platforms and developer tools — automate workflows with Salesforce, ServiceNow, and HubSpot, or test and evaluate assistants with Coval.
sources:
  - url: https://developers.telnyx.com/docs/inference/ai-assistants/integrations/index
    content_hash: 06ad74580bef71d1afe035c790205e0e9e2554b420e9ad5c046d2ac658b6aa00
updated_at: 2026-04-10T00:00:00Z
---

# AI assistant integrations

Connect your Telnyx AI assistants with enterprise platforms and developer tools — automate workflows with Salesforce, ServiceNow, and HubSpot, or test and evaluate assistants with Coval.

Telnyx AI assistants can integrate with leading enterprise platforms to access customer data, create tickets, update records, and automate workflows directly during conversations.

## Available integrations

| Integration    | Description                                         | Common Use Cases                                               |
| -------------- | --------------------------------------------------- | -------------------------------------------------------------- |
| **Salesforce** | CRM platform for sales, service, and marketing      | Lead qualification, case management, contact updates           |
| **ServiceNow** | IT service management and workflow automation       | Incident creation, ticket updates, service requests            |
| **Jira**       | Project management and issue tracking               | Bug reporting, task creation, project updates                  |
| **HubSpot**    | Marketing, sales, and service CRM                   | Contact management, deal tracking, ticket creation             |
| **Zendesk**    | Customer service and support platform               | Ticket creation, customer lookup, case management              |
| **Intercom**   | Customer messaging and support platform             | Conversation management, user data access                      |
| **GitHub**     | Code hosting and version control                    | Issue creation, repository access, pull request management     |
| **Greenhouse** | Applicant tracking and recruiting platform          | Candidate lookup, interview scheduling, application management |
| **Coval**      | Simulation and evaluation for voice and chat agents | Automated testing, regression detection, production monitoring |

## Getting started

### Prerequisites

Before connecting an integration, make sure you have:

1. **Platform account**

    Active access with the right permissions on the target platform.

2. **API credentials**

    Platform-specific keys or tokens required by the integration.

3. **Telnyx AI assistant**

    A configured assistant ready to connect the integration.

### Connection workflow

4. **Open your assistant**

    Navigate to [AI Assistants](https://portal.telnyx.com/#/ai/assistants) and open an existing assistant or create a new one.

5. **Go to Integrations**

    Select the **Integrations** tab for that assistant.

6. **Add a platform**

    Click **Add Integration**, choose a provider from the dropdown, and enter the required credentials.

7. **Configure & save**

    Enable the tools you need, adjust defaults, and save the assistant.

<img alt="Mission Control Portal showing Add Integration dropdown with available platforms including GitHub, Greenhouse, HubSpot, Intercom, Jira, Salesforce, and Zendesk" />

## See integrations in action

Watch how Telnyx Voice AI Agents connect to enterprise platforms like ServiceNow to create, update, and resolve tickets through natural voice conversation:

<iframe />

This demonstration shows the integration workflow in the Mission Control Portal and real-time ticket management capabilities that work across all supported platforms.

## Platform-specific setup

> **Note:** Select your integration platform below. If you don't see your platform, scroll horizontally to view all available options.

### GitHub

    ### GitHub

    Connect your AI assistant to GitHub for code hosting, version control, and development workflows.

    #### Prerequisites

    * GitHub account with repository access.
    * Permissions to create personal access tokens.
    * Appropriate repository scopes for integration needs.

    #### Required credentials

    When connecting GitHub, you'll need to provide:

8. **Access token**

        Generate a GitHub Personal Access Token at [https://github.com/settings/tokens](https://github.com/settings/tokens) by clicking **Generate new token → Generate new token (classic)** and selecting scopes such as `repo`, `read:user`, and `read:org`, then copy the token (it only appears once).

    <img alt="GitHub integration credentials dialog showing Personal Access Token input field" />

    #### Available tools

    After connecting GitHub, your assistant can:

    * **Create issues** - Log bugs, feature requests, or tasks in repositories.
    * **Search repositories** - Find repos by name, description, or topics.
    * **Manage pull requests** - Create, review, or update PRs.
    * **Access code** - Read file contents and repository structure.
    * **Manage labels** - Add or remove issue and PR labels.

    #### Use cases

    **Bug Reporting**

    ```
    Developer: "We have a login bug affecting Safari users"
    Assistant: [Creates issue in GitHub repository]
    Assistant: [Adds labels: bug, priority:high, browser:safari]
    Assistant: "I've created issue #234 in the main repo and notified the team."
    ```

    **Repository Search**

    ```
    Developer: "Find our authentication libraries"
    Assistant: [Searches GitHub repos by keyword and topic]
    Assistant: "I found 3 authentication repos: auth-service, jwt-utils, and oauth-client."
    ```

### Greenhouse

    ### Greenhouse

    Connect your AI assistant to Greenhouse for applicant tracking and recruiting workflows.

    #### Prerequisites

    * Greenhouse account with API access.
    * Access to Greenhouse Dev Center.
    * Harvest API permissions.

    #### Required credentials

    When connecting Greenhouse, you'll need to provide:

9. **Harvest API key**

        Log in to Greenhouse, go to **Dev Center → API Credential Management**, create a Harvest API key with the permissions you need, and copy the generated token.

    <img alt="Greenhouse integration credentials dialog showing API Key input field" />

    #### Available tools

    After connecting Greenhouse, your assistant can:

    * **Candidate lookup** - Search for candidates by name, email, or application ID.
    * **Interview scheduling** - View and coordinate interview schedules.
    * **Application management** - Track application status and progress.
    * **Job posting access** - View open positions and job details.
    * **Scorecard review** - Access candidate evaluations and feedback.

    #### Use cases

    **Candidate Status Check**

    ```
    Recruiter: "What's the status of the candidate who interviewed yesterday?"
    Assistant: [Searches Greenhouse by interview date]
    Assistant: "Sarah Johnson completed her technical interview yesterday. She's in the Reference Check stage."
    ```

    **Interview Coordination**

    ```
    Recruiter: "Schedule the next round for top candidates"
    Assistant: [Retrieves candidate list and interview availability]
    Assistant: [Checks interviewer calendars]
    Assistant: "I can schedule 3 final interviews for next Tuesday and Wednesday."
    ```

### HubSpot

    ### HubSpot

    Connect your AI assistant to HubSpot for marketing, sales, and customer service workflows.

    #### Prerequisites

    * HubSpot account with API access.
    * Private app access token or OAuth credentials.

    #### Required credentials

    When connecting HubSpot, you'll need to provide:

10. **Private app token**

        Create a private app in HubSpot (Settings → Integrations → Private Apps) and copy the access token from the **Auth** tab.

    <img alt="HubSpot integration credentials dialog showing Private app token input field" />

    #### Available tools

    After connecting HubSpot, your assistant can:

    * **Manage contacts** - Create, update, or search contacts.
    * **Deal tracking** - Create deals, update deal stages.
    * **Ticket management** - Create support tickets, update status.
    * **Company records** - Access and update company information.
    * **Engagement tracking** - Log calls, emails, and notes.

    #### Use cases

    **Lead Capture**

    ```
    Prospect: "I'd like a demo of your product"
    Assistant: [Creates contact in HubSpot]
    Assistant: [Creates deal in pipeline]
    Assistant: [Schedules demo meeting]
    ```

    **Support Ticketing**

    ```
    Customer: "I have a billing question"
    Assistant: [Searches HubSpot for customer record]
    Assistant: [Creates ticket in support pipeline]
    Assistant: [Associates ticket with contact and deal]
    ```

### Intercom

    ### Intercom

    Connect your AI assistant to Intercom for customer messaging and support workflows.

    #### Prerequisites

    * Intercom account with API access.
    * Permissions to create private apps.
    * Access token with appropriate scopes.

    #### Required credentials

    When connecting Intercom, you'll need to provide:

11. **Access token**

        Create a private app in Intercom (Settings → Developers → Developer Hub → Your Apps → New App) and copy the access token from the authentication section.

    <img alt="Intercom integration credentials dialog showing Access Token input field" />

    #### Available tools

    After connecting Intercom, your assistant can:

    * **Access conversation history** - Retrieve past customer interactions and messages.
    * **Create notes** - Add internal notes to customer conversations.
    * **Update customer attributes** - Modify user data and custom attributes.
    * **Search users** - Find customers by email, user ID, or other identifiers.
    * **Manage tags** - Add or remove conversation tags for organization.

    #### Use cases

    **Customer Support Context**

    ```
    Customer: "I need help with my subscription"
    Assistant: [Searches Intercom for customer by phone/email]
    Assistant: [Reviews conversation history]
    Assistant: "I can see you upgraded to Pro last month. How can I help with your subscription?"
    ```

    **User Data Management**

    ```
    Customer: "Please update my company name"
    Assistant: [Updates customer attributes in Intercom]
    Assistant: [Adds note documenting the change]
    Assistant: "I've updated your company name in our system."
    ```

### Jira

    ### Jira

    Connect your AI assistant to Jira for project management, issue tracking, and software development workflows.

    #### Prerequisites

    * Jira account (Cloud or Server).
    * API token or password.
    * Project access and permissions.

    #### Required credentials

    When connecting Jira, you'll need to provide:

12. **Account email**

        The Jira username or email that has access to the project.

13. **API token**

        Generate a token at [https://id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens) by selecting **Create API token**.

14. **Site URL**

        Provide the base URL of your Jira instance (for example `yourcompany.atlassian.net`) without the `https://` prefix.

    <img alt="Jira integration credentials dialog showing Email, API token, and Site URL input fields" />

    #### Available tools

    After connecting Jira, your assistant can:

    * **Create issues** - Create bugs, tasks, stories, or epics.
    * **Update issues** - Change status, assignee, or priority.
    * **Search issues** - Find issues by project, assignee, or status.
    * **Add comments** - Comment on existing issues.
    * **Transition issues** - Move issues through workflow states.

    #### Use cases

    **Bug Reporting**

    ```
    Developer: "Users are reporting a login error"
    Assistant: [Creates bug in Jira]
    Assistant: [Sets priority to High, component to Authentication]
    Assistant: "Created PROJ-1234. I've assigned it to the on-call engineer."
    ```

    **Task Management**

    ```
    Manager: "Create a task to update the documentation"
    Assistant: [Creates task in Jira project]
    Assistant: [Sets due date based on conversation]
    ```

### Salesforce

    ### Salesforce

    Connect your AI assistant to Salesforce to access customer records, create cases, update opportunities, and more.

    #### Prerequisites

    * Salesforce account with API access.
    * Username and password.
    * Security token (reset in Personal Settings → Reset My Security Token).
    * Organization ID (found in Setup → Company Settings → Company Information).

    #### Required credentials

    When connecting Salesforce, you'll need to provide:

15. **Instance domain**

        Your Salesforce hostname such as `acme.my.salesforce.com` (production) or `acme.sandbox.my.salesforce.com` (sandbox) without `https://` or trailing `/`.

16. **Username**

        The Salesforce username or email with integration access.

17. **Password**

        The password for that Salesforce user.

18. **Security token**

        The security token from Personal Settings → Reset My Security Token (it arrives via email).

19. **Organization ID**

        Your org ID from Setup → Company Settings → Company Information.

    <img alt="Salesforce integration credentials dialog showing Instance domain, Username, Password, Security token, and Organization ID input fields" />

    #### Available tools

    After connecting Salesforce, your assistant can use tools to:

    * **Search records** - Find accounts, contacts, leads, opportunities.
    * **Create records** - Create new cases, leads, tasks, or opportunities.
    * **Update records** - Modify existing records with new information.
    * **Query data** - Run SOQL queries for custom data retrieval.

    #### Use cases

    **Customer Service**

    ```
    Customer: "I need help with my recent order"
    Assistant: [Searches Salesforce for customer by phone number]
    Assistant: "I found your account, let me check your recent orders..."
    ```

    **Lead Qualification**

    ```
    Prospect: "I'm interested in your enterprise plan"
    Assistant: [Creates lead in Salesforce with details from conversation]
    Assistant: [Updates lead score based on budget and timeline discussed]
    ```

    **Case Management**

    ```
    Customer: "My service is down"
    Assistant: [Creates high-priority case in Salesforce]
    Assistant: "I've created case #12345 for you. Our team will reach out within 2 hours."
    ```

### ServiceNow

    ### ServiceNow

    Connect your AI assistant to ServiceNow for IT service management, incident tracking, and workflow automation.

    #### Prerequisites

    * ServiceNow instance with API access.
    * User account with appropriate roles (e.g., itil, admin).
    * Instance URL and credentials.

    #### Required credentials

20. **Instance URL**

        Provide the ServiceNow hostname, for example `acme.service-now.com` or `acme-dev.service-now.com`.

21. **Username**

        Supply the ServiceNow user with the necessary roles.

22. **Password**

        Enter the password for that user.

    <img alt="ServiceNow integration credentials dialog showing Instance URL, Username, and Password input fields" />

    #### Available tools

    After connecting ServiceNow, your assistant can:

    * **Create incidents** - Log IT incidents with priority and categorization.
    * **Update tickets** - Modify incident status, assignment, or details.
    * **Search knowledge base** - Find KB articles for issue resolution.
    * **Query records** - Access CMDB, user records, or service catalogs.

    #### Use cases

    **IT Support**

    ```
    Employee: "My laptop won't connect to WiFi"
    Assistant: [Creates incident in ServiceNow]
    Assistant: [Categorizes as Network → WiFi]
    Assistant: "I've logged incident INC0012345. IT will assist you shortly."
    ```

    **Service Requests**

    ```
    Employee: "I need access to the marketing drive"
    Assistant: [Creates service request in ServiceNow]
    Assistant: [Routes to appropriate approval group]
    ```

### Zendesk

    ### Zendesk

    Connect your AI assistant to Zendesk for customer service and support workflows.

    #### Prerequisites

    * Zendesk account with API access.
    * Admin access to generate API tokens.
    * Subdomain and email credentials.

    #### Required credentials

    When connecting Zendesk, you'll need to provide:

23. **Subdomain**

        Enter only the subdomain portion (e.g., `company` if your portal is `company.zendesk.com`); the rest is added automatically.

24. **Email**

        The Zendesk account email that owns the API token.

25. **API token**

        Generate a token in Admin Center → Apps and integrations → APIs → Zendesk API.

    <img alt="Zendesk integration credentials dialog showing Subdomain, Email, and API token input fields" />

    #### Available tools

    After connecting Zendesk, your assistant can:

    * **Create tickets** - Log customer support requests with priority and categorization.
    * **Search customer history** - Find previous tickets and interactions by customer.
    * **Update ticket status** - Modify ticket status, assignment, or priority.
    * **Access knowledge base** - Search KB articles for issue resolution.

    #### Use cases

    **Support Ticketing**

    ```
    Customer: "I'm having an issue with my account login"
    Assistant: [Creates ticket in Zendesk]
    Assistant: [Categorizes as Account → Login Issues]
    Assistant: "I've created ticket #12345. Our support team will reach out within 2 hours."
    ```

    **Customer History Lookup**

    ```
    Customer: "What's the status of my previous request?"
    Assistant: [Searches Zendesk by phone number or email]
    Assistant: "I found your ticket #12340 from last week. It was resolved on Monday."
    ```

### Coval

    ### Coval

    Connect your AI assistant to [Coval](https://www.coval.dev/) for automated simulation, evaluation, and production monitoring of voice and chat agents.

    > **Note:** Coval is a **testing and evaluation** tool — unlike the other integrations on this page, it does not add tools your assistant uses during conversations. Instead, it tests and monitors the assistant itself, helping you catch regressions and validate behavior at scale.

    #### Prerequisites

    * Coval account at [coval.dev](https://www.coval.dev/).
    * A configured Telnyx AI assistant to evaluate.

    #### Required credentials

    When connecting Coval, you'll need to provide:

26. **Coval API key**

        Log in to your Coval dashboard, navigate to your workspace settings, and copy your API key.

    #### Capabilities

    After connecting Coval, you can:

    * **Automated scenario simulation** — Generate thousands of test scenarios from a few seed cases, covering edge cases and unexpected user behaviors.
    * **CI/CD regression testing** — Automatically detect performance regressions on every code change before deploying to production.
    * **Production monitoring** — Log live calls, receive instant alerts for performance drops, and replay transcripts and audio.
    * **Built-in evaluation metrics** — Measure latency, accuracy, tool-call effectiveness, and instruction compliance across all interactions.

    #### Use cases

    **Pre-deployment validation**

    ```
    Run hundreds of simulated conversations against your assistant to verify
    it handles greetings, edge cases, and tool calls correctly before going live.
    ```

    **Regression testing in CI/CD**

    ```
    Add Coval evaluation steps to your deployment pipeline so every assistant
    update is automatically tested against your scenario library.
    ```

    **Production quality monitoring**

    ```
    Monitor live assistant conversations for performance drops, then replay
    specific calls to diagnose issues.
    ```

## Managing integrations

### Viewing connected integrations

27. **Open your assistant**

    Navigate to the assistant you want to review in the Mission Control Portal.

28. **Select Integrations**

    Open the **Integrations** tab.

29. **Review Connected section**

    View everything listed under **Connected Integrations**.

<img alt="Integrations section displaying Jira under Connected Integrations with description and unassign button" />

### Disconnecting an integration

To disconnect an integration from your assistant:

30. **Open the assistant integration tab**

    Navigate to your assistant and open the **Integrations** tab.

31. **Locate the integration**

    Find it within the **Connected Integrations** list.

32. **Unassign**

    Click the chain-link **unassign** button.

33. **Confirm**

    Approve the confirmation dialog to finish disconnecting.

<img alt="Jira integration card in Connected Integrations showing unassign button (chain link icon)" />

After disconnecting:

* The integration is removed from this assistant.
* All associated tools are disabled for this assistant.
* The integration moves to **Available Integrations** and can be reconnected later.

> **Note:** Disconnecting an integration only removes it from the current assistant. The integration remains in your account and can be connected to other assistants or reconnected to this one.

### Deleting an integration

To permanently delete an integration from your account:

34. **Open the Integrations tab**

    Navigate to your AI assistant and open the **Integrations** tab.

35. **Find the integration**

    Look under **Available Integrations**.

36. **Delete**

    Click the trash icon next to the integration.

37. **Confirm**

    Approve the deletion to remove stored credentials permanently.

<img alt="Jira integration card in Available Integrations showing connect button and delete button (trash icon)" />

> **Warning:** Deleting an integration permanently removes it from your account, including all stored credentials. You will need to set it up again from scratch if you want to use it in the future.

## Best practices

### Security

38. **Use dedicated service accounts**

    Create integration-specific profiles with only the permissions the workflow needs.

39. **Rotate credentials regularly**

    Update API tokens and passwords on a routine cadence.

40. **Monitor usage**

    Review integration activity through platform audit logs.

41. **Limit permissions**

    Grant only the scopes required for each integration use case.

42. **Use sandbox environments**

    Test and validate integrations in non-production environments first.

### Configuration

43. **Start with read-only tools**

    Enable search/read capabilities first, then gradually introduce write actions.

44. **Provide clear descriptions**

    Document when and how each tool should be used so assistants respond correctly.

45. **Test thoroughly**

    Validate integration behavior across multiple conversation scenarios.

46. **Use tool parameters**

    Configure sensible defaults (e.g., priority, project) to reduce user input errors.

47. **Handle errors gracefully**

    Define fallback behavior when integration calls fail or return unexpected results.

### Performance

48. **Minimize API calls**

    Avoid duplicate searches or redundant requests where possible.

49. **Cache frequently accessed data**

    Store reusable values (for example, via dynamic variables) for the duration of a session.

50. **Set appropriate timeouts**

    Configure timeout thresholds that balance responsiveness with reliability.

51. **Monitor rate limits**

    Track provider limits and design workflows to stay within allocation.

## Troubleshooting

### Connection failures

**Symptom**: Unable to connect integration, credentials rejected.

**Solutions**:

* Verify credentials are correct and have not expired.
* Check that the user account has API access enabled.
* Ensure security tokens or API keys are current.
* For Salesforce: Confirm security token is included.
* For cloud platforms: Verify instance URL format (no `https://` or trailing `/`).

### Tools not appearing

**Symptom**: Integration connected but no tools available.

**Solutions**:

* Refresh the page and check again.
* Verify the integration account has required permissions.
* Check that the platform subscription includes API access.
* Disconnect and reconnect the integration.

### Authentication errors during calls

**Symptom**: Tools fail with authentication errors during conversations.

**Solutions**:

* Regenerate API tokens or security tokens.
* Update stored credentials in the integration.
* Verify account has not been locked or suspended.
* Check IP allowlists (if applicable).

### Missing data or records

**Symptom**: Assistant cannot find expected records.

**Solutions**:

* Verify the integration account can access the records.
* Check record permissions and sharing settings.
* Confirm records exist in the platform.
* Verify search parameters and filters.

### Rate limiting

**Symptom**: Integration calls fail with rate limit errors.

**Solutions**:

* Reduce frequency of integration calls.
* Implement caching for frequently accessed data.
* Contact platform support to increase limits.
* Distribute calls across multiple service accounts.

## Next steps

* **[Voice Assistant Quickstart](https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant)** - Learn how to create and configure AI assistants.
* **[Workflow](workflow.md)** - Visualize how your integrations and tools connect in your assistant's conversation flow.
* **[Agent Handoff](https://developers.telnyx.com/docs/inference/ai-assistants/agent-handoff)** - Enable multiple specialized assistants with integrations.
* **[Dynamic Variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)** - Pass integration-specific context to your assistant.
* **[API Reference](https://developers.telnyx.com/api-reference/assistants/list-assistants)** - Programmatic assistant management.

## Related resources

* [Integration Secrets](https://portal.telnyx.com/#/integration-secrets) - Securely store API keys and tokens.
* [AI Assistants Portal](https://portal.telnyx.com/#/ai/assistants) - Configure assistants and integrations.


## Related Pages

- [Voice Assistant Quickstart](../runbooks/voice-assistant-quickstart.md)
