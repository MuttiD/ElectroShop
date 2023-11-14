# Planning Phase

## User Experience (UX)

### *Site Objective*

The Electronics Shop website is a fictional B2C implemented with Django, Python, HTML, and CSS and aims to expand our market base and provide easily accessible information on what our company stands for.

The user can access the products and make purchases (if logged in), and make their reviews and ratings.

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

* Product reviews.
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


**----------kanban image to be ADDED**

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
* ...**rate products** and see the ratings in product listings.

As a **SITE OWNER**, I want to... 
* ...**encourage user engagement** by allowing reviews and ratings on products, which can **enhance trust and customer loyalty**.
* ...**include al 404 response page** so that **users clearly understand if an error occurs** when using the site and they can easily navigate back again.



# Features

## Home

## Review Details

## Sign Up Page

## Login Page

## Logout Page

## Create a Review

## Create a Comment

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

* [Looka](https://looka.com/) for making the logo.

* [TinyPNG](https://tinypng.com/) for compress image size.


JSON Formatter

# Testing

## Validation

### HTML

### CSS

### Python

### Site Testing

## Issues

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
