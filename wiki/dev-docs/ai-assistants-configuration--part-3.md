---
title: AI Assistants Configuration
summary: Covers advanced configuration options for Telnyx AI assistants, including
  client-side tools, custom LLM providers, dynamic variables, webhook filler messages,
  and importing assistants from third-party providers.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/client-side-tools
- url: https://developers.telnyx.com/docs/inference/ai-assistants/custom-llm
- url: https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables
- url: https://developers.telnyx.com/docs/inference/ai-assistants/filler-messages
- url: https://developers.telnyx.com/docs/inference/ai-assistants/importing/index
updated_at: 2026-08-05T13:45:16Z
---

# AI Assistants Configuration

*Part 3 of 5 — see also: [Part 1](ai-assistants-configuration--part-1.md), [Part 2](ai-assistants-configuration--part-2.md), [Part 4](ai-assistants-configuration--part-4.md), [Part 5](ai-assistants-configuration--part-5.md)*

Covers advanced configuration options for Telnyx AI assistants, including client-side tools, custom LLM providers, dynamic variables, webhook filler messages, and importing assistants from third-party providers.

## Dynamic Variables

Dynamic variables let you configure a template for your agent's behavior. You can re-use the same general instructions while dynamically personalizing every conversation your agent has.

### Overview

Dynamic variables enable you to create a single AI assistant configuration that can handle personalized conversations for different users and contexts. Instead of creating multiple assistants for different scenarios, you can use placeholders that get filled with specific values at runtime.

#### How dynamic variables work

The dynamic variable lifecycle follows these steps:

1. **Define**: Create placeholders in your assistant's instructions, greeting, or tools using `{{variable_name}}` syntax.
2. **Inject**: Provide values through API calls, webhooks, SIP headers, or default configurations.
3. **Resolve**: Telnyx replaces placeholders with actual values when the conversation starts.
4. **Use**: Your assistant uses the personalized content throughout the conversation.

#### Key benefits

- **Scalability**: One assistant configuration serves multiple use cases.
- **Personalization**: Each conversation can be tailored to specific users or contexts.
- **Efficiency**: Reduce configuration overhead and maintenance complexity.
- **Flexibility**: Update values dynamically without modifying the assistant.

#### Common use cases

- **Customer Service**: Personalize greetings with customer names and account details.
- **Appointment Scheduling**: Include facility names, departments, and contact information.
- **Account Management**: Reference specific account numbers, balances, or service details.
- **Healthcare**: Customize interactions with patient names, appointment types, and provider information.

### Best practices

#### Variable naming and organization

- **Use descriptive names**: Choose clear, meaningful variable names like `customer_name` instead of generic names like `name`.
- **Follow consistent conventions**: Use snake_case for variable names (`facility_name`, `account_number`).
- **Group related variables**: Organize logically related variables together (`facility_name`, `facility_department`, `facility_contact`).
- **Avoid reserved namespaces**: Don't use the `telnyx_` prefix, which is reserved for system variables.

```
// Good variable naming
{
  "customer_name": "Sarah Johnson",
  "account_number": "ACC-12345",
  "facility_name": "Memorial Hospital",
  "facility_department": "Cardiology"
}

// Poor variable naming
{
  "name": "Sarah",
  "num": "12345",
  "place": "Hospital",
  "dept": "Card"
}
```

#### Implementation strategy

- **Start with defaults**: Set default values in the Assistant builder for testing and as fallback values.
- **Use API injection for dynamic data**: Pass call-specific values through the `AIAssistantDynamicVariables` parameter in API calls.
- **Leverage webhooks for complex lookups**: Use the dynamic variables webhook for real-time data retrieval or database lookups.
- **Implement graceful degradation**: Ensure your assistant can handle scenarios where variables fail to resolve.

#### Security and data handling

- **Protect sensitive information**: Be cautious about including sensitive data in variables that may appear in logs.
- **Validate webhook data**: Implement proper validation for data returned from webhook endpoints.
- **Consider data retention**: Review your data retention and privacy requirements for variable content.
- **Handle timeouts gracefully**: Webhook responses must return within the configured timeout (default 1.5 seconds, up to 10 seconds via `dynamic_variables_webhook_timeout_ms`) or the call proceeds with fallback values.

#### Performance and reliability

- **Optimize webhook response time**: Keep webhook responses fast (well under your configured timeout; the default is 1.5 seconds).
- **Implement error handling**: Plan for scenarios where webhooks fail or return invalid data.
- **Use caching strategies**: Cache frequently accessed data to improve response times.
- **Test across channels**: Verify variable resolution works consistently across phone calls, web calls, and SMS.

#### Testing and debugging

- **Test with Portal defaults**: Use the Assistant builder's default values to test variable behavior during development.
- **Monitor webhook logs**: Use the conversation transcript and webhook logs in the Portal to debug variable resolution issues.
- **Validate fallback behavior**: Ensure unresolved variables (displayed as `{{variable_name}}`) don't break conversation flow.
- **Test transfer scenarios**: Verify that variables pass correctly when using transfer tools with SIP headers.

#### Cross-channel considerations

- **Ensure universal compatibility**: Test that your variables work across phone calls, web calls, and SMS channels.
- **Handle channel-specific data**: Consider how variables might behave differently across conversation channels.
- **Plan for transfer scenarios**: When transferring calls, use SIP headers to pass variable data to the receiving assistant.

### Dynamic variables syntax

Dynamic variables are placeholders surrounded by double curly braces. For example:

```
Hello, this is ABC Ambulance. Am I speaking with {{full_name}} with {{facility_name}} - {{facility_department}}?"
```

You can template them in the following fields:

- Instructions
- Greeting
- Tools

### Telnyx system variables

Telnyx also provides these system variables:

| Variable | Description | Example |
| --- | --- | --- |
| `{{telnyx_current_time}}` | The current date and time in UTC | `Monday, February 24 2025 04:04:15 PM UTC` |
| `{{telnyx_conversation_channel}}` | This can be `phone_call` , `web_call`, or `sms_chat` | `phone_call` |
| `{{telnyx_agent_target}}` | The phone number, SIP URI, or other identifier associated with the agent. | `+13128675309` |
| `{{telnyx_end_user_target}}` | The phone number, SIP URI, or other identifier associated with the end user | `+15551234567` |
| `{{telnyx_shaken_stir_attestation}}` | The SHAKEN/STIR attestation level for inbound phone calls, if available. This can be `a`, `b`, or `c`. | `a` |
| `{{call_control_id}}` | The call control ID for the call, if applicable | `v3:u5OAKGEPT3Dx8SZSSDRWEMdNH2OripQhO` |

#### Date and time variables

In addition to the default `{{telnyx_current_time}}`, Telnyx provides a family of reserved date/time variables. Use these to give the assistant timezone-aware context, convenient shorthands, or a fully custom format. The timezone variants and shorthands use the same default formatting as `{{telnyx_current_time}}` — a different format is only used when you explicitly specify one with the `date` filter.

| Variable | Description | Example output |
| --- | --- | --- |
| `{{telnyx_current_time_<IANA tz>}}` | Current date and time, in the given timezone | `Monday, February 24 2025 11:04:15 AM EST` |
| `{{telnyx_current_date}}` | Current date (UTC) | `February 24 2025` |
| `{{telnyx_current_time_of_day}}` | Current time of day (UTC) | `04:04:15 PM UTC` |
| `{{telnyx_current_time_of_day_<IANA tz>}}` | Current time of day, in the given timezone | `11:04:15 AM EST` |
| `{{telnyx_current_weekday}}` | Current day of the week (UTC) | `Monday` |
| `{{telnyx_current_month}}` | Current month name (UTC) | `February` |
| `{{telnyx_current_day}}` | Current day of the month (UTC) | `24` |
| `{{telnyx_current_year}}` | Current year (UTC) | `2025` |

The shorthand variables (`telnyx_current_date`, `telnyx_current_time_of_day`, `telnyx_current_weekday`, `telnyx_current_month`, `telnyx_current_day`, `telnyx_current_year`) are evaluated in UTC. To render them for a specific timezone, use the `_<tz>` variants or the `date` filter described below.

##### Timezone variants

Append an [IANA timezone name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) to `telnyx_current_time_` or `telnyx_current_time_of_day_` to render the value in that zone. These use the same default formatting as `{{telnyx_current_time}}`:

- `{{telnyx_current_time_America/New_York}}` → `Monday, February 24 2025 11:04:15 AM EST`
- `{{telnyx_current_time_Australia/Sydney}}` → `Tuesday, February 25 2025 03:04:15 AM AEDT`
- `{{telnyx_current_time_of_day_Europe/London}}` → `04:04:15 PM GMT`

##### Custom formatting with the `date` filter

The default format is used everywhere unless you explicitly request a different one. For full control over formatting, pipe `telnyx_current_time` through the `date` filter. The filter takes a standard [`strftime`](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) format string and an optional IANA timezone. These are the same `%`-style codes used by `strftime` across most languages (C, Python, Ruby, and others):

| Template | Example output |
| --- | --- |
| `{{ telnyx_current_time | date: "%A, %B %d, %Y" }}` | `Monday, February 24, 2025` (UTC) |
| `{{ telnyx_current_time | date: "%I:%M %p", "America/New_York" }}` | `11:04 AM` (in the given zone) |
| `{{ telnyx_current_time | date: "%A, %B %d, %Y at %I:%M %p %Z", "America/Los_Angeles" }}` | `Monday, February 24, 2025 at 08:04 AM PST` |

When the timezone argument is omitted, the value is formatted in UTC.

###### Common format codes

These are the most useful `strftime` codes for the `date` filter. For the complete list, see any [standard `strftime` reference](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes):

| Code | Meaning | Example |
| --- | --- | --- |
| `%A` | Weekday name | `Monday` |
| `%a` | Abbreviated weekday | `Mon` |
| `%B` | Month name | `February` |
| `%b` | Abbreviated month | `Feb` |
| `%d` | Day of month (zero-padded) | `24` |
| `%Y` | Four-digit year | `2025` |
| `%I:%M %p` | 12-hour time | `11:04 AM` |
| `%H:%M` | 24-hour time | `16:04` |
| `%Z` | Timezone abbreviation | `PST` |
| `%z` | UTC offset | `-0800` |

Combine codes with any literal text, e.g. `%A, %B %d at %I:%M %p %Z`.

If a timezone is unknown, a format string is invalid, or a variable is unrecognized, the template placeholder is left untouched rather than rendered to an empty or error value.

### Customer-defined dynamic variables

You can also define your own variables. There are several ways to resolve a customer-defined dynamic variable before a conversation. They follow this order of precedence.

**1. Pass the variables via the outbound API call**

```
curl --request POST \
  --url https://api.telnyx.com/v2/texml/ai_calls/<texml_app_id> \
  --header "Authorization: Bearer $TELNYX_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
      "From": "+13128675309",
      "To": "+15551234567",
      "AIAssistantId": "assistant-6207ab25-b185-478f-b2ef-85159e226727",
      "AIAssistantDynamicVariables": {
        "full_name": "James Smith",
        "facility_name": "Cleveland Clinic Main Campus",
        "facility_department": "Emergency Department"
      }
  }'
```

![AI Assistant Outbound Call Variables](https://mintcdn.com/telnyx/33ANQJ-HKUTIlR5u/img/call-dynamic-vars.png?fit=max&auto=format&n=33ANQJ-HKUTIlR5u&q=85&s=2c483d56dbdae39d797906c1a9f85c4d)

**2. Custom SIP Headers**

Custom SIP headers using the `X-` prefix will be mapped to dynamic variables. Header names are case-insensitive, and `-` in the header names will be replaced by `_` in the variable names. For instance, `X-Full-Name` will be resolved as `{{full_name}}`.

*Telnyx reserves the `{{telnyx_}}` namespace for system variables, meaning SIP headers beginning `X-Telnyx` will not be resolved to dynamic variables.*

Here you can see an example of passing a dynamic variable to another AI Assistant using custom SIP headers in the Transfer tool.

![AI Assistant SIP Header Config](https://mintcdn.com/telnyx/33ANQJ-HKUTIlR5u/img/ai-assistant-custom-sip-variable.png?fit=max&auto=format&n=33ANQJ-HKUTIlR5u&q=85&s=d6598863fdf9ae05590b3568878edad1)

**3. Configure Dynamic Variables Webhook**

If the `dynamic_variables_webhook_url` is set for the assistant, we will `POST` the following payload at the start of the conversation. Telnyx will [sign this webhook](https://developers.telnyx.com/development/api-fundamentals/webhooks/receiving-webhooks#webhook-signing) so that the authenticity of the request can be verified.

![AI Assistant Variable Config](https://mintcdn.com/telnyx/d2AUJO5qdne_WnZI/img/configure-dynamic.png?fit=max&auto=format&n=d2AUJO5qdne_WnZI&q=85&s=2868ce1f60c770a3d22a10d080163cce)

```
{
  "data": {
    "record_type": "event",
    "id": "event_12345678-90ab-cdef-1234-567890abcdef",
    "event_type": "assistant.initialization",
    "occurred_at": "2025-04-07T10:00:00Z",
    "payload": {
      "telnyx_conversation_channel": "phone_call",
      "telnyx_agent_target": "+13128675309",
      "telnyx_end_user_target": "+15551234567",
      "telnyx_end_user_target_verified": false,
      "call_control_id": "v3:u5OAKGEPT3Dx8SZSSDRWEMdNH2OripQhO",
      "assistant_id": "assistant_12345678-90ab-cdef-1234-567890abcdef"
    }
  }
}
```

*For inbound phone calls to an assistant, the `telnyx_end_user_target_verified` field will be set to `true` if the call has Full (A) [STIR/SHAKEN attestation](https://support.telnyx.com/en/articles/5402969-stir-shaken-with-telnyx) and Telnyx was able to verify the authenticity of the PASSporT token.*

We expect a JSON response with the following structure. If we do not receive this response within the configured timeout (default 1.5 seconds, up to 10 seconds via the `dynamic_variables_webhook_timeout_ms` field on the assistant), the call will proceed "best effort" with the alternatives listed below. All three fields (`dynamic_variables`, `memory`, and `conversation`) are optional. The `dynamic_variables` field sets the values for the specified dynamic variables. You can read more about the `memory` and `conversation` fields in our [tutorial on Memory](https://developers.telnyx.com/docs/inference/ai-assistants/memory).

```
{
  "dynamic_variables": {
    "full_name": "Rachel Thomas",
    "facility_name": "UCHealth",
    "facility_department": "Cardiology",
    "account_number": "ACC-12345",
    "appointment_time": "2:30 PM"
  },
  "memory": {
    "conversation_query": "metadata->telnyx_end_user_target=eq.+13128675309&limit=5&order=last_message_at.desc"
  },
  "conversation": {
    "metadata": {
      "customer_tier": "premium",
      "preferred_language": "en",
      "timezone": "America/Denver"
    }
  }
}
```

**4. Configure default dynamic variables in the Assistant builder**

In the above view, you can also set default values for dynamic variables at the agent level. These will serve as a fallback if any of the above mechanisms do not properly resolve a variable.

**5. Unset variables**

Variables not set by any of the above methods will remain in their raw form (`{{full_name}}`).

### Troubleshooting

#### Common issues

##### Variables not resolving

When variables appear as raw text (`{{variable_name}}`) in conversations, check these potential causes:

- **Webhook timeout**: Your webhook endpoint took longer than the configured timeout (default 1.5 seconds) to respond, causing fallback to defaults.
- **Variable name mismatch**: Typos or case sensitivity differences between variable definition and usage.
- **Incorrect precedence**: Understanding the resolution order (API > SIP headers > webhook > defaults).
- **Missing configuration**: Variable not defined in any resolution method.

##### Incorrect formatting

Variables may not work correctly due to formatting issues:

- **Invalid JSON**: Webhook responses contain malformed JSON syntax.
- **Wrong data types**: Sending numbers instead of strings or vice versa.
- **Missing required fields**: Webhook response missing `dynamic_variables` object.
- **Template syntax errors**: Incorrect mustache template usage (`{variable}` instead of `{{variable}}`).

##### Timeout issues

Webhook timeouts are a common source of variable resolution failures:

- **Slow database queries**: Optimize database lookups in webhook endpoints.
- **Network connectivity**: Check firewall rules and network connectivity to webhook URLs.
- **External service delays**: Implement proper timeout handling for third-party API calls.
- **Processing overhead**: Minimize computation time in webhook response generation.

#### Debugging checklist

Follow this step-by-step process to diagnose variable issues:

##### 1. Verify variable definition

- Check variable name spelling and case sensitivity.
- Confirm variables are used in supported fields (`instructions`, `greeting`, `tools`).
- Validate mustache syntax: `{{variable_name}}`.
- Ensure variable names don't use reserved `telnyx_` prefix.

##### 2. Check resolution priority

Test variables using the resolution hierarchy:

```
# Test API injection (highest priority)
curl --request POST \
  --url https://api.telnyx.com/v2/texml/ai_calls/<texml_app_id> \
  --header "Authorization: Bearer $TELNYX_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
      "From": "+13128675309",
      "To": "+15551234567",
      "AIAssistantId": "assistant-6207ab25-b185-478f-b2ef-85159e226727",
      "AIAssistantDynamicVariables": {
        "test_variable": "API_VALUE"
      }
  }'
```

- Verify SIP header format for transfer scenarios: `X-Variable-Name` becomes `{{variable_name}}`.
- Confirm webhook endpoint is reachable and responding correctly.
- Set default values in Assistant builder as fallback.

##### 3. Validate webhook implementation

- Test webhook endpoint independently using tools like Postman.
- Verify JSON response format matches expected structure.
- Check response time (must be under the configured timeout; default is 1.5 seconds).
- Validate all required payload fields are present.

##### 4. Test in Portal

- Use Assistant builder default values for initial testing.
- Review conversation logs for variable resolution behavior.
- Check webhook logs for errors, timeouts, or unexpected responses.

#### Webhook debugging

##### Using webhook logs effectively

To facilitate troubleshooting webhook issues, logs are viewable per conversation in the portal alongside the conversation transcript and insights.

![AI Assistant Webhook Logs](https://mintcdn.com/telnyx/fKocYsWR7KyFBdpc/img/dynamic-webhook-log.png?fit=max&auto=format&n=fKocYsWR7KyFBdpc&q=85&s=8fcd9dacddabfddfb84ce3c35c46afed)

**Understanding webhook logs:**

- **Request logs**: Show the exact payload Telnyx sent to your webhook
- **Response logs**: Display your webhook's response and any errors
- **Timing information**: Reveals if responses exceeded the configured timeout
- **Error details**: Provide specific error messages for failed requests

##### Common webhook issues

**Authentication failures:**

```
// Webhook response indicating auth failure
{
  "error": "Unauthorized: Invalid API key",
  "dynamic_variables": {}
}
```

**Malformed JSON responses:**

```
// Incorrect - missing quotes around keys
{
  dynamic_variables: {
    customer_name: "John Doe"
  }
}

// Correct JSON format
{
  "dynamic_variables": {
    "customer_name": "John Doe"
  }
}
```

**Timeout handling:**

```
// Webhook response for timeout scenarios
{
  "dynamic_variables": {
    "customer_name": "Default Name"
  },
  "message": "External service timeout, using cached data"
}
```

##### Testing webhook endpoints

**Independent webhook testing:**

```
# Test your webhook with the exact payload Telnyx sends
curl --request POST \
  --url https://your-webhook-url.com/dynamic-variables \
  --header 'Content-Type: application/json' \
  --data '{
    "data": {
      "record_type": "event",
      "id": "event_12345678-90ab-cdef-1234-567890abcdef",
      "event_type": "assistant.initialization",
      "occurred_at": "2025-04-07T10:00:00Z",
      "payload": {
        "telnyx_conversation_channel": "phone_call",
        "telnyx_agent_target": "+13128675309",
        "telnyx_end_user_target": "+15551234567",
        "call_control_id": "v3:test-call-control-id"
      }
    }
  }'
```

#### Variable validation

##### Input validation

**Sanitize variable values:**

```
// Good - Clean, safe variable values
{
  "dynamic_variables": {
    "customer_name": "John Smith",
    "account_number": "ACC-12345",
    "appointment_time": "2:30 PM"
  }
}

// Avoid - Potentially problematic values
{
  "dynamic_variables": {
    "customer_name": "<script>alert('xss')</script>",
    "account_number": "'; DROP TABLE users; --",
    "appointment_time": null
  }
}
```

**Handle special characters properly:**

- Escape quotes and backslashes in variable content.
- Validate data types match expected formats.
- Provide meaningful defaults for empty or null values.

##### Response format validation

**Ensure proper JSON structure:**

```
// Complete webhook response format
{
  "dynamic_variables": {
    "customer_name": "Sarah Johnson",
    "facility_name": "Memorial Hospital"
  },
  "memory": {
    "conversation_query": "metadata->customer_id=eq.12345"
  },
  "conversation": {
    "metadata": {
      "customer_tier": "premium"
    }
  }
}
```

##### Testing scenarios

**Cross-channel testing:**

- Verify variables work consistently across phone calls, web calls, and SMS.
- Test variable behavior in transfer scenarios using SIP headers.
- Validate fallback behavior when webhook endpoints are unavailable.

**Load testing:**

- Test webhook endpoint performance under expected call volumes.
- Verify response times remain under your configured timeout (default 1.5 seconds) during peak usage.
- Monitor for memory leaks or performance degradation over time.
