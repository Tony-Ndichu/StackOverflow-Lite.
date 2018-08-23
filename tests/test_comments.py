"""

#app/test/test_comments.py
Handles all the tests related to answers
"""
import json
from api import create_app
from flask_testing import TestCase
#from manage import create_tables
from api.database.connect import conn, cur
import os



class Base(TestCase):
    """contains config for testing"""

    def create_app(self):
        """sets config to testing"""
        self.app = create_app('testing')
        return self.app

    def setUp(self):
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.test_client = self.app.test_client()
        self.sample_data1 = {
            'title': 'What is a tuple?',
            'description': 'A tuple is a python data structure'
        }

        self.answer = {
            "answer": "This is a sample answer"
        }

        self.answer2 = {
            "answer": "This is another sample question"
        }

        self.comment = {
            "comment" : "This is a sample comment"
        }

        self.signup_details = {
            "first_name" : "John",
            "last_name" : "Doe",
            "username" : "josdhndoe",
            "email" : "johndsdoe@gmail.com",
            "password" : "absdcd1234"
            } 

        self.login_details = {            
            "username" : "josdhndoe",
            "password" : "absdcd1234"           
            } 



        self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details),
            content_type='application/json')

        self.que = self.client.post(
            '/api/v1/auth/login',
            data=json.dumps(self.login_details),
            content_type='application/json')


    def tearDown(self):
        self.app_context.pop() 
   

class TestApp(Base):

    """Contains all the methods for testing answers"""

    def post_question_for_testing_purposes(self):
        """posts question to enable testing where existing question is needed"""


        access_que = json.loads(self.que.data.decode())
        access_token = access_que['access_token']

        result = self.client.post(
            'api/v1/questions', data=json.dumps(self.sample_data1), content_type='application/json',
             headers = {'Authorization' : 'Bearer '+ access_token })
        return result


    def post_answer_for_testing_purposes(self):
        """posts answer to enable testing where existing answer is needed"""

        access_que = json.loads(self.que.data.decode())
        access_token = access_que['access_token']

        result = self.client.post(
            'api/v1/questions/1/answers',
            data=json.dumps(self.answer),
            content_type='application/json', headers = {'Authorization' : 'Bearer '+ access_token })

        return result

    def test_user_can_add_comment(self):
        """checks that users can add an answer"""
        self.post_question_for_testing_purposes()
        access_que = json.loads(self.que.data.decode())
        access_token = access_que['access_token']

        comment = self.client.post(
            'api/v1/questions/1/answers/1/comment',
            data=json.dumps(self.comment),
            content_type='application/json',  headers = {'Authorization' : 'Bearer '+ access_token })

        self.assertEqual(comment.status_code, 201)