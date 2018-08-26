"""

#app/test/test_answers.py
Handles all the tests related to answers
"""
import json
from api import create_app
from flask_testing import TestCase
from api.database.connect import conn, cur
import os
from api.manage import tables


class Base(TestCase):
    """contains config for testing"""

    def create_app(self):
        """sets config to testing"""
        self.app = create_app('testing')
        return self.app

    def setUp(self):
        tables("create")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.test_client = self.app.test_client()
        self.signup_details = {
            "first_name" : "John",
            "last_name" : "Doe",
            "username" : "josdhndoe",
            "email" : "johndsdoe@gmail.com",
            "password" : "absdcd1234"
            } 

        self.signup_details_false_1 = {
            "first_name" : "J",
            "last_name" : "Doe",
            "username" : "false1",
            "email" : "false1@gmail.com",
            "password" : "absdcd1234"
            } 

        self.signup_details_false_2 = {
            "first_name" : "John",
            "last_name" : "D",
            "username" : "false2",
            "email" : "false2@gmail.com",
            "password" : "absdcd1234"
            } 

        self.signup_details_false_3 = {
            "first_name" : "Johntftfghjjhvvjvjhvjvj",
            "last_name" : "Doe",
            "username" : "false3",
            "email" : "false3@gmail.com",
            "password" : "absdcd1234"
            } 

        self.signup_details_false_4 = {
            "first_name" : "1234",
            "last_name" : "Doe",
            "username" : "false4",
            "email" : "false4@gmail.com",
            "password" : "absdcd1234"
            } 

        self.signup_details_false_5 = {
            "first_name" : "John",
            "last_name" : "5678",
            "username" : "false5",
            "email" : "false5@gmail.com",
            "password" : "absdcd1234"
            } 

        self.login_details = {            
            "username" : "josdhndoe",
            "password" : "absdcd1234"           
            } 

        self.login_details_false1 = {            
            "username" : "josdhndoe",
            "password" : "absdcd"           
            } 

        self.login_details_false2 = {            
            "username" : "josd",
            "password" : "absdcd1234"           
            } 

    def tearDown(self):
        self.app_context.pop()  
        tables("drop")  


class TestUsers(Base):
    """contains the test methods"""
    def test_user_can_register(self):
        req = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details),
            content_type='application/json')

        self.assertEqual(req.status_code, 201)

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

        req3 = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details_false_3),
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
        self.assertEqual(req2.status_code, 409)
        self.assertEqual(req3.status_code, 409)
        self.assertEqual(req4.status_code, 409)
        self.assertEqual(req5.status_code, 409)




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
        self.assertEqual(req3.status_code, 404)



    def test_user_can_logout(self):

        que = self.client.post(
            '/api/v1/auth/login',
            data=json.dumps(self.login_details),
            content_type='application/json')

        result = json.loads(que.data.decode())

        req = self.client.post(
            '/api/v1/auth/logout',
            content_type='application/json')

        self.assertEqual(req.status_code, 200)