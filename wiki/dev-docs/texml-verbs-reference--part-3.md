---
title: TeXML Verbs Reference
summary: A consolidated reference for the TeXML verbs available in Telnyx Programmable
  Voice, covering call control, media playback, recording, transcription, conferencing,
  payments, and SIPREC. Each verb section lists attributes, child nouns, examples,
  and the callbacks that the platform emits.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/gather
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/hangup/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/httprequest
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/leave
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/pause
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/pay
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/play
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/record
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/recording
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/redirect
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/refer
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/reject
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/say
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/siprec
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/start
updated_at: 2026-08-05T14:05:15Z
---

# TeXML Verbs Reference

*Part 3 of 7 — see also: [Part 1](texml-verbs-reference--part-1.md), [Part 2](texml-verbs-reference--part-2.md), [Part 4](texml-verbs-reference--part-4.md), [Part 5](texml-verbs-reference--part-5.md), [Part 6](texml-verbs-reference--part-6.md), [Part 7](texml-verbs-reference--part-7.md)*

A consolidated reference for the TeXML verbs available in Telnyx Programmable Voice, covering call control, media playback, recording, transcription, conferencing, payments, and SIPREC. Each verb section lists attributes, child nouns, examples, and the callbacks that the platform emits.

## Pay

The `<Pay>` verb collects payment information from a caller using DTMF and either charges or tokenizes the payment method through a configured Pay connector. Connectors may run in test or live mode. Test-mode connectors accept only the documented test card numbers.

### Attributes

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `action` | Optional URL where TeXML requests the next set of instructions after `<Pay>` completes. The request includes normalized `PayResult`, the raw `Result`, and available payment result fields. | — | — |
| `method` | HTTP request type used for the `action` URL. | `GET`, `POST` | `POST` |
| `statusCallback` | Optional URL where Telnyx will send status callbacks for payment progress and completion events. | — | — |
| `statusCallbackMethod` | HTTP request type used for `statusCallback`. | `GET`, `POST` | `POST` |
| `paymentConnector` | The name of the payment connector to use. The connector must be configured in the Telnyx API. | — | `Default` |
| `chargeAmount` | The amount to charge (e.g. `10.50`). Required when `transactionType` is `charge`. Ignored for `tokenize` transactions. | — | — |
| `currency` | The currency for the charge. Pay currently supports `USD`. | `USD` | `USD` |
| `paymentToken` | An existing payment token to use for the transaction. If provided, the payment data collection steps are skipped. | — | — |
| `paymentMethod` | The payment method to collect. `credit-card` collects card number, expiration date, postal code, and security code. `ach-debit` collects bank routing and account numbers. | `credit-card`, `ach-debit` | `credit-card` |
| `transactionType` | The transaction type. `charge` processes a payment and returns a `ChargeId`. `tokenize` tokenizes the payment data and returns a `TokenId`. If omitted, Pay infers `tokenize` when `chargeAmount` is absent or zero and `charge` when it is positive. | `charge`, `tokenize` | — |
| `description` | An optional description for the payment transaction. | — | — |
| `maxAttempts` | The maximum number of attempts for each payment collection step before failing. | `1`–`3` | `1` |
| `timeout` | The timeout in seconds for each DTMF input step. | `1`–`600` | `5` |
| `interDigitTimeout` | The timeout in seconds between consecutive DTMF digits during input. | `1`–`600` | `5` |
| `voice` | The voice used for payment prompts (e.g. `female`, `male`). | — | `female` |
| `language` | The language used for payment prompts (e.g. `en-US`, `es-ES`). | — | `en-US` |
| `serviceLevel` | The service level for payment processing. | `premium` | `premium` |
| `parameters` | A JSON string of additional parameters to pass to the payment connector. | — | — |
| `prompts` | A JSON string of custom prompts for payment collection steps. Can also be specified using nested `<Prompt>` elements. | — | — |
| `metadata` | A JSON string of metadata to attach to the payment transaction. | — | — |

### Child verbs/nouns

- `Parameter` — optional key-value parameter merged into the Pay parameters map. Use the `name` and `value` attributes to specify the key and value.
- `Prompt` — custom text-to-speech prompt for a specific payment collection step. Use the `for` attribute to specify the step and include the prompt text in a nested `<Say>` element.

### Connector modes and test cards

Pay connectors can operate in `test` or `live` mode. Before contacting the configured processor, a test-mode connector rejects every card number except those below.

| Card type | Card number | Security code | Expiration date |
| --- | --- | --- | --- |
| Visa | `4111 1111 1111 1111` | Any 3 or 4 digits | Any four digits in `MMYY` format |
| Mastercard | `5555 5555 5555 4444` | Any 3 or 4 digits | Any four digits in `MMYY` format |
| American Express | `3782 822463 10005` | Any 3 or 4 digits | Any four digits in `MMYY` format |
| Discover | `6011 1111 1111 1117` | Any 3 or 4 digits | Any four digits in `MMYY` format |
| Diners Club | `3065 9300 0902 0004` | Any 3 or 4 digits | Any four digits in `MMYY` format |
| JCB | `3566 0020 2036 0505` | Any 3 or 4 digits | Any four digits in `MMYY` format |
| UnionPay | `6200 0000 0000 0005` | Any 3 or 4 digits | Any four digits in `MMYY` format |
| Maestro | `6771 7980 2100 0008` | Any 3 or 4 digits | Any four digits in `MMYY` format |

A test-mode payment using any other card number fails with `ErrorType=invalid-card-number`. Live-mode connectors pass the captured payment details to the configured payment processor.

### Charge a credit card

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Pay paymentConnector="MyConnector"
         chargeAmount="10.50"
         currency="USD"
         transactionType="charge"
         action="https://example.com/payment-complete"
         statusCallback="https://example.com/pay-status" />
</Response>
```

### Tokenize a credit card

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Pay paymentConnector="MyConnector"
         transactionType="tokenize"
         action="https://example.com/payment-complete"
         statusCallback="https://example.com/pay-status" />
</Response>
```

If `transactionType` is omitted, Pay infers `tokenize` when `chargeAmount` is absent or zero and `charge` when `chargeAmount` is positive.

### Collect ACH bank-account details

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Pay paymentConnector="MyConnector"
         paymentMethod="ach-debit"
         transactionType="charge"
         chargeAmount="25.00"
         currency="USD"
         action="https://example.com/payment-complete"
         statusCallback="https://example.com/pay-status" />
</Response>
```

### Custom prompts

Override a payment step's text-to-speech prompt with a nested `<Prompt>` and `<Say>`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Pay paymentConnector="MyConnector"
         transactionType="charge"
         chargeAmount="10.50"
         action="https://example.com/payment-complete">
        <Prompt for="payment-card-number">
            <Say>Please enter your credit card number.</Say>
        </Prompt>
        <Prompt for="security-code">
            <Say>Please enter the security code from your card.</Say>
        </Prompt>
    </Pay>
</Response>
```

The supported `for` values are `payment-card-number`, `expiration-date`, `postal-code`, `security-code`, `bank-routing-number`, and `bank-account-number`. Prompts may be qualified by `attempt`, `errorType`, and `cardType`. Qualifiers are optional and may be combined. `attempt` accepts a space-separated list of 1-based attempt numbers. Card-type values are lowercase and case-sensitive.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Pay paymentConnector="MyConnector"
         transactionType="charge"
         chargeAmount="10.50"
         maxAttempts="3">
        <Prompt for="security-code" cardType="amex">
            <Say>Please enter the 4-digit security code from the front of your card.</Say>
        </Prompt>
        <Prompt for="security-code">
            <Say>Please enter the security code from your card.</Say>
        </Prompt>
        <Prompt for="payment-card-number" attempt="2 3" errorType="invalid-card-number">
            <Say>That card number was not accepted. Please try again.</Say>
        </Prompt>
    </Pay>
</Response>
```

The `prompts` JSON attribute is an alternative to nested `<Prompt>` elements. Each step may contain a string or a list of prompt objects:

```xml
<Response>
    <Pay paymentConnector="MyConnector"
         transactionType="tokenize"
         prompts='{"payment-card-number":[{"text":"Enter your card number."},{"text":"Please try again.","attempt":"2 3"}]}' />
</Response>
```

### Additional connector parameters

Pass extra string parameters with nested `<Parameter>` elements. Child parameters override keys with the same name in the `parameters` JSON attribute.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Pay paymentConnector="MyConnector"
         transactionType="charge"
         chargeAmount="10.50"
         parameters='{"source":"phone"}'>
        <Parameter name="order_id" value="ORD-12345" />
        <Parameter name="customer_id" value="CUST-67890" />
    </Pay>
</Response>
```

### Status callbacks

When `statusCallback` is set, TeXML sends callbacks as payment collection progresses and another callback when the Pay session completes. Parameters are form encoded for `POST` callbacks and query encoded for `GET` callbacks. The following call and payment context fields are included when available:

| Parameter | Description |
| --- | --- |
| `AccountSid` | ID of the Telnyx account that owns the call. |
| `CallSid` | Call Control ID of the call leg running Pay. |
| `CallSidLegacy` | The same Call Control ID, provided for compatibility. |
| `CallSessionId` | ID shared by call legs in the same call session. |
| `ConnectionId` | ID of the Call Control or TeXML connection. |
| `PaymentMethod` | Payment method: `credit-card` or `ach-debit`. |
| `PaymentConnector` | Name of the Pay connector used for the transaction. |
| `For` | Current collection step, such as `payment-card-number`, `expiration-date`, `postal-code`, `security-code`, `bank-routing-number`, `bank-account-number`, or `payment-processing`. |

#### Progress callback

A progress callback always contains `Status=processing` and `Result=pending`. It can also contain:

| Parameter | Description |
| --- | --- |
| `Attempt` | Current 1-based attempt number for the step. |
| `ErrorType` | Step-level error, such as `timeout`, `invalid-card-number`, `invalid-date`, `invalid-security-code`, `invalid-postal-code`, `invalid-bank-routing-number`, or `invalid-bank-account-number`. Omitted when the step succeeds. |
| `PaymentError` | Processor-level error description, when available. |

Progress callbacks accumulate the masked payment data collected so far. For example, the expiration-date callback can include the card number and card type collected by an earlier step.

#### Completed callback

The final status callback contains `Status=completed` and a normalized `Result` of `success` or `failed`. It can also contain:

| Parameter | Description |
| --- | --- |
| `ChargeId` | Charge identifier returned for a successful `charge` transaction. |
| `TokenId` | Token identifier returned for a successful `tokenize` transaction. |
| `ErrorType` | Step-level error that caused the Pay session to fail, when available. |
| `PaymentError` | Processor-level error description, when available. |
| `PayErrorCode` | Error code returned by the payment connector or processor, when available. |
| `Attempt` | Last reported attempt number, when available. |

#### Masked payment-data fields

Progress and completed callbacks include these fields when the corresponding values have been collected:

| Parameter | Description |
| --- | --- |
| `PaymentCardNumber` | Masked card number with only the last four digits visible. |
| `PaymentCardType` | Detected lowercase card type, such as `visa`, `mastercard`, `amex`, `discover`, `diners-club`, or `jcb`. |
| `ExpirationDate` | Expiration date in `MMYY` format. |
| `SecurityCode` | Fully masked security code. |
| `PaymentCardPostalCode` | Billing postal code. |
| `BankAccountNumber` | Masked bank account number with only the last two digits visible. |
| `BankRoutingNumber` | Bank routing number. |
| `BankAccountType` | Bank account type when supplied by the processor. |

### Action request

After Pay completes, TeXML requests the `action` URL using `method`. If `action` is omitted, TeXML requests the current document URL instead. The response must contain the next TeXML instructions. The action request has its own payload shape; it is not identical to the completed `statusCallback` payload.

| Parameter | Description |
| --- | --- |
| `PayResult` | Normalized result: `success` or `failed`. |
| `Result` | Raw Pay result, such as `success`, `validation-error`, `payment-connector-error`, `internal-error`, `too-many-failed-attempts`, or `cancelled`. |
| `CallSessionId` | Call session ID, when available. |
| `PaymentMethod` | Payment method: `credit-card` or `ach-debit`. |
| `PaymentConnector` | Name of the Pay connector used. |
| `PaymentStep` | Last payment step, when available. |
| `ErrorCode` | Step-level error from the Pay result, when available. |
| `PaymentError` | Processor-level error description, when available. |
| `PayErrorCode` | Connector or processor error code, when available. |
| `ChargeId` | Charge identifier for a successful `charge` transaction. |
| `PaymentConfirmationCode` | Alias of `ChargeId`. |
| `TokenId` | Token identifier for a successful `tokenize` transaction. |
| `PaymentToken` | Alias of `TokenId`. |

The action request also includes any available masked payment-data fields listed above.
