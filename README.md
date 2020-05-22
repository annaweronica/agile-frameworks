
[Agile frameworks heroku-LIVE](https://agile-frameworks.herokuapp.com/)

[ROADMAP](/roadmap.md)<br>
[STATEMENT](/statement.md)<br>


# FEATURES

## Features implemented

1. User authentication
2. Addin, editing and deleting a packacge. CRUD implemented on the level of superuser
3. Contact form
4. *See the offer* button to redirect the user to the *OFFER*
5. Navbar navigations easily throught the site
6. Navbar with different available options for different level user
7. Ability to add, edit and delete a packacge on a superuser level
8. Ability to give a package a rating on a superuser level
8. Browse all available packages on the *Offer* site
9. Buy a chosen package
10. Add another package to the checkout *cart*
11. Pay for the package
12. 

## Features to be implemented

1. Reviews for users to wrote connected with existing rating


# USER STORIES

## Main page

1. As a user I want to get to know what is the website about to define is the content relevant for me
2. As a user I want to be able to easily navigate across the website
3. As a user I want to be able to pay for selected service
4. As a user I want to be able to contact the owner of the website
5.

## Registration

1. As a new user I want to register to discover more content
2. As a user I want to get confirmation about being registrated

## Login 

1. As a user I want to be able to login to see more content
2. As a user I want to be able to pay for the selected service
2. As a user I want to be able to use contact form to discuss date/details
3. As a user I want to be able to leave Testemonials

## Checkout

1. As a user I want to be able to select the package.
2. As a user I want to be able to view the selected package in the purchase summary.
3. As a user I want to enter my payment infomation
4. As a user I want to see the order confirmation after Checkout
5. As a user I want to see email confirmation after checking out

# UX

- [wireframes](/wireframes.md)

# TECHNOLOGIES

- Fronend: 
    - HTML
    - CSS
    - JS
    - Bootstrap

- Backend:

    - Python
    - Django
    - Stripe for payments
    - PosteSQL for database
    - AWS for storing media files

# TESTING

[TESTTING](/testing.md)<br>


# EXTERNAL RESOURCES USED IN THE PEOJECT

- [Header](https://www.codeply.com/go/ljI9F6aRLk)
- [Template HTML](https://www.w3schools.com/w3css/tryit.asp?filename=tryw3css_templates_architect&stacked=h)
- [navbar and carousel](https://startbootstrap.com/snippets/half-slider/)
- [template for packages](https://startbootstrap.com/snippets/portfolio-item/)
- [template for shop with reviews](https://startbootstrap.com/previews/shop-item/)
- [template for a checkout form](https://codepen.io/manassehl/pen/OYVeXB)
- [template for a shopping cart/bag](https://bootstrapious.com/p/bootstrap-shopping-cart)
- [template for a review](https://www.bootdey.com/snippets/view/bs4-Ratings-and-Reviews-page#html)
- [templete for offer description](https://startbootstrap.com/previews/modern-business/)

<br>
- [Inspiration for the project](https://uxdesignmasterclass.com/)

# DEPLOYMENT

## Requirements

It's highly recommended to work in a virtual environment, but not absolutely required.

In order to run this project locally on your own system, you will need the following installed (as a bare minimum):
- Python3 to run the application
- PIP to install all app requirements
- GIT for cloning and version control
- Gitpod or any suitable IDE to develop your project

## Local deployment

- Clone this GitHub repository by either clicking the green "Clone or download" button above in order to download the project as a zip-file (remember to unzip it first), or by entering the following command into the Git CLI terminal:
git clone https://github.com/annaweronica/agile-frameworks.git
- Navigate to the correct file location after unpacking the files.
cd <path to folder>
- Create a .env file with your own credentials. An example .env file can be found here (.env_sample).
Note: the example .env file contains environmental variables for both local and remote deployment. (see below for remote deployment details)
- Install all requirements from the requirements.txt file using this command:
sudo -H pip3 -r requirements.txt
- In the IDE terminal, use the following command to launch the Django project:
python manage.py runserver
- The Django server should be running locally now on http://127.0.0.1:8000 or similar. If it doesn't automatically open, you can copy/paste it into your browser of choice.
- The Django server should be running locally now on http://127.0.0.1:8000 (or similar). If it doesn't automatically open, you can copy/paste it into your browser of choice.
- Next, you'll need to make migrations to create the database schema:
        - python manage.py makemigrations
        - python manage.py migrate
- In order to access the Django Admin Panel, you must generate a superuser:
        - python manage.py createsuperuser (assign an admin username, email, and secure password)

## Remote deployment

To deploy The House of Mouse webshop to heroku, take the following steps:

- Create a requirements.txt file using the terminal command pip freeze > requirements.txt
- Create a Procfile with the terminal command echo web: python app.py > Procfile
- git add and git commit the new requirements and Procfile and then git push the project to GitHub
- Create a new app on the Heroku website by clicking the "New" button in your dashboard. Give it a name and set the region to whichever is applicable for your location
- From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub
- Confirm the linking of the heroku app to the correct GitHub repository
- In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars"
- Set the following config vars:


 KEY                     | Value                           | 
| ----------------------- |:--------------------------:    | 
| AWS_ACCESS_KEY_ID       | `<your secret key>`            | 
| AWS_SECRET_ACCESS_KEY   | `<your secret key>`            |
| AWS_STORAGE_BUCKET_NAME | `<your AWS S3 bucket name>`    |
| DATABASE_URL            | `<your postgres database url>` |
| EMAIL_HOST_PASS         | `<your secret key>`            |
| EMAIL_HOST_USER         | `?emial adres?`                |
| STRIPE_PUBLIC_KEY       | `<your secret key>`            |
| STRIPE_SECRET_KEY       |`<your secret key>`             |


- From the command line of your local IDE:
        - Enter the heroku postres shell
        - Migrate the database models
        - Create your superuser account in your new database
        - Instructions on how to do these steps can be found in the [heroku devcenter documentation](https://devcenter.heroku.com/articles/heroku-postgresql)
- In your heroku dashboard, click "Deploy". Scroll down to "Manual Deploy", select the master branch then click "Deploy Branch"
- Once the build is complete, click the "Open app" button provided
- From the link provided add /admin to the end of the url, log in with your superuser account and create instances of Packages in the new database
- Once the instance exists in your database your heroku site will run as expected

# CREDITS

- [Chris Zielinski and CI vidoes on Django module](https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/info)
- [Anna Greaves for ReadMe inspiration](https://github.com/AJGreaves/thehouseofmouse)
- [Tim Nelson for ReadMe inspiration](https://github.com/TravelTimN/ci-milestone05-fsfw)

<br>
All pictures on this site comes from [Stock Adobre](https://stock.adobe.com/se/)

