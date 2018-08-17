"""
#app/api/__init__.py
Handles create_app method and blueprint registration
"""

from flask import Flask
from .config import CONFIG
from .questions.views import QUESTION_BLUEPRINT
from .answers.views import ANSWER_BLUEPRINT


def create_app(config):
    """Receives the necessary configurationa and passes to create_app"""
    app = Flask(__name__)
    app.config.from_object(CONFIG[config])
    app.url_map.strict_slashes = False

    app.register_blueprint(QUESTION_BLUEPRINT)
    app.register_blueprint(ANSWER_BLUEPRINT)
    return app
