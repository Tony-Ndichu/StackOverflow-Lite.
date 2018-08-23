"""
#app/run.py
Provides entry point for app
"""
import os
from .api import create_app

APP = create_app(config=os.getenv("CONFIG"))

if __name__ == ('__main__'):
	APP.run()



