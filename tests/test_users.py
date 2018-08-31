"""

#app/test/test_answers.py
Handles all the tests related to answers
"""
from tests.base import Base
import json

class TestUsers(Base):
    """contains the test methods"""
    def test_user_can_register(self):
        req = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details_true),
            content_type='application/json')

        self.assertEqual(req.status_code, 201)
        self.assertEqual(req.message, "Success!! User account has been created successfully")
        


    def test_user_registration_details(self):
        """ensures user registers with valid details"""
        req1 = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details_false_1),
            content_type='application/json')

        req2 = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details_false_2),
            content_type='application/json')

        req4 = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details_false_4),
            content_type='application/json')

        req5 = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details_false_5),
            content_type='application/json')

        self.assertEqual(req1.status_code, 409)
        self.assertIn(req1.message, "is too short, please add more characters")

        self.assertEqual(req2.status_code, 409)
        self.assertIn(req2.message, "is too short, please add more characters")

        self.assertEqual(req4.status_code, 400)
        self.assertEqual(req4.message, "First name cannot be digits only")

        self.assertEqual(req5.status_code, 400)
        self.assertEqual(req5.message, "First name cannot be digits only")





    def test_user_cannot_register_with_existing_credentials(self):
        req = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details),
            content_type='application/json')

        req2 = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details),
            content_type='application/json')

        self.assertEqual(req2.status_code, 409)
        self.assertEqual(req2.message, "Sorry, This username has already been taken")




    def test_user_can_login(self):

        self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details),
            content_type='application/json')    


        req1 = self.client.post(
            '/api/v1/auth/login',
            data=json.dumps(self.login_details),
            content_type='application/json')

        req3 = self.client.post(
            '/api/v1/auth/login',
            data=json.dumps(self.login_details_false2),
            content_type='application/json')

        self.assertEqual(req1.status_code, 200)
        self.assertEqual(req1.message, "Successfully logged in!!")





    def test_user_can_logout(self):

        que = self.client.post(
            '/api/v1/auth/login',
            data=json.dumps(self.login_details),
            content_type='application/json')

        access_que = json.loads(self.que.data.decode())
        access_token = access_que['access_token']

        req = self.client.post(
            '/api/v1/auth/logout',
            content_type='application/json', headers = {'Authorization' : 'Bearer '+ access_token})

        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.message, "Successfully logged out")
