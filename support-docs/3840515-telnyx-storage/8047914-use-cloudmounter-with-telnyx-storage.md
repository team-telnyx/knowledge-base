---
source_url: https://support.telnyx.com/en/articles/8047914-use-cloudmounter-with-telnyx-storage
scraped: 2026-06-11
---

Use Cloudmounter with Telnyx Storage | Telnyx Help Center

[Skip to main content](#main-content)

# Use Cloudmounter with Telnyx Storage

Discover how to configure CloudMounter with Telnyx Storage to seamlessly access and manage your files across multiple cloud accounts

Written by Telnyx Engineering

June 6, 2024

Table of contents

[CloudMounter](https://cloudmounter.net/) is a powerful file management tool that allows you to mount various cloud storage services directly on your computer, providing seamless access and file synchronization across multiple platforms.

In this guide, we will walk you through the step-by-step process of integrating CloudMounter with [Telnyx Storage](https://telnyx.com/products/cloud-storage). This guide will help you effortlessly connect and manage your Telnyx storage within the CloudMounter application, enabling efficient file transfers and storage management.

---

# How to configure Cloudmounter to work with Telnyx Storage

## **Step 1**

Visit the Cloudmounter site and download the application for either Mac or Windows [here!](https://cloudmounter.net/)

## **Step 2**

Install CloudMounter on your computer, and launch the application.  
​

[![CloudMounter interface. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770438148/ea30538e0713296ff23c2fe6/TH5Xbxv1XkuKlz9_4vv__s7E8sVWMAXaBO0D-lLUegsLypbAPvR8sFQJyU1rwXB5IC89_CE_csfj3HDswq-83hFzGVpx0P9ghQ-l_r3FhhY7xblETAYPsBTjT7C_KB83F7G8NZ0Q1aDF8p-HiQb4ug?expires=1781168400&signature=a0d8361355c921d0f708f5c43c8f845e71fa23716733877a80ef0330c2b3273a&req=cycnEsp2nIVXFb4f3HP0gEn271E7zuSMljP0K0grucWCWCpXIuKSZcMVs63s%0AYOgTZklvr1s9%2BDje0g%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770438148/ea30538e0713296ff23c2fe6/TH5Xbxv1XkuKlz9_4vv__s7E8sVWMAXaBO0D-lLUegsLypbAPvR8sFQJyU1rwXB5IC89_CE_csfj3HDswq-83hFzGVpx0P9ghQ-l_r3FhhY7xblETAYPsBTjT7C_KB83F7G8NZ0Q1aDF8p-HiQb4ug?expires=1781168400&signature=a0d8361355c921d0f708f5c43c8f845e71fa23716733877a80ef0330c2b3273a&req=cycnEsp2nIVXFb4f3HP0gEn271E7zuSMljP0K0grucWCWCpXIuKSZcMVs63s%0AYOgTZklvr1s9%2BDje0g%3D%3D%0A)

## **Step 3**

Select “**Amazon S3”** as the type of storage to be mounted.  
​

[![Amazon S3 interface. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770438155/eb3fd448b18c21fc3449ffe6/n9AbL6DvqAwiMIjYWKdt6wncsUHvlCimk-AUuSDo64213pc9pJ0Ot4yPjpUpGZqQ2xXNo2P2ylsL3uzsf6pIJ94BEfy0fF2n_0lGj0-IjQ2cJYgAtN8bhNJ4aZQcFsToSbRsGI4oO2s6hM7gCojDCQ?expires=1781168400&signature=30c987681cb12b04f0c80a16d93fb6b9527626056b6552664e7b87a86ac96524&req=cycnEsp2nIRaFb4f3HP0gFOjWC6X%2ByOaMpF30hcHOLhWyDevDQGw6LUPxL2e%0AmgookVAJizMGC12S0A%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770438155/eb3fd448b18c21fc3449ffe6/n9AbL6DvqAwiMIjYWKdt6wncsUHvlCimk-AUuSDo64213pc9pJ0Ot4yPjpUpGZqQ2xXNo2P2ylsL3uzsf6pIJ94BEfy0fF2n_0lGj0-IjQ2cJYgAtN8bhNJ4aZQcFsToSbRsGI4oO2s6hM7gCojDCQ?expires=1781168400&signature=30c987681cb12b04f0c80a16d93fb6b9527626056b6552664e7b87a86ac96524&req=cycnEsp2nIRaFb4f3HP0gFOjWC6X%2ByOaMpF30hcHOLhWyDevDQGw6LUPxL2e%0AmgookVAJizMGC12S0A%3D%3D%0A)

## **Step 4**

A window below will pop up, then fill in the details:

1. **Name:** Input your name
2. **Access Key:** Input your Telnyx API Key in the Access Key ID field. You can get this from your [Telnyx portal](https://portal.telnyx.com/#/app/api-keys).
3. **Secret Key:** The secret access key is not used by Telnyx Storage, but is needed by Cloudmounter. Type out anything you want here, as long as it doesn't include spaces, quoting, or special characters of any kind.
4. **Server Endpoint:** Copy and paste one of our available [API Endpoints](https://developers.telnyx.com/docs/cloud-storage/api-endpoints).
5. **Bucket:** Add a bucket name from your list of buckets on the [storage](https://portal.telnyx.com/#/app/storage/buckets) section of the Telnyx portal

[![Amazing S3 connections settings. ](https://downloads.intercomcdn.com/i/o/888708132/4072de4db2024f0d97956b4c/Screenshot+2023-11-20+at+11.19.51%E2%80%AFAM.jpg?expires=1781168400&signature=7ceb4113044e453e4caa080cac5780ef4158f021b8ef9eccf0cfe4a7cda7af4f&req=fCgvEcl2nIJdFb4f3HP0gOQeTVPKNSbKVqhlGEXXDJ6tw2qWz0iEty%2Bhmbjw%0A7cli30IKRymFU8zNzg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/888708132/4072de4db2024f0d97956b4c/Screenshot+2023-11-20+at+11.19.51%E2%80%AFAM.jpg?expires=1781168400&signature=7ceb4113044e453e4caa080cac5780ef4158f021b8ef9eccf0cfe4a7cda7af4f&req=fCgvEcl2nIJdFb4f3HP0gOQeTVPKNSbKVqhlGEXXDJ6tw2qWz0iEty%2Bhmbjw%0A7cli30IKRymFU8zNzg%3D%3D%0A)

## **Step 5**

After filling in all the details above, click on the “**Mount”** button to connect CloudMounter with Telnyx Storage.  
​

That's it! You have successfully configured CloudMounter with Telnyx storage, allowing you to conveniently access and manage your files stored in Telnyx from within the CloudMounter application. With this integration, you can enjoy seamless file synchronization, easy file transfers, and enhanced collaboration across different cloud storage platforms.

---

**Additional Resources**

For more detailed information and advanced features of CloudMounter, please refer to the CloudMounter [blog](https://cloudmounter.net/blog/).

If you have any further questions or need additional assistance, feel free to reach out. Happy file managing with CloudMounter and Telnyx Storage!  
​

---

Related Articles

[Use S3 Browser with Telnyx Storage](https://support.telnyx.com/en/articles/6965267-use-s3-browser-with-telnyx-storage)[Use Syncovery with Telnyx Storage](https://support.telnyx.com/en/articles/8047874-use-syncovery-with-telnyx-storage)[Use ExpanDrive with Telnyx Storage](https://support.telnyx.com/en/articles/8047945-use-expandrive-with-telnyx-storage)[Use ODrive with Telnyx Storage](https://support.telnyx.com/en/articles/8047956-use-odrive-with-telnyx-storage)[Use AirExplorer with Telnyx Storage](https://support.telnyx.com/en/articles/8048045-use-airexplorer-with-telnyx-storage)

Did this answer your question?

😞😐😃

Table of contents
