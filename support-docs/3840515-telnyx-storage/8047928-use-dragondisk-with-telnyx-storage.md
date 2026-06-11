---
source_url: https://support.telnyx.com/en/articles/8047928-use-dragondisk-with-telnyx-storage
scraped: 2026-06-11
---

Use DragonDisk with Telnyx Storage | Telnyx Help Center

[Skip to main content](#main-content)

# Use DragonDisk with Telnyx Storage

Set up DragonDisk with your cloud storage provider for effortless file management and seamless access to your data across multiple accounts.

Written by Telnyx Engineering

February 1, 2024

Table of contents

In this guide, discover how to set up [DragonDisk](http://www.s3-client.com/), a client for S3-compatible storage with [Telnyx Storage](https://telnyx.com/products/cloud-storage) for secure and automated backup and recovery.

[DragonDisk](http://www.s3-client.com/) is a robust file manager for Amazon S3® and other S3 API-compatible cloud storage solutions. This guide provides a step-by-step process to integrate DragonDisk with Telnyx storage, enabling seamless data management and sharing. Experience the user-friendly interface and advanced features of DragonDisk while securely utilising Telnyx storage.

---

# **How to configure DragonDisk to work with Telnyx Storage**

## Step 1

Download and install the latest version of DragonDisk [here!](http://www.s3-client.com/download-s3-compatible-cloud-client.html)

## Step 2

Open the DragonDisk application

## Step 3

Click on **File**, and select **Accounts**.  
​

[![File section. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770441531/ca30ed6dfb16961b60dcc489/jggwIMa6KBGlDUiLZFJqTVgIZSZeHuxDFdPa51Mb3qmhSLHrRy33AjCYfW8QvMBzRztH8Bvk2pQcrEj8yHVpAoXZV1nfEpf5Jh4RNAFXG0E-Kqt-S94fVwuG6jk28NIJI_PzMpqH1xEGWJjrIxlfJA?expires=1781168400&signature=c849afb3d0c8d4ceec699391d7927e28e14e2e325030efaaa67838fb6ace9323&req=cycnEs1%2FmIJeFb4f3HP0gBuzfy6vwmnpMJ8OEsuL9rlw6ZL0qsDAXSNdc26m%0Aahrm%2FI9X5OPePhzo5A%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770441531/ca30ed6dfb16961b60dcc489/jggwIMa6KBGlDUiLZFJqTVgIZSZeHuxDFdPa51Mb3qmhSLHrRy33AjCYfW8QvMBzRztH8Bvk2pQcrEj8yHVpAoXZV1nfEpf5Jh4RNAFXG0E-Kqt-S94fVwuG6jk28NIJI_PzMpqH1xEGWJjrIxlfJA?expires=1781168400&signature=c849afb3d0c8d4ceec699391d7927e28e14e2e325030efaaa67838fb6ace9323&req=cycnEs1%2FmIJeFb4f3HP0gBuzfy6vwmnpMJ8OEsuL9rlw6ZL0qsDAXSNdc26m%0Aahrm%2FI9X5OPePhzo5A%3D%3D%0A)

## Step 4

1. The **Accounts** window will pop up, click on **New**.  
   ​

   [![Accounts section. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770441540/3fb1cf5fa83acc737798d929/FKJzc1Z741nmChfQp17P83oKUDCbblNH8Uih7Z6RE_1_LlLTDvVkKF2qc6FPiUU-fSBBsGKAaqF4RslXGNRMe1dgcXT_tR7WLdanwspHdGiPP0dTat9eGT0OGp2dLAJ96YltfBXRUa_wOvKL44688w?expires=1781168400&signature=848a4fa5d5395cbae995c814fc8b62cf2f0374a07d886979b3a38071885a16c0&req=cycnEs1%2FmIVfFb4f3HP0gLlweHn6oG00fJxGkMWgYKLV18ZBw1fTzUUttqXy%0AMpc%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770441540/3fb1cf5fa83acc737798d929/FKJzc1Z741nmChfQp17P83oKUDCbblNH8Uih7Z6RE_1_LlLTDvVkKF2qc6FPiUU-fSBBsGKAaqF4RslXGNRMe1dgcXT_tR7WLdanwspHdGiPP0dTat9eGT0OGp2dLAJ96YltfBXRUa_wOvKL44688w?expires=1781168400&signature=848a4fa5d5395cbae995c814fc8b62cf2f0374a07d886979b3a38071885a16c0&req=cycnEs1%2FmIVfFb4f3HP0gLlweHn6oG00fJxGkMWgYKLV18ZBw1fTzUUttqXy%0AMpc%3D%0A)

## Step 5

1. Select **Other S3 compatible service**, from the dropdown on the **Provider** field. Then fill in the details.

   1. **Service Endpoint:** enter *<https://storage.telnyx.com>*
   2. **Account name: you can add your name/nickname here.**
   3. **Comment:** add a comment to recall this account.
   4. **Access Key:** copy and paste your [Telnyx API Key](https://portal.telnyx.com/#/app/api-keys) in this field.
   5. **Secret Key:** the secret key is not used by Telnyx Storage, but is needed by DragonDisk . You can type out anything you want here, as long as it doesn’t include spaces, quoting, or special characters of any kind.  
      ​

      [![Advanced settings of the account section. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770441548/c2535ec7d9b4e197abcdab72/jDYzU5gko4dwSHAKRUh392t4cE4SLycrwNN88NsuITA37S-lTH2lkSikoKc2ElKEbVaOo1aq__OXj5IA0WfjgLwdfnh3V8XQZTkAokN-OKF7F1nEAwQJvwuyqK-TQmmHM7heSsu10uyPYrBGagrnlw?expires=1781168400&signature=872fd6d368a09990b12a7a7ad62283d420735574d4be45a35f034715de35b0a1&req=cycnEs1%2FmIVXFb4f3HP0gHkRKx18TANksocSFJIHFVQxO56KSdVJt3wV8tLM%0AZ60%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770441548/c2535ec7d9b4e197abcdab72/jDYzU5gko4dwSHAKRUh392t4cE4SLycrwNN88NsuITA37S-lTH2lkSikoKc2ElKEbVaOo1aq__OXj5IA0WfjgLwdfnh3V8XQZTkAokN-OKF7F1nEAwQJvwuyqK-TQmmHM7heSsu10uyPYrBGagrnlw?expires=1781168400&signature=872fd6d368a09990b12a7a7ad62283d420735574d4be45a35f034715de35b0a1&req=cycnEs1%2FmIVXFb4f3HP0gHkRKx18TANksocSFJIHFVQxO56KSdVJt3wV8tLM%0AZ60%3D%0A)
2. Then click on **OK** to configure DragonDisk with Telnyx Storage

And that’s it! We have successfully configured DragonDisk with Telnyx Storage and unlocked powerful file management capabilities. Start maximizing productivity and efficiency with DragonDisk and Telnyx Storage today!

---

**Additional Resources**

For more information on how to use DragonDisk, check out their [FAQ page](http://www.s3-client.com/faq.html).

---

Related Articles

[Use S3 Browser with Telnyx Storage](https://support.telnyx.com/en/articles/6965267-use-s3-browser-with-telnyx-storage)[Use GoodSync with Telnyx Storage](https://support.telnyx.com/en/articles/8047898-use-goodsync-with-telnyx-storage)[Use Cloudmounter with Telnyx Storage](https://support.telnyx.com/en/articles/8047914-use-cloudmounter-with-telnyx-storage)[Use ExpanDrive with Telnyx Storage](https://support.telnyx.com/en/articles/8047945-use-expandrive-with-telnyx-storage)[Use AirExplorer with Telnyx Storage](https://support.telnyx.com/en/articles/8048045-use-airexplorer-with-telnyx-storage)

Did this answer your question?

😞😐😃

Table of contents
