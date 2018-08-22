"""
#app/api/answers/view.py
This is the module that handles answers and their methods
"""
from datetime import datetime
from flask import Flask, Blueprint
from flask_restful import reqparse, Api, Resource
from ..common import validator
from ..models.answer import AnswerModel
from ..models.question import QuestionModel
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


APP = Flask(__name__)


ANSWER_BLUEPRINT = Blueprint('answer', __name__)
API = Api(ANSWER_BLUEPRINT, prefix='/api/v1')


class Answer(Resource):
    """This class deals with posting answers and getting answers to specific questions"""
    parser = reqparse.RequestParser()
    parser.add_argument('answer', type=str, required=True,
                        help='Please enter an answer.')

    @classmethod
    @jwt_required
    def post(cls, questionid):
        """Handles posting of questions"""

        data = cls.parser.parse_args()

        QUESTION_LIST = QuestionModel.get_all_questions()

        check_question = validator.check_using_id(
            QUESTION_LIST, int(questionid))

        if not check_question:
            return {'message': 'Oops, that question is missing, you cant add answers to it'}, 404

        check_answer = validator.check_for_answer(data['answer'])

        if check_answer:
            return {"message":
                    "Please enter a different answer, you cannot enter the same answer twice"}, 409

        check_quality = validator.check_quality(data['answer'])

        if check_quality:
            return {"message": check_quality}, 409

        current_user_id = get_jwt_identity()

        save_answer = AnswerModel.save_answer(
            current_user_id, int(questionid), data['answer'])

        if save_answer:
            return {"message": "Success!! Your answer has been added"}, 201
        return {"message": "Sorry, an error occured during saving"}

    @classmethod
    def get(cls, questionid):
        """Handles getting answers for a specific question"""

        check_answer = validator.find_answers_to_a_question(
            ANSWER_LIST, int(questionid))

        if check_answer:
            return check_answer, 200
        return {"message": "Sorry, this question has no answers at the moment."}, 404


class AcceptAnswer(Resource):
    """Handles updating an answer's status"""
    @classmethod
    @jwt_required
    def put(cls, question_id, answer_id):
        """Handles accepting an answer"""

        current_user_id = get_jwt_identity()
        confirm_that_user_asked_que = AnswerModel.confirm_que_poster(
            current_user_id, int(question_id))

        if confirm_that_user_asked_que:
            return {"message": confirm_that_user_asked_que}, 401

        check_if_already_accepted = AnswerModel.check_if_already_accepted(
            int(question_id))

        if check_if_already_accepted:
            return {"message": check_if_already_accepted}, 409

        accept_answer = AnswerModel.accept_answer(int(answer_id))

        if accept_answer:
            return {"message": "Success!! You have accepted this answer"}, 201


API.add_resource(Answer, "/questions/<questionid>/answers")
API.add_resource(
    AcceptAnswer, "/questions/<question_id>/answers/<answer_id>/accept")

if __name__ == '__main__':
    APP.run()
