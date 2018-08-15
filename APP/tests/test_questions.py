from unittest import TestCase
from api.questions import views
from api import create_app
from flask_testing import TestCase
import json


class TestApp(TestCase):


    def create_app(self):
        self.app = create_app('testing')
        return self.app

    def setUp(self):
        self.client = self.app.test_client()

    def test_get_all_questions_status_code_when_no_questions(self):
        response = self.client.get('/api/v1/questions')
        self.assertEqual(response.status_code, 404)

    def test_get_all_questions_status_code_when_questions_exist(self):
        response = self.client.get('/api/v1/questions')
        self.assertNotEqual(response.status_code, 200)

    