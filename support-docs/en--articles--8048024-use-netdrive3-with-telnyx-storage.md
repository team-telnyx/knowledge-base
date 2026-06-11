---
source_url: https://support.telnyx.com/en/articles/8048024-use-netdrive3-with-telnyx-storage
scraped: 2026-06-11
---

Use NetDrive3 with Telnyx Storage | Telnyx Help Center

[Skip to main content](#main-content)

# Use NetDrive3 with Telnyx Storage

Learn how to integrate NetDrive3, a powerful remote storage mapping tool, with Telnyx Storage for seamless management of your data.

Written by Telnyx Engineering

June 6, 2024

Table of contents

[NetDrive3](https://netdrive.net/) is a robust remote storage mapping tool that allows you to access and manage files stored on various cloud storage platforms, network drives, and FTP/SFTP servers. With NetDrive3, you can easily mount [Telnyx Storage](https://telnyx.com/products/cloud-storage) as a virtual drive on your computer for convenient file operations.

---

# **How to integrate NetDrive3 to work with Telnyx Storage:**

## Step 1

Download and install the latest version of NetDrive3 [here!](https://netdrive.net/)

## Step 2

Launch NetDrive3 and click on the **"+"** button to create a new connection.  
​

[![NetDrive3 start page. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770468015/873fdc89efd088ee7d5d1168/m0VJRRO3UPfXx3BHMAa2MJ4-iCoY0Uow-RTFSkw3i1_LnF98TknzrbhEjUJ_YS3KzVmrhC2udTV2C8cyIcjL4joMufK2VxU-wjmCiChPmA_OcRo7IdZtn4L-liA_KbU9IKwIisQwihNf6P3Tw2jxZA?expires=1781168400&signature=95d6fa9dd77eab17182178455b962604f3a683a320d8d8016b72cb9322a41698&req=cycnEs92nYBaFb4f3HP0gB4%2FPBnW9SQ%2FVgQK19PmVxzzfwAaOeL5fnnMV7WY%0AhBbaTjHdJNgYtHSmYA%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770468015/873fdc89efd088ee7d5d1168/m0VJRRO3UPfXx3BHMAa2MJ4-iCoY0Uow-RTFSkw3i1_LnF98TknzrbhEjUJ_YS3KzVmrhC2udTV2C8cyIcjL4joMufK2VxU-wjmCiChPmA_OcRo7IdZtn4L-liA_KbU9IKwIisQwihNf6P3Tw2jxZA?expires=1781168400&signature=95d6fa9dd77eab17182178455b962604f3a683a320d8d8016b72cb9322a41698&req=cycnEs92nYBaFb4f3HP0gB4%2FPBnW9SQ%2FVgQK19PmVxzzfwAaOeL5fnnMV7WY%0AhBbaTjHdJNgYtHSmYA%3D%3D%0A)

## Step 3

In the “Add a Personal Drive” window, Select “**S3**” as the storage type from the dropdown and click on “**Connect**” to set up the connection.  
​

[![“Add a Personal Drive” window. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770468020/d98c816a42e92157263a53e5/ACEUS4YYd4w3erqX-ym8sNzQ1eHJLb9kIJV0M844dCliTvYStNm19zSjHz9ds4rn4FD6AWpQ0sWouNifX7c_TnGb9XDbr7DKocxBh7bTPi7I3LjFeikpjOify0ISOy5Kjf11DEdgglzIRHxwdCGMtQ?expires=1781168400&signature=525c74702c9f600d59607c79146a9489f9a7cefe232cb09f55f2840df22528b6&req=cycnEs92nYNfFb4f3HP0gDo3%2BTj2%2BBYOcpTa5jjcvCLMi2gaYM%2Fc9SBdTeZs%0AeHO3IkBtaoctWmUgTA%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770468020/d98c816a42e92157263a53e5/ACEUS4YYd4w3erqX-ym8sNzQ1eHJLb9kIJV0M844dCliTvYStNm19zSjHz9ds4rn4FD6AWpQ0sWouNifX7c_TnGb9XDbr7DKocxBh7bTPi7I3LjFeikpjOify0ISOy5Kjf11DEdgglzIRHxwdCGMtQ?expires=1781168400&signature=525c74702c9f600d59607c79146a9489f9a7cefe232cb09f55f2840df22528b6&req=cycnEs92nYNfFb4f3HP0gDo3%2BTj2%2BBYOcpTa5jjcvCLMi2gaYM%2Fc9SBdTeZs%0AeHO3IkBtaoctWmUgTA%3D%3D%0A)

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

   [![Personal storage type addition section. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770468024/be559197a570f2b681ffb044/Ka0rHyYS7Otw_ZJ81xox9vzDS4zIJjM6OV1W0mXWxKl1415B6ruu94Kg-rnMlW2D_jq0xj3zmdqtyt0IjiNN-pn_ztuMpoJasDfGiXWM4NKWPclNJ-yljKYR9JWU0xKXULzoHhUE3d9jH_igc1-Jpw?expires=1781168400&signature=fd7dda46e17f3d3ca8aa6fbd1d72889809ae3d0204acd10bf9eff30c4f0def3b&req=cycnEs92nYNbFb4f3HP0gAkKZVodZk1miN7d0Yt47CbBNVJn9nxsbiirXOb3%0AWrc%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770468024/be559197a570f2b681ffb044/Ka0rHyYS7Otw_ZJ81xox9vzDS4zIJjM6OV1W0mXWxKl1415B6ruu94Kg-rnMlW2D_jq0xj3zmdqtyt0IjiNN-pn_ztuMpoJasDfGiXWM4NKWPclNJ-yljKYR9JWU0xKXULzoHhUE3d9jH_igc1-Jpw?expires=1781168400&signature=fd7dda46e17f3d3ca8aa6fbd1d72889809ae3d0204acd10bf9eff30c4f0def3b&req=cycnEs92nYNbFb4f3HP0gAkKZVodZk1miN7d0Yt47CbBNVJn9nxsbiirXOb3%0AWrc%3D%0A)

## Step 6

After the setup above for the connection is completed, this window will pop up. Click on **Connect** to link NetDrive3 with Telnyx Storage.  
​

[![NetDrive3 - Telnyx connection setup. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770468027/b6909c2aef6dacccb4d1d76c/umqliiA1fJM_Fmfqwd96q5F81353DL3r7LcefZSYsIsClux5d_BTqMo6mcyzXzcxowTRwhAJaosTfYE1bzWiYwQmxhEzGP8PWGzM3eFvtdX9XkUP3RpaWxG5wl7bRXNwjQOer_YVGO3rRHSjXqGD7A?expires=1781168400&signature=3cbb40ec56966ae788f6f23a1dd517a62253415442cc7f165c32eb3afc44465d&req=cycnEs92nYNYFb4f3HP0gHLEknBpJpH1p2xsHot8V54d6WjebTumKCm3Ih8N%0AD4hua2U4DZqxQbXiZQ%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770468027/b6909c2aef6dacccb4d1d76c/umqliiA1fJM_Fmfqwd96q5F81353DL3r7LcefZSYsIsClux5d_BTqMo6mcyzXzcxowTRwhAJaosTfYE1bzWiYwQmxhEzGP8PWGzM3eFvtdX9XkUP3RpaWxG5wl7bRXNwjQOer_YVGO3rRHSjXqGD7A?expires=1781168400&signature=3cbb40ec56966ae788f6f23a1dd517a62253415442cc7f165c32eb3afc44465d&req=cycnEs92nYNYFb4f3HP0gHLEknBpJpH1p2xsHot8V54d6WjebTumKCm3Ih8N%0AD4hua2U4DZqxQbXiZQ%3D%3D%0A)

## Step 7

Once connected, NetDrive3 will display the Telnyx Storage site as a virtual drive on your computer. You can now access and manage your files stored in Telnyx Storage seamlessly.  
​

[![Telnyx storage on NetDrive3. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770468033/7675c11d7b4cf45efb727c60/rNCHrNgtO5UqDzKNgfHwDCN_Buuklmh4flUE0Bc_u9pwD2Sst6zASqq2ejDqIGutG1fG0j264dYP8z8qesJQ8gRlSaqZdw1LXZw6I9StF4_ee8a3G_-b3Sg4eBKzr1GWOOfoTW5Jr_ST7u-qtHpojg?expires=1781168400&signature=e3c6791f822fd0384d8382a9c3da2325a01a177437b310efae39e0cf099636f5&req=cycnEs92nYJcFb4f3HP0gJ0MhDRFxzsGA61YcYMuekuZlrasqJvggTxWxdyU%0AnREjG54oQiUCtHEIZQ%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770468033/7675c11d7b4cf45efb727c60/rNCHrNgtO5UqDzKNgfHwDCN_Buuklmh4flUE0Bc_u9pwD2Sst6zASqq2ejDqIGutG1fG0j264dYP8z8qesJQ8gRlSaqZdw1LXZw6I9StF4_ee8a3G_-b3Sg4eBKzr1GWOOfoTW5Jr_ST7u-qtHpojg?expires=1781168400&signature=e3c6791f822fd0384d8382a9c3da2325a01a177437b310efae39e0cf099636f5&req=cycnEs92nYJcFb4f3HP0gJ0MhDRFxzsGA61YcYMuekuZlrasqJvggTxWxdyU%0AnREjG54oQiUCtHEIZQ%3D%3D%0A)

That's it! You have successfully integrated NetDrive3 with Telnyx Storage, allowing you to work with your files using a virtual drive interface conveniently.  
​

Feel free to explore the capabilities of NetDrive3 and leverage the power of Telnyx Storage for your file management needs.

---

**Additional Resources**

If you need more information or assistance, you can refer to NetDrive3's [documentation.](https://netdrive.net/support/)

---

Related Articles

[Use GoodSync with Telnyx Storage](https://support.telnyx.com/en/articles/8047898-use-goodsync-with-telnyx-storage)[Use ExpanDrive with Telnyx Storage](https://support.telnyx.com/en/articles/8047945-use-expandrive-with-telnyx-storage)[Use ODrive with Telnyx Storage](https://support.telnyx.com/en/articles/8047956-use-odrive-with-telnyx-storage)[Use WebDrive with Telnyx Storage](https://support.telnyx.com/en/articles/8047969-use-webdrive-with-telnyx-storage)[Use AirExplorer with Telnyx Storage](https://support.telnyx.com/en/articles/8048045-use-airexplorer-with-telnyx-storage)

Did this answer your question?

😞😐😃

Table of contents
