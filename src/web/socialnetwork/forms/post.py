from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import  DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField("What's on your mind?", validators=[DataRequired()])
    submit = SubmitField('Post')