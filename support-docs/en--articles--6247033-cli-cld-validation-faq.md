---
source_url: https://support.telnyx.com/en/articles/6247033-cli-cld-validation-faq
title: "CLI & CLD Validation FAQ"
description: "Dive into Telnyx's enhanced CLI & CLD validation mechanism. See Telnyx guidance and requirements Learn more about CLI & CLD Validation FAQ with Telnyx."
scraped: 2026-07-08
content_hash: c7fce9b2209c747579a641dd48273b660e4883e177f636661b5ff89676b29192
---







# CLI & CLD Validation FAQ

Dive into Telnyx's enhanced CLI & CLD validation mechanism. See Telnyx guidance and requirements Learn more about CLI & CLD Validation FAQ with Telnyx.




## **CLI & CLD Validation Frequently Asked Questions**

On June 6th, 2022. Telnyx enhanced its existing validation mechanism by adding checks to North American National Numbering databases for CLI and CLD.

## **What are CLI and CLD?**

Calling Line Identity (CLI) refers to the number the call came from and Calling Line Destination (CLD) refers to the number that was dialed.

## What does a valid number format look like?

The International Telecommunications Union (ITU) assigned country code "1" to the NANP area. The NANP conforms with ITU Recommendation E.164, the international standard for telephone numbering plans.

NANP numbers are ten-digit numbers consisting of a three-digit Numbering Plan Area (NPA) code, commonly called an area code, followed by a seven-digit local number. The format is usually represented as:

```
NXX-NXX-XXXX
```

where N is any digit from 2 through 9 and X is any digit from 0 through 9.

## What are CLI and CLD Validation?

If a CLI or CLD is in an invalid format or does not appear in the North American National Numbering databases, calls from that number will be rejected.

## **Are CLI and CLD Validation applied to all my calls?**

CLI and CLD Validation will be applied to all outbound calls between NANPA (Number American Numbering Plan Administration) numbers, except Toll-Free Numbers, from June 6th, 2022.

## **Are calls to international destinations subject to CLI and CLD validation?**

CLI and CLD validation are subject to outbound calls from Telnyx customers to the PSTN, between CLI and CLD from North American Numbering Plan geographies. These comprise the United States and its territories, Canada, Bermuda, Anguilla, Antigua & Barbuda, the Bahamas, Barbados, the British Virgin Islands, the Cayman Islands, Dominica, the Dominican Republic, Grenada, Jamaica, Montserrat, Sint Maarten, St. Kitts and Nevis, St. Lucia, St. Vincent and the Grenadines, Trinidad and Tobago, and Turks & Caicos.

## **Can I disable CLI and CLD validation?**

Since CLI and CLD validation is enabled at the service level, it will affect all customers and customers will not be able to turn off this validation.

## **How will I know if my calls are being blocked?**

If **CLI validation fails**, calls from that number will be rejected with a specific code:

* **SIP 403** “*The origination number does not have a subscriber assigned. The number is invalid.*”

If **CLD validation fails**, calls from that number will be rejected with a specific code:

* **SIP 404** “*The destination number does not have a subscriber assigned. The number is invalid.*”

Telnyx users can check this information in the Mission Control Portal through the *[debugging tools](https://support.telnyx.com/en/articles/4304872-telnyx-debugging-tools)*.

## **Is there a way to check if my calls will be blocked prior to calling?**

Telnyx Users can verify if numbers are CLI and CLD validated using the *[Number Lookup](https://support.telnyx.com/en/articles/4366901-your-number-lookup-guide) tool in the portal*.

**Is CLI validation applicable to Telnyx numbers only?**

CLI validation will be applicable to all numbers used to perform outbound calls through the Telnyx network, regardless of the number provider.

## **What should I do if my call is blocked, even if my CLI or CLD are valid?**

If there is a case where your call has been blocked by CLI and CLD validation, and the CLI and CLD are valid, please [report to our support team](https://support.telnyx.com/en/articles/5170721-best-practices-for-contacting-support).

---

Related Articles

[Caller ID Number Policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy)[Oracle: Acme Packet SBC Setup](https://support.telnyx.com/en/articles/4194697-oracle-acme-packet-sbc-setup)[Telnyx SIP Response Codes](https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes)[Verified Numbers FAQ](https://support.telnyx.com/en/articles/6790265-verified-numbers-faq)[HD Voice - Number Feature](https://support.telnyx.com/en/articles/8394071-hd-voice-number-feature)

Did this answer your question?

😞😐😃
