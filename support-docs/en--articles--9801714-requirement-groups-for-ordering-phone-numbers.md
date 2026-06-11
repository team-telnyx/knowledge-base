---
source_url: https://support.telnyx.com/en/articles/9801714-requirement-groups-for-ordering-phone-numbers
scraped: 2026-06-11
---

Requirement Groups for Ordering Phone Numbers | Telnyx Help Center

[Skip to main content](#main-content)

# Requirement Groups for Ordering Phone Numbers

Requirement Groups allow you to view, manage, and fulfill regulatory requirements in advance for a particular order type. Learn more today!

Written by Telnyx Engineering

November 5, 2024

Table of contents

Requirement Groups allow you to view, manage, and fulfill regulatory requirements in advance for a particular order type. By creating a Requirement Group, you can pre-fill all necessary information and documentation just once, and then reuse this group across multiple orders. This eliminates the need to re-upload the same requirements for each order, saving you time and ensuring accuracy.

Requirement Groups are optional in most countries. However, starting September 16, 2024, they will be required to order phone numbers in the following countries:

* CH (Switzerland)
* DK (Denmark)
* IT (Italy)
* NO (Norway)
* PT (Portugal)
* SE (Sweden)

This guide will walk you through how to use Requirement Groups on number orders. We also have a developer guide [here](https://developers.telnyx.com/docs/numbers/phone-numbers/requirement-groups) if you are interested in integrating with Requirement Groups.

---

# How it works:

1. Navigate to the `Requirement Groups` [page in the portal](https://portal.telnyx.com/#/numbers/requirements/requirement-groups).  
   ​

   [![](https://downloads.intercomcdn.com/i/o/1162886745/937f2b43806341471fd3c93d/Screenshot+2024-08-29+at+3_44_06%E2%80%AFPM.png?expires=1781168400&signature=58917b664cd4ae48e3202c14826256bfeac8c1d2671ad6285d978facb7872339&req=dSEhFMF2m4ZbXPMW1HO4zWSixo0KFCLPfK1AqWQm5n2hz9jqDafItdlYYC%2BS%0Ac4yD%0A)](https://downloads.intercomcdn.com/i/o/1162886745/937f2b43806341471fd3c93d/Screenshot+2024-08-29+at+3_44_06%E2%80%AFPM.png?expires=1781168400&signature=58917b664cd4ae48e3202c14826256bfeac8c1d2671ad6285d978facb7872339&req=dSEhFMF2m4ZbXPMW1HO4zWSixo0KFCLPfK1AqWQm5n2hz9jqDafItdlYYC%2BS%0Ac4yD%0A)
2. Click on the `New Requirement Group` button. This will take you to a form where you can create your first requirement group.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/1162888063/bd97a3e6c9eadac86881a408/Screenshot+2024-08-29+at+3_47_08%E2%80%AFPM.png?expires=1781168400&signature=457e141dd200b720a6e3e6c276e4a2b6a843a2bef8cdb2f357edbe242aa6b28e&req=dSEhFMF2lYFZWvMW1HO4zaIoc7VgL3LlOBMt2jBe5NeBvoO7xh7VxleCeKlr%0Atbed%0A)](https://downloads.intercomcdn.com/i/o/1162888063/bd97a3e6c9eadac86881a408/Screenshot+2024-08-29+at+3_47_08%E2%80%AFPM.png?expires=1781168400&signature=457e141dd200b720a6e3e6c276e4a2b6a843a2bef8cdb2f357edbe242aa6b28e&req=dSEhFMF2lYFZWvMW1HO4zaIoc7VgL3LlOBMt2jBe5NeBvoO7xh7VxleCeKlr%0Atbed%0A)
3. Each Requirement Group is only valid for a particular combination of `Country`, `phone_number_type`, and `type of order`. For example a `Portugal` `local` `ordering` requirement group can only be associated with Portugal local number orders. It could not be associated with any other order.   
   ​  
   Please specify the country, phone number type, and order type that you would like to create a requirement group for. For this example, I know that I want to purchase UK mobile numbers, so I am going to create a `UK` `mobile` `ordering` requirement group. I am also going to add a customer reference (optional) so its easy to distinguish this requirement group from my other requirement groups.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/1162895734/8ad3b383129055ce4ac7235c/Screenshot+2024-08-29+at+3_50_35%E2%80%AFPM.png?expires=1781168400&signature=e7e8d7f11e2f892fb59726dcb6a0927948a8f56409a4a52f6bdcb107c7d04025&req=dSEhFMF3mIZcXfMW1HO4zdlKdPUqI37pCMkNMGQUuss9dRFk61IvkC1SNZsi%0Ar%2Fy5%0A)](https://downloads.intercomcdn.com/i/o/1162895734/8ad3b383129055ce4ac7235c/Screenshot+2024-08-29+at+3_50_35%E2%80%AFPM.png?expires=1781168400&signature=e7e8d7f11e2f892fb59726dcb6a0927948a8f56409a4a52f6bdcb107c7d04025&req=dSEhFMF3mIZcXfMW1HO4zdlKdPUqI37pCMkNMGQUuss9dRFk61IvkC1SNZsi%0Ar%2Fy5%0A)
4. Once the Requirement Group is created, it will show the expected requirements for the relevant order. So in this example, my Requirement Group shows the expected requirements for a `UK` `mobile` number order.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/1162900425/3a256e047442ddcf59cb3fc6/Screenshot+2024-08-29+at+3_55_16%E2%80%AFPM.png?expires=1781168400&signature=6334f41f36fd9fdb1c256f3547d1adc6173f95a979ee3a33f3fcdec09fdece96&req=dSEhFMB%2BnYVdXPMW1HO4zTPPauOKper8ZrKccHIOWfssApE62Kt%2FZrw18a%2FG%0AWqZn%0A)](https://downloads.intercomcdn.com/i/o/1162900425/3a256e047442ddcf59cb3fc6/Screenshot+2024-08-29+at+3_55_16%E2%80%AFPM.png?expires=1781168400&signature=6334f41f36fd9fdb1c256f3547d1adc6173f95a979ee3a33f3fcdec09fdece96&req=dSEhFMB%2BnYVdXPMW1HO4zTPPauOKper8ZrKccHIOWfssApE62Kt%2FZrw18a%2FG%0AWqZn%0A)
5. Fill out all of the requirements and click `Submit`.   
   ​

   [![](https://downloads.intercomcdn.com/i/o/1162904336/30362462bc39d18274d38c44/Screenshot+2024-08-29+at+4_01_55%E2%80%AFPM.png?expires=1781168400&signature=7a53ef99ac0d73d536935a68aa8be14f547af3715793a412ae2a4a8d26eb743a&req=dSEhFMB%2BmYJcX%2FMW1HO4zb4yio8h8Yr9KOfWZXVYew2%2FjR8ewOoStzcdqxgd%0A2H1h%0A)](https://downloads.intercomcdn.com/i/o/1162904336/30362462bc39d18274d38c44/Screenshot+2024-08-29+at+4_01_55%E2%80%AFPM.png?expires=1781168400&signature=7a53ef99ac0d73d536935a68aa8be14f547af3715793a412ae2a4a8d26eb743a&req=dSEhFMB%2BmYJcX%2FMW1HO4zb4yio8h8Yr9KOfWZXVYew2%2FjR8ewOoStzcdqxgd%0A2H1h%0A)
6. Go to the `Buy Numbers` page ([here](https://portal.telnyx.com/#/numbers/buy-numbers)) and order the phone number(s) that match the Requirement Group you just created. Add the phone number(s) you would like to purchase to your cart.  
   ​  
   So in this example, I will search and add 3 `UK` `mobile` phone numbers to my cart.  
   ​
7. In the cart, there is a `Requirement Groups` column in the phone number table. For each phone number in your cart, select the appropriate Requirement Group.   
   ​

   [![](https://downloads.intercomcdn.com/i/o/1162911483/a1e05cd73d433f3611a9b477/Screenshot+2024-08-29+at+4_07_05%E2%80%AFPM.png?expires=1781168400&signature=9e53aca0b8cddac10bb7243f9d3f264925f7052758e0773cdbd703c4f5587fd2&req=dSEhFMB%2FnIVXWvMW1HO4zTMu23H42mv35DebFvzVGfytT8hu6WxEzYlCAIKh%0Ab%2BRP%0A)](https://downloads.intercomcdn.com/i/o/1162911483/a1e05cd73d433f3611a9b477/Screenshot+2024-08-29+at+4_07_05%E2%80%AFPM.png?expires=1781168400&signature=9e53aca0b8cddac10bb7243f9d3f264925f7052758e0773cdbd703c4f5587fd2&req=dSEhFMB%2FnIVXWvMW1HO4zTMu23H42mv35DebFvzVGfytT8hu6WxEzYlCAIKh%0Ab%2BRP%0A)

   In this example, I am selecting the `United Kingdom | mobile | Ordering | uk_mobile_1` requirement group for each of my phone numbers. Since that is the Requirement Group I created in steps 3-5 previously.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/1162923472/254b75aa51c2a130aa3f9d58/Screenshot+2024-08-29+at+4_21_17%E2%80%AFPM.png?expires=1781168400&signature=f2e24c45e01d7b1d393ce49895a87680569891e8bbc747aecaaa6ceac04de011&req=dSEhFMB8noVYW%2FMW1HO4zXoyqlBwgZWIv2WBm8XyUL9ZqwR23FbIhV%2BcIrSQ%0Altsa%0A)](https://downloads.intercomcdn.com/i/o/1162923472/254b75aa51c2a130aa3f9d58/Screenshot+2024-08-29+at+4_21_17%E2%80%AFPM.png?expires=1781168400&signature=f2e24c45e01d7b1d393ce49895a87680569891e8bbc747aecaaa6ceac04de011&req=dSEhFMB8noVYW%2FMW1HO4zXoyqlBwgZWIv2WBm8XyUL9ZqwR23FbIhV%2BcIrSQ%0Altsa%0A)
8. Place your order.  
   ​
9. If you view your order, you will see that the requirements from the Requirement Group were automatically added to your order. At which point, your order will be under review by our Operations team.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/1162915315/685ed313775ce2d9638e2bab/Screenshot+2024-08-29+at+4_12_56%E2%80%AFPM.png?expires=1781168400&signature=9e193b86e439aeacccbf409ca24a7ee2ff650eca53ba65c20a269c54699b3661&req=dSEhFMB%2FmIJeXPMW1HO4zYAXu1ebkDRZsobfKqjBOAVr33rWI40NFuKhmtz%2F%0AoVOk%0A)](https://downloads.intercomcdn.com/i/o/1162915315/685ed313775ce2d9638e2bab/Screenshot+2024-08-29+at+4_12_56%E2%80%AFPM.png?expires=1781168400&signature=9e193b86e439aeacccbf409ca24a7ee2ff650eca53ba65c20a269c54699b3661&req=dSEhFMB%2FmIJeXPMW1HO4zYAXu1ebkDRZsobfKqjBOAVr33rWI40NFuKhmtz%2F%0AoVOk%0A)

   ​

And that's all there is to it! You can re-use each Requirement Group for as many orders as you would like (assuming it is the correct country + phone number type).

---

Related Articles

[Portugal DID Requirements](https://support.telnyx.com/en/articles/5466980-portugal-did-requirements)[International Number Requirements Tool](https://support.telnyx.com/en/articles/7003167-international-number-requirements-tool)[Rwanda DID Requirements](https://support.telnyx.com/en/articles/9961409-rwanda-did-requirements)[Zambia DID Requirements](https://support.telnyx.com/en/articles/10058901-zambia-did-requirements)[Phone Number Ordering Restrictions](https://support.telnyx.com/en/articles/10715715-phone-number-ordering-restrictions)

Did this answer your question?

😞😐😃

Table of contents
