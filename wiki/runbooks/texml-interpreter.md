---
title: TeXML Interpreter
summary: TeXML is an XML based data structure used by Telnyx to build quick applications.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-interpreter/index
    content_hash: 80f44c23d05377929782d3e9bd93c428468a7f2dcfeb2463eae22072d74d2802
updated_at: 2026-04-10T00:00:00Z
---

# TeXML Interpreter

TeXML is an XML based data structure used by Telnyx to build quick applications

## Basic Syntax

A proper TeXML response comprises the following elements:

* **`` element** -- tag defining the body of the TeXML document
* **verb** -- an XML tag denoting the desired action
* **noun** -- an XML tag denoting the object of the desired action

Here is a simple TeXML file containing an example of a **verb** and **noun** used together:

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

<!-- TeXML files must contain the Response element -->

 <!-- Say and Dial are Verbs -->
    Thank you for calling Telnyx. Please hold.

   <!-- Number is a Dial Noun -->
        +13129457420

```

## Dynamic parameters

When creating a TeXML set of instructions you can make use of [Mustache Templates](https://mustache.github.io/mustache.5.html) to generate instructions dynamically at runtime.

### Inserting dynamic content

You can make use of Mustache Dynamic templating to insert content into your TeXML instructions through HTTP request parameters in the webhook URL we use to fetch your TeXML set of instructions. For example, you could create a TeXML set of instructions that calls a number that is set until the HTTP request is made to fetch your TeXML instructions.

You first create your TeXML instructions using Mustache Templating and set the `{{PhoneNumber}}` as a variable like this

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    {{PhoneNumber}}

```

The phone number can now be replaced at runtime by setting your TeXML webhook URL to have `PhoneNumber` as a parameter.

```bash theme={null}
curl -X POST https://api.telnyx.com/v2/texml/calls/{connection_id} \
--data-urlencode "To=+13121230000" \
--data-urlencode "From=+13120001234" \
--data-urlencode "Url=https://www.example.com/texml.xml?PhoneNumber=+18771234567" \
--data-urlencode "StatusCallback=https://www.example.com/statuscallback-listener" \
--header "Authorization: Bearer YOUR_API_KEY"
```

The request parameters set by Telnyx, i.e. CallSid, From, and To are also available for the Mustache Template. The list of the parameters for each of the callbacks can be found on our developer [documentation page](https://developers.telnyx.com/api-reference/texml-applications/list-all-texml-applications).

### Iterate through lists

You can set arrays as parameters in your TeXML webhook URL and let Mustache Template handle them. If for example, you want the dial command to have two numbers, you could add a `Numbers` list parameter to your callback Url.

```bash theme={null}
curl -X POST https://api.telnyx.com/v2/texml/calls/{connection_id} \
--data-urlencode "To=+13121230000" \
--data-urlencode "From=+13120001234" \
--data-urlencode "Url=https://www.example.com/texml.xml?PhoneNumbers[]=+18771234567&PhoneNumbers[]=+18771234568" \
--data-urlencode "StatusCallback=https://www.example.com/statuscallback-listener" \
--header "Authorization: Bearer YOUR_API_KEY"
```

Then you can handle the `PhoneNumbers` parameter in the TeXML instructions using the following syntax.

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

  {{#PhoneNumbers}}
    {{.}}
  {{/PhoneNumbers}}

```

This will end up being parsed as

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    +18771234567
    +18771234568

```

### Render conditional content

Conditional content is supported by using `if/else` statements in the TeXML instructions. You could define a set of instructions to dial a specific number depending on `From` parameter present in the HTTP request.

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

{{#if From == +18771234567}}

    +18771234568

{{#elseif From == +18771234568}}

    +18771234567

{{#else}}
  No valid number is present
{{/if}}

```

Supported operators are `==`, `!=` and no operator for checking if the parameter value is not null.
