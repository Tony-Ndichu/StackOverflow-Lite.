"""
#app/run.py
Provides entry point for app
"""

from .api import create_app
from flask_jwt_extended import JWTManager
from datetime import timedelta

APP = create_app('development')
APP.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
APP.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
jwt = JWTManager(APP)

if __name__ == ('__main__'):
	APP.run()

