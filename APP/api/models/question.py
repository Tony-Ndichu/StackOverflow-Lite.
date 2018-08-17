""""

#app/api/models/question.py
This is the question model
"""


class QuestionModel():
    """this class handles question-related operations"""

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def make_dict(self, question_id):
        """receives question object and turns it to dict"""
        return dict(
            title=self.title,
            description=self.description,
            question_id=question_id
        )
