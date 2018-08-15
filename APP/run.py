"""
Provides entry point for app
"""

import os

from .api import create_app

app = create_app('development')

if __name__ == ('__main__'):
    app.run()