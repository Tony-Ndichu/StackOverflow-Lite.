"""

#app/test/test_answers.py
Handles all the tests related to answers
"""
from tests.base import Base
import json

class TestUsers(Base):
    """contains the test methods"""
    def test_user_can_register(self):
        req = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details_true),
            content_type='application/json')
        mess = json.loads(req.data.decode())


        self.assertEqual(req.status_code, 201)
        self.assertEqual(mess['message'], "Success!! User account has been created successfully")
        

    def test_user_registration_details(self):
        """ensures user registers with valid details"""
        req1 = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details_false_1),
            content_type='application/json')
        mess1 = json.loads(req1.data.decode())

        req2 = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details_false_2),
            content_type='application/json')
        mess2 = json.loads(req2.data.decode())


        req4 = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details_false_4),
            content_type='application/json')
        mess4 = json.loads(req4.data.decode())


        req5 = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details_false_5),
            content_type='application/json')
        mess5 = json.loads(req5.data.decode())

        req6 = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details_false_6),
            content_type='application/json')

        mess6 = json.loads(req6.data.decode())

        req7 = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details_false_7),
            content_type='application/json')

        mess7 = json.loads(req7.data.decode())

        req8 = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details_false_8),
            content_type='application/json')

        mess8 = json.loads(req8.data.decode())

        req9 = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details_false_9),
            content_type='application/json')

        mess9 = json.loads(req9.data.decode())

        req10 = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details_false_10),
            content_type='application/json')

        mess10 = json.loads(req10.data.decode())

        self.assertEqual(req1.status_code, 409)
        self.assertEqual(mess1['message'], "'J' is too short, please add more characters")

        self.assertEqual(req2.status_code, 409)
        self.assertEqual(mess2['message'], "'D' is too short, please add more characters")

        self.assertEqual(req4.status_code, 400)
        self.assertEqual(mess4['message'], "Ooops! '1234' is not a valid input. No spaces or special characters allowed")

        self.assertEqual(req5.status_code, 400)
        self.assertEqual(mess5['message'], "Ooops! '5678' is not a valid input. No spaces or special characters allowed")

        self.assertEqual(req6.status_code, 400)
        self.assertEqual(mess6['message'], "Ooops! 'false6gmailcom' is not a valid email address")

        self.assertEqual(req7.status_code, 400)
        self.assertEqual(mess7['message'], "Ooops! '1111' is not a valid input. No spaces or special characters allowed")

        self.assertEqual(req8.status_code, 400)
        self.assertEqual(mess8['message'], "Ooops! '1111' is not a valid input. No spaces or special characters allowed")

        self.assertEqual(req9.status_code, 400)
        self.assertEqual(mess9['message'], "Ooops! '1111' is not a valid input. No spaces or special characters allowed")

        self.assertEqual(req10.status_code, 409)
        self.assertEqual(mess10['message'], "'J' is too short, please add more characters")





    def test_user_cannot_register_with_existing_credentials(self):
        req = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details),
            content_type='application/json')

        req2 = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details),
            content_type='application/json')

        req3 = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details_used_email),
            content_type='application/json')

        mess = json.loads(req2.data.decode())
        mess2 = json.loads(req3.data.decode())


        self.assertEqual(req2.status_code, 409)
        self.assertEqual(mess['message'], "Sorry, This username has already been taken")

        self.assertEqual(req3.status_code, 409)
        self.assertEqual(mess2['message'], "Sorry, This email is already in use")




    def test_user_can_login(self):

        self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details),
            content_type='application/json')    


        req1 = self.client.post(
            '/api/v1/auth/login',
            data=json.dumps(self.login_details),
            content_type='application/json')
        mess = json.loads(req1.data.decode())


        self.assertEqual(req1.status_code, 200)
        self.assertEqual(mess['message'], "Successfully logged in!!")


    def test_user_cannot_login_With_fake_credentials(self):

        self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details),
            content_type='application/json')    


        req1 = self.client.post(
            '/api/v1/auth/login',
            data=json.dumps(self.login_details_true),
            content_type='application/json')
        mess = json.loads(req1.data.decode())


        req2 = self.client.post(
            '/api/v1/auth/login',
            data=json.dumps(self.login_details_wrong_password),
            content_type='application/json')
        mess = json.loads(req1.data.decode())


        self.assertEqual(req1.status_code, 404)
        self.assertEqual(mess['message'], "Sorry, we have no user with those credentials")

        self.assertEqual(req2.status_code, 404)
        self.assertEqual(mess['message'], "Sorry, we have no user with those credentials")


    def test_user_can_logout(self):

        que = self.client.post(
            '/api/v1/auth/login',
            data=json.dumps(self.login_details),
            content_type='application/json')

        access_que = json.loads(self.que.data.decode())
        access_token = access_que['access_token']

        req = self.client.post(
            '/api/v1/auth/logout',
            content_type='application/json', headers = {'Authorization' : 'Bearer '+ access_token})

        mess = json.loads(req.data.decode())

        self.assertEqual(req.status_code, 200)
        self.assertEqual(mess['message'], "Successfully logged out")

    def test_user_can_fetch_their_profile(self):
        req = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.signup_details_true),
            content_type='application/json')

        que = self.client.post(
            '/api/v1/auth/login',
            data=json.dumps(self.login_details_true),
            content_type='application/json')

        access_que = json.loads(self.que.data.decode())
        access_token = access_que['access_token']

        req2 = self.client.get(
            '/api/v1/auth/profile',
            content_type='application/json', headers = {'Authorization' : 'Bearer '+ access_token})

        mess = json.loads(req2.data.decode())

        self.assertEqual(req2.status_code, 200)
        self.assertEqual(mess['message'], "Success!! Here are your profile details")

    def test_user_can_fetch_all_his_or_her_questions(self):
        """get all questions belonging to the logged in user"""
        result = json.loads(self.que.data.decode())
        access_token = result['access_token']

        response = self.client.get('/api/v1/auth/questions', headers = {'Authorization' : 'Bearer '+ access_token })

        mess = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 404)
        self.assertEqual(mess['message'], "Sorry, you have no questions in our records")

        self.client.post(
            'api/v1/questions',
            data=json.dumps(self.sample_data7),
            content_type='application/json',  headers = {'Authorization' : 'Bearer '+ access_token })

        response2 = self.client.get('/api/v1/auth/questions', headers = {'Authorization' : 'Bearer '+ access_token })

        mess2 = json.loads(response2.data.decode())

        self.assertEqual(response2.status_code, 200)
        self.assertEqual(mess2['message'], "Success!! Here are your questions")


    def test_user_can_fetch_his_most_answered_question(self):
        """get all questions belonging to the logged in user in order of most answered"""
        result = json.loads(self.que.data.decode())
        access_token = result['access_token']


        response = self.client.get('/api/v1/auth/questions/most_answered', headers = {'Authorization' : 'Bearer '+ access_token })

        mess = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 404)
        self.assertEqual(mess['message'], "Sorry, none of your questions have any answers at the moment")

        self.client.post(
            'api/v1/questions',
            data=json.dumps(self.sample_data7),
            content_type='application/json',  headers = {'Authorization' : 'Bearer '+ access_token })

        self.client.post(
            'api/v1/questions/1/answers',
            data=json.dumps(self.answer),
            content_type='application/json',  headers = {'Authorization' : 'Bearer '+ access_token })

        response2 = self.client.get('/api/v1/auth/questions/most_answered', headers = {'Authorization' : 'Bearer '+ access_token })

        mess2 = json.loads(response2.data.decode())

        self.assertEqual(response2.status_code, 200)
        self.assertEqual(mess2['message'], "Here, are your most answered questions")