"""
Provides entry point for app
"""

import os

from .api import create_app
try:
    config = os.environ['CONFIG_ENVIRONMENT']
    app = create_app(config)
except KeyError:
    app = create_app('development')

if __name__ == ('__main__'):
    app.run()