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
    * [Existing Features](#existing-features)
    * [Features left to implement](#features-left-to-implement)
* [Templates](#templates)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

***

#  User Experience:

-   ## User Stories:

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
        -   Majority of images used in the site will come from users post and thir profile images. These images will be stored in a cloudinary account. The other images used for example in the login page are taken from Unsplash.

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
    -   [PostgreSQL](https://www.postgresql.org/)
    -   [Balsamiq](https://balsamiq.com/)
    -   [Font Awesome Icons](https://fontawesome.com/)

[Back to Top](#table-of-contents)

# Features 

## Existing Features

-   Index/Home page
    -   When a user first enters the site they are greated with a welcome title, a featured post and a information side widget explaining the site.
    -   As the user srolls down they can see the other posts, they are organized by date posted. The new posts are displayed first.
    -   The page is paginated by 6 posts, so after every 6 posts a new page is created for the rest.

<img src="media/images/home.png">

-   Naviagtion Bar
    -   There are different naviagtion bar elements that get displayed depending on whether the user is logged in or not.
    -   When first visiting the site the user can view the posts displayed anywhere on the site, browse the different category pages, register an account or log in.
        <img src="media/images/nav-bar-not-logged-in.png">
    -   When the user is logged in they can do they same as a new user and have the option to make posts and has access to edit various data. 
        <img src="media/images/nav-bar-logged-in.png">
        <img src="media/images/nav-bar-user-logged-in-menu.png">
    -   When a new user creates an account and logs in for the first time the navigation bar is slightly different. The user can not make posts until a user profile is created which is displayed. Note that the user does not have to fill this form, but it does need to be submitted in order to make posts.
        <img src="media/images/new-user-home-page.png">
        <img src="media/images/new-user-create-profile-page.png">
    -   Once that's been submitted the user is redirected to the home page with a success message and the navbar is updated to reflect it.
        <img src="media/images/new-user-home-page-after-profile-created.png">

-   The footer
    -   Here the user can find out more about the developer with links to their social accounts. It also has a short description about the site
        <img src="media/images/footer.png">

-   The register/login page
    -   The register/login pages uses the django authentication system. The forms used are extended from the respected django forms to style using bootstrap. 
    -   All the errors in he filling of the register form is handled by the django authentication system. Once all the details are filled correctly they are then redirected to the login page with a success message.
        <img src="media/images/register-page.png">

        <img src="media/images/login-page.png">
    -   The login form has a simple error message if the user enters the wrong details.

        <img src="media/images/login-page-error.png">
    -   On successful login the user is then taken to the homepage.

-   Logged in dropdown options
    -   When a user has logged in they are given access to options under their username on the navigation bar.
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
        -   Here the user can edit their user details. It uses the django UserChangeForm and extends from that to style using bootstrap.
        -   There's also a link to change their password which redirections them to the next option.

            <img src="media/images/edit-details-page.png">

    -   Change password 
        -   Here a user can change their password. It uses the django PasswordChangeForm and extends from that to style using bootstrap.

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
    -   Every category has their own page, they can be accessed by with the category dropdown on the navigation bar or the link to the category on the post.
    -   It's similar to the homepage layout, only difference is that the posts are slightly larger. 
        <img src="media/images/category-page.png">

-   The post detail Page
    -   An indivdual post can be viewed on its own page by clicking on the available link.
    -   It takes the user to a new page with a full view of the post with its comment section.
    -   The user can only comment or like a post if they are logged in and has the links to the appropriate pages.

        <img src="media/images/post-detail-page.png">

[Back to Top](#table-of-contents)

## Features left to implement

-   Possible features to add in an update:
    -   Password reset when users cannot remember their passwords.
    -   Ability for users to edit/delete comments.
    -   Show number of comments on the post in the home view.
    -   Ability for user to delete account.
    -   Sort posts by their popularity e.g. likes, comments on their own page.
    -   Have a nested comment section so users can directly reply to specific messages.
    -   Account registration with social accounts.

# Templates