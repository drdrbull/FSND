import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from database.models import *
from auth.auth import AuthError, requires_auth

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)

    return app

app = create_app()
setup_db(app)
CORS(app)

'''
    GET /films
        it should be a public endpoint
    returns status code 200 and json {"success": True, "films": films} where films is the list of films
        or appropriate status code indicating reason for failure
'''
@app.route('/movies', methods=['GET'])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth('get:movies')
def get_films(jwt):
    films = Film.query.all()
    returnMe = []
    for f in films:
        returnMe.append(f.long())

    print(returnMe)
    return jsonify({
        "success": True,
        "films": returnMe
    })

'''
    POST /film
        adds a new film to the film table
    returns status code 200 and json {"success": True, "films": drink} where film an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''
@app.route('/movies', methods=['POST'])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth('post:movies')
def post_movies(jwt):
    newFilmInfo = request.get_json()
    new_title = newFilmInfo['title']
    new_release_date = newFilmInfo['release_date']

    films = []
    film = Film(title=new_title, release_date=new_release_date)
    film.insert()
    films.append(film.long())

    return jsonify({
        "success": True,
        "films": films
    })

'''
    PATCH /film
        modifies a film or assigns an actor to it
    returns status code 200 and json {"success": True, "films": drink} where film an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''
@app.route('/movies', methods=['PATCH'])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth('patch:movies')
def patch_movies(jwt):
    newFilmInfo = request.get_json()
    film_id = newFilmInfo['film_id']

    films = []
    film = Film.query.filter(Film.id == film_id).one_or_none()
    if film is None:
        raise AuthError({
            'code': 'not found',
            'description': 'Not found'
        }, 404)

    for key, value in newFilmInfo.items():
        print(key)

        if key == 'new_title':
            print(value)
            film.title = value

        if key == 'new_release_date':
            print(value)
            film.release_date = value

        if key == 'new_actor':
            print(value)
            actor = Actor.query.filter(Actor.id == value).one_or_none()
            print(actor.short())
            if actor is None:
                raise AuthError({
                    'code': 'not found',
                    'description': 'Not found'
                }, 404)
            film.actors.append(actor)

    film.update()

    films.append(film.long())

    return jsonify({
        "success": True,
        "films": films
    })

'''
    DELETE /movies/1
        where <id> is the existing movie id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''
@app.route('/movies/<int:id>', methods=['DELETE'])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth('delete:movies')
def delete_film(jwt, id):
    film = Film.query.filter(Film.id == id).one_or_none()
    if film is None:
        raise AuthError({
            'code': 'not found',
            'description': 'Not found'
        }, 404)

    film.delete()

    return jsonify({
        "success": True,
        "film_id": id
    })

'''
    GET /actors
        it should be a public endpoint
    returns status code 200 and json {"success": True, "films": films} where films is the list of films
        or appropriate status code indicating reason for failure
'''
@app.route('/actors', methods=['GET'])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth('get:movies')
def get_actors(jwt):
    actors = Actor.query.all()
    returnMe = []
    for a in actors:
        returnMe.append(a.long())

    print(returnMe)
    return jsonify({
        "success": True,
        "actors": returnMe
    })

'''
    POST /actor
        adds a new actor to the film table
    returns status code 200 and json {"success": True, "actor": actor} where film an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''
@app.route('/actors', methods=['POST'])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth('post:actors')
def post_actor(jwt):
    newActorInfo = request.get_json()
    new_name = newActorInfo['name']
    new_age = newActorInfo['age']
    new_gender = newActorInfo['gender']

    actors = []
    actor = Actor(name=new_name, age=new_age, gender = new_gender)
    actor.insert()
    actors.append(actor.long())

    return jsonify({
        "success": True,
        "actors": actors
    })

'''
    PATCH /actor
        updates an actor
        actor_id identities actor
    returns status code 200 and json {"success": True, "actor": actor} where film an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''
@app.route('/actors', methods=['PATCH'])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth('patch:actors')
def patch_actor(jwt):

    newActorInfo = request.get_json()
    actor_id = newActorInfo['actor_id']
    print(actor_id)
    actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
    if actor is None:
        raise AuthError({
            'code': 'not found',
            'description': 'Not found'
        }, 404)

    for key, value in newActorInfo.items():
        print(key)

        if key == 'new_name':
            print(value)
            actor.name = value

        if key == 'new_age':
            print(value)
            actor.age = value

        if key == 'new_gender':
            print(value)
            actor.gender = value

    actors = []
    actor.update()
    actors.append(actor.long())

    return jsonify({
        "success": True,
        "actors": actors
    })

'''
    DELETE /actors/1
        where <id> is the existing actor id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''
@app.route('/actors/<int:id>', methods=['DELETE'])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth('delete:actors')
def delete_actors(jwt, id):
    actor = Actor.query.filter(Actor.id == id).one_or_none()
    if actor is None:
        raise AuthError({
            'code': 'not found',
            'description': 'Not found'
        }, 404)

    actor.delete()

    return jsonify({
        "success": True,
        "actor_id": id
    })

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422

@app.errorhandler(403)
def notPermissioned(error):
    return jsonify({
        "success": False,
        "error": 403,
        "message": "unprocessable"
    }), 403

@app.errorhandler(404)
def notFound(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404

@app.errorhandler(AuthError)
def notAuthorised(error):
    return jsonify({
        "success": False,
        "error": error.status_code,
        "message": error.error
    }), error.status_code
