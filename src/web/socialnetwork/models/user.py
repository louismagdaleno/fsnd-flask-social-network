from datetime import datetime

from flask_dance.consumer.backend.sqla import OAuthConsumerMixin
from flask_login import UserMixin
from socialnetwork import login_manager
from werkzeug.security import generate_password_hash, check_password_hash

from . import db


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """Model to define User"""
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    profile_image = db.Column(db.String(250), nullable=False,
                              default="{{ url_for('static', filename='profile_pics/default_profile.png') }}")
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(250), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy=True)
    time_inserted = db.Column(db.DateTime(), default=datetime.utcnow)
    time_updated = db.Column(db.DateTime(), default=datetime.utcnow)

    def __init__(self, email, name, username, password='1234'):
        self.email = email
        self.name = name
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""

        return {
            'email': self.id,
            'profile_image': self.profile_image,
            'email': self.email,
            'username': self.username,
            'password_hash': self.password_hash}

    def __repr__(self):
        return f"Username {self.username}"


class UserAuth(db.Model, OAuthConsumerMixin):
    """Model to define UserAuth to store oAuth tokens"""
    __tablename__ = 'userauth'

    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)
