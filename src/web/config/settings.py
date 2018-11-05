import os


basedir = os.path.abspath(os.path.dirname(__file__))

class Default:
    """Default Configuration that all environments will default to"""
    APP_NAME = "socialnetwork"
    TESTING = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "hcculdcpxaauasotixrjdvjpre"
    ENV = os.environ.get("ENV")
    SERVER = os.environ.get("SERVER") or 'localhost'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///socialnetworkdb.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    GOOGLE_OAUTH_CLIENT_ID =\
        '119051372590-r419hgkam5hcg7mbf2lv6i1hi4t7ct3n' \
        '.apps.googleusercontent.com'
    GOOGLE_OAUTH_CLIENT_SECRET = 'fyGxtAaGrMcHo6Yjg-StvoLu'
    GOOGLE_OAUTH_CLIENT_SCOPE = [
        "https://www.googleapis.com/auth/plus.me",
        "https://www.googleapis.com/auth/userinfo.email",
    ]
    GOOGLE_OAUTH_CLIENT_USERINFO_URI = "/oauth2/v2/userinfo"
