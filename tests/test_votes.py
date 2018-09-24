"""

#app/test/test_answers.py
Handles all the tests related to answers
"""
from tests.base import Base
import json


class TestApp(Base):

    """Contains all the methods for testing votes"""

    def post_question_for_testing_purposes(self):
        """posts question to enable testing where existing question is needed"""


        access_que = json.loads(self.que.data.decode())
        access_token = access_que['access_token']

        result = self.client.post(
            'api/v1/questions', data=json.dumps(self.sample_data7), content_type='application/json',
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

    def test_user_can_upvote_answer(self):
        """checks that a user can upvote an answer"""
        self.post_question_for_testing_purposes()
        self.post_answer_for_testing_purposes()
        result = json.loads(self.que.data.decode())
        access_token = result['access_token']

        accept_que=self.client.post(
            'api/v1/answers/1/upvote',
            data=json.dumps(self.answer2),
            content_type='application/json',  headers = {'Authorization' : 'Bearer '+ access_token })

        mess = json.loads(accept_que.data.decode())

        self.assertEqual(accept_que.status_code, 200)
        self.assertEqual(mess['message'], "Success!! You have upvoted this answer")

    def test_user_can_remove_upvote(self):
        """checks that a user can undo their upvote"""
        self.post_question_for_testing_purposes()
        self.post_answer_for_testing_purposes()
        result = json.loads(self.que.data.decode())
        access_token = result['access_token']

        self.client.post(
            'api/v1/answers/1/upvote',
            data=json.dumps(self.answer2),
            content_type='application/json',  headers = {'Authorization' : 'Bearer '+ access_token })

        accept_que=self.client.post(
            'api/v1/answers/1/upvote',
            data=json.dumps(self.answer2),
            content_type='application/json',  headers = {'Authorization' : 'Bearer '+ access_token })

        mess = json.loads(accept_que.data.decode())

        self.assertEqual(accept_que.status_code, 200)
        self.assertEqual(mess['message'], "Success, you have undone your upvote")

    def test_user_can_downvote_answer(self):
        """checks that a user can downvote an answer"""
        self.post_question_for_testing_purposes()
        self.post_answer_for_testing_purposes()
        result = json.loads(self.que.data.decode())
        access_token = result['access_token']

        accept_que=self.client.post(
            'api/v1/answers/1/downvote',
            data=json.dumps(self.answer2),
            content_type='application/json',  headers = {'Authorization' : 'Bearer '+ access_token })

        mess = json.loads(accept_que.data.decode())

        self.assertEqual(accept_que.status_code, 200)
        self.assertEqual(mess['message'], "Success!! You have downvoted this answer")

    def test_user_can_remove_downvote(self):
        """checks that a user can remove downvote"""
        self.post_question_for_testing_purposes()
        self.post_answer_for_testing_purposes()
        result = json.loads(self.que.data.decode())
        access_token = result['access_token']

        self.client.post(
            'api/v1/answers/1/downvote',
            data=json.dumps(self.answer2),
            content_type='application/json',  headers = {'Authorization' : 'Bearer '+ access_token })

        accept_que=self.client.post(
            'api/v1/answers/1/downvote',
            data=json.dumps(self.answer2),
            content_type='application/json',  headers = {'Authorization' : 'Bearer '+ access_token })

        mess = json.loads(accept_que.data.decode())

        self.assertEqual(accept_que.status_code, 200)
        self.assertEqual(mess['message'], "Success, you have undone your downvote")
