'''
___init__.py
main config  file
'''

from flask import Flask
from .config import CONFIG
from .questions.views import question_blueprint
from .answers.views import answer_blueprint


def create_app(config):
    ''' function that receives configaration and creates the app'''
    app = Flask(__name__)
    app.config.from_object(CONFIG[config])
    app.url_map.strict_slashes = False

    app.register_blueprint(question_blueprint)
    app.register_blueprint(answer_blueprint)
    return app
