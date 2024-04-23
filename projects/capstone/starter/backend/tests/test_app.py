import pytest
import os
from database.models import setup_db
from flask import Flask, request, jsonify
from werkzeug.datastructures import Headers
from flask_cors import CORS, cross_origin
from api.api import app
'''
def create_app(test_config=None):
# create and configure the app
print('hello')
app = Flask(__name__)
CORS(app)

print('started app')
return app

app = create_app()
setup_db(app)
CORS(app)
'''

@pytest.fixture
def client():

    '''
    app = create_app()
    '''
    app.database_name = "casting"
    app.database_path = 'postgresql://postgres@localhost:5432/casting'
    app.config['TESTING'] = True
    app.config['AUTHORIZATION'] = jwt
    app.config['HTTP_AUTHORIZATION'] = jwt

    with app.test_client() as client:
        with app.app_context():
            setup_db(app)
            client.environ_base['HTTP_AUTHORIZATION'] = jwt
            client.environ_base['AUTHORIZATION'] = jwt
        yield client

jwt = 'Bearer= eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjRjV0E3ZzdfcGY0V3lITzMtdG12WCJ9.eyJpc3MiOiJodHRwczovL2Rldi0zdGp4b2FpeTM2cXNxamlhLnVrLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NWNjYTZlNDkzMDJhZjEyZTJlMzA2NDAiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTcxMzcyODM1MiwiZXhwIjoxNzEzNzM1NTUyLCJzY29wZSI6IiIsImF6cCI6ImFOQ3R5N0hpQnVFc2RvZ3hTTnB5UnY4dzJhWG96Z1hzIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.nV4XoysBNon0odzYwJXOhkbcUmj-0XXFZfDufT-UNr3acE0KyNT6DyU17TBWDMjo_O-iDxKFX2NCoAiShp-cZydjx_GR6a2_aWgRAia5ZlqpCfK_ooV9CX2uGnGoCI-oNGs3wqtaO3sdN9HEcsLRbpretjL52R6e0zAG3_ssIbf5clCTHr35ncAxpO5xC8Z5ADyi66zVHUHkn-wjR5KY3sae6m0-UZKx4H3igqPz893E9-qJqooUA12mnZo1ygcpI9OHiqHTyVwFpDj-ymkwgl3jGHdrp0fWRo3irUju50TMZmM7mkMZSR-83jvzVql5jgrGTeB3rk3RxD2K_pDrhw'

'''
    Tried writing these additional tests but cannot follow the lecture notes for unit testings as they seem to be incompatible with
    using a package structure and/or auth. I cannot find any way to mock the authentication which works with this
'''
def test_empty_db(client):
    print('A')
    api_key_headers = Headers({
        'AUTHORIZATION': jwt
    })
    rv = client.get('/actors' , headers = {"HTTP_AUTHORIZATION": jwt})
    print(rv)
    print(rv.get_json())
    print(rv.status_code)
    assert rv.status_code == 200
    '''
    assert b'No entries here so far' in rv.data
    '''
