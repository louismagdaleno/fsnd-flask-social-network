from datetime import datetime
from . import db


class Post(db.Model):
    """Model to define Item"""
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(140), nullable=False)
    text = db.Column(db.Text, nullable=False)
    time_inserted = db.Column(db.DateTime(), default=datetime.utcnow)
    time_updated = db.Column(db.DateTime(), default=datetime.utcnow)

    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""

        return {
            'post_id': self.id,
            'title': self.title,
            'date': self.date,
            'author name': self.author.name,
            'user_id': self.user_id,
            'text': self.text
        }

    def __repr__(self):
        return f"Post Id: {self.id} " \
               f"--- Date: {self.date} " \
               f"--- Title: {self.title}"
