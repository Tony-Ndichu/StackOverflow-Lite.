"""
#app/run.py
Provides entry point for app
"""

from .api import create_app
from flask_jwt_extended import JWTManager

APP = create_app('development')
APP.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(APP)

if __name__ == ('__main__'):
	APP.run()

