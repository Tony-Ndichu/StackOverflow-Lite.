class QuestionModel():
  
    def __init__(self, title, description):
            ''' constructor method to give a question its attributes'''
            self.title = title
            self.description = description


    def make_dict(self, questionId):
        ''' turns the question object to a dictionary'''
        return dict(
            title=self.title,
            description=self.description,
            question_id = questionId
        )