"""

#app/test/test_answers.py
Handles all the tests related to answers
"""
from tests.base import Base
import json

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

    def test_get_all_questions_when_questions_exist(self):
        """checks that a 200 status code is given when questions are available"""

        self.post_for_testing_purposes()
        result = json.loads(self.que.data.decode())
        access_token = result['access_token']

        response = self.client.get('api/v1/questions', headers = {'Authorization' : 'Bearer '+ access_token })

        mess = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(mess['message'], "Success!! Here are your records")

    def test_get_all_questions_when_no_questions_exist(self):
        """checks that a 404 status code is given when no questions are available"""

        result = json.loads(self.que.data.decode())
        access_token = result['access_token']

        response = self.client.get('api/v1/questions', headers = {'Authorization' : 'Bearer '+ access_token })

        mess = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 404)
        self.assertEqual(mess['message'], "Sorry, but there are no questions at the moment")


    def test_user_can_post_question(self):
        access_que = json.loads(self.que.data.decode())
        access_token = access_que['access_token']

        que = self.client.post(
            'api/v1/questions',
            data=json.dumps(self.sample_data7),
            content_type='application/json',  headers = {'Authorization' : 'Bearer '+ access_token })
        mess = json.loads(que.data.decode())

        self.assertEqual(que.status_code, 201)
        self.assertEqual(mess['message'], "Your question has been added successfully")

    def test_user_cannot_post_same_question_title_twice(self):
        access_que = json.loads(self.que.data.decode())
        access_token = access_que['access_token']

        self.client.post(
            'api/v1/questions',
            data=json.dumps(self.sample_data7),
            content_type='application/json',  headers = {'Authorization' : 'Bearer '+ access_token })

        que=self.client.post(
            'api/v1/questions',
            data=json.dumps(self.sample_data7),
            content_type='application/json',  headers = {'Authorization' : 'Bearer '+ access_token })

        mess = json.loads(que.data.decode())

        self.assertEqual(que.status_code, 409)
        self.assertEqual(mess['message'], "Sorry, This title has already been used in another question")

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

    def test_fetch_a_specific_question(self):
        """checks that user can fetch a specific question"""
        access_que = json.loads(self.que.data.decode())
        access_token = access_que['access_token']

        self.post_for_testing_purposes()

        response = self.client.get('/api/v1/questions/1', headers = {'Authorization' : 'Bearer '+ access_token })
        response2 = self.client.get('/api/v1/questions/10', headers = {'Authorization' : 'Bearer '+ access_token })

        mess = json.loads(response.data.decode())
        mess2 = json.loads(response2.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(mess['message'], "Successfully retrieved question")

        self.assertEqual(response2.status_code, 404)
        self.assertEqual(mess2['message'], "Oops, that question is missing")


    def test_user_can_delete_question(self):
        """checks that user can delete a specific question"""
        access_que = json.loads(self.que.data.decode())
        access_token = access_que['access_token']

        self.post_for_testing_purposes()

        result = self.client.delete(
            'api/v1/questions/1',
            content_type="application/json", headers = {'Authorization' : 'Bearer '+ access_token })

        result2 = self.client.delete(
            'api/v1/questions/10',
            content_type="application/json", headers = {'Authorization' : 'Bearer '+ access_token })

        mess = json.loads(result.data.decode())
        mess2 = json.loads(result2.data.decode())

        self.assertEqual(result.status_code, 200)
        self.assertEqual(mess['message'], "Success!! The question has been deleted.")

        self.assertEqual(result2.status_code, 404)
        self.assertEqual(mess2['message'], "Sorry, we couldn't find that question, it may have already been deleted")

    def test_user_must_enter_question_id_as_integer_in_uri(self):
        """checks that users cant do something like 'api/v1/questions/one """
        self.post_for_testing_purposes()

        response = self.client.get('/api/v1/questions/one')

        mess = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 400)
        self.assertEqual(mess['message'], "Sorry, questionid must be a number or an integer")

    def test_user_must_have_posted_question_to_delete_it(self):
        """checks that user is owner of question before deleting it"""

        access_que = json.loads(self.que.data.decode())
        access_token = access_que['access_token']

        self.post_for_testing_purposes()

        user2_signup = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details_true),
            content_type='application/json')

        user2_login = self.que = self.client.post(
            '/api/v1/auth/login',
            data=json.dumps(self.login_details_true),
            content_type='application/json')

        result = json.loads(user2_login.data.decode())
        access_token2 = result['access_token']

        user2_que = self.client.post(
            'api/v1/questions',
            data=json.dumps(self.sample_data7),
            content_type='application/json',  headers = {'Authorization' : 'Bearer '+ access_token2 })

        user2_delete_que_1 = self.client.delete(
            'api/v1/questions/1',
            content_type="application/json", headers = {'Authorization' : 'Bearer '+ access_token2 })

        mess = json.loads(user2_delete_que_1.data.decode())

        self.assertEqual(user2_delete_que_1.status_code, 401)
        self.assertEqual(mess['message'], "Sorry, you can't delete this question, only owner has permission")

    def deleting_a_question_also_deletes_its_answers(self):
        """ensures that all a question's answers are deleted when the question is deleted"""

        access_que = json.loads(self.que.data.decode())
        access_token = access_que['access_token']

        self.post_for_testing_purposes()

        self.client.post(
            'api/v1/questions/1/answers',
            data=json.dumps(self.answer),
            content_type='application/json',  headers = {'Authorization' : 'Bearer '+ access_token })

        result = self.client.delete(
            'api/v1/questions/1',
            content_type="application/json", headers = {'Authorization' : 'Bearer '+ access_token })

        mess = json.loads(result.data.decode())

        self.assertEqual(result.status_code, 200)
        self.assertEqual(mess['message'], "Success!! The question has been deleted.")