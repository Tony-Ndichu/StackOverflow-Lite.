"""
This is the code for get all questions
"""

from flask import make_response, jsonify, Flask, Blueprint, request
from flask_restful import reqparse, abort, Api, Resource
from ..common import validator
from ..models import question
from ..models.question import Question


app = Flask(__name__)


question_blueprint = Blueprint('question', __name__)
api = Api(question_blueprint, prefix='/api/v1')


QUESTION_LIST = []


class AllQuestions(Resource):
    """
    this enables getting all the questions and posting a new
    question"""

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
    def get(self):
        if not QUESTION_LIST:
            return {'Empty': 'Sorry, but there are no questions at the moment'}, 404
        return QUESTION_LIST, 200

    @classmethod
    def post(cls):
        data = cls.parser.parse_args()

        if validator.check_if_already_exists(QUESTION_LIST, data['title'], data['description']):
            return {"message": "Sorry, this question has already been posted"}, 409

        Verify_Question = validator.question_verification(data['title'] , data['description'])

        if Verify_Question:
            return {"message" : Verify_Question }, 409

        id_count = 1

        for item in QUESTION_LIST:
            id_count += 1

        new_question = Question(data['title'], data['description'])

        new_question_dict = new_question.make_dict(id_count)

        QUESTION_LIST.append(new_question_dict)

        return {'message': 'Your question has been added successfully'} , 201


api.add_resource(AllQuestions, "/questions")


if __name__ == '__main__':
    app.run()
