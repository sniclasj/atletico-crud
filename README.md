# Atletico Crud
Atletico Crud is an online soccer/football database.

The database contains players who are renowned as having 'legend status' for a particular club, in a particular league within a particular country _e.g. Alan Shearer who played for Newcastle United in the Premier League in England._

The aim of the website is for users to view players who have already been inducted to the database and for them to submit their own suggestions for players to be entered into the database via a Form.

The website's admin will then review the submitted forms and decide whether to create a new entry.

# User Stories
- As a user, I want to be able to register as a user on the website.
- As a user, I want to be able to log in and log out from the website.
- As a user, I want to be able to read/view countries, leagues, clubs and players that have already been inducted into the database.
- As a user, I want to be able to submit a form to suggest a player that should be added to the database.
- As a user, I want to be able to receive confirmation that my form has been sent.
- As a user, I want to be able to navigate to view all countries, leagues, clubs and players.
- As a user I want to be able to view the website across multiple devices and screen sizes.
- As an admin, I want to be able to create/add data to the database.
- As an admin, I want to be able to read/view data on the database.
- As an admin, I want to be able to updtae/edit data within the database.
- As an admin, I want to be able to delete data from the database.
- As an admin, I want to receive confirmation that actions involving creating, editing or deleting have been successful or unsuccessful.
- As a user I want to be able to create/add, read/view, update/edit and delete content on the website across multiple devices and screen sizes.

# UX
The aim of the site is to be as minimal as possible so that attention is focused on the database content.

Once registered or logged in, users are taken their profile page. From here, the ever present navigation bar allows the user to navigate to Countries, Leagues, Clubs or Players. When utilising the links in the navbar directly _e.g. clicking Clubs_, the user will be directed to a view showing all clubs across all leagues present in the database. However, if the player were to navigate to _Leagues_ first before selecting _Premier League_, the club's visible would be filitered so that only Premier League clubs are displayed. This gives the user the felxibility to look at what they are most interested in viewing.

Users can also navigate to a _Form_ page to submit their suggestions for players who they believe should be inducted into the database.

The website utilises Materialize CSS to responsively react to different screen sizes so that the user can view content on multiple devices.

## Colour Scheme
I selected the dark-cyan and white colour scheme as they contrasted nicely with each other _e.g. white text on a dark-cyan background or vice versa_. The dark-cyan also didn't clash with any country flag, league logo or club crest/kit and was a more interesting colour than a dark grey or black.

## Typography
The font used for the logo and the page headings is Monoton from Google Fonts. I chose this font as it reminded me of the font utilised by the football/soccer magazine 'Mundial'.

# Visual ERD
![Visual ERD](documentation/testing/atletico-crud-erd-image.png)

# Wireframes
![Wireframes Country](documentation/wireframes/atletico-crud-wireframe-country-page.jpg)
![Wireframes League](documentation/wireframes/atletico-crud-wireframe-league-page.jpg)
![Wireframes Club](documentation/wireframes/atletico-crud-wireframe-club-page.jpg)
![Wireframes Player](documentation/wireframes/atletico-crud-wireframe-player-page.jpg)

# Features

## Existing Features

## Features Left to Implement

# Technologies Used

# Testing

# Deployment

# Set Up Steps

# Initial Set Up SQLAlchemy
![Install Flask-SQLAlchemy](documentation/deployment/atletico-crud-install-flask-sqlalchemy.png)
![Completed Flask-SQLAlchemy Install](documentation/deployment/atletico-crud-flask-sqlalchemy-installed.png)
![Create env.py File](documentation/deployment/atletico-crud-create-env-file.png)
![Add env.py and __pycache__ to .gitignore](documentation/deployment/atletico-crud-files-added-to-gitignore.png)
![Import OS To env.py](documentation/deployment/atletico-crud-import-os.png)
![Create atleticocrud Folder With __init__.py File](documentation/deployment/atletico-crud-folder-with-init-file.png)
![Imports To __init__.py](documentation/deployment/atletico-crud-imports.png)
![Set Initial Variables In __init__.py](documentation/deployment/atletico-crud-set-init-vars.png)
![Create routes.py File](documentation/deployment/atletico-crud-create-routes-file.png)
![Imports To routes.py](documentation/deployment/atletico-crud-routes-imports.png)
![Create app.py File](documentation/deployment/atletico-crud-create-app-file.png)
![Imports To app.py File](documentation/deployment/atletico-crud-app-file-imports.png)
![Create templates Directory With base.html file](documentation/deployment/atletico-crud-templates-directory-with-base-file.png)
![base.html Boilerplate Set-Up](documentation/deployment/atletico-crud-base-html.png)
![Initial app.py run](documentation/deployment/atletico-crud-initial-app-run.png)
![Create models.py File](documentation/deployment/atletico-crud-create-models-file.png)

![Postgres CLI](documentation/deployment/atletico-crud-create-database-postgres-cli.png)
![Generate And Migrate Models](documentation/deployment/atletico-crud-generate-migrate-models.png)

# Flask-Migrate
![Install Flask Migrate](documentation/deployment/atletico-crud-install-flask-migrate.png)
![Flask Migrate Installed](documentation/deployment/atletico-crud-flask-migrate-installed.png)
![Import Flask Migrate To __init__.py](documentation/deployment/atletico-crud-import-flask-migrate-to-init.png)
![Define Migrate In __init__.py](documentation/deployment/atletico-crud-define-migrate-in-init.png)
![Flask DB Init Command](documentation/deployment/atletico-crud-flask-db-init.png)
![Initial Migration Command](documentation/deployment/atletico-crud-initial-migration.png)
![Flask DB Upgrade To Apply Migration](documentation/deployment/atletico-crud-apply-migration-via-flask-db-upgrade.png)

# Initial Set Up MongoDB
![Connecting to Mongo DB](documentation/deployment/atletico-crud-connect-mongo-db.png)
![Confirmation of Mongo DB Connection](documentation/deployment/atletico-crud-mongo-connection-confirmation.png)
![Install DNS Python](documentation/deployment/atletico-crud-install-dnspython.png)
![Install Pymongo](documentation/deployment/atletico-crud-install-pymongo.png)
![Install Flask-PyMongo](documentation/deployment/atletico-crud-install-flask-pymongo.png)
![Adding Mongo URI to env.py](documentation/deployment/atletico-crud-add-mongo-uri-to-env.png)

# Heroku Deployment
![Freeze requirements.txt](documentation/deployment/atletico-crud-heroku-freeze-requirements.png)
![Create Procfile](documentation/deployment/atletico-crud-heroku-procfile.png)
![Connect Heroku and GitHub ](documentation/deployment/atletico-crud-heroku-connect-to-github.png)
![Set Config Vars](documentation/deployment/atletico-crud-heroku-config-vars.png)
![Enable Auto Deployment](documentation/deployment/atletico-crud-heroku-enable-auto-deploys.png)
![App Successfully Deployed](documentation/deployment/atletico-crud-heroku-successfully-deployed-app.png)

# Credits
