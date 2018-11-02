from enum import Enum
import os


basedir = os.path.abspath(os.path.dirname(__file__))


class ValidEnvironments(Enum):
    """Enum to control valid environment config inputs"""
    Development = 'Development',
    Test = 'Test',
    Production = 'Production'


class Default:
    """Default Configuration that all environments will default to"""
    APP_NAME = "itemcatalog"
    TESTING = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "hcculdcpxaauasotixrjdvjpre"
    ENV = os.environ.get("ENV") or ValidEnvironments.Development
    SERVER = os.environ.get("SERVER") or 'localhost'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///lm-ca-dev-001.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    GOOGLE_OAUTH_CLIENT_ID = '119051372590-r419hgkam5hcg7mbf2lv6i1hi4t7ct3n.apps.googleusercontent.com'
    GOOGLE_OAUTH_CLIENT_SECRET = 'fyGxtAaGrMcHo6Yjg-StvoLu'
    GOOGLE_OAUTH_CLIENT_SCOPE = [
        "https://www.googleapis.com/auth/plus.me",
        "https://www.googleapis.com/auth/userinfo.email",
    ]
    GOOGLE_OAUTH_CLIENT_USERINFO_URI = "/oauth2/v2/userinfo"


class Development(Default):
    """Development environment"""
    DEBUG = False
    TESTING = True
    ENV = os.environ.get("ENV") or ValidEnvironments.Development
    SERVER = os.environ.get("SERVER") or "lm-ca-dev-001"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///lm-ca-dev-001.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class Test(Default):
    """Continuous Integration (CI) / User Acceptance"""
    DEBUG = False
    TESTING = True
    ENV = os.environ.get("ENV") or ValidEnvironments.Test
    SERVER = os.environ.get("SERVER") or "lm-ca-dev-001"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///lm-ca-test-001.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class Production(Default):
    """Production"""
    DEBUG = False
    TESTING = False
    ENV = os.environ.get("ENV") or ValidEnvironments.Production
    SERVER = os.environ.get("SERVER") or "lm-ca-prd-001"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///lm-ca-prd-001.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
