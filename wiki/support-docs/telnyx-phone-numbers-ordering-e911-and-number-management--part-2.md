---
title: 'Telnyx Phone Numbers: Ordering, E911, and Number Management'
summary: This page consolidates Telnyx guidance on phone number ordering, including
  account verification restrictions, searching and buying numbers, requirement groups,
  working with the numbering team, E911 address registration and setup, testing E911
  with 933, handling spam/scam-likely flags, and managing numbers through the My Numbers
  Page.
sources:
- url: https://support.telnyx.com/en/articles/10715715-phone-number-ordering-restrictions
- url: https://support.telnyx.com/en/articles/1130647-register-e911-addresses
- url: https://support.telnyx.com/en/articles/1130683-e911-setup-guide
- url: https://support.telnyx.com/en/articles/1130709-how-do-i-test-e911-service
- url: https://support.telnyx.com/en/articles/4088988-telnyx-how-to-handle-spam-scam-likely
- url: https://support.telnyx.com/en/articles/4294429-addresses-overview
- url: https://support.telnyx.com/en/articles/4349113-my-numbers-page
- url: https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers
- url: https://support.telnyx.com/en/articles/7205411-numbering-team-best-practices
- url: https://support.telnyx.com/en/articles/9801714-requirement-groups-for-ordering-phone-numbers
updated_at: 2026-07-17T09:01:25Z
---

# Telnyx Phone Numbers: Ordering, E911, and Number Management

*Part 2 of 6 — see also: [Part 1](telnyx-phone-numbers-ordering-e911-and-number-management--part-1.md), [Part 3](telnyx-phone-numbers-ordering-e911-and-number-management--part-3.md), [Part 4](telnyx-phone-numbers-ordering-e911-and-number-management--part-4.md), [Part 5](telnyx-phone-numbers-ordering-e911-and-number-management--part-5.md), [Part 6](telnyx-phone-numbers-ordering-e911-and-number-management--part-6.md)*

This page consolidates Telnyx guidance on phone number ordering, including account verification restrictions, searching and buying numbers, requirement groups, working with the numbering team, E911 address registration and setup, testing E911 with 933, handling spam/scam-likely flags, and managing numbers through the My Numbers Page.

## Requirement Groups

Requirement Groups let you view, manage, and fulfill regulatory requirements in advance for a particular order type. By creating a Requirement Group, you can pre-fill all necessary information and documentation once and reuse it across multiple orders, eliminating the need to re-upload the same requirements for each order.

Requirement Groups are optional in most countries. However, starting September 16, 2024, they are required to order phone numbers in:

- CH (Switzerland)
- DK (Denmark)
- IT (Italy)
- NO (Norway)
- PT (Portugal)
- SE (Sweden)

### Creating and Using a Requirement Group

1. Navigate to the [Requirement Groups page](https://portal.telnyx.com/#/numbers/requirements/requirement-groups) in the portal.
2. Click **New Requirement Group** to open the creation form.
3. Each Requirement Group is valid only for a specific combination of Country, phone_number_type, and type of order. For example, a Portugal local ordering requirement group can only be associated with Portugal local number orders. Specify the country, phone number type, and order type, and optionally add a customer reference.
4. Once created, the Requirement Group displays the expected requirements for the relevant order.
5. Fill out all requirements and click **Submit**.
6. Go to the [Buy Numbers page](https://portal.telnyx.com/#/numbers/buy-numbers) and add matching phone numbers to your cart.
7. In the cart, select the appropriate Requirement Group for each phone number using the Requirement Groups column.
8. Place your order.
9. The requirements from the Requirement Group are automatically added to your order, which then enters review by the Operations team.

Each Requirement Group can be reused for as many orders as needed, provided the country and phone number type match.

## Working with the Numbering Team

### Before Contacting the Numbering Team

1. Search for the number you want in the portal at [portal.telnyx.com](https://portal.telnyx.com/#/voice/my-numbers/buy).
2. If the number is available, purchase it. If unavailable, click the **Request Number** button.
3. After placing an order, two scenarios are possible:
   - **Scenario 1:** The numbers have no ordering requirements, and the order completes momentarily. No further action is needed.
   - **Scenario 2:** The numbers have ordering requirements, and the order transitions to "pending" until you provide additional information.
4. Find your pending order on the [Number Orders page](https://portal.telnyx.com/#/voice/orders) and fulfill any regulatory requirements. Upload ordering requirements within 2 days to avoid auto-cancellation.
5. Once requirements are fulfilled, the request is sent to the numbering team for review and approval. The team will contact you directly if further information is needed. Lead times vary by country and number type.
6. You will receive an update via a comment on the order or by email once the transaction is approved or denied.

### Contacting the Numbering Team

The numbering team is available Monday to Friday, 9am–5pm CT. Messages outside these hours are attended to on the next business day.

You can contact the team in two ways:

- Click the chat icon at the bottom right of the screen when signed into the Portal to open a chat window.
- Send an email to [numbering@telnyx.com](mailto:numbering@telnyx.com).

### Choosing the Right Support Method

- **To request a new number:** Use the numbering request form on the portal.
- **For an update on an existing order:** Use the chat function on the Portal.
- **For urgent issues requiring ticket expediting:** Open a new chat or email [numbering@telnyx.com](mailto:numbering@telnyx.com) during work hours.
- **For document requirements by country:** Search by country on support.telnyx.com.

## E911 Emergency Addresses

The Addresses section of your Telnyx portal account contains addresses used for E911 emergency services and for number ordering regulatory requirements.

### Adding an Address

To find the [Addresses](https://portal.telnyx.com/#/numbers/emergency-addresses) section, click **Numbers** in the left navigation bar, then select **Compliance** from the dropdown. Click the **Emergency Addresses** tab at the top of the page.

When you first visit this page, no addresses are listed. Click **Add Address** in the top right. You can either manually enter all address details or use the built-in address search feature to find your desired address from partial details.

Once created, the address appears in the list on the same page. The list can be filtered to locate specific addresses, and addresses can be deleted. Note: deleting an address associated with a DID for E911 services will make that DID no longer viable for E911 services.

### Registering E911 Addresses

To register an E911 address:

1. Under **Real-Time Communications** in the left sidebar, click **My Numbers** under the Numbers section.
2. Click the [Emergency Address](https://portal.telnyx.com/#/numbers/emergency-addresses) sub-tab.
3. Click **Add Address** on the right.
4. Fill out the form with First Name, Last Name, or Business Name.
5. Use the autocomplete "search for an address" field to auto-search, or manually set Country, State/Province/Region, City, ZIP/Postal Code, Street Address, and Extended Address.

**Note:** Failure to register an address and enable emergency services on numbers used for emergency calls will be considered unregistered and will incur a $100 penalty.

### Activating E911 on a Number

To activate E911 services on a DID with one of your added addresses:

1. Navigate to the [Numbers](https://portal.telnyx.com/#/app/numbers/my-numbers) section of your account.
2. Find your desired DID and enter its settings.
3. Click the **Emergency** tab.
4. Activate Emergency services by checking the box.
5. Select your desired address from the dropdown menu, or enter a new address.
