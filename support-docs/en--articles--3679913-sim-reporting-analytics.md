---
source_url: https://support.telnyx.com/en/articles/3679913-sim-reporting-analytics
title: "SIM Reporting & Analytics"
description: "In this article we will explain where to find your WDRs in the Telnyx Mission Control Portal and API. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 9a5dd42bc9de2e69d23acbfb61d587ef2a6a1526acc30c29893ea0bdc74e8736
---







# SIM Reporting & Analytics

In this article we will explain where to find your WDRs in the Telnyx Mission Control Portal and API. See Telnyx guidance and requirements.




## How to Pull Your WDR CSV Report

Pull reports on WDRs from the Reporting section of the Portal - just like you would with MDRs (for messaging) or CDRs (for voice). WDR stands for wireless detail record and represents a single data session from your SIM card.

Report can be downloaded as a CSV and will include the following:

|  |  |
| --- | --- |
| Record Opening Time (UTC) | The time the related session was opened. |
| Telephone Number | Telephone number tied to your Telnyx SIM card. |
| Downlink Data (MB) | Amount of data downloaded in the related session. |
| Uplink Data (MB) | Amount of data uploaded in the related session. |
| SIM Card ID | UUID for SIM card resource. |
| SIM Group ID | UUID for SIM group resource. |
| Data Plan ID | UUID for the related data plan resource. Data plans are only used for specific customer use cases. |
| Mobile Country Code (MCC) | A unique code to check which country the SIM was being used. |
| Mobile Network Code (MNC) | A unique code to check which carrier your SIM was connected to. |
| International Mobile Subscriber Identity ([IMSI](https://telnyx.com/resources/imsi-switching)) | Used to identify the user on the network similar to a MAC address. |
| Sim Card Tags | A comma-separated list of associated tags. |

Head to the Reporting tab in Mission Control:

## How to Pull Your WDR JSON Analytics

You can also track your data usage analytics via our JSON API. The below cURL command will give you back a paginated response from our RESTful API with a single record per WDR:

```
curl --request GET \
  --url https://api.telnyx.com/v2/wireless/detail/records/reports/{id} \
  --header 'Authorization: Bearer <token>'
```

This command will respond with all session information from yesterday for your active SIM cards.

API specifications for this JSON endpoint can be viewed [here](https://developers.telnyx.com/api-reference/reporting/get-a-wireless-detail-record-wdr-report).

The response will include the following fields:

|  |  |
| --- | --- |
| closed\_at | Datetime in which the related session was closed. |
| created\_at | Datetime in which the related session was started. |
| currency | Billing currency. |
| data\_cost | The total cost of the data ran in this session. |
| data\_rate | The unit price for each MB ran in this session. |
| data\_unit | The unit of measurement for units in this session - nearly always MB. |
| downlink\_data | Amount of data downloaded in the related session. |
| id | UUID for this specific session. |
| imsi | Used to identify the user on the network similar to a MAC address. |
| ip\_address | The IP address that the SIM card had when this session was active. |
| is\_telnyx\_billable | Always true. |
| mcc | A unique code to check which country the SIM was being used. |
| mnc | A unique code to check which carrier your SIM was connected to. |
| phone\_number | Telephone number tied to your Telnyx SIM card. |
| record\_type | The type of API resource that this is - it will always be wireless\_detail\_record |
| sim\_card\_id | UUID for SIM card resource. |
| sim\_card\_tags | A comma-separated list of associated tags. |
| sim\_group\_id | UUID for SIM group resource. |
| sim\_group\_name | The name of the related SIM group at the time that the session was active. |
| uplink\_data | Amount of data uploaded in the related session. |

---

Related Articles

[Telnyx Global SIMs FAQs](https://support.telnyx.com/en/articles/3270136-telnyx-global-sims-faqs)[Notification Settings](https://support.telnyx.com/en/articles/4277896-notification-settings)[SIM Setup and Configuration](https://support.telnyx.com/en/articles/4298710-sim-setup-and-configuration)[SIM Connectivity Logs](https://support.telnyx.com/en/articles/5666594-sim-connectivity-logs)[SIM Card Location and Device Details](https://support.telnyx.com/en/articles/5812302-sim-card-location-and-device-details)

Did this answer your question?

😞😐😃
