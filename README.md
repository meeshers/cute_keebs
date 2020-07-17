# Dream Keebs

https://dream-keebs.herokuapp.com/
## Introduction
Dream Keebs is a site made for both new and old keyboard enthusiasts. It takes into account of each keyboard component, breaks it down, and allows the community to contribute by adding parts that they would like to put into their own keyboard if the default options already provided do not match their needs. Some users may already have a vast number of keyboards, so being able to have a place to access the information about each individual keyboard will help immensely. Other users may just be starting out and testing the waters on their first custom build. By reading up on the various types of parts gathered in one location, it will help the users pick their ideal parts. Another large part of becoming a keyboard enthusiast is being able to keep track of many interest checks and group buys. This site has a feature for that as well to help manage everything in one place!

## User Stories
The landing page will display a simple background with a prompt to sign up for an account to access the features the site has to offer.  If they are not signed in, they will only be able to access "Getting Started," which provides resources and videos for those that are new to the mechanical keyboard community.

Upon signing up or signing in, the user will now have access to "Discover" and their user profile.
In their user profile, they user will be able to keep track of:
  * Keyboards they already own
  * Keyboards they would like to make
  * Interest checks and group buys they want to keep track of
  * They will be able to edit and delete any of these items if they no longer have the item or have an interest in them
  * By default, the keyboard creation will have the default data plus whatever the community has contributed to the parts
  
For the "Discover":
  * Users can browse all the parts that are in the database, whether it is seeded or added by the community
  * Users can also create parts for their own needs if they need it for their custom dream build

## Wireframes
### Landing Page
<img src="/images/Home.png">

### Sign In/Sign Up Modal
<img src="/images/Sign in_Sign up.png">

### Discover Parts
<img src="/images/Discover parts.png">

### Tips Page
<img src="/images/Tips.png">

### Profile Page
<img src="/images/Profile page.png">

### Keyboard Creation Page
<img src="/images/Create keyboard.png">

### Keyboard Edit Page
<img src="/images/Keyboard Edit Page.png">

### Keyboard Show Page 
<img src="/images/Keyboard showpage.png">

### All Parts Show Page
<img src="/images/Parts show page.png">

## ERD
<img src="/images/keeb ERD.jpg">

## Technologies
Dream Keebs utilizes the following technologies:
  * HTML/CSS
    * Semantic UI
  * Python
  * Mongo
  * Django
  * Postgres SQL
  * Javascript

## Installation
To install the dependencies for this project, the user must do the following below:
  * Make sure they are running a virtual environment in python 3
  * Activate the virtual environment
  * Run `pip3 install -r requirements.txt`
 
      * IF it does not work:
      * Install pip packages for Django and psycopg2 using `pip3 install Django` and `pip3 install psycopg2` or `psycopg2-binary`
  * Run `python3 manage.py migrate` to import all models
  
  OPTIONAL:
  * To load the JSON data into the database, you must do `python3 manage.py loaddata /main_app/fixture/file_name.json`

## Future Features
 * Allow users to be able to edit and delete the part that they created
 * Create a blog/forum space to allow the community to interact with each other
 * Generate a checklist based on a dream keyboard, and allow the user to track what they have already purchased for their build
 * Create a search functionality for parts

## Unsolved Problems
 * Sign up/Sign in verification not fully functioning
 * Creation of keyboard requires two steps instead of one
