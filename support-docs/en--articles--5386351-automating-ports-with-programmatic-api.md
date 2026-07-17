---
source_url: https://support.telnyx.com/en/articles/5386351-automating-ports-with-programmatic-api
title: "Automating Ports With Programmatic API"
description: "Revolutionize your porting process using the Documents API. See Telnyx guidance and requirements Learn more about Automating Ports With Programmatic API with."
scraped: 2026-07-08
content_hash: d151b6891dd692d9401e4db6cde2648c6efc9ee177226cf34e95a4439e55244c
---







# Automating Ports With Programmatic API

Revolutionize your porting process using the Documents API. See Telnyx guidance and requirements Learn more about Automating Ports With Programmatic API with.




While Telnyx has always supported the purchasing and porting of numbers through the Telnyx Portal, we have recently introduced new tools to assist with automating this process through our API. You can now [programmatically manage document uploads](https://developers.telnyx.com/api/documents/list-document-links) to completely remove the manual intervention required for porting new numbers. This is particularly useful if you have built custom tools that allow your customers to port numbers through our API.

​

## Programmatic Number Porting

In order to validate your port-in, Telnyx requires you to provide a [letter of agency/authorization](https://support.telnyx.com/en/articles/2034326-how-to-fill-out-an-loa) and an invoice from your current provider. Through the Documents API, this process no longer requires the manual management of documents from the Portal.

To begin porting a number, you first need to [run a portability check](https://developers.telnyx.com/api/porting/portability-check/post-portability-check). If the portability check is successful, you can [initiate a porting order](https://developers.telnyx.com/api/porting/porting-order/list-porting-orders) from our v2/porting\_orders endpoint.

## Enhancing Porting with the Documents API

Previously, without the Documents API, you would have needed to manually upload the supporting documents through the Portal, but you can now [upload a new document](https://developers.telnyx.com/api/documents/list-document-links) using our endpoint, which will return a UUID.

Now, you can simply [update the porting order](https://developers.telnyx.com/api/porting/porting-order/list-porting-orders) to provide the relevant document UUID in the "documents" parameter. In the same request, you can supply the "end\_user" information, "activation\_settings" (FOC date), and "phone\_number\_configuration" settings. Finally, you must [confirm the porting order](https://developers.telnyx.com/api/porting/porting-order/list-porting-orders).

You may also choose to configure webhooks to manage your notifications regarding your port-ins. For an overview of this process, please see [our Quickstart guide](https://developers.telnyx.com/docs/numbers/porting/quickstart).

​
​

​
​

---

Related Articles

[International Number Porting - Required Documents](https://support.telnyx.com/en/articles/1130626-international-number-porting-required-documents)[Port numbers to Telnyx](https://support.telnyx.com/en/articles/1130634-port-numbers-to-telnyx)[Port Request Statuses](https://support.telnyx.com/en/articles/3284588-port-request-statuses)[Porting + Bundles](https://support.telnyx.com/en/articles/8709331-porting-bundles)[Porting away from Skype](https://support.telnyx.com/en/articles/10715399-porting-away-from-skype)

Did this answer your question?

😞😐😃
