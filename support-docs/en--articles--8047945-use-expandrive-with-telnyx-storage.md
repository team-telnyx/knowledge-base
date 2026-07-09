---
source_url: https://support.telnyx.com/en/articles/8047945-use-expandrive-with-telnyx-storage
scraped: 2026-07-08
content_hash: 0eff199459f814b43a0a472d47421c39df8a8c3b56eb4f667b4cdb5cf154b87e
---

Use ExpanDrive with Telnyx Storage | Telnyx Help Center

[Skip to main content](#main-content)

# Use ExpanDrive with Telnyx Storage

Learn how to integrate ExpanDrive, a powerful cloud storage client, with Telnyx Storage for seamless access and management of your files.

Written by Telnyx Engineering

June 6, 2024

Table of contents

[ExpanDrive](https://www.expandrive.com/) is a versatile cloud storage client that allows you to mount cloud storage as a local drive on your computer. It provides a unified interface to access and manage files across multiple cloud storage providers, including Telnyx Storage. With ExpanDrive, you can easily navigate and interact with your Telnyx Storage files as if they were stored locally.

---

# **How to configure ExpanDrive to work with Telnyx Storage**

## Step 1

Download and install the latest version of ExpanDrive [here!](https://www.expandrive.com/desktop/)

## Step 2

Launch the ExpanDrive application click on **“ExpanDrive”** and then “**New Connection”.**  
​

![ExpanDrive section. ](_images/ed62ee9807d50ecd.png)

## Step 3

Select **"Amazon S3"** from the list of storage options.  
​

![Amazon s3 button. ](_images/3d5c0bf65065502a.png)

## Step 4

Fill in the storage options with the information below:

1. **Server:** Copy and paste one of our available [API Endpoints](https://developers.telnyx.com/docs/cloud-storage/api-endpoints).
2. **Access Key:** Copy and paste your [Telnyx API Key](https://portal.telnyx.com/#/app/api-keys) in this field.
3. **Secret Key:** You can type out anything you want here, as long as it doesn’t include spaces, quoting, or special characters of any kind.
4. **Custom Region:** Copy and paste the matching region from [API Endpoints](https://developers.telnyx.com/docs/cloud-storage/api-endpoints). For example, if you chose the [https://us-central-1.telnyxstorage.com](https://us-central-1.telnyxstorage.com/) endpoint, you will use us-central-1 as the region.
5. **Nickname:** Use your nickname or whatever name you want.
6. **Bucket:** You can enter the bucket name on your Telnyx storage on leave it blank.
7. **Drive Letter:** Select the drive letter from your local storage. It could be any of the letters.  
   ​

   ![Storage options section. ](_images/ad0927067aa545b9.jpg)

## Step 5

1. Click on the "**Save**" button to set up the connection. ExpanDrive will authenticate your Telnyx Storage account using the provided API Key.

Once the authentication is successful, you can access your Telnyx Storage files through the ExpanDrive interface, which will appear as a mounted drive on your computer.

![Telnyx Storage files section. ](_images/674fe6b4d0f52077.png)

---

**Additional Resources**

For more information on how to use ExpanDrive and its features, check out their [blog.](https://www.expandrive.com/)

---

Related Articles

[Use Cloudmounter with Telnyx Storage](https://support.telnyx.com/en/articles/8047914-use-cloudmounter-with-telnyx-storage)[Use ODrive with Telnyx Storage](https://support.telnyx.com/en/articles/8047956-use-odrive-with-telnyx-storage)[Use WebDrive with Telnyx Storage](https://support.telnyx.com/en/articles/8047969-use-webdrive-with-telnyx-storage)[Use NetDrive3 with Telnyx Storage](https://support.telnyx.com/en/articles/8048024-use-netdrive3-with-telnyx-storage)[Use AirExplorer with Telnyx Storage](https://support.telnyx.com/en/articles/8048045-use-airexplorer-with-telnyx-storage)

Did this answer your question?

😞😐😃

Table of contents
