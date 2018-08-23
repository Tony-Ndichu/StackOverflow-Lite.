"""
#app/api/answers/views.py
This is the module that handles question operations and their methods
"""

from flask import Flask, Blueprint
from flask_restful import reqparse, Api, Resource
from ..common import validator
from ..models.question import QuestionModel
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

APP = Flask(__name__)


QUESTION_BLUEPRINT = Blueprint('question', __name__)
API = Api(QUESTION_BLUEPRINT, prefix='/api/v1')


class AllQuestions(Resource):
    """
    this class deals with posting questions and getting all questions
    """

    parser = reqparse.RequestParser()
    parser.add_argument('title',
                        type=str,
                        required=True,
                        help='Please enter a title.',

                        )

    parser.add_argument('description',
                        type=str,
                        required=True,
                        help='Please enter a description.',

                        )

    @classmethod
    @jwt_required
    def get(cls):
        """Handles getting a list of all questions"""
        QUESTION_LIST = QuestionModel.get_all_questions()
        if not QUESTION_LIST:
            return {'Empty': 'Sorry, but there are no questions at the moment'}, 404
        return {"message": "Success!! Here are your records", "list": QUESTION_LIST}, 200

    @classmethod
    @jwt_required
    def post(cls):
        """Handles posting a question"""
        current_user_id = get_jwt_identity()

        data = cls.parser.parse_args()

        QUESTION_LIST = QuestionModel.get_all_questions()

        exists = validator.check_if_already_exists(
            QUESTION_LIST, data['title'], data['description'])

        if exists:
            return {"message": exists}, 409

        verify_question = validator.question_verification(
            data['title'], data['description'])

        if verify_question:
            return {"message": verify_question}, 409

        model_data = QuestionModel(
            data['title'], data['description'], current_user_id)

        save_to_db = model_data.save_to_db()

        if save_to_db:
            return {'message': 'Your question has been added successfully'}, 201
        return {'message': 'Sorry. an error occured during saving'}, 409


class SpecificQuestion(Resource):
    """this class handles fetching a specific question and deleting it"""

    @classmethod
    @jwt_required
    def get(cls, questionid):
        """this handles getting the question using it's id"""

        QUESTION_LIST = QuestionModel.get_all_questions()

        check_id = validator.check_using_id(QUESTION_LIST, int(questionid))

        if check_id:
            return {"message": "Successfully retrieved question", "question": check_id}, 200
        return {'message': 'Oops, that question is missing'}, 404

    @classmethod
    def delete(cls, questionid):
        """this handles deleting the question using it's id"""

        QUESTION_LIST = QuestionModel.get_all_questions()

        check_id = validator.check_using_id(QUESTION_LIST, int(questionid))

        if not check_id:
            return {"message":
                    "Sorry, we couldn't find that question, it may have already been deleted"}, 404

        queid = int(questionid)
        delete_que = QuestionModel.delete_question(queid)

        return {"message": "Success!! The question has been deleted."}, 200

API.add_resource(AllQuestions, "/questions")
API.add_resource(SpecificQuestion, "/questions/<questionid>")


if __name__ == '__main__':
    APP.run()
