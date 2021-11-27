# Test report


[View README.md](README.md)

[View the live project](https://mg-brands.herokuapp.com/)

This document describes testing of the MG Brands E-commerce site against the User Stories mentioned in the ReadMe file, manual tests and other automated tests for code validation and performance.

## User Stories
- browse all available products on the site.

<div><img src="media/testing/Screenshot 2021-10-10 at 13.11.54.png"></div>

- filter by product category.
 
<div><img src="media/testing/Screenshot 2021-10-10 at 13.17.40.png"></div>

- search by keywords.

<div><img src="media/testing/Screenshot 2021-10-10 at 13.19.01.png"></div>

- add products in my bag.

<div><img src="media/testing/Screenshot 2021-10-10 at 13.19.28.png"></div>

- view products in my bag.

<div><img src="media/testing/Screenshot 2021-10-10 at 13.19.49.png"></div>

- get delivery discount.

<div><img src="media/testing/Screenshot 2021-10-10 at 13.20.57.png"></div>

- sort the products by name, category, rating, price .

<div><img src="media/testing/Screenshot 2021-10-10 at 13.38.57.png"></div>

- have my shipping details on my profile.

<div><img src="media/testing/Screenshot 2021-10-10 at 13.25.32.png"></div>

- view product.

<div><img src="media/testing/Screenshot 2021-10-10 at 13.25.59.png"></div>

- register for an account that stores my info.

<div><img src="media/testing/Screenshot 2021-10-10 at 13.26.42.png"></div>

- login for an account that stores my info.

<div><img src="media/testing/Screenshot 2021-10-10 at 13.26.51.png"></div>

- make payments.

<div><img src="media/testing/Screenshot 2021-10-10 at 13.27.43.png"></div>

- manage products to add, edit or/and delete products.

<div><img src="media/testing/Screenshot 2021-10-10 at 13.30.16.png"></div>

- view product management visible only to admin.

<div><img src="media/testing/Screenshot 2021-10-10 at 13.30.44.png"></div>

## **Manual Tests**
The following items have been successfully tested on each page or component:
### Navbar
- Logo link to home page.
- Navbar items and drop-down menus link to correct site page.
- Search box finds items in product title and description by keyword.
- The search box shows an error if no search term entered.
- The Profile/Product Management drop-down menu shows Profile for authenticated users and Product Management for Site Owners.
- The navbar toggler is shown on smaller screen sizes and menu items display correctly.

### Landing
- 'Wear me' button link correctly.

### Products
- All products are displayed correctly at different screen sizes.
- Product number is shown correctly.
- Sort for price, rating, category and name orders items correctly.
- Back to top button works.
- Product cards link through to the product detail page for the product shown.

### Product detail
- Product ID, price category and description are shown correctly.
- The rating is shown correctly.
- Add to Cart and Continue Shopping buttons link correctly.
- Product quantity can adjust correctly.
- Add and keep on Shopping buttons are working.

### Add/Edit/Delete Product
- Add Product form will not submit unless all mandatory fields are completed and valid.
- Images can be added and removed successfully.
- Message is displayed to notify filename to be added for all images.

### Site Owner features
- Add product button is functioning.
- Images can be added.
- Edit and Delete links are shown on product detail page for all products in product listings.
- Delete modal is displayed when Delete link is clicked.

### Profile
- Contact details and delivery address details are pre-populated from Checkout page.
- Contact details and address can be updated via the Update Delivery Info button. 
- Updated contact and address details are displayed on the Checkout page.
- Order History is shown correctly.

<div align="left"><img src="media/testing/Screenshot 2021-10-10 at 13.27.23.png"></div>

- Reference link for each order opens correctly.

### Cart
- Displays product name, quantity and price correctly.
- Quantity is disabled below 1 and above 99 via increment/decrement buttons and manual entry.
- Remove link removes product from cart.
- The sub-total for each size is correct. 
- The sub total for the cart is correct.
- Delivery is shown for orders below 40€ and is removed above that threshold.
- The order total shows correctly including delivery.
- Secure Checkout and Continue Shopping buttons link correctly.

### Checkout
- Pre-populated contact and address details are shown.
- The checkbox to save address details back to the profile works.
- A message is displayed advising the customer the correct amount will be taken from their card.
- The Complete Order button will not submit unless all mandatory fields are complete and valid.
- The card payment box accepts valid card numbers only and displays an error if not.
- The order details shown including number of items, sub-total, delivery and order total is correct.
- Complete Order button submits form and processing graphic is displayed.

### Checkout success
- Order number, date, delivery address, contact and order details are correct.
- Continue shopping button links correctly.
- Order placed successfully and notification is shown.
- Order appears in Admin area.
- Webhook attempts succeed.

### Notifications
- Toast notifications are shown correctly for success, informational purposes and errors.
- Notifications show all products in the cart with the correct price and total.
- The View Cart and Checkout buttons work on the notification.
- The correct number of shopping items are shown in the header.
- Notifications appear in top right corner and scroll with page.
- Notifications are dismissed on click.

## Responsiveness
- As the site has been designed using Bootstrap, it adheres to the Bootstrap grid layout and breakpoints.  Additional media queries have been used to align many aspects of the site including header, images, font-size, images, buttons, etc. 
- The website has been tested across a broad range of physical and virtual desktop, tablet and mobile devices. 

## Issues and Bugs

- Logo disalignment
    fixed it through CSS manually
- Images doesnt show up
    - I have set up back the secret to visible and its works!
- Registering and logging in
    - I followed the LMS to uncomment elements
- Search box
    - I have widened the description to find right tags
- Error in showing countries
    - I have spelled correctly

### Unresolved bugs

- Templates
    - due to lack of time