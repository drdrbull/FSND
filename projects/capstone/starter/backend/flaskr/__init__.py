from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from database.models import setup_db

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)
    setup_db(app)
    print('started app')
    return app
