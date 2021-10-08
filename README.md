![Screenshotproject](https://res.cloudinary.com/food-channel/image/upload/v1633632716/Screenshot_2021-10-07_at_20.51.38_vbpegh.png)

# MG Brands
### A fourth Milestone Project 

Live Link : https://mg-brands.herokuapp.com/ 

<p><strong>MG Brands </strong> is an e-commerce website application for those who loves Urban fashion. 
 </p>

<p>Inspired by my onlineshop in the Philippines managed by my sister. I have decided my online shop through facebook and Instagram only since the pandemic started. People shop from home due to lockdowns. I guess this is the right time to make a website for my shop and it is perfectly match with the Milestone project 4. 

 This project is designed to demonstrate my capabilities to create a Full Stack web application with the use of [Python3](https://www.python.org/download/releases/3.0/) and [Django](https://www.djangoproject.com/). The project is an e-commerce application which used a Sql type database to store products, users, orders.</p>

# UX 
## User Stories

| As a/an        | I want to...        | So that I can...        |
| ------------- |:-------------:| :-----:|
| SHOPPER| browse all available products on the site | find something to buy. |
|        | filter by product category|easily find what I am interested in.|
|        | search by keywords|find the products faster.|
|        | add and view products in my bag|know how much I am spending.|
|        | get delivery discount|afford toI could save|
|        | see my past orders|track how much I spent and buy some products again.|
|        | sort the products by price|see the expensive/cheapest ones first.|
|        | sort the products by rating|see the quality/review first.|
|        | sort the products by name|find the names easily|
|        | sort the products by category|find which one I am looking for first.|
|        | have my shipping details on my profile|complete my purchase faster.|
|        | view product|read more information about it.|
|        | register/login for an account that stores my info|return and navigate the site faster and more intuitively.|
|        | pay at the website|for a convenient shopping|
| STORE OWNER| manage products to add, edit or/and delete products|add more products, make updates to existing ones and/or delete products.|
|            | view product management visble only to admin|secure every changes in the site.|


## Development Planes

### 1. **_Strategy Plane_**

The Website is being developed as an e-commerce shop. 
It is suitable for all gender and for all ages. It broken into three categories which focused on the following target audiences:
- **Roles:**
     - New Users (Non-Registered)
     - Returning Users (Registered)
     - Admin (Site Management)

The website needs to enable the user to:
- Register/Login to an account
- Create account
- Search product created in the database 
- View products with the following information:
    - by price
    - by rating
    - by category
    - by clothing
- Save and access the product
- Edit product quantity
- Rating view
- Provide payment and save information

### 2. **_Scope Plane_**

Features implemented:

* Ability for the User to register an account.
* Ability for the User to browse products in different categories.
* Ability for the not registered User to browse products in different categories.
* Ability for the registered User to receive confirmation emails for registration and order confirmation.
* Ability for the registered User to browse products in different categories.
* Ability for the registered User to buy products.
* Ability for the registered User to save items.
* Ability for the registered User to delete items.
* Ability for the registered User to view the order history.
* Ability for the registered User to login / logout from the website.
* Ability for any User to search products.
* Ability for any User to modify the cart by removing unwanted products.
* Ability for the Admin to add, edit and update products and category.
* User friendly website.
* Easy to navigate.
* Mobile first design.









### 3. **_Structure_**

* The products are divided in 3 categories: Shoes, Bags and Caps.
* The Equipment category is composed by 3 type of products: Ropes, Helmets and Harnesses.
* The Clothing category is composed by 2 type of products: Shoes and Trousers.
* The Camping category is composed by 2 type of products: Tents and Sleeping bags.
* The Climbing shoes category is composed by 2 type of products: Mens and Women.
* A search function will allow Users to search products.  
* The Categories are accessible from the main page under the search box if clicked a sub menu will open showing the types of products.  
* The Users will be able to access registration, login/logout functionality from the navigation menu.  
* The Users will be able to access the cart from the navigation bar.
* The User will be able to access delivery information, purchase history.
* The registered User to view the order history via the navigation bar under the Account menu.
* Any user will be able to access a contact us page via the footer.

### 4. **_Skeleton_**

* The website will be easy to navigate by having displayed the different pages and sub menus via the navigation bar.
* The User will be able to search the products by using the search bar present throughout the website.
* When browsing the products, the products will be shown in a card like style with pictures and minimum information.
* When clicking on the product's card the product with full information will be shown.
* To register, login and to add delivery informations, forms will be implemented with validations features.
* On the footer a link for directing the Users to the contact page will always be present.
* The contact page will hold a form to contact the developer.
* The logo and "Home" link in the Navigation bar will redirect the Users to the main page and will always be present.
* The shopping cart will display the products added in a card style format.
* The checkout page will show the list of product and the form to add delivery and payment information with validation functionality.

### 5. **_Surface_**

The website uses [Bootstrap](https://getbootstrap.com/) as a framework. Mobile first approach will be use. For the design and look of the website I have taken ideas and styles from Boutique Ado Code Institute tutorial and [Gooutdoors](https://www.gooutdoors.co.uk/) e-commerce.
The color use is mainly grey.
* The color #545659 is used for the main navigation and footer.
* The product bar uses color #9c9c9c.
* When in mobile view main navigation the color #9c9c9c is used. I have decided to change color due to the size of the screen and by having a lighter grey the page is easier to read then using dark grey color #545659.
* The buttons also use color #545659.
* The text inside banners uses 2 colors. Black with in banners with color #9c9c9c and color #fafafa with banner color #545659 to help with contrast.
* The fonts chosen are from [Google Fonts](https://fonts.google.com/) 'Oxygen' and as a back up 'sans-serif'.
* The icons used throughout the web site are from [Fontawesome](https://fontawesome.com/).