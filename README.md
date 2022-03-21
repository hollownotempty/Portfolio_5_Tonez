# Tonez - Sample Store

![home_page](static/images/screenshots/home_page_screenshot.png)

## Contents

1. [Strategy](#strategy)
   1. [Project Goals](#project-goals)
   2. [User Goals](#user-goals)
2. [Structure](#structure)
3. [Flowchart](#flowchart)
4. [User Stories](#user-stories)
5. [Technology Design](#technology-design)
   1. [User Interface](#user-interface)
6. [Technologies Used](#technologies-used)
   1. [Languages](#languages)
   2. [Frameworks](#frameworks)
   3. [Applications](#applications)
7. [Validation](#validation)
8. [Testing](#testing)
9. [Deployment](#deployment)
   1. [Forking the Github Repository](#forking-the-github-repository)
   2. [Making a Local Clone](#making-a-local-clone)
   3. [Heroku](#heroku)
10. [Credits](#credits)

## Strategy

### Project Goals
   Tonez is built to sell royalty free sounds in sample packs that people can purchase and use in their music, movies, tv shows, podcasts or any other audio based project. Any packs purchased can then be re-downloaded by the user from their profile page.

### User Goals
   Any user coming to Tonez will be looking for inspiration for their project or to find a specific sound they are looking for to use in their projects. On Tonez they will be able to browse for sounds by category or just have a look at what is available and find something that might be useful. Once they purchase a pack it will be on their profile for them to redownload at any time, so they don't need to worry about it taking up space on their hard-drive if they don't use it very often. 

## Structure

### Common Elements

There are some common elements across all pages on the site. These include the nav bar on the side of the screen, the search bar and the shopping cart. On the mobile version of the site, some of these elements collapse into the side menu. 

### Home

This page features a sliding carousel of some of the currently available packs and a button to go directly to the packs page. 

### Login/Signup

Simple login and signup layout page, powered by Django Allauth and styled using bootstrap. 

### Packs Page

This page uses django template logic to render all of the packs on the site into a scrollable view. From here packs can be clicked to open the pack detail page, or the pack category can be clicked to display all of the packs with the same category. Similary, any search queries that have been made with the search bar return this page with any packs that contain the query in either the title or the description. 

### Pack Detail Page

The pack detail page features all the necessary information for the user. This includes the artwork, name, description, price and an 'add to cart' button. This page also features an embedded Soundcloud player with a demo of the pack. This is either a loop from the pack or a selection of sounds.

### Checkout Page

The checkout page for this app directs users to the prebuilt Stripe checkout page. This checkout page is populated using the Stripe ID field on each product and displaying the corresponding item that has been set on the Stripe dashboard.

### Checkout Success Page

This is the page that users are redirected to once the checkout has succeeded. It displays there order number and gives them the links to download the products that they purchased.

### Profile Page

Seeing as this site doesn't have much in the way of a social aspect, I decided to use the profile page as a list of the users previous orders. From here they can also redownlaod any purchased packs from the list.

### Admin Panel

The admin panel can be accessed through the profile page of any superuser on the site. From here you can add, remove or update any product for the site.

## Wireframes

The basic wireframes for this project can be viewed [here](#)

## Facebook

A facebook business page was created for this assignment in accordance with the project requirements. The live page can be viewed [here](https://www.facebook.com/tonez.aiff/)

![tonez_facebook](../Portfolio_5_Tonez/media/images/facebook_tonez_screenshot%20.png)

## User Stories

User stories and their respective tests are documented in ![TESTING.md](TESTING.md)

## Technology Design

### Data Models

There are multiple custom models for this project:

1. Order - Orders made by customers
2. OrderLineItem - The individual items within an order
3. ContactSubmission - Any contact submissions made with the contact form are saved in this model
4. UserProfile - The profile tied to an User, used to display any necessary information on the profile page
5. Packs - Each individual pack falls into this model, containing all of the information for the store as well as the url for the downloadable file
6. Categories - The categories associated with each pack

### User Interface

The user interface for this site was styled using Bootstrap. From the beginning of the project I wanted to move away from the classic navbar at the top of the screen. This led to the sidebar with the changing content section on the right. For the notification system, I used django's messages framework and bootstrap's toasts functionality to display tasteful messages to the user when they interacted with the site. 

Using Stripe's documentation I figured out how to redirect to their own built checkout page. This brings users to a fleshed out page to fulfill their orders and returns them to checkout success page where they can download their products at the end. 

## Technologies Used

### Languages
   1. HTML
   2. CSS
   3. Javascript
   4. Python
   5. Django Template Language

### Frameworks
   1. [Django](https://www.djangoproject.com/) - The main framework used to create this project.
   2. [Bootstrap](https://getbootstrap.com/) - Used for responsive and easy css. 
   2. [Font Awesome](https://fontawesome.com/) - Easy to use icon cdn. 

### Applications
   1. TinyPNG - Used to compress images
   2. Gitpod - Cloud based IDE used for development
   2. [VS Code](https://code.visualstudio.com/) - I switched to VS Code during the project for ease of use
   3. Heroku - Cloud platform used to host app
   4. [unsplash](https://www.unsplash.com/) - Stock image site used to source images
   5. [Stripe](https://www.stripe.com/) - Financial software used to process payments

## Validation 
All validations passed with no errors (except for HTML, which had non important errors thrown by the django template language that were ignored)
   - All Python code has been validated using the [PEP8 Online Check](http://pep8online.com/)
   - HTML has been validated using the [W3C validator](https://validator.w3.org/nu/)
   - CSS has been validated using the [Jigsaw validator](https://jigsaw.w3.org/css-validator/)

## Testing

Full information on the testing of this application can be found in [TESTING.md](TESTING.md)

## Deployment

### Forking the GitHub Repository

1. Go to the page of the relevant Github repository
2. Click 'Fork' on the top right.
3. This will have cloned the repository to your Github account.

### Making a Local Clone

1. Go to the page of the relevant Github repository
2. Click on the 'Code' button.
3. Clone the repository using HTTPS by copying the link.
4. Open Git Bash.
5. Navigate to the directory where your clone will go.
6. Type ```git clone {your clone url}```
7. Press Enter.
8. Your local clone will be in the specified directory.

### Heroku

These are the steps used to deploy this application to Heroku:

- Create an account at [heroku.com](https://.heroku.com/)
- Create a new app with your app name and region.
- Click on create app.
- Go to Resources and search for/add Heroku Postgres.
- Navigate to the "Settings" tab on your app dashboard.
- Under Config Vars, add any sensitive data (creds.json for example)
- In the deploy tab, click 'Connect to Github'.
- Search for your repository and click connect.
- Choose the correct branch for your application
- If desired, click on "Enable Automatic Deploys", which updates the deployed version with the latest commit you have pushed to Github. 

## Credits

### Coding tips and tricks

1. I had help with Stripe webhooks from the official [Stripe Youtube Channel](https://www.youtube.com/watch?v=oYSLhriIZaA&t=254s).
2. [Section.io](https://www.section.io/engineering-education/how-to-send-email-in-django/) had a great article on how to send emails over smtp using Gmail and Django.
3. [Alasdair](https://stackoverflow.com/questions/8971606/how-to-set-foreign-key-during-form-completion-python-django) on Stack Overflow helped when trying to set a foreign key in my reply form. 

### Acknowledgments
