"""
#app/api/config.py
"""
import os

class Base():
    """parent clas that all other classes inherit"""
    DEBUG = False
    TESTING = False


class Development(Base):
    """config related to config environment"""
    DEBUG = True
    TESTING = True


class Test(Base):
    """config related to testing environment"""
    TESTING = True
    DEBUG = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    TESTDB_URL = os.getenv("DB_TEST_URL")


class Production(Base):
    """config related to testing environment"""
    TESTING = False


CONFIG = {
    'development': Development,
    'testing': Test,
    'production': Production
}
