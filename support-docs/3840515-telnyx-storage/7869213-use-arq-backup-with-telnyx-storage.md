---
source_url: https://support.telnyx.com/en/articles/7869213-use-arq-backup-with-telnyx-storage
scraped: 2026-06-11
---

Use Arq Backup with Telnyx Storage | Telnyx Help Center

[Skip to main content](#main-content)

# Use Arq Backup with Telnyx Storage

Discover how to set up Arq Backup with Telnyx Storage for secure and efficient file backup and storage management.

Written by Telnyx Engineering

June 19, 2024

Table of contents

Arq Backup is a backup software designed for developers that securely backs up their important files and data to various storage providers. It offers features such as incremental backups, versioning, compression, and encryption, as well as customizable backup schedules and a backup health monitor.

---

# How to configure Arq Backup to work with Telnyx Storage

1. Download and install the latest version of Arq backup [here](https://www.arqbackup.com/)!
2. Open the Arq Backup application. Then, click on the button to create a **New Storage Location**

[![New Storage Location button. ](https://downloads.intercomcdn.com/i/o/735026176/6f3c79c871b7283e6b896191/a18bbb8b-f41a-4e07-96f5-15206b56305c?expires=1781168400&signature=251e5f29ebb0cbc30a2d16ee4c77fbd9f8fbb4aaa8645e56e634a732c37f2bcf&req=cyMiFst4nIZZFb4f3HP0gJ9MDDDhL13ay5bDVLUsrSxef77EJ38XOtHchByx%0A8IZz7vx7nUsBLYV1lQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/735026176/6f3c79c871b7283e6b896191/a18bbb8b-f41a-4e07-96f5-15206b56305c?expires=1781168400&signature=251e5f29ebb0cbc30a2d16ee4c77fbd9f8fbb4aaa8645e56e634a732c37f2bcf&req=cyMiFst4nIZZFb4f3HP0gJ9MDDDhL13ay5bDVLUsrSxef77EJ38XOtHchByx%0A8IZz7vx7nUsBLYV1lQ%3D%3D%0A)

## Select the option for **S3-Compatible Server**

[![S3-Compatible Server button. ](https://downloads.intercomcdn.com/i/o/735026596/a9660423662a49d7a89580fb/3e717306-e4ff-4882-817c-a43d9bf7ef85?expires=1781168400&signature=357f3d626c3a71c77551cd035fea10ce7e020d3e5e282c087baedc6586f0d26f&req=cyMiFst4mIhZFb4f3HP0gG7Ziyg1nd4FaORLSURkYa1RJsJ96zF3rL586uzW%0AFJVBeu%2F6oFDK68F4CA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/735026596/a9660423662a49d7a89580fb/3e717306-e4ff-4882-817c-a43d9bf7ef85?expires=1781168400&signature=357f3d626c3a71c77551cd035fea10ce7e020d3e5e282c087baedc6586f0d26f&req=cyMiFst4mIhZFb4f3HP0gG7Ziyg1nd4FaORLSURkYa1RJsJ96zF3rL586uzW%0AFJVBeu%2F6oFDK68F4CA%3D%3D%0A)

1. In the window, enter in the following information and then click **Connect**:

   1. **Server URL:** Copy and paste one of our available [API Endpoints](https://developers.telnyx.com/docs/cloud-storage/api-endpoints).
   2. **Access Key ID:** Copy and paste your [Telnyx API Key](https://portal.telnyx.com/#/app/api-keys) in this field
   3. **Secret Access Key:** The secret access key is not used by Telnyx Storage, but Arq will complain if it doesn’t exist. Type out anything you want here, as long as it doesn't include spaces, quoting, or special characters of any kind.
   4. **Region:** Copy and paste the matching region from [API Endpoints](https://developers.telnyx.com/docs/cloud-storage/api-endpoints). For example, if you chose the [https://us-central-1.telnyxstorage.com](https://us-central-1.telnyxstorage.com/) endpoint, you will use us-central-1 as the region.

      [![Bucket name section. ](https://downloads.intercomcdn.com/i/o/885760521/07e125ce72ded2e6ec820191/Screenshot+2023-11-15+at+2.52.40%E2%80%AFPM.jpg?expires=1781168400&signature=a1958b9d6fb648b77aa9b85bb90c08aed888900a613734eb849c8dbd6cda7e8d&req=fCgiEc9%2BmINeFb4f3HP0gL3Qbfv04WpK3QAX%2Fo%2FTvz71vbru55z4vEcD1w%2BN%0AqxU%3D%0A)](https://downloads.intercomcdn.com/i/o/885760521/07e125ce72ded2e6ec820191/Screenshot+2023-11-15+at+2.52.40%E2%80%AFPM.jpg?expires=1781168400&signature=a1958b9d6fb648b77aa9b85bb90c08aed888900a613734eb849c8dbd6cda7e8d&req=fCgiEc9%2BmINeFb4f3HP0gL3Qbfv04WpK3QAX%2Fo%2FTvz71vbru55z4vEcD1w%2BN%0AqxU%3D%0A)
2. Finally, decide which bucket you would like to store your backups in. You can either create a brand new bucket, or use one of your existing buckets.

[![Bucket creation section. ](https://downloads.intercomcdn.com/i/o/735029704/a2df2b1264914a40415063a3/6f617b72-b11f-4053-84df-a63eab483339?expires=1781168400&signature=97c259afd016d0c02c9f0e7064535bea9a494d0089c47d2ceb82f08df4f49e1a&req=cyMiFst3moFbFb4f3HP0gIfHFreefwyvfgitdCATlGiS4obVIYDALJJ2siVW%0ATZ5Q5KZl68tqUkc9JQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/735029704/a2df2b1264914a40415063a3/6f617b72-b11f-4053-84df-a63eab483339?expires=1781168400&signature=97c259afd016d0c02c9f0e7064535bea9a494d0089c47d2ceb82f08df4f49e1a&req=cyMiFst3moFbFb4f3HP0gIfHFreefwyvfgitdCATlGiS4obVIYDALJJ2siVW%0ATZ5Q5KZl68tqUkc9JQ%3D%3D%0A)

## **Completed**

And that’s all there is to it! Now, you can create new backup plans with Telnyx Storage as your storage location using Arq.

[![Telnyx storage section. ](https://downloads.intercomcdn.com/i/o/735030125/e7f4fbb330a9d81cc5091fc9/9c8fbb5b-c411-49de-a68f-aefc91228ccb?expires=1781168400&signature=959bbef9f31d2442a1601f798f4e3d1800d2946274e430ce125898ece2c14631&req=cyMiFsp%2BnINaFb4f3HP0gBM29SuXnUt08M6zwZTrI63IDPYWLH6abcxZ%2Fb2R%0A8dT1V6x558ovRyAwMA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/735030125/e7f4fbb330a9d81cc5091fc9/9c8fbb5b-c411-49de-a68f-aefc91228ccb?expires=1781168400&signature=959bbef9f31d2442a1601f798f4e3d1800d2946274e430ce125898ece2c14631&req=cyMiFsp%2BnINaFb4f3HP0gBM29SuXnUt08M6zwZTrI63IDPYWLH6abcxZ%2Fb2R%0A8dT1V6x558ovRyAwMA%3D%3D%0A)

---

**Additional Resources**

For more information on how to use Arq Backup, check out their [knowledge base here](https://www.arqbackup.com/learn/).

---

Related Articles

[Use Backup4all with Telnyx Storage](https://support.telnyx.com/en/articles/7869264-use-backup4all-with-telnyx-storage)[Use Duplicati with Telnyx Storage](https://support.telnyx.com/en/articles/7873510-use-duplicati-with-telnyx-storage)[Use WinSCP with Telnyx Storage](https://support.telnyx.com/en/articles/7903390-use-winscp-with-telnyx-storage)[Use GoodSync with Telnyx Storage](https://support.telnyx.com/en/articles/8047898-use-goodsync-with-telnyx-storage)[Use AirExplorer with Telnyx Storage](https://support.telnyx.com/en/articles/8048045-use-airexplorer-with-telnyx-storage)

Did this answer your question?

😞😐😃

Table of contents
