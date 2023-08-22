# Volbomzutter: A simple blog web-application
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
This project was made by our hackathon team VolBomZur for practicing our skills in web-development.

## Setup
First of all, create and start up a docker container  
`docker run --name pg -p 5432:5432 -e POSTGRES_USER=user -e POSTGRES_PASSWORD=123 -e POSTGRES_DB=db -d postgres`  

Create the database table  
`python db_api/create_db.py`

Start the flask server  
`flask --app volvomzutter run`

## Contribution
- [Denis Indenbom](https://github.com/denisindenbom): PostrgreSQL Database + Docker setup
- [Maxim Mazur](https://github.com/martosinc): Database and backend merge + Minor work on database
- [Zahar Voloshko](https://github.com/zinko-dev): Backend
