"""
#app/api/config.py
"""


class BaseConfig():
    """parent clas that all other classes inherit"""
    DEBUG = False
    TESTING = False


class Development(BaseConfig):
    """config related to config environment"""
    DEBUG = True
    TESTING = True


class Test(BaseConfig):
    """config related to testing environment"""
    TESTING = True
    DEBUG = True


class Production(BaseConfig):
    """config related to testing environment"""
    TESTING = False


CONFIG = {
    'development': Development,
    'testing': Test,
    'production': Production
}
