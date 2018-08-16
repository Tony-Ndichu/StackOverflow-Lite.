'''answer model'''
from datetime import datetime


class AnswerModel():
    '''answer class conaining answer related operations'''

    def __init__(self, answer):
        '''constructor method to initialize an object'''
        self.answer = answer
        self.answer_date = datetime.now()

    def make_answer_dict(self, id_num, questionid):
        '''take user object and return __dict__ representation'''
        return dict(
            answer=self.answer,
            answer_id=id_num,
            answer_date=self.answer_date,            
            question_id=questionid,
            votes=0,
            accept_status=False,
            date_accepted= None ,
        )
