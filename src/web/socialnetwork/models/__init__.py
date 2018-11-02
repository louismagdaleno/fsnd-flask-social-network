from socialnetwork import app
from flask_sqlalchemy import SQLAlchemy

__all__ = ['db']

db = SQLAlchemy(app)
