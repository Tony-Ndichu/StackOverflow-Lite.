"""

#app/api/models/answer.py
This is the answer model
"""
from datetime import datetime

class AnswerModel():
    """handles operations for the answers"""

    def __init__(self, answer):
        self.answer = answer
        self.answer_date = datetime.now()

    def make_answer_dict(self, id_num, questionid):
        """receives answer object and turns it to dict"""
        return dict(
            answer=self.answer,
            answer_id=id_num,
            answer_date=self.answer_date,
            question_id=questionid,
            votes=0,
            accept_status=False,
            date_accepted=None,
        )


