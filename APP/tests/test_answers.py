from unittest import TestCase

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
            'title' : 'What is a tuple?',
            'description' : 'A tuple is a python data structure'
        }

        self.answer = {
            "answer" : "This is a sample answer"
        }

        self.answer2 = {
            "answer" : "This is another sample question"
        }

        self.empty_answer = {
            'answer' : ""
        }
    def tearDown(self):
        '''make the questions list empty after each test case'''
        del QUESTION_LIST[:]
        del ANSWER_LIST[:]

class TestApp(Base):   

    def post_question_for_testing_purposes(self):
        result = self.client.post('api/v1/questions', data=json.dumps(self.sample_data1),content_type='application/json')
        return result

    def post_answer_for_testing_purposes(self):
        result = self.client.post(
            'api/v1/questions/1/answers',
            data=json.dumps(self.answer),
            content_type='application/json')

        return result

    def test_user_can_answer_question(self):

        self.post_question_for_testing_purposes()

        answer = self.client.post(
            'api/v1/questions/1/answers',
            data=json.dumps(self.answer),
            content_type='application/json')

        self.assertEqual(answer.status_code, 201)

    def test_user_cannot_answer_with_empty_content(self):

        self.post_question_for_testing_purposes()

        result = self.client.post(
            'api/v1/questions/1/answers',
            data=json.dumps(self.empty_answer),
            content_type='application/json')

        self.assertEqual(result.status_code, 409)

    def test_user_fetch_answers_for_specific_question(self):
        self.post_question_for_testing_purposes()

        self.client.post(
            'api/v1/questions/1/answers',
            data=json.dumps(self.answer),
            content_type='application/json')

        answer = self.client.get(
            'api/v1/questions/1/answers', content_type="application/json")

        self.assertNotEqual(answer.status_code, 200)








	

