"""
This is the code for get all questions
"""

from flask import make_response , jsonify , Flask, Blueprint , request
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)


question_blueprint = Blueprint('question', __name__)
api = Api(question_blueprint , prefix='/api/v1')


QUESTIONS = []


class AllQuestions(Resource):
    """
    this enables getting all the questions and posting a new
    question"""
    def get(self):
        if not QUESTIONS:
            return { 'Empty' : 'Sorry, but there are no questions at the moment'}, 404
        return   QUESTIONS  , 200

api.add_resource(AllQuestions , "/questions")



if __name__ == '__main__':
    app.run()
