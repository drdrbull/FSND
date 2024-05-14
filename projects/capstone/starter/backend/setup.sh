#!/bin/bash
echo 'Test'
export FLASK_APP=app.py
export FLASK_DEBUG=true
export AUTH0_DOMAIN='dev-3tjxoaiy36qsqjia.uk.auth0.com'
export ALGORITHMS=["RS256"]
export API_AUDIENCE='capstone'
flask run