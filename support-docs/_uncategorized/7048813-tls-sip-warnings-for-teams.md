---
source_url: https://support.telnyx.com/en/articles/7048813-tls-sip-warnings-for-teams
scraped: 2026-06-11
---

TLS & SIP Warnings for Teams | Telnyx Help Center

[Skip to main content](#main-content)

# TLS & SIP Warnings for Teams

Fix warnings related to TLS connectivity and SIP Options in your existing Microsoft Teams Direct Routing SBC setup.

Written by Telnyx Engineering

January 29, 2026

Table of contents

# TLS Connectivity and SIP Options Warnings for Existing Microsoft Teams Direct Routing SBC Setup

If you already have Microsoft Teams Direct Routing configured with an SBC, you may encounter warnings related to TLS connectivity and SIP Options status.

While these warnings do not impact call quality or reliability, we recommend implementing the following setup to address any potential configuration issues and ensure an optimal experience.

First, you will need to have PowerShell installed.

You will be performing all the configurations there.

To install Powershell on your Microsoft Windows computer follow [this](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-windows?view=powershell-7.4&viewFallbackFrom=powershell-7.3) article.

To install Powershell on your Mac follow [this](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-macos?view=powershell-7.4&viewFallbackFrom=powershell-7.3) article.

## Run PowerShell in Microsoft Windows

Run *cmd.exe* and execute the following command:

```
PowerShell
```

## Run PowerShell in Mac

Run Mac Terminal and execute the following command:  
​

```
pwsh
```

In Powershell, import the Microsoft Teams module if you don’t already have it by running the following command:

```
Import-Module MicrosoftTeams
```

Connect to the Customer tenant using the Teams module:

```
Connect-MicrosoftTeams
```

A window will pop up for the credentials to be inserted as any other time we login into the desired account.

### **Add a new Online PSTN Usage**:

Execute the following command:  
​

```
Set-CsOnlinePstnUsage -Identity Global -Usage @{Add="Telnyx"}
```

Verify that the usage was created by entering:

```
Get-CSOnlinePSTNUsage
```

Which returns a list of names that may be truncated:

[![List of names. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/683899878/e1892a30632f5d07df6f854e/3tqrt74Nxh4Z_mLTP7YL9T6o8fcM_7CE5WqNvskkZqwFYBK3Gq6tWKDsAYUNpxVO_Rqsa198CWnBoOy0_s1cpfwwD-8ZNtH5px4tWl6M5gSz9lQxMNWrxfSXP_45-I-hStly6ZPqg1zA_CvudPHDzeI?expires=1781168400&signature=5600e90193b9c349df8da7568f9000349bca76002f8a5c5b03d47ab36503b0ab&req=cigkHsB3lYZXFb4f3HP0gOqZdwVbulp3%2FoJ%2FfLmQ3GVAkBQqkS7dkqPdTFR6%0Ai7DDJ1qAG0Y8rl1X8g%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/683899878/e1892a30632f5d07df6f854e/3tqrt74Nxh4Z_mLTP7YL9T6o8fcM_7CE5WqNvskkZqwFYBK3Gq6tWKDsAYUNpxVO_Rqsa198CWnBoOy0_s1cpfwwD-8ZNtH5px4tWl6M5gSz9lQxMNWrxfSXP_45-I-hStly6ZPqg1zA_CvudPHDzeI?expires=1781168400&signature=5600e90193b9c349df8da7568f9000349bca76002f8a5c5b03d47ab36503b0ab&req=cigkHsB3lYZXFb4f3HP0gOqZdwVbulp3%2FoJ%2FfLmQ3GVAkBQqkS7dkqPdTFR6%0Ai7DDJ1qAG0Y8rl1X8g%3D%3D%0A)

### **Add a new voice profile**

Which uses the subdomain previously verified on the account

In this step, we are going to associate the existing subdomain auto-generated in the Telnyx SIP connection to the new Voice Profile.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2002430488/66d94073f2a4dff1636933a1e84b/Screenshot+from+2026-01-28+22-49-58.png?expires=1781168400&signature=44ac1be6d02ebf66fdcb3ef4f3cfe9b747621777004de6c23501909034ddfa16&req=diAnFM19nYVXUfMW1HO4zRrxHuNmct735HuaHzJcH0CdxE2fxJEagPpZXgN3%0AWIbMJ9YogKftjyBhAKc%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2002430488/66d94073f2a4dff1636933a1e84b/Screenshot+from+2026-01-28+22-49-58.png?expires=1781168400&signature=44ac1be6d02ebf66fdcb3ef4f3cfe9b747621777004de6c23501909034ddfa16&req=diAnFM19nYVXUfMW1HO4zRrxHuNmct735HuaHzJcH0CdxE2fxJEagPpZXgN3%0AWIbMJ9YogKftjyBhAKc%3D%0A)

In order to do that, you should run the following command (tailored to your configuration):

```
New-CsOnlineVoiceRoute -Name "Multi-Tenant" -Priority 1 -OnlinePSTNUsage "Telnyx" -OnlinePSTNGatewayList <string_from_the_telnyx_portal_connection>.mstsbc.telnyx.tech -NumberPattern '^(\+1[0-9]{10})$' -Description "Telnyx"
```

You should get an output similar to the one below:

[![Output sequence section. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/683899892/faaa8088ee85819a131bdb60/WxnRENW9gNqhzvP54tvZQ2m6uf0nljdXryVS7olWzT4eQnfpNtdTrRy2sUBsCayI9MipgHotrl1YZg-IWHHRYqNMO23nHCbIlDZIVXt8RC9G5zKtOLQI6Rig3a_gbX77lxfw02fcVNCE-zZYz-KgSFY?expires=1781168400&signature=3b85a46d8dad4d7cdd9b89d142befd2dbca09ec73ff6b796f37b0793c5828fa4&req=cigkHsB3lYhdFb4f3HP0gMaLQluZVF7sItPugwB8gZ0zYzr4HZXYYzg96%2BkL%0A4z5iS1RfBJAw%2BwubbA%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/683899892/faaa8088ee85819a131bdb60/WxnRENW9gNqhzvP54tvZQ2m6uf0nljdXryVS7olWzT4eQnfpNtdTrRy2sUBsCayI9MipgHotrl1YZg-IWHHRYqNMO23nHCbIlDZIVXt8RC9G5zKtOLQI6Rig3a_gbX77lxfw02fcVNCE-zZYz-KgSFY?expires=1781168400&signature=3b85a46d8dad4d7cdd9b89d142befd2dbca09ec73ff6b796f37b0793c5828fa4&req=cigkHsB3lYhdFb4f3HP0gMaLQluZVF7sItPugwB8gZ0zYzr4HZXYYzg96%2BkL%0A4z5iS1RfBJAw%2BwubbA%3D%3D%0A)

From now on, on the customer tenant there are no OPTIONS to check, just the voice route.

### **Add a new Routing Policy**

To add a new Routing Policy run the following command (tailored to your configuration):  
​

```
New-CsOnlineVoiceRoutingPolicy "Telnyx" -OnlinePstnUsages "Telnyx"
```

```
Grant-CsOnlineVoiceRoutingPolicy -Identity "<user_email>" -PolicyName "Telnyx"
```

To verify the Voice Routing Policy was correctly created and attached to the user you specified, run the following command:

```
Get-CsOnlineUser "<your_user>@<string_from_the_telnyx_portal_connection>.mstsbc.telnyx.tech" | select OnlineVoiceRoutingPolicy
```

You should get an output similar to the one below:

[![Output sequence. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/683899899/2fe8f53e2b593e17fae2b80e/PNrXoPfb5PbxSdcMPWLpXSKhzGMxUVhTlcNlC0DgoweZaOokOnzWMn_K0D1m1MAudL4lz_wIut64f1TtoowVx3jF9fQqeHduGDc8k1A3bfXbd521GCHiUtshYuT80IZFg4GU2yR64F7bWxhvF0E3Feg?expires=1781168400&signature=bc968862213c2a4e7913c9efc329d8a6bf933f82ee6b53fe9c83c7f76348ceb4&req=cigkHsB3lYhWFb4f3HP0gBPMAKNBQtYgtVF7zvLYMQB4%2FVX3iRd8gmuEwc2q%0AHShnV4t0JQfH97ldSA%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/683899899/2fe8f53e2b593e17fae2b80e/PNrXoPfb5PbxSdcMPWLpXSKhzGMxUVhTlcNlC0DgoweZaOokOnzWMn_K0D1m1MAudL4lz_wIut64f1TtoowVx3jF9fQqeHduGDc8k1A3bfXbd521GCHiUtshYuT80IZFg4GU2yR64F7bWxhvF0E3Feg?expires=1781168400&signature=bc968862213c2a4e7913c9efc329d8a6bf933f82ee6b53fe9c83c7f76348ceb4&req=cigkHsB3lYhWFb4f3HP0gBPMAKNBQtYgtVF7zvLYMQB4%2FVX3iRd8gmuEwc2q%0AHShnV4t0JQfH97ldSA%3D%3D%0A)

Then, the final steps required to start making calls are all on the user level.  
The necessary changes are on the user:

### **User Policy**

* #### **CallingPolicy: Allow Calling**

  This can be done in the Teams Admin center (Teams UI). Create a new Calling Policy in **Voice** > **Calling Policies** according to your needs.

[![Voice &gt; Calling Policies section. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/683899903/6124d3bd40075a0b1de9c4ba/LT_Afl_XcffoD-YhLVF55xOy9nXQPyPPWCFBMFen3odFG-QStn7tM7uQC1isVFaH5E0ln_1LUk02MXW6XC8AIg6b0hdOwlohEbZw8jJQRCfwHO1ZgxxOmMFz3QlMa5PUv7aqyrjS63_cakq7QupS1K4?expires=1781168400&signature=daab6cc6384130b89576ec551f30bc4d68a38de4a31e4bb0ae7b08f21d034c29&req=cigkHsB3lIFcFb4f3HP0gDXQp5vsV8iX9QnJlxa9ZnJ5bhU1FPwdoYXnaCBc%0Am2pWOku1jr2H7cDxFw%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/683899903/6124d3bd40075a0b1de9c4ba/LT_Afl_XcffoD-YhLVF55xOy9nXQPyPPWCFBMFen3odFG-QStn7tM7uQC1isVFaH5E0ln_1LUk02MXW6XC8AIg6b0hdOwlohEbZw8jJQRCfwHO1ZgxxOmMFz3QlMa5PUv7aqyrjS63_cakq7QupS1K4?expires=1781168400&signature=daab6cc6384130b89576ec551f30bc4d68a38de4a31e4bb0ae7b08f21d034c29&req=cigkHsB3lIFcFb4f3HP0gDXQp5vsV8iX9QnJlxa9ZnJ5bhU1FPwdoYXnaCBc%0Am2pWOku1jr2H7cDxFw%3D%3D%0A)

To associate a calling policy to a user go to **Users** > Select the user you want to allow to make calls > **Policies** > **Assigned** **policies** > **Calling policy** > <**Name\_of\_your\_Calling\_Policy**>.

[![Assigned policies section. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/683899905/cc8d3ecf1e482a8b9c044241/bWyI0emcBih4OcCjOcR1Fhy1qZkv7kkQmJrPlm-6N3WpBbIHAeX4ZweAcB6roNGRmd8pt6Glalnx9wlE4Th-NO2G1yF9ozdtTLCIHUasKetXxn-SaOeHl6WDfL-aPONZ7pipYe-H5iIGW0mpqOVk14U?expires=1781168400&signature=a893c702376c5f07477d60dd18599ba07a9b4d1f4b06b6628f30619e544656ba&req=cigkHsB3lIFaFb4f3HP0gBxscZNvywAckyP8etLbyFXvahpJ7%2BQeZ7xM1BC8%0A0Tduod7RSTI5SDaMWA%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/683899905/cc8d3ecf1e482a8b9c044241/bWyI0emcBih4OcCjOcR1Fhy1qZkv7kkQmJrPlm-6N3WpBbIHAeX4ZweAcB6roNGRmd8pt6Glalnx9wlE4Th-NO2G1yF9ozdtTLCIHUasKetXxn-SaOeHl6WDfL-aPONZ7pipYe-H5iIGW0mpqOVk14U?expires=1781168400&signature=a893c702376c5f07477d60dd18599ba07a9b4d1f4b06b6628f30619e544656ba&req=cigkHsB3lIFaFb4f3HP0gBxscZNvywAckyP8etLbyFXvahpJ7%2BQeZ7xM1BC8%0A0Tduod7RSTI5SDaMWA%3D%3D%0A)

* #### **DialPlan:**

Create a new Dialplan in **Voice** > **Dial** **Plans** according to your needs.

[![Voice &gt; Dial Plans section. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/683899911/359db7bd24e31ddcc05ca17e/ww9KCALbjhUxkSVDrU2Jmg33Q1ybgM54-DdXRKH1N0OIKH1kJjRwqG7i5tDKknNdgyx2Z-OTA2MWhN3vET-uWO2sYdc_inCIcdFDXTLva-k_HZVq8CYms0f1j8XQ_mmRB-1x8j388ggX_WCtbrJi9eM?expires=1781168400&signature=028b20ac3864c7eb30c1cfa0ff1eb70ff5a4a8eca5ca06420ff5328deb01ab99&req=cigkHsB3lIBeFb4f3HP0gAh1Ovm4qMoqvEdOuRFQWvvtIQLvW730OAcQ32zP%0Aya5IEq3StWftZ%2B7xog%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/683899911/359db7bd24e31ddcc05ca17e/ww9KCALbjhUxkSVDrU2Jmg33Q1ybgM54-DdXRKH1N0OIKH1kJjRwqG7i5tDKknNdgyx2Z-OTA2MWhN3vET-uWO2sYdc_inCIcdFDXTLva-k_HZVq8CYms0f1j8XQ_mmRB-1x8j388ggX_WCtbrJi9eM?expires=1781168400&signature=028b20ac3864c7eb30c1cfa0ff1eb70ff5a4a8eca5ca06420ff5328deb01ab99&req=cigkHsB3lIBeFb4f3HP0gAh1Ovm4qMoqvEdOuRFQWvvtIQLvW730OAcQ32zP%0Aya5IEq3StWftZ%2B7xog%3D%3D%0A)

Then associate it to the desired user in **Users** > Select the user you want to allow to make calls > **Policies** > **Assigned policies** > **Dial plan** > <**Your\_Dial\_Plan\_Name**>

[![Dial plan name section. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/683899914/7e8c57fe162d07d7fefad7e5/bAYjubhbgK5vDWDbGtrCBq4WErzjKsxn7fx_2KRs5-guMiEniREUNm93HbZ3UKvkMzEC_gChVwsTWHB0iM7bTvQn91md9bhudRR5RsEFWlqTZ1QB9yHOSVub1GbENwWQSFz0Fk2Ugvmse_kjqeb7JCU?expires=1781168400&signature=d8a397be33f673a6038e4a382b0f6bb7a21eab4196542e2a712c916196241da7&req=cigkHsB3lIBbFb4f3HP0gOrtzdDo6YD3f78yZQDbwjflVDr0cGXa%2F%2B5WOuzv%0ABSj7dS6kvuKkeWwwTg%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/683899914/7e8c57fe162d07d7fefad7e5/bAYjubhbgK5vDWDbGtrCBq4WErzjKsxn7fx_2KRs5-guMiEniREUNm93HbZ3UKvkMzEC_gChVwsTWHB0iM7bTvQn91md9bhudRR5RsEFWlqTZ1QB9yHOSVub1GbENwWQSFz0Fk2Ugvmse_kjqeb7JCU?expires=1781168400&signature=d8a397be33f673a6038e4a382b0f6bb7a21eab4196542e2a712c916196241da7&req=cigkHsB3lIBbFb4f3HP0gOrtzdDo6YD3f78yZQDbwjflVDr0cGXa%2F%2B5WOuzv%0ABSj7dS6kvuKkeWwwTg%3D%3D%0A)

* #### **Voice routing policy:**

This one is the one we created in PowerShell, which can also be consulted in **Voice** > **Voice Routing Policies**

Associate it to the user in **Users** > Select the user you want to allow to make calls > **Policies** > **Assigned policies** > **Voice Routing Policy** > <**Your\_Voice\_Routing\_Policy\_Name**>

[![Voice routing policy section. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/683899922/13e28ddaa518798a5581d92b/4SwXXhNnbqGivir9BSloOHiNRrSKU5WdVJIJBqwz_mB95eSKwBuZwrZX1q2EgzM2tCievKQ-G8hb2QQLMr802yjtsYkRyryTXz6H1HeM3pxx5OokV1zprJ-ovSEcyqw4I-5jOPmZ54KJmQGid_I2EmM?expires=1781168400&signature=a763f68b3cd7c426241e5daa638a96eb332da96c1d72c48bef913c42ecff5e57&req=cigkHsB3lINdFb4f3HP0gFC%2B9L9OB1Vi5wB3Q9t9pA3MUeGOGUQBV6JmtMxl%0ArkaDjJlE90%2BGFE0qjQ%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/683899922/13e28ddaa518798a5581d92b/4SwXXhNnbqGivir9BSloOHiNRrSKU5WdVJIJBqwz_mB95eSKwBuZwrZX1q2EgzM2tCievKQ-G8hb2QQLMr802yjtsYkRyryTXz6H1HeM3pxx5OokV1zprJ-ovSEcyqw4I-5jOPmZ54KJmQGid_I2EmM?expires=1781168400&signature=a763f68b3cd7c426241e5daa638a96eb332da96c1d72c48bef913c42ecff5e57&req=cigkHsB3lINdFb4f3HP0gFC%2B9L9OB1Vi5wB3Q9t9pA3MUeGOGUQBV6JmtMxl%0ArkaDjJlE90%2BGFE0qjQ%3D%3D%0A)

#### Ensure the user is enabled for Enterprise Voice with a Direct Routing Phone Number.

#### To ensure that the user which you intend to make calls over Direct Routing has all the proper configurations in place, run the following command in Powershell:

```
Get-CsOnlineUser -Identity "<user_email>"
```

#### Below you can find an example of an expected output is:

```
PS /Users/rita> Get-CsOnlineUser -Identity "rabbani@rita.mstsbc.telnyx.tech"  
AccountEnabled                         : TrueAlias                                  : rabbaniApplicationAccessPolicy                :AssignedPlan                           : {MCOProfessional, MCOMEETADD, MCOEV, Teams}CallingLineIdentity                    :City                                   :Company                                :Country                                :CountryAbbreviation                    :Department                             :DialPlan                               : PTDisplayName                            : RabbaniEnterpriseVoiceEnabled                 : TrueExternalAccessPolicy                   :FeatureTypes                           : {AudioConferencing, PhoneSystem, Teams}GivenName                              : RabbaniHideFromAddressLists                   :   
FalseHostingProvider                        : sipfed.online.lync.comIdentity                               : 34eac5d7-a18b-41b6-853d-c3432252654cInterpretedUserType                    : PureOnlineTeamsOnlyUserIsSipEnabled                           : TrueLastName                               :LastSyncTimeStamp                      : 31/01/2023 09:32:28LineUri                                : tel:+18772404795LocationPolicy                         :OnPremEnterpriseVoiceEnabled           : FalseOnPremHostingProvider
```

#### #

```
     :
```

#### #

```
FalseTeamsUpgradeOverridePolicy             :TeamsUpgradePolicy                     : UpgradeToTeamsTeamsUpgradePolicyIsReadOnly           : ModeAndNotificationsTeamsVdiPolicy                         :TeamsVerticalPackagePolicy             :TeamsVideoInteropServicePolicy         :TenantDialPlan                         : RITE-DPTenantId                               : 0fb5c7fa-614f-4ab2-b4b7-37d99c515524Title                                  :UsageLocation                          : PTUserDirSyncEnabled                     :UserPrincipalName                      : rabbani@rita.mstsbc.telnyx.techUserValidationErrors                   : {}WhenChanged                            : 31/01/2023 09:32:29WhenCreated                            : 23/01/2023 13:04:17LastProvisionTimeStamps                : {[UserAuthoredProps, 2023-01-31T09:32:03.1286014+00:00]}LastPublishTimeStamps                  : {[ProvisionedPlanPublishAuthoredProps, 2023-01-23T13:04:36.7381079+00:00],                                         [UserEventDistributionProcessor, 2023-01-23T13:04:45.8365073+00:00],                                         [PublishUserCloudAttributesProcessor, 2023-01-31T09:32:04.0575536+00:00],                                         [UpdateBvdUserProcessor, 2023-01-31T09:32:06.9756276+00:00]…}
```

#### **If you encounter a similar output (with the appropriate names, times, and regions), please note that it may take up to 30 minutes for the changes to be fully implemented and take effect.**

#### **After this period, everything should be working as intended.**

---

Related Articles

[SIP Connection: Settings](https://support.telnyx.com/en/articles/4351104-sip-connection-settings)[Telnyx SIP Response Codes](https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes)[Configuring Telnyx with Microsoft Teams Direct Routing](https://support.telnyx.com/en/articles/5253876-configuring-telnyx-with-microsoft-teams-direct-routing)[Grandstream UCM6xxx: SIP Trunks](https://support.telnyx.com/en/articles/5748258-grandstream-ucm6xxx-sip-trunks)[Wildix: SIP Trunk Setup](https://support.telnyx.com/en/articles/5799830-wildix-sip-trunk-setup)

Did this answer your question?

😞😐😃

Table of contents
