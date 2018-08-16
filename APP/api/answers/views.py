"""
This is the code for post an answer
"""

from flask import make_response, jsonify, Flask, Blueprint, request
from flask_restful import reqparse, abort, Api, Resource
from ..common import validator
from ..models import answer
from ..models.answer import AnswerModel
from ..questions.views import QUESTION_LIST


app = Flask(__name__)


answer_blueprint = Blueprint('answer', __name__)
api = Api(answer_blueprint, prefix='/api/v1')

ANSWER_LIST = []

class Answer(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument('answer',
                        type=str,
                        required=True,
                        help='Please enter an answer.'                        
                        )

	@classmethod 
	def post(cls, questionid):

		data = cls.parser.parse_args()

        
		CheckQuestion = validator.check_using_id(QUESTION_LIST , int(questionid))

		if not CheckQuestion:
			return {'message' : 'Oops, that question is missing, you cant add answers to it' }, 404



		CheckAnswer = validator.check_for_answer(ANSWER_LIST , data['answer'])

		if CheckAnswer:
			return {"message" : "Please enter a different answer, you cannot enter the same answer twice"} , 409

		CheckQuality = validator.check_quality(data['answer'])

		if CheckQuality:
			return {"message" : CheckQuality}, 409

		id_num = 1
		for item in ANSWER_LIST:
			id_num += 1

		new_answer = AnswerModel(data['answer'])

		new_answer_dict = new_answer.make_answer_dict(id_num, questionid)

		ANSWER_LIST.append(new_answer_dict)

		return {"message" : "Success!! Your answer has been added"} , 201


api.add_resource(Answer, "/questions/<questionid>/answers")

if __name__ == '__main__':
    app.run()

       

