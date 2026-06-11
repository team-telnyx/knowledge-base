---
source_url: https://support.telnyx.com/en/articles/8103257-global-ip-edge-routing
scraped: 2026-06-11
---

Global IP & Edge Routing | Telnyx Help Center

[Skip to main content](#main-content)

# Global IP & Edge Routing

Step by step process on how to get started with Telnyx Networking via procurement of Global IPs and setting up Global Edge Routing

Written by Telnyx Engineering

October 16, 2025

Table of contents

# Setting up Networking for Global Edge Routing

## **NOTE:** Please note that Global IP for customers is currently disabled. At present there are no plans to re-enable it in the near future. **Step 1. Create a Network**

[![Network creation settings section. ](https://downloads.intercomcdn.com/i/o/779394899/19fe2f5371207f1b7d8c2bef/step1.png?expires=1781168400&signature=66245455a968a050c9c174752372cf0bbc1d3e7aa80f5064aae3fb7c557f1066&req=cycuFcB6lYhWFb4f3HP0gMZtt%2FMfN2yEJBzxbBvaTf7MPGn8Ip%2FyMB4tEaJC%0A59zJAuyTeS46xkl53g%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/779394899/19fe2f5371207f1b7d8c2bef/step1.png?expires=1781168400&signature=66245455a968a050c9c174752372cf0bbc1d3e7aa80f5064aae3fb7c557f1066&req=cycuFcB6lYhWFb4f3HP0gMZtt%2FMfN2yEJBzxbBvaTf7MPGn8Ip%2FyMB4tEaJC%0A59zJAuyTeS46xkl53g%3D%3D%0A)

## **Step 2. Create a WireGuard Interface**

[![Wireguard interface section. ](https://downloads.intercomcdn.com/i/o/779395270/1a3dd33ef65d85b31fede220/step8.png?expires=1781168400&signature=538bbc3d58ae3c1e1b6a81ff4604629a7457f8076885e4fb01cb68149b53d8d1&req=cycuFcB7n4ZfFb4f3HP0gCQ69T%2BlgypHlqfKcxAx2Hbattq%2FgahPjkz2Hhpw%0ARcRC%2FT0H4NytR8eV0A%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/779395270/1a3dd33ef65d85b31fede220/step8.png?expires=1781168400&signature=538bbc3d58ae3c1e1b6a81ff4604629a7457f8076885e4fb01cb68149b53d8d1&req=cycuFcB7n4ZfFb4f3HP0gCQ69T%2BlgypHlqfKcxAx2Hbattq%2FgahPjkz2Hhpw%0ARcRC%2FT0H4NytR8eV0A%3D%3D%0A)

## **Step 3: Wait for WireGuard Interface to finish provisioning**

[![Wireguard interface section. ](https://downloads.intercomcdn.com/i/o/779395272/d58722eb86bb321aa61f3ae5/step7.png?expires=1781168400&signature=a9e1911a3da3b5ed0db8205038f4724887befa0fdfe333908cd7dd8f835d8de8&req=cycuFcB7n4ZdFb4f3HP0gJZvOSsusnxomZrA0IsaLM%2FraByPAUTVcf5nmp7n%0AUe46yYq%2FK7mUrCaUwQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/779395272/d58722eb86bb321aa61f3ae5/step7.png?expires=1781168400&signature=a9e1911a3da3b5ed0db8205038f4724887befa0fdfe333908cd7dd8f835d8de8&req=cycuFcB7n4ZdFb4f3HP0gJZvOSsusnxomZrA0IsaLM%2FraByPAUTVcf5nmp7n%0AUe46yYq%2FK7mUrCaUwQ%3D%3D%0A)

## **Step 4: Create a WireGuard Peer**

[![Wireguard interface section. ](https://downloads.intercomcdn.com/i/o/779395271/e333fcad453bef89918bb61e/step6.png?expires=1781168400&signature=726d32992c61b2c1fc9abab1f4db761fb4375d6117602287ef624bf44e1e329f&req=cycuFcB7n4ZeFb4f3HP0gJjQol7slywDePNn12z4dRufhY3ENBaI3e80YEk3%0AXqGn6f%2F45Ivgvo%2FIzg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/779395271/e333fcad453bef89918bb61e/step6.png?expires=1781168400&signature=726d32992c61b2c1fc9abab1f4db761fb4375d6117602287ef624bf44e1e329f&req=cycuFcB7n4ZeFb4f3HP0gJjQol7slywDePNn12z4dRufhY3ENBaI3e80YEk3%0AXqGn6f%2F45Ivgvo%2FIzg%3D%3D%0A)

## **Step 5: Make note of the Private Key returned**

[![Wireguard interface section for private key. ](https://downloads.intercomcdn.com/i/o/779395269/d84d9d01443421c585c1ed97/step5.png?expires=1781168400&signature=e6b13026eca89d871e349fb4c6dcb70575bfceb8f9ef9c75249c9486742cc1c1&req=cycuFcB7n4dWFb4f3HP0gAnvmfgZUBosoaKUD%2FO73Hc8NP9xVfq%2Fx4H2aurw%0AMhW%2F%2BqkiQOktWvOdYA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/779395269/d84d9d01443421c585c1ed97/step5.png?expires=1781168400&signature=e6b13026eca89d871e349fb4c6dcb70575bfceb8f9ef9c75249c9486742cc1c1&req=cycuFcB7n4dWFb4f3HP0gAnvmfgZUBosoaKUD%2FO73Hc8NP9xVfq%2Fx4H2aurw%0AMhW%2F%2BqkiQOktWvOdYA%3D%3D%0A)

## **Step 6: Acquire Global IP**

[![Wireguard interface section for global IP. ](https://downloads.intercomcdn.com/i/o/779395274/49008aeee5ea138666915c37/step4.png?expires=1781168400&signature=c17d25037dfe22e01322e7d556ef92ae14c2f1030188d688401770b1de549c73&req=cycuFcB7n4ZbFb4f3HP0gDfM0vXskVZxQmOlNLY%2Fxsx9YhiDwpV0QqkrxUj4%0A87PbNM0DtCQKw7Geww%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/779395274/49008aeee5ea138666915c37/step4.png?expires=1781168400&signature=c17d25037dfe22e01322e7d556ef92ae14c2f1030188d688401770b1de549c73&req=cycuFcB7n4ZbFb4f3HP0gDfM0vXskVZxQmOlNLY%2Fxsx9YhiDwpV0QqkrxUj4%0A87PbNM0DtCQKw7Geww%3D%3D%0A)

## **Step 7: Assign WireGuard Peer to Global IP**

[![Wireguard interface section for Wireguard Peer. ](https://downloads.intercomcdn.com/i/o/779395265/6c2d13a8bdf22c2ce4fcd147/step3.png?expires=1781168400&signature=ec9d43bb98597d2c06359e7360173aa7ea010ebdf57878631f0a2b5a0fef6898&req=cycuFcB7n4daFb4f3HP0gJtcOVgcMohzDXkFzRx6oYSL6gig2aqUx7hD5ho9%0ANcUnfx5XL91jufTIyg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/779395265/6c2d13a8bdf22c2ce4fcd147/step3.png?expires=1781168400&signature=ec9d43bb98597d2c06359e7360173aa7ea010ebdf57878631f0a2b5a0fef6898&req=cycuFcB7n4daFb4f3HP0gJtcOVgcMohzDXkFzRx6oYSL6gig2aqUx7hD5ho9%0ANcUnfx5XL91jufTIyg%3D%3D%0A)

## **Step 8: Copy and paste WireGuard config to service VM, using the Private Key in Step 5**

[![Wireguard interface for service VM. ](https://downloads.intercomcdn.com/i/o/779395266/dd79c4bb8009f27d7e3d3eb0/step2.png?expires=1781168400&signature=ed60e4a9bc6b31ab5b9607543b58f4e3c7e6c62120bd0f42856472659a660f78&req=cycuFcB7n4dZFb4f3HP0gPpgq3ccaeZEqFjQOCXycTZRlK%2FBIXG4DvDCZkVF%0APIZTSag%2BYXmHpbZu7Q%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/779395266/dd79c4bb8009f27d7e3d3eb0/step2.png?expires=1781168400&signature=ed60e4a9bc6b31ab5b9607543b58f4e3c7e6c62120bd0f42856472659a660f78&req=cycuFcB7n4dZFb4f3HP0gPpgq3ccaeZEqFjQOCXycTZRlK%2FBIXG4DvDCZkVF%0APIZTSag%2BYXmHpbZu7Q%3D%3D%0A)

---

Related Articles

[FreePBX V14: IP Trunk - ChanSIP](https://support.telnyx.com/en/articles/3284736-freepbx-v14-ip-trunk-chansip)[Positron IP Phone](https://support.telnyx.com/en/articles/5811761-positron-ip-phone)[How to configure Global Edge Router with Telnyx](https://support.telnyx.com/en/articles/8002565-how-to-configure-global-edge-router-with-telnyx)[Telnyx Networking on AWS VPC](https://support.telnyx.com/en/articles/8104309-telnyx-networking-on-aws-vpc)[Intro to Telnyx Edge Router](https://support.telnyx.com/en/articles/8126141-intro-to-telnyx-edge-router)

Did this answer your question?

😞😐😃

Table of contents
