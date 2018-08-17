"""
#app/api/answers/views.py
This is the module that handles question operations and their methods
"""

from flask import Flask, Blueprint
from flask_restful import reqparse, Api, Resource
from ..common import validator
from ..models.question import QuestionModel


APP = Flask(__name__)


QUESTION_BLUEPRINT = Blueprint('question', __name__)
API = Api(QUESTION_BLUEPRINT, prefix='/api/v1')

QUESTION_LIST = [
    {
        "question_id": 1,
        "title": "Here",
        "description": "sdsfdffsfd"
    },
    {
        "question_id": 2,
        "title": "Here",
        "description": "sdsfdffsfd"
    }

]


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
    def get(cls):
        """Handles getting a list of all questions"""
        if not QUESTION_LIST:
            return {'Empty': 'Sorry, but there are no questions at the moment'}, 404
        return QUESTION_LIST, 200

    @classmethod
    def post(cls):
        """Handles posting a question"""
        data = cls.parser.parse_args()

        exists = validator.check_if_already_exists(
            QUESTION_LIST, data['title'], data['description'])

        if exists:
            return {"message": exists}, 409

        verify_question = validator.question_verification(
            data['title'], data['description'])

        if verify_question:
            return {"message": verify_question}, 409

        id_count = 1

        for item in QUESTION_LIST:
            id_count += 1

        new_question = QuestionModel(data['title'], data['description'])

        new_question_dict = new_question.make_dict(id_count)

        QUESTION_LIST.append(new_question_dict)

        return {'message': 'Your question has been added successfully'}, 201


class SpecificQuestion(Resource):
    """this class handles fetching a specific question and deleting it"""

    @classmethod
    def get(cls, questionid):
        """this handles getting the question using it's id"""

        check_id = validator.check_using_id(QUESTION_LIST, int(questionid))

        if check_id:
            return check_id, 200
        return {'message': 'Oops, that question is missing'}, 404

    @classmethod
    def delete(cls, questionid):
        """this handles deleting the question using it's id"""

        check_id = validator.check_using_id(QUESTION_LIST, int(questionid))

        if not check_id:
            return {"message":
                    "Sorry, we couldn't find that question, it may have already been deleted"}, 404

        QUESTION_LIST.remove(check_id)
        return {"message": "Success!! The question has been deleted successfully"}, 200

API.add_resource(AllQuestions, "/questions")
API.add_resource(SpecificQuestion, "/questions/<questionid>")


if __name__ == '__main__':
    APP.run()
