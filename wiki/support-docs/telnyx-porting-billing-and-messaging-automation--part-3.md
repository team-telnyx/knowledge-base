---
title: Telnyx Porting, Billing, and Messaging Automation
summary: This page consolidates Telnyx support documentation covering number porting
  (CSRs, LOAs, automated validation, porting requirements, and the auto-generated
  LOA feature), billing models (per-minute billing increments and channel billing
  with zone-based pricing), CLI/CLD validation for North American calls, and Zapier-based
  SMS automations including forwarding texts to mobile or email, automated replies,
  and the Textable integration.
sources:
- url: https://support.telnyx.com/en/articles/1130614-obtaining-a-csr-from-your-carrier
- url: https://support.telnyx.com/en/articles/1130659-billing-increments
- url: https://support.telnyx.com/en/articles/1130678-channel-billing-and-how-to-use-it
- url: https://support.telnyx.com/en/articles/1516776-automated-port-request-validation
- url: https://support.telnyx.com/en/articles/2034326-how-to-fill-out-an-loa
- url: https://support.telnyx.com/en/articles/3231942-forwarding-sms-to-your-mobile-number
- url: https://support.telnyx.com/en/articles/3232529-automated-replies-for-messages-using-zapier
- url: https://support.telnyx.com/en/articles/3685327-textable-setup-guide
- url: https://support.telnyx.com/en/articles/3723768-zapier-forward-texts-to-email
- url: https://support.telnyx.com/en/articles/6247033-cli-cld-validation-faq
- url: https://support.telnyx.com/en/articles/6460777-porting-requirements
- url: https://support.telnyx.com/en/articles/8268276-loa-template-download
- url: https://support.telnyx.com/en/articles/8428806-channel-billing
- url: https://support.telnyx.com/en/articles/8588086-auto-generated-letter-of-authorization-loa
updated_at: 2026-07-17T09:02:58Z
---

# Telnyx Porting, Billing, and Messaging Automation

*Part 3 of 7 — see also: [Part 1](telnyx-porting-billing-and-messaging-automation--part-1.md), [Part 2](telnyx-porting-billing-and-messaging-automation--part-2.md), [Part 4](telnyx-porting-billing-and-messaging-automation--part-4.md), [Part 5](telnyx-porting-billing-and-messaging-automation--part-5.md), [Part 6](telnyx-porting-billing-and-messaging-automation--part-6.md), [Part 7](telnyx-porting-billing-and-messaging-automation--part-7.md)*

This page consolidates Telnyx support documentation covering number porting (CSRs, LOAs, automated validation, porting requirements, and the auto-generated LOA feature), billing models (per-minute billing increments and channel billing with zone-based pricing), CLI/CLD validation for North American calls, and Zapier-based SMS automations including forwarding texts to mobile or email, automated replies, and the Textable integration.

## LOA Template Download (API)

If you need to use the Telnyx API capabilities for porting, you will need to be able to download LOA Template PDFs. The following Node.js example shows how to download an LOA template PDF for a given porting order:

![PDF made with Node example](_images/7244d3c03cadaff2.png)

```
'use strict'
const Fs = require('fs')
const Path = require('path')
const Axios = require('axios')

async function downloadPDF () {
  const url = 'https://api.telnyx.com/v2/porting_orders/{porting_id}/loa_template'
  const path = Path.resolve(__dirname, `test.pdf`)
  const writer = Fs.createWriteStream(path)
  const response = await Axios({
    url,
    method: 'GET',
    responseType: 'stream',
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
      Authorization:"Bearer API_KEY",
    }
  })
  // console.log(response.data);
  response.data.pipe(writer)
  return new Promise((resolve, reject) => {
    writer.on('finish', resolve)
    writer.on('error', reject)
  })
}

downloadPDF()
```

## Billing Increments

A billing increment is how Telnyx calculates billing for each call of unique duration. Telnyx uses 60/60 billing increments: if your call is 11 seconds long, you will be charged for 60 seconds. If your call is 96 seconds long, you'll be charged for 120 seconds (2 × 60 seconds).

International calling is billed in 60-second increments in most cases but can vary for calls to certain locations. For a full breakdown of billing increments by country, you can download your international rates from within the [Mission Control Portal](https://portal.telnyx.com/#/app/pricing).

**Note:** Telnyx no longer offers 6-second billing increments.
