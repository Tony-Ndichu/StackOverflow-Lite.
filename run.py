"""
#app/run.py
Provides entry point for app
"""

from .api import create_app

APP = create_app('development')

if __name__ == ('__main__'):
    APP.run()
