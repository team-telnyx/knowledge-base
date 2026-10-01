---
source_url: https://support.telnyx.com/en/articles/8048024-use-netdrive3-with-telnyx-storage
title: "Use NetDrive3 with Telnyx Storage"
description: "Learn how to integrate NetDrive3, a powerful remote storage mapping tool, See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 53827025a4d5d2207988c93f182b2b45244f2cfb6fd37a3a522d5db7f99fc758
---







# Use NetDrive3 with Telnyx Storage

Learn how to integrate NetDrive3, a powerful remote storage mapping tool, See Telnyx guidance and requirements.




[NetDrive3](https://netdrive.net/) is a robust remote storage mapping tool that allows you to access and manage files stored on various cloud storage platforms, network drives, and FTP/SFTP servers. With NetDrive3, you can easily mount [Telnyx Storage](https://telnyx.com/products/cloud-storage) as a virtual drive on your computer for convenient file operations.

---

## **How to integrate NetDrive3 to work with Telnyx Storage:**

## Step 1

Download and install the latest version of NetDrive3 [here!](https://netdrive.net/)

## Step 2

Launch NetDrive3 and click on the **"+"** button to create a new connection.
​

![NetDrive3 start page. ](_images/fd46f50d5e1371f1.png)

## Step 3

In the “Add a Personal Drive” window, Select “**S3**” as the storage type from the dropdown and click on “**Connect**” to set up the connection.
​

![“Add a Personal Drive” window. ](_images/2a716c80be2dd9cf.png)

## Step 4

Fill in these fields with the information below:

1. **Server Address:** Copy and paste one of our available [API Endpoints](https://developers.telnyx.com/docs/cloud-storage/api-endpoints).
2. **Access ID:** Copy and paste your [Telnyx API Key](https://portal.telnyx.com/#/app/api-keys) into this field.
3. **Secret Key:** Although Telnyx Storage does not use the secret key, input any value without spaces or special characters.
4. **Bucket name:** Enter the bucket name on your [Telnyx Storage](https://portal.telnyx.com/#/app/storage/buckets) that you want to connect.

## Step 5

After entering the information above, you’ll see **S3** added as a storage type.

1. You’ll also see the remote path which is based on the bucket name you entered above.
2. Click on **OK** to continue the setup.
   ​

   ![Personal storage type addition section. ](_images/4456da3065a23210.png)

## Step 6

After the setup above for the connection is completed, this window will pop up. Click on **Connect** to link NetDrive3 with Telnyx Storage.
​

![NetDrive3 - Telnyx connection setup. ](_images/377dede35e60841a.png)

## Step 7

Once connected, NetDrive3 will display the Telnyx Storage site as a virtual drive on your computer. You can now access and manage your files stored in Telnyx Storage seamlessly.
​

![Telnyx storage on NetDrive3. ](_images/c73646827087e6e7.png)

That's it! You have successfully integrated NetDrive3 with Telnyx Storage, allowing you to work with your files using a virtual drive interface conveniently.
​

Feel free to explore the capabilities of NetDrive3 and leverage the power of Telnyx Storage for your file management needs.

---

**Additional Resources**

If you need more information or assistance, you can refer to NetDrive3's [documentation.](https://netdrive.net/support/)
