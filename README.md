<h1 align="left">Memebase</h1>

![Screen sizes](image here)

This project was focused on creating a Full-Stack developed site using the Django Framework with the use of a database. 

Memebase is a reddit style blog for memes, the users can come here to share/view memes in various categories. A user can visit to purely view the content, but, they would need to register an account in order to be able to post or comment on other's posts.

add more info?

The live link can be found here: https://portfolio-4-memebase.herokuapp.com/

***

#   Table of Contents:
* [User Experience](#user-experience)
    * [User Stories](#user-stories)
    * [Wireframes](#wireframes)
    * [Design](#design)
        * [1. Typography](#1-typography)
        * [2. Color Scheme](#2-color-scheme)
        * [3. Imagery](#3-imagery)
* [Database Schema](#database-schema)
* [Technologies Used](#technologies-used)
* [Features](#features)
    * [Feature left to implement](#Feature-left-to-implement)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

***

##  User Experience:

-   ### User Stories:

    -   ### First Time vistitor/User Goals
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
        -   As a Administrator, I want to be able to access the Administration panel.
        -   As a Administrator, I want to have the ability to manage site contents.
        -   As a Administrator, i want to be able to give other users administrator abilities to help maintain the site.

[Back to Top](#table-of-contents)

-   ### Wireframes

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

-   ### Design

    -   ### Typography
        -   The Roboto font was used for the headings, the Lato font is used for the body elements and both have sans-serif as a backup. These fonts were chosen because they compliment each other well.

    -   ### Color Scheme
        -   No Particular color scheme was used due to the nature of user's will be adding their own images as posts. Therefore a simple white background is used with a bootstrap dark for the nav-bar and footer to contrast each other.

    -   ### Imagery 
        -   Majority of images used in the site will come from users post and thir profile images. These images will be stored in a cloudinary account. The other images used for example in the login page are taken from Unsplash.

[Back to Top](#table-of-contents)

-   ### Database Schema
    -   Here are the tables used to plan out the models for the memeblog app.

    -   ### The Post table 
        <img src="media/images/post-table.png">

    -   ### The Category table
        <img src="media/images/category-table.png">

    -   ### The Comment table
        <img src="media/images/comment-table.png">

    -   ### The User Profile table
        <img src="media/images/user-profile-table.png">

[Back to Top](#table-of-contents)

-   ### Technologies Used

    -   ### Programming Languages, Framworks and Editors
        -   [HTML5](https://en.wikipedia.org/wiki/HTML5)
        -   [CSS3](https://en.wikipedia.org/wiki/CSS)
        -   [JavaScript](https://en.wikipedia.org/wiki/JavaScript) 
        -   [Python](https://www.python.org/)
        -   [Django](https://www.djangoproject.com/)
        -   [Git](https://git-scm.com/)
        -   [Github](https://github.com/)
        -   [Heroku](https://www.heroku.com/)

    -   ### Tools Used:
        -   [PostgreSQL](https://www.postgresql.org/)
        -   [Balsamiq](https://balsamiq.com/)
        -   [Font Awesome Icons](https://fontawesome.com/)

[Back to Top](#table-of-contents)

-   ### Features 