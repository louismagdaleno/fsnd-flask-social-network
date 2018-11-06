#!/usr/bin/python3
import config  # noqa:E401
from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager
import os


app = Flask(__name__)

# Environment Configuration
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)
app.config.from_object('config.settings.' + os.environ['ENV'])

# User Session Management
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'users.login'

# Database
from .models import db, user, post # noqa:E401
from .models.user import User # noqa:E401
from .models.post import Post # noqa:E401

db.create_all()
db.session.commit()


# Blueprints
from socialnetwork.routes.userauth import userauth # noqa:E401
from socialnetwork.routes.post import post # noqa:E401
from socialnetwork.routes.main import main # noqa:E401
from socialnetwork.routes.errorhandlers import errorhandlers # noqa:E401
from socialnetwork.routes.account import users # noqa:E401

app.register_blueprint(userauth)
app.register_blueprint(post)
app.register_blueprint(main)
app.register_blueprint(errorhandlers)
app.register_blueprint(users)
