# Full Stack Casting Agency API Backend

## About
The Casting Agency models a company that is responsible for creating movies and managing and 
assigning actors to those movies. A system is required in order to simplify and streamline the process.

This casting agency proof of concept app is used to create a database of films and actors. In addition actors can
be assigned a role for a particular film.

A user can send a post request with the film name and release date to add a new film to the database. 
They can also send a post request with an actor's details to store in the information.
They can also send a patch request to update the film or actor's details and to cast an actor in film role.

The endpoints and how to send requests to these endpoints for products and items are described in 
the 'End Points' section of the README.

All endpoints need to be tested using curl or postman since there is no frontend for the app yet.

## Getting Started

### Installing Dependencies

#### Python 3.9

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### PIP Dependencies

In the backend directory, run the following to install all necessary dependencies:

```bash
pip install -r requirements.txt
```

This will install all of the required packages.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Render Deployment
- Sign up to a Render account using https://dashboard.render.com/register
- Create a PostgresSQL database following the standard steps described on the render website
  * Give the database the name "casting" and note DB URL, username and password
- Create a new web service following the standard steps
  * Enter the gitlab repository URL: https://github.com/drdrbull/FSND
  * Set the root directory to be: projects/capstone/starter/backend
  * Set the start command to be: gunicorn app:app  
  * Enter the build command: pip install -r requirements.txt  
  * Complete the satabase connection properties to match the ones recorded in the previous step
  * Make a note of the render URL to access this app, the example currently deployed is: https://fsnd-ibw4.onrender.com

## Gitlab Repository

https://github.com/drdrbull/FSND/projects/capstone/starter/backend 

## Running the server

## Starting Application
FLASK_APP=app.py FLASK_DEBUG=true flask run

It is also possible to start the service via Render using the URL:
https://fsnd-ibw4.onrender.com

First time the app is deployed, it is necessary to uncomment this step:
= db_drop_and_create_all()
in order to create the database.

The live application can only be used to generate tokens via Auth0, the endpoints have to be tested using curl or Postman
using the token since there is no frontend developed for this proof of concept

# DATA MODELING:
## models.py
The schema for the database and helper methods to simplify API behavior are in models.py:
- There are three tables created: actor, film and film_actor
- The actor table is used to store details about the actors
- The film table is used to store details about the films
- The film_actor table is to cast actors to film roles

## Roles
Three roles are defined (and a user must have one or more roles to use this API):
- Casting Assistant:
  * Can view actors and movies
- Casting Director: 
  * all permissions a Casting Assistant has
  * add or delete an actor from the database, 
  * modify actors or films
  * cast an actor in a role for a film
- Executive Producer: 
  * all permissions a Casting Director has 
  * add or delete a movie from the database
  
# API ARCHITECTURE AND TESTING
## End Points
### Casting Assistent
GET '/actors'
- Fetches the list of all actors supported by this casting agency
- Request Arguments: None
- Returns: An object with a single key, actors, that contains a list of actors {
  "actors": [
  {
  "age": 21,
  "gender": "F",
  "id": 1,
  "name": "Margot Robbie",
  "roles": []
  }
  ],
  "success": true
  }

GET '/movies'
- Fetches the list of all films supported by this casting agency
- Request Arguments: None
- Returns: An object with a single key, films, that contains a list of films {
  "films": [
  {
  "cast": [
  {
    "age": 21,
    "gender": "F",
    "id": 1,
    "name": "Margot Robbie"
  }
  ],
  "id": 2,
  "release_date": "2023-09-01",
  "title": "Barbenheimer"
  }
  ],
  "success": true
  }

### Casting Director
In addition to above:

POST '/actors'
- Sends a post request to register a new actor
- Request Body:
  {
  "name" : "Margot Robbie",
  "age" : "21",
  "gender" : "F"
  }
- Returns: An object with a single key, actors, that contains a single entry describing the new actor: {
  "actors": [
  {
  "age": 21,
  "gender": "F",
  "id": 8,
  "name": "Margot Robbie",
  "roles": []
  }
  ],
  "success": true
  }
  
PATCH '/actors'
= Sends a patch request to update the actors details
- Request Body:
  {
  "actor_id" : 2,
  "name" : "Margot Robbie",
  "age" : "21",
  "gender" : "F"
  }
- Returns: An object with a single key, actors, that contains a single entry describing the updated actor: {
  "actors": [
  {
  "age": 21,
  "gender": "F",
  "id": 2,
  "name": "Margot Robbie",
  "roles": []
  }
  ],
  "success": true
  }  


DEL '/actors/{actor_id}'
- Sends a request to remove an actor from the database
- Request Arguments: id - integer  
- Returns: The actor_id that has been deleted: {
  "actor_id": 7,
  "success": true
  }


PATCH movies
- Sends a request to update the film information, including assigning an actor to this film
- Request body:  {
  "film_id" : 2,
  "new_title" : "Barbenheimer",
  "new_release_date" : "2023-09-01",
  "new_actor" : 1
  }
- Returns the updated film information: {
  "film_id" : 2,
  "new_title" : "Barbenheimer",
  "new_release_date" : "2023-09-01",
  "new_actor" : 1
  }

### Executive Producer
In addition to above: 
POST '/movies'
- Adds a new film to the database
- Request body: {
  "title" : "Barbie",
  "release_date" : "2024-03-01"
  }
- Returns An object with a single key, films, that contains a single entry describing the updated film: {
  "films": [
  {
  "cast": [],
  "id": 6,
  "release_date": "2024-03-01",
  "title": "Barbie"
  }
  ],
  "success": true
  }
  
DEL '/movies/{movie_id}/
- Sends a request to remove a film from the database
- Request Arguments: id - integer
- Returns: The film_id that has been deleted: {
  "film_id": 7,
  "success": true
  }
  
## AUTHO configuration
AUTH0_DOMAIN = 'dev-3tjxoaiy36qsqjia.uk.auth0.com'
ALGORITHMS = ["RS256"]
API_AUDIENCE = 'capstone'

## Unit Tests
Postman Script:  Capstone.postman_collection.json
Postman Results: Capstone.postman_test_run.json