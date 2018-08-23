"""

#app/test/test_answers.py
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
            'description': 'A tuple is a python data structure'
        }

        self.sample_data2 = {
            'title': 'What is a title?'
        }

        self.sample_data3 = {
            'title': '',
            'description': 'A tuple is a python data structure'

        }

        self.sample_data4 = {
            'title': 'What is a title?',
            'description': ''

        }

        self.sample_data5 = {
            'title': '12345',
            'description': 'A tuple is a python data structure'

        }

        self.sample_data6 = {
            'title': 'What is a title?',
            'description': '12345'

        }

        self.sample_data7 = {

            'title': 'What is a tuple?',
            'description': 'A tuple is a python data structure'
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

    """Contains all the methods for testing questions"""


    def post_for_testing_purposes(self):
        """post question to enable testing"""
        result = json.loads(self.que.data.decode())
        access_token = result['access_token']

        result = self.client.post(
            'api/v1/questions',
            data=json.dumps(self.sample_data7),
            content_type='application/json',  headers = {'Authorization' : 'Bearer '+ access_token })
        return result

    def test_get_all_questions(self):
        """checks that a 404 status code is given when no questions are available"""
       
        result = json.loads(self.que.data.decode())
        access_token = result['access_token']

        response = self.client.get('/api/v1/questions', headers = {'Authorization' : 'Bearer '+ access_token })
        self.assertEqual(response.status_code, 200)

    def test_get_all_questions_status_code_when_questions_exist(self):
        """checks that a successful 200 status code is given when questions exist"""
        result = json.loads(self.que.data.decode())
        access_token = result['access_token']

        response = self.client.get('/api/v1/questions', headers = {'Authorization' : 'Bearer '+ access_token })
        self.assertEqual(response.status_code, 200)

    def test_post_question_with_no_title(self):
        """checks that user cannot post a question without a title"""

        access_que = json.loads(self.que.data.decode())
        access_token = access_que['access_token']

        que = self.client.post(
            '/api/v1/questions', headers = {'Authorization' : 'Bearer '+ access_token }, 
            data=self.sample_data1)

        result = json.loads(que.data.decode())
        self.assertEqual(
            result['message'], {'title': 'Please enter a title.'})
        self.assertEqual(que.status_code, 400)

    def test_post_question_with_no_description(self):
        """checks that a user cannot post a question without a description"""

        access_que = json.loads(self.que.data.decode())
        access_token = access_que['access_token']

        que = self.client.post(
            '/api/v1/questions',
            data=self.sample_data2, headers = {'Authorization' : 'Bearer '+ access_token })

        result = json.loads(que.data.decode())
        self.assertEqual(
            result['message'], {'description': 'Please enter a description.'})
        self.assertEqual(que.status_code, 400)

    def test_post_question_with_empty_string_title(self):
        """checks that user cannot post an empty string title"""
        access_que = json.loads(self.que.data.decode())
        access_token = access_que['access_token']

        que = self.client.post(
            '/api/v1/questions',
            data=self.sample_data3, headers = {'Authorization' : 'Bearer '+ access_token })

        result = json.loads(que.data.decode())
        self.assertEqual(
            result['message'], 'You cannot post an empty title, Please add a title')
        self.assertEqual(que.status_code, 409)

    def test_post_question_with_empty_string_description(self):
        """checks that user cannot post an empty string description"""
        access_que = json.loads(self.que.data.decode())
        access_token = access_que['access_token']

        que = self.client.post(
            '/api/v1/questions',
            data=self.sample_data4, headers = {'Authorization' : 'Bearer '+ access_token })

        result = json.loads(que.data.decode())
        self.assertEqual(
            result['message'], 'You cannot post an empty description, Please add a description')
        self.assertEqual(que.status_code, 409)

    def test_post_question_where_title_is_only_digits(self):
        """checks that user cannot post a title with digits only"""

        access_que = json.loads(self.que.data.decode())
        access_token = access_que['access_token']

        que = self.client.post(
            '/api/v1/questions',
            data=self.sample_data5, headers = {'Authorization' : 'Bearer '+ access_token })

        result = json.loads(que.data.decode())
        self.assertEqual(
            result['message'],
            'You cannot post a title with digits only, Please describe with some words')
        self.assertEqual(que.status_code, 409)

    def test_post_question_where_description_is_only_digits(self):
        """checks that user cannot post a description with digits only"""

        access_que = json.loads(self.que.data.decode())
        access_token = access_que['access_token']

        que = self.client.post(
            '/api/v1/questions',
            data=self.sample_data6, headers = {'Authorization' : 'Bearer '+ access_token })

        result = json.loads(que.data.decode())
        self.assertEqual(
            result['message'],
            'You cannot post a description with digits only, Please describe with some words')
        self.assertEqual(que.status_code, 409)

    def test_fetch_a_question(self):
        """checks that user can fetch a specific question"""
        access_que = json.loads(self.que.data.decode())
        access_token = access_que['access_token']

        self.post_for_testing_purposes()

        response = self.client.get('/api/v1/questions/1', headers = {'Authorization' : 'Bearer '+ access_token })
        self.assertEqual(response.status_code, 200)

    def test_user_can_delete_question(self):
        """checks that user can delete a specific question"""
        access_que = json.loads(self.que.data.decode())
        access_token = access_que['access_token']

        self.post_for_testing_purposes()

        result = self.client.delete(
            'api/v1/questions/1',
            content_type="application/json", headers = {'Authorization' : 'Bearer '+ access_token })

        self.assertEqual(result.status_code, 200)



    def test_user_can_fetch_all_his_or_her_questions(self):
        """get all questions belonging to the logged in user"""
        result = json.loads(self.que.data.decode())
        access_token = result['access_token']

        self.post_for_testing_purposes()

        response = self.client.get('/api/v1/auth/questions', headers = {'Authorization' : 'Bearer '+ access_token })
        self.assertEqual(response.status_code, 200)


