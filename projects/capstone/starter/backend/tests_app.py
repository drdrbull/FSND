import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from api.api import app
from database.models import *

class CastingAcademyTestCase(unittest.TestCase):

    def setUp(self):
        print('aa')
        """Define test variables and initialize app."""
        self.app = create_app()
        self.database_name = "casting"
        self.database_path = 'postgresql://postgres@localhost:5432/casting'
        self.app.client = self.app.test_client
        print('bb')
        setup_db(self.app, database_path)
        print('cc')
        print(self.app.app_context())
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
        print('dd')

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_actors(self):
        print('A')
        res = self.app.client().get("/actors")
        print(res)
        print(res.data)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        print(data)

'''
def mock_auth0_authentication(*args, **kwargs):
    # Implement your mock authentication logic here
    # For example, you can return a mock token or bypass the authentication entirely
    return "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjRjV0E3ZzdfcGY0V3lITzMtdG12WCJ9.eyJpc3MiOiJodHRwczovL2Rldi0zdGp4b2FpeTM2cXNxamlhLnVrLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NWNjYTZlNDkzMDJhZjEyZTJlMzA2NDAiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTcxMzExNzAyNCwiZXhwIjoxNzEzMTI0MjI0LCJzY29wZSI6IiIsImF6cCI6ImFOQ3R5N0hpQnVFc2RvZ3hTTnB5UnY4dzJhWG96Z1hzIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.fzm1jPPdfc1QUQEAHl_5VZ-6W_LnmyNrEDRJYDz976MMQjfAeN0eHmKjSu5x0vNeG2C__s0fIDhxk-3Q5NETbSlVhiJt1dAqJL52gVbtNsAsW7lRa7P8RdFXnzSgo99hzgPLahuinaB27h161yiHChzDaQUYpY3IrALNiPBBSVucwvbBb_jRyDczQWgYiisFXmrTHSjWkjcmAGel9TSV1sJYAYOK2XclPO7pU1_uPy_6iBldPgj-YMNYnGnuOg-rft0kXVIu15UDPofK-NlHmreaqeemfeR6GHqaEKxaeLTwn7r5DJYsbzDwn1-NABpoGlZ4iP5BQm8UT9QWAGpSIw"

@patch('auth.auth.requires_auth', return_value='{}')
'''
if __name__ == '__main__':
    unittest.main()