# InnoCPC
Site for Innopolis University to track preparedness for sport programming contests among students


## How to run:
Use ```docker-compose up``` to start the server. But you need to specify required environment variables 


## Environment variables
You can create ```.env``` file in root directory of the project and set environment variables: \
Required: \
```SECRET_KEY``` - Path to database file (you can leave its default value) \
```MODE``` - Mode of server may be: DEBUG, PRODUCTION \
```POSTGRES_PASSWORD``` - Password for postgres database. It is required because Docker uses it \
```BOTNAME``` - Bot alias with which users log in [(You need to setdomain in @Botfather)](https://core.telegram.org/widgets/login) \
Optional: \
```SET_POSTGRES``` - May be 'True' to use postgres as database or 'False' to use sqlite \
```POSTGRES_DB_NAME``` - Name of database in postgres \
```POSTGRES_USERNAME``` - Username in posrgres
