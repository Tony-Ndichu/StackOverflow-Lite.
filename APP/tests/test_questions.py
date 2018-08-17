"""

#app/tests/test_questions
Handles question-related tests
"""

import json
from flask_testing import TestCase
from api import create_app
from api.questions.views import QUESTION_LIST
from api.answers.views import ANSWER_LIST


class Base(TestCase):
    """Base class to be inherited"""

    def create_app(self):
        """sets up test config"""
        self.app = create_app('testing')
        return self.app

    def setUp(self):
        """setup to be ran before the tests"""
        self.client = self.app.test_client()
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

    def tearDown(self):
        """empty lists after tests have been run"""
        del QUESTION_LIST[:]
        del ANSWER_LIST[:]


class TestApp(Base):

    """Contains all the methods for testing questions"""

    def post_for_testing_purposes(self):
        """post question to enable testing"""
        result = self.client.post(
            'api/v1/questions',
            data=json.dumps(self.sample_data7),
            content_type='application/json')
        return result

    def test_get_all_questions_status_code_when_no_questions(self):
        """checks that a 404 status code is given when no questions are available"""

        response = self.client.get('/api/v1/questions')
        self.assertEqual(response.status_code, 404)

    def test_get_all_questions_status_code_when_questions_exist(self):
        """checks that a successful 200 status code is given when questions exist"""
        self.post_for_testing_purposes()

        response = self.client.get('/api/v1/questions')
        self.assertEqual(response.status_code, 200)

    def test_post_question_with_no_title(self):
        """checks that user cannot post a question without a title"""
        que = self.client.post(
            '/api/v1/questions',
            data=self.sample_data1)

        result = json.loads(que.data.decode())
        self.assertEqual(
            result['message'], {'title': 'Please enter a title.'})
        self.assertEqual(que.status_code, 400)

    def test_post_question_with_no_description(self):
        """checks that a user cannot post a question without a description"""
        que = self.client.post(
            '/api/v1/questions',
            data=self.sample_data2)

        result = json.loads(que.data.decode())
        self.assertEqual(
            result['message'], {'description': 'Please enter a description.'})
        self.assertEqual(que.status_code, 400)

    def test_post_question_with_empty_string_title(self):
        """checks that user cannot post an empty string title"""
        que = self.client.post(
            '/api/v1/questions',
            data=self.sample_data3)

        result = json.loads(que.data.decode())
        self.assertEqual(
            result['message'], 'You cannot post an empty title, Please add a title')
        self.assertEqual(que.status_code, 409)

    def test_post_question_with_empty_string_description(self):
        """checks that user cannot post an empty string description"""
        que = self.client.post(
            '/api/v1/questions',
            data=self.sample_data4)

        result = json.loads(que.data.decode())
        self.assertEqual(
            result['message'], 'You cannot post an empty description, Please add a description')
        self.assertEqual(que.status_code, 409)

    def test_post_question_where_title_is_only_digits(self):
        """checks that user cannot post a title with digits only"""
        que = self.client.post(
            '/api/v1/questions',
            data=self.sample_data5)

        result = json.loads(que.data.decode())
        self.assertEqual(
            result['message'],
            'You cannot have a title with digits only, Please describe with some words')
        self.assertEqual(que.status_code, 409)

    def test_post_question_where_description_is_only_digits(self):
        """checks that user cannot post a description with digits only"""

        que = self.client.post(
            '/api/v1/questions',
            data=self.sample_data6)

        result = json.loads(que.data.decode())
        self.assertEqual(
            result['message'],
            'You cannot have a description with digits only, Please describe with some words')
        self.assertEqual(que.status_code, 409)

    def test_fetch_a_question(self):
        """checks that user can fetch a specific question"""
        self.post_for_testing_purposes()

        response = self.client.get('/api/v1/questions/1')
        self.assertEqual(response.status_code, 200)

    def test_user_can_delete_question(self):
        """checks that user can delete a specific question"""
        self.post_for_testing_purposes()

        result = self.client.delete(
            'api/v1/questions/1',
            content_type="application/json")

        self.assertEqual(result.status_code, 200)
