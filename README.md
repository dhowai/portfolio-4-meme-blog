<h1 align="left">Memebase</h1>

![Screen sizes](image here)

This project was focused on creating a Full-Stack developed site using the Django Framework.

Memebase is a reddit style blog where content is curated by the users who can view, like and comment on the content. The site is maintained by the administrators to help maintain the integrity of the site. 

The live link can be found here: https://portfolio-4-memebase.herokuapp.com/

***

#   Table of Contents:
* [User Experience](#user-experience)
    * [User Stories](#user-stories)
    * [Wireframes](#wireframes)
    * [Design](#design)
        * [1. Typography](#typography)
        * [2. Color Scheme](#color-scheme)
        * [3. Imagery](#imagery)
* [Database Schema](#database-schema)
* [Technologies Used](#technologies-used)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Features left to implement](#features-left-to-implement)
* [Templates](#templates)
* [Testing](#testing)
    * [User Stories Testing](#user-stories-testing)
    * [Code Validation](#code-validation)
    * [Maual Testing](#manual-testing)
    * [Automated Testing](#automated-testing)
* [Bugs](#bugs)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknowlegments](#credits)

***

#  User Experience:

-   ## User Stories:

    -   ### First Time visitor/User Goals
        -   As a first time User, I want to be able to easily navigate the site.
        -   As a first time User, I want to have the ability to register on the site.
        -   As a first time User, I want to view content that other's have created.

    -   ### Returning registered User Goals 
        -   As a registered User, I want to have the ability to login to the site with my credentials
        -   As a registered User, I want to be able to view new content posted by other users
        -   As a registered User, I want to be able to Create, edit and delete my posts.
        -   As a registered User, I want to be able to edit any information I entered Prior.
        -   As a registered User, I want to have the ability to logout of the site. 

    -   ### Frequent User Goals 
        -   As a frequent User, I want to easily find any new updates to the site.
    
    -   ### Administrator User Goals
        -   As an Administrator, I want to be able to access the Administration panel.
        -   As an Administrator, I want to have the ability to manage site contents.
        -   As an Administrator, i want to be able to give other users administrator abilities to help maintain the site.

[Back to Top](#table-of-contents)

-   ## Wireframes

    I used Balsamiq to create initial site layout wireframes. Wireframe's for the add/edit post, change password, edit details etc use similar structures.

    -   ### Home Page
        <img src="media/images/home-wireframe.png">

    -   ### Register Page
        <img src="media/images/register-page-wireframe.png">

    -   ### Login Page
        <img src="media/images/login-page-wireframe.png">

    -   ### Add/Edit Post Page
        <img src="media/images/add-edit-post-wireframe.png">

    -   ### Category Page
        <img src="media/images/category-page-wireframe.png">

    -   ### Mobile Home Page
        <img src="media/images/home-mobile-wireframe.png">

    -   ### Mobile Login Page 
        <img src="media/images/login-page-mobile-wireframe.png">

    -   ### Mobile Add/Edit Page
        <img src="media/images/add-edit-post-mobile-wireframe.png">

[Back to Top](#table-of-contents)

-   ## Design

    -   ### Typography
        -   The Roboto font was used for the headings, the Lato font is used for the body elements and both have sans-serif as a backup. These fonts were chosen because they compliment each other well.

    -   ### Color Scheme
        -   No Particular color scheme was used due to the nature of user's will be adding their own images as posts. Therefore a simple white background is used with a bootstrap dark for the nav-bar and footer to contrast each other.

    -   ### Imagery 
        -   The majority of images used in the site will come from users post and their profile images. These images will be stored in a cloudinary account. The other images used for example in the login page are taken from Unsplash.

[Back to Top](#table-of-contents)

# Database Schema

-   Here are the tables used to plan out the models for the memeblog app.

    -   ## The Post table 
        <img src="media/images/post-table.png">

    -   ## The Category table
        <img src="media/images/category-table.png">

    -   ## The Comment table
        <img src="media/images/comment-table.png">

    -   ## The User Profile table
        <img src="media/images/user-profile-table.png">

[Back to Top](#table-of-contents)

# Technologies Used

-   ## Programming Languages, Framworks and Editors
    -   [HTML5](https://en.wikipedia.org/wiki/HTML5)
    -   [CSS3](https://en.wikipedia.org/wiki/CSS)
    -   [JavaScript](https://en.wikipedia.org/wiki/JavaScript) 
    -   [Python](https://www.python.org/)
    -   [Django](https://www.djangoproject.com/)
    -   [Git](https://git-scm.com/)
    -   [Github](https://github.com/)
    -   [Heroku](https://www.heroku.com/)

-   ### Tools Used:
    -   [Cloudinary](https://cloudinary.com/)
    -   [Bootstrap](https://getbootstrap.com/)
    -   [PostgreSQL](https://www.postgresql.org/)
    -   [Balsamiq](https://balsamiq.com/)
    -   [Font Awesome Icons](https://fontawesome.com/)

[Back to Top](#table-of-contents)

# Features 

## Existing Features

-   Index/Home page
    -   When a user first enters the site they are greated with a welcome title, a featured post and a information side widget explaining the site.
    -   As the user scrolls down, they can see the other posts, they are organized by date posted. The new posts are displayed first.
    -   The page is paginated by 6 posts, so after every 6 posts a new page is created.

<img src="media/images/home.png">

-   Navigation Bar
    -   There are different navigation bar elements that get displayed depending on whether the user is logged in or not.
    -   When first visiting the site the user can view the posts displayed anywhere on the site, browse the different category pages, register an account or log in.
    -   It's important to note that the category list can only be updated in the admin section of the site.
        <img src="media/images/nav-bar-not-logged-in.png">
    -   When the user is logged in they can do they same as a new user, make posts and has access to edit various data. 
        <img src="media/images/nav-bar-logged-in.png">
        <img src="media/images/nav-bar-user-logged-in-menu.png">
    -   When a new user creates an account and logins for the first time the navigation bar is slightly different. The user cannot make posts until a user profile is created. Note that the user does not have to fill this form, but it does need to be submitted in order to make posts.
        <img src="media/images/new-user-home-page.png">
        <img src="media/images/new-user-create-profile-page.png">
    -   Once that's been submitted the user is redirected to the home page with a success message and the navbar is updated to reflect it.
        <img src="media/images/new-user-home-page-after-profile-created.png">

-   The footer
    -   Here the user can find out more about the developer with links to their social accounts. It also has a short description about the site.
        <img src="media/images/footer.png">

-   The register/login page
    -   The registration/login pages use the Django authentication system. The forms used are extended from the respected Django forms to style using bootstrap. 
    -   The form validation of the register form are handled by the Django authentication system. Once all the details are filled correctly, they are then redirected to the login page with a success message.
        <img src="media/images/register-page.png">

        <img src="media/images/login-page.png">
    -   The login form has a simple error message if the user enters the wrong details.

        <img src="media/images/login-page-error.png">
    -   On successful login the user is then taken to the homepage.

-   Logged in drop-down options
    -   When a user has logged in they are given access to options under their username in the navigation bar.
    -   When any of these options are updated a success message is displayed accordingly.

    -   Profile
        -   The first option is to view their user profile. It gathers the User profile generated with the details the user inputs when registering and account with the additional information when they create a profile.
        -   From here they can view all the information and have access to edit their information from that page.
        -   Other users can click on your username from your posts to view your profile.

            <img src="media/images/user-profile-page.png">

    -   Edit Profile 
        -   Here the user can edit their profile picture and bio

            <img src="media/images/edit-profile-page.png">

    -   Edit User Details
        -   Here the user can edit their user details. It uses the Django UserChangeForm and extends from that to style using bootstrap.
        -   There's also a link to change their password which redirections them to the next option.

            <img src="media/images/edit-details-page.png">

    -   Change password 
        -   Here a user can change their password. It uses the Django PasswordChangeForm and extends from that to style using bootstrap.

            <img src="media/images/change-password-page.png">     
        -   The last option is for the user to logout.


-   Adding/Editing/Deleting post content 
    -   Once the user has a registed account with a configured user profile they can start to post content to the site.
    -   The add post option is locate on the navigation bar. Once clicked they are taken to the add post page.
    -   To add a post, the form needs a unique title, a category from the selectable options and an image.
    -   Every post has the title, author's username, category and date and time posted. With links to the author's profile page and the posts category page.

        <img src="media/images/add-post-page.png">
    -   On success the user is redirected to the home page with a success message displaying their post name and the category it has been posted in.

        <img src="media/images/add-post-message.png">
    -   Once a post is created the author of that post can see options underneath the post to edit or delete their post.
    -   This uses user authentication, the condition behind it is that the user needs to be logged in and the user.id must match the post.author.id
        ```
        {% if user.is_authenticated %}
        {% if user.id == post.author.id %}
        <a href="{% url 'edit_post' post.pk %}"> Edit |</a>
        <a href="{% url 'delete_post' post.pk %}"> Delete</a>
        {% endif %}
        {% endif %}
        ```
    -   The edit option allows the author of the post to edit the title, the category or the image itself.

        <img src="media/images/edit-post-page.png">
        <img src="media/images/edit-post-update-message.png">


    -   The delete option allows the user to delete their post entirely. It gives them a warning message before hand.

        <img src="media/images/delete-post-page.png">
        <img src="media/images/delete-post-page-message.png">

-   The category Page
    -   The posts are categorized by their category given when the post initially gets created.
    -   Every category has their own page, they can be accessed by with the category drop-down on the navigation bar or the link to the category on the post.
    -   It's similar to the homepage layout, only difference is that the posts are slightly larger.
    -   Only administrators can add/edit categories on the site. 
        <img src="media/images/category-page.png">

-   The post detail Page
    -   An individual post can be viewed on its own page by clicking on the available link.
    -   It takes the user to a new page with a full view of the post with its comment section.
    -   The user can only comment or like a post if they are logged in and has the links to the appropriate pages.

        <img src="media/images/post-detail-page.png">

[Back to Top](#table-of-contents)

## Features left to implement

-   Possible features to add in future updates:
    -   Password reset when users cannot remember their passwords.
    -   Ability for users to edit/delete comments.
    -   Show number of comments on the post in the home view.
    -   Ability for user to delete their account.
    -   Sort posts by their popularity, e.g. likes, comments.
    -   Have a nested comment section so users can directly reply to specific messages.
    -   Account registration with social accounts.
    -   Have a way for users to report offensive content.
    -   Implement a contact us section for users to email site owners/admins.
    -   A search ability to find content easily. 
    -   Organize the images with folder in cloudinary.


# Templates

-   Two applications were used to create this project:
    -   One is called memebers, it handles all the aspects that have to do with the user e.g. registration, login etc.
    -   The second is called memeblog, this handles the main part of the blog. e.g. posting, commenting etc.

-   The template folder in this project has two folders:
    -   One called registration, which holds all the HTML templates for the memeber's application.
    -   The other called blog hold all the HTML templates for the memeblog/blog application.
-   All templates on the site extends from the base.html which is in the main folder from templates.
-   This base.html has the navigation and footer elements which can be found on all site pages.
-   This is the section in the base.html where the content from the other pages are placed into.
    ``` 
    <main>
        {% block content %}
        <!--Content goes here-->
        {% endblock content %}
    </main>
    ```

[Back to Top](#table-of-contents)

# Testing

## User Stories Testing

-   First Time visitor/User Goals

    -   As a first time User, I want to be able to easily navigate the site.
    
        -   When the visitor first enters the site they are greeted with a welcome message.
        -   The homepage has a featured post which gives the user a sense of what the site is about.
        -   The user can browse any category through the navigation bar or from the posts themselves.
        -   The new user can view all the content and would only need to register or login to interact with the content.

    -   As a first time User, I want to have the ability to register on the site.
        
        -   There is a side widget next to the featured post that explains briefly what the site is about and how a user can interact with the content with the relevant links.
        -   There is the register option on the navigation bar.
        -   When a user clicks on a post they can see text explaining that they need to be logged in to interact e.g. liking and commenting on a post. These texts have links to the corresponding pages.

    -   As a first time User, I want to view content that other's have created.

        -   The new user can view any post, be it on the homepage or the category page.

-   Returning registered User Goals 

    -   As a registered User, I want to have the ability to login to the site with my credentials

        -   The user can do so from the navigation bar.
        -   From the homepage side widget called information.
        -   Or from any post, which requires them to log in to interact with the content.

    -   As a registered User, I want to be able to view new content posted by other users

        -   When a user creates a post it gets posted to the home page and all the posts are sorted by date/time posted.
        -   New content would be easy to find this way.

    -   As a registered User, I want to be able to Create, edit and delete my posts.

        -   A user can find their posts by category or from the home page.
        -   The add post is at the top of the navigation bar so the user can easily make posts when logged in.
        -   If they are the author, through the conditioning they will be able to edit, delete the posts they made.

    -   As a registered User, I want to be able to edit any information I entered Prior.

        -   The user has options on the navigation bar under their username.
        -   Here they can edit various previously entered information.
        
    -   As a registered User, I want to have the ability to logout of the site. 

        -   From the navigation bar, the username dropdown gives the user the option to logout.

-   Frequent User Goals

    -   As a frequent User, I want to easily find any new updates to the site.

        -   Any new posts made will always appear first on the homepage and their respected category pages.
        -   Any new updates to the site will be posted in the information side widget on the home page.

[Back to Top](#table-of-contents)

## Code Validation 

-   HTML

    -   Each page of the site had their source page looked up and ran the HTML through the [W3C Validation](https://validator.w3.org/).
    -   The validator showed an issue on the edit user details page. This page uses Django's UserChangeForm and even though I did not state in the EditUserDetailsForm to use the password field, it still appears.
        <img src="media/images/edit-user-details-form-html-error.png">
        <img src="media/images/edit-user-details-form-html-error-code.png">
    -   This is the only error found and have not found a solution.

-   CSS

    -   No errors were returned when passing through the official [(jigsaw) validatior](https://jigsaw.w3.org/css-validator)

        <img src="media/images/w3c-css-validator-results.png">

-   JavaScript

    -   [JSHint](https://jshint.com/) was used to check for any major errors in the scripts. The only errors found were for the 'let' due to being only available in ES6.

-   Python Code

    -   No errors were returned when testing python code with [PEP8](http://pep8online.com/) except for some instances where imports were asking for docstrings in github.

        <img src="media/images/pep8-test-example.png">

## Manual Testing

-   Google Chrome developer tools were used throughout the development process to test the layout of the different pages.
-   Bootstrap made this easier to test and fix by using their documentation page to buid the sites elements.
-   Github issues and projects was used to track down the features that I wanted the site to have. Each feature was given their own label to determine how important it was to develop the site. The priority was to have the core functionality of the site up and running that was labeled with Must Have. Should Have labels are features to further improve the user experience, Could Have labels represent the features that weren't a must but would be beneficial to have and lastly the Wont Have are the features the site will not have at launch, but could have in later updates.
-   All functionality of the site was tested in the different stages of development to test whether the user was redirected to correct page after doing something. The URL naming convention has the same name, path as the view to keep it intuitive to the action.
-   The majority of the forms were extended from the various Django forms to style them with bootstrap. Each has their own error message system which ensures only valid information is accepted and a success message gets displayed on successful input.
-   The site also has User authentication to keep track of which user can post, edit and delete depending if they are they author of a post.

## Automated Testing 

-   Unit test was used from the python standard library module to test the models, forms and views for the applications. 
-   Coverage was installed to find out how much of the code was tested. Using ```pip3 install coverage``` and ```coverage --source=app manage.py test``` to generate the html file.
-   the majority of the code uses Django's class based views and forms which required no testing.

-   Coverage results for the members application

    <img src="media/images/coverage-report-members.png">

-   Coverage results for the memeblog application

    <img src="media/images/coverage-report-memeblog.png">

[Back to Top](#table-of-contents)

# Bugs

-   Database Migration

    The main issue I faced during development was working with the database. Initially the Postges database was used by default, I believe the error occurred during the creating of the second application called members. When it came to making any changes to the model in the memeblog app, (then called blog) the migrations were being made but the changes were not migrating to the database. I thought nothing of it and continued working. 
    Further on in the development more changes needed to be made and the issue persisted and now migrations were not happening at all. Went to check stack overflow if any users came across something similar. The general solution was to clear past migration files and try a new migration. This solution seemed to work, but was temporary.
    Later on, more changes needed to be made and the previous solution was not working anymore. I therefore believed it was a database issue and decided to delete my postgres database on heroku and attached a fresh database and start the migrations again.
    This caused a new error, Django was looking for a specific table and without it the migrations would not proceed. This cause a confusion as this was a new database. 
    I then contacted student care and they had not seen this error before. I moved the database to a local one using sqlite and every time I deleted the past migrations in order to start fresh, Django was still looking for that table, that didn't exist. I tried various methods with no success. The next day I recontacted student care and it began the troubleshooting again until we came accross this post [link](https://stackoverflow.com/questions/34548768/Django-no-such-table-exception/67283136#67283136). With nothing else working I tried it, deleting the application and installed a new one. 
    Initially I moved all the files it to their respected folders, e.g. the models, forms, urls which caused the same error to appear. I then removed all those files except the models, and to my joy the migrations went through. It was a very stressful experience, but I feel I learned more about how Django works which benefits me in the long run. I did notice later on that the error came from the main folders urls and simply commenting out the url path to the app, then running the migrations fixed the issue.

# Deployment

This fullstack application was deployed to GitHub pages, using Gitpod as a development environment. The changes were commited using the git version control, using the push command in Gitpod to save changes with messages into GitHub. Any secret environment variables were stored in an `env.py` files which was added by default to the `.gitignore` file using Code Institutes Gitpod template. 

## Deployment to Heroku

-   Push the code to github and commit the changes
-   Create an app using Heroku and link the project from your github account to your new Heroku app
-   In the heroku app click on setting an then reveal config vars
-   Add the secret environment variables there and in the env.py fill in gitpod. 
-   In gitpod, add the DATBASE_URL to the settings.py file
-   Make the postgres database from heroku the default database 
`DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}`
-   Then `python3 manage.py migrate` the to database
-   Then go back to heroku in the deploy section, scroll down and click deploy branch.

[Back to Top](#table-of-contents)

# Credits

-  All code was written by the author.
-   [Overstackflow](https://stackoverflow.com/) to help troubleshoot problems.
-   Codemy's Create blog [playlist](https://www.youtube.com/playlist?list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi)
-   [Very Academy](https://www.youtube.com/playlist?list=PLOLrQ9Pn6cawWd-5UZM6CIm0uqFXeBcTd)

## Media

-   Used a Blog home bootstrap started template from [Start Bootstrap](https://startbootstrap.com/template/blog-home)
-   Used snippets from bootdey.com for [comments](https://www.bootdey.com/snippets/view/blog-comments#preview) and [User information](https://www.bootdey.com/snippets/view/Table-user-information#preview)
-   Used snippet form bboostrap for a [footer](https://bbbootstrap.com/snippets/bootstrap-fixed-footer-template-social-icons-59664838)
-   Unsplash images by Fakurian Design [first](https://unsplash.com/photos/HmgeiuZE0Iw), [second](https://unsplash.com/photos/nNLQGgWZD7Q)
-   [Wallpaperswide](http://wallpaperswide.com/destiny_2_beyond_light_2020_game_europa-wallpapers.html) for homepage image

# Acknowledgements

-   The students on Slack for peer review
-   The tutor support provided by Code Institute
-   Stackoverflow for troubleshooting problems

[Back to Top](#table-of-contents)