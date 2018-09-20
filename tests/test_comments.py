"""

#app/test/test_comments.py
Handles all the tests related to answers
"""
from tests.base import Base
import json

class TestApp(Base):

    """Contains all the methods for testing answers"""

    def post_question_for_testing_purposes(self):
        """posts question to enable testing where existing question is needed"""


        access_que = json.loads(self.que.data.decode())
        access_token = access_que['access_token']

        result = self.client.post(
            'api/v1/questions', data=json.dumps(self.sample_data_que), content_type='application/json',
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
        self.post_answer_for_testing_purposes()
        access_que = json.loads(self.que.data.decode())
        access_token = access_que['access_token']

        comment = self.client.post(
            'api/v1/questions/1/answers/1/comments',
            data=json.dumps(self.comment),
            content_type='application/json',  headers = {'Authorization' : 'Bearer '+ access_token })

        mess = json.loads(comment.data.decode())

        self.assertEqual(comment.status_code, 201)
        self.assertEqual(mess['message'], "Success!! Your comment has been added")

    def test_user_cannot_add_comment_to_an_answer_that_doesnt_exist(self):
        """checks that answer exists inorder for comment to be added"""
        self.post_question_for_testing_purposes()
        self.post_answer_for_testing_purposes()
        access_que = json.loads(self.que.data.decode())
        access_token = access_que['access_token']

        comment = self.client.post(
            'api/v1/questions/1/answers/3/comments',
            data=json.dumps(self.comment),
            content_type='application/json',  headers = {'Authorization' : 'Bearer '+ access_token })

        mess = json.loads(comment.data.decode())

        self.assertEqual(comment.status_code, 404)
        self.assertEqual(mess['message'], "Oops, that answer is missing, you cant add comments to it")


    def test_user_must_enter_answer_id_as_integer_in_uri(self):
        """checks that users cant do something like 'api/v1/questions/1/answers/one/comments"""
        self.post_question_for_testing_purposes()
        self.post_answer_for_testing_purposes()
        access_que = json.loads(self.que.data.decode())
        access_token = access_que['access_token']

        comment = self.client.post(
            'api/v1/questions/1/answers/one/comments',
            data=json.dumps(self.comment),
            content_type='application/json',  headers = {'Authorization' : 'Bearer '+ access_token })

        mess = json.loads(comment.data.decode())

        self.assertEqual(comment.status_code, 400)
        self.assertEqual(mess['message'], "Sorry, answerid must be a number or an integer")


    def test_comment_quality_is_checked(self):
        """checks that an answer isnt too short for example"""

        self.post_question_for_testing_purposes()
        self.post_answer_for_testing_purposes()
        access_que = json.loads(self.que.data.decode())
        access_token = access_que['access_token']

        comment = self.client.post(
            'api/v1/questions/1/answers/1/comments',
            data=json.dumps(self.comment_short),
            content_type='application/json',  headers = {'Authorization' : 'Bearer '+ access_token })

        comment2 = self.client.post(
            'api/v1/questions/1/answers/1/comments',
            data=json.dumps(self.comment_empty),
            content_type='application/json',  headers = {'Authorization' : 'Bearer '+ access_token })

        mess = json.loads(comment.data.decode())
        mess2 = json.loads(comment2.data.decode())

        self.assertEqual(comment.status_code, 409)
        self.assertEqual(mess['message'], "Too Short, Please add more input")

        self.assertEqual(comment2.status_code, 400)
        self.assertEqual(mess2['message']['comment'], "Please enter a comment.")