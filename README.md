# Planning Phase

## User Experience (UX)

### *Site Objective*

The Electronics Shop website is a fictional B2C implemented with Django, Python, HTML, and CSS and aims to expand our market base and provide easily accessible information on what our company stands for.

The user can access the products and make purchases (if logged in), and make their reviews and ratings.

The deployed site can be visited here: [ElectroShop](https://app-electro.herokuapp.com/)

![Mock Up](/electroshop/docs/mockup.png)




### *Scope*

To create a minimum functional E-commerce site, The below must be prioritiesed :

* Full CRUD Functionality.
* User login/register.
* Checkout system.
* Account profile.
* Mailing list.
* Product Filters/searching.
* Stripe payments.
* SEO language throughout.
* Order History.
* Social Media page.
* User feedback.
* Saved customer details on checkout.


To enhance user experience and increase site functionality, the below should be addressed:

* Product testimonials and comments.
* Admin can add/remove products.
* Delivery information.
* Terms and conditions.


### *Agile Methodologies*

The Agile Methodology was used to plan this project. This was implemented through Github and the Project Board, which can be seen here - [Project Dashboard](https://github.com/users/MuttiD/projects/5/views/1)

Through the use of the Kanban board in the projects view in Github, the project was divided into five Milestones, which helped me to oversee the completion of the tasks:

* Project Vision and Initial Planning

* Sprint 1 - User Registration

* Sprint 2 - Product Catalog

* Sprint 3 - Shopping Cart and Payment Processing

* Sprint 4 - User Reviews and Final Testing


![Dashboard](/electroshop/docs/dashboard_kanban.png)

Github issues were used to create User Stories and any other Fixes or Updates for the project. This is where the project user was assigned; labels were added to show at a glance importance of tasks and help prioritize jobs. User Stories and Site Owner Stories were added to the appropriate Iteration and the project.


### *User and Site Owner Stories*

#### ```[MILESTONE 1]``` Project Vision and Initial Planning

As a **USER**, I want to... 
* ...be able to **browse and purchase electronics online** so that I can conveniently **shop for gadgets**.
* ...**easily see the purpose of the site** from the landing page so that **I can see if the site is relevant to my needs**.

As a **SITE OWNER**, I want to... 
* ...**establish an online electronics store** to **expand our market reach and increase sales revenue**.
* ...**create a site document in the form as a Readme File** so that I can demonstrate **achievements and test performances of the website** and its general quality;
    Also, it will have **UX design work** undertaken for this project, including any **wireframes, mockups, diagrams**, etc., created as part of the design process and its reasoning.
* ...**create a Facebook Page** so that **I can direct user queries to the website**.
* ...**Include a sitemap to allow search engine bot** crawling as well as a **robots.txt file** to control search engine bot crawling
* ...**add a signup form** so that **customers will be notified when new deals and promotions are applied**.
* ...all these **functionalities are successfuly implemented: create, select/read, update, delete**.



#### ```[MILESTONE 2]``` Sprint 1 - User Registration

As a **USER**, I want to... 
* ...**create an account** with my email and password so that I can **save my information for future purchases**.
* ...**log in to my account** with my email and password to **access my saved information**.
* ...**receive a confirmation email** after registering to **verify my account**.

As a **SITE OWNER**, I want (to)... 
* ...**users to be able to create accounts** easily to **collect customer data for marketing and future analysis**.


#### ```[MILESTONE 3]``` Sprint 2 - Product Catalog

As a **USER**, I want to... 
* ...**view a list of electronics** products with images, short descriptions, and prices.
* ...**filter products by category** on drop down menus to **find what I'm looking for**.
* ...**search for products** by keywords or brand names.

As a **SITE OWNER**, I want to... 
* ...**showcase our product catalog** effectively with appealing images, detailed descriptions, and competitive pricing to **attract and retain customers**.
* ...**add products with descriptions, prices and pictures to the database**;


#### ```[MILESTONE 4]``` Sprint 3 - Shopping Cart and Payment Processing

As a **USER**, I want to... 
* ...**add items to my shopping cart** and see a **summary of my selected products**.
* ...**proceed to checkout** from my shopping cart and **enter my payment information securely**.
* ...**receive an order confirmation email** after successfully completing a purchase.
* ...**be able to remove and update items** to cart and **process payment accordingly**.
* ...**see if the product I am interested in have a full description and ratings**, **its price and the option to aldd it to my cart**;

As a **SITE OWNER**, I want to... 
* ...**streamline the checkout process** to **minimize cart abandonment and maximize conversions**.


#### ```[MILESTONE 5]``` Sprint 4 - User Reviews and Final Testing

As a **USER**, I want to... 
* ...**read and submit reviews** for products I've purchased.
* ...**rate products** and see the ratings in product listings (testimonials).

As a **SITE OWNER**, I want to... 
* ...**encourage user engagement** by allowing reviews and ratings on products, which can **enhance trust and customer loyalty**.
* ...**include al 404 response page** so that **users clearly understand if an error occurs** when using the site and they can easily navigate back again.
* ...**ensure all tests HTML, CSS and Python** passed

# Skeleton

## Wireframes
Wireframes were created using Miro to visualize how the site would look and function. 

Included below are the main wireframes used to plan the site's layout, in which de secondary sites were derived (not shown all of them).


**HOME**

![Home](/electroshop/docs/miro_home.png)

**PRODUCTS CATALOG**

![Catalog](/electroshop/docs/miro_product_catal.png)


**PRODUCTS DETAIL**

![ProductDetail](/electroshop/docs/miro_product_detail.png)


**SHOPPING BAG**

![ShoppingBag](/electroshop/docs/miro_shopping_bag.png)


**CHECKOUT**

![Checkout](/electroshop/docs/miro_checkout.png)


## Color

The main color used in the project was #165F16 alongside with white and it passed on the color analyser, as shown below.

![color](/electroshop/docs/color%20contrast%20analyser.png)

# Features

## Home

**NAVIGAITON BAR**

It comprises search box, account and bags display and drop-down menus where the user can navigate straight to the product he is interested.

Note that in the menus, the user can filter the catalog of products by price, rating, category.

They can also filter by:

* Categories:
    * Components
    * Boards
    * Special Offers

and 

* Subcategories:
    * Components:
        * Microchips
        * Capacitors
        * Connectors
    * Boards:
        * Motherboards
        * Video Boards
    * Special Offers
        * New Arrivals
        * Deals
        * Clearance

<br>
![navbar](/electroshop/docs/nav_bar.png)

**FRONT PAGE**

![frontpage](/electroshop/docs/front_page.png)

**MAILER LITE - NEWSLETTER**

At first I was considering using mail chimp for the newsletter but as I was struggling to make the subscribers appears in the chimp dashboard, at last minute I changed to Mailer Lite services, which is very similar and will do the job.

![newsletter](/electroshop/docs/newsletter.png)

![Subscribers](/electroshop/docs/subscribers_mailer2.png)

**FOOTER**

The footer comprises links to Privacy Policy, Home and Contact Us Pages. 
The icon (font awesome) for Twitter was updated from its original logo recently and it is placed here.

![footer](/electroshop/docs/footer.png)



## Product Catalog

The product catalog is nothing more than a list of all the products (electronics) contents in the site.
As there are over 10 products as of today, and to facilitate navigation avoiding scrowling to the top, it was placed a little green arrow in the bottom right of the page, once you click on it, it will go stright to the top of the page.

![ProductList](/electroshop/docs/product_list.png)

## Product Detail

In this page, the user will have a nice description of the product he is interested in.

![ProductDetail](/electroshop/docs/detail_product.png)

## Sign Up Page and confirmation of Accounts

In this page, the user can create their own account and receive an email confirmation establishing they could buy products and make comments, once they are logged in.

![SignUp](/electroshop/docs/signup.png)

![Email](/electroshop/docs/account_create_email.png)

![Confirmation](/electroshop/docs/email_conf_success.jpg)

## Login Page

![Login](/electroshop/docs/signin.png)

## Profile Page

In the profile page, the user will have a history of all the orders that they have made, and also make updates on their profile information.

![Profile](/electroshop/docs/profile.png)


## Logout Page

![Logout](/electroshop/docs/signout.png)


## Shopping Bag and Check Out Pages

In this page, the user will have the opportunity to make modifications of their quantities, for example, to update and remove it from the bag.

![ShoppingBag](/electroshop/docs/shopping_bag2.png)

![Bag](/electroshop/docs/shopping_bag3.png)

In the checkout page, the user can fill the form putting their data as well as the card details.

![Checkout](/electroshop/docs/checkout_page.png)

The image below confirms that the order has been placed once the instances and payment process on Stripe has been succeeded.

![Order Success](/electroshop/docs/checkout_order_success.png)


## Create, Upgrade or Delete a Comment

The user, once logged in, besides making order for products of their interests, can also make comments, save, update and delete, very simplistic.

There are opportunities for improvements in this session.

![Comment](/electroshop/docs/add_del_upgrade_comment.png)

## Make a Testimonial and score a Rating

The user that is not authenticated can make also their own testimonial, rating the products of their own way by overal, quality and delivery services of the site.

![Testimonial](/electroshop/docs/create_testimonial.png)


## Contact Us Page

![ContactUs](/electroshop/docs/contact_us.png)

## 404 Error Page

![404](/electroshop/docs/404.png)


# Web Marketing Strategy

## SEO Consideration

Effective SEO research is essential for boosting website traffic through browser-based searches, such as on Google. To enhance search engine ranking, I've meticulously crafted individual titles for the project, and the site is equipped with meta tags containing concise descriptions and relevant keywords that encapsulate the overall content and focus of this B2C platform.

### Keyword Research

Prior to developing the Wireframes, I conducted thorough keyword research to gain insights into the topics and categories that users typically search for when shopping for elecronics and related products online. Subsequently, I researched these words utilizing wordtracker.com, I assessed the competitiveness, relevance, authority, and trustworthiness of these keywords.

The resulting findings, outlined below, significantly contributed to establishing effective naming conventions and crafting compelling descriptions for products and page URLs, ultimately enhancing the site's overall searchability.

Short-tail Keywords

* Robotics
* Automation
* PLC
* PC/LAPTOP
* GAME
* Microchips
* Connectors
* MotherBoards
* Videoboards
* Capacitors

Long-tail Keywords

* electronics parts
* electronics stores
* electronics shop near me
* electronics shop online shopping
* electronic components shop
* new electronics

### SiteMap XML

Moreover, to facilitate search engine crawling of the website, I've integrated an XML sitemap file into the main root directory. This file was generated using the complimentary service provided by XML-Sitemaps.com. A sitemap serves as an organizational tool for a website, delineating the URLs and associated data within each section. While sitemaps were historically crafted with a user-centric approach, Google's XML format specifically caters to search engines, enabling them to locate and index data more swiftly and efficiently.

In addition, a robots.txt file has been incorporated into the build to instruct search engine crawlers on which URLs they are permitted to access on the site. This measure is implemented primarily to prevent overloading the site with excessive requests.

![Sitemap](/electroshop/docs/site_map.png)


### Mailer Lite Newsletter

To facilitate communication between the business and its customers for promoting products and events through digital marketing, I've established a partnership with Mailer Lite. 

Upon submission, a success message is promptly displayed to express gratitude for their subscription.

### Facebook Page

To further boost website traffic, a Facebook page has been established to showcase information about the products and the family-run business. This platform serves as an additional avenue for engaging with potential customers and providing insights into the offerings and the ethos of the business.

![FacebookPage](/electroshop/docs/facebook_page.png)


### Meta Data

Metadata has been strategically incorporated within the HTML head element to enhance website traffic. Furthermore, each site page is aptly titled, serving as an additional method to guide users and inform them of their specific location on the site. This dual approach contributes to a more navigable and user-friendly experience, ultimately supporting increased traffic.

# Technologies Used

* [Python](https://www.python.org/). Used as the main backend langague for this project.

* [Django](https://www.djangoproject.com/). Django was used as the python framework in the project.

* [Heroku](https://www.heroku.com/). Used to deploy the page and make it publicly available.

* [ElephantSQL](https://www.elephantsql.com/). Used for the database during deployment.

* SQLlite3. Was used during development as a database to test models.

* [HTML5](https://www.geeksforgeeks.org/html5-introduction/) Was the base language used to lay out the skeleton of all templates.

* [CSS](https://www.tutorialspoint.com/css/css3_tutorial.htm). Was used to style the page.

* [Javascript](https://www.tutorialspoint.com/javascript/index.htm). To manipulate the DOM.

* [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/). Used to style HTML, CSS, minor javascript.

* [Font awesome](https://fontawesome.com/). All icons throughout the page.

* [AWS S3](https://aws.amazon.com/s3/). Used to store static and media files.

* [Stripe](https://stripe.com/ie). Used to handle payments.

* [Miro](https://miro.com/) was used to create the wireframes.

* [GitHub](https://github.com/) was used to store my repository.

* Fonts were taken from [Google Fonts](https://fonts.google.com/).

* [MailerLite](https://www.mailerlite.com/) was used for the newsletter.

* [TinyPNG](https://tinypng.com/) for compress image size.




# Testing

In the pursuit of an approach to development and deployment, I have opted for manual testing for the MVP. This testing process is designed to verify that the deployed site aligns seamlessly with the developmental version, encompassing the following comprehensive aspects:

1. **User Stories:** Validation to ensure that the user requirements have been effectively delivered for the MVP release.

2. **Page Validation:** Verification that all features and links across the site are functioning as intended and developed.

3. **Responsiveness:** Ensuring each page is responsive across various devices through three media queries, covering mobiles, tablets-laptops, and desktop monitors.

4. **Performance:** Utilizing Chrome's developer tool 'Lighthouse Testing' to evaluate pages for performance, best practices, SEO, and accessibility.

5. **Code Validation:** Ensuring the code base is validated using industry-standard tools for HTML, CSS, and Python code, maintaining high-quality coding practices.



## Validation

### User and Site Owner Story Testing
<br>
**Project Vision and Initial Planning**


| USER                                    | Results   | Comments                                 |
| --------------------------------------- | --------- | ---------------------------------------- |
| browse and purchase electronics online  | PASS      | landing page, catalogs and details       |
| easily see the purpose of the site      | PASS      | front page with banners and messages     |


| SITE OWNER                              | Results   | Comments                                 |
| --------------------------------------- | --------- | ---------------------------------------- |
| establish an online electronics store   | PASS      | all purchases functionalities working    |
| create Readme File and UX design work   | PASS      | it has been created                      |
| Include a sitemap and Robots.txt file   | PASS      | it has been included both                |
| add a signup form                       | PASS      | it has added                             |
| Add CRUD functionalities                | PASS      | users can manage CRUD in bag and profiles|

<br>
**Sprint 1 - User Registration**


| USER                                    | Results   | Comments                                 |
| --------------------------------------- | --------- | ---------------------------------------- |
| create an account                       | PASS      | users can create account <sign up form>  |
| log in to my account                    | PASS      | users and admins can login               |
| receive a confirmation email            | PASS      | real emails can be received by users     |


| SITE OWNER                              | Results   | Comments                                 |
| --------------------------------------- | --------- | ---------------------------------------- |
| users to be able to create accounts     | PASS      | users can create account                 |
 
<br>
**Sprint 2 - Product Catalog**


| USER                                    | Results   | Comments                                 |
| --------------------------------------- | --------- | ---------------------------------------- |
| view a list of electronics              | PASS      | catalog is in "All Products"             |
| filter products by category             | PASS      | drop-down <sort feature>                 |
| search for products                     | PASS      | search for a keyword at nav-bar          |


| SITE OWNER                              | Results   | Comments                                 |
| --------------------------------------- | --------- | ---------------------------------------- |
| showcase our product catalog            | PASS      | it has been shown in Products page       |
| add products (prices, pictures, descr.) | PASS      | admin can add products once logged in    |


<br>
**Sprint 3 - Shopping Cart and Payment Processing**


| USER                                    | Results   | Comments                                 |
| --------------------------------------- | --------- | ---------------------------------------- |
| add items to my shopping bag            | PASS      | in shopping bag area                     |
| proceed to checkout                     | PASS      | users will see a summary of products     |
| receive an order confirmation email     | PASS      | order receipt confirmation               |
| be able to remove and update items      | PASS      | users can add, subtract and remove items |
| see products have a full description    | PASS      | they can see in product detail page      |


| SITE OWNER                              | Results   | Comments                                 |
| --------------------------------------- | --------- | ---------------------------------------- |
| streamline the checkout process         | PASS      | checkput process orders with Stripe      |

<br>
**Sprint 4 - User Reviews and Final Testing**

| USER                                    | Results   | Comments                                 | 
| --------------------------------------- | --------- | ---------------------------------------- |
| read and submit reviews                 | PASS      | They can make comments and testimonials  |
| rate products                           | PASS      | quality, overall, delivery features (1-5)|



| SITE OWNER                              | Results   | Comments                                 |
| --------------------------------------- | --------- | ---------------------------------------- |
| encourage user engagement               | PASS      | banners, newsletter, messages features   |
| include al 404 response page            | FAIL      | not rendering in mobile size             |
| ensure all tests passed                 | FAIL      | HTML failed in 2no errors                |



### HTML

In the frst trial, HTML checker found eleven errors and I managed to sort nine of them, but I have not been able to address the two remaining errors encountered in the HTML checker.

![HTML-11errors](/electroshop/docs/html%20checker.png)

![HTML-02errors](/electroshop/docs/html%20checker%202.png)

### CSS

![CSS](/electroshop/docs/css%20validator.png)

### Python

All Python .py files have been submitted to the Code Institute PEP8 checker and all passed.

[CI PEP8](https://pep8ci.herokuapp.com/)

### LightHouse



### Browsers

All sites were tested in Google Chrome and Microsoft Edge and passed.

Functionalities tested:

* clicks
* links
* renderization
* shopping bag and checkout pages
* drop-down menus
* searching
* filtering
* forms


### Responsiveness

Media Queries worked well in screen sizes for all devices, including monitors, tablets and mobiles


<br>

## Remaining Issues

* 404 error page not been rendered in mobile view
* 2no errors have not been sorted out when passed HTML checker


# Deployment

## Heroku

1. Log in to Heroku at https://heroku.com - create an account if needed.

2. From the Heroku dashboard, click the Create new app button. For a new account an icon will be visible on screen to allow you to Create an app, otherwise a link to this function is located under the New dropdown menu at the top right of the screen.

3. On the Create New App page, enter a unique name for the application and select region. Then click Create app.

4. On the Application Configuration page for the new app, click on the Resources tab.

5. Next, click on Settings on the Application Configuration page and click on "Reveal Config Vars".

6. Add a new Config Var called DISABLE_COLLECTSTATIC and assign it a value of 1, and click Add to save it. Remove this when releasing for Production.

7. Add a new Config Var called SECRET_KEY and assign it a value - any random string of letters, digits and symbols, and click Add to save it.

8. Add a new Config Var called DATABASE_URL and paste in the value for your ElephantSQL database, and click Add to save it.

9. The settings.py file should be updated to use the DATABASE_URL and SECRET_KEY environment variable values as follows :

 DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}

 SECRET_KEY = os.environ.get('SECRET_KEY')
In Gitpod, in the project terminal window, to initialize the data model in the postgres database, run the command : python3 manage.py migrate

10. Update the requirements.txt file with all necessary supporting files by entering the command : pip freeze > requirements.txt

11. Commit and push any local changes to GitHub.

12. In order to be able to run the application on localhost, add SECRET_KEY and DATABASE_URL and their values to env.py

## Connect GitHub Repo to Heroku App

1. Navigate to Application Configuration page for the application on Heroku and click on the Deploy tab.

2. Select GitHub as the Deployment Method and if prompted, confirm that you want to connect to GitHub. Enter and search for the required repository, then click on Connect to link them up..

3. Scroll down the page and choose to either Automatically Deploy each time changes are pushed to GitHub, or Manually deploy - I chose the latter for the initial deployment to watch the   
    build and then opted for Automatic Deployment.

4. The application can be run from the Application Configuration page by clicking on the Open App button.

5. Each time you push code from your GitHub Repo it will be automatically reflected in your Heroku App.



## Pre Production Deployment

When you are ready to move to production, the following steps must be taken to ensure your site works correctly and is secure.

In GitPod:

1. Set DEBUG flag to False in settings.py

2. Update the requirements.txt file with all necessary supporting files by entering the command : pip freeze > requirements.txt

3. Commit and push code to GitHub In the Heroku App:

4. Settings > Config Vars : Delete environment variable : DISABLE_COLLECTSTATIC

5. Deploy : Click on deploy branch




# Credits

* Code Institute - For the course material and the support throughout.

* [Leather Works](https://github.com/LauraMayock/Leather-works-sustainable-products) project by colleague Laura Mayock for README file template.

* [Farnell Electronics](https://ie.farnell.com/) webpage for inspiration of the project.

* [pexel](https://www.pexels.com/) and [pixabay](https://pixabay.com/) for sourcing free images.


# Acknowledgments

I would like to thank all the lecturers of CI for their unique classes, as well as their tutors and specially my mentor Daisy Mc Girr for her patience and priceless guidance.
