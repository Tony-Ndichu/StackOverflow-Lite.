"""
#app/api/__init__.py
Handles create_app method and blueprint registration
"""

from flask import Flask
from .config import CONFIG
from .questions.views import QUESTION_BLUEPRINT
from .answers.views import ANSWER_BLUEPRINT
from .users.views import USER_BLUEPRINT
from .manage import create_tables 
from flask_jwt_extended import JWTManager
from datetime import timedelta





def create_app(config):
	"""This is the application factory"""
	app = Flask(__name__)
	app.config.from_object(CONFIG[config])
	app.url_map.strict_slashes = False
	app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
	jwt = JWTManager(app)
	create_tables()
	app.register_blueprint(QUESTION_BLUEPRINT)
	app.register_blueprint(ANSWER_BLUEPRINT)
	app.register_blueprint(USER_BLUEPRINT)
	return app

