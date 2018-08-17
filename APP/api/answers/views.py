"""
#app/api/answers/view.py
This is the module that handles answers and their methods
"""
from datetime import datetime
from flask import Flask, Blueprint
from flask_restful import reqparse, Api, Resource
from ..common import validator
from ..models.answer import AnswerModel
from ..questions.views import QUESTION_LIST

APP = Flask(__name__)


ANSWER_BLUEPRINT = Blueprint('answer', __name__)
API = Api(ANSWER_BLUEPRINT, prefix='/api/v1')

ANSWER_LIST = [
    {
        "answer_id": 1,
        "answer": "HGHH",
        "question_id": 1,
        "votes" : 0,
        "accept_status" : False,
        "date_accepted" : None
    },
    {
        "answer_id": 2,
        "answer": "HGHgggfgfgH",
        "question_id": 1,
        "votes" : 0,
        "accept_status" : False,
        "date_accepted" : None
    }
]


class Answer(Resource):
    """This class deals with posting answers and getting answers to specific questions"""
    parser = reqparse.RequestParser()
    parser.add_argument('answer', type=str, required=True,
                        help='Please enter an answer.')

    @classmethod
    def post(cls, questionid):
        """Handles posting of questions"""

        data = cls.parser.parse_args()

        check_question = validator.check_using_id(
            QUESTION_LIST, int(questionid))

        if not check_question:
            return {'message': 'Oops, that question is missing, you cant add answers to it'}, 404

        check_answer = validator.check_for_answer(ANSWER_LIST, data['answer'])

        if check_answer:
            return {"message":
                    "Please enter a different answer, you cannot enter the same answer twice"}, 409

        check_quality = validator.check_quality(data['answer'])

        if check_quality:
            return {"message": check_quality}, 409

        id_num = 1
        for item in ANSWER_LIST:
            id_num += 1

        new_answer = AnswerModel(data['answer'])

        new_answer_dict = new_answer.make_answer_dict(id_num, questionid)

        ANSWER_LIST.append(new_answer_dict)

        return {"message": "Success!! Your answer has been added"}, 201

    @classmethod
    def get(cls, questionid):
        """Handles getting answers for a specific question"""

        check_answer = validator.find_answers_to_a_question(
            ANSWER_LIST, int(questionid))

        if check_answer:
            return check_answer, 200
        return {"message": "Sorry, this question has no answers at the moment."}, 404


class AcceptAnswer(Resource):
    """This class handles accepting answers as the official answer to questions"""

    @classmethod
    def put(cls, answerid):
        """Handles updating an answer to 'accepted' status """

        check_id = validator.check_using_id(ANSWER_LIST, int(answerid))

        if not check_id:
            return {"message": "Sorry, we can't seem to find that answer"}, 404

        if check_id['accept_status']:
            return {"message": "You have already accepted this answer"}, 409

        check_id['accept_status'] = True
        check_id['date_accepted'] = datetime.now()
        return {"message": "Success!! You have accepted this answer"}, 200


API.add_resource(Answer, "/questions/<questionid>/answers")
API.add_resource(AcceptAnswer, "/questions/<questionid>/answers/<answerid>")

if __name__ == '__main__':
    APP.run()
