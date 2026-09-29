---
source_url: https://support.telnyx.com/en/articles/8268276-loa-template-download
title: "LOA Template Download"
description: "Learn how to create a PDF in Node.js for Telnyx Porting LOA API. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 07656135d28742732ad8c3c7aa28cd96f7c41c9b0c92c16afe7e60677329c4d7
---







# LOA Template Download

Learn how to create a PDF in Node.js for Telnyx Porting LOA API. See Telnyx guidance and requirements.

K




## How to Create a PDF in Node.js for Telnyx Porting LOA API

If you need to use the Telnyx API capabilities for porting then you will need to be able to download LOA Template PDFs. Here is an example of a request you can send you may start working on functionality for Porting numbers by API. A step you may run into

![PDF made with Node example](_images/7244d3c03cadaff2.png)

```
'use strict' const Fs = require('fs') const Path = require('path') const Axios = require('axios') async function downloadPDF () { const url = 'https://api.telnyx.com/v2/porting_orders/{porting_id}/loa_template' const path = Path.resolve(__dirname, `test.pdf`) const writer = Fs.createWriteStream(path) const response = await Axios({ url, method: 'GET', responseType: 'stream', headers: { "Content-Type": "application/json", Accept: "application/json", Authorization:"Bearer API_KEY", } }) // console.log(response.data); response.data.pipe(writer) return new Promise((resolve, reject) => { writer.on('finish', resolve) writer.on('error', reject) }) } downloadPDF()
```
