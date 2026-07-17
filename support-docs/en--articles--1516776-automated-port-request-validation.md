---
source_url: https://support.telnyx.com/en/articles/1516776-automated-port-request-validation
title: "Automated Port Request Validation"
description: "Learn about how Telnyx automatically validates the information on your port… See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: f3d52f613fae9be143f47bb89a984f6ece0f6fc381c0aa16b50a7737e0d13a18
---







# Automated Port Request Validation

Learn about how Telnyx automatically validates the information on your port… See Telnyx guidance and requirements.




## **Automated Port Request Validation**

Porting numbers can be frustrating. Seemingly minor inconsistencies in the data provided can cause porting delays or outright rejections. Telnyx has created new functionality that automatically validates your port request with the losing carrier.
​

## How Does It Work

1. When customers submit port requests, Telnyx checks if the losing (current) carrier supports automated CSR ([Customer Service Record](https://support.telnyx.com/en/articles/1130614-obtaining-a-csr-from-your-carrier)) validation.
2. If supported, Telnyx will request a CSR using the Billing Telephone Number (BTN), account number, end customer name, and service address. It can take up to 30 minutes for a CSR to come back from the carrier.
3. Telnyx will match the submitted information with what was returned from the CSR. If the information matches, Telnyx's Porting Team will start working on the final port submission to the losing carrier.
4. If the information does not match, Telnyx will put the port request into Exception status and notify you of the errors. Customers can use the port request comments feature to provide updates to any of the fields that failed validation. Once corrected, Telnyx will re-submit the port request to the losing carrier.

## A Few Things To Note

* Only major carriers support automated validation such as Level 3, AT&T and CenturyLink. Telnyx is regularly adding support for additional carriers.
* It can take up to 30 minutes for the data to come back from the carrier. If the data provided by you is materially different from what is on file with the carrier, then the carrier will likely not return any data. Typically this is due to having an incorrect BTN, account number of service address.
* For privacy reasons, Telnyx cannot share the corrected data with you. We can only tell you if the data matched. It is up to you to provide the correct data.
* Even if data validation fails, Telnyx will continue to work on the port request. Often times the data has a minor inconsistency that Telnyx can resolve without the customer's help. We will notify you if we need further action from you.

---

Related Articles

[Porting Error Messages](https://support.telnyx.com/en/articles/1618776-porting-error-messages)[Port Request Rejected](https://support.telnyx.com/en/articles/1782930-port-request-rejected)[Porting away from Twilio](https://support.telnyx.com/en/articles/3947850-porting-away-from-twilio)[Porting away from Bandwidth](https://support.telnyx.com/en/articles/3947875-porting-away-from-bandwidth)[Porting Requirements](https://support.telnyx.com/en/articles/6460777-porting-requirements)

Did this answer your question?

😞😐😃
