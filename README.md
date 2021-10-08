![Screenshotproject](https://res.cloudinary.com/food-channel/image/upload/v1633632716/Screenshot_2021-10-07_at_20.51.38_vbpegh.png)

# MG Brands
### A fourth Milestone Project 

Live Link : https://mg-brands.herokuapp.com/ 

<p><strong>MG Brands </strong> is an e-commerce website application for those who loves Urban fashion. 
 </p>

<p>Inspired by my onlineshop in the Philippines managed by my sister. I have decided my online shop through facebook and Instagram only since the pandemic started. People shop from home due to lockdowns. I guess this is the right time to make a website for my shop and it is perfectly match with the Milestone project 4. 

 This project is designed to demonstrate my capabilities to create a Full Stack web application with the use of [Python3](https://www.python.org/download/releases/3.0/) and 
[Django](https://www.djangoproject.com/). The project is an e-commerce application which will be using a Sql type database to store products, users, orders, reviews and wishlists.</p>






## **_UX_**  
### **_Strategy / Site Owner story_**

I have designed this website to allow the User to be able to check and buy climbing equipment. The main users will be climbers and mountain lovers. The User can come to the website and be able to purchase goods without the need of registering. If the User register an account within the website the user will be able to store delivery information to quickly checkout for the next purchases, be able to check an order history, add reviews to products and create a wishlist. For Admin and maintenance purposes an admin account will be created.

#### **_Data schema_**

The database for this project is Sql. Sql works with tables instead of documents like in MongoDb databases.
* For the products of the website I have created 2 tables. One containing the categories of products and the second table containing the products. 
* I have created a Order table to save orders and I have created a OrderLine Item table to save the products in the orders. 
* For the User I have created a table to store information of the user with all the related field necessary for delivery.
* To save the reviews related to one product I have created a table with a User field to connect to the user that created the review and also the products reviewed.
* For the wishlist I have created 2 tables one for the wishlist containing the user and the second one for the wishlist item containing the wishlist and the product needed to create the wishlist.

### **_Scope_**

Features that I want to implement are:

* Ability for the User to browse climbing products in different categories.
* Ability for the not registered User to browse climbing products in different categories.
* Ability for the not registered User to buy climbing products.
* Ability for the User to register an account. 
* Ability for the registered User to receive confirmation emails for registration and order confirmation.
* Ability for the registered User to retrieve lost password for login.
* Ability for the registered User to browse climbing products in different categories.
* Ability for the registered User to buy climbing products.
* Ability for the registered User to save items in the wishlist.
* Ability for the registered User to delete items from the wishlist.
* Ability for the registered User to view the order history.
* Ability for the registered User to login / logout from the website.
* Ability for any User to search products.
* Ability for any User to modify the cart by removing unwanted products.
* Ability for the Admin to add, edit and update products and category.
* Ability for any User to contact the Admin/Developer via the Contact Us page.
* Easy design and navigation.
* Mobile first design.


### **_Structure_**

* The products are divided in 4 categories: Equipment, Clothing, Camping and Climbing shoes.  
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


### **_Skeleton_**

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

### **_Surface_**

The website uses [Bootstrap](https://getbootstrap.com/) as a framework. Mobile first approach will be use. For the design and look of the website I have taken ideas and styles from Boutique Ado Code Institute tutorial and [Gooutdoors](https://www.gooutdoors.co.uk/) e-commerce.
The color use is mainly grey.
* The color #545659 is used for the main navigation and footer.
* The product bar uses color #9c9c9c.
* When in mobile view main navigation the color #9c9c9c is used. I have decided to change color due to the size of the screen and by having a lighter grey the page is easier to read then using dark grey color #545659.
* The buttons also use color #545659.
* The text inside banners uses 2 colors. Black with in banners with color #9c9c9c and color #fafafa with banner color #545659 to help with contrast.
* The fonts chosen are from [Google Fonts](https://fonts.google.com/) 'Oxygen' and as a back up 'sans-serif'.
* The icons used throughout the web site are from [Fontawesome](https://fontawesome.com/).







<a href="#" alt="MG Brands"></a>
# MG Brands
### A fourth Milestone Project 

<p><strong>MG Brands </strong> is an e-commerce website application for those who loves Urban fashion.
 </p>

<p>Inspired by my onlineshop in the Philippines managed by my sister. I have decided my online shop through facebook and Instagram only since the pandemic started. People shop from home due to lockdowns. I guess this is the right time to make a website for my shop and it is perfectly match with the Milestone project 4. </p>

[View the live project here](#)
<hr>

### Table of contents
1. UX
     1. Project Goals
     2. User Stories
     3. Development Planes
2. Data Schema
     1. Categories Collection
     2. Users Collection
3. Features to Implement in the future
4. Issues and Bugs
5. Technologies used
     1. Languages
     2. Tools
     3. Libraries
     4. Database Management
6. Testing
7. Deployment
     1. Database Creation
     2. Local Copy Creation
     3. Heroku App Creation
8. Credits
9. Acknowledgements
10. Technical Support
***

# UX 
## Project Goals
The primary goal of **MG Brands** is to provide a n e-commerce website, that is simplistic and user friendly design, 
that allows users to **create**, **read**, **update**, **delete**, and **search** their orders. Users can add, update, remove orders from shopping cart. Users can make payments as well with secure check out after shopping.

This is the fourth of Milestone Project that the developer student must complete during their Full Stack Web Development 
Program at The Code Institute and the main requirements is to build a full-stack website allowing users to manage a common dataset using 
**HTML5**, **CSS3**, **JavaScript**, **Python**, and **Django**.

#### User Goals
The user is looking for:
- easy navigation throughout the site
- Mobile friendly site
- A searchable database.
- Create a user account.
- An easy-to-use dataset management system with **CRUD** conventions
- Add, update, remove items from the shopping cart.
- Secure payment.

#### Developer / Site Owner Goals
The Developer is looking to:

- Create a user-friendly website for users to enjoy while shopping
- Demonstrate their proficiency in a variety of software development skills, using newly learned languages and libraries as well as a document database system.
- Deploy a project they are proud of, and excited to have, on their portfolio.

## User Stories
**As a General User, I want to:**

1. Create, Read, Update, Delete account and find them on the database. 
2. add items to shopping bag
3. View items in the bag and adjust them.
4. Provide secure payment.
5. See total of shopping bag.
6. Checkout using credit/debit card.
7. Be notified if my card info is invalid.

**As a Non-Registered User, I want to:**

1. Navigate to Sign-Up page to Register an account.

**As a Registered User, I want to:**

1. Log into my account.
2. Navigate to my orders.

**As an Admin, I want to:**

1. View, manage website and should be only visible to admin.


## Development Planes

***1. Strategy Plane*** 

***2. Scope Plane*** 

***3. Structure Plane*** 

***4. Skeleton Plane*** 

***5. Surface Plane*** 

## Issues and Bugs 


## Technologies Used
### Languages
- [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wiki")
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets "Link to CSS Wiki")
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript "Link to JavaScript Wiki")
- [Python](https://www.python.org/ "Link to Python Homepage")

### Tools
- [Git](https://git-scm.com/ "Link to Git homepage")
     - Git was used for version control to commit to Git and push to Heroku.
- [GitHub](https://github.com/ "Link to GitHub")
     - GitHub was used to store the project repository, after pushing.
- [Heroku](https://id.heroku.com/login "Link to Heroku login page")
     -  Heroku was used in order to deploy the website.
- [Balsamiq](https://balsamiq.com/" Link to Balsamiq homepage")
     - Figma was used to create the wireframes during the design phase of the project.
- [Am I Responsive?](http://ami.responsivedesign.is/# "Link to Am I Responsive Homepage")
     - Am I Responsive was used in order to validate the responsiveness of the design, and to generate mockup imagery to be used.
- [COLOORS](https://coolors.co/ "Link to COLOORS homepage")
     - COLOORS is a  colour picker tool and created image out of it.
- [Unsplash](https://unsplash.com/ "LINK TO COLOORS") 
     - Unsplash was used for images.
- [Cloudinary](https://cloudinary.com/ "Link to Cloudinary site")
     - Cloudinary is being used to access the image through cloud and edited the images as well using it.
- [Font Awesome](https://fontawesome.com/ "Link to Font Awesome site")
     - Font Awesome was used in conjunction with Iconify for icons used throughout the website.


### Libraries


[Back to top ⇧](#table-of-contents)

## Testing


## Deployment


[Back to top ⇧](#table-of-contents)

## Credits 

## Acknowledgements 

[Back to top ⇧](#table-of-contents)

***

## Technical Support


# Note to the Assesor

[Back to top ⇧](#table-of-contents)

*** 