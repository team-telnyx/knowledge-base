---
title: Porting and SMS Guidelines Reference
summary: A consolidated reference covering Telnyx porting requirements, how to fill
  out and auto-generate a Letter of Authorization (LOA), El Salvador-specific porting
  and DID requirements, and SMS guidelines for a range of countries including Andorra,
  El Salvador, Dominican Republic, Macao, Saint Pierre and Miquelon, Sao Tome and
  Principe, Trinidad & Tobago, Turks and Caicos Islands, and South Korea.
sources:
- url: https://support.telnyx.com/en/articles/2034326-how-to-fill-out-an-loa
- url: https://support.telnyx.com/en/articles/5179083-el-salvador-number-porting
- url: https://support.telnyx.com/en/articles/5464176-el-salvador-did-requirements
- url: https://support.telnyx.com/en/articles/6460777-porting-requirements
- url: https://support.telnyx.com/en/articles/6563890-andorra-sms-guidelines
- url: https://support.telnyx.com/en/articles/6574078-el-salvador-sms-guidelines
- url: https://support.telnyx.com/en/articles/6665730-dominican-republic-sms-guidelines
- url: https://support.telnyx.com/en/articles/6675024-macao-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679441-saint-pierre-and-miquelon-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680003-sao-tome-and-principe-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683379-trinidad-tobago-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683396-turks-and-caicos-islands-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683734-korea-sms-guidelines
- url: https://support.telnyx.com/en/articles/8268276-loa-template-download
- url: https://support.telnyx.com/en/articles/8588086-auto-generated-letter-of-authorization-loa
updated_at: 2026-08-05T13:34:48Z
---

# Porting and SMS Guidelines Reference

*Part 2 of 3 — see also: [Part 1](porting-and-sms-guidelines-reference--part-1.md), [Part 3](porting-and-sms-guidelines-reference--part-3.md)*

A consolidated reference covering Telnyx porting requirements, how to fill out and auto-generate a Letter of Authorization (LOA), El Salvador-specific porting and DID requirements, and SMS guidelines for a range of countries including Andorra, El Salvador, Dominican Republic, Macao, Saint Pierre and Miquelon, Sao Tome and Principe, Trinidad & Tobago, Turks and Caicos Islands, and South Korea.

## Auto-Generated Letter of Authorization (LOA)

On select port orders, Telnyx provides users with the ability to auto-generate a Letter of Authorization (LOA). This LOA is pre-populated with the same information entered on the porting order form. These LOAs can be custom branded with your own company logos and information, and the LOA can be easily shared with the authorized user to sign.

### Eligibility

This feature is currently only available for ports that meet the following criteria:

- Port orders with `US` `local` phone numbers
- Port orders with `CA` `local` phone numbers

### How to Use Auto-Generate LOA and Share LOA

1. Go to the `Port Numbers` page and click on `New Port Request`.
2. Run the portability check on your phone numbers. Hit `Next` to create a port order.
3. Fill in the `Order Details` page. Hit `Next`.
4. On the `Additional Requirements` page, there will be two buttons: `Auto-generate LOA` and `Share LOA`.

![Port Request section.](_images/6aacdb027b6e383d.png)

### Auto-Generate LOA

When you click the `Auto-generate LOA` button, a modal will pop up:

![Auto-generate LOA template.](_images/688c5f98fc3b085a.png)

The left side of the modal includes all of the interactive components:

1. **LOA Template:** If you have multiple branded templates, you can select which one to apply.
2. **Print Name:** The printed name of the authorized user signing the LOA.
3. **Date:** The date that the LOA is signed.
4. **Draw Signature:** The user can draw their signature in the box, which is then transferred to the LOA.

There are three buttons:

1. **Modify:** Saves the changes you made in the inputs. Useful for previewing changes before further action.
2. **Download:** Downloads the LOA to your local computer. Any input changes are included even if you forget to hit **Modify**.
3. **Submit:** Attaches the LOA to the porting order. Any input changes are included even if you forget to hit **Modify**.

The right side of the modal shows a preview of the auto-generated LOA so you can verify it is filled out correctly before downloading or attaching it.

### Share LOA

Even though you are creating the porting order, you may not be the individual authorized to sign the LOA. Use the `Share LOA` button to generate a link to share with the authorized user. The authorized user can visit that link to easily sign and attach the LOA to the port order.

To use this feature:

1. Click the `Share LOA` button.
2. A modal will pop up. Copy the link and send it to the authorized user.

![LOA shareable link page.](_images/00a03ca907f3c786.png)

3. Save the port order into a "draft" status by clicking the `Save and Close` button.
4. The authorized user signs the LOA and attaches it to the port order.
5. Return to the port order, edit it, and finish submitting it.

Notes on this feature:

- You cannot submit your porting order until an LOA has been attached. Use `Save and Close` to save your port order as a "draft" while you wait.
- The link expires after 48 hours. If it expires, generate a new link or upload a signed LOA manually.
- The authorized user does not need a Telnyx Portal account. As long as they have the link and it has not expired, they can sign and submit the LOA.

Email notifications are sent for key LOA events:

- Once the authorized user signs and attaches the LOA, the Telnyx user is emailed so they can revisit the draft port order and finish submitting it.
- If the link expires before an LOA is attached, the Telnyx user is emailed so they can decide whether to upload an LOA manually or generate a new link.

### Customizing LOAs with Your Own Branding

By default, the auto-generated LOA is branded with Telnyx's logo and company information. You can customize the auto-generated LOAs to reflect your own company's branding and information.

Visit the [Customize LOA page](https://portal.telnyx.com/#/numbers/port-numbers/customize-loa) in the portal and click `New LOA Template` in the top right.

![New LOA template creation page.](_images/1f93e158e4917714.png)

Fill out the form with your own company name, email address, phone number, and physical address. There are three buttons:

1. **Cancel:** LOA template is not created, and you are brought back to the previous page.
2. **Preview:** Before saving the template, you can preview what the LOA will look like. The preview appears on the right side of the page.

![Customizable LOA.](_images/c7ecb95f9fc28410.png)

3. **Save:** Saves the template.

Once the template is saved, it is automatically applied to your auto-generated LOAs, replacing the Telnyx-branded LOA template. You can create one or more templates. If you have multiple templates, the most recently created template is used by default. Once the LOA has been generated, you may change the LOA template by using the `LOA Template` dropdown in the modal.

![LOA template.](_images/864952ab5a25cb5c.png)

## LOA Template Download via API

If you need to use the Telnyx API capabilities for porting, you will need to be able to download LOA Template PDFs. The following Node.js example shows how to download an LOA template PDF for a given porting order.

![PDF made with Node example](_images/7244d3c03cadaff2.png)

```javascript
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

## El Salvador Number Porting

For local/national number types in El Salvador, the following documents are required:

1. Valid LOA (local address required)
2. Copy of identification (DUI) or passport of the authorized person
3. Copy of the latest invoice with a local carrier
4. Proof of payment of the latest invoice with the local carrier
5. Company registration certificate (only if the numbers belong to a company)
6. Power of Attorney (only if the numbers belong to a company)

Contact [porting@telnyx.com](mailto:porting@telnyx.com) for the LOA template for number porting in El Salvador.

### Submission Process and Tips

When submitting the required documents, ensure that all copies are clear and legible. Digital submissions should be in high-resolution formats, preferably PDF or JPEG. Always double-check the completeness of your documents before submission to avoid delays.

If submitting physically, keep a personal copy of all documents for your records. For digital submissions, ensure you receive a confirmation of receipt from the relevant department or platform.
