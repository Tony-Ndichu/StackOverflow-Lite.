"""

#app/test/test_users.py
Handles all the tests related to answers
"""
import json
from flask_testing import TestCase
import os


class Base(TestCase):
    """contains config for testing"""

    def create_app(self):
        """sets config to testing"""
        self.app = create_app('testing')
        return self.app

    def setUp(self):
        os.environ['APP_SETTINGS'] = 'testing'
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.test_client = self.app.test_client()
        self.signup_details = {
            "first_name" : "John",
            "last_name" : "Doe",
            "username" : "johndoe",
            "email" : "johndoe@gmail.com",
            "password" : "absdcd1234"
            } 

    def tearDown(self):
        self.app_context.pop()     


class TestUsers(Base):
    """contains the test methods"""


    def test_user_can_signup(self):
        """checks that users can add an answer"""

        req = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details),
            content_type='application/json')

        self.assertEqual(req.status_code, 409)



   