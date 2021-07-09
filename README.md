# InnoCPC
Site for Innopolis University to track preparedness for sport programming contests among students


## How to run:
Use `docker-compose up -d` to start the server. But you need to specify required environment variables 


## Environment variables
You need to create `.env` file in root directory of the project. You can copy env example file `cp .env.example .env` 
and set environment variables:\
Required: \
`POSTGRES_PASSWORD` - Password for postgres database. It is required because Docker uses it \
`BOTNAME` - Bot alias with which users log in [(You need to setdomain in @Botfather)](https://core.telegram.org/widgets/login) \
`BOTTOKEN` - Token of bot to verify user data \
Optional: \
`DEBUG` - True/False do not use debug mode in production server \
`POSTGRES_HOST` - Use `localhost` to develop. For production delete this field \
`POSTGRES_DB_NAME` - Name of database in postgres \
`POSTGRES_USERNAME` - Username in postgres
