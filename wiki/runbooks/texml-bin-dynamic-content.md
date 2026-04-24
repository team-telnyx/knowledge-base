---
title: TeXML Bin Dynamic Content
summary: Telnyx's TeXML service provides dynamic text-to-speech translation for your applications.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-bin-dynamic/index
    content_hash: 71f10b9dc639069ca64919a2b49accfd8b73291d0d5b543b15b8533a602cb290
updated_at: 2026-04-10T00:00:00Z
---

# TeXML Bin Dynamic Content

Telnyx's TeXML service provides dynamic text-to-speech translation for your applications. With TeXML, you can easily create and manage voice commands, menus, and more.

In this guide, we’ll cover how to create dynamic parameters in TeXML Bin using <a href="https://mustache.github.io/mustache.5.html">Mustache Templates</a>.

You can get started with TeXML Bin in the Mission Control Portal by following the first steps in our [previous guide](https://developers.telnyx.com/docs/voice/programmable-voice/texml-bin-quickstart "TeXML Bin Static Interactions").

## Dynamic parameters for TeXML

<a href="https://mustache.github.io/mustache.5.html">Mustache</a> is a logic-less web template system used mainly for mobile and web applications. And a great way to generate instructions dynamically at runtime when creating a TeXML set of instructions.

By using Mustache Dynamic templating you can insert content into your TeXML instructions through HTTP request parameters in the webhook URL that is used to fetch your TeXML set of instructions.

For example, you could create a TeXML set of instructions that calls a phone number which is set until the HTTP request is made to fetch your TeXML instructions.

To do this you'll first need create your TeXML instructions using Mustache Templating, and set the `{{PhoneNumber}}` as a variable like this:

```xml theme={null}
  <?xml version="1.0" encoding="UTF-8"?>

       {{PhoneNumber}}    

```

<Callout type="info">
  After pasting the above content, kindly check and remove any new lines added

The phone number can now be replaced at runtime by setting your TeXML webhook url to have `PhoneNumber` as a parameter like so:

<Callout type="info">
  *Don't forget to update `YOUR_API_KEY` here.*

```bash theme={null}
    curl -X POST https://api.telnyx.com/v2/texml/calls/{connection_id} \
    --data-urlencode "To=+13121230000" \
    --data-urlencode "From=+13120001234" \
    --data-urlencode "Url=https://www.example.com/texml.xml?PhoneNumber=+18771234567" \
    --data-urlencode "StatusCallback=https://www.example.com/statuscallback-listener" \
    --header "Authorization: Bearer YOUR_API_KEY"
```

The request parameters set by Telnyx - for example, CallSid, From and To - are also available for the Mustache Template. The list of parameters for each of the callbacks can be found on our [TeXML Instruction Fetching](https://developers.telnyx.com/docs/voice/programmable-voice/texml-instruction-fetching "TeXML Instruction Fetching") page.

### Iterating through lists

TeXML Bin allows users to set arrays as parameters in the TeXML webhook url and let Mustache Template handle them.

For example, if you want the dial command to have two numbers, you could add a `Numbers` list parameter to your callback Url.

```bash theme={null}
    curl -X POST https://api.telnyx.com/v2/texml/calls/{connection_id} \
    --data-urlencode "To=+13121230000" \
    --data-urlencode "From=+13120001234" \
    --data-urlencode "Url=https://www.example.com/texml.xml?PhoneNumbers[]=+18771234567&PhoneNumbers[]=+18771234568" \
    --data-urlencode "StatusCallback=https://www.example.com/statuscallback-listener" \
    --header "Authorization: Bearer YOUR_API_KEY"
```

Then you can handle the `PhoneNumbers` parameter in the TeXML instructions using the following syntax:

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    {{#PhoneNumbers}}
       {{.}}    
    {{/PhoneNumbers}}

```

This will end up being parsed as:

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    +18771234567
    +18771234568

```

### How to render conditional content

Conditional content is supported by using `if/else` statements in the TeXML instructions. You could define a set of instructions to dial an specific number depending on `From` parameter present in the HTTP request.

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

{{#if {{From}} == +18771234567}}

    +18771234568

{{#elseif {{From}} == +18771234568}}

    +18771234567

{{#else}}
  No valid number is present
{{/if}}

```

Note that supported operators are `==`, `!=` and there is no operator for checking if the parameter value is not null.


## Related Pages

- [TeXML Fundamentals](../runbooks/texml-fundamentals.md)
