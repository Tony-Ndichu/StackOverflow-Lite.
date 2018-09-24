"""
#app/api/votes/views.py
This is the module that handles answers and their methods
"""
from datetime import datetime
from flask import Flask, Blueprint
from flask_restful import reqparse, Api, Resource
from ..common import validator
from ..models.answer import AnswerModel
from ..models.question import QuestionModel
from ..models.vote import VoteModel
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


APP = Flask(__name__)


VOTE_BLUEPRINT = Blueprint('vote', __name__)
API = Api(VOTE_BLUEPRINT, prefix='/api/v1')


class Upvote(Resource):
	"""This class deals with upvoting answers"""
	@classmethod
	@jwt_required
	def post(cls, answer_id):
		"""Handles upvotes"""
		current_user_id = get_jwt_identity()

		check_if_already_upvoted = VoteModel.check_if_upvoted(current_user_id, answer_id)

		if check_if_already_upvoted:
			remove_upvote = VoteModel.remove_upvote(current_user_id, answer_id)
			count_upvotes = VoteModel.count_upvotes(answer_id)
			return {"message" : "Success, you have undone your upvote" , "count" : count_upvotes[0] }, 200

		upvote_answer = VoteModel.upvote_answer(current_user_id, answer_id)

		if upvote_answer:
			count_upvotes = VoteModel.count_upvotes(answer_id)

			return { "message" : "Success!! You have upvoted this answer", "count" : count_upvotes[0]}, 200


class Downvote(Resource):
	"""This class deals with upvoting answers"""
	@classmethod
	@jwt_required
	def post(cls, answer_id):
		"""Handles upvotes"""
		current_user_id = get_jwt_identity()

		check_if_already_downvoted = VoteModel.check_if_downvoted(current_user_id, answer_id)

		if check_if_already_downvoted:
			remove_downvote = VoteModel.remove_downvote(current_user_id, answer_id)
			count_downvotes = VoteModel.count_downvotes(answer_id)
			return {"message" : "Success, you have undone your downvote" , "count" : count_downvotes[0] }, 200

		downvote_answer = VoteModel.downvote_answer(current_user_id, answer_id)

		if downvote_answer:
			count_downvotes = VoteModel.count_downvotes(answer_id)

			return { "message" : "Success!! You have downvoted this answer", "count" : count_downvotes[0]}, 200

API.add_resource(
    Upvote, "/answers/<answer_id>/upvote")

API.add_resource(
    Downvote, "/answers/<answer_id>/downvote")