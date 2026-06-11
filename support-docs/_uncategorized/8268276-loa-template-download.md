---
source_url: https://support.telnyx.com/en/articles/8268276-loa-template-download
scraped: 2026-06-11
---

LOA Template Download | Telnyx Help Center

[Skip to main content](#main-content)

# LOA Template Download

Learn how to create a PDF in Node.js for Telnyx Porting LOA API. Download the LOA Template PDFs using the Telnyx API for porting numbers.

K

Written by Klane Pedrie

February 1, 2024

Table of contents

# How to Create a PDF in Node.js for Telnyx Porting LOA API

If you need to use the Telnyx API capabilities for porting then you will need to be able to download LOA Template PDFs. Here is an example of a request you can send you may start working on functionality for Porting numbers by API. A step you may run into

[![PDF made with Node example](https://downloads.intercomcdn.com/i/o/809997952/7c93c96bbcc72ba498f0b5d3/Screenshot+2023-08-17+at+1.13.23+PM.png?expires=1781168400&signature=9b0208146e90b1b106eb615c8b1a00a375112d623131be99fbbe60f40e6ad7a4&req=fCAuH8B5lIRdFb4f3HP0gEtl%2F%2FgIo1EJIIg6pMQcQfv1DOWZ2SR2nSxHj50y%0AigE8b%2BRA1HWZUqaudw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/809997952/7c93c96bbcc72ba498f0b5d3/Screenshot+2023-08-17+at+1.13.23+PM.png?expires=1781168400&signature=9b0208146e90b1b106eb615c8b1a00a375112d623131be99fbbe60f40e6ad7a4&req=fCAuH8B5lIRdFb4f3HP0gEtl%2F%2FgIo1EJIIg6pMQcQfv1DOWZ2SR2nSxHj50y%0AigE8b%2BRA1HWZUqaudw%3D%3D%0A)

```
'use strict' const Fs = require('fs') const Path = require('path') const Axios = require('axios') async function downloadPDF () { const url = 'https://api.telnyx.com/v2/porting_orders/{porting_id}/loa_template' const path = Path.resolve(__dirname, `test.pdf`) const writer = Fs.createWriteStream(path) const response = await Axios({ url, method: 'GET', responseType: 'stream', headers: { "Content-Type": "application/json", Accept: "application/json", Authorization:"Bearer API_KEY", } }) // console.log(response.data); response.data.pipe(writer) return new Promise((resolve, reject) => { writer.on('finish', resolve) writer.on('error', reject) }) } downloadPDF()
```

---

Related Articles

[3CX: Configuring a 3CX V20 PBX 20.0 Update 5 (Build 20.0.5.551) (March 2025 Update)](https://support.telnyx.com/en/articles/8683996-3cx-configuring-a-3cx-v20-pbx-20-0-update-5-build-20-0-5-551-march-2025-update)

Did this answer your question?

😞😐😃

Table of contents
