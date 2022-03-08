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


### Home

### Login/Signup

### Packs Page

### Pack Detail Page

### Profile Page

## Wireframes

The wireframes for this project can be viewed [here](#)

## User Stories

## Technology Design

### Data Models

### User Interface

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

### Applications
   1. TinyPNG - Used to compress images
   2. Gitpod - Cloud based IDE used for development
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
2. 

### Acknowledgments
