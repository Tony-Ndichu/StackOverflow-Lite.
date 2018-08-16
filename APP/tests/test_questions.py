from unittest import TestCase
from api.questions import views
from api import create_app
from flask_testing import TestCase
import json
from api.questions.views import QUESTION_LIST
from api.answers.views import ANSWER_LIST

class Base(TestCase):

    def create_app(self):
        self.app = create_app('testing')
        return self.app

    def setUp(self):
        self.client = self.app.test_client()
        self.sample_data1 = {
            'description' : 'A tuple is a python data structure'
        }

        self.sample_data2 = {
            'title' : 'What is a title?'
        }

        self.sample_data3 = {
            'title' : '',
            'description' : 'A tuple is a python data structure'

        }

        self.sample_data4 = {
            'title' : 'What is a title?',
            'description' : ''

        }

        self.sample_data5 = {
            'title' : '12345',
            'description' : 'A tuple is a python data structure'

        }

        self.sample_data6 = {
            'title' : 'What is a title?',
            'description' : '12345'

        }

        self.sample_data7 = {
          
            'title' : 'What is a tuple?',
            'description' : 'A tuple is a python data structure'
        }

    def tearDown(self):
        '''make the questions list empty after each test case'''
        del QUESTION_LIST[:]

class TestApp(Base):

   

    def post_for_testing_purposes(self):
        result = self.client.post(
            'api/v1/questions',
            data=json.dumps(self.sample_data7),
            content_type='application/json')
        return result


    def test_get_all_questions_status_code_when_no_questions(self):
        
        response = self.client.get('/api/v1/questions')
        self.assertEqual(response.status_code, 404)

    def test_get_all_questions_status_code_when_questions_exist(self):
        self.post_for_testing_purposes()

        response = self.client.get('/api/v1/questions')
        self.assertEqual(response.status_code, 200)

    def test_post_question_with_no_title(self):
    
        que = self.client.post(
            '/api/v1/questions',
            data=self.sample_data1)
                   
        result = json.loads(que.data.decode())
        self.assertEqual(
            result['message'], {'title' : 'Please enter a title.'})
        self.assertEqual(que.status_code, 400)


    def test_post_question_with_no_description(self):
    
        que = self.client.post(
            '/api/v1/questions',
            data=self.sample_data2)
                   
        result = json.loads(que.data.decode())
        self.assertEqual(
            result['message'], {'description' : 'Please enter a description.'})
        self.assertEqual(que.status_code, 400)

    def test_post_question_with_empty_string_title(self):
    
        que = self.client.post(
            '/api/v1/questions',
            data=self.sample_data3)
                   
        result = json.loads(que.data.decode())
        self.assertEqual(
            result['message'], 'You cannot post an empty title, Please add a title')
        self.assertEqual(que.status_code, 409)

    def test_post_question_with_empty_string_description(self):
    
        que = self.client.post(
            '/api/v1/questions',
            data=self.sample_data4)
                   
        result = json.loads(que.data.decode())
        self.assertEqual(
            result['message'], 'You cannot post an empty description, Please add a description')
        self.assertEqual(que.status_code, 409)

    def test_post_question_where_title_is_only_digits(self):
    
        que = self.client.post(
            '/api/v1/questions',
            data=self.sample_data5)
                   
        result = json.loads(que.data.decode())
        self.assertEqual(
            result['message'], 'You cannot have a title with digits only, Please describe with some words')
        self.assertEqual(que.status_code, 409)

    def test_post_question_where_description_is_only_digits(self):
    
        que = self.client.post(
            '/api/v1/questions',
            data=self.sample_data6)
                   
        result = json.loads(que.data.decode())
        self.assertEqual(
            result['message'], 'You cannot have a description with digits only, Please describe with some words')
        self.assertEqual(que.status_code, 409)

    def test_fetch_a_question(self):
        
        self.post_for_testing_purposes()

        response = self.client.get('/api/v1/questions/1')
        self.assertEqual(response.status_code, 200)

    def test_user_can_delete_question(self):

        self.post_for_testing_purposes()

        result = self.client.delete(
            'api/v1/questions/1',
            content_type="application/json")

        self.assertEqual(result.status_code, 200)