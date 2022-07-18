# Set Up

## Initial Set Up SQLAlchemy

- Install Flask-SQLAlchemy

![Install Flask-SQLAlchemy](documentation/deployment/atletico-crud-install-flask-sqlalchemy.png)

- Confirmation of SQLAlchemy Installation

![Completed Flask-SQLAlchemy Install](documentation/deployment/atletico-crud-flask-sqlalchemy-installed.png)

- Creation of env.py File

![Create env.py File](documentation/deployment/atletico-crud-create-env-file.png)

- Add env.py and pychache to gitignore

![Add env.py and __pycache__ to .gitignore](documentation/deployment/atletico-crud-files-added-to-gitignore.png)

- Import os to env.py

![Import OS To env.py](documentation/deployment/atletico-crud-add-mongo-uri-to-env-redacted.jpg)

- Create atleticocrud Folder with init.py File

![Create atleticocrud Folder With __init__.py File](documentation/deployment/atletico-crud-folder-with-init-file.png)

- Add Imports to init.py File

![Imports To __init__.py](documentation/deployment/atletico-crud-imports-update.png)

- Set Variables in init.py

![Set Variables In __init__.py](documentation/deployment/atletico-crud-set-init-vars-update.png)

- Create routes.py File

![Create routes.py File](documentation/deployment/atletico-crud-create-routes-file.png)

- Add Imports to routes.py

![Imports To routes.py](documentation/deployment/atletico-crud-routes-imports-update.png)

- Create app.py File

![Create app.py File](documentation/deployment/atletico-crud-create-app-file.png)

- Add Imports to app.py

![Imports To app.py File](documentation/deployment/atletico-crud-app-file-imports.png)

- Create Templates Folder with base.html File

![Create templates Directory With base.html file](documentation/deployment/atletico-crud-templates-directory-with-base-file.png)

- Set Up base.html Boilerplate

![base.html Boilerplate Set-Up](documentation/deployment/atletico-crud-base-html.png)

- Initial App Run in Development Environment

![Initial app.py run](documentation/deployment/atletico-crud-initial-app-run.png)

- Create models.py File

![Create models.py File](documentation/deployment/atletico-crud-create-models-file.png)

- Create Database Postgres From CLI

![Postgres CLI](documentation/deployment/atletico-crud-create-database-postgres-cli.png)

- Generate and Migrate Models

![Generate And Migrate Models](documentation/deployment/atletico-crud-generate-migrate-models-update.png)

## Flask-Migrate

During the course of development, it became necessary to update the Postgres models. In order to do this, Flask-Migrate was used.

- Install Flask-Migrate

![Install Flask Migrate](documentation/deployment/atletico-crud-install-flask-migrate.png)

- Flask-Migrate Install Confirmed

![Flask Migrate Installed](documentation/deployment/atletico-crud-flask-migrate-installed.png)

- Import Flask-Migrate to init.py

![Import Flask Migrate To __init__.py](documentation/deployment/atletico-crud-import-flask-migrate-to-init.png)

- Define Migrate in init.py

![Define Migrate In __init__.py](documentation/deployment/atletico-crud-define-migrate-in-init.png)

- Enter Flask DB Init Command to CLI

![Flask DB Init Command](documentation/deployment/atletico-crud-flask-db-init.png)

- Carry Out Initial Migration in CLI

![Initial Migration Command](documentation/deployment/atletico-crud-initial-migration.png)

- Carry Out DB Upgrade in CLI

![Flask DB Upgrade To Apply Migration](documentation/deployment/atletico-crud-apply-migration-via-flask-db-upgrade.png)

## Initial Set Up MongoDB

- Connect MongoDB

![Connecting to Mongo DB](documentation/deployment/atletico-crud-connect-mongo-db.png)

- Confirmation of MongoDB Connection

![Confirmation of Mongo DB Connection](documentation/deployment/atletico-crud-mongo-connection-confirmation-update.png)

- Install DNS Python

![Install DNS Python](documentation/deployment/atletico-crud-install-dnspython.png)

- Install PyMongo

![Install Pymongo](documentation/deployment/atletico-crud-install-pymongo.png)

- Install Flask-PyMongo

![Install Flask-PyMongo](documentation/deployment/atletico-crud-install-flask-pymongo.png)

- Get MONGO_URI

Click on the cluster created for the project.

![Mongo URI Step One](documentation/deployment/atletico-crud-mongo-uri-step-one.png)

Click on the _Connect_ button.

![Mongo URI Step Two](documentation/deployment/atletico-crud-mongo-uri-step-two.png)

Click _Connect Your Application_.

![Mongo URI Step Three](documentation/deployment/atletico-crud-mongo-uri-step-three.png)

Copy the connection string and ensure to replace `<password>` with your own password.

![Mongo URI Step Four](documentation/deployment/atletico-crud-mongo-uri-step-four.png)

Paste this string into the env.py file and Heroku config var as the value for the MONGO_URI key.

- Add Mongo URI to env.py.

![Adding Mongo URI to env.py](documentation/deployment/atletico-crud-add-mongo-uri-to-env-redacted.jpg)