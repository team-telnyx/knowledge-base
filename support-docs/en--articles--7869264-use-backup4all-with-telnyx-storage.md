---
source_url: https://support.telnyx.com/en/articles/7869264-use-backup4all-with-telnyx-storage
title: "Use Backup4all with Telnyx Storage"
description: "Learn how to set up Backup4all, a comprehensive backup software, with Telnyx Storage for automated and reliable data… See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 4c685b6d3cb40d4a50dcd489116fa8916a241627f2aeb584099269166653879c
---







# Use Backup4all with Telnyx Storage

Learn how to set up Backup4all, a comprehensive backup software, with Telnyx Storage for automated and reliable data… See Telnyx guidance and requirements.




Backup4all is a comprehensive backup software that enables users to securely and efficiently backup their data to various storage locations such as cloud services, network drives, and external hard drives. It offers a range of features including full, differential, and incremental backups, compression, encryption, scheduling, and backup verification.

---

## How to configure Cyberduck to work with Telnyx Storage

1. Download and install the latest version of Backup4all [here](https://www.backup4all.com/)!
2. Click `File` and `New` to create a new backup job
3. For `Destination`, select **Online** on the left navigation bar and then select **S3 Compatible** from the dropdown menu

   ![S3 Compatible button.](_images/a79df60c63cddc8d.jpg)
4. For the remainder of the configuration window, enter the following and then click `Next`:

   1. **Endpoint:** Copy and paste one of our available [API Endpoints](https://developers.telnyx.com/docs/cloud-storage/api-endpoints).
   2. **Access ID**: Copy and paste your [Telnyx API Key](https://portal.telnyx.com/#/app/api-keys) in this field
   3. **Secret Key**: The secret access key is not used by TelnyxStorage, but Backup4all will complain if it doesn’t exist. Type out anything you want here, as long as it doesn't include spaces, quoting, or special characters of any kind.
   4. **Region:** leave as `default`
   5. **Signature:** Version 4
   6. **Bucket:** the name of the bucket you want your data stored inSelect the sources that you wish to backup
      ​

      ![Backup sources settings section. ](_images/7785c78728b2daa7.jpg)

And that's all there is to it! You can continue the flow creating your backup job, and once finished your data will be backed up to Telnyx Storage!

---

**Additional Resources**

For more information on how to use Backup4all, check out their [product resources here](https://www.backup4all.com/table-of-contents-help.html).
​

---

Related Articles

[Use Arq Backup with Telnyx Storage](https://support.telnyx.com/en/articles/7869213-use-arq-backup-with-telnyx-storage)[Use Duplicati with Telnyx Storage](https://support.telnyx.com/en/articles/7873510-use-duplicati-with-telnyx-storage)[Use Syncovery with Telnyx Storage](https://support.telnyx.com/en/articles/8047874-use-syncovery-with-telnyx-storage)[Use GoodSync with Telnyx Storage](https://support.telnyx.com/en/articles/8047898-use-goodsync-with-telnyx-storage)[Use NetDrive3 with Telnyx Storage](https://support.telnyx.com/en/articles/8048024-use-netdrive3-with-telnyx-storage)

Did this answer your question?

😞😐😃
